---
layout: default
title: "Chips, badges and cards"
parent: "Admin (AapliAdmin)"
grand_parent: Design Standards
has_children: false
nav_order: 10
permalink: /design-standards/admin/chips-cards/
---

{% raw %}
# 6.6 Chips and badges {#66-chips-and-badges}

![Chips, badge, cards and status flag](/assets/images/design-standards/admin/ds-chips-cards.svg)


| Class | Spec | Use |
|---|---|---|
| `.ab-chip` | 12px, `2px 8px`, pill radius, `--ab-surface-2` with `--ab-line` border, muted text | Read-only context: "Content type: RPG Application" |
| `.ab-chip--primary` / `--ok` / `--danger` / `--warn` | Tinted background, full-strength text, no border | Status: "Published", "Draft", "Failed" |
| `.ab-badge` | 10px / 500 uppercase, primary fill, white, 8px radius | "New" on a nav or rail item. One word. Remove after a release. |

Chips are not buttons. If it can be clicked or removed, it is a different component (use Material chips and document it here first).

# 6.7 Cards — `.ab-card` {#67-cards--ab-card}

- White, 1px `--ab-line`, `--ab-radius-sm`, padding `14px 16px`. No shadow.
- `.ab-card--selectable`: pointer cursor, hover border `--ab-line-strong`; `.is-selected` adds a primary border, a very faint primary tint and a 3px primary inset bar on the left. Selecting a card should also tick its checkbox if it has one; the card and the checkbox must not disagree.
- Card title: `.ab-subtitle`; description: 12–14px muted.
{% endraw %}
