export type ThemeId = "paper" | "sumi" | "tokyo" | "gruvbox";
export type ThemeKind = "light" | "dark";
export type Locale = "en" | "es";

export interface ThemeDefinition {
  id: ThemeId;
  label: string;
  kind: ThemeKind;
  note: Record<Locale, string>;
  colors: Record<string, string>;
}

/**
 * Single source of truth for every palette. The CSS custom properties are
 * generated from this list and injected once by BaseLayout, so the theme lab
 * and the rendered site can never drift apart.
 */
export const themes: ThemeDefinition[] = [
  {
    id: "paper",
    label: "Paper",
    kind: "light",
    note: {
      en: "Washi paper, black ink, hard shadows. The editorial mode.",
      es: "Papel washi, tinta negra, sombras duras. El modo editorial.",
    },
    colors: {
      bg: "#fffdf7",
      surface: "#fcf9f8",
      card: "#ffffff",
      ink: "#161616",
      "ink-2": "#4d515f",
      line: "#161616",
      "line-strong": "#161616",
      bw: "2px",
      blue: "#1e4fd8",
      "on-blue": "#ffffff",
      "blue-text": "#1e4fd8",
      "blue-deep": "#004ac6",
      "blue-soft": "#ebf1ff",
      green: "#00a878",
      "green-deep": "#007f56",
      "green-soft": "#e8f8f2",
      yellow: "#ffe37e",
      "gold-deep": "#7a5f00",
      coral: "#ff5a5f",
      "coral-deep": "#b91c1c",
      "coral-soft": "#fff0f0",
      purple: "#7c3aed",
      "purple-soft": "#f3e8ff",
      terminal: "#161616",
      "terminal-text": "#fffdf7",
      "terminal-muted": "#a7b7ad",
      "terminal-line": "rgba(255, 253, 247, 0.2)",
      "contact-bg": "#161616",
      "contact-fg": "#fffdf7",
      "contact-muted": "#d8d2c4",
      "badge-ink": "#161616",
      "soft-line": "rgba(22, 22, 22, 0.2)",
      "header-bg": "rgba(255, 253, 247, 0.95)",
      "mark-bg": "#ffe37e",
      "mark-fg": "#161616",
      "mark-border": "#161616",
      "btn-bg": "#161616",
      "btn-fg": "#fffdf7",
      "shadow-xs": "2px 2px 0 #161616",
      "shadow-sm": "3px 3px 0 #161616",
      "shadow-md": "5px 5px 0 #161616",
      "shadow-lg": "7px 7px 0 #161616",
      "shadow-hover-sm": "3px 3px 0 #161616",
      "shadow-hover-md": "6px 6px 0 #161616",
    },
  },
  {
    id: "sumi",
    label: "Sumi",
    kind: "dark",
    note: {
      en: "Kanagawa. Sumi ink, wave blue, oni violet. The default editor.",
      es: "Kanagawa. Tinta sumi, azul ola, violeta oni. El editor por defecto.",
    },
    colors: {
      bg: "#1f1f28",
      surface: "#24242f",
      card: "#2f2f3d",
      ink: "#dcd7ba",
      "ink-2": "#c8c093",
      line: "#4a4a60",
      "line-strong": "#54546d",
      bw: "1px",
      blue: "#7e9cd8",
      "on-blue": "#1f1f28",
      "blue-text": "#7e9cd8",
      "blue-deep": "#a3d4d5",
      "blue-soft": "#223249",
      green: "#98bb6c",
      "green-deep": "#98bb6c",
      "green-soft": "#22301f",
      yellow: "#e6c384",
      "gold-deep": "#e6c384",
      coral: "#ff5d62",
      "coral-deep": "#ff9b9b",
      "coral-soft": "#2a1a1a",
      purple: "#a98fce",
      "purple-soft": "#2a2438",
      terminal: "#16161e",
      "terminal-text": "#dcd7ba",
      "terminal-muted": "#828793",
      "terminal-line": "rgba(220, 215, 186, 0.14)",
      "contact-bg": "#2f2f3d",
      "contact-fg": "#dcd7ba",
      "contact-muted": "#c8c093",
      "badge-ink": "#1f1f28",
      "soft-line": "rgba(220, 215, 186, 0.14)",
      "header-bg": "rgba(31, 31, 40, 0.92)",
      "mark-bg": "rgba(230, 195, 132, 0.16)",
      "mark-fg": "#e6c384",
      "mark-border": "rgba(230, 195, 132, 0.45)",
      "btn-bg": "#7e9cd8",
      "btn-fg": "#1f1f28",
      "shadow-xs": "0 1px 2px rgba(0, 0, 0, 0.35)",
      "shadow-sm": "0 8px 20px rgba(0, 0, 0, 0.35)",
      "shadow-md": "0 14px 32px rgba(0, 0, 0, 0.4)",
      "shadow-lg": "0 20px 48px rgba(0, 0, 0, 0.45)",
      "shadow-hover-sm": "0 10px 24px rgba(0, 0, 0, 0.4)",
      "shadow-hover-md": "0 16px 36px rgba(0, 0, 0, 0.45)",
    },
  },
  {
    id: "tokyo",
    label: "Tokyo Night",
    kind: "dark",
    note: {
      en: "Tokyo Night. Cold night blue, electric accents, zero sepia.",
      es: "Tokyo Night. Azul nocturno frío, acentos eléctricos, sin sepia.",
    },
    colors: {
      bg: "#1a1b26",
      surface: "#1f2335",
      card: "#272b40",
      ink: "#c0caf5",
      "ink-2": "#a9b1d6",
      line: "#414868",
      "line-strong": "#545c8a",
      bw: "1px",
      blue: "#7aa2f7",
      "on-blue": "#1a1b26",
      "blue-text": "#7aa2f7",
      "blue-deep": "#7dcfff",
      "blue-soft": "#1f2a44",
      green: "#9ece6a",
      "green-deep": "#9ece6a",
      "green-soft": "#1f2f22",
      yellow: "#e0af68",
      "gold-deep": "#e0af68",
      coral: "#f7768e",
      "coral-deep": "#ff9eae",
      "coral-soft": "#2a1a24",
      purple: "#bb9af7",
      "purple-soft": "#2a2340",
      terminal: "#16161e",
      "terminal-text": "#c0caf5",
      "terminal-muted": "#7d84ad",
      "terminal-line": "rgba(192, 202, 245, 0.12)",
      "contact-bg": "#272b40",
      "contact-fg": "#c0caf5",
      "contact-muted": "#a9b1d6",
      "badge-ink": "#1a1b26",
      "soft-line": "rgba(192, 202, 245, 0.14)",
      "header-bg": "rgba(26, 27, 38, 0.92)",
      "mark-bg": "rgba(224, 175, 104, 0.16)",
      "mark-fg": "#e0af68",
      "mark-border": "rgba(224, 175, 104, 0.42)",
      "btn-bg": "#7aa2f7",
      "btn-fg": "#1a1b26",
      "shadow-xs": "0 1px 2px rgba(0, 0, 0, 0.35)",
      "shadow-sm": "0 8px 20px rgba(0, 0, 0, 0.35)",
      "shadow-md": "0 14px 32px rgba(0, 0, 0, 0.4)",
      "shadow-lg": "0 20px 48px rgba(0, 0, 0, 0.45)",
      "shadow-hover-sm": "0 10px 24px rgba(0, 0, 0, 0.4)",
      "shadow-hover-md": "0 16px 36px rgba(0, 0, 0, 0.45)",
    },
  },
  {
    id: "gruvbox",
    label: "Gruvbox",
    kind: "dark",
    note: {
      en: "Gruvbox. Warm retro contrast, easy on the eyes at night.",
      es: "Gruvbox. Contraste retro cálido, cómodo de noche.",
    },
    colors: {
      bg: "#1d2021",
      surface: "#282828",
      card: "#3a3735",
      ink: "#ebdbb2",
      "ink-2": "#bdae93",
      line: "#504945",
      "line-strong": "#665c54",
      bw: "1px",
      blue: "#83a598",
      "on-blue": "#1d2021",
      "blue-text": "#8fc2b4",
      "blue-deep": "#8ec07c",
      "blue-soft": "#1e2f2c",
      green: "#b8bb26",
      "green-deep": "#b8bb26",
      "green-soft": "#2a2f1a",
      yellow: "#fabd2f",
      "gold-deep": "#fabd2f",
      coral: "#fb4934",
      "coral-deep": "#fb4934",
      "coral-soft": "#2f1a17",
      purple: "#d3869b",
      "purple-soft": "#2f2026",
      terminal: "#161616",
      "terminal-text": "#ebdbb2",
      "terminal-muted": "#928374",
      "terminal-line": "rgba(235, 219, 178, 0.14)",
      "contact-bg": "#3a3735",
      "contact-fg": "#ebdbb2",
      "contact-muted": "#bdae93",
      "badge-ink": "#1d2021",
      "soft-line": "rgba(235, 219, 178, 0.14)",
      "header-bg": "rgba(29, 32, 33, 0.92)",
      "mark-bg": "rgba(250, 189, 47, 0.16)",
      "mark-fg": "#fabd2f",
      "mark-border": "rgba(250, 189, 47, 0.45)",
      "btn-bg": "#83a598",
      "btn-fg": "#1d2021",
      "shadow-xs": "0 1px 2px rgba(0, 0, 0, 0.35)",
      "shadow-sm": "0 8px 20px rgba(0, 0, 0, 0.35)",
      "shadow-md": "0 14px 32px rgba(0, 0, 0, 0.4)",
      "shadow-lg": "0 20px 48px rgba(0, 0, 0, 0.45)",
      "shadow-hover-sm": "0 10px 24px rgba(0, 0, 0, 0.4)",
      "shadow-hover-md": "0 16px 36px rgba(0, 0, 0, 0.45)",
    },
  },
];

