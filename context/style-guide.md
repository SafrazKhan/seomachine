# Doorware Style Guide

Editorial and formatting standards for Doorware: product copy, guides, meta fields, and LLM-generated merchandising text. Pair with `@context/brand-voice.md` and `@context/seo-guidelines.md`.

**LLM header (global style)**:

```text
Use US English. Prefer sentence case for headings in prose and UI where the platform allows. Express dimensions in US inches with standard fractional inch notation (e.g. 2-3/8"). Be authoritative, technical, and plainspoken—no retail hype. Do not use: amazing, luxurious, perfect, beautiful, cheap, stunning, game-changer (and similar empty superlatives). Active voice where possible; short sentences in merchandising blocks.
```

---

## Grammar & mechanics

### Capitalization

**Headlines & subheadings (site and long-form)**:
- **Sentence case** for blog/guide H2/H3 unless a brand line requires title case (e.g. vendor series name exactly as trademarked).
- Product titles on PDPs: follow `@context/.archive/release-v1/brand/products.md` pattern when still authoritative—function and material first, then finish/series/SKU as needed.

**Brand and vendor names**:
- **Doorware**: capitalize; “Doorware” not “doorware” in customer-facing copy.
- **Vendor/series**: Match manufacturer spelling and casing (e.g. series names on packaging).

**Industry terms**:
- **door / Door**: lowercase “door” in general copy; capitalize in titles per sentence case.
- **BHMA / ANSI**: all caps; spell out on first use in long-form if audience is mixed: “Builders Hardware Manufacturers Association (BHMA).”
- **SEO / URL / SKU / PDP**: OK without expansion for trade-heavy copy; expand for beginner guides.

### Numbers

**Inches and measurements**:
- Always use numerals with inch marks: `2-3/8"`, `1-3/4"` (match orchestrator: standard US inch formatting).
- Spell out fractions in running copy when cleaner: “two and three-eighths inch backset” is acceptable once per section if paired with numeral form elsewhere.

**Counts and quantities**:
- Use numerals for counts 10+; numerals for dimensions, SKU fragments, and specs regardless of size.

**Money**:
- `$199` or `$199.00` per storefront convention; be consistent sitewide.

### Punctuation

**Oxford comma**: Yes (A, B, and C).

**Em dashes**: Use for aside—`—`—sparingly; or hyphen for compound modifiers (“marine-grade”).

**Quotation marks**: Prefer curly quotes in marketing copy where the CMS supports them; straight quotes acceptable in JSON/CSV.

**Inch marks**: Use `"` for inches, not doubled prime, in plain text/Markdown when required for clarity.

### Abbreviations & acronyms

**First use in guides**:
- Spell out with acronym in parentheses for mixed audiences (e.g. “Americans with Disabilities Act (ADA)” when relevant to hardware selection).

**Common hardware terms** (define on first use in consumer-facing guides):
- **Backset**: distance from door edge to center of bore.
- **Handing**: LH/RH/LHR/RHR as industry standard abbreviations after one plain-language sentence if needed.

**Latin**:
- Prefer plain English over “e.g./i.e.” in customer copy; acceptable in internal or technical notes.

---

## Word choice & usage

### Preferred terms

**Say this** → **Not that**
- Deadbolt, lever, handleset, passage, privacy, keyed entry → vague “lock thing,” “door thing”
- Backset, bore, strike → “hole position” without teaching the term
- Finish (e.g. satin stainless) → “color” when “finish” is industry-accurate
- Solid brass / grade / marine **when in data** → “premium quality” with no spec
- Verify prep / confirm compatibility → “works for every door”

### Words to avoid (align with automation)

Avoid in merchandising prose: **amazing, luxurious, perfect, beautiful, cheap, stunning, game-changer**, and similar hype. Avoid unqualified “best,” “strongest,” “most secure” unless tied to a cited standard or test in source data.

### Inclusive language

- Use gender-neutral job titles (“installer,” “property manager”).
- Avoid idioms that do not translate for international readers on global-facing pages.

---

## Formatting standards

### Text emphasis

- **Bold**: rare emphasis, subheads in rich text where supported—not every keyword.
- *Italics*: product line names or titles when style guide requires; sparingly.
- **ALL CAPS**: SKU fragments or manufacturer-mandated strings only—not full sentences.

### Lists

- **Bullets**: Parallel structure; sentence case; period only if each item is a full sentence.
- **Feature lines (PDP)**: `Benefit: Detail` or `Benefit — Detail` consistently per channel.
- **Numbered**: ordered steps (measure, verify, install).

### Links

- Descriptive anchors: “measure backset for your entry door” not “click here.”
- External links to codes or manufacturer docs when citing requirements—accurate URLs only.

### Code & technical

- Inline SKUs, model strings: monospace or plain per theme; consistent with JSON pipelines (`sku`, `legacy_product_id` immutable).

---

## Content structure

### Product description (AI + human)

1. What it is + primary application.
2. Fit: backset, thickness range, function, handing if relevant.
3. Material / durability / environment **when sourced**.
4. Short selection note (finish, keying, trim) **when options exist in data**.

### Blog / guide introduction

1. Problem or measurement mistake hook.
2. What the reader will know or do after reading.
3. Optional credibility only when factual (years sourcing, testing protocol—no fabrication).

### Conclusion

- Recap 3 points max + one concrete next step (measure, compare functions, open collection).

---

## SEO-specific style (Doorware)

- **Meta titles**: ~50–60 characters for articles; product titles per `@context/seo-guidelines.md` pipeline rules.
- **Meta descriptions**: complete sentences; 150–160 characters for articles; product per JSON rules.
- **Slugs**: lowercase, hyphens; include primary phrase; avoid stop-word bloat.

---

## Dates & time

- **Publication**: “April 9, 2026” or ISO in front matter per CMS.
- **Time zones**: specify for events or limited offers only.

---

## Statistics & claims

- Cite manufacturer specs, code excerpts, or lab results—never invent.
- Year-stamp volatile stats (“as of 2026”) when relevant.

---

## Images & media

- **Alt text**: describe hardware and context (“single-cylinder deadbolt in satin nickel on exterior door”)—125 characters or fewer when possible.
- **File names**: descriptive, hyphenated (`marine-grade-deadbolt-satin-nickel.jpg`).

---

## Brand-specific guidelines

### Doorware references

- First person plural optional for brand voice (“we stock,” “we publish specs”)—keep factual.
- Do not imply Doorware **manufactures** unless true; prefer “carries,” “lists,” “sells.”

### Competitors

- Name only when useful (comparison guides); factual, no mudslinging.
- Prefer differentiation by **data quality and assortment clarity**.

---

## Voice & tone reminders

1. Technical first, sales second.
2. Confident, plainspoken, accurate.
3. Helpful to trade and retail simultaneously.
4. No hype; specs and application win.

---

## Editing checklist

- [ ] Measurements in US inches consistently
- [ ] No forbidden hype words (pipeline list + brand list)
- [ ] Claims traceable to product data or cited sources
- [ ] Terminology: function, backset, finish used correctly
- [ ] Meta lengths within SEO guidelines
- [ ] Links descriptive; internal links to collections/PDPs where useful

---

**Style guide version**: 1.0 (Doorware)  
**Last updated**: April 2026  
**Next review**: Quarterly or when storefront/CMS conventions change
