---
layout: default
title: "Buttons"
parent: "Admin (AapliAdmin)"
grand_parent: Design Standards
has_children: false
nav_order: 6
permalink: /design-standards/admin/buttons/
---

{% raw %}
# 6.2 Buttons — `.ab-btn` {#62-buttons--ab-btn}

![Button variants in every state](/assets/images/design-standards/admin/ds-buttons.svg)

Base: inline-flex, 6px gap, `7px 14px` padding, min-height 34px, `--ab-radius-sm`, 14px / 500, 20px icon. Always a `<button type="button">` (or `<a>` for navigation).

| Variant | Class | Look | Use |
|---|---|---|---|
| Primary | `.ab-btn--primary` | `--ab-primary` fill, white text; hover `--ab-primary-hover` | The one main action in a view: Save, Create, Confirm |
| Stroked | `.ab-btn--stroked` | White, `--ab-line` border, primary text; hover `--ab-line-strong` border and faint tint | Secondary actions: Add property, Preview, Cancel, Discard changes, Next |
| Text | `.ab-btn--text` | No border, muted text, tight padding | Tertiary and in-line actions: Back, Clear search |
| Danger | `.ab-btn--danger` | Muted icon or text; hover red text on red tint | Row-level remove (`delete_outline`) |
| Danger solid | `.ab-btn--danger-solid` | Red fill, white text | The confirm button in a destructive dialog only |
| Icon | `.ab-btn--icon` | 34×34, muted, hover faint grey | Close, overflow menus. **Must** have `aria-label` and a tooltip |
| Small | `.ab-btn--sm` | `4px 10px`, min-height 28px, 12px | Dense toolbars and inline actions |

**States:** hover as above; focus-visible 2px primary ring offset 1px; disabled (`:disabled`, `[aria-disabled=true]`, `.is-disabled`) 45% opacity and `not-allowed`; loading: swap the icon for an 18px `mat-spinner`, change the label to the present participle ("Saving…"), set `[disabled]` and `aria-busy`.

**One theme for every button.** Inside the admin console (`.admin-content`), the form builder (`.ab-theme`) and their dialogs (`.cdk-overlay-container`), `_buttons-bridge.scss` maps every older button class to these looks, so the same action looks the same everywhere and never takes the tenant colour: `.primary-button`, `.button-blue`, `.form__button-blue`, `.btn-primary`, Material raised / flat primary or accent → **Primary**; `.secondary-button`, `.cancel-button`, `.btn-secondary`, `.btn-outline-*`, Material stroked → **Stroked**; `.btn-danger`, Material warn → **Danger solid**. New markup still uses `.ab-btn` directly.

**Rules**

- One primary button per view (per dialog, per action bar).
- Labels are verbs in sentence case: "Save properties", "Add property", "Discard changes". Not "OK", not "Submit", not "Click here".
- Leading icon for actions (`add`, `save`); trailing icon only for direction (`arrow_forward`).
- When a button is disabled, say why next to it (see [Editing and saving](/design-standards/admin/patterns/#71-editing-and-saving)).
- Don't build buttons from `<div>` or `<span>` with `(click)`; they are not keyboard accessible. (The old form builder footer did this; it has been replaced.)
{% endraw %}
