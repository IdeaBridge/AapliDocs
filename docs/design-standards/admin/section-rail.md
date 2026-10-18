---
layout: default
title: "Section rail"
parent: "Admin (AapliAdmin)"
grand_parent: Design Standards
has_children: false
nav_order: 4
permalink: /design-standards/admin/section-rail/
---

{% raw %}
# 5. Section rail {#5-section-rail}

![Section rail with active, hover and badge](/assets/images/design-standards/admin/ds-section-rail.svg)


The vertical list of sections **inside** a workspace tab (the form builder's Settings tab). Same visual language as the left nav, single level.

**Form builder › Settings** is one tab and one rail: **Application settings** first (name, category, type), then the property sections (Information, Views, Roles and permissions, Other settings, Points, AI features, Integrations). It is the first tab and opens on Application settings for a new or edited application; creating from a template skips Application settings, as before. Save errors about the name, category or type reopen it. There is no separate Properties tab. In code: `app-properties` takes `[leadSection]` and projects `[props-lead]` as rail position 0.

| Part | Spec |
|---|---|
| Container `.ab-rail` | 260px wide (`--ab-rail-w`, wide enough for "Roles and Permissions" plus its icon), `--ab-surface-2`, right border, padding `16px 8px`, sticky, scrolls on its own |
| List `.ab-rail__list` | Column, 2px gap |
| Item `.ab-rail__item` | `<button>` (or `<a>` if it changes the URL), icon + label, padding `9px 12px`, 10px gap, `--ab-radius-sm`, `--ab-muted` |
| Hover | `rgba(primary, .05)` background, `--ab-fg` text |
| Active `.is-active` / `[aria-selected=true]` | `--ab-primary-tint` background, `--ab-primary` text, 500 |
| Badge | `.ab-badge` pushed right ("New" for a recently added section; remove after one release) |

- Markup is a vertical tab list: `ul[role=tablist][aria-orientation=vertical] > li[role=none] > button[role=tab]`, with `aria-selected`, roving `tabindex` (0 on the active item, −1 on the others) and `↑` / `↓` / `Home` / `End` moving between sections. The pane is `role="tabpanel"` with `aria-labelledby` pointing at the active item.
- Drive the active state from component state (`[class.is-active]="selectedTabIndex === i"`), never by adding and removing classes on DOM elements.
- At ≤ 760px the rail becomes a horizontal scrolling row above the pane.
- 3–10 sections. Labels are sentence case nouns.
{% endraw %}
