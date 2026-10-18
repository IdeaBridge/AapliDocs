---
layout: default
title: "Implementing in Angular"
parent: "Admin (AapliAdmin)"
grand_parent: Design Standards
has_children: false
nav_order: 21
permalink: /design-standards/admin/angular/
---

{% raw %}
# 10. Implementing in Angular {#10-implementing-in-angular}

## 10.1 Files {#101-files}

| Path | What |
|---|---|
| `src/scss/design-system/_tokens.scss` | All `--ab-*` tokens |
| `src/scss/design-system/_components.scss` | `.ab-*` classes |
| `src/scss/design-system/_material.scss` | Angular Material token alignment inside `.ab-theme` |
| `src/scss/design-system/_legacy-bridge.scss` | Restyles legacy classes inside `.ab-theme` (temporary) |
| `src/scss/design-system/_index.scss` | Forwards the above; loaded once from `src/scss/styles.scss` |
| `src/app/_view/_ui-components/side-nav/` | `<app-side-nav>` standalone component and `SideNavNode` model |
| `src/app/_services/settings.service.ts` | `adminNav`, `ADMIN_NAV_GROUPS`, `ADMIN_NAV_KEYWORDS` |
| `src/app/_view/admin-console/` | Hosts the left nav |
| `src/app/_view/form-builder/form-builder.component.*` | Workspace shell: app bar, main tabs, action bar |
| `src/app/_view/form-builder/properties/properties.component.*` | Section rail |
| `docs/design-system/diagrams/` | Annotated diagrams (`ds-*.svg`) for each pattern, and `gen_ds_svgs.py`, which draws them from the tokens |

## 10.2 Adopting the system in a screen {#102-adopting-the-system-in-a-screen}

1. Add `ab-theme` to the screen's outermost element.
2. Build new markup from the `.ab-*` classes. Component stylesheets should only contain layout specific to that screen (grid areas, heights), using tokens.
3. Use `var(--ab-…)` for every colour, size and space. No hex values, no `--primaryColor` in new code.
4. Prefer real elements (`button`, `a`, `nav`, `header`, `footer`, `table`) and the ARIA in [section 9](/design-standards/admin/accessibility/#9-accessibility).
5. Remove the screen's now-unused legacy styles in the same PR.

## 10.3 Rules for stylesheets {#103-rules-for-stylesheets}

- Never `@use 'config/_button'` (or other legacy global rule files) in a component stylesheet: Angular scopes them to that template, where `button[_ngcontent]` outranks `.ab-btn` and blanks design-system buttons (this hid Users' Add user button). The global styles already include them.
- New shared styles go in `_components.scss` with a section in this document. Don't create a second copy of a component in a screen stylesheet.
- No `!important`, except to beat an existing `!important` you can't remove yet; comment why.
- Avoid `::ng-deep`. Where you must reach into a Material component, scope it under `:host` and the component's own class, and prefer setting Material's `--mat-*` tokens over overriding its internal classes.
- No inline `style="…"` for colours or spacing.
- Keep selectors shallow: one class, plus a state class or element where needed.

## 10.4 Legacy bridge {#104-legacy-bridge}

`_legacy-bridge.scss` restyles older classes (Bootstrap `.form-control` / `.btn-primary`, `.primary-button`, `.secondary-button`, `.dark-button`, `h2.title`, `.sub-title`, `.section-title`, `.bg-grey`, border utilities) **only inside `.ab-theme`**, so a screen can take on the new look before its markup is rewritten. It uses `.ab-theme.ab-theme` to outrank component-scoped styles without `!important`.

- Do **not** use legacy classes in new markup, and do not add rules to the bridge for new work.
- When the last use of a legacy class inside `.ab-theme` screens is gone, delete its bridge rule.

## 10.5 Angular Material {#105-angular-material}

- Inside `.ab-theme`, Material components take admin colours from `_material.scss` (it sets `--mat-*` tokens at the component level, because the prebuilt theme sets them there).
- Overlays (select panels, menus, dialogs, tooltips) render outside `.ab-theme` in the CDK overlay container. Pass `panelClass="ab-theme"` (select, menu) or add it to the dialog's `panelClass` when the overlay needs the admin look.

## 10.6 Tenant theme colour {#106-tenant-theme-colour}

The rest of the app still uses the tenant's `--primaryColor`. `.ab-theme` overrides it only for its descendants. Don't change `--primaryColor` globally, and don't use `--ab-primary` in end-user (non-admin) screens.
{% endraw %}
