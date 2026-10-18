---
layout: default
title: "Left navigation"
parent: "Admin (AapliAdmin)"
grand_parent: Design Standards
has_children: false
nav_order: 3
permalink: /design-standards/admin/left-navigation/
---

{% raw %}
# 4. Left navigation {#4-left-navigation}

The admin console navigation. **One list** with search and up to **two levels**. Replaces the old Operations / Configurations split.

Component: `<app-side-nav>` (`src/app/_view/_ui-components/side-nav/`). Data: `SettingsService.adminNav`.

## 4.1 Anatomy {#41-anatomy}

![Left navigation anatomy, expanded and collapsed](/assets/images/design-standards/admin/ds-left-nav.svg)

![Left navigation: Data open with Templates active, Others above the pinned General link](/assets/images/design-standards/admin/left-nav.png)

*Current page Data › Templates; Others is the last group; General pinned at the bottom.*

```
┌──────────────────────────────┐
│ Admin settings          [≡]  │  heading (18/500) + collapse toggle (icon button)
│ ┌──────────────────────────┐ │
│ │ 🔍 Search settings    ✕ │ │  search input (.ab-input) with icon and clear button
│ └──────────────────────────┘ │
│ 👥 People                 ⌄ │  group: icon + label + chevron (a <button>)
│ │  Users                     │  second level: label only, indented 42px,
│ │  Roles                     │  with a 1px guide line under the group icon
│ │▓ User properties ▓▓▓▓▓▓▓▓▓│  active page: primary tint + primary text, 500
│ ▦ Applications            ⌄ │  collapsed group
│ ▤ Content                 ⌄ │
│            (scrolls)         │
├──────────────────────────────┤
│ ⚙ General                    │  pinned link: footer, outside the scroll
└──────────────────────────────┘
```

| Part | Spec |
|---|---|
| Container | `--ab-surface-2` background, right border `--ab-line`, padding `16px 8px`, full height, sticky. Width `--ab-nav-w` (264px); collapsed `--ab-nav-w-collapsed` (64px). |
| Heading | `h2`, 18px / 500, single line with ellipsis. Hidden when collapsed. |
| Collapse toggle | 32×32 icon button, `menu_open` when expanded, `menu` when collapsed. Tooltip and `aria-label` "Collapse navigation" / "Expand navigation", `aria-expanded`. |
| Search | Full-width `.ab-input`, 34px left padding for the `search` icon, clear button (`close`, 18px) on the right when there is a query. Placeholder "Search settings". |
| Top-level item | Min-height 38px, padding `9px 12px`, 10px icon gap, `--ab-radius-sm`, `--ab-muted` text, 20px icon. |
| Group header | As a top-level item, plus a 20px `expand_more` chevron on the right that rotates 180° when open. It is a `<button>` with `aria-expanded` and `aria-controls`. |
| Second-level item | Min-height 34px, padding `7px 12px 7px 42px`, 13.5px text, **no icon**. A 1px `--ab-line` guide line runs down the left at 21px. |
| Badge | `.ab-badge` on the right ("New"). One word. |
| Gap between items | 2px. |
| Pinned footer | `ul.ab-nav__pinned` below the scrolling list, top border `--ab-line`, 8px top padding. Holds top-level links (`pinned: true`) that should always be in reach (General). One or two items at most. |

## 4.2 States {#42-states}

![Navigation item states](/assets/images/design-standards/admin/ds-left-nav-states.svg)

| State | Treatment |
|---|---|
| Rest | `--ab-muted` text, transparent background |
| Hover | `rgba(primary, .05)` background, `--ab-fg` text |
| Focus (keyboard) | 2px `--ab-primary` outline, inset (`outline-offset: -2px`) so it is not clipped by the scroll area |
| Active page | `--ab-primary-tint` background, `--ab-primary` text, weight 500, `aria-current="page"` |
| Group containing the active page | Text and icon `--ab-primary`, weight 500, **no fill** (the fill belongs to the page). When the nav is collapsed the group gets the fill instead, because the page itself is hidden. |
| Disabled | 50% opacity, `not-allowed` cursor, `lock` icon on the right, tooltip with the reason (for example "Your licence does not permit adding additional applications"). Still focusable so the tooltip is reachable; `aria-disabled="true"`. |
| Search match | Matching characters wrapped in `<mark class="ab-mark">` (soft yellow) |

