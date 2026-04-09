# Doorware Features & Benefits

This document summarizes what Doorware **is** (a door hardware–focused retailer and catalog), what customers get, and how to describe capabilities in marketing and LLM context—without inventing SaaS-style “features” that do not exist.

**LLM header (context for generation)**:

```text
Doorware sells architectural and residential door hardware (deadbolts, levers, handlesets, hinges, specialty sliding/pocket/barn hardware, and related trim). Copy must stay technical-first: fit, function, material, environment (interior/exterior/coastal), and verifiable specs. Audience: architects, contractors, property managers, and informed homeowners. Do not claim services or guarantees not stated in source data.
```

---

## Core value propositions

### 1. **Specs-first merchandising**
- **What it is**: Product pages organized around function, prep compatibility (e.g. backset, thickness), material/finish, and application—not vague lifestyle copy.
- **Benefit**: Fewer wrong orders; faster verification on the job site or at the kitchen table.
- **Conversion angle**: “Know the backset and function before you buy—clear copy and structured specs for every SKU we publish.”

### 2. **Breadth across core hardware families**
- **What it is**: Curated assortment spanning deadbolts, lever and knob sets, entry handlesets, hinges and pivots, and specialty hardware (e.g. barn, pocket, multipoint-related trim) aligned to `@context/brand-voice.md` and product taxonomy.
- **Benefit**: One place to match trim, function, and finish across openings when the catalog carries compatible lines.
- **Conversion angle**: “Shop by function and environment—from interior passage to coastal-rated exterior.”

### 3. **Trade- and DIY-friendly clarity**
- **What it is**: Language that works for contractors (dense facts) and homeowners (plain explanations of why prep matters).
- **Benefit**: Less friction between “what I need” and “what I’m ordering.”
- **Conversion angle**: “Same product truth for pros and retail—no dumbing down, no hype.”

### 4. **Coastal and environment-aware selection (where stocked)**
- **What it is**: When data supports it, SKUs call out marine-grade materials, exterior ratings, and corrosion-relevant context—**only** as stated in vendor or structured data.
- **Benefit**: Appropriate hardware for salt-air and high-moisture installs without guesswork.
- **Conversion angle**: “Match hardware to environment when our listings document grade and material—verify against your job conditions.”

### 5. **Contractor-aware commerce (when enabled)**
- **What it is**: Pricing or programs that recognize pro buyers (e.g. contractor pricing when logged in)—describe only what the storefront actually implements.
- **Benefit**: Repeatable ordering for crews and PMs.
- **Conversion angle**: “Pro pricing where available—see cart and account for current rules.”

### 6. **AI-assisted catalog enrichment (internal pipeline)**
- **What it is**: JSON pipelines (e.g. `ai_orchestratorv2.py`) generate `description_html`, feature bullets, and SEO fields from `product_data` under strict guardrails—verbatim specs override prose.
- **Benefit**: Scalable, consistent technical tone without inventing certifications.
- **Conversion angle**: Not customer-facing as a “feature name”—use only in internal/docs context.

---

## Technical / catalog capabilities (grouped)

### Product data and PDPs
- **Structured specs**: Key-value or parsed specs drive factual bullets and compatibility language.
- **Configurable options**: Finishes, backset, handing, keying—**only** when present in `filters.filter_options` or equivalent; never invent variants.
- **SKU integrity**: SKU, vendor, and legacy IDs are deterministic—never rewritten by LLM passes.

### Categories and navigation
- **Hardware families**: Deadbolts; levers/knobs; handlesets; hinges/pivots; sliding and specialty—consistent labels in collections and `product_type` (see `@context/.archive/release-v1/brand/products.md` if still canonical).
- **Plain-language collection titles**: Function + environment (e.g. coastal exterior, marine-grade stainless) where assortment supports it.

### Trust and accuracy
- **No hallucinated standards**: ANSI/BHMA, fire, or life-safety claims only when present in source data.
- **Inch measurements**: US fractional inch style in copy (e.g. `2-3/8"`).

