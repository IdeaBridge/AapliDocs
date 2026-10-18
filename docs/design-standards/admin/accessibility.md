---
layout: default
title: "Accessibility"
parent: "Admin (AapliAdmin)"
grand_parent: Design Standards
has_children: false
nav_order: 20
permalink: /design-standards/admin/accessibility/
---

{% raw %}
# 9. Accessibility {#9-accessibility}

Target: **WCAG 2.2 AA**.

- **Contrast**: body text ≥ 4.5:1 (`--ab-fg` 13.4:1, `--ab-muted` 5.8:1 on white); UI component boundaries ≥ 3:1 where the boundary is the only cue (focus ring and active states use `--ab-primary`, 6.2:1).
- **Focus**: visible 2px `--ab-primary` outline on `:focus-visible`, offset 1px (inset in scroll areas). Never `outline: none` without a replacement.
- **Semantics**: `<nav>` with `aria-label` for the left nav and the section rail; `<header>` and `<footer>` for the app bar and action bar; real `<button>`s and `<a>`s; headings in order (one `h1` in the app bar, `h2` per pane).
- **State**: `aria-current="page"` on the active nav link; `aria-expanded` and `aria-controls` on group headers and the collapse toggle; `aria-selected` on tabs and rail items; `aria-invalid` on invalid fields; `aria-busy` on a saving button; `aria-disabled` on disabled-with-reason items.
- **Names**: every icon-only button has `aria-label` and a tooltip; decorative icons `aria-hidden="true"`; table inputs have `aria-label`s; the remove button names its row.
- **Live regions**: search result counts and save confirmations are announced (`aria-live="polite"`).
- **Keyboard**: everything reachable with `Tab`; lists and rails support arrow keys ([4.4](/design-standards/admin/left-navigation/#44-behaviour), [5](/design-standards/admin/section-rail/#5-section-rail)); `Esc` clears search and closes overlays.
- **Motion**: respect `prefers-reduced-motion`.
- **Zoom**: usable at 200% zoom and 320px width without page-level horizontal scroll.
- `.ab-sr-only` visually hides text that must still be read out.
{% endraw %}
