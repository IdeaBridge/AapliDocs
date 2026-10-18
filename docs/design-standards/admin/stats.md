---
layout: default
title: "Stats"
parent: "Admin (AapliAdmin)"
grand_parent: Design Standards
has_children: false
nav_order: 16
permalink: /design-standards/admin/stats/
---

{% raw %}
# 6.16 Stats — `.ab-stats` / `.ab-stat` {#616-stats--ab-stats--ab-stat}

![Stats tiles](/assets/images/design-standards/admin/ds-stats.svg)

A row of summary figures at the top of a list screen, between the title and the actions. Read only; never a substitute for the table. Used on People › Users (users on the licence, suspended users, administrator), which took these figures over from the old home page.

![Users page stats: users, suspended users and administrator](/assets/images/design-standards/admin/stats.png)

| Part | Spec |
|---|---|
| Row `ul.ab-stats` | Grid `repeat(auto-fit, minmax(180px, 1fr))`, 12px gap, `12px 0 16px` margin. `aria-label` naming the summary; `aria-busy` while loading |
| Tile `li.ab-stat` | `--ab-surface`, 1px border, `--ab-radius-sm`, padding `12px 16px`; [icon tile](/design-standards/admin/right-panel/#69-feature-list-and-detail-panel) then label and value |
| Label `.ab-stat__label` | 12px muted |
| Value `.ab-stat__value` | 22px / 500, tabular figures. `--text` modifier for words (a name): 14px, wraps |
| Variant `.ab-stat--danger` | Red icon tile, for figures that need attention (suspended users) |

**Rules**

- 2–4 tiles. Show "…" while loading and "–" when a value is missing, never a blank tile.
- Figures use thousands separators. Labels are sentence case nouns ("Suspended users").
- If a figure is a link to a filtered list, make the whole tile a link and say so in its label.
- On an `app-item-management` screen, put the stats in the `[item-header-extra]` slot so they sit between the title and the actions.
{% endraw %}
