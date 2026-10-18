---
layout: default
title: "Foundations"
parent: "Admin (AapliAdmin)"
grand_parent: Design Standards
has_children: false
nav_order: 1
permalink: /design-standards/admin/foundations/
---

{% raw %}
# 2. Foundations {#2-foundations}

All tokens are CSS custom properties defined on `:root` in `src/scss/design-system/_tokens.scss`. They are prefixed `--ab-` so they never collide with Bootstrap, Angular Material or the tenant theme variables (`--primaryColor` and so on).

## 2.1 Colour {#21-colour}

![Colour tokens with their values and uses](/assets/images/design-standards/admin/ds-colour.svg)


The admin uses a **fixed brand blue** (`#0062b5`). It does not follow the tenant's theme colour: tenants theme what their users see, not the admin tool. Inside an `.ab-theme` container the legacy `--primaryColor` and `--primaryColorRGBA` variables are re-pointed at the admin blue, so older markup inside a redesigned screen follows along.

### Surfaces and lines {#surfaces-and-lines}

| Token | Value | Use |
|---|---|---|
| `--ab-bg` | `#f4f6f9` | Page background behind the shell; background of tab bodies that hold cards |
| `--ab-surface` | `#ffffff` | Shell, panes, cards, inputs |
| `--ab-surface-2` | `#f8f8f8` | One step down: left nav, section rail, table headers, notes, disabled inputs |
| `--ab-line` | `#e2e6ec` | Every border and divider |
| `--ab-line-strong` | `#cfd5dd` | Hover border on inputs and stroked buttons |

### Text {#text}

| Token | Value | Use |
|---|---|---|
| `--ab-fg` | `#2b2f36` | Body text and headings |
| `--ab-muted` | `#5f6670` | Secondary text, subtitles, hints, inactive tabs and nav items (5.8:1 on white) |
| `--ab-placeholder` | `#8a919b` | Input placeholders only. Never for text people need to read |

### Brand and state {#brand-and-state}

| Token | Value | Use |
|---|---|---|
| `--ab-primary` | `#0062b5` | Primary buttons, active tab, active nav item, links, focus ring, checked controls |
| `--ab-primary-hover` | `#00539a` | Hover on primary buttons |
| `--ab-primary-tint` | `rgba(0,98,181,.10)` | Background of the active nav or rail item, primary chips |
| `--ab-primary-tint-strong` | `rgba(0,98,181,.16)` | Pressed or selected-and-hovered states |
| `--ab-primary-rgb` | `0, 98, 181` | For `rgba(var(--ab-primary-rgb), x)` when another alpha is needed |
| `--ab-on-primary` | `#ffffff` | Text and icons on primary |
| `--ab-danger` / `--ab-danger-tint` | `#c62828` / `rgba(198,40,40,.08)` | Errors, invalid fields, destructive hover |
| `--ab-ok` / `--ab-ok-tint` | `#2e7d32` / `rgba(46,125,50,.10)` | Success, "on" status, HTTP method labels |
| `--ab-warn` / `--ab-warn-tint` | `#8a5300` / `rgba(237,160,0,.12)` | Warnings that need attention but do not block |

### Code {#code}

| Token | Value |
|---|---|
| `--ab-code-bg` | `#0f1b2a` |
| `--ab-code-fg` | `#d6e4f5` |
| `--ab-code-key` | `#7cc4ff` |
| `--ab-code-str` | `#a5d6a7` |

**Rules**

- Text on `--ab-surface` or `--ab-surface-2` uses `--ab-fg` or `--ab-muted`. Nothing lighter.
- Status is never shown by colour alone. Pair it with text or an icon (for example "Export to IF tab: shown" next to a green dot).
- Tints are backgrounds only. Do not put tinted text on a tinted background of the same hue except in chips, where the text uses the full-strength colour.
- Dark mode is not supported yet. The prototype's dark values are kept in the prototype for reference. When it is added, it will be a second set of token values only; no component should need changing, which is another reason never to hard-code colours.

## 2.2 Typography {#22-typography}

![Type scale](/assets/images/design-standards/admin/ds-type.svg)


| Token | Value |
|---|---|
| `--ab-font-ui` | `"Roboto", system-ui, -apple-system, "Segoe UI", sans-serif` |
| `--ab-font-mono` | `"Roboto Mono", ui-monospace, Consolas, monospace` |

Both are loaded from Google Fonts in `src/index.html` (Roboto 300/400/500/700, Roboto Mono 400/500).

### Type scale {#type-scale}

