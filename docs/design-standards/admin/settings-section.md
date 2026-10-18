---
layout: default
title: "Settings section"
parent: "Admin (AapliAdmin)"
grand_parent: Design Standards
has_children: false
nav_order: 11
permalink: /design-standards/admin/settings-section/
---

{% raw %}
# 6.8 Settings section — `.ab-section` {#68-settings-section--ab-section}

![Settings section in view and edit mode](/assets/images/design-standards/admin/ds-settings-section.svg)


One group of saved settings (Company name, Company address, Date format, Number format, Application type), usually inside a Settings detail panel. When embedded in a panel the section heading is visually hidden (`[embedded]="true"`) because the panel title already says it, and the Edit button stays on the right (`.ab-section__edit`). Shows the current values read-only, with an **Edit** button; Edit swaps the body for a form with **Cancel** and **Save**. Each section saves on its own.

![Company profile: three settings sections in view mode](/assets/images/design-standards/admin/settings-section-view.png)

![Contact information section being edited, with a field error and Save disabled](/assets/images/design-standards/admin/settings-section-edit.png)

| Part | Spec |
|---|---|
| Card `.ab-section` | `--ab-surface`, 1px border, `--ab-radius-sm`, padding `16px 20px`, 16px bottom margin, `max-width: 960px` |
| Editing `.is-editing` | Primary border and 3px primary inset bar on the left (same as a selected card) |
| Header `.ab-section__head` | `h3.ab-subtitle` on the left; Edit button (`.ab-btn--stroked.ab-btn--sm`, `edit` icon) on the right, hidden while editing. **Embedded in a panel** (heading visually hidden): the header has no row of its own; it floats right so Edit sits on the same line as the first label / value |
| Description `.ab-section__desc` | Optional, 12px muted, under the header, full width |
| Values `dl.ab-dl` | Auto-fill grid of `minmax(220px, 1fr)` columns, gaps 16px × 24px. Each pair is `<div><dt>Label</dt><dd>Value</dd></div>`: `dt` 12px muted, `dd` 14px `--ab-fg`. Empty values show `.ab-dl__empty` ("Not set") in `--ab-placeholder` |
| Form layout `.ab-form-grid` | Two equal columns, 16px gap; `.ab-field--full` and fieldsets span both; one column at ≤ 760px |
| Field groups `fieldset.ab-fieldset` | No border; `legend` 12px / 500 as the group label (e.g. "Company address") |
| Actions | `.ab-actionbar--inline`: Cancel (stroked), Save (primary, `save` icon), then `.ab-status` when Save is unavailable ("Fix the highlighted fields to save.") or to show "Unsaved changes" |

**Rules**

- Only one section is in edit mode at a time where possible; never auto-save a section that has a Save button. (Exception, flagged in its hint: the theme colour swatch saves when picked.)
- View mode shows every value the form can change, so admins don't have to open Edit to read a setting.
- Machine values (formats, domains, colour codes) are in mono.
- Addresses: labelled fields (Street address, Town or city, County or state, Postcode, Country) with `autocomplete` tokens, not placeholders as labels.
- A choice between a few options with explanations (App type) uses selectable cards with a radio inside (`.ab-card--selectable`, `.is-selected`).
{% endraw %}
