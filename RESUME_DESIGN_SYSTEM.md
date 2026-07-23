# Resume Design System — One-Page ATS-Safe Layout

## 1. Page Geometry

- **Page size:** A4 (210mm × 297mm)
- **Print margins:** 8mm top/bottom, 10mm left/right (`@page { size: A4; margin: 8mm 10mm; }`)
- **Content padding:** 0 on screen; all spacing handled by `@page` margins
- **Target page count:** exactly one page
- **Reflow rule:** avoid widows and orphans; every section has `page-break-inside: avoid;`

## 2. Typography

### Font

- **Primary:** `Inter` 400/500/600/700 from Google Fonts
- **Fallback:** `-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif`
- **Body size:** 9.5pt (0.5pt smaller than the current version to recover vertical space)
- **Line height:** 1.35 for bullets, 1.25 for headings and single-line metadata

### Scale

| Element | Size | Weight | Case / Style |
|---|---|---|---|
| Name | 26pt | 700 | Sentence case, letter-spacing -0.5px |
| Role | 12pt | 600 | Title case, color `--accent` |
| Certification badge | 8pt | 700 | Uppercase, white on `--accent` |
| Section headings | 10pt | 700 | Uppercase, letter-spacing 1.2px, underline 1px `--rule` |
| Job / project titles | 10.5pt | 700 | Title case |
| Body / bullets | 9.5pt | 400 | Sentence case, max two lines per bullet where possible |
| Metadata / tech tags | 8.5pt | 400 | `--muted` color, no italic |
| Skills labels | 9pt | 600 | `--ink` color |
| Skills items | 9pt | 400 | `--muted` color, comma-separated |

## 3. Color Palette

- `--ink`: #0F172A (near-black for body and headings)
- `--accent`: #2563EB (blue for role, links, title accents)
- `--muted`: #475569 (secondary text, tags, metadata)
- `--rule`: #CBD5E1 (light slate for dividers)
- `--bg`: #FFFFFF
- `--subtle`: #F1F5F9 (lightest fill for badges/cert rows)

## 4. Section Hierarchy

Order is tuned for recruiter scanning:

1. **Header** — name + role + cert badge + contact row
2. **Professional Summary** — one tight paragraph with value and stack
3. **Certifications** — compact visible row of verified certs (high trust)
4. **Technical Skills** — five category rows, two-column grid
5. **Experience** — one employer, 5-7 metric bullets
6. **Projects** — three projects, one-line tagline + 2-3 bullets each
7. **Education** — one line + JEE note

## 5. Header Layout

- Name as `<h1>` for semantic ATS priority
- Role on same visual line as the cert badge, separated by `1fr auto` flex
- Contact as a single horizontal row: city | email | phone | LinkedIn | GitHub | Portfolio
- Use `|` separators with 12px horizontal gaps
- No extra blank lines under header; bottom border is 2px `--accent`

## 6. Certification Visibility

Use a responsive grid that feels like a row of credentials, not a wall of text:

- 3-column grid on desktop, wrapping on narrow screens
- Each cert rendered as a subtle pill/row with a left accent bar
- Verification links included in the PDF text; keep cert name bold and issuer + date muted
- Leading with Databricks + DP-700 because they are the strongest hiring signals

## 7. Project Readability

Each project block is compact and identical:

```
Project Title — github.com/... (muted link, right-aligned)
Stack: ... (muted)
- Impact metric in bold, then explanation.
- Second bullet.
```

- No extra spacing between title and sub-line
- Use `display: flex; justify-content: space-between;` for title + repo URL
- Bullets use `compact-list` with 2pt bottom margin

## 8. Spacing Rules

- Header bottom border and padding: `border-bottom: 2px solid var(--accent); padding-bottom: 6px; margin-bottom: 10px;`
- Section bottom margin: `8px`
- Section heading bottom margin: `5px`
- Bullet bottom margin: `2px`
- Last bullet in a section: `margin-bottom: 0`
- Paragraph margin: `0 0 4px 0`

## 9. ATS / Accessibility Compatibility

- All content inside semantic tags: `<header>`, `<section>`, `<h1>`, `<h2>`, `<ul>`, `<li>`
- No reliance on CSS-only generated content for critical information
- Links are real `<a href>`; print styles remove underlines but keep text
- Avoid `display: grid` for the entire page layout; use it only for skill grid and cert grid
- Ensure text color contrast ratios exceed 4.5:1 (`#0F172A` on `#FFFFFF` and `#2563EB` on `#FFFFFF`)

## 10. Print Behavior

```css
@media print {
  body { background: #fff; }
  .page {
    width: 100%;
    margin: 0;
    padding: 0;
    box-shadow: none;
    min-height: auto;
  }
  a { color: var(--ink); text-decoration: none; }
  section { page-break-inside: avoid; }
}
```

## 11. PDF Generation Checklist

When converting `SASIDHAR_RESUME.html` to PDF:

- Use Chrome / Edge `Print → Save as PDF` with margins set to **None** (CSS handles margins)
- Or use `paged-cli` / `weasyprint` with the same `@page` rule
- Verify no clipping on the right edge
- Verify one page only; if overflow, reduce summary word count or project bullets first
- Check font rendering: Inter must load; if printing offline, embed fonts via `wkhtmltopdf` or local font files
- Verify link URLs are not truncated; print preview should show full addresses or rely on the HTML digital resume
