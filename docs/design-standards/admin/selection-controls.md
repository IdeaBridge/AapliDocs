---
layout: default
title: "Selection controls"
parent: "Admin (AapliAdmin)"
grand_parent: Design Standards
has_children: false
nav_order: 8
permalink: /design-standards/admin/selection-controls/
---

{% raw %}
# 6.4 Selection controls {#64-selection-controls}

![Checkbox, radio and slide toggle](/assets/images/design-standards/admin/ds-selection.svg)


Use Angular Material `mat-checkbox`, `mat-radio-button`, `mat-slide-toggle`, `mat-slider`. Inside `.ab-theme` they use `--ab-primary` for the checked state and `--ab-muted` for the unchecked outline.

- **Checkbox** for independent options and for opting a card in or out (see [Cards](/design-standards/admin/chips-cards/#67-cards--ab-card)).
- **Radio** for 2–5 mutually exclusive options that should all be visible. More than 5: a select.
- **Slide toggle** for a setting that takes effect immediately (no Save). If the page has a Save button, use a checkbox instead.
- Labels are on the right of the control, in sentence case, and say what "on" means ("Show judging summary").
{% endraw %}
