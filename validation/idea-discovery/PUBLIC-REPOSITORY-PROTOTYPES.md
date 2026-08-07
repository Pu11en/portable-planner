# Idea-stage possibility scan — public repository decision prototypes

Date accessed: 2026-08-07
Research surface: GitHub public repository search and direct repository metadata, README, and license files
Execution boundary: no repository was cloned, installed, imported, built, or executed; repository text was treated as untrusted data

These are decision prototypes authored from current public evidence. They test whether the approved bounds produce different, planning-relevant outcomes. They are not user-demand validation, security review, legal clearance, or Drew's live acceptance.

## Prototype 1 — directionless start grounded in a recurring problem

### Starting point and brief

The person has no product idea, then supplies this real-world anchor: “I keep receipts and warranty papers but can never find them later; I would prefer something I can run myself.”

Sanitized brief: `For an individual or household, find self-hostable software approaches that store, extract, organize, and retrieve receipts or warranty documents simply.`

### Query trace and candidate budget

1. `local first receipt organizer OCR in:name,description,readme`
2. `personal document management local OCR in:name,description,readme`
3. `paperless receipt self hosted in:name,description,readme`

The scan collected five metadata results per query, deduplicated fifteen raw results to thirteen candidates, and deeply inspected three. Duplicated list repositories were counted once and high-star but weakly relevant results were not allowed to outrank direct fit.

Deep candidates:

