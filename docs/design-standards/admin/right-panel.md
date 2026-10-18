---
layout: default
title: "Feature list and right panel"
parent: "Admin (AapliAdmin)"
grand_parent: Design Standards
has_children: false
nav_order: 12
permalink: /design-standards/admin/right-panel/
---

{% raw %}
# 6.9 Feature list and detail panel {#69-feature-list-and-detail-panel}

![Feature list anatomy](/assets/images/design-standards/admin/ds-feature-list.svg)

![Right-hand panel anatomy](/assets/images/design-standards/admin/ds-right-panel.svg)

![Panel widths and variants](/assets/images/design-standards/admin/ds-panel-variants.svg)


For screens that are a set of separate things to switch on, install or configure: Features, Site design, Marketplace, Integrations, and Organisation › Settings (Company name, Company address, Date format, Number format, Application type, Currencies). Use it for any future "services", "integrations" or "add-ins" list too. A scannable list of everything available, and a panel from the right with one feature's explanation, its on/off switch and its settings. The list stays visible behind the panel so admins keep their place.

![Feature list grouped by category, with icon, name, description and status](/assets/images/design-standards/admin/feature-list.png)

![Detail panel open over the list: title, description, Turn on checkbox, settings and Save](/assets/images/design-standards/admin/feature-panel.png)

**List**

| Part | Spec |
|---|---|
| Header | `h2.ab-title` + `.ab-sub`, then a toolbar with a search field (leading `search` icon, filters as you type) and a count |
| Table | `.ab-table` with `table-layout: fixed`. Columns: **Name** (34%), **Description**, **Status** (96px, right aligned) |
| Group rows | One `<tbody>` per category with a full-width `th` overline row on `--ab-bg` ("Authentication and access", "AI"…). Groups with no matches are hidden |
| Name cell | 32px icon tile (`--ab-primary-tint` background, primary icon, `--ab-radius-sm`) + feature name 14px / 500. The name is a `<button>` with `aria-expanded` and `aria-controls` pointing at the panel; the whole row is also clickable |
| Description | 13px muted, one line with ellipsis (the panel shows it in full). Hidden at ≤ 760px |
| Status | `.ab-chip` "On" (`--ok`) or "Off" (neutral). Text, not colour alone |
| Selected row | The row whose panel is open gets `--ab-primary-tint` |
| Empty | "No features match “query”." or "No features are available for your organisation." |

The list never changes a setting by itself: no switches in rows. Everything happens in the panel, so every change is explained first and committed with Save.

**Detail panel**

| Part | Spec |
|---|---|
| Container | Fixed to the right edge, full height, `min(520px, 100vw)` wide, `--ab-surface`, left border and a soft shadow. Slides in 24px with a fade (off with reduced motion). `role="dialog"`, `aria-modal="true"`, `aria-labelledby` the title |
| Scrim | `rgba(15,27,42,.32)` over the page; clicking it closes the panel. Panel and scrim sit just below the CDK overlay layer (z 990/991) so dialogs opened from the panel (Send a test email, confirmations) appear on top |
| Header | Title 22px / 500 (the feature name), close icon button top right |
| Description | Full description, 14px `--ab-fg`, 24px below. Optional "Learn more about …" link under it when there is documentation |
| On/off | A checkbox labelled **"Turn on {feature name}"**, not a switch, because nothing happens until Save |
| Read only | When the admin can't change it, an `.ab-note--info` with a `lock` icon says who can ("Only a Points Admin can change this"); the checkbox and fields are disabled and Save stays disabled |
| Settings | Shown only while the checkbox is ticked, under a divider with an `.ab-overline` "Settings" heading, using the normal [form fields](/design-standards/admin/form-fields/#63-form-fields) |
| Footer | Pinned to the bottom with a top border: **Save** (primary) then **Cancel** (stroked), left aligned. In a narrow panel the primary action comes first so it sits under the content being edited; this is the one exception to "primary last". A panel whose content is [settings sections](/design-standards/admin/settings-section/#68-settings-section--ab-section) (each with its own Edit / Save) has **no footer**; the close button is enough |
| Width | `.ab-panel` 520px for a checkbox and a few fields; `.ab-panel--wide` 720px for forms with two columns or a list (Company name, Company address, Application type); `.ab-panel--xwide` 960px for a table (Currencies). Always `min(…, 100vw)` |

**Settings: list items without a status**

Settings uses the same list without the Status column, one row per area, and each area's panel holds the existing component with `[embedded]="true"`, which hides its own page title (the panel shows it) and keeps section headings for screen readers only. The open area is in the URL (`/admin/organisation/settings/<area>`) using componentless child routes, so the list does not re-render when a panel opens, and links, the nav search and the back button all work.

![Settings: six areas listed with icon, name and description](/assets/images/design-standards/admin/settings-list.png)

**Choosing one option from a list** (Application type): use the same row look inside the panel, with a radio first: radio · icon tile · name · description · "Current" chip on the saved value. The selected row is tinted. Not a grid of cards.

![Application type panel: one option per row with icon, name and description](/assets/images/design-standards/admin/settings-panel-application-type.png)

**Behaviour**

- Opening a feature loads its saved state into a draft; ticking or unticking the checkbox and editing settings change only the draft.
- **Save** is disabled until there is something to save: the on/off state changed, or the feature has settings and is on.
- Save closes the panel, updates the row's status and shows a toast ("AI chat saved"). Turning off something with consequences (Point reset) asks for confirmation first.
- **Cancel**, the close button, the scrim and `Esc` all close without saving. Focus moves to the panel title on open and back to the row's name button on close.
- One panel at a time; selecting another row replaces the panel's content.

**Every right-hand panel looks the same** (`.ab-panel`, `_components.scss`): a tinted (blue) header band with the title and, under it, the description (`.ab-panel__heading` > `.ab-panel__title` + `.ab-panel__desc`); a white body; content groups (`.ab-panel__card`, optional `.ab-panel__card-title` with a primary icon) with no box of their own, split by a hairline with 20px either side; actions in the footer on white. Inside a group, settings sections drop their own frame and `.ab-dl` becomes the two-column list with hairlines used in user details. Add / edit panels (`app-item-management`, Microsoft Teams, Slack, Teams app download) follow it too; a host with several groups of fields brings its own cards (`[editInCards]="true"`, as Edit user does: Account, System roles, Profile).

**Inside a larger editor** (form builder › Settings: Information, Views, Other settings, AI features), the panel edits the application being built, which is saved with the editor's own Save. There the panel applies changes as they are made and its footer is **Done** (primary) with "Saved with the application." beside it; Cancel and a draft are not used. Settings that need room (a view's columns and preview, the Info tab's columns) use `.ab-panel--wide`. Items the application type can't use show an "Unavailable" chip and a locked note in the panel. Integrations rows open their own set-up panel and show **Connected** / **Not set up**.
{% endraw %}