| Role | Token | Size | Weight | Line height | Notes |
|---|---|---|---|---|---|
| Workspace title (app bar `h1`) | `--ab-text-page` | 18px | 500 | 1.25 | Full-screen editors only (form builder) |
| **Admin page title** (`h2.ab-title`) | `--ab-text-section` | **17px** | **500** | 1.25 | First line of every admin screen; see [3.6](/design-standards/admin/layout/#36-page-frame-and-title) |
| Admin page description (`p.ab-sub`) | `--ab-text-body` | 14px | 400 | 1.5 | Under the page title, `--ab-muted`, full width of the section |
| Sub-heading (`.ab-subtitle`) | `--ab-text-body` | 14px | 500 | 1.5 | Groups inside a section |
| Body | `--ab-text-body` | 14px | 400 | 1.5 | Default for everything |
| Mono input / code | `--ab-text-mono` | 13px | 400 | 1.5 | Keys, IDs, expressions |
| Small | `--ab-text-sm` | 12px | 400 | 1.45 | Hints, errors, counts, chips, status |
| Overline (`.ab-overline`, `th`) | `--ab-text-overline` | 11px | 500 | 1.4 | UPPERCASE, `letter-spacing: .06em` |
| Badge | — | 10px | 500 | 1.6 | UPPERCASE, `letter-spacing: .06em` |

**Rules**

- **500 is the only emphasis weight** in UI: headings, active items, buttons. Use 700 (`<b>`) only inside running prose such as notes.
- Never use 300 (light) or 100 for text.
- Subtitles and descriptions (`.ab-sub`, panel and section descriptions) run the full width of their section. Only notes (`.ab-note`) keep a 70ch cap.
- Headings use `text-wrap: balance`.
- Sentence case everywhere: "Custom properties", not "Custom Properties". (Existing screen names are being migrated; new text must be sentence case.)
- Mono is for machine values: keys, IDs, endpoints, expressions, JSON. Not for emphasis.

## 2.3 Spacing {#23-spacing}

![Spacing scale, radius and icon sizes](/assets/images/design-standards/admin/ds-spacing-shape.svg)


A 4px grid. Use the tokens; a value off the grid needs a comment.

| Token | Value | Typical use |
|---|---|---|
| `--ab-space-0` | 2px | Gap between stacked nav or rail items |
| `--ab-space-1` | 4px | Label to input, title to subtitle |
| `--ab-space-2` | 8px | Between buttons in a toolbar, icon to text in dense rows |
| `--ab-space-3` | 12px | App bar vertical padding, table cell horizontal padding |
| `--ab-space-4` | 16px | Page gutter, field to field, note padding |
| `--ab-space-5` | 20px | App bar and action bar horizontal padding |
| `--ab-space-6` | 24px | Pane top padding |
| `--ab-space-7` | 28px | Pane side padding, gap between pane and aside |
| `--ab-space-8` | 32px | Large separations |

Fixed component paddings that come from the prototype (and are already in the classes, so you do not repeat them): nav and rail items `9px 12px`; inputs `7px 9px`; buttons `7px 14px`; table header cells `8px 12px` (36px row), body cells `6px 12px` (40px row, see [Row height](/design-standards/admin/tables/#row-height)); main tabs `12px 14px`.

## 2.4 Shape, borders and elevation {#24-shape-borders-and-elevation}

| Token | Value | Use |
|---|---|---|
| `--ab-radius-sm` | 4px | Inputs, buttons, nav and rail items, tables, notes, code, cards |
| `--ab-radius-md` | 6px | The framed shell |
| `--ab-radius-pill` | 10px | Chips |

- Borders are always `1px solid var(--ab-line)`.
- Separation comes from borders and the `bg` / `surface` / `surface-2` steps, **not shadows**. The only shadows allowed are the ones Angular Material puts on overlays (menus, dialogs, tooltips).
- A selected card gets a 3px inset bar on its left in `--ab-primary` (see [Cards](/design-standards/admin/chips-cards/#67-cards--ab-card)).

## 2.5 Icons {#25-icons}

- **Material Icons** (filled), as already loaded by the app. Use `<mat-icon>` or `<span class="material-icons">`.
- Sizes: `--ab-icon` (20px) by default; `--ab-icon-sm` (16px) in overlines and dense metadata.
- Icons sit to the left of their label with a 6–10px gap. Chevrons and "open" arrows sit on the right.
- **Icons take the colour of the text around them** (`color: inherit` inside `.ab-theme`): white on a primary button, red in a danger menu item, primary in an active tab. Never let the app-wide `.mat-icon { color: var(--iconColor) }` paint an icon dark grey on a coloured background. Give an icon its own colour only for meaning (a green check in a list of what an app adds).
- Decorative icons get `aria-hidden="true"`. An icon-only button must have `aria-label` and a tooltip.
- One icon means one thing across the admin. Current assignments:

| Concept | Icon |
|---|---|
| Add | `add` |
| Remove / delete row | `delete_outline` |
| Save | `save` |
| Preview | `visibility` |
| Close | `close` |
| Search | `search` |
| Back / next | `arrow_back` / `arrow_forward` |
| Expand group | `expand_more` (rotates 180° when open) |
| Collapse / expand nav | `menu_open` / `menu` |
| API / endpoint | `api` |
| Success toast | `check_circle` |
| Locked / not available | `lock` |
| Form builder tabs | Settings `settings` · Form `design_services` · Request workflow `account_tree` · Response workflow `alt_route` · Tasks `assignment` · Dashboard `space_dashboard` |
| Settings rail | Application settings `tune` · Information `info` · Views `dashboard` · Roles and permissions `security` · Other settings `settings` · Points `star` · AI features `smart_toy` · Integrations `integration_instructions` · Custom properties `data_object` |

## 2.6 Motion {#26-motion}

- `--ab-duration: .2s` with `--ab-ease: cubic-bezier(.2, 0, 0, 1)` for colour, border and small transforms (chevrons, nav width).
- No entrance animations on page content. Tabs switch instantly (`animationDuration="0ms"`).
- Everything respects `prefers-reduced-motion: reduce`; the shared stylesheet turns transitions off inside `.ab-theme`.

## 2.7 Layering {#27-layering}

| Token | Value | Use |
|---|---|---|
| `--ab-z-sticky` | 20 | Sticky action bars and headers |
| `--ab-z-toast` | 1000 | Toasts |

Exception: the form builder footer keeps `z-index: 9999`, because the Design and Workflow canvases stack their own layers high. Do not copy this elsewhere.

## 2.8 Breakpoints {#28-breakpoints}

| Width | Behaviour |
|---|---|
| > 1100px | Pane and aside side by side |
| ≤ 1100px | Aside drops below the pane |
| ≤ 760px | Section rail becomes a horizontal scrolling row above the pane; pane padding reduces to `18px 14px`; app bar chips are hidden |

The admin is a desktop tool, but nothing may scroll horizontally at page level at any width. Wide tables scroll inside `.ab-table-wrap`.
{% endraw %}
