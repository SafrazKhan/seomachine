## Doorware Design System – 2026 Rebrand

Doorware’s design system is the **single source of truth** for how the brand looks and behaves across the Shopify storefront.  
This document **leads** the theme implementation (it is not just a dump of existing CSS).

Use this file whenever you:

- Design or modify **Shopify sections/snippets**.
- Add new **components** (e.g. product cards, PDP tabs, content blocks).
- Make decisions about **colors, typography, spacing, or motion**.

---

## 1. Brand foundations

- **Positioning**: Premium, architect‑grade hardware for coastal and design‑driven projects.
- **Audience**:  
  - Trade professionals (contractors, builders, designers).  
  - Serious homeowners who care about performance and aesthetics.
- **Mood**: Clean, architectural, coastal‑industrial, technical but approachable.
- **Overall feel**: Similar to high‑end hardware brands (e.g. Riobel / Ferguson PDPs): **large product imagery, lots of white space, restrained color, clear hierarchy.**

---

## 2. Color system

All colors are referenced via **tokens**, not raw hex values, in the theme.

### 2.1 Core palette

These are the neutral inks and surfaces used across the storefront. They are derived from the `doorware-final-product-page.html` reference and should be treated as the canonical values.

| Token                     | Hex      | Usage                                          |
| ------------------------- | -------- | ---------------------------------------------- |
| `color.bg.page`           | `#f8f7f5`| Default page background                        |
| `color.bg.surface`        | `#ffffff`| Cards, content areas, PDP info panels          |
| `color.text.primary`      | `#0f1923`| Primary body text, key PDP copy                |
| `color.text.muted`        | `#64748b`| Secondary text, labels, helper copy            |
| `color.text.inverse`      | `#ffffff`| Text on dark surfaces                          |
| `color.border.subtle`     | `#e2e8f0`| Dividers, card borders, table rows             |
| `color.border.strong`     | `#c2c5cc`| Strong separators (e.g. filter panel outline)  |

### 2.2 Brand accents

These are the Doorware‑specific brand colors layered on top of the neutrals.

| Token                     | Hex      | Usage                                          |
| ------------------------- | -------- | ---------------------------------------------- |
| `color.brand.primary`     | `#9b1c1c`| Primary accent (links, key CTAs, key highlights) |
| `color.brand.primarySoft` | `#fef2f2`| Soft background blocks, badges, subtle callouts|
| `color.brand.secondary`   | `#8b5a3c`| Warm metallic accent (handlesets, luxury feel) |
| `color.brand.highlight`   | `#b45309`| Data/metrics highlights, small UI details      |

These colors should feel **coastal + engineered** (deep blue/graphite neutrals + warm metal and rust accents).

### 2.3 Semantic colors

| Token                      | Hex      | Usage                                 |
| -------------------------- | -------- | ------------------------------------- |
| `color.success`            | `#1c7c4d`| Success messages, “in stock” hints    |
| `color.warning`            | `#c78a1b`| Non‑blocking warnings                 |
| `color.error`              | `#c93838`| Form errors, validation messages      |
| `color.info`               | `#1f7ea8`| Informational notes                    |

Contrast must always meet or exceed accessibility requirements when pairing these with text.

---

## 3. Typography

Typography should feel **precise, minimal, and readable**. Keep the number of different styles small.

### 3.1 Typefaces

- **Display / primary headings**: `'Playfair Display', serif`  
  - Used for logo lockup, hero page titles, and select H1s where we want an architectural, editorial feel.
- **Body / UI / secondary headings**: `'Outfit', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif`  
  - Used for all body copy, labels, buttons, and most H2/H3 headings.

These choices are implemented in the reference PDP (`doorware-final-product-page.html`) and should be mirrored in theme font settings and CSS (global `body` font = Outfit, with specific selectors using Playfair Display where needed).

### 3.2 Type scale

Use rem‑based sizes assuming a base of `16px`.

