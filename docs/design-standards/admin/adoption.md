---
layout: default
title: "Adoption status"
parent: "Admin (AapliAdmin)"
grand_parent: Design Standards
has_children: false
nav_order: 23
permalink: /design-standards/admin/adoption/
---

{% raw %}
# 12. Adoption status and known gaps {#12-adoption-status-and-known-gaps}

| Area | Status |
|---|---|
| Admin left nav | **Done.** Single list, search (including third-level tabs), two levels, collapse, keyboard. |
| Roles | **Done.** Promoted to a nav group (System roles, Custom roles); no tabs. |
| Page frame and titles | **Done.** All admin screens: title at 24px / 28px, 17px Roboto 500; description 14px. |
| Site design | **Done.** List + detail panel: Logo and favicon, Homepage banners, Website branding, Homepage widgets, Custom CSS. |
| Marketplace | **Done.** List + detail panel with Installed status and Install / Go to Applications. |
| Integrations | **Done.** List; Microsoft Teams app opens its panel (restyled to match `.ab-panel`), Xoxoday opens its own page (› marker). |
| Tables | **Done.** Every table uses `app-ab-data-table` (6.5.1): all `app-item-management` tables (Users, Categories, Evaluation matrix, Cards, Announcements, Pages, Notifications, Custom roles, Failed submissions, SSO, Currencies, Email logs), Applications, Entity builder, Import data history, Form management. The `angular2-smart-table` package is removed; its data sources were replaced by `ab-data-source.ts`. |
| People › User properties | **Done.** Same table style as Users: search, count, Unsaved changes, Save changes, Add property; name with type icon, settings as chips, parent, associated roles, ⋮ (Edit, Add below, Edit list options, Delete); drag to reorder (off while searching); row click opens the property panel. |
| People › Users | **Done.** Matches the reference: stats, toolbar (search, count, Bulk add, More, Add user), checkbox column and bulk bar (Export, Suspend), Name / Role / Status / Last sign-in, ⋮ (Edit details, Reset password, Suspend / Reactivate, Delete user). Last sign-in shows once the list API returns `LastLoggedin`. |
| Home page | **Dropped.** `/` and `/admin` open the first nav item. Its licence figures moved to People › Users as stats; the asset management sidebar lost its Home item, and the other sidebar's Home became "Admin settings". |
| Data | **Done.** (Was "Import export data".) Promoted to a nav group (Import data, Templates, Export data, Import history); no tabs or in-page menu. Import data shows its four steps one per row, full width. Import history opens a file's row log in a right panel (`.ab-panel--xwide`, "Open page" for the shareable `data/history/:fileId` address). |
| Failed submissions | Moved to the Others group, the last group above General. |
| Features | **Done.** Rebuilt as the feature list and detail panel; settings moved from the expanding rows into the panel. |
| Settings | **Done.** Rows show each area's current value under its name, description in an info tooltip (option C of `design-system/settings-value-prototypes.html`); list + detail panel: Company name, Company address, Date format, Number format, Application type (was Organisation settings), Currencies. Company profile parts and Application type use settings sections. Currencies keeps the shared item-management table (title hidden in the panel). |
| Form builder shell (app bar, main tabs, action bar) | **Done.** Preview moved to the app bar; Save is the primary button, right-most. |
| Form builder › Settings | **Done.** Application settings and Properties combined in one tab and rail; opens first. Information, Views, Other settings, AI features and Integrations use the item list + detail panel. Roles and permissions and Points keep their tables. |
| Form builder › Properties section rail | **Done.** Vertical tab list with keyboard support. |
| Form builder › Application settings, Form, Tasks, Dashboard, Settings | **Done.** Rebuilt with `.ab-*` markup (17/10/2026). Workflow tabs keep the BPMN editor's own look. |
| Custom properties section | Prototype only; needs backend support (`content/get` `CustomProperties`). Build to the prototype and this document. |
| Admin console screens | **Done.** `.admin-content` is an `.ab-theme` root; Applications, Data (import, history, dry run), Site design widgets, Evaluation matrices, Notifications, Billing, Pages, System roles, User import mapping, SSO, Cards, Categories, Email logs, Announcements, Marketplace details, Company banner and footer, Currency and application settings rebuilt (audit 17/10/2026). Add / edit panes use `.ab-panel`. |
| Entity builder | **Done.** Same shell as the form builder (app bar, tabs, action bar); design form, palette, entities panel, overview and diagram rebuilt. |
| Material overlays (select panels, dialogs) | **Done.** `.ab-theme` by default via `MAT_DIALOG_DEFAULT_OPTIONS` / `MAT_SELECT_CONFIG`. |
| Dark mode | Not supported (tokens are ready for it). |
{% endraw %}
