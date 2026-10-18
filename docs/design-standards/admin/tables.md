---
layout: default
title: "Tables and data table"
parent: "Admin (AapliAdmin)"
grand_parent: Design Standards
has_children: false
nav_order: 9
permalink: /design-standards/admin/tables/
---

{% raw %}
# 6.5 Tables — `.ab-table` {#65-tables--ab-table}

![Table anatomy and row height](/assets/images/design-standards/admin/ds-table.svg)


```html
<div class="ab-table-wrap">
  <table class="ab-table">
    <thead><tr><th>Key</th><th>Value</th><th class="ab-table__actions"><span class="ab-sr-only">Remove</span></th></tr></thead>
    <tbody>…</tbody>
  </table>
</div>
```

| Part | Spec |
|---|---|
| Wrapper `.ab-table-wrap` | 1px border, `--ab-radius-sm`, `overflow-x: auto` |
| Table | Full width, collapsed borders, `min-width: 560px` (scrolls inside the wrapper below that) |
| `th` | 11px / 500 uppercase `.06em`, muted, `8px 12px`, row height 36px (`--ab-row-h-head`), `--ab-surface-2` background, bottom border, no wrap |
| `td` | `6px 12px` (`--ab-cell-py` / `--ab-cell-px`), row height 40px (`--ab-row-h`), bottom border (none on last row), `vertical-align: middle` |
| Row hover | `rgba(primary, .02)` |
| Actions column `.ab-table__actions` | 48px, right aligned, header text visually hidden |

## Row height {#row-height}

One row height everywhere in the console: lists, data tables, the form builder's Roles and permissions, Points and Assign tasks grids, and any new table.

| Row | Height | Cell padding | Token |
|---|---|---|---|
| Header | 36px | `8px 12px` | `--ab-row-h-head` |
| Body, one line of text | 40px | `6px 12px` | `--ab-row-h`, `--ab-cell-py`, `--ab-cell-px` |
| Body, name with a sub-line (person, icon tile) | grows to fit, no extra padding | `6px 12px` | — |

- Content in a row must fit 28px: checkboxes use a 32px touch area (`--mat-checkbox-state-layer-size: 32px`), icon buttons 28px, inputs (Points) 28px, chips 26px or less.
- The rule lives once in `_components.scss` (`:is(.ab-table, .abdt__table, .fbp-rp__table, .ti-table, .at__table)`); a new table either uses `.ab-table` or is added to that list. Don't set row padding in a component.
- Cells are vertically centred. A cell that shows an error under an input grows; the rest of the row stays centred.

## Row actions {#row-actions}

![Row actions: one always-visible menu per row](/assets/images/design-standards/admin/ds-row-menu.svg)


![Option A: row menu](/assets/images/design-standards/admin/row-menu.png)

Every row's actions sit behind **one ⋮ button that is always visible** in the last column. **Actions never appear on hover.**

