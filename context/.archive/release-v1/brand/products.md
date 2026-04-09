## Doorware Product Semantics & PDP Rules

This file defines how Doorware products should be named, categorized, and presented on the storefront — especially on product detail pages (PDPs).

---

## 1. Product taxonomy

### 1.1 Core hardware families

- **Deadbolts**
  - Single cylinder, double cylinder, one‑sided, etc.  
  - Often used with matching levers or handlesets.
- **Lever sets / knob sets**
  - Passage, privacy, keyed entry, dummy.  
  - Interior vs exterior usage.
- **Handlesets**
  - Front‑door entrance sets (single cylinder, double cylinder, dummy).  
  - With matching interior trim.
- **Hinges & pivots**
  - Residential butt hinges, ball bearing hinges, heavy‑duty, specialty.  
  - Exterior vs interior ratings.
- **Sliding and specialty hardware**
  - Barn door kits, pocket door hardware, multipoint lock trim, etc.

These families should be reflected consistently in Shopify `product_type`, collections, and navigation labels.

---

## 2. Product naming conventions

### 2.1 PDP title pattern

For most products, use:

> **Function**, key spec or material, finish, series/brand, SKU (optional)

Examples:

- “Round Single Cylinder Marine Grade 316 Stainless Steel Deadbolt, DWD‑RDB316SS”  
- “Square Lever Set for Interior Doors, Satin Stainless Steel”  
- “Entry Handleset with Deadbolt, Marine Grade 316 Stainless Steel”.

### 2.2 Collection titles

- Prefer **plain language + function**:
  - “Marine Grade 316 Deadbolts”  
  - “Coastal Exterior Door Hardware”  
  - “Stainless Steel Hinges for Exterior Doors”.

---

## 3. PDP information hierarchy

### 3.1 Above the fold (right column)

In order:

1. **Product title** and brand.  
2. **Key highlights**:
   - Function (deadbolt, lever, hinge, handleset).  
   - Material and finish (e.g. “Marine Grade 316 stainless steel, Satin finish”).  
   - Environment / rating (coastal, exterior, interior, grade).  
3. **Pricing**:
   - Retail price and compare‑at price if relevant.  
   - Contractor price (when logged in) clearly labeled.  
4. **Configuration controls**:
   - Door thickness range.  
   - Backset (2‑3/8\" or 2‑3/4\"; multipoint specifics where applicable).  
   - Keying (keyed alike, keyed different, keyway, supplied keys).  
   - Handing (LH, RH, LHR, RHR) if needed.  
   - Finish selection (if more than one finish is available via options).  
5. **Add‑to‑cart and trust messaging**:
   - Add to cart, quantity.  
   - Short shipping/lead time note and corrosion/warranty reassurance.

### 3.2 Below the fold

Content should appear in this order:

1. **Description**  
   - 2–4 paragraphs giving use‑case context and benefits.  
   - Bullet list of core features (security, durability, install, compatibility).
2. **Specifications** (tables)
   - Grouped tables pulled from structured metafields where possible:  
     - Material & finish (e.g. Marine Grade 316 stainless, Satin Stainless Steel).  
     - Dimensions & fit (door thickness range, backset, bore size, projection, rose size).  
     - Included components (latch, strike, screws, trim rings, keys).  
     - Certifications & ratings (Grade, UL, fire rating, salt‑spray tests if applicable).
3. **Documents & resources**
   - Links to PDFs: install instructions, templates, spec sheets, CAD files.  
4. **Related / matching products**
   - Matching levers, hinges, handlesets, companion SKUs in the same finish or series.

---

## 4. Specification rules

### 4.1 Door thickness and backset

- Always express door thickness as a **range** with units:  
  - `1‑3/8\" to 2‑3/4\"` instead of “fits standard doors”.  
- Backset must be explicit:
  - `2‑3/8\" or 2‑3/4\" adjustable` or `fixed 2‑3/8\"`.  
- If a thick‑door kit is required above a threshold, call it out in the description and specs.

### 4.2 Material and finish

- Material field:
  - Use precise descriptions: “Marine Grade 316 stainless steel”, “Solid brass”, “Zinc alloy”.  
- Finish field:
  - Use finish names consistently across products (e.g. “Satin Stainless Steel”, “Oil Rubbed Bronze”).  
- If a product’s key value is corrosion resistance, mention “Marine Grade 316” in:
  - Title, highlights, and first spec table.

### 4.3 Keying and security

- Always list:
  - Keyway (e.g. “5‑pin Schlage C keyway”).  
  - How many keys are supplied.  
  - Whether products can be keyed alike/different and how to request it.
- Where applicable, include:
  - Security grade (e.g. “Grade 1 ANSI/BHMA”).  
  - Hardened inserts or other anti‑tamper features.

---

## 5. Related products behavior

- **Goal**: help customers complete the opening, not just buy one SKU.

### 5.1 What to show

- Matching or coordinating:
  - Handlesets and interior levers.  
  - Deadbolts that pair with passage or privacy sets.  
  - Hinges and accessories in the same finish/material.  
- Limit to **4–8 items** in a clean horizontal row or side‑scroll.

### 5.2 Rules

- Prioritize:
  - Same series and finish.  
  - Same function family (e.g. all deadbolts) when cross‑selling upgrades.  
  - Practical companions (hinges with door‑mounted hardware, latches with trim).

---

## 6. Data sources (for agents and backend)

- **Structured specs** should come from:
  - Parsed `descriptionHtml` specs block (as described in the product specs plan).  
  - Normalized metafields (e.g. `dw_specs.material`, `dw_specs.finish`, `dw_specs.door_thickness_min/max`, `dw_specs.backset`, `dw_specs.function`).  
  - Option‑derived metafields (e.g. `dw_options.door_thickness_options`, `dw_options.keying_options`).
- PDP templates should **prefer these structured fields** over scraping text out of the long description.

---

## For agents (implementation notes)

- When creating or modifying PDP templates:
  - Follow the **information hierarchy** in section 3.  
  - Use **structured metafields** where possible for spec tables and badges.  
  - Keep key specs (material, finish, door thickness, backset, keying) readily visible above the fold.
- When naming products, ensure titles are:
  - Descriptive of function and key spec.  
  - Consistent across the site for similar hardware.  
- When configuring related products, prioritize **useful, project‑oriented companions** in matching finishes over random upsells.

