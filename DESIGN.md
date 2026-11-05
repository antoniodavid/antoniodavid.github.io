---
name: Antonio David Portfolio
description: A source-backed visual system for a bilingual portfolio with four selectable themes.
colors:
  paper-bg: "#fffdf7"
  paper-surface: "#fcf9f8"
  paper-card: "#ffffff"
  paper-ink: "#161616"
  paper-blue: "#1e4fd8"
  paper-green: "#00a878"
  paper-yellow: "#ffe37e"
  paper-coral: "#ff5a5f"
  paper-purple: "#7c3aed"
  sumi-bg: "#1f1f28"
  sumi-surface: "#24242f"
  sumi-card: "#2f2f3d"
  sumi-ink: "#dcd7ba"
  sumi-blue: "#7e9cd8"
  sumi-green: "#98bb6c"
  sumi-yellow: "#e6c384"
  sumi-coral: "#ff5d62"
  sumi-purple: "#a98fce"
  tokyo-bg: "#1a1b26"
  tokyo-surface: "#1f2335"
  tokyo-card: "#272b40"
  tokyo-ink: "#c0caf5"
  tokyo-blue: "#7aa2f7"
  tokyo-green: "#9ece6a"
  tokyo-yellow: "#e0af68"
  tokyo-coral: "#f7768e"
  tokyo-purple: "#bb9af7"
  gruvbox-bg: "#1d2021"
  gruvbox-surface: "#282828"
  gruvbox-card: "#3a3735"
  gruvbox-ink: "#ebdbb2"
  gruvbox-blue: "#83a598"
  gruvbox-green: "#b8bb26"
  gruvbox-yellow: "#fabd2f"
  gruvbox-coral: "#fb4934"
  gruvbox-purple: "#d3869b"
typography:
  display:
    fontFamily: '"Fraunces Variable", "Fraunces", Georgia, "Times New Roman", serif'
    fontSize: "clamp(2.8rem, 4.6vw, 4rem)"
    fontWeight: 700
    lineHeight: 1.04
    letterSpacing: "-0.02em"
  body:
    fontFamily: '"IBM Plex Sans Variable", "IBM Plex Sans", "Avenir Next", "Segoe UI", system-ui, sans-serif'
    fontSize: "1rem"
    lineHeight: 1.6
  label:
    fontFamily: '"JetBrains Mono Variable", "JetBrains Mono", "SFMono-Regular", "Cascadia Code", monospace'
    fontSize: "0.66rem"
    fontWeight: 600
    letterSpacing: "0.04em"
  theme-choice:
    fontFamily: '"JetBrains Mono Variable", "JetBrains Mono", "SFMono-Regular", "Cascadia Code", monospace'
    fontSize: "0.58rem"
  specialty-tag:
    fontFamily: '"JetBrains Mono Variable", "JetBrains Mono", "SFMono-Regular", "Cascadia Code", monospace'
    fontSize: "0.58rem"
    fontWeight: 700
    letterSpacing: "0.04em"
  mono:
    fontFamily: '"JetBrains Mono Variable", "JetBrains Mono", "SFMono-Regular", "Cascadia Code", monospace'
    fontSize: "0.7rem"
    lineHeight: 1.8
rounded:
  xs: "2px"
  sm: "4px"
  md: "6px"
  pill: "999px"
spacing:
  gutter: "clamp(1.25rem, 4vw, 2.5rem)"
  section: "clamp(4rem, 8vw, 6rem)"
components:
  button-primary:
    backgroundColor: "var(--btn-bg)"
    textColor: "var(--btn-fg)"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: "0.8rem 1.2rem"
  button-secondary:
    backgroundColor: "var(--card)"
    textColor: "var(--ink)"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: "0.8rem 1.2rem"
  button-blue:
    backgroundColor: "var(--blue)"
    textColor: "var(--on-blue)"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: "0.8rem 1.2rem"
  nav-link:
    textColor: "var(--ink)"
    typography: "{typography.label}"
  theme-choice:
    typography: "{typography.theme-choice}"
    rounded: "{rounded.sm}"
    padding: "0.5rem 0.6rem"
  specialty-tag:
    typography: "{typography.specialty-tag}"
    rounded: "{rounded.xs}"
    padding: "0.2rem 0.5rem"
  card-featured:
    backgroundColor: "var(--card)"
    textColor: "var(--ink)"
    rounded: "{rounded.md}"
    padding: "1.75rem"
  terminal-panel:
    backgroundColor: "var(--terminal)"
    textColor: "var(--terminal-text)"
    typography: "{typography.mono}"
    rounded: "{rounded.md}"
    padding: "1rem"
