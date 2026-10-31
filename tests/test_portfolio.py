from html.parser import HTMLParser
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"


def css_color(styles, token):
    match = re.search(rf"--{token}:\s*(#[0-9a-fA-F]{{6}})\s*;", styles)
    if match is None:
        raise AssertionError(f"Missing color token --{token}")
    value = match.group(1).lstrip("#")
    return tuple(int(value[index : index + 2], 16) for index in (0, 2, 4))


def theme_css_block(page):
    match = re.search(r'<style id="theme-tokens"[^>]*>(.*?)</style>', page, re.DOTALL)
    if match is None:
        raise AssertionError("Missing the generated theme token block")
    return match.group(1)


def theme_tokens(theme_css, theme_id):
    match = re.search(
        rf'\[data-theme="{theme_id}"\]\s*\{{(.*?)\}}', theme_css, re.DOTALL
    )
    if match is None:
        raise AssertionError(f"Missing theme tokens for {theme_id}")
    return match.group(1)


def relative_luminance(color):
    channels = []
    for channel in color:
        value = channel / 255
        channels.append(
            value / 12.92 if value <= 0.04045 else ((value + 0.055) / 1.055) ** 2.4
        )
    return sum(
        weight * channel
        for weight, channel in zip((0.2126, 0.7152, 0.0722), channels)
    )


def contrast_ratio(first, second):
    lighter, darker = sorted(
        (relative_luminance(first), relative_luminance(second)), reverse=True
    )
    return (lighter + 0.05) / (darker + 0.05)


class PortfolioMarkup(HTMLParser):
    def __init__(self):
        super().__init__()
        self.elements = []
        self.text = []
        self.list_items = []
        self._open_list_items = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        self.elements.append((tag, attributes))
        if tag == "li":
            self._open_list_items.append({"hrefs": [], "text": []})
        elif tag == "a" and self._open_list_items:
            self._open_list_items[-1]["hrefs"].append(attributes.get("href", ""))

    def handle_startendtag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))

    def handle_data(self, data):
        self.text.append(data)
        for item in self._open_list_items:
            item["text"].append(data)

    def handle_endtag(self, tag):
        if tag == "li" and self._open_list_items:
            item = self._open_list_items.pop()
            self.list_items.append(
                {"hrefs": item["hrefs"], "text": " ".join(item["text"]).casefold()}
            )


class PortfolioTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        page_path = DIST / "index.html"
        styles_path = DIST / "styles.css"
        if not page_path.exists() or not styles_path.exists():
            raise AssertionError("Build the site first: npm run build")
        cls.page = page_path.read_text(encoding="utf-8")
        cls.styles = styles_path.read_text(encoding="utf-8")
        cls.theme_css = theme_css_block(cls.page)
        cls.tokens = {
            theme: theme_tokens(cls.theme_css, theme)
            for theme in ("paper", "sumi", "tokyo", "gruvbox")
        }
        cls.parser = PortfolioMarkup()
        cls.parser.feed(cls.page)
        cls.text = " ".join(cls.parser.text)
        cls.lowered_text = cls.text.casefold()

    def test_page_has_an_accessible_semantic_document_shell(self):
        self.assertIn("<!doctype html>", self.page.lower())
        self.assertRegex(self.page, r'<html\b[^>]*\blang=["\']en["\']')
        self.assertIn('name="viewport"', self.page)
        self.assertIn("<title>", self.page)
        self.assertIn('href="/styles.css"', self.page)

        tags = [tag for tag, _ in self.parser.elements]
        self.assertIn("nav", tags)
        self.assertIn("main", tags)
        self.assertIn("footer", tags)
        self.assertIn("details", tags)
        self.assertEqual(tags.count("h1"), 1)
        self.assertIn('id="main-content"', self.page)
        self.assertIn('href="#main-content"', self.page)

    def test_hero_states_the_verified_public_achievements(self):
        for claim in (
            "290",
            "10",
            "78",
            "1,477",
            "79%",
            "OCA contributor",
        ):
            with self.subTest(claim=claim):
                self.assertIn(claim.casefold(), self.lowered_text)

    def test_first_section_introduces_antonio_with_the_github_avatar(self):
        avatars = [
            attributes
            for tag, attributes in self.parser.elements
            if tag == "img" and attributes.get("class") == "profile-avatar"
        ]
        self.assertEqual(len(avatars), 1)
        avatar = avatars[0]
        self.assertEqual(avatar.get("src"), "/avatar.webp")
        self.assertEqual(avatar.get("alt"), "Antonio David")
        self.assertTrue(avatar.get("width"))
        self.assertTrue(avatar.get("height"))
        self.assertTrue((DIST / "avatar.webp").exists())
        self.assertIn("odoo developer", self.lowered_text)
        self.assertIn("Cuba", self.text)

    def test_focus_pillars_cover_ai_odoo_owl_and_oca(self):
        for pillar in (
            "Odoo modules & migrations",
            "AI delivery",
            "OWL interfaces",
            "OCA & review",
        ):
            with self.subTest(pillar=pillar):
                self.assertIn(pillar.casefold(), self.lowered_text)

        hrefs = [
            attributes.get("href", "")
            for tag, attributes in self.parser.elements
            if tag == "a"
        ]
        for href in (
            "https://github.com/antoniodavid/odf-agent-team",
            "https://github.com/antoniodavid/hacking-owl",
            "https://github.com/antoniodavid/osem",
        ):
            with self.subTest(href=href):
                self.assertIn(href, hrefs)

    def test_featured_projects_match_the_verified_public_stack(self):
        for name in (
            "ODF Agent Team",
            "odoo.nvim",
            "OSEM",
            "Conecta",
            "Omarchy Agents",
            "Hacking OWL",
        ):
            with self.subTest(project=name):
                self.assertIn(name.casefold(), self.lowered_text)

        for language in ("TypeScript", "Lua", "Go", "QML", "Python"):
            with self.subTest(language=language):
                self.assertIn(language.casefold(), self.lowered_text)

        self.assertNotIn("odoo language server", self.lowered_text)

    def test_oca_ledger_links_every_merged_change_and_the_open_review(self):
        expected = {
            "https://github.com/OCA/delivery-carrier/pull/1079",
            "https://github.com/OCA/delivery-carrier/pull/1082",
            "https://github.com/OCA/stock-logistics-reporting/pull/404",
            "https://github.com/OCA/bank-statement-import/pull/864",
            "https://github.com/OCA/l10n-spain/pull/4083",
            "https://github.com/OCA/partner-contact/pull/1728",
            "https://github.com/OCA/pos/pull/1309",
            "https://github.com/OCA/reporting-engine/pull/968",
            "https://github.com/OCA/reporting-engine/pull/969",
            "https://github.com/OCA/website/pull/1095",
        }
        for href in expected:
            with self.subTest(merged_pull_request=href):
                item = next(
                    (item for item in self.parser.list_items if href in item["hrefs"]),
                    None,
                )
                self.assertIsNotNone(item, f"missing contribution row for {href}")
                self.assertIn("merged", item["text"])

        billcom_url = "https://github.com/OCA/l10n-usa/pull/166"
        billcom_item = next(
            (item for item in self.parser.list_items if billcom_url in item["hrefs"]),
            None,
        )
        self.assertIsNotNone(billcom_item, "Bill.com #166 must be explicitly listed")
        self.assertIn("open for review", billcom_item["text"])
        self.assertNotIn("merged", billcom_item["text"])
        self.assertNotIn("lead architect", billcom_item["text"])

    def test_oca_summary_and_teamwork_counts_are_visible(self):
        for claim in (
            "37",
            "19",
            "10",
            "53",
            "26 repositories",
            "22 authors",
        ):
            with self.subTest(claim=claim):
                self.assertIn(claim.casefold(), self.lowered_text)

    def test_bright_palette_keeps_text_contrast(self):
        paper = self.tokens["paper"]
        pairs = (
            ("ink", "bg"),
            ("ink", "surface"),
            ("ink", "card"),
            ("ink", "yellow"),
            ("ink", "green-soft"),
            ("ink", "coral-soft"),
            ("ink", "blue-soft"),
            ("ink", "purple-soft"),
            ("on-blue", "blue"),
            ("on-blue", "blue-deep"),
            ("bg", "ink"),
            ("contact-muted", "contact-bg"),
        )
        for foreground, background in pairs:
            with self.subTest(foreground=foreground, background=background):
                self.assertGreaterEqual(
                    contrast_ratio(
                        css_color(paper, foreground),
                        css_color(paper, background),
                    ),
                    4.5,
                )

        for foreground, background in (
            ("blue-deep", "blue-soft"),
            ("green-deep", "green-soft"),
            ("coral-deep", "coral-soft"),
            ("purple", "purple-soft"),
            ("ink-2", "bg"),
        ):
            with self.subTest(foreground=foreground, background=background):
                self.assertGreaterEqual(
                    contrast_ratio(
                        css_color(paper, foreground),
                        css_color(paper, background),
                    ),
                    4.5,
                )

    def test_audited_accessibility_fixes_hold(self):
        brand = next(
            (
                attributes
                for tag, attributes in self.parser.elements
                if tag == "a" and attributes.get("class") == "brand"
            ),
            None,
        )
        self.assertIsNotNone(brand)
        self.assertIn("AD Antonio David", brand.get("aria-label", ""))

        brand_markup = re.search(r'<a class="brand".*?</a>', self.page, re.DOTALL)
        self.assertIsNotNone(brand_markup)
        self.assertRegex(
            brand_markup.group(0),
            r"AD</span>\s+<span",
            "keep a space between the brand mark and the brand text",
        )

        self.assertIsNotNone(
            re.search(
                r"\.flagship\s*\{[^}]*border:\s*var\(--bw\)\s+solid\s+var\(--line\)",
                self.styles,
                re.DOTALL,
            ),
            "the flagship project should use the theme border tokens",
        )
        self.assertIsNotNone(
            re.search(
                r"\.terminal\s*\{[^}]*background:\s*var\(--terminal\)",
                self.styles,
                re.DOTALL,
            ),
            "the proof terminal should use the dark terminal surface",
        )

    def test_styles_support_responsive_keyboard_and_reduced_motion_use(self):
        self.assertTrue(self.styles.strip(), "The site stylesheet should exist.")
        self.assertIn(":focus-visible", self.styles)
        self.assertIn("prefers-reduced-motion", self.styles)
        self.assertIn("@media", self.styles)
        self.assertNotIn("transition: all", self.styles.lower())

        self.assertNotRegex(
            self.styles,
            r"\.profile-card\s*\{[^}]*order:\s*-1",
            "the hero copy must stay before the profile card on narrow screens",
        )
        self.assertNotRegex(
            self.styles,
            r"h1 mark\s*\{[^}]*white-space:\s*nowrap",
            "the highlighted headline must be allowed to wrap on small phones",
        )
        self.assertRegex(
            self.styles,
            r"h1\s*\{\s*font-size:\s*clamp\(1\.8rem, 9vw, 2\.9rem\)",
            "the narrow-screen headline must fit a 320px viewport",
        )
        self.assertRegex(
            self.styles,
            r"\.hero-proof\s*\{[^}]*display:\s*flex",
            "proof stats must wrap between complete value/label pairs",
        )
        self.assertRegex(
            self.styles,
            r"\.hero-proof \.proof-unit\s*\{[^}]*white-space:\s*nowrap",
        )
        self.assertRegex(
            self.styles,
            r"\.site-nav\s*\{[^}]*justify-content:\s*flex-start",
            "tablet navigation must stay grouped instead of stretching full width",
        )
        self.assertRegex(
            self.styles,
            r"@media \(min-width: 60\.0625rem\) and \(max-width: 65rem\)\s*\{\s*\.brand-tagline\s*\{\s*display:\s*none",
            "the header tagline must yield before the navigation wraps near 1024px",
        )
        self.assertRegex(
            self.styles,
            r"\.site-nav\s*\{[^}]*gap:\s*0\.4rem",
            "the five navigation labels must stay on one row at 320px",
        )

    def test_dark_themes_keep_text_contrast(self):
        pairs = (
            ("ink", "bg"),
            ("ink", "card"),
            ("ink-2", "bg"),
            ("blue-text", "bg"),
            ("blue-text", "card"),
            ("on-blue", "blue"),
            ("btn-fg", "btn-bg"),
            ("green-deep", "green-soft"),
            ("coral-deep", "coral-soft"),
            ("purple", "purple-soft"),
            ("blue-deep", "blue-soft"),
            ("contact-muted", "contact-bg"),
            ("contact-fg", "contact-bg"),
            ("terminal-text", "terminal"),
            ("terminal-muted", "terminal"),
        )
        for theme in ("sumi", "tokyo", "gruvbox"):
            tokens = self.tokens[theme]
            for foreground, background in pairs:
                with self.subTest(theme=theme, foreground=foreground, background=background):
                    self.assertGreaterEqual(
                        contrast_ratio(
                            css_color(tokens, foreground),
                            css_color(tokens, background),
                        ),
                        4.5,
                    )

            for badge in ("yellow", "green", "coral"):
                with self.subTest(theme=theme, badge=badge):
                    self.assertGreaterEqual(
                        contrast_ratio(
                            css_color(tokens, "badge-ink"),
                            css_color(tokens, badge),
                        ),
                        4.5,
                    )

    def test_dark_themes_separate_surfaces_and_borders(self):
        for theme in ("sumi", "tokyo", "gruvbox"):
            tokens = self.tokens[theme]
            with self.subTest(theme=theme):
                self.assertGreaterEqual(
                    contrast_ratio(css_color(tokens, "card"), css_color(tokens, "bg")),
                    1.15,
                    "cards must read as a distinct surface",
                )
                self.assertGreaterEqual(
                    contrast_ratio(css_color(tokens, "line"), css_color(tokens, "card")),
                    1.3,
                    "borders must stay visible against cards",
                )
                self.assertGreaterEqual(
                    contrast_ratio(css_color(tokens, "line"), css_color(tokens, "bg")),
                    1.5,
                    "borders must stay visible against the page",
                )

    def test_header_offers_the_four_palettes_and_the_lab(self):
        self.assertIn('popovertarget="theme-menu"', self.page)
        self.assertIn('id="theme-menu"', self.page)
        self.assertEqual(self.page.count('name="theme-menu"'), 5)
        for theme in ("paper", "sumi", "tokyo", "gruvbox"):
            with self.subTest(theme=theme):
                self.assertIn(f'data-theme="{theme}"', self.page)
                self.assertIn(f'value="{theme}"', self.page)
        self.assertIn('href="/theme/"', self.page)
        self.assertIn('legacy = { light: "paper", dark: "sumi" }', self.page)
        self.assertIn('localStorage.setItem("theme"', self.page)
        self.assertNotIn(
            "◐",
            self.page,
            "the theme control must not rely on a font glyph with no fallback",
        )
        self.assertRegex(self.page, r'class="theme-icon"[^>]*>\s*<svg')
        self.assertRegex(
            self.page,
            r'class="theme-swatch theme-swatch-system"[^>]*>\s*</span>',
        )
        self.assertRegex(
            self.styles,
            r"\.theme-swatch-system\s*\{[^}]*border-radius:\s*50%",
        )

    def test_theme_lab_previews_every_palette(self):
        page = (DIST / "theme" / "index.html").read_text(encoding="utf-8")
        parser = PortfolioMarkup()
        parser.feed(page)
        text = " ".join(parser.text).casefold()

        self.assertRegex(page, r'<html\b[^>]*\blang=["\']en["\']')
        self.assertEqual(page.count('class="theme-card"'), 4)
        self.assertEqual(page.count('class="theme-preview"'), 4)
        self.assertEqual(page.count('class="theme-apply"'), 4)
        self.assertEqual(page.count('name="theme-lab"'), 5)
        self.assertIn("data-theme-status", page)
        self.assertRegex(page, r"<dd>\d+\.\d:1</dd>")

        for theme, name in (
            ("paper", "Paper"),
            ("sumi", "Sumi"),
            ("tokyo", "Tokyo Night"),
            ("gruvbox", "Gruvbox"),
        ):
            with self.subTest(theme=theme):
                self.assertIn(f'data-theme="{theme}"', page)
                self.assertIn(name.casefold(), text)

        self.assertIn('href="/es/theme/"', page)
        self.assertIn('href="/"', page)

    def test_spanish_theme_lab_is_translated(self):
        page = (DIST / "es" / "theme" / "index.html").read_text(encoding="utf-8")
        self.assertRegex(page, r'<html\b[^>]*\blang=["\']es["\']')
        for claim in (
            "Cuatro paletas",
            "Usar este tema",
            "Seguir al sistema",
            "Se guarda en este navegador",
        ):
            with self.subTest(claim=claim):
                self.assertIn(claim.casefold(), page.casefold())
        self.assertIn('href="/es/"', page)
        self.assertIn("https://antoniodavid.github.io/es/theme/", page)
        self.assertIn("https://antoniodavid.github.io/theme/", page)

    def test_editor_chrome_adds_a_gutter_statusline_and_diagnostics(self):
        self.assertEqual(self.page.count('class="line-no"'), 6)
        for number in ("01", "02", "03", "04", "05", "06"):
            with self.subTest(line=number):
                self.assertIn(
                    f'class="line-no" aria-hidden="true">{number}</span>',
                    self.page,
                )

        self.assertEqual(self.page.count('class="diag diag-merged"'), 10)
        self.assertEqual(self.page.count('class="diag diag-open"'), 1)
        self.assertIn('class="statusline" aria-hidden="true"', self.page)
        self.assertIn('class="status-mode">NORMAL</span>', self.page)
        self.assertIn("data-status-theme", self.page)

        for selector in (".line-no", ".statusline", ".diag-merged", ".diag-open"):
            with self.subTest(selector=selector):
                self.assertIn(selector, self.styles)

        self.assertIn("@media (min-width: 78rem)", self.styles)

    def test_terminal_types_with_a_reduced_motion_fallback(self):
        self.assertEqual(self.page.count('class="terminal-line"'), 5)
        self.assertEqual(self.page.count('class="terminal-cursor"'), 5)
        self.assertIn("IntersectionObserver", self.page)
        self.assertIn('prefers-reduced-motion: reduce', self.page)
        self.assertIn('terminal.classList.add("is-typing")', self.page)

        self.assertIn(".terminal-cursor", self.styles)
        self.assertIn("animation: terminal-blink", self.styles)
        self.assertIn(".terminal-line.is-typing .terminal-cursor", self.styles)
        self.assertRegex(
            self.styles,
            r"\.terminal-cursor\s*\{\s*animation:\s*none !important;",
        )

    def test_theme_tokens_are_present_on_every_page(self):
        for relative in (
            "index.html",
            "es/index.html",
            "theme/index.html",
            "es/theme/index.html",
        ):
            page = (DIST / relative).read_text(encoding="utf-8")
            block = theme_css_block(page)
            with self.subTest(page=relative):
                for theme in ("paper", "sumi", "tokyo", "gruvbox"):
                    self.assertIn(f'[data-theme="{theme}"]', block)

    def test_spanish_page_is_translated_and_linked(self):
        page = (DIST / "es" / "index.html").read_text(encoding="utf-8")
        parser = PortfolioMarkup()
        parser.feed(page)
        text = " ".join(parser.text)
        lowered = text.casefold()

        self.assertRegex(page, r'<html\b[^>]*\blang=["\']es["\']')
        for claim in (
            "Diseño arquitecturas sólidas",
            "Odoo, AI y OWL",
            "En qué trabajo",
            "Proyectos que mantengo",
            "Mergeado en OCA",
            "Cómo trabajo",
            "necesitas un módulo",
            "antoniodavid8@gmail.com",
        ):
            with self.subTest(claim=claim):
                self.assertIn(claim.casefold(), lowered)

        for href in (
            "https://github.com/OCA/delivery-carrier/pull/1079",
            "https://github.com/OCA/reporting-engine/pull/968",
            "https://github.com/OCA/l10n-usa/pull/166",
        ):
            with self.subTest(href=href):
                self.assertIn(href, page)

        self.assertIn("mergeado", lowered)
        self.assertIn("abierto para review", lowered)
        self.assertIn('hreflang="en"', page)
        self.assertIn('hreflang="es"', page)
        self.assertIn("avatar.webp", page)
        self.assertIn("profile-avatar", page)

    def test_static_page_has_no_remote_scripts_or_remote_styles(self):
        tags = [tag for tag, _ in self.parser.elements]
        self.assertLessEqual(tags.count("script"), 3)
        self.assertNotRegex(self.page, r"<script[^>]+src=")
        es_page = (DIST / "es" / "index.html").read_text(encoding="utf-8")
        self.assertNotRegex(es_page, r"<script[^>]+src=")
        self.assertNotRegex(self.styles.lower(), r"@import\s+url\s*\(")
        self.assertNotRegex(self.styles.lower(), r"url\s*\(\s*[\"']?https?://")


if __name__ == "__main__":
    unittest.main()
