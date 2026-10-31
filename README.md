# antoniodavid.github.io

Astro source for Antonio David's portfolio.

## Development

```sh
npm install
npm run dev
```

## Build and test

```sh
npm run build
python -m unittest discover -s tests
```

The tests read the generated `dist/` output, so build before running them.

## Routes and themes

- `/` — English
- `/es/` — Spanish
- `/theme/` — English theme lab
- `/es/theme/` — Spanish theme lab

Four palettes are available: **Paper** (light), **Sumi** (Kanagawa, the default
dark), **Tokyo Night**, and **Gruvbox**. The header menu and the theme lab share
one per-browser choice, stored in `localStorage` under `theme`; the `system`
option follows `prefers-color-scheme` (Paper in light, Sumi in dark). Legacy
`light` / `dark` values migrate automatically.

`src/data/themes.ts` is the single source of truth: CSS custom properties are
generated from it and injected inline by `BaseLayout.astro`, so the lab's
contrast figures and the rendered site use the same tokens.

## Deploy

Pushes to `main` run `.github/workflows/deploy.yml`, build the site, and publish
`dist/` through GitHub Pages. The repository's Pages source must be set to
**GitHub Actions**.
