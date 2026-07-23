# PDF Quality Audit — SASIDHAR_RESUME.pdf

## 1. Audit Method

This audit checks the generated PDF of `SASIDHAR_RESUME.html` for the items a recruiter or hiring manager notices in the first 10 seconds of opening it:

- One-page fit
- Font rendering
- Margins and alignment
- Section hierarchy
- Link formatting
- Print color consistency
- ATS text extraction safety

## 2. Current PDF Status

The existing `SASIDHAR_RESUME.pdf` (6,073 bytes) is stale and does not reflect the latest content or design changes. It must be regenerated from `SASIDHAR_RESUME.html` before distribution.

## 3. Corrections Already Applied to `SASIDHAR_RESUME.html`

The following changes were made to improve PDF output:

| Item | Before | After |
|---|---|---|
| Print margins | 10mm / 12mm | 8mm top/bottom, 10mm left/right (`@page`) |
| Body font size | 10pt | 9.5pt |
| Body line height | 1.45 | 1.35 |
| Name size | 30pt | 26pt |
| Section bottom margin | 10px | 8px |
| Heading font size | 11pt | 10pt |
| Heading bottom margin | 7px | 5px |
| Cert grid styling | plain two-column | subtle left-accent pills |
| Page-break behavior | none | `page-break-inside: avoid` on every section, job, project, and cert grid |
| Semantic ATS name | `<div class="name">` | `<h1 class="name">` |
| Print padding | `.page` padding persisted in print | `.page` padding removed in `@media print` |

## 4. PDF Generation Guide

### Recommended tools

1. **Chrome / Edge (best font fidelity)**
   - Open `SASIDHAR_RESUME.html` in the browser.
   - `Ctrl + P` → Destination: **Save as PDF**.
   - Margins: **None**.
   - Enable **Background graphics** if you want the subtle fills.
   - Save as `SASIDHAR_RESUME.pdf`.

2. **Playwright / Puppeteer (programmatic)**
   ```bash
   # Node example
   npx playwright open SASIDHAR_RESUME.html
   # Then print to PDF or use page.pdf()
   ```

3. **weasyprint / wkhtmltopdf (CLI)**
   ```bash
   weasyprint SASIDHAR_RESUME.html SASIDHAR_RESUME.pdf
   # or
   wkhtmltopdf --page-size A4 --margin-top 8 --margin-bottom 8 --margin-left 10 --margin-right 10 SASIDHAR_RESUME.html SASIDHAR_RESUME.pdf
   ```

### Must-check list after generation

- [ ] File is exactly **one page**.
- [ ] No section splits across pages.
- [ ] Name and role are at the top; no orphans.
- [ ] Certification pills are not clipped.
- [ ] Skill grid does not wrap awkwardly.
- [ ] Project URLs are visible and not truncated.
- [ ] No font substitution artifacts (e.g., Times New Roman fallback).
- [ ] File size is under 500 KB for email attachment.

## 5. Known PDF Risks to Avoid

| Risk | Cause | Fix |
|---|---|---|
| Two-page bleed | Content too long / margins too big | Reduce font or trim bullets; use `@page` margins above |
| Clipped right edge | `.page` width 210mm plus body margins | Set `@page` margins and remove `.page` padding in print |
| Broken links | PDF printer not preserving hyperlinks | Use Chrome print with default link handling enabled |
| Faded text in print | Light gray body text on white | Keep `--muted` at `#475569` or darker |
| ATS cannot read headers | Using images or CSS-only content | Keep `<h1>`, `<h2>`, and real text; no critical content in `::before`/`::after` |

## 6. One-Page Target Verification

If the generated PDF is still two pages, trim in this order:

1. Shorten the professional summary to two lines.
2. Remove the least relevant certification (keep Databricks + DP-700 top).
3. Collapse the three projects into one compact section (title, one-line stack, one impact bullet each).
4. Reduce skill rows to four categories.

## 7. Final PDF Action

1. Regenerate `SASIDHAR_RESUME.pdf` from the updated `SASIDHAR_RESUME.html`.
2. Rename the old PDF or replace it in the `Portfolio` repo.
3. Update the `README.md` badge if needed (it already points to the HTML resume).
4. Upload the PDF to LinkedIn, Naukri, and attach it to recruiter outreach.
