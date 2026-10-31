# Portfolio Redesign: Minimalist Engineering Monograph

## Objective

Make the portfolio professional, attractive, and easy to scan, with the work
visible without effort and the verified record at the center. Put AI, Odoo,
OWL, and OCA collaboration in the foreground.

## Specs

- S1: Use a bright, restrained palette (cream, ink, blue, green, yellow, coral,
  purple) with AA contrast for every text/background pair used.
- S2: The first viewport shows the headline and a compact proof line:
  290 merged PRs, 10 OCA merges, 78 reviews, and 1,477 ODF tests.
- S3: Four visible specialty pillars: Odoo modules & migrations, AI delivery,
  OWL interfaces, and OCA & review. Each states the public work behind it.
- S4: Keep all 10 merged OCA pull requests and the open `l10n-usa#166` in a
  compact ledger, with the 37 submitted / 19 repositories / 10 merged /
  53 reviews summary and the 26-repository, 22-author review note.
- S5: Keep the six featured projects and their verified stats. No private work,
  no unverified claims.
- S6: Keep the static Astro build and no remote assets. JavaScript is limited to
  inline, dependency-free helpers for theming.
- S7: Keep semantic HTML, keyboard focus, reduced-motion support, and no
  horizontal overflow at 390x844 and 1440x1000.
- S8: Keep the real contact email and social links.
- S9: Use the latest Stitch screen, `Antonio David — Minimalist Engineering
  Monograph` (`projects/13861423383984747592/screens/b30685f432894b5d8d9f78a5616fdaf2`),
  as the visual reference.
- S10: Replace every invented project, PR, email, metric, or title in the
  Stitch mock with verified public evidence.
- S11: The first section introduces Antonio with his GitHub avatar, name, role,
  location, and direct links.
- S12: Use first-person, concrete copy focused on shipped work. Remove generic
  marketing phrases and unverified claims.
- S13: Add a Spanish route at `/es/` with translated copy, metadata, navigation,
  status labels, and a working EN/ES switcher.
- S14: Add a light/dark theme toggle that respects the system preference,
  persists the choice, and keeps AA contrast in both themes.
- S15: Offer three distinct dark palettes (Sumi/Kanagawa, Tokyo Night, Gruvbox)
  plus the Paper light mode; expose them through a `/theme/` and `/es/theme/`
  lab with live previews and measured contrast, and keep one shared choice
  across the header menu and the lab.
- S16: In dark palettes, use editor-grade chrome: tinted surfaces, visible
  hairline borders, soft shadows, and an accent-blue call to action rather than
  inverted cream slabs.
- S17: Carry the editor metaphor into the page itself: section line numbers in
  the wide-screen gutter, a vim-style statusline, merge-state diagnostics in the
  OCA ledger, and a terminal that types once on scroll. The chrome must be
  decorative and accessible, and the typing must respect reduced motion.

## Tasks

- [x] T1 — Replaced the tokens and layout with the vivid dashboard system.
- [x] T2 — Built the sticky proof ribbon, hero scoreboard, merge wall, and win ticker.
- [x] T3 — Added the four focus pillars and the eight-card wins grid.
- [x] T4 — Restyled the projects and turned the OCA ledger into a 3-column card grid with whole-card links.
- [x] T5 — Restyled method, timeline, toolbox, contact, and footer.
- [x] T6 — Updated the ten regression tests for the new structure and palette.
- [x] T7 — Built, tested, and verified 390/1440 with Lighthouse.
- [x] T8 — Generated and implemented the Stitch "Atelier Ink & Logic" direction (superseded).
- [x] T9 — Reviewed the latest Stitch screen, "Antonio David — Minimalist Engineering Monograph", via the Stitch MCP.
- [x] T10 — Implemented the minimalist monograph: header, hero, specialty cards, selected projects, OCA ledger, approach, contact, and footer.
- [x] T11 — Self-hosted and preloaded Sora / DM Sans / JetBrains Mono, updated the tests, and re-verified Lighthouse.
- [x] T12 — Added the GitHub avatar and a profile card to the first section, with name, role, location, and links.
- [x] T13 — Rewrote the hero and section copy around shipped work, removed generic marketing lines, and added a regression test for the avatar.
- [x] T14 — Extracted the page into shared content and components, added the Spanish `/es/` route, and verified both languages.
- [x] T15 — Added the dark theme tokens, persistence, system-preference default, and toggle; verified light and dark with Lighthouse.
- [x] T16 — Restored the headline the user requested: "I design solid Odoo, AI, and OWL architectures that solve complex problems without friction."
- [x] T17 — Replaced the single dark theme with a palette engine in `src/data/themes.ts` and inline generated tokens shared by every page.
- [x] T18 — Added the `/theme/` and `/es/theme/` lab with four live previews, contrast chips, radio selection, and a system option.
- [x] T19 — Replaced the toggle with a native popover theme menu, migrated legacy `light`/`dark` values, kept the system preference reactive, and updated the tests.
- [x] T20 — Added the `01`–`06` gutter numbers at 78rem and wider, a vim-style statusline in the footer, and merged/open diagnostic dots in the OCA ledger.
- [x] T21 — Added the typed terminal with one block cursor, `IntersectionObserver` triggering, and a static reduced-motion path; fixed the `<pre>` whitespace and reserved the terminal height.

