---
layout: default
title: "Form fields"
parent: "Admin (AapliAdmin)"
grand_parent: Design Standards
has_children: false
nav_order: 7
permalink: /design-standards/admin/form-fields/
---

{% raw %}
# 6.3 Form fields {#63-form-fields}

![Text box anatomy](/assets/images/design-standards/admin/ds-text-box-anatomy.svg)

![Text box states](/assets/images/design-standards/admin/ds-text-box-states.svg)

![Dropdown: closed, selected, invalid and open](/assets/images/design-standards/admin/ds-dropdown.svg)

| Class | Spec |
|---|---|
| `.ab-field` | Column wrapper, 4px gap, 16px bottom margin |
| `.ab-label` | 12px / 500, `--ab-fg`. Required marker `<span class="ab-required">*</span>` in `--ab-danger` |
| `.ab-input` | `input`, `select`, `textarea`. 100% width, `7px 9px` padding, min-height 34px, white, 1px `--ab-line`, `--ab-radius-sm`, 14px |
| `.ab-input--mono` | Roboto Mono 13px. Keys, IDs, codes, expressions |
| `.ab-hint` | 12px muted, 4px top margin. Format and limits |
| `.ab-error` | 12px `--ab-danger`, 4px top margin. Replaces the hint when invalid |

**States:** placeholder `--ab-placeholder`; hover border `--ab-line-strong`; focus border `--ab-primary` + 1px primary ring (no glow); invalid (`.is-invalid` or `aria-invalid="true"`) red border and `--ab-danger-tint` background; disabled `--ab-surface-2` background, muted text.

- `select.ab-input` draws its own chevron; `textarea.ab-input` is at least 80px tall and resizes vertically.
- Every input has a visible `<label>` (or, in tables, an `aria-label` that names the row: "Key", "Value").
- Link the hint or error with `aria-describedby`.
- Placeholders show an example ("e.g. ExportToIFTab"), never the label or an instruction.
- Show character limits as a hint ("Up to 100 characters") or a counter (`12/40`) when the limit is likely to be reached.
- **Angular Material fields** (`mat-form-field`, `mat-select`) are fine where they already exist. Everywhere (not only inside `.ab-theme`) they are 36px high with 14px text and look like `.ab-input`: white, 1px `--ab-line-strong` border, 4px corners, darker border on hover, primary border + 1px ring when focused, no grey fill and no underline (`_material.scss`, and the select rules in `material-reset.scss`). Open lists are white with a 1px border and a soft shadow. A filled field with its label inside can overlap at 36px; put the label above the field (`.ab-label`). For new simple fields prefer the native `.ab-input`.
{% endraw %}
