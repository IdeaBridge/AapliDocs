---
layout: default
title: "Pull request checklist"
parent: "Admin (AapliAdmin)"
grand_parent: Design Standards
has_children: false
nav_order: 22
permalink: /design-standards/admin/pr-checklist/
---

{% raw %}
# 11. Pull request checklist {#11-pull-request-checklist}

Copy into the PR description for any admin UI change.

- [ ] Screen root has `.ab-theme`; new markup uses `.ab-*` classes.
- [ ] No hard-coded colours, font sizes or spacing; tokens only.
- [ ] One primary button per view, on the right of the action bar.
- [ ] Every pane has an `h2.ab-title` and an `.ab-sub` that explains consequences.
- [ ] Text is British English, sentence case; dates DD/MM/YYYY.
- [ ] Lists of records use `app-ab-data-table`, not a hand-built or third-party table.
- [ ] Table rows: one always-visible ⋮ menu for actions; row click opens details only; nothing appears on hover.
- [ ] Icons on coloured backgrounds inherit the text colour (no dark icons on primary buttons).
- [ ] All interactive elements are `<button>`/`<a>`; icon-only buttons have `aria-label` + tooltip.
- [ ] Keyboard: reachable, visible focus, arrow keys in lists and rails, `Esc` clears search.
- [ ] Validation messages under the field, say what to do, and Save explains why it is disabled.
- [ ] Empty, loading and error states designed.
- [ ] Works at 1100px and 760px widths with no page-level horizontal scroll.
- [ ] On/off capabilities use the feature list and detail panel (no switches that save on click).
- [ ] New sub-page, list area or panel: listed in `ADMIN_NAV_TABS` with its own address, so nav search finds it.
- [ ] New nav item: added to a group in `ADMIN_NAV_GROUPS`, with `description` and keywords, at an address that follows the nav (4.6).
- [ ] Moved screen: old address redirects with `pathMatch: "full"`.
- [ ] No real personal data in examples, fixtures or screenshots.
- [ ] This document updated if a token, component or rule changed (and changelog entry added).
{% endraw %}