## Progress

- Latest Stitch screen reviewed: `projects/13861423383984747592/screens/b30685f432894b5d8d9f78a5616fdaf2`, 2560×7826, desktop.
- The Stitch mock used Spanish copy and invented several claims: "Senior Engineer & Tech Lead", `hello@antoniodavid.dev`, LangGraph, OWL 2.0, Pytest/Mocks, and fictional project descriptions. None were copied.
- The implementation keeps the verified record and the established English copy for the international OCA audience: 290 merged PRs, 10 OCA merges across 8 repos, 37 OCA PRs across 19 repos, 78 reviews, 53 OCA reviews, 1,477 ODF tests, and the six real projects.
- The GitHub avatar is stored locally as `public/avatar.webp` (440×440, 27 KB), with explicit dimensions to avoid layout shift.
- `npm ci` and `npm run build` pass and generate `/`, `/es/`, `/theme/`, and
  `/es/theme/`; `python -m unittest discover -s tests` passes 20 tests.
- Lighthouse on the built pages: 100 performance, accessibility, best practices, SEO, and agentic browsing for `/` in Paper and Sumi, `/theme/` in Paper and Sumi, and `/` in Sumi on mobile; 0 failures. Fonts are preloaded to avoid layout shift.
- Verified at 390×844 and 1440×1000: no horizontal overflow, no remote assets. JavaScript is limited to three inline helpers: the theme initializer, the theme control, and the terminal typing.
- The theme defaults to the system preference and persists in `localStorage` under `theme`; the header popover and the theme lab share one radio state, legacy `light`/`dark` values migrate to `paper`/`sumi`, and the language switcher keeps the equivalent route under `/` and `/es/`.
- The dark palettes were measured against their own tokens: text, accent, action, badges, terminal, and contact pairs pass 4.5:1; cards and borders use separate surface tokens instead of cream hairlines.
- Editor chrome: the gutter numbers appear only at 78rem and wider, the footer statusline is decorative (`aria-hidden`) and keeps the live theme name, the ledger dots count 10 merged plus 1 open, and the terminal types once in view with a single block cursor. With `prefers-reduced-motion: reduce` the full text and a static cursor render immediately.
- The work was stacked as `feat/avatar-copy` (PR #5), `feat/theme-lab` (PR #6), and `feat/editor-chrome` (PR #7), then merged into `main`; the responsive follow-up builds on that base.

## Log

- L1 (2026-10-30, user request, verbatim): "excelente, pero creo que puede ser mejorable, la UI hacerla mas amigable con colores vivos y llamativos, alegres. Que el descubrimiento de las cosas realizadas no sea a base de scroll, sino que el trabjo sea visible claramente sin esfuerzo, sea intrusivo mostrando los avances y victorias. Haz enfoque en la IA, Odoo, OWL y las colaboraciones con la OCA"
- L2: Implemented the vivid proof dashboard: sticky 290 / 10 / 78 / 1,477 ribbon, four focus pillars, wins grid, and compact OCA grid.
- L3 (2026-10-30, user request, verbatim): "usa el mcp stitch para apartir del design del portfolio mejorarlo con stitch y hacer un portforlio muy profesional, atractivo, entretenido y que capture mucho el interes mostrando los proyectos personales, PR hechos, colaboraciones con la OCA."
- L4: Generated the Stitch "Atelier Ink & Logic" concept and implemented its editorial direction.
- L5 (2026-10-30, user request, verbatim): "Revisar en stitch el ultimo design llamado Antonio David — Minimalist Engineering Monograph implementarlo"
- L6: Reviewed the latest Monograph screen through the Stitch MCP, implemented its minimal layout with verified content, preloaded the fonts, and re-verified build, tests, responsive layout, and Lighthouse.
- L7 (2026-10-30, user request, verbatim): "En la primera seccion no agregaste el avatar que tengo en el perfil de github, es una seccion para darme a conocer, tambien me gustaria que le quitaras todos los AI slop usando los skills y generaras una buena pagina enfocada en lo que antonio ha realizado"
- L8: Added the GitHub avatar and profile card, rewrote the hero and section copy around shipped work, removed generic marketing lines, and re-verified 11 tests plus Lighthouse on mobile and desktop.
- L9 (2026-10-30, user request, verbatim): "agregarle i18n al lenguaje spanish, tambien crearle su version dark mode. en la 1era seccion me gusta este escrito en cambio I design solid Odoo, AI, and OWL architectures that solve complex problems without friction."
- L10: Restored the requested headline, extracted shared content, added the Spanish route and language switcher, added the persisted light/dark theme with dark tokens, and verified 13 tests plus Lighthouse in English light/dark and Spanish.
- L11 (2026-10-30, user request): Replace the weak dark mode with an editor-grade system: three dark palettes (Sumi/Kanagawa, Tokyo Night, Gruvbox), a `/theme` lab to preview and apply them, and IDE-style chrome.
- L12: Verified the old dark theme failed perceptually (card/background 1.11:1, 24 cream borders at ~16:1, invisible black shadows); replaced it with generated palette tokens, 1 px hairlines, tinted surfaces, soft shadows, and an accent CTA; added the theme lab, popover menu, legacy migration, and 18 tests.
- L13 (2026-10-30, continuation of L11): Added the editor chrome — gutter line numbers, statusline, OCA diagnostics, and the typed terminal — with reduced-motion and no-JS fallbacks; raised the inline-script budget to three and the suite to 20 tests.
- L14 (2026-10-30, user request, verbatim): "https://antoniodavid.github.io/, revisar esta pagina que se ve mal" — Fixed the visible responsive defects: replaced the font-dependent `◐` theme glyph with an inline SVG, moved the hero copy before the profile card on narrow screens so the CTA is above the fold, wrapped proof stats as complete value/label units, made the highlighted headline fit a 320px viewport, grouped the tablet navigation, let the header tagline yield before the nav wraps near 1024px, and kept the 320px Spanish nav on one row. Re-verified 20 tests, no horizontal overflow at 320/360/390/768/1024/1440, and Lighthouse 100 in all five categories for Paper and Sumi on desktop and mobile.
- L15 (2026-10-31, user request, verbatim): "Quiero agregar las herramientas con las que trabajo en mi dia a dia, que estan siendo revolucionarias, como opencode, pi, codex, herdr, nvim, lazygit, omarchy fan, doodba como plataforma de desarrollo y otros, crea una seccion muy graciosa donde introduzcas estas herramientas con sus links de referencias con las que trabajo en mi dia a dia. expande la idea y mejorala. haz una buena seccion usando las skills" + "agrega el harness ODF como herramienta tambien" — Added `#stack`, a daily-drivers sponsor band between Method and Contact: ODF Agent Team, OpenCode, pi, Codex, Herdr, Neovim, Lazygit, Doodba, Omarchy, plus six add-ons; all links point to official project sites. Both locales, no new JS or dependencies; extended the existing 20 tests and tightened the six-label navigation at 320px, 961–1200px, and the tagline band to keep every header on one row.
- L16 (2026-10-31, user request, verbatim): "la secion del stack, es muy largo peudes hacerlo a lo ancho? como una marquesina, esa seccion que tenga buen contraste quizas como unsa seccion de sponsoring. anima la seccion, que tenga vida, ponle iconos animados que salten cuando se loe pone el mouse encima" + "actualiza el link del ODF https://antoniodavid.github.io/odf-agent-team" — Redesigned `#stack` as a full-bleed dark sponsor band with an animated ticker, nine tool tiles in a 3×3 desktop grid, horizontal tool/add-on strips on mobile, inline SVG icons that hop on hover/focus, a pulsing “sponsored by nobody” badge, and a compact total strip. ODF now links to `https://antoniodavid.github.io/odf-agent-team/`. Verified 20 tests, no horizontal overflow at 320/360/390/768/1024/1440 on all four pages, reduced-motion disables the ticker/pulse/hop, and Lighthouse is 100 in all five categories for EN/ES desktop and EN mobile (ES mobile 0.99 performance, 100 in the other four).
