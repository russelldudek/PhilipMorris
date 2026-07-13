import { chromium } from 'playwright';
import AxeBuilder from '@axe-core/playwright';
import fs from 'node:fs/promises';

const baseURL = process.env.QA_BASE_URL || 'http://127.0.0.1:4173';
const out = process.env.QA_OUT || 'qa-output';
await fs.mkdir(out, { recursive: true });

const viewports = [
  ['desktop', 1440, 900],
  ['laptop', 1280, 800],
  ['tablet', 768, 1024],
  ['mobile', 390, 844],
];
const browser = await chromium.launch({ headless: true });
const results = [];

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

for (const [name, width, height] of viewports) {
  const context = await browser.newContext({ viewport: { width, height } });
  const page = await context.newPage();
  const errors = [];
  page.on('console', message => {
    if (message.type() === 'error' || message.type() === 'warning') errors.push(`${message.type()}: ${message.text()}`);
  });
  page.on('pageerror', error => errors.push(`pageerror: ${error.message}`));
  await page.goto(`${baseURL}/index.html`, { waitUntil: 'networkidle' });
  assert((await page.title()).includes('PMI'), `${name}: wrong page identity`);
  assert(await page.locator('#hero-title').isVisible(), `${name}: hero not visible`);
  assert(await page.locator('.rf-brand img').evaluate(img => img.complete && img.naturalWidth > 0), `${name}: PMI wordmark missing`);
  if (width >= 1200) {
    const logoBox = await page.locator('.rf-brand img').boundingBox();
    assert(logoBox && logoBox.width >= 240, `${name}: PMI wordmark too small (${logoBox?.width})`);
  }
  const overflow = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
  assert(overflow <= 1, `${name}: horizontal overflow ${overflow}px`);
  const laneOpacity = await page.locator('.gene-lane').first().evaluate(el => getComputedStyle(el).opacity);
  assert(Number(laneOpacity) >= .99, `${name}: inactive lanes are visually suppressed`);
  const trackHeight = await page.locator('.gene-track').first().evaluate(el => parseFloat(getComputedStyle(el).height));
  assert(trackHeight >= 4, `${name}: sequencer track lacks visual weight`);
  const outcomeColor = await page.locator('#scan-outcome').evaluate(el => getComputedStyle(el).color);
  assert(outcomeColor !== 'rgba(0, 0, 0, 0)', `${name}: sequencer outcome invisible`);
  await page.screenshot({ path: `${out}/${name}-hero.png`, fullPage: false });
  await page.screenshot({ path: `${out}/${name}-full.png`, fullPage: true });

  if (name === 'desktop') {
    const initial = await page.locator('#scan-status').textContent();
    await page.locator('[data-genome-control="mutation"]').click();
    assert((await page.locator('#genome-verdict').textContent()) === 'REPAIR', 'desktop: mutation interaction did not resolve to REPAIR');
    assert((await page.locator('#scan-status').textContent()) !== initial, 'desktop: hero status did not change');
    await page.locator('[data-genome-control="mutation"]').focus();
    await page.keyboard.press('ArrowRight');
    assert((await page.locator('#genome-verdict').textContent()) === 'EVOLVE', 'desktop: keyboard transition did not resolve to EVOLVE');
    const axe = await new AxeBuilder({ page }).withTags(['wcag2a', 'wcag2aa']).analyze();
    const serious = axe.violations.filter(v => ['serious', 'critical'].includes(v.impact));
    assert(serious.length === 0, `desktop: serious accessibility violations: ${serious.map(v => v.id).join(', ')}`);
  }
  if (name === 'mobile') {
    await page.locator('.rf-menu').click();
    assert(await page.locator('#rf-links').evaluate(el => el.classList.contains('is-open')), 'mobile: navigation did not open');
  }
  assert(errors.length === 0, `${name}: console errors: ${errors.join(' | ')}`);
  results.push({ name, width, height, overflow, errors });
  await context.close();
}

const reduced = await browser.newContext({ viewport: { width: 1280, height: 800 }, reducedMotion: 'reduce' });
const reducedPage = await reduced.newPage();
await reducedPage.goto(`${baseURL}/index.html`, { waitUntil: 'networkidle' });
const pulseDisplay = await reducedPage.locator('.gene-track .pulse').first().evaluate(el => getComputedStyle(el).display);
assert(pulseDisplay === 'none', `reduced motion: animated pulse remains ${pulseDisplay}`);
await reducedPage.screenshot({ path: `${out}/reduced-motion.png`, fullPage: false });
await reduced.close();

for (const route of ['resume.html', 'cover-letter.html']) {
  const context = await browser.newContext({ viewport: { width: 1280, height: 900 } });
  const page = await context.newPage();
  await page.goto(`${baseURL}/${route}`, { waitUntil: 'networkidle' });
  const text = await page.locator('body').innerText();
  for (const value of ['412.287.8640', 'russelldudek@gmail.com', 'linkedin.com/in/russelldudek', 'github.com/russelldudek/PhilipMorris']) {
    assert(text.includes(value), `${route}: missing ${value}`);
  }
  if (route === 'resume.html') {
    assert((await page.locator('.resume-head .contact').count()) === 2, 'resume: both page headers must carry contact information');
    assert(await page.locator('a[href="cover-letter.html"]').isVisible(), 'resume: View Cover Letter missing');
  } else {
    assert(await page.locator('.letter-body a[href="https://github.com/russelldudek/PhilipMorris"]').isVisible(), 'cover letter: repository link missing from body');
    assert((await page.locator('.letter-body').innerText()).includes('The repository contains the candidate vision'), 'cover letter: repository is not explained');
    assert(await page.locator('a[href="resume.html"]').isVisible(), 'cover letter: View Resume missing');
  }
  const overflow = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
  assert(overflow <= 1, `${route}: horizontal overflow ${overflow}px`);
  await page.screenshot({ path: `${out}/${route.replace('.html','')}.png`, fullPage: true });
  await context.close();
}

await fs.writeFile(`${out}/results.json`, JSON.stringify(results, null, 2));
await browser.close();
console.log('Rendered visual QA passed.');