| Token           | Size   | Weight | Usage                                        |
| --------------- | ------ | ------ | -------------------------------------------- |
| `type.h1`       | 2.5rem | 600    | Page titles, hero headlines                  |
| `type.h2`       | 2.0rem | 600    | Section titles (e.g. “Product specifications”) |
| `type.h3`       | 1.5rem | 500    | Card titles, sub‑section headings           |
| `type.body`     | 1.0rem | 400    | Default body copy                            |
| `type.bodySmall`| 0.875rem| 400   | Meta info, labels, helper text               |
| `type.overline` | 0.75rem| 600    | All‑caps labels above headings (optional)    |

### 3.3 Rules

- **Max line length**: Aim for 60–80 characters per line on desktop content blocks.
- **Line-height**:  
  - Headings: ~1.2–1.3  
  - Body: ~1.5–1.65
- **Capitalization**:
  - Use **Sentence case** for most headings and CTAs.
  - Reserve **ALL CAPS** for short overline labels only.

---

## 4. Spacing & layout

### 4.1 Spacing scale

All padding/margins should use the following steps (in px):  
`4, 8, 12, 16, 24, 32, 40, 48, 64`

Define tokens:

- `space.xs` = 4px  
- `space.sm` = 8px  
- `space.md` = 16px  
- `space.lg` = 24px  
- `space.xl` = 40px+ (depending on context)

### 4.2 Layout containers

- **Max content width**: `1200–1280px` for the main content container.
- **Gutters**:
  - Desktop grids: 24px between columns.
  - Mobile: 16px side padding.
- **Section rhythm**:
  - Standard vertical spacing between major sections: `space.xl`.
  - Reduce to `space.lg` inside nested blocks (e.g. within a card or panel).

### 4.3 Breakpoints

- `sm`: 0–767px (mobile)
- `md`: 768–1023px (tablet)
- `lg`: 1024–1439px (desktop)
- `xl`: 1440px+ (large desktop)

Components must **reflow**, not shrink; prioritize stacked layouts on small screens.

---

## 5. Core components

This section guides how to build key Shopify theme components.

### 5.1 Header & navigation

- **Structure**:
  - Left: logo.
  - Center: primary navigation (3–7 top‑level items).
  - Right: search, account, cart icons.
- **Behavior**:
  - Sticky on desktop when scrolling product/category pages.
  - On mobile, collapsible drawer with clear sections for Shopping vs Help/Guides.
- **Do**:
  - Keep the header visually light (white or `color.bg.surface`) with `color.brand.primary` accents.
  - Make **Search** easy to discover (icon + label or large search in nav on PDPs).
- **Don’t**:
  - Overload the top nav with more than one secondary row of links.

### 5.2 Product card

- **Image**:
  - Consistent aspect ratio (3:4 or 4:5). No randomly cropped heights.
  - Background should be neutral and uncluttered.
- **Content stack** (top → bottom):
  - Product type / overline (optional).
  - Product title (max 2 lines).
  - Key attribute (e.g. finish or collection).
  - Price + contractor price (if applicable).
  - Optional small badges (Sale, New, Marine Grade 316, etc.).
- **Interaction**:
  - Hover: subtle lift or shadow, optional quick “View details”.
  - Never introduce heavy animations; motion should be under 200ms and easing gentle.

### 5.3 Product detail page (PDP)

- **Layout**:
  - Left: gallery (hero image + thumbnails, zoom/lightbox on click).
  - Right:  
    - Title, collection, short spec highlights (material, finish, function).  
    - Pricing (retail + contractor), availability.  
    - Configuration controls (door thickness, keying, etc.).  
    - Add‑to‑cart + trust elements (shipping, returns, warranties).
- **Below the fold**:
  - Tabs or stacked sections for: Description, Specifications, Instructions/Downloads, Related products.
  - Specifications should be in **structured tables** that align with the metafield schema (material, finish, backset, door thickness, etc.).

