# Philip Morris International Brand Intelligence

## Brand fidelity decision

This campaign uses the full Philip Morris International crest-and-wordmark lockup as the primary employer-identification layer and keeps the candidate-created Process Genome mark secondary as the role-specific operating artifact. The site states immediately that it is independent candidate work by Russell Dudek and does not imply PMI authorship, sponsorship, or endorsement.

## Sources reviewed

- PMI corporate site: https://www.pmi.com/
- PMI careers overview: https://www.pmi.com/careers/overview
- PMI corporate identity reference: https://www.pmi.com/resources/images/default-source/default-album/pmi-logoa4f115bd6c7468f696e2ff0400458fff.svg?sfvrsn=37857db4_0
- User-selected crest-and-wordmark transport asset: https://seekvectorlogo.net/wp-content/uploads/2019/10/philip-morris-international-pmi-vector-logo.png
- PMI Value Report hub: https://www.pmi.com/sustainability/reporting-on-sustainability

The user-selected image presents the complete PMI crest and horizontal wordmark more clearly at the campaign header scale than the previously used corporate SVG rendering. The build workflow downloads that exact supplied asset, removes only its empty white canvas, converts the white background to transparency, preserves the crest and wordmark proportions, and creates a higher-resolution derivative for PDF stamping. The mark itself is not redrawn, stretched, animated, or combined with a candidate logo.

## Committed brand asset package

- `assets/brand/pmi-wordmark-source.png` - original user-selected transport image
- `assets/brand/pmi-wordmark.png` - tightly trimmed transparent browser asset generated from the supplied image
- `assets/brand/pmi-wordmark-hires.png` - two-times transparent PDF-stamping derivative
- `assets/brand/README.md` - asset provenance and use boundary
- `brand-tokens.css` - documented brand tokens
- `brand-overrides.css` and `visual-qa.css` - company-recognition, contrast, responsive, and document-continuity layers

## Color tokens

| Token | Value | Classification | Evidence / use |
|---|---:|---|---|
| `--brand-primary` | `#0074C2` | source-sampled | Dominant blue measured from PMI identity assets |
| `--brand-primary-deep` | `#004A80` | source-derived | Accessible dark expression of PMI blue for large fields |
| `--brand-primary-soft` | `#DCEEFA` | source-derived | Light editorial background derived from PMI blue |
| `--brand-sky` | `#52A7D8` | source-derived | Secondary data/variation state |
| `--brand-red` | `#B43403` | source-sampled | Warm red used as a restrained candidate-campaign detail |
| `--brand-ink` | `#13293D` | source-derived | Editorial navy for text and evidence systems |
| `--campaign-accent` | `#6D8291` | candidate-original | Subordinate steel accent for the Process Genome evidence state |

PMI blue, white, and deep editorial blue dominate the recognition layer. Candidate-created state colors remain subordinate and are used only to teach the Process Genome classification model.

## Typography decision

An official PMI web property historically declared Lato across its public interface. Lato is open source and available in the rendering environment, so the campaign uses `Lato, "Helvetica Neue", Arial, sans-serif` without copying or distributing proprietary font binaries. The implementation mirrors PMI's public typographic behavior through clean sans-serif forms, broad editorial headlines, disciplined weights, and substantial white space.

## Visual grammar

- white, evidence-led editorial canvas;
- strong PMI-blue rules and large data typography;
- restrained warm-red detail;
- crisp square or low-radius information framing rather than generic soft SaaS cards;
- science, transformation, and decision-system cues;
- high-contrast sequencer states that remain readable while inactive;
- calm measured motion rather than decorative spectacle.

## Visible-use decision

- Website header and first viewport: complete PMI crest-and-wordmark lockup at a legible scale plus an immediate independent-candidate qualifier.
- Process Genome: PMI identity names the target employer; the Process Genome mark identifies Russell's original operating artifact.
- Resume, cover letter, interview brief, 120-day plan, and objection analysis: restrained PMI wordmark, PMI-blue rule, Lato typography, and candidate-work label.
- Generated PDFs: high-resolution wordmark in the footer brand zone and PMI-blue page rule.

## Usage boundary

The PMI mark is used solely to identify the target employer in an independent candidate campaign. It is not animated, recolored, distorted, merged into a candidate logo, or placed in a fake corporate navigation or letterhead system. The campaign does not imply endorsement and does not republish tobacco-product advertising or proprietary PMI interfaces.