## 4.3 Information architecture {#43-information-architecture}

Top level is a small number of **groups**; screens are the **second level**. Current groups, in order:

| Group | Icon | Items |
|---|---|---|
| Organisation | `domain` | Settings† · Billing |
| Applications | `apps` | Applications · Application categories · Entity builder · Evaluation matrix · Features |
| People | `group` | Users · User properties · User import mapping · SSO settings |
| Roles | `admin_panel_settings` | System roles · Custom roles (a screen promoted to a group, see below) |
| Content | `web` | Menu · Pages · Cards · Announcements · Site design |
| Communication | `forum` | Notifications · Email logs |
| Data | `import_export` | Import data · Templates · Export data · Import history (a screen promoted to a group) |
| Integrations | `integration_instructions` | Integrations · Xoxoday · Marketplace |
| Others | `more_horiz` | Failed submissions, plus any screen not yet placed in a group. Always the last group |
| *(pinned)* | `settings` | General, at the bottom of the nav |

† Has a third level shown as a [list with a detail panel](/design-standards/admin/right-panel/#69-feature-list-and-detail-panel): Settings → Company name · Company address · Date format · Number format · Application type (Plus Innovations only) · Currencies (not for asset management).

Old addresses redirect to the new ones (see [4.6](#46-addresses-routes)); for example `/admin/configurations/company-profile` → the Settings list, `/organisation-settings` → Settings › Application type, `/currency-settings` → Settings › Currencies.

Which items appear depends on the app type and licence (`SettingsService.initModulesEnabled`). A group with no enabled items is removed. A group left with one item is still shown as a group, so the nav keeps the same shape across tenants.

**Rules**

- **Two levels in the nav.** When a screen has sub-pages, pick one of three treatments, never two at once, and never a second menu down the left of a screen:
  1. **Promote the screen to a group** when its sub-pages are separate destinations admins go to directly (Roles → System roles, Custom roles; Data → Import data, Templates, Export data, Import history). The screen draws no tabs. Configure it in `ADMIN_NAV_GROUPS` with `screen` and `children`.
  2. **List with a detail panel** when the sub-pages are a set of small, separate settings (Settings → Company name, Date format…). See [6.9](/design-standards/admin/right-panel/#69-feature-list-and-detail-panel).
  3. **In-page tabs** when the sub-pages are views of one thing that admins switch between without leaving it. No admin screen uses this at the moment; see [4.8](#48-third-level-in-page-tabs).
  For 2 and 3, list the sub-pages in `ADMIN_NAV_TABS` so the nav search finds them.
- **5–9 groups.** Each group holds **2–7 items**. If a group grows past 7, split it.
- A top-level **link** (no children) is allowed for a destination used constantly by everyone. Pin it to the bottom (`ADMIN_NAV_PINNED`, as General is) rather than mixing it in with the groups.
- Group order is set by the product owner (currently Organisation, Applications, People, Roles first). Order items within a group by how often admins use them, not alphabetically.
- Labels are nouns, sentence case, 1–3 words, and match the screen's `h1`/`h2` exactly.
- Every item has a `description` (shown as a tooltip and used by search). Add `keywords` for synonyms and old names, so an admin searching "SAML" finds SSO settings.
- **Adding a screen:** add its `SettingItem` to `operationsList` or `configurationsList` in `settings.service.ts` (this keeps the route and module gating), then add its `routerLink` to the right group in `ADMIN_NAV_GROUPS`, and any synonyms to `ADMIN_NAV_KEYWORDS`. A screen not placed in a group is shown under **Others** at the end, which is a reminder to place it, not a home. If the screen has sub-pages, also add them to `ADMIN_NAV_TABS` (see 4.8).

## 4.4 Behaviour {#44-behaviour}

- **Expand / collapse groups** independently; more than one group can be open. The group holding the current page opens itself on load and on navigation. Open groups are remembered per browser.
- **Search** filters as you type (no submit), case-insensitive, across item label, description and keywords, and across both levels.
  - Several words must all match ("user import" finds User import mapping).
  - If a group's own label matches, all its items are shown.
  - Third-level pages (in-page tabs and detail-panel items) are searched too and listed under their group as **Screen › Page** ("Settings › Currencies"), with the screen name muted. Choosing one opens that tab or panel directly. They never appear in the tree when not searching.
  - Every group with a hit is shown open while searching; your own open/closed choices come back when the search is cleared.
  - Matches are highlighted.
  - `Enter` opens the first result and clears the search. `Esc` clears the search. `↓` moves from the search box into the results.
  - No results: "No settings match “query”." with a **Clear search** text button.
  - The result count is announced to screen readers through a polite live region.
- **Collapsed mode** (64px): top-level icons only, each with a tooltip on the right. The search becomes a `search` icon button. Choosing a group or search **expands the nav first** (a group has nothing to show at 64px), then opens the group or focuses the search. Collapsed / expanded is remembered per browser.
- **Keyboard:** `Tab` moves through the nav as normal. Inside the list, `↑` / `↓` move between visible items, `Home` / `End` jump to the first / last, and `↑` from the first item returns to search. `Enter` / `Space` open a link or toggle a group.
- Choosing an item emits `navigate`, which the admin console uses to show its loading overlay.

## 4.5 API {#45-api}

```html
<app-side-nav
  heading="Admin settings"
  ariaLabel="Admin settings"
  searchPlaceholder="Search settings"
  storageKey="adminConsole.nav"
  [items]="adminNav"
  [(collapsed)]="sidebarCollapsed"
  (navigate)="showNavigationLoader()">
</app-side-nav>
```

| Input / output | Type | Notes |
|---|---|---|
| `items` | `SideNavNode[]` | Top level. A node with `children` is a group; otherwise it needs `routerLink`. |
| `heading` | `string` | Optional heading above the search. |
| `searchPlaceholder` | `string` | Also the search box's accessible name. |
| `collapsible` | `boolean` | Default `true`. |
| `collapsed` / `collapsedChange` | `boolean` | Two-way. The parent uses it to size its column. |
| `storageKey` | `string` | Prefix for remembered state (`<key>.expanded`, `<key>.collapsed`). Empty: remember nothing. |
| `ariaLabel` | `string` | Accessible name of the `<nav>`. |
| `navigate` | `EventEmitter<SideNavNode>` | Fires when a link is chosen. |

```ts
interface SideNavNode {
  id: string;              // stable; not derived from the label
  label: string;
  icon?: string;           // required on top-level nodes
  routerLink?: string;
  description?: string;    // tooltip + search
  keywords?: string[];     // search only
  exact?: boolean;         // active only on this exact URL
  children?: SideNavNode[]; // group: its screens. screen: its in-page tabs (search only)
  disabled?: boolean;
  disabledTooltip?: string;
  badge?: string;          // one word, e.g. 'New'
  pinned?: boolean;        // top level only: shown in the footer below the scrolling list
}
```

## 4.6 Addresses (routes) {#46-addresses-routes}

There is no admin home page: `/` and `/admin` open the first item in the nav (Organisation › Settings). Admin addresses follow the nav: **`/admin/<group>/<screen>`**, lower case, hyphenated, nouns. A group's own address redirects to its first screen. Third-level pages add one more segment.

| Group | Addresses |
|---|---|
| Organisation | `organisation/settings` (areas: `organisation/settings/<area>`, e.g. `…/currencies`), `organisation/billing` |
| Applications | `applications/list`, `applications/categories`, `applications/entity-builder`, `applications/evaluation-matrix`, `applications/features` |
| People | `people/users`, `people/user-properties`, `people/user-import-mapping`, `people/sso` |
| Roles | `roles/system`, `roles/custom` |
| Content | `content/menu`, `content/pages`, `content/cards`, `content/announcements`, `content/site-design` (areas: `content/site-design/<area>`) |
| Communication | `communication/notifications`, `communication/email-logs` |
| Data | `data/import`, `data/templates`, `data/export`, `data/history`, `data/history/:fileId` |
| Integrations | `integrations/connections`, `integrations/xoxoday`, `integrations/marketplace` |
| Others | `others/failed-submissions` |
| Pinned | `general` |

**Rules**

- When a screen moves in the nav, its address moves with it, and the old address gets a redirect at the bottom of the admin routes in `app-routing.module.ts`. Never delete an old address: bookmarks and links in emails still use it. (Every pre-redesign `operations/…` and `configurations/…` address redirects.)
- **Every redirect uses `pathMatch: "full"`.** A prefix redirect on a parent segment (as `configurations` once was) captures every address under it and silently breaks those links.
- Write addresses in one place. Nav links live in `settings.service.ts`; screens that link to another screen use a constant (as `ImportRoutes` does) rather than a string literal.
- Guards check the address **after** redirects, so the asset management allow list (`AuthGuard`) lists new addresses only.
- Screens that are not in the nav (Import data upload, Reports, Application settings, SMS) keep their old addresses until they are given a place.

## 4.7 Don't {#47-dont}

- Don't split the nav into tabs or separate lists (Operations / Configurations). One list.
- Don't draw a third level in the nav, and don't put icons on second-level items.
- Don't put actions ("Add user") in the nav. The nav is for places.
- Don't hide an item the admin is not licensed for if they would reasonably look for it; show it disabled with the reason.
- Don't style the nav per screen. Change the component and this section.

## 4.8 Third level: in-page tabs {#48-third-level-in-page-tabs}

When a screen's sub-pages are views of one thing that admins switch between without leaving it, the nav keeps one entry for the screen and the sub-pages appear as a **tab bar across the top of the screen**. (For the other two treatments, promoted group and list with a detail panel, see the rules in 4.3.) This keeps the nav short and stable, works when the nav is collapsed, and gives each sub-page its own URL so links and the browser back button work.

![Example of in-page tabs (Import export used this before it became a nav group)](/assets/images/design-standards/admin/in-page-tabs.png)

```html
<nav class="ab-tabs" aria-label="Example">
  <a class="ab-tab" routerLink="/admin/example/overview" routerLinkActive="is-active"
     [routerLinkActiveOptions]="{ exact: true }" ariaCurrentWhenActive="page">
    <mat-icon aria-hidden="true">dashboard</mat-icon>Overview
  </a>
  <a class="ab-tab" routerLink="/admin/example/history" routerLinkActive="is-active"
     ariaCurrentWhenActive="page">
    <mat-icon aria-hidden="true">history</mat-icon>History
  </a>
</nav>
<router-outlet></router-outlet>
```

- Same look as the [main tabs](/design-standards/admin/layout/#34-main-tabs--ab-tabs--ab-mat-tabs): 20px icon + label, muted, primary text and 2px underline when active.
- They are links (`<a routerLink>`), not buttons, because each tab is a page. The screen's own URL is the first tab and is matched exactly.
- The nav entry for the screen stays active on every tab (its URL is a prefix of theirs).
- 2–6 tabs, sentence case nouns. The tooltip carries the tab's description.
- List the tabs in `ADMIN_NAV_TABS` (`settings.service.ts`) so nav search finds them. Prefer drawing the tab bar from `SettingsService.navTabsFor(link)`, which also applies `enableKey` and `excludeAppTypes`, so the bar and the search can never disagree. 
- A tab the tenant can't use is left out, not shown disabled.
- No fourth level. If a tab needs sub-sections, use a [section rail](/design-standards/admin/section-rail/#5-section-rail) inside it.

**Every third level is searchable, whatever its treatment.** The same `ADMIN_NAV_TABS` list feeds tabs *and* list + detail panel screens: Organisation › Settings (its six areas), Content › Site design (Logo and favicon, Homepage banners, Website branding, Homepage widgets, Custom CSS) and Integrations › Connections (Microsoft Teams app). The screen draws its list from `navTabsFor(link)` and opens the panel from the URL (`<screen>/<area>`, componentless `:area` child routes), so a search result lands on the open panel. Per-item conditions are fields on the entry: `enableKey`, `excludeAppTypes`, `superAdminOnly`. A list screen whose items are data (Features, Marketplace) is not listed; its own page has a search box.
{% endraw %}
