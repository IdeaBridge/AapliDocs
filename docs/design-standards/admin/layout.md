---
layout: default
title: "Layout"
parent: "Admin (AapliAdmin)"
grand_parent: Design Standards
has_children: false
nav_order: 2
permalink: /design-standards/admin/layout/
---

{% raw %}
# 3. Layout {#3-layout}

![Workspace layout: app bar, main tabs, section rail, pane, aside and action bar](/assets/images/design-standards/admin/ds-layout-shell.svg)

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ LEFT NAV │  ┌ SHELL ─────────────────────────────────────────────────────┐   │
│ (264px / │  │ APP BAR   [icon] Title  (chip)              [Preview] [x]  │   │
│  64px)   │  ├────────────────────────────────────────────────────────────┤   │
│          │  │ MAIN TABS  Overview  Design  Workflow  Tasks  Properties   │   │
│ Search   │  ├──────────┬─────────────────────────────────────────────────┤   │
│ ▸ Group  │  │ SECTION  │ PANE                          │ ASIDE (340px)   │   │
│ ▾ Group  │  │ RAIL     │ h2 Title                      │ OVERLINE        │   │
│    Item  │  │ (260px)  │ Subtitle                      │ preview / help  │   │
│    Item  │  │          │ [toolbar]                     │                 │   │
│ ▸ Group  │  │          │ content                       │                 │   │
│          │  ├──────────┴─────────────────────────────────────────────────┤   │
│          │  │ ACTION BAR  [Back]                [Cancel] [Next] [Save]   │   │
│          │  └────────────────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────────────────────────┘
```

Not every screen uses every region. A simple settings screen is: left nav → pane (title, subtitle, content, inline action bar).

![Form builder workspace: app bar, main tabs, section rail, pane with aside, sticky action bar](/assets/images/design-standards/admin/workspace-shell.png)

*Reference render of the shell (form builder › Properties) with fictional data.*

## 3.1 Theme root — `.ab-theme` {#31-theme-root--ab-theme}

Put `.ab-theme` on the outermost element of a redesigned screen. It:

- sets the Roboto type, 14px base size, `--ab-fg` text colour and a box-sizing reset;
- re-points `--primaryColor`, `--primaryColorRGBA` and `--paragraphColor` at the admin tokens;
- aligns Angular Material controls (checkbox, radio, slide toggle, slider, tabs, form field, spinner) with the admin colours;
- turns on the [legacy bridge](/design-standards/admin/angular/#104-legacy-bridge) for older classes inside it;
- adds the standard focus ring to anything focused by keyboard.

## 3.2 Page and shell {#32-page-and-shell}

| Class | Spec |
|---|---|
| `.ab-page` | `background: --ab-bg`, padding 16px. Wraps a framed shell. |
| `.ab-shell` | Framed: `--ab-surface`, 1px `--ab-line` border, `--ab-radius-md`, overflow hidden. Use inside the admin console. |
| `.ab-shell--full` | Full-bleed: no border, radius or overflow clipping. Use for full-screen editors (the form builder). Clipping is removed so a sticky action bar inside still sticks. |

## 3.3 App bar — `.ab-appbar` {#33-app-bar--ab-appbar}

The identity row of a workspace.

- Padding `12px 20px`, min-height 56px, bottom border, `flex-wrap: wrap`, 12px gap.
- Order, left to right: **icon** (`.ab-appbar__icon`, primary colour) → **title** → **context chips** → spacer (`.ab-spacer`) → **secondary actions** (stroked buttons, e.g. Preview) → **close** (icon button, last).
- Title is an `h1.ab-appbar__title` (18px / 500). Where the name is editable in place, use `input.ab-appbar__title-input`: it looks like the heading until hovered (border) or focused (primary border, white background). It needs a visually hidden `<label>` and a placeholder ("Untitled application").
- Chips describe context, not state that changes often: "Content type: RPG Application".
- The app bar does **not** hold Save. Save lives in the action bar.

## 3.4 Main tabs — `.ab-tabs` / `.ab-mat-tabs` {#34-main-tabs--ab-tabs--ab-mat-tabs}

![Main tabs: active, error and hover states](/assets/images/design-standards/admin/ds-tabs.svg)

The top-level sections of a workspace (Overview, Design, Workflow…).

- Row: `0 12px` padding, 4px gap, bottom border, horizontal scroll if it overflows (never wraps).
- Tab: icon (20px) + label, `12px 14px` padding, `--ab-muted` text, 2px transparent bottom border.
- Hover: text `--ab-fg`. Active: text and 2px underline `--ab-primary`, weight 500.
- A tab whose content has a validation problem shows a 6px `--ab-danger` dot after its label (`.has-error`, or `.taberror` in the form builder). Give the user the reason inside the tab; the dot only says where to look.
- With Angular Material put `class="ab-mat-tabs"` on `<mat-tab-group>` and use `animationDuration="0ms"`, `[stretchTabs]="false"`, `disableRipple`. With plain markup use `div.ab-tabs[role=tablist] > button.ab-tab[role=tab][aria-selected]`.
- 3–8 tabs. If you need more, the workspace is doing too much; move secondary areas into the section rail of one tab.

## 3.5 Body — `.ab-body` {#35-body--ab-body}

Grid of `260px` section rail + flexible pane (`--ab-rail-w`). See [Section rail](/design-standards/admin/section-rail/#5-section-rail).

## 3.6 Page frame and title {#36-page-frame-and-title}

![Page frame: title 24px from the top and 28px from the nav](/assets/images/design-standards/admin/ds-page-frame.svg)

Every admin screen's header sits at the same place in the same type, whatever link opened it.

| Property | Value |
|---|---|
| Frame | `.admin-content` in the admin console, padding **24px top, 28px left and right, 32px bottom** (`--ab-space-6` / `--ab-space-7` / `--ab-space-8`) |
| Title position | Top of the title's line box 24px below the top of the content area, left edge 28px from the left nav |
| Title | `h2.ab-title`: Roboto (`--ab-font-ui`), **17px**, weight **500**, line height 1.25 (21px), `--ab-fg`, no top margin, 4px bottom margin, `text-wrap: balance` |
| Description | `p.ab-sub`: Roboto, **14px**, weight 400, line height 1.5, `--ab-muted`, full width, 18px bottom margin |
| Then | Toolbar (search, count, actions) → content |

**Rules**

- The frame owns the gutter. A screen adds **no outer padding or margin** and starts directly with its title. Bootstrap `.container`/`.container-fluid` wrappers, `.px-*` and `.col` at a screen's root have their side padding removed by the frame, and anything above the title loses its top margin.
- One `h2` page title per screen. Use `h3` and smaller for sections within the page (`h2`s inside a screen are restyled as page titles).
- Shells that hold sub-pages (Roles, Data) add no padding either; their screens follow the same rule.
- Detail panels, dialogs and previews keep their own title styles (the frame rules exclude `.ab-panel`, `[class*="modal"]` and `[class*="preview"]`).
- Implementation: `src/scss/design-system/_page-frame.scss`. Its resets exist for older screens and use `!important` to beat Bootstrap utilities such as `mt-*`; remove a reset once nothing needs it.

- **Subtitles run the full width of their section** (page, panel header, settings section). Don't cap them at a character width.

## 3.6.1 Pane — `.ab-pane` {#361-pane--ab-pane}

- Inside the frame, a pane needs no padding of its own (`.ab-pane` keeps `24px 28px` only for use outside the admin console, e.g. the form builder's Properties tab).
- `.ab-pane--with-aside`: two columns, content + 340px aside (`--ab-aside-w`), 28px gap. Collapses to one column at ≤ 1100px.
- Starts with `h2.ab-title` and `p.ab-sub`. Then, in order: toolbar → content → inline action bar → notes.

## 3.7 Aside — `.ab-aside` {#37-aside--ab-aside}

Supporting information that reacts to what is being edited: an API preview, a live preview, a help panel. Never required to complete the task. Heading is an `h3.ab-overline` with a 16px icon.

## 3.8 Action bar — `.ab-actionbar` {#38-action-bar--ab-actionbar}

![Sticky action bar, button order and status text](/assets/images/design-standards/admin/ds-action-bar.svg)

Where the user commits or abandons work.

- `--sticky`: pinned to the bottom of the viewport with top border, `12px 20px` padding. Use for multi-tab workspaces (the form builder).
- `--inline`: no border or padding, 18px top margin. Use under a single form in a pane.
- **Order:** navigation back on the far left (text button) → spacer → Cancel / Discard (stroked) → Next (stroked) → **primary action last, far right** (Save). Exactly one primary button.
- Status text (`.ab-status`, 12px muted) sits next to the buttons: "Unsaved changes", "All changes saved", "2 rows need fixing before you can save".
{% endraw %}
