## Doorware brand voice (production)

Doorware copy should sound like a senior door hardware specialist: precise, practical, and trustworthy.
It should help both contractors and homeowners make the right decision quickly, without hype.

---

## 1) Core voice rules

- **Technical first, sales second**
  - Lead with fit, function, compatibility, and durability.
  - Mention style/finish as support, not the main point.

- **Confident and plainspoken**
  - Use direct language and short sentences.
  - Avoid fluff, exaggeration, and vague superlatives.

- **Accurate and grounded**
  - Only state facts present in source data.
  - Do not invent standards, certifications, dimensions, or compatibility.

- **Helpful to trade and retail**
  - Explain why a detail matters ("2-3/8\" or 2-3/4\" backset fits common residential prep.").
  - Keep terms professional but readable.

---

## 2) Scope for Step1c / Claude Desktop copywriting

When used for pipeline generation, this voice file applies to AI-authored text fields only:

- `text.description_html`
- `text.features`
- `text.seo_title_ai`
- `text.seo_description_ai`
- `text.seo_focus_keyword`

Do not rewrite, regenerate, or mutate these fields in LLM output:

- `legacy_product_id`
- `sku`
- `parsed_specs`
- `spec_sections`
- `resources`

Those are handled by deterministic Python transforms.

---

## 3) SEO usage policy

- Use `text.seo.title`, `text.seo.description`, and `text.seo.keywords` as guidance.
- Integrate high-intent terms naturally; do not keyword-stuff.
- Keep copy readable first, SEO second.
- Keep brand and SKU references factual and relevant. using existing fields 'product_data.core.sku' and vendor

SEO output style:

- 2-4 short paragraphs in `text.description_html` using HTML `<p>` tags only.
- 6-8 concise `text.features` bullets using:
  - `Benefit - practical explanation`
- `text.seo_title_ai`: 45-60 chars preferred (max 70)
- `text.seo_description_ai`: 135-160 chars preferred (max 170)
- `text.seo_focus_keyword`: must be one exact keyword from `text.seo.keywords` input

---

## 4) Product page writing pattern

For each product:

1. Start with what it is and where it is used.
2. Add core functional fit details (backset, thickness, prep compatibility, function type).
3. Reinforce material/performance value (security, durability, fire/corrosion context if provided).
4. End with concise selection guidance (function/finish/trim choices when relevant).

Do not:

- Dump raw specs in paragraph form.
- Repeat full spec tables as prose.
- Include document links inside narrative bullets.

---

## 5) Tone examples

Prefer:

- "Solid brass construction for long-term durability in high-use entry applications."
- "Fits 2-3/8\" or 2-3/4\" backset, supporting standard residential door prep."
- "Single-cylinder function provides keyed exterior access with interior thumbturn operation."

Avoid:

- "This amazing set is perfect for every home."
- "Top quality craftsmanship with unbeatable elegance."
- "Fits most doors" (too vague).

---

## 6) Formatting and style standards

- Sentence case throughout.
- Keep paragraphs compact and scannable.
- Use US English and inch formatting like `2-3/8\"`.
- Keep feature bullets parallel in structure.
- Prefer concrete nouns and measurable facts over adjectives.

---

## 7) Agent checklist before final output

Before finalizing LLM copy:

- Verify no fabricated claims.
- Verify no links appear in `text.description_html` or `text.features`.
- Verify no mutation of specs/resources/id fields.
- Verify tone is practical, professional, and non-hype.

If uncertain, reduce claims and stay factual.

---

## 8) Step1c output contract (ai_content schema)

For ai generation in `backend-python/production/ai_content/ai_<legacy_id>.json`, keep a strict separation:

- `text`: AI-authored output fields
- `text_raw`: source provenance copied from `backend-python/production/output/output_<legacy_id>.json`

Required `text` fields:

- `description_html` (rewritten narrative only)
- `features`
- `seo_title_ai`
- `seo_description_ai`
- `seo_focus_keyword`

Required `text_raw` fields:

- `description_html_input` (primary source; exact input text)
- `seo_title_input`
- `seo_description_input`
- `seo_keywords_input_csv`

Guardrails:

- The primary rewrite source is always `product_data.text.description_html`.
- `text.seo_focus_keyword` must be selected from `text_raw.seo_keywords_input_csv` (no invented focus terms).
- Do not rewrite deterministic fields such as specs/resources/id/sku in LLM output.

