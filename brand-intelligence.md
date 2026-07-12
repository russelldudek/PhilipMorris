# Philip Morris International Brand Intelligence

## Brand fidelity decision

This campaign uses Philip Morris International's official horizontal wordmark as the primary employer-identification layer and keeps the candidate-created Process Genome mark secondary as the role-specific operating artifact. The site states immediately that it is independent candidate work by Russell Dudek and does not imply PMI authorship, sponsorship, or endorsement.

## Official sources reviewed

- PMI corporate site: https://www.pmi.com/
- PMI careers overview: https://www.pmi.com/careers/overview
- Official corporate wordmark served by PMI: https://www.pmi.com/resources/images/default-source/default-album/pmi-logoa4f115bd6c7468f696e2ff0400458fff.svg?sfvrsn=37857db4_0
- Current official PMI emblem: https://www.pmi.com/content/dam/pmicom/global/images/default-album/pmi-emblem.png
- PMI Value Report hub: https://www.pmi.com/sustainability/reporting-on-sustainability

The official wordmark was validated against the PMI corporate source. Because the build runtime could not retrieve the PMI CDN asset directly, a visually identical public mirror was used only for byte transport, then stored locally at `assets/brand/pmi-wordmark.png`. The mark remains unmodified in proportions, colors, and composition.

## Committed brand asset package

- `assets/brand/pmi-wordmark.png` - official PMI horizontal wordmark, locally served
- `assets/brand/README.md` - asset provenance and use boundary
- `brand-tokens.css` - documented brand tokens
- `brand-overrides.css` - company-recognition and document-continuity layer

## Color tokens

| Token | Value | Classification | Evidence / use |
|---|---:|---|---|
| `--brand-primary` | `#0074C2` | source-sampled | Dominant blue measured from the official PMI wordmark |
| `--brand-primary-deep` | `#004A80` | source-derived | Accessible dark expression of PMI blue for large fields |
| `--brand-primary-soft` | `#DCEEFA` | source-derived | Light editorial background derived from PMI blue |
| `--brand-sky` | `#52A7D8` | source-derived | Secondary data/variation state |
| `--brand-red` | `#B43403` | source-sampled | Warm red measured from the wordmark underline detail |
| `--brand-ink` | `#13293D` | source-derived | Editorial navy for text and evidence systems |
| `--campaign-accent` | `#6D8291` | candidate-original | Subordinate steel accent for the Process Genome evidence state |

PMI blue, white, and deep editorial blue dominate the recognition layer. Candidate-created state colors remain subordinate and are used only to teach the Process Genome classification model.

## Typography decision

An official PMI web property historically declared Lato across its public interface. Lato is open source and is available in the rendering environment, so the campaign uses `Lato, "Helvetica Neue", Arial, sans-serif` without copying or distributing proprietary font binaries. The implementation mirrors PMI's public typographic behavior through clean sans-serif forms, broad editorial headlines, disciplined weights, and substantial white space.

## Visual grammar

- white, evidence-led editorial canvas;
- strong PMI-blue rules and large data typography;
- restrained warm-red detail taken from the wordmark;
- crisp square or low-radius information framing rather than generic soft SaaS cards;
- science, transformation, and decision-system cues;
- calm measured motion rather than decorative spectacle.

## Visible-use decision

- Website header and first viewport: official PMI wordmark plus `Candidate vision by Russell Dudek` distinction.
- Process Genome: PMI wordmark identifies the employer; the Process Genome mark identifies Russell's original operating artifact.
- Resume, cover letter, interview brief, 120-day plan, and objection analysis: restrained PMI wordmark, PMI-blue rule, Lato typography, and candidate-work label.
- Generated PDFs: official wordmark in the footer brand zone and PMI-blue page rule.

## Usage boundary

The PMI mark is used solely to identify the target employer in an independent candidate campaign. It is not animated, recolored, distorted, merged into a candidate logo, or placed in a fake corporate navigation or letterhead system. The campaign does not imply endorsement and does not republish tobacco-product advertising or proprietary PMI interfaces.
