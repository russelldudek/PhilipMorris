(() => {
  const isArtifact = document.body.classList.contains('artifact-page');
  document.querySelectorAll('.rf-brand').forEach(brand => {
    const image = brand.querySelector('img');
    const label = brand.querySelector('span');
    const qualifier = brand.querySelector('small');
    if (image) {
      image.src = 'assets/brand/pmi-wordmark.png';
      image.alt = 'Philip Morris International';
    }
    if (label) label.textContent = isArtifact
      ? 'Process Genome · candidate operating artifact'
      : 'Candidate vision for Business Process Excellence';
    if (qualifier) qualifier.textContent = 'by Russell Dudek · independent candidate work';
  });

  const docNav = document.querySelector('.doc-nav');
  if (docNav && !docNav.querySelector('.doc-company-lockup')) {
    const lockup = document.createElement('span');
    lockup.className = 'doc-company-lockup';
    const logo = document.createElement('img');
    logo.src = 'assets/brand/pmi-wordmark.png';
    logo.alt = 'Philip Morris International';
    const note = document.createElement('small');
    note.textContent = 'Candidate application by Russell Dudek · independent work';
    lockup.append(logo, note);
    docNav.prepend(lockup);
    docNav.classList.add('has-dom-lockup');
  }

  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const menu = document.querySelector('.rf-menu');
  const links = document.querySelector('#rf-links');
  if (menu && links) {
    menu.addEventListener('click', () => {
      const open = menu.getAttribute('aria-expanded') === 'true';
      menu.setAttribute('aria-expanded', String(!open));
      links.classList.toggle('is-open', !open);
    });
    links.addEventListener('click', event => {
      if (event.target.closest('a')) {
        menu.setAttribute('aria-expanded', 'false');
        links.classList.remove('is-open');
      }
    });
  }

  const genomeData = {
    core: {
      kicker: 'The stable enterprise truth',
      heading: 'Define the invariant process contract.',
      decision: 'What must remain common for the process to create value and control risk?',
      failure: 'Local optimization that breaks the end-to-end outcome.',
      proof: 'Outcome ownership, decision rights, controls, interfaces, and common measures.',
      verdict: 'PROTECT',
      signal: 'Different market approval path',
      status: 'Scanning process core',
      outcome: 'Keep the invariant process contract intact.'
    },
    variant: {
      kicker: 'Legitimate local expression',
      heading: 'Bound variation without erasing reality.',
      decision: 'Is this difference required by regulation, market structure, product, channel, or a temporary system constraint?',
      failure: 'False standardization that drives work into shadow processes.',
      proof: 'Documented rationale, accountable owner, common outcome measure, and a review date.',
      verdict: 'BOUND',
      signal: 'Required regulatory exception',
      status: 'Testing legitimate variation',
      outcome: 'Permit the difference with ownership and review.'
    },
    mutation: {
      kicker: 'Process debt made visible',
      heading: 'Repair deviation that creates friction without value.',
      decision: 'Which workaround, duplicate approval, hidden queue, rework loop, or zombie exception should stop?',
      failure: 'Normalizing inherited friction until it becomes invisible and expensive.',
      proof: 'Root cause, risk logic, economic burden, owner, and observed change after repair.',
      verdict: 'REPAIR',
      signal: 'Duplicate approval and side spreadsheet',
      status: 'Locating process mutation',
      outcome: 'Remove unmanaged debt and restore flow.'
    },
    evidence: {
      kicker: 'The basis for evolution',
      heading: 'Change the standard only when the evidence earns it.',
      decision: 'Did the intervention improve outcome, flow, economics, risk, adoption, and learning speed?',
      failure: 'Scaling novelty, local heroics, or stakeholder preference without sustained proof.',
      proof: 'Baseline, trial result, control confidence, retained adoption, and benefit validation.',
      verdict: 'EVOLVE',
      signal: 'Pilot outcome exceeds the current standard',
      status: 'Reading evidence signal',
      outcome: 'Update the standard and preserve the learning.'
    }
  };

  const controls = [...document.querySelectorAll('[data-genome-control]')];
  const heroLanes = [...document.querySelectorAll('.gene-lane')];
  let activeKey = 'core';
  let autoTimer;

  function setText(id, value) {
    const el = document.getElementById(id);
    if (el) el.textContent = value;
  }

  function activateGenome(key, { focus = false } = {}) {
    if (!genomeData[key]) return;
    activeKey = key;
    const item = genomeData[key];
    controls.forEach(control => {
      const active = control.dataset.genomeControl === key;
      control.setAttribute('aria-pressed', String(active));
      if (control.getAttribute('role') === 'tab') {
        control.setAttribute('aria-selected', String(active));
        control.tabIndex = active ? 0 : -1;
      }
      control.classList.toggle('is-active', active);
      if (focus && active) control.focus();
    });
    heroLanes.forEach(lane => lane.classList.toggle('is-active', lane.dataset.gene === key));
    const visual = document.querySelector('[data-genome-visual]');
    if (visual) visual.dataset.genomeVisual = key;
    setText('genome-kicker', item.kicker);
    setText('genome-heading', item.heading);
    setText('genome-decision', item.decision);
    setText('genome-failure', item.failure);
    setText('genome-proof', item.proof);
    setText('genome-verdict', item.verdict);
    setText('artifact-verdict', item.verdict);
    setText('artifact-signal', item.signal);
    setText('scan-status', item.status);
    setText('scan-outcome', item.outcome);
    document.documentElement.style.setProperty('--active-gene', `var(--gene-${key})`);
  }

  controls.forEach((control, index) => {
    control.addEventListener('click', () => {
      activateGenome(control.dataset.genomeControl);
      stopAuto();
    });
    control.addEventListener('keydown', event => {
      if (!['ArrowRight', 'ArrowDown', 'ArrowLeft', 'ArrowUp', 'Home', 'End'].includes(event.key)) return;
      event.preventDefault();
      let next = index;
      if (event.key === 'ArrowRight' || event.key === 'ArrowDown') next = (index + 1) % controls.length;
      if (event.key === 'ArrowLeft' || event.key === 'ArrowUp') next = (index - 1 + controls.length) % controls.length;
      if (event.key === 'Home') next = 0;
      if (event.key === 'End') next = controls.length - 1;
      activateGenome(controls[next].dataset.genomeControl, { focus: true });
      stopAuto();
    });
  });

  function startAuto() {
    stopAuto();
    if (reduceMotion.matches || !heroLanes.length) return;
    const keys = Object.keys(genomeData);
    autoTimer = window.setInterval(() => {
      const next = keys[(keys.indexOf(activeKey) + 1) % keys.length];
      activateGenome(next);
    }, 3600);
  }
  function stopAuto() {
    if (autoTimer) window.clearInterval(autoTimer);
    autoTimer = undefined;
  }
  reduceMotion.addEventListener?.('change', event => event.matches ? stopAuto() : startAuto());
  activateGenome('core');
  startAuto();

  const revealTargets = [...document.querySelectorAll('.rf-section-head, .metric-ribbon, .tension-axis article, .decision-river li, .evidence-trail article, .sequence-run article')];
  if (!reduceMotion.matches && 'IntersectionObserver' in window) {
    revealTargets.forEach(el => el.classList.add('rf-reveal'));
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.14 });
    revealTargets.forEach(el => observer.observe(el));
  }
})();