---

# Design System: Antonio David Portfolio

## Overview

**Creative North Star: "The Engineering Monograph"** — provisional recommendation, not user-confirmed.

Confirmed context: the bilingual portfolio and its selectable theme lab remain as implemented. The Engineering Monograph frame is a provisional visual recommendation—not a user-confirmed brand statement—grounded in the existing editorial typography, ruled sections, technical labels, and evidence panels.

This capture is source-derived. Rendered browser inspection was unavailable because the CUA browser host was unavailable, so no visual-verification claim is made.

**Key Characteristics:**
- Editorial serif display type sits beside sans-serif reading copy and monospaced technical labels.
- Ruled sections, theme-colored borders, and tonal surfaces organize dense information.
- Paper, Sumi, Tokyo Night, and Gruvbox retain separate color identities over shared layout and component patterns.
- The precise, tactile, flat/ruled direction is a provisional recommendation, not a user-confirmed preference.

## Colors

The site exposes four runtime-switchable palettes through one theme source. The values below capture each palette's background, surface, card, ink, and recurring accent roles; the generated theme variables remain the runtime source of truth.

### Primary
- **Paper Blue** (`paper-blue`): the blue action and link accent in Paper.
- **Sumi Wave Blue** (`sumi-blue`): the blue action and link accent in Sumi.
- **Tokyo Night Blue** (`tokyo-blue`): the cool action and link accent in Tokyo Night.
- **Gruvbox Blue** (`gruvbox-blue`): the action and link accent under the Gruvbox label.

### Secondary
- **Paper Green** (`paper-green`) and **Paper Yellow** (`paper-yellow`): retain their existing status and highlight roles.
- **Sumi Green** (`sumi-green`) and **Sumi Yellow** (`sumi-yellow`): retain their existing status and highlight roles.
- **Tokyo Night Green** (`tokyo-green`) and **Tokyo Night Yellow** (`tokyo-yellow`): retain their existing status and highlight roles.
- **Gruvbox Green** (`gruvbox-green`) and **Gruvbox Yellow** (`gruvbox-yellow`): retain their existing status and highlight roles.

### Tertiary
- **Paper Coral** (`paper-coral`) and **Paper Purple** (`paper-purple`): the existing open-state and category accents.
- **Sumi Coral** (`sumi-coral`) and **Sumi Purple** (`sumi-purple`): the existing open-state and category accents.
- **Tokyo Night Coral** (`tokyo-coral`) and **Tokyo Night Purple** (`tokyo-purple`): the existing open-state and category accents.
- **Gruvbox Coral** (`gruvbox-coral`) and **Gruvbox Purple** (`gruvbox-purple`): the existing open-state and category accents.

### Neutral
- **Paper** (`paper-bg`, `paper-surface`, `paper-card`, `paper-ink`): the light background, quiet surface, card face, and primary text.
- **Sumi** (`sumi-bg`, `sumi-surface`, `sumi-card`, `sumi-ink`): the dark background, quiet surface, card face, and primary text.
- **Tokyo Night** (`tokyo-bg`, `tokyo-surface`, `tokyo-card`, `tokyo-ink`): the dark background, quiet surface, card face, and primary text.
- **Gruvbox** (`gruvbox-bg`, `gruvbox-surface`, `gruvbox-card`, `gruvbox-ink`): the dark background, quiet surface, card face, and primary text.

**The Theme-Family Rule.** Provisional recommendation: keep each palette's surfaces and accents together rather than mixing colors across themes.

## Typography

**Display Font:** Fraunces Variable (Fraunces, Georgia, Times New Roman, serif)
**Body Font:** IBM Plex Sans Variable (IBM Plex Sans, Avenir Next, Segoe UI, system-ui, sans-serif)
**Label/Mono Font:** JetBrains Mono Variable (JetBrains Mono, SFMono-Regular, Cascadia Code, monospace)

**Character:** the display serif gives headings an editorial voice; the sans face carries reading copy, while monospaced labels and code mark technical metadata.

### Hierarchy
- **Display** (700, clamp(2.8rem, 4.6vw, 4rem), line-height 1.04, letter-spacing -0.02em): the main heading.
- **Title** (600, 1.35rem, line-height 1.2, letter-spacing -0.01em): the tertiary heading and card title.
- **Body** (1rem, line-height 1.6): default reading copy.
- **Label** (600, 0.66rem, letter-spacing 0.04em, uppercase): primary navigation and compact metadata.
- **Code** (0.7rem, line-height 1.8): terminal output and technical data.