---

## Integrations & ecosystem

Doorware is not a middleware SaaS product. Replace “integrations” with **commerce and data** touchpoints:

- **Ecommerce platform** (e.g. Shopify): cart, checkout, inventory, and merchandising fields.
- **PIM / feed sources**: Vendor or ERP-derived `product_data` JSON driving descriptions and specs.
- **Search**: On-site search and filters should respect same taxonomy as collections (function, finish, brand, environment).

---

## Competitive differentiation (positioning, not trash talk)

### vs. generic big-box listings
- **Clearer function and prep language** tied to real specs.
- **Less lifestyle fluff**—more compatibility-oriented copy when data allows.

### vs. purely wholesale catalogs
- **Retail-friendly explanations** without dropping technical accuracy.
- **SKU-level pages** suitable for search and sharing—when SEO fields are filled per `@context/seo-guidelines.md`.

### vs. undocumented marketplaces
- **Consistent naming and spec presentation** per internal guides; fewer “mystery” listings.

---

## Use cases by segment

### Contractors and installers
- Need: correct backset, function, handing, keying, and material for job conditions.
- Messaging: lead with fit, then durability and code/rating context **only if sourced**.

### Homeowners and DIY
- Need: confidence they’re ordering the right replacement or new install set.
- Messaging: one-line “why this detail matters” (e.g. backset measurement) + link to how-to content when available.

### Designers and architects (light commercial / residential)
- Need: series consistency, finish coordination, documented performance language.
- Messaging: material, grade, and aesthetic support **after** function is correct.

### Property maintenance / facility buyers
- Need: repeatability, keyed-alike options when offered, documented SKUs.
- Messaging: SKU, brand line, and replacement path clarity.

---

## Pricing & offers

Document **actual** Doorware policies here as they evolve (tiers, pro pricing, shipping thresholds). Do not invent discounts or warranties in LLM copy—pull from live site or legal pages only.

---

## Key messaging for conversions

### High-intent PDP CTAs
- “Add to cart—verify backset and function against your door prep.”
- “Confirm finish and keying options on the product page before checkout.”
- “Questions on compatibility? Use stated specs and vendor line name to match existing hardware.”

### Pain → response
- **“I ordered the wrong backset.”** → Teach measurement upfront in guides; PDP copy repeats critical prep dimensions when data exists.
- **“Is this rated for exterior/coastal?”** → Only state what specs or vendor copy support; otherwise defer to manufacturer documentation.
- **“Does this match my existing handleset?”** → Same series/finish/vendor alignment when catalog data allows; otherwise avoid implying compatibility without evidence.

### Social proof (use only if true and current)
- Replace placeholder stats with real figures: years in business, SKUs live, verified reviews aggregate, trade accounts served.

---

## Common questions (content hooks)

### “What backset do I need?”
**Answer**: Measure from door edge to center of the bore; common residential preps are often `2-3/8"` or `2-3/4"`. Always match what your door is drilled for.

### “Single vs double cylinder?”
**Answer**: Single-cylinder: key outside, thumbturn inside. Double-cylinder: keyed both sides—know local code restrictions for egress paths.

### “Marine grade vs standard stainless?”
**Answer**: Use environment-appropriate materials when specs document grade (e.g. 316 for harsh coastal)—do not extrapolate beyond source data.

---

## Content creation guidelines (Doorware)

1. **Lead with fit and function**, then material and finish—see `@context/brand-voice.md`.
2. **Use specific examples**: real inch sizes, function names, series names when in data.
3. **Proof points**: standards and ratings **only** when cited from vendor/spec.
4. **Objections**: compatibility and code—answer conservatively.
5. **CTAs**: verify prep, compare functions, add to cart—no vague “learn more” without destination.
6. **Differentiation**: accuracy and clarity—not superlatives.
7. **Audience**: tune depth for pro vs DIY in guides; PDPs serve both with scannable structure.

---

*Update when assortment, platforms, or pro programs change. Keep aligned with `brand-voice.md` and SEO pipeline rules.*
