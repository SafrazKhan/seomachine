# Doorware Writing Examples

Reference copy for Doorware: **product/merchandising** (matches JSON pipelines like `ai_orchestratorv2.py`) and **long-form** placeholders. Replace or extend blog sections with URLs and full articles from your live site as you publish.

**LLM header (what “good” looks like)**:

```text
Doorware copy is authoritative, technical, and plainspoken. Product JSON: two short prose paragraphs (no HTML inside JSON strings), technical_features as benefit+detail pairs grounded in specs, seo_title like [Brand] [Series/Model] [Product Type] - [SKU], seo_description 140-160 chars with keyword and SKU, seo_keyword from provided list only. No hype words: amazing, luxurious, perfect, beautiful, cheap, stunning, game-changer. US inch measurements.
```

---

## A. Product copy exemplars (pipeline-shaped)

These mirror the **intent** of `build_json_prompt` output (structure only—always tie live JSON to real `product_data`).

### Example A1: Deadbolt (fictional illustrative SKU)

**Context**: Use only when similar facts exist in source data; do not copy claims onto unrelated SKUs.

**`prose_paragraphs` (plain text before `<p>` wrap)**:

1. "Round single-cylinder deadbolt in marine-grade 316 stainless steel for exterior doors in coastal and high-moisture environments. Single-cylinder function provides keyed access outside and thumbturn operation inside for typical residential entry prep."
2. "Fits doors prepared for `2-3/8"` or `2-3/4"` backset with a `2-1/8"` cross bore; confirm thickness and strike alignment against your existing setup before installation."

**`technical_features`** (benefit + detail):

| Benefit | Detail |
|--------|--------|
| Marine-grade 316 stainless body | Alloy selected for salt-air corrosion resistance when used as specified by the manufacturer for exterior applications. |
| Adjustable backset latch | Accommodates common `2-3/8"` and `2-3/4"` residential preps without re-drilling the door edge when prep matches standard dimensions. |
| Single-cylinder entry function | Keyed cylinder outside with interior thumbturn—pair with local code requirements for egress paths. |

**SEO (illustrative)**:

- `seo_title`: `[Vendor] Coastal Round Single Cylinder Deadbolt - DWD-RDB316SS` (verify length)
- `seo_description`: `Marine 316 stainless deadbolt (DWD-RDB316SS). Keyed exterior, thumbturn interior; fits 2-3/8" or 2-3/4" backset. Verify door prep before install.` (re-count characters for production)
- `seo_keyword`: chosen from **provided** `text.seo.keywords` list only (e.g. `marine grade deadbolt` if present in list)

---

### Example A2: Handleset (illustrative)

**`prose_paragraphs`**:

1. "Entry handleset combines exterior grip and deadbolt for residential front doors where a one-piece trim layout is preferred. Finish and trim profile should match companion levers or deadbolts in the same collection when coordinating multiple openings."
2. "Confirm backset, door thickness, and handing with the manufacturer’s template; use stated strike and latch specifications when replacing an existing unit."

**`technical_features`**:

| Benefit | Detail |
|--------|--------|
| Coordinated entry trim | Grip, cylinder, and interior lever or knob on a common mounting platform per series design—verify compatibility with related SKUs in the same line. |
| Single-cylinder configuration | Keyed access outside with interior thumbturn on the deadbolt where code allows—double-check egress rules for your jurisdiction. |

---

## B. Blog / guide examples (to be filled from production)

Add **3–5 published articles** when available. For each, paste metadata and full Markdown/HTML from the CMS.

### Example B1: [Article title — TBD]

**URL**: [https://doorware.com/...]  
**Primary keyword**: [e.g. how to measure door backset]  
**Word count**: [~X words]  
**Publication date**: [Month Day, Year]

**Why it’s strong**:
- [Specific reason: e.g. step-by-step measurement photos]
- [Reason 2: aligns with assortment (links to deadbolt collection)]
- [Reason 3: schema/FAQ or clear internal links]

**Full content**:

```markdown
[Paste complete article here when published.]
```

---

### Example B2: [Article title — TBD]

**URL**: […]  
**Primary keyword**: […]  
**Word count**: […]  
**Publication date**: […]

**Why it’s strong**:
- […]
- […]
- […]

**Full content**:

```markdown
[Paste complete article here.]
```

---

### Example B3: [Article title — TBD]

**URL**: […]  
**Primary keyword**: […]  
**Word count**: […]  
**Publication date**: […]

**Why it’s strong**:
- […]
- […]
- […]

**Full content**:

```markdown
[Paste complete article here.]
```

---

## C. Short-form snippets (category intros, email)

Use the same voice as `@context/brand-voice.md`.

**Collection intro (example)**:

> Marine-grade and coastal-rated hardware in this collection is selected for exterior exposure where materials matter. Compare finish, function, and backset options on each PDP—start from your door prep measurements, not from aesthetics alone.

**What makes it work**: Technical priority, clear next step (measure prep), no hype.

---

## Tips for selecting future blog examples

1. Mix **how-to** (measurement, installation) with **selection** (function types, finishes).
2. Include at least one piece targeting **commercial intent** (collection or product category).
3. Prefer posts with stable rankings or strong engagement—paste updated versions when refreshed.
4. Keep examples aligned with **current** brand voice (technical-first).

---

**Remember**: For merchandising JSON, **accuracy beats eloquence**—if a fact is not in `product_data`, leave it out.