| Part | Spec |
|---|---|
| ⋮ button | 32×32, `more_vert`, `--ab-muted`; hover/focus `--ab-surface-2` background. Accessible name "Actions" (or "Actions for {name}"). Last column 56px wide, right aligned |
| Menu `.ab-menu` | Opens under the button (above it if there is no room), right edges aligned; 200–280px wide, `--ab-surface`, 1px border, 6px radius, soft shadow, 6px vertical padding |
| Item `.ab-menu__item` | 38px high, 20px muted icon + label in sentence case ("Reset password"). Hover/focus `--ab-surface-2` |
| Order | Most used first (View, Edit…), state changes next (Enable / Disable, shown as one item whose label matches the row's state), destructive last after a divider (`.ab-menu__divider`), in `--ab-danger` |
| Keyboard | Opening focuses the first item; `↑`/`↓`/`Home`/`End` move; `Enter` runs; `Esc` closes and returns focus to ⋮; `Tab` closes |
| Closing | Choosing an item, clicking outside, `Esc`, scrolling or resizing |

**Clicking the row** (anywhere except ⋮ and checkboxes) **opens the detail panel with details only**: the record's values as an `.ab-dl`, no action buttons. Actions are only in the ⋮ menu. A table with its own details screen shows that; otherwise `app-item-management` builds the panel from the table's columns.

**Bulk actions**: where a table offers them, a checkbox column first; selecting rows replaces the toolbar with a tinted bar: "N selected", the bulk actions as text buttons, and a clear (×) button.

In `app-item-management` and every [data table](#651-data-table--app-ab-data-table) this is built in: the existing `disableEdit` / `disableToggle` / `disableDelete` / `disablePassword` / `disableView` inputs, `moreCustomActions` and `passwordActionHiddenWhen` decide which items each row's menu contains.

- **Editable rows**: inputs fill the cell; the remove button is `.ab-btn--danger` with `delete_outline` and `aria-label="Remove <key>"`.
- **Empty state**: one row, `colspan` across all columns, `.ab-empty` text that says how to add the first item ("No custom properties yet. Select **Add property** to create one.").
- **Toolbar** above the table (`.ab-toolbar`): count on the left (`.ab-count`), actions on the right.
- Lists of records (search, sort, pages) use the [data table component](#651-data-table--app-ab-data-table). The `angular2-smart-table` package has been removed.

# 6.5.1 Data table — `app-ab-data-table` {#651-data-table--app-ab-data-table}

![Data table: toolbar, person cell, status chips, footer and bulk bar](/assets/images/design-standards/admin/ds-data-table.svg)


![People › Users: the reference data table](/assets/images/design-standards/admin/users-table.png)

![Rows selected: the toolbar becomes the bulk bar](/assets/images/design-standards/admin/users-table-bulk.png)

The one component for lists of records (`src/app/_view/_ui-components/ab-data-table/`, standalone). It takes the existing column configs and data sources, so a screen moves over by swapping the tag. Data sources live beside it in `ab-data-source.ts`: `AbLocalDataSource` (rows in memory) and `AbServerDataSource` (paging, filtering and sorting by an endpoint: `page`/`perPage` or `_page`/`_limit`, `<field>_like`, `_sort`/`_order`, rows at `dataKey`, total at `totalKey` or the `x-total-count` header). `IBEXTNG2ServerDataSource` extends `AbServerDataSource` with the busy callback and the local sort fallback. `app-item-management` uses it for all its tables; Applications, Entity builder, Import data history and Form management use it directly. People › Users is the reference.

| Part | Spec |
|---|---|
| Toolbar | Search box (320px, `search` icon inside, placeholder naming what it searches: "Search by name, email, role or status"), then the count ("1,248 users", `.ab-count`), then the screen's actions on the right: secondary actions stroked, the main action last and primary with an icon ("Add user", `person_add`). Rarely used actions go in a ⋮ "More" menu beside them (Users: Bulk add template, Download all users, Import users from AD, Bulk delete from file) |
| Bulk bar | Replaces the toolbar while rows are ticked: `--ab-primary-tint` bar, "N selected" (500, primary), bulk actions as text buttons (primary; destructive in red), clear (×). Only on tables with bulk actions (`selectable`) |
| Header | As `.ab-table`. Sortable columns are buttons; the arrow shows on hover and stays on the sorted column (asc → desc → off), `aria-sort` set. Checkbox column 44px with select-all for the page (indeterminate when some) |
| Rows | `td` 10px 12px, vertically centred. Hover `rgba(primary,.02)`; ticked or open in a panel: `--ab-primary-tint`. Clickable rows are focusable; `Enter` opens |
| Person cell (`abType: 'person'`) | 30px round avatar (photo, or initials on `--ab-primary-tint` in primary, 12px / 500), name 500, secondary line (email) 12px muted |
| Status cell | Chip with a 6px dot, 12px, 10px radius: Active `--ok`, Awaiting approval / pending `--warn`, Suspended / Inactive / Failed `--danger`, others neutral. Any column titled "Status" gets it; `abTone(row, label)` overrides the guess |
| Mono cell (`abType: 'mono'`) | Dates, IDs, codes in Roboto Mono 12.5px. Dates DD/MM/YYYY; recent sign-ins "Today, 09:12", "Yesterday"; never "Never" |
| ⋮ menu | [Row actions](#row-actions): `rowActions(row)` returns the items; destructive ones are moved last after a divider automatically |
| Footer | "1–20 of 1,248 users" on the left; "Rows per page" (10 / 20 / 50 / 100, default 20) and ‹ Page 1 of 63 › on the right, 12px muted |
| Loading | 2px indeterminate bar along the top of the table, rows dimmed; first load says "Loading users…" |
| Empty | One row across all columns, `.ab-empty`: "No users yet", or "No users match “term”" while searching |

```html
<app-ab-data-table [source]="source" [columns]="columns" itemName="user" [selectable]="true"
  [rowActions]="rowActionsFor" searchPlaceholder="Search users" [searchFilter]="userSearch"
  (rowClick)="openDetails($event)" (rowAction)="onAction($event)" (selectionChange)="selected = $event">
  <button ab-table-actions class="ab-btn ab-btn--primary"><mat-icon>person_add</mat-icon>Add user</button>
  <button ab-table-bulk class="ab-btn ab-btn--text"><mat-icon>download</mat-icon>Export</button>
</app-ab-data-table>
```

**Columns** keep the angular2-smart-table shape: `title`, `hide`, `valuePrepareFunction(value, cell)`, `type: 'custom'` with `renderComponent` + `componentInitFunction(instance, cell)` (the instance also gets `rowData` and `value`), `type: 'html'`, `isFilterable`, `isSortable`, `sortDirection`, `width`, `class`. Design-system extras: `abType` (`person` / `status` / `mono`), `abPerson(row)`, `abTone(row, label)`.

**Sort**: header click sends the sort as `_sort`/`_order` and `sortColumn`/`sortOrder`. If the page that comes back is not in that order, the endpoint doesn't sort, and `IBEXTNG2ServerDataSource` sorts that column itself from then on (whole list loaded once, then filtered, sorted and paged locally; dropped on refresh). Objects sort by their name (Category → `ContentType.Name`).

**Search** filters one column by default (the first filterable one; placeholder "Search by {column}"). The server ANDs `<field>_like` filters and can't filter on every field, so a table that must search several fields gives `searchFilter(term)` and, where needed, a data source that does the matching. People › Users uses `UsersDataSource` (`people/users-data-source.ts`): with no search it pages on the server; with a search it loads the whole list once (parallel pages), matches **first name, last name, email, role or status** (status as shown: "suspended" finds Inactive users), each word matching any of them ("alex admin"), then sorts and pages locally. The copy is dropped when the search is cleared or the table refreshes after an add, edit, suspend or delete.

**Rules**

- Row actions only in ⋮; nothing on hover; row click opens details only. People › Users' details panel is the model (below): a tinted identity band with a 64px avatar (photo, or initials in white on primary), name 22px / 500, email, status chip and role chips; **Details** and **Activity** tabs; on a `--ab-bg` body, white cards (8px radius) titled with a primary icon and 15px / 500 text: **Account** (username, email, names, status, prefix) and **Profile** (user properties with a value, "4 of 14 set"; empty ones behind "Show N empty fields", shown in italic placeholder "Not set"). Values are full-strength text (#1d2127) at 14px with 12px / 500 labels, so the panel stays crisp.

![User details panel](/assets/images/design-standards/admin/user-details.png)
- Checkbox column only where bulk actions exist. Selection is per page and clears when the page, search or sort changes.
- Counts and ranges use British number format (1,248) and the item noun (`itemName`, `itemNamePlural`).
- Each action label says what it does to what: "Edit details", "Delete user", "Edit in form builder", "Export package".
{% endraw %}
