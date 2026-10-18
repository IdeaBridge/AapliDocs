---
layout: default
title: "Admin (AapliAdmin)"
parent: Design Standards
has_children: true
nav_order: 1
permalink: /design-standards/admin/
---

{% raw %}
# Aapli Admin design system {#aapli-admin-design-system}

**Status:** v2.7.1 · adopted 15/10/2026, updated 17/10/2026
**Applies to:** the admin console (left navigation) and the form builder. Every new admin screen, and every change to an existing one, must follow this document.
**Code:** `src/scss/design-system/` (tokens and shared classes) and `src/app/_view/_ui-components/side-nav/` (left navigation).
**Reference prototype:** *Application Custom Properties* (Admin › Form Builder › Properties). This system is drawn from it.

> If the code and this document disagree, that is a bug. Fix whichever is wrong in the same pull request, and record the change in the [changelog](/design-standards/admin/changelog/#13-changelog).

> This is the developer copy of `docs/DESIGN_SYSTEM.md` in the AapliAdmin repository (branch `redesign`), split into pages and illustrated with a diagram for each pattern. The AapliAdmin file is the source of truth: change it first, then regenerate these pages with `_design-src/admin/build_admin_ds.py`.

---

## Contents {#contents}

| Page |
|---|
| [Foundations](/design-standards/admin/foundations/) |
| [Layout](/design-standards/admin/layout/) |
| [Left navigation](/design-standards/admin/left-navigation/) |
| [Section rail](/design-standards/admin/section-rail/) |
| [Headings and text](/design-standards/admin/headings-text/) |
| [Buttons](/design-standards/admin/buttons/) |
| [Form fields](/design-standards/admin/form-fields/) |
| [Selection controls](/design-standards/admin/selection-controls/) |
| [Tables and data table](/design-standards/admin/tables/) |
| [Chips, badges and cards](/design-standards/admin/chips-cards/) |
| [Settings section](/design-standards/admin/settings-section/) |
| [Feature list and right panel](/design-standards/admin/right-panel/) |
| [Notes, code and status flag](/design-standards/admin/notes-code-flag/) |
| [Toast, empty, loading and error](/design-standards/admin/feedback/) |
| [Dialogs](/design-standards/admin/dialogs/) |
| [Stats](/design-standards/admin/stats/) |
| [Accordions](/design-standards/admin/accordions/) |
| [Patterns](/design-standards/admin/patterns/) |
| [Content and copy](/design-standards/admin/content-copy/) |
| [Accessibility](/design-standards/admin/accessibility/) |
| [Implementing in Angular](/design-standards/admin/angular/) |
| [Pull request checklist](/design-standards/admin/pr-checklist/) |
| [Adoption status](/design-standards/admin/adoption/) |
| [Changelog](/design-standards/admin/changelog/) |

## 1. Principles {#1-principles}

1. **Quiet chrome, clear content.** Surfaces are white or near-white, separated by 1px hairlines. No drop shadows, gradients or heavy fills. Colour is kept for meaning: the primary action, the current location, and status.
2. **One accent.** The brand blue (`--ab-primary`) marks what is selected, active or primary. If everything is blue, nothing is.
3. **Tell people what will happen.** Every setting has a plain-language subtitle. Where a setting affects behaviour elsewhere (an API response, a feature switch), show the effect next to it, as the API preview in the prototype does.
4. **Never lose work silently.** Show whether there are unsaved changes, say why Save is unavailable, and confirm before discarding.
5. **Keyboard and screen reader first-class.** Every interactive element is a real `<button>` or `<a>`, has a visible focus ring, and has an accessible name.
6. **Tokens, not values.** Colours, sizes and spacing come from `--ab-*` tokens. A raw hex value or a one-off pixel size in a component stylesheet needs a reason in a comment.

## Reference prototypes {#reference-prototypes}

Clickable design options that were used to choose the current patterns. They use fictional data.

- [Points](/assets/design-standards/admin/prototypes/points-prototypes.html)
- [Roles and permissions](/assets/design-standards/admin/prototypes/roles-permissions-prototypes.html)
- [Settings values](/assets/design-standards/admin/prototypes/settings-value-prototypes.html)
- [Table row actions](/assets/design-standards/admin/prototypes/table-actions-prototypes.html)
- [Assign tasks](/assets/design-standards/admin/prototypes/tasks-prototypes.html)

{% endraw %}
