# Impeccable Document — Existing Visual System

## Objective

Record the current visual system in `DESIGN.md` and the Impeccable sidecar without changing the website implementation.

## Problem and Why

The existing bilingual Astro portfolio has a coherent, multi-theme visual system but no `DESIGN.md`. Impeccable Live is configured, but its helper requires the existing system to be documented before a Live session can start. The user approved `$impeccable document`.

## Scope and Constraints

- Authorized outputs: `DESIGN.md`, `.impeccable/design.json`, and this recovery document.
- Do not change UI source, theme tokens, `PRODUCT.md`, build-path config, or CSP.
- Extract only existing tokens and behaviors; do not invent palette values, components, or product/brand claims.
- Separate user-confirmed product context from visual interpretations; because the user said “continue” rather than selecting visual options, use code-grounded recommendations and explicitly label the creative direction provisional.
- Browser rendered inspection was attempted, but the CUA browser host was unavailable. Use source evidence and disclose this limitation; do not claim visual verification.

## Route and Checks

- **Route:** delegated direct for the two non-trivial design artifacts; trigger evidence: broad visual-system scan spans multiple source files, and `DESIGN.md` plus `.impeccable/design.json` are coupled outputs.
- **TDD:** enabled by the workspace instructions; source: explicit project instruction. `npm test` is the project runner, but behavior tests are not applicable to these documentation/design-token artifacts. Verify by structural readback, source-to-token consistency, and JSON parsing.
- **Delivery strategy:** `ask-on-risk`; no PR requested. Forecast: approximately 150–250 authored lines in `DESIGN.md`; generated sidecar excluded from authored-line estimate, below the ~400-line heuristic.

## Acceptance Criteria

- `DESIGN.md` uses the canonical section order and records only source-backed tokens and visual rules.
- Qualitative language is based on the user's answers; unresolved preferences are not presented as settled invariants.
- `.impeccable/design.json` is valid JSON and its extracted tokens/components/narrative agree with `DESIGN.md` and the implementation.
- No UI source or CSP files are modified; browser inspection limitation is reported honestly.

## Tasks

- [x] **DOC-01 — Map incumbent visual system.** Inspect tokens, styles, layout, representative components, and responsive/motion rules. Evidence: `src/data/themes.ts`, `public/styles.css`, `src/layouts/BaseLayout.astro`, `src/components/ThemeLab.astro`. CodeGraph used before broad source inspection; rendered browser inspection unavailable.
- [x] **DOC-02 — Resolve qualitative direction.** User said “continue” after the first structured round; proceed with source-grounded recommendations rather than claim personal preference: Engineering Monograph, editorial/technical/precise voice, preserve the four palette identities, flat/ruled elevation, and precise/tactile components. Label these choices provisional in `DESIGN.md`.
- [x] **DOC-03 — Create design artifacts.** Created `DESIGN.md` and `.impeccable/design.json`. Scoped corrections replaced the unsupported Project Chip with the source-backed Theme Selection Radio, aligned the Featured Project Card heading to its responsive clamp and width cap, and added the source-backed `.specialty-tag` example plus matching typography/component frontmatter tokens.
- [x] **DOC-04 — Verify and close.** Independent verification passed: canonical section order and source claims, 36 color tokens, component references, examples, and provisional direction align; parent spot-check confirmed JSON parsing and `git diff --check` passed. Browser-rendered inspection remains unavailable because the CUA browser host was unavailable; no visual verification is claimed.

## Progress and Next Step

DOC-01 through DOC-04 are complete. Design artifacts passed independent source/structure verification and JSON parsing. No UI source or CSP was changed. Rendered inspection was unavailable. Next: commit the design documentation work unit on `feature/impeccable-document`, then record the resulting commit identity here.