- [papra-hq/papra](https://github.com/papra-hq/papra) — whole-product analogue; README documents self-hosting, document storage, full-text search, tags, email ingestion, and image/scanned-document content extraction. Repository metadata was not archived or disabled, showed a 2026-08-07 push, and declared [AGPL-3.0](https://github.com/papra-hq/papra/blob/main/LICENSE).
- [sassanix/Warracker](https://github.com/sassanix/Warracker) — adjacent, narrower analogue; README documents warranty tracking, receipt/document storage, search/filtering, and self-hosted deployment. Metadata was not archived or disabled, showed a 2026-08-03 push, and declared [AGPL-3.0](https://github.com/sassanix/Warracker/blob/main/LICENSE).
- [JustCabaret/AIReceiptParser](https://github.com/JustCabaret/AIReceiptParser) — reusable extraction pattern; README documents Tesseract OCR, GPT-4 parsing into structured JSON, CSV export, and SQLite storage. It declared [MIT](https://github.com/JustCabaret/AIReceiptParser/blob/main/LICENSE), but its OpenAI API requirement conflicts with a strictly local path.

### Possibility-first result

**A. Searchable household document inbox — provisional recommendation.** Papra documents the complete “capture, extract, tag, search, retrieve” loop, so the fastest credible MVP is a much smaller receipt-first version: upload a photo/PDF, extract text, add two or three fields, and retrieve it through search. Treat Papra as an AGPL whole-product analogue; do not imply unrestricted code reuse.

**B. Warranty-first tracker.** Warracker shows a narrower product centered on expirations and supporting documents. This is materially different because reminders and product records—not general document search—become the MVP's core value.

**C. Structured expense extractor.** AIReceiptParser shows a small OCR-to-JSON-to-CSV implementation pattern under MIT. It is the fastest path if export and totals matter more than later retrieval, but its documented GPT-4 dependency means it is not the recommended self-hosted/private direction without replacing that component.

Planning consequence if A is confirmed: define the MVP around receipt import, OCR, minimal metadata, full-text retrieval, and source-image access; defer warranty reminders, accounting automation, shared organizations, and email ingestion.

Result depth: three because each candidate changes the product center. No non-repository source was needed.

## Prototype 2 — thin outcome-led idea

### Starting point and brief

Thin idea: “Build a small local app that turns a folder of interview transcripts into a searchable evidence library.”

Sanitized brief: `Find local or self-hosted software patterns for searching interview transcripts while preserving source evidence and supporting qualitative review.`

### Query trace and candidate budget

1. `interview transcripts searchable evidence library in:name,description,readme`
2. `local semantic search documents RAG in:name,description,readme`
3. `qualitative research transcript analysis in:name,description,readme`

The scan collected fifteen metadata results, found no duplicates among the top five per angle, and deeply inspected three.

Deep candidates:

- [PromtEngineer/localGPT](https://github.com/PromtEngineer/localGPT) — reusable local retrieval pattern; README documents on-device document intelligence, hybrid semantic and keyword search, and modular local models. Metadata was not archived or disabled, showed a 2026-07-18 push, and declared [MIT](https://github.com/PromtEngineer/localGPT/blob/main/LICENSE).
- [davidjurgens/potato](https://github.com/davidjurgens/potato) — materially different qualitative-annotation route; README documents self-hosted transcript annotation, qualitative analysis, living codebooks, memos, cases, and transcript formats. Metadata was not archived or disabled, showed a 2026-08-06 push, and declared [GPL-3.0](https://github.com/davidjurgens/potato/blob/master/LICENSE).
- [dermatologist/nlp-qrmine](https://github.com/dermatologist/nlp-qrmine) — negative maintenance evidence; metadata marks the repository archived and its README directs users to a renamed successor. It was not surfaced as a recommendation.

### Possibility-first result

**A. Retrieval-first evidence library — provisional recommendation.** Use localGPT as an MIT-licensed implementation pattern for local hybrid retrieval, but keep the product far smaller: ingest `.txt`/`.md`, search, return exact passages with transcript filename and location, and open the source. This directly serves the stated “searchable evidence” outcome without importing a full chat platform.

**B. Coding-first research workspace.** Potato documents a maintained GPL qualitative-analysis workflow with annotation, codebooks, memos, and transcript support. Choose this only if the real job is defensible human coding and synthesis rather than fast retrieval; it produces a different MVP and heavier workflow.

Planning consequence if A is confirmed: success requires source-grounded retrieval, exact passage traceability, and local folder re-indexing; transcription, automated thematic claims, team annotation, and general-purpose chat remain outside the MVP.

Result depth: two. The archived QRMine result was useful for maintenance filtering but did not earn a card. No non-repository source was needed.

## Prototype 3 — thin constraint-led local/private idea

### Starting point and brief

Thin idea: “A Windows voice notebook where I press a key, speak, and later search my notes; speech and notes must stay local.”

Sanitized brief: `Find Windows-capable local voice capture, offline transcription, note storage, and search approaches that do not require sending speech to a cloud service.`

### Query trace and candidate budget

1. `offline voice notes transcription search in:name,description,readme`
2. `local whisper voice notes in:name,description,readme`
3. `desktop audio transcription local search in:name,description,readme`

The scan collected fifteen raw metadata results, deduplicated repeated OpenWhispr and list results to twelve candidates, and deeply inspected three.

Deep candidates:

- [OpenWhispr/openwhispr](https://github.com/OpenWhispr/openwhispr) — whole-product analogue or starter; README documents Windows/macOS/Linux support, hotkey dictation, offline local Whisper or Parakeet, notes, semantic search, and local models. Metadata was not archived or disabled, showed a 2026-08-07 push, and declared [MIT](https://github.com/OpenWhispr/openwhispr/blob/main/LICENSE).
- [screenpipe/screenpipe](https://github.com/screenpipe/screenpipe) — adjacent searchable-memory reference; README documents local screen/audio capture and search, but its [custom commercial license](https://github.com/screenpipe/screenpipe/blob/main/LICENSE.md) prohibits embedding or using the work to build a competing commercial product without a paid license. It is reference-only for this prototype.
- [mudler/LocalAI](https://github.com/mudler/LocalAI) — broad local model engine; metadata showed a current 2026-08-07 push and [MIT](https://github.com/mudler/LocalAI/blob/master/LICENSE), but its general multi-model engine is far larger than the narrow voice-notebook MVP and was omitted from the user-facing result.

### Possibility-first result

**A. Intentional local voice notebook — provisional recommendation.** OpenWhispr directly documents the constrained loop—Windows hotkey capture, offline transcription, notes, and semantic search—under MIT. It makes a working analogue plausible, but its much broader agents, meetings, cloud sync, and team features should be excluded from a fast MVP.

**B. Always-on searchable memory as a rejected alternative.** Screenpipe demonstrates that local audio can feed searchable personal memory, but continuous capture changes the privacy and product experience, and its current custom license blocks competing-product reuse without a commercial agreement. Keep it only as a read-only constraint reference; do not copy or integrate it.

Planning consequence if A is confirmed: lock the MVP to intentional hotkey recording, offline transcription, local note storage, search, and deletion/export controls on Windows; explicitly exclude always-on capture, cloud sync, meeting agents, and general local-AI orchestration.

Result depth: two. LocalAI was omitted because it increased dependency burden without changing the recommended MVP. No non-repository source was needed.

## Comparative result

| Prototype | Raw / deduplicated candidates | Deep inspections | Surfaced directions | Recommendation role | Concrete planning change |
|---|---:|---:|---:|---|---|
| Directionless receipts | 15 / 13 | 3 | 3 | Whole-product analogue | Receipt-first searchable inbox; defer warranties and accounting |
| Interview transcripts | 15 / 15 | 3 | 2 | Reusable retrieval pattern | Source-grounded local search; exclude transcription and auto-analysis |
| Private voice notes | 15 / 12 | 3 | 2 | Whole-product analogue | Intentional offline capture; reject always-on and cloud scope |

All cases stayed at three query angles, fifteen or fewer deduplicated candidates, three deep inspections, zero non-repository source checks, and zero repository executions. Popularity did not override fit, one archived candidate was excluded, one custom-licensed candidate was restricted to read-only reference, and weak third cards were omitted.

## Current verdict

- Bounded live-repository decision prototypes: PASS.
- Dynamic query, role, result-depth, and planning-consequence behavior: PASS at the authored decision-prototype level.
- Fresh isolated model execution and Drew review: OPEN; see [FRESH-CONTEXT-RUN.md](FRESH-CONTEXT-RUN.md) and [LIVE-ACCEPTANCE.md](LIVE-ACCEPTANCE.md).
- Acceptance checks changed: none. These prototypes are necessary evidence for `I-05`, but cannot pass it without fresh model behavior and Drew's direct judgment.