export const themeIds = themes.map((theme) => theme.id);

const declarations = (colors: Record<string, string>) =>
  Object.entries(colors)
    .map(([token, value]) => `--${token}: ${value};`)
    .join("");

/** Generated once and injected as an inline <style> before the main sheet. */
export const themeCss = themes
  .map(
    (theme) =>
      `[data-theme="${theme.id}"]{color-scheme:${theme.kind};${declarations(theme.colors)}}`,
  )
  .join("\n");

export const themeBackgrounds = Object.fromEntries(
  themes.map((theme) => [theme.id, theme.colors.bg]),
);

export const themeLabels = Object.fromEntries(
  themes.map((theme) => [theme.id, theme.label]),
);

function hexToRgb(hex: string): [number, number, number] | null {
  const match = /^#([0-9a-f]{6})$/i.exec(hex);
  if (!match) return null;
  const value = match[1];
  return [
    Number.parseInt(value.slice(0, 2), 16),
    Number.parseInt(value.slice(2, 4), 16),
    Number.parseInt(value.slice(4, 6), 16),
  ];
}

function relativeLuminance(hex: string): number {
  const rgb = hexToRgb(hex);
  if (!rgb) return 0;
  const channels = rgb.map((channel) => {
    const value = channel / 255;
    return value <= 0.04045 ? value / 12.92 : ((value + 0.055) / 1.055) ** 2.4;
  });
  return channels[0] * 0.2126 + channels[1] * 0.7152 + channels[2] * 0.0722;
}

export function contrastRatio(first: string, second: string): number {
  const a = relativeLuminance(first);
  const b = relativeLuminance(second);
  return (Math.max(a, b) + 0.05) / (Math.min(a, b) + 0.05);
}

export function paletteContrast(theme: ThemeDefinition) {
  return {
    text: contrastRatio(theme.colors.ink, theme.colors.bg),
    accent: contrastRatio(theme.colors["blue-text"], theme.colors.bg),
    action: contrastRatio(theme.colors["btn-fg"], theme.colors["btn-bg"]),
  };
}
