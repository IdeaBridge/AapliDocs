---
layout: default
title: "Headings and text"
parent: "Admin (AapliAdmin)"
grand_parent: Design Standards
has_children: false
nav_order: 5
permalink: /design-standards/admin/headings-text/
---

{% raw %}
# 6. Components {#6-components}

All classes live in `src/scss/design-system/_components.scss`. Naming: `.ab-block`, `.ab-block__element`, `.ab-block--modifier`, state as `.is-*` (`.is-active`, `.is-selected`, `.is-invalid`, `.is-on`, `.is-disabled`).

## 6.1 Headings and text {#61-headings-and-text}

| Class | Element | Spec |
|---|---|---|
| `.ab-title` | `h2` | 17px / 500, `--ab-fg`, 4px bottom margin. First thing in a pane. |
| `.ab-sub` | `p` | 14px / 400, `--ab-muted`, line height 1.5, full width, 18px bottom margin. Explains what the section does and what happens when it is changed. |
| `.ab-subtitle` | `h3` | 14px / 500. A group inside a section. |
| `.ab-overline` | `h3`/`div` | 11px / 500, uppercase, `.06em`, `--ab-muted`, optional 16px icon. Aside headings and small section labels. |
| `.ab-count` | `span` | 12px muted. "3 properties". |
| `.ab-mono` | `code`/`span` | Roboto Mono 12.5px. |

Every pane has a title and a subtitle. If you can't write the subtitle, the section probably needs rethinking.
{% endraw %}
