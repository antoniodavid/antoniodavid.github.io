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
- S6: Keep the static Astro build, no JavaScript, and no remote assets.
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

## Progress

- Latest Stitch screen reviewed: `projects/13861423383984747592/screens/b30685f432894b5d8d9f78a5616fdaf2`, 2560×7826, desktop.
- The Stitch mock used Spanish copy and invented several claims: "Senior Engineer & Tech Lead", `hello@antoniodavid.dev`, LangGraph, OWL 2.0, Pytest/Mocks, and fictional project descriptions. None were copied.
- The implementation keeps the verified record and the established English copy for the international OCA audience: 290 merged PRs, 10 OCA merges across 8 repos, 37 OCA PRs across 19 repos, 78 reviews, 53 OCA reviews, 1,477 ODF tests, and the six real projects.
- The GitHub avatar is stored locally as `public/avatar.webp` (440×440, 27 KB), with explicit dimensions to avoid layout shift.
- `npm ci` and `npm run build` pass; `python -m unittest discover -s tests` passes 11 tests.
- Lighthouse on the built page: mobile and desktop 100 accessibility / 100 best practices / 100 SEO / 100 agentic browsing, 0 failures. Fonts are preloaded to avoid layout shift.
- Verified at 390×844 and 1440×1000: no horizontal overflow, no JavaScript, no remote assets.
- The work is on `feat/minimalist-monograph` and PR #4; it is not merged.

## Log

- L1 (2026-10-30, user request, verbatim): "excelente, pero creo que puede ser mejorable, la UI hacerla mas amigable con colores vivos y llamativos, alegres. Que el descubrimiento de las cosas realizadas no sea a base de scroll, sino que el trabjo sea visible claramente sin esfuerzo, sea intrusivo mostrando los avances y victorias. Haz enfoque en la IA, Odoo, OWL y las colaboraciones con la OCA"
- L2: Implemented the vivid proof dashboard: sticky 290 / 10 / 78 / 1,477 ribbon, four focus pillars, wins grid, and compact OCA grid.
- L3 (2026-10-30, user request, verbatim): "usa el mcp stitch para apartir del design del portfolio mejorarlo con stitch y hacer un portforlio muy profesional, atractivo, entretenido y que capture mucho el interes mostrando los proyectos personales, PR hechos, colaboraciones con la OCA."
- L4: Generated the Stitch "Atelier Ink & Logic" concept and implemented its editorial direction.
- L5 (2026-10-30, user request, verbatim): "Revisar en stitch el ultimo design llamado Antonio David — Minimalist Engineering Monograph implementarlo"
- L6: Reviewed the latest Monograph screen through the Stitch MCP, implemented its minimal layout with verified content, preloaded the fonts, and re-verified build, tests, responsive layout, and Lighthouse.
- L7 (2026-10-30, user request, verbatim): "En la primera seccion no agregaste el avatar que tengo en el perfil de github, es una seccion para darme a conocer, tambien me gustaria que le quitaras todos los AI slop usando los skills y generaras una buena pagina enfocada en lo que antonio ha realizado"
- L8: Added the GitHub avatar and profile card, rewrote the hero and section copy around shipped work, removed generic marketing lines, and re-verified 11 tests plus Lighthouse on mobile and desktop.
