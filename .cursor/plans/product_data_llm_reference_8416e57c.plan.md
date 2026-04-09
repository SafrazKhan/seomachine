---
name: Product data LLM reference
overview: Add a single markdown reference under `context/` that documents the Doorware `output_*.json` product envelope, field-by-field semantics, and LLM-safe usage rules, using [doorware/products/output/output_10002.json](doorware/products/output/output_10002.json) as the concrete example.
todos:
  - id: draft-schema-md
    content: "Author context/product-data-schema.md: envelope, product_data sections, option_sets, LLM rules, example pointer, diagram"
    status: pending
  - id: optional-claude-md
    content: Optionally add CLAUDE.md Context Files bullet linking to product-data-schema.md
    status: pending
isProject: false
---

# Doorware product data schema (LLM reference doc)

## Goal

Create **`context/product-data-schema.md`** (name can be adjusted to `context/doorware-product-data-schema.md` if you prefer explicit naming) so agents and pipelines have one authoritative, human-readable map of the JSON shape—aligned with real files like [`doorware/products/output/output_10002.json`](doorware/products/output/output_10002.json).

## What the doc will cover

### 1. File envelope (root)

Document the four top-level keys visible in the example:

| Area | Purpose |
|------|--------|
| `legacy_product_id` | Stable id string; **immutable** in LLM outputs (same rule as existing [`context/brand-voice.md`](context/brand-voice.md) pipeline section). |
| `sync_state` | Operational: `needs_update`, `sync_status`, `last_synced`—not for merchandising copy. |
| `product_data` | Primary blob for titles, copy, SEO, specs, filters—this is what [`context/seo-guidelines.md`](context/seo-guidelines.md) refers to as paths under `product_data`. |
| `option_sets` | **Sibling of `product_data`**, not nested inside it: Shopify-style options (`Dropdown`, `label`, `choices[]` with `price_impact`, `weight_impact`, optional `image` / `sku_ref`). Call out that some pipelines pass only the inner `product_data` dict to prompts; `option_sets` may need explicit merging if the LLM should reason about variant-level pricing. |

Include a small **mermaid** diagram: `Root` → `legacy_product_id`, `sync_state`, `product_data`, `option_sets`.

### 2. `product_data` (schema_version 2)

- **`core`**: `title`, `vendor`, `status` (e.g. `ARCHIVED` / `ACTIVE`), `sku`, `mpn`, `price`, `compare_at_price`, `contractor_price`, `shipping_weight`, `tags[]`, `image_url_original`, `image_url_shopify`—note stringly-typed prices as in the example.
- **`text`**: `description_html` (rich HTML), `seo.title` / `seo.description` / `seo.keywords` (keywords as comma-separated string in the example), `specifications[]` as `{ key, value }` pairs mirroring spec content.
- **`filters`**: `product_type`, `google_category`, `taxonomy_node_id`, `collections[]` (`name`, `sort`), `related_products[]` (`legacy_product_id`, `sort`), `filter_options[]` as **flattened strings** (mix of spec lines and purchasable options like finish, trim, handing, keying—matches lines 145–168 in `output_10002.json`).

### 3. LLM-oriented rules (concise, actionable)

Mirror and cross-link existing guidance without duplicating full brand prose:

- **Source priority**: `text.specifications` (and verbatim spec blocks) over marketing adjectives in `description_html` when facts conflict; `filters.filter_options` for **purchase/configuration** choices; do not invent finishes/options not implied there (consistent with [`context/seo-guidelines.md`](context/seo-guidelines.md) “global rules”).
- **Do not hallucinate**: standards (e.g. ANSI/BHMA), dimensions, warranties—only what appears in source fields.
- **Fields typically immutable for LLM**: `legacy_product_id`, `sku`, structured ids in `related_products`, raw option machinery—generation targets are the usual AI text fields described in brand/SEO docs.

### 4. Example anchoring

- Explicit pointer: **Reference product**: [`doorware/products/output/output_10002.json`](doorware/products/output/output_10002.json) (Kwikset Arlington double-cylinder handleset) with one sentence on why it’s representative (rich `filter_options`, multiple `option_sets`, full `specifications`).

### 5. Optional short appendix

- **Variant coverage**: One paragraph noting that `output_10004.json` (dummy handleset, `ACTIVE`) differs mainly in copy/options—readers can diff for edge cases.
- **Cross-references**: [`context/brand-voice.md`](context/brand-voice.md), [`context/seo-guidelines.md`](context/seo-guidelines.md), and optionally [`CLAUDE.md`](CLAUDE.md) under “Context Files” if you want discoverability.

## Files to add/change

| Action | File |
|--------|------|
| **Add** | [`context/product-data-schema.md`](context/product-data-schema.md) — full content as above. |
| **Optional one-line add** | [`CLAUDE.md`](CLAUDE.md) — bullet under Context Files pointing to the new doc (only if you want it in the default agent path). |

## Out of scope (unless you ask)

- Auto-generating JSON Schema files or codegen.
- Changing Python orchestrators or import paths.
