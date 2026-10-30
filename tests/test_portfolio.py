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
            "OCA upstream",
        ):
            with self.subTest(claim=claim):
                self.assertIn(claim.casefold(), self.lowered_text)

    def test_focus_pillars_cover_ai_odoo_owl_and_oca(self):
        for pillar in (
            "Odoo core",
            "AI & agents",
            "OWL frontend",
            "Architecture & review",
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
        pairs = (
            ("ink", "bg"),
            ("ink", "surface"),
            ("ink", "white"),
            ("ink", "yellow"),
            ("ink", "green-soft"),
            ("ink", "coral-soft"),
            ("ink", "blue-soft"),
            ("ink", "purple-soft"),
            ("white", "blue"),
            ("white", "blue-deep"),
            ("bg", "ink"),
            ("contact-soft", "ink"),
        )
        for foreground, background in pairs:
            with self.subTest(foreground=foreground, background=background):
                self.assertGreaterEqual(
                    contrast_ratio(
                        css_color(self.styles, foreground),
                        css_color(self.styles, background),
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
                        css_color(self.styles, foreground),
                        css_color(self.styles, background),
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
                r"\.flagship\s*\{[^}]*border:\s*2px solid var\(--ink\)",
                self.styles,
                re.DOTALL,
            ),
            "the flagship project should carry the ink monograph border",
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

    def test_static_page_has_no_remote_assets_or_unneeded_script(self):
        tags = [tag for tag, _ in self.parser.elements]
        self.assertNotIn("script", tags)
        self.assertNotIn("<script", self.page.lower())
        self.assertNotRegex(self.styles.lower(), r"@import\s+url\s*\(")
        self.assertNotRegex(self.styles.lower(), r"url\s*\(\s*[\"']?https?://")


if __name__ == "__main__":
    unittest.main()
