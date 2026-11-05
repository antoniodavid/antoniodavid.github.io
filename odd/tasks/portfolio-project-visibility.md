# Portfolio Project Visibility

## Objective

Make every currently listed project visible on the portfolio homepage by converting the five-item collapsed “More experiments” disclosure into a compact, always-visible archive.

## Problem and Why

The user confirmed that the portfolio is for programmers and recruiters and exists to make all their work visible. The homepage currently places five additional projects inside a collapsed disclosure, which weakens discovery of the breadth of the portfolio.

## Scope and Constraints

- Authorized source scope: homepage project markup and its styles; add or update a focused test only if the existing test structure supports a reliable check.
- Preserve all existing project facts, names, descriptions, links, bilingual behavior, four theme palettes, and theme-aware visual language.
- Keep the five additional projects visually secondary and compact; do not alter headline metrics or reconcile OCA counts without a source of truth.
- Do not redesign unrelated sections, rewrite PRODUCT.md or DESIGN.md, add dependencies, or change CSP.
- Rendered browser inspection may remain unavailable; report that limitation honestly.

## Route and Checks

- **Route:** delegated direct. Mapping trigger fired because understanding crossed four source files; a read-only mapper narrowed the change to the homepage project archive. Writer delegation is required because the change spans non-trivial markup and styles.
- **TDD:** strict TDD enabled by explicit workspace instructions. Exact runner: `npm test` (Astro build followed by Python unittest discovery). Writer must observe RED before implementation, then GREEN, REFACTOR; do not fabricate RED evidence.
- **Delivery strategy:** `ask-on-risk`; no PR requested. Expected source delta is a compact, single behavior slice below the ~400 authored-line heuristic.

## Acceptance Criteria

- All five existing additional project links and descriptions are visible without user interaction on both English and Spanish homepages.
- The archive remains visually subordinate to the featured project and readable at mobile widths.
- Keyboard focus, link names, semantic landmarks/headings, and all four themes remain usable.
- Project facts and existing content remain unchanged; no headline/OCA metrics are edited.
- Applicable tests/build pass; report rendered inspection availability honestly.

## Tasks

- [x] **VIS-01 — Implement the always-visible project archive.** Replaced the collapsed disclosure with a compact semantic archive and responsive theme-aware styles. Reused all five existing localized labels, links, and descriptions. Added a generated-homepage test covering all five links in both locales and asserting they are not inside a closed disclosure. Work-unit commit: `2173250` (`feat(portfolio): surface all listed projects`).
- [x] **VIS-02 — Verify and close.** Strict TDD evidence: `npm test` RED after build with all 10 locale/project visibility checks failing; after implementation/refactor, `npm test` passed the Astro build and all 21 tests. Independent verification and parent-ordered spot check also passed; `git diff --check` clean. No browser rendering was available; no visual verification is claimed.

## Progress and Next Step

The five entries previously under “More experiments” are now visible as a dense secondary archive, using existing bilingual links and copy. The user confirmed the TDD contract: both homepage locales must expose all five links without opening the disclosure. Writer and independent verifier checks passed. No metrics, CSP, unrelated sections, or project facts changed. The work unit is committed on `feature/impeccable-document` as `2173250`; this follow-up records that evidence in the task file.