### 5.4 Collection grid

- Use a **simple grid** (2–4 columns depending on screen size).
- Keep card heights consistent per row; avoid masonry unless a specific layout calls for it.
- Filters and sorting should use the same tokens for borders, spacing, and typography as the rest of the system.

### 5.5 Content / guide blocks

- Max width: keep long‑form content constrained (~720–800px) for readability.
- Layout patterns:
  - **Text + image** split 50/50 or 60/40.
  - Use `space.lg` between paragraphs and `space.xl` between major sections.
- Guides should use the same heading and body tokens as PDP descriptions for consistency.

---

## 6. Buttons & interactive elements

### 6.1 Buttons

- **Primary button** (e.g. “Add to cart”, key CTAs):
  - Background: `color.brand.primary`
  - Text: `color.text.inverse`
  - Border radius: 4–6px (subtle, not pill‑shaped).
  - Hover: slightly darker `color.brand.primary`, same text color.
- **Secondary button**:
  - Background: `transparent`
  - Border: `1px solid color.brand.primary`
  - Text: `color.brand.primary`
  - Hover: light `color.brand.primarySoft` background.
- **Ghost button** (on dark imagery):
  - Background: `transparent`
  - Border: `1px solid color.text.inverse`
  - Text: `color.text.inverse`

### 6.2 Form inputs

- Background: `color.bg.surface`
- Border: `1px solid color.border.subtle`
- Focus: `1px solid color.brand.primary` plus subtle glow using `color.brand.primarySoft`.
- Error: `border-color: color.error`, with small helper text in `color.error`.

---

## 7. Badges, labels & metadata

- Keep badges small and legible; they should **support** the content, not dominate it.
- Examples:
  - `Marine Grade 316`
  - `Contractor exclusive`
  - `New`
  - `Limited stock`
- Use `color.brand.primarySoft` or a subtle neutral background with `color.text.primary` for most badges; reserve bright contrasting backgrounds for rare, important states.

---

## 8. Imagery & iconography

- **Product photography**:
  - Neutral backgrounds, consistent lighting, minimal reflections.
  - Show both **hero product** and, where helpful, context (e.g. installed on a door).
- **Technical diagrams**:
  - Keep them sharp and legible; avoid embedding text that becomes unreadable on mobile.
  - When used, pair with a short caption and a link to full‑size/download (PDF).
- **Icons**:
  - Use a simple, line‑based icon set with consistent stroke width.
  - Limit usage to navigation, statuses, and spec hints (e.g. material, warranty).

---

## 9. Accessibility & motion

- **Color contrast**:
  - All text must meet WCAG AA contrast; large headings should be comfortably readable on backgrounds used.
- **Focus states**:
  - Every interactive element (links, buttons, inputs) must have a clear focus outline or state using `color.brand.primary` or `color.brand.highlight`.
- **Motion**:
  - Keep transitions short (150–200ms).
  - Avoid auto‑advancing carousels or animations that compete with product information.

---

## 10. Token naming & usage conventions

- All theme styles should use **token names** (e.g. `color.brand.primary`, `space.md`, `type.body`) rather than direct hex/px values.
- When adding new tokens:
  - Follow the existing prefixing scheme (`color.*`, `space.*`, `type.*`).
  - Avoid creating one‑off tokens for one component; prefer reusing or extending the core system.

---

## For agents (implementation notes)

- **Always** read this file before creating or modifying Shopify sections/snippets that affect layout or styling.
- **Use tokens**: do not hard‑code colors, font sizes, or spacings; wire CSS/JSON settings to the tokens defined here.
- When building new components:
  - Reuse the **type scale**, **spacing scale**, and **color system** from this document.
  - Align PDPs, collection grids, and cards to the component patterns in section 5.
- If a design choice is not covered here, default to:
  - Simple layouts, generous white space, minimal borders.
  - Hierarchy driven by typography and spacing instead of heavy decoration.

