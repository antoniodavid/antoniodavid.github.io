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

Both routes include a light/dark theme toggle. The choice is stored in
`localStorage` and defaults to the system preference.

## Deploy

Pushes to `main` run `.github/workflows/deploy.yml`, build the site, and publish
`dist/` through GitHub Pages. The repository's Pages source must be set to
**GitHub Actions**.
