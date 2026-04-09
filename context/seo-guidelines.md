# SEO Guidelines for Doorware Content

SEO rules for Doorware span **product and merchandising copy** and **long-form guides or blog content** (secondary). Read `@context/brand-voice.md` for voice; this file covers structure, lengths, and search mechanics.

---

## LLM prompt alignment (product copy pipeline)

Use the following as the canonical framing when building prompts for JSON product copy (local LLM or API). Mirror tags if your stack wraps XML-style sections.

### Persona

```text
You are a senior door hardware copywriter and technical SEO expert. Your writing is authoritative, highly technical, and plainspoken. You write for architects, contractors, and informed homeowners. Do not use marketing fluff.
```

### Input schema (logical sources)

Paths are relative to the inner `product_data` object (e.g. from `output_*.json`):

- `core.sku`, `core.title`, `core.vendor`
- `text.description_html` (plain text from paragraph body only—spec blocks, also-available, sizes, and images stripped)
- `text.seo.keywords`
- `filters.filter_options` (secondary—purchase/configuration choices)
- Optional: `text.specifications`—when present, **verbatim**; authoritative for core facts

### Global rules

1. **Tone**: Authoritative, technical, and plainspoken.
2. **No hype**: Write like a senior architectural hardware consultant—not retail fluff.
3. **Formatting**: Standard US inch formatting (e.g. `2-3/8"` or `1-1/4"`).
4. **Accuracy**: Rely **only** on provided product data. Do not hallucinate features, certifications, or dimensions.
5. **Source priority**: Align prose and SEO with core identity and description. When canonical specifications (verbatim) are present, treat them as authoritative for facts and dimensions. Use filter options only as secondary context for purchase/configuration; do not invent finishes, trims, or keying not implied there.

### SEO rules (JSON output fields)

1. **SEO title (`seo_title`)**: Prefer `[Brand] [Series/Model] [Product Type] - [SKU]`. Target **maximum ~65 characters** (orchestrator QA flags outside ~30–75; tune to channel).
2. **SEO description (`seo_description`)**: **140–160 characters**. Include the main keyword, the **SKU**, and end with a technical specification or a precise next-step CTA (verify fit, confirm backset, etc.).
3. **SEO keyword (`seo_keyword`)**: Select the single most search-relevant, high-intent keyword from the **provided** keyword list—do not invent a focus term.

### JSON output expectations (reference)

- Output **strict JSON** only—no markdown fences, no conversational wrapper.
- **Do not** put HTML tags inside JSON string values for `prose_paragraphs` (downstream wraps in `<p>`).
- `technical_features`: array of objects with short **benefit** + **detail** (detail grounded in specs/description).

### QA and guardrails (automation)

- **Forbidden words** in prose (example list—extend in code as needed): `amazing`, `luxurious`, `perfect`, `beautiful`, `cheap`, `stunning`, `game-changer`.
- **Prose**: Minimum length checks may apply; final HTML must include `<p>` wrappers after assembly.
- **Title length**: Keep within bounds your job enforces (e.g. ~30–75 characters for review routing).

---

## Product page (PDP) and AI merchandising SEO

### Title and meta

- **Primary pattern**: Brand + product type + differentiator + SKU when space allows—see persona SEO rules above.
- **Uniqueness**: Every PDP title unique; avoid duplicate titles across SKUs.
- **Accuracy**: Title must match what the product **is** (function, series, material when stated)—not aspirational marketing.

### Meta description

- One clear value line + fit/function cue + SKU + technical hook or CTA within 140–160 characters.
- **Do not** stuff keywords; readability and truthfulness first.

### Focus keyword

- Must be chosen **only** from supplied `text.seo.keywords` (CSV or list)—pipeline should resolve/validate focus against input.

### Body copy and bullets

- **Paragraphs**: Short, 2–4 `<p>` blocks typical; lead with what it is, where it’s used, then fit (backset, thickness, function), then materials/performance when data supports.
- **Feature bullets**: `Benefit: detail` or `Benefit — detail`; parallel structure; no links inside bullets unless the channel explicitly allows.
- **Specs**: Verbatim structured specs win over marketing paraphrase when both exist.

### Structured data

- Use product schema where platform supports it (name, SKU, brand, offers, `aggregateRating` only if real).
- Follow `@context/brand-voice.md` for claims—no invented ratings or certifications.

---

## Educational / blog content (Doorware)

Use when publishing guides (installation, code basics, selection, coastal/corrosion topics). Product PDP rules above still apply to **tone and accuracy**; length and heading rules below are tuned for articles.

### Content length

- **Standard article**: ~1,500–2,500 words when the topic needs depth.
- **Pillar / comprehensive**: up to ~4,000 words; split into a series if longer.
- **News or short updates**: ~800–1,200 words.
- Prefer **density over padding**—do not add words to hit a quota.

### Keyword practice

- One **primary** keyword per URL; 3–5 supporting phrases where natural.
- **Natural language first**—no robotic repetition. Use variants: “deadbolt,” “bore,” “backset,” “entry set.”
- **Placement**: Primary keyword in title (H1), introduction, at least one H2, and conclusion where it reads naturally; meta title and description; URL slug.

### Structure

- Single **H1**; logical **H2** / **H3** hierarchy; no skipped levels.
- Introduction: problem or question → what the reader will learn → credibility only when true (e.g. sourcing, testing).
- Conclusion: recap + specific next step (measure prep, compare functions, see collection).

### Meta (blog)

- **Meta title**: ~50–60 characters when possible; primary keyword near the front; optional `| Doorware` if space allows.
- **Meta description**: ~150–160 characters; benefit + keyword + CTA; complete sentences.
- **Slug**: lowercase, hyphens, 3–6 words, primary keyword.

### Internal linking

- Link to relevant category/collection pages and flagship PDPs using descriptive anchors (“marine-grade exterior deadbolts,” not “click here”).
- Maintain `@context/internal-links-map.md` when that file is populated for Doorware.

### External linking

- Cite standards bodies, manufacturers’ technical docs, or code references when making claims about ratings or compliance—only when accurate.

### Readability

- Aim for clear, plain language; define terms like **backset**, **handing**, **function** on first use for mixed audiences.
- Short paragraphs (2–4 sentences) for mobile scanning.

---

## Checklist: product JSON / PDP copy

- [ ] Facts match `text.specifications` and description—no invented dimensions or certs
- [ ] SEO title format and length within pipeline limits
- [ ] Meta description 140–160 characters with keyword, SKU, technical/CTA close
- [ ] Focus keyword from provided list only
- [ ] No forbidden hype words in assembled prose
- [ ] Feature bullets grounded; parallel structure
- [ ] Filter options used only as allowed configuration context

## Checklist: blog article

- [ ] Primary keyword chosen; no cannibalization against stronger existing URL without a plan
- [ ] H1/H2 structure logical; scannable sections
- [ ] Meta title and description unique and complete
- [ ] Internal links to relevant Doorware pages where helpful
- [ ] Sources for statistics or code-related claims

---

**Remember**: Search visibility follows **trust**. For Doorware, accurate fit-and-function copy outperforms keyword-stuffed blurbs.
