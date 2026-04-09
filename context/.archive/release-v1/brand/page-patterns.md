## Doorware Page Patterns

This file defines **standard layouts** for key Shopify page types so themes feel consistent and predictable.  
Agents should start here before creating or modifying templates or sections.

---

## 1. Product detail page (PDP)

The competitor example you shared (Riobel faucet PDP) is the reference pattern: **clear gallery, strong spec tables, and related items below**.

### 1.1 Overall layout (top to bottom)

1. **Breadcrumbs & page header**
   - Breadcrumb row with collection path (e.g. “Home → Bath → Faucets → Widespread”).  
   - Product title directly under or next to breadcrumbs.
2. **Primary PDP band (two‑column layout on desktop)**
   - **Left column**: image gallery.  
   - **Right column**: key details and purchase controls.
3. **Detail section**
   - Narrative description (rich text).  
   - One or more spec tables (material, dimensions, installation, included components, etc.).
4. **Expandable sections / accordions**
   - Reviews, Q&A, additional documents as collapsible panels.
5. **Related and complementary products**
   - Horizontal scroller of recommended SKUs (same series, coordinated hardware, etc.).

### 1.2 Primary PDP band: left column (gallery)

- Image area:
  - Hero image in a fixed aspect ratio (3:4 or 4:5).  
  - Thumbnail strip below or to the side; selected state clearly indicated.
- Behavior:
  - Clicking thumbnails changes the hero image.  
  - Optional zoom or lightbox for technical details and finishes.

### 1.3 Primary PDP band: right column (content)

Order (top to bottom):

1. **Product title** and **brand** (if relevant).  
2. **Key highlights** — 3–5 bullet points summarizing:
   - Function (deadbolt, lever, hinge).  
   - Environment (exterior, coastal, interior).  
   - Material / finish and any standout spec (e.g. “Marine Grade 316 stainless steel”).  
3. **Pricing block**
   - Retail price, compare‑at price if applicable.  
   - Contractor price (when logged in) with clear label.  
   - Stock / availability, estimated ship time if known.
4. **Configuration controls**
   - Options derived from `option_sets` / metafields: door thickness, keying, handing, finish, etc.  
   - Each option has:
     - Clear label (“Door thickness”, “Keying”).  
     - Input type (dropdown, radio, swatch) aligned with the design system.  
     - Helper text only when needed.
5. **Add‑to‑cart zone**
   - Quantity selector.  
   - Primary “Add to cart” button.  
   - Secondary actions (Add to list, Ask a question, Download spec sheet).
6. **Trust/support content**
   - Short row for shipping & returns, corrosion resistance claims, warranty summary.  

---

## 2. Collection / category pages

### 2.1 Layout

1. **Hero / header block**
   - Collection title and 1–2 line description explaining what this hardware solves.  
   - Optional background image or subtle illustration.
2. **Filter + sort bar**
   - Left: filters (by function, finish, material, backset, door thickness range, etc.).  
   - Right: sort (Best match, Newest, Price).
3. **Product grid**
   - 2–4 columns depending on screen size.  
   - Each card uses the standard product card pattern from the design system.  
4. **Pager / load more**
   - Standard pagination or “Load more” button; avoid infinite scroll for trade users.

### 2.2 Content guidance

- Use collection descriptions to:
  - Clarify **where** and **why** you’d use this hardware family.  
  - Highlight key shared specs (e.g. “All hardware in this collection is rated for coastal exteriors.”).

---

## 3. Home page

### 3.1 Layout

1. **Hero**
   - Single hero with one strong headline and one CTA (e.g. “Shop Marine Grade 316 Hardware”).  
   - Background image or clean architectural illustration.
2. **Featured categories**
   - 3–6 tiles leading into main product groupings (Deadbolts, Handlesets, Pulls, Hinges, Sliding hardware, etc.).
3. **Featured series or brands**
   - Carousel or grid of highlight collections (e.g. specific stainless series or design lines).
4. **Guides / content**
   - Cards linking to selection guides and hardware education (“Choosing hardware for a coastal home”, etc.).
5. **Social proof / trust**
   - Short row for logos, testimonials, or “Trusted by builders since …”.

---

## 4. Guides & educational pages

### 4.1 Layout

1. **Intro section**
   - Clear problem statement and outcome (“How to choose the right deadbolt for coastal doors.”).
2. **Body sections**
   - H2 sections for major steps, each with text and supporting images/diagrams.  
   - Bulleted checklists for decisions (door thickness, backset, handing, function).
3. **Decision summary**
   - Short recap of what to choose and why.  
   - Links to relevant collections or curated product lists.

---

## 5. Reusable blocks & patterns

- **Spec tables**:
  - Two‑column tables with clear labels on the left and values on the right.  
  - Group by theme: “Material & finish”, “Dimensions & fit”, “Included components”, etc.
- **Accordions / collapsible sections**:
  - Use for secondary content: reviews, Q&A, installation notes, extended documentation.  
  - Keep titles short and descriptive.
- **Related products / matching sets**:
  - Show visually related, practical suggestions: matching handleset, interior levers, hinges in the same finish.

---

## For agents (implementation notes)

- Before editing or creating templates/sections:
  - Identify the **page type** (PDP, collection, home, guide).  
  - Follow the corresponding layout pattern above.
- When implementing a new PDP or changing an existing one:
  - Preserve the **two‑column primary band** (gallery left, details right).  
  - Ensure narrative description + spec tables appear **below** that band, not mixed into it.  
  - Keep related products and extended content **below** specs.
- When in doubt, default to:
  - Simple, linear layouts with clear headings.  
  - Generous white space and standard spacing tokens from `brand/design-system.md`.