**The Three-Register Rule.** Keep display, reading, and technical text in their observed type roles; do not use the mono face as paragraph copy.

## Layout

Content sits in a centered container capped at 72rem, with horizontal gutters that grow responsively from 1.25rem to 2.5rem. Sections use a fluid vertical rhythm from 4rem to 6rem. The wide hero is a two-column grid with a generous fluid gap; at 60rem and below it becomes one column. The profile panel becomes a compact image-and-copy row at that breakpoint.

At 60rem and below, project-led feature grids and the theme lab collapse to one column; at 48rem and below, project rows stack and the header call-to-action and brand tagline hide. At 36rem and below, hero actions fill the available width, and the main heading scales down. The layout keeps a 320px minimum viewport width.

## Elevation & Depth

The stylesheet contains no box-shadow declarations. Cards, sections, and terminal panels are separated with theme-aware borders and background/surface/card tones, including a darker terminal surface. The provisional flat/ruled recommendation preserves this existing depth model rather than adding shadows.

**The Ruled-Surface Rule.** Provisional recommendation: use borders and tonal surfaces for separation; do not add shadows to imitate the incumbent system.

## Shapes

The form language uses compact rectangles with 2px, 4px, and 6px radii; 999px pills are reserved for a small number of status/availability badges. Borders use a theme-selected 2px width in Paper and 1px width in Sumi, Tokyo Night, and Gruvbox. Cards keep the same modest radius; the terminal panel clips its contents to its border.

## Components

Component examples capture implemented visual patterns; any sample labels in the sidecar are illustrative, not replacement product copy.

### Buttons
- **Shape:** gently rounded corners (4px); body sans, 0.82rem and weight 700, with 0.8rem × 1.2rem padding.
- **Primary:** the dark/light theme-aware action uses each theme's button foreground/background; the secondary surface variant uses the card and ink colors; a blue-accent variant uses the palette's blue/on-blue pair.
- **Hover / Focus:** hover shifts the border to the theme's blue-text color. Focus-visible links keep the 3px theme-blue outline with 3px offset.
- **Header action:** a separate compact link uses 0.5rem × 0.8rem padding and the theme's blue/on-blue pair.

### Tags and badges
- **Style:** compact tag labels use 2px corners. Status and availability badges retain the theme's status colors; availability uses the pill shape.

### Theme selection
- **Control:** a native radio sits in a 4px rounded label with a 1px theme-strong border and 0.5rem × 0.6rem padding.
- **Label and state:** uppercase JetBrains Mono at 0.58rem; hover fills with the theme surface, the radio uses the theme blue accent, and the selected theme card receives a 2px blue-text outline with 3px offset.

### Cards / Containers
- **Corner Style:** the recurring profile and feature cards use 6px corners.
- **Background:** card surfaces use the active theme's card token; contact and terminal panels use their dedicated theme tokens.
- **Shadow Strategy:** no shadows are used in the stylesheet; borders and theme-toned fills define separation.
- **Border:** card outlines use the theme's line token and border width.
- **Internal Padding:** the featured panel uses 1.75rem; the profile panel uses 0.9rem.
- **Featured heading:** expands to clamp(2rem, 3.4vw, 2.8rem) and is capped at 20ch.

### Terminal Panel
- **Character:** precise, tactile technical panel; descriptive direction is provisional.
- **Frame:** 6px corners, clipped content, and a bottom-rule header.
- **Text:** 0.7rem JetBrains Mono with 1.8 line height and theme-specific terminal colors.
- **Motion:** the cursor blinks in the implementation; it stops under reduced-motion preference.

### Navigation
- **Style:** sticky top bar with a bottom rule; links use uppercase JetBrains Mono at 0.66rem, weight 600, and 0.04em letter spacing.
- **Responsive:** the nav wraps below 60rem; the header call-to-action and brand tagline are hidden below 48rem.

## Do's and Don'ts

### Do:
- **Do** keep the four theme identities and their runtime-selected token families intact.
- **Do** use the existing Fraunces, IBM Plex Sans, and JetBrains Mono roles.
- **Do** preserve the theme-aware border and tonal-surface model when extending components.
- **Do** retain visible link focus and reduced-motion behavior.

### Don't:
- **Don't** mix palette tokens across the four themes.
- **Don't** add shadows as a substitute for the existing ruled, tonal separation.
- **Don't** widen card corners beyond the existing modest radius scale without an explicit design decision.
- **Don't** present the Engineering Monograph or precise/tactile language as user-confirmed.
