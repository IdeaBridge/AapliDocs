---
layout: default
title: "Notes, code and status flag"
parent: "Admin (AapliAdmin)"
grand_parent: Design Standards
has_children: false
nav_order: 13
permalink: /design-standards/admin/notes-code-flag/
---

{% raw %}
# 6.10 Notes — `.ab-note` {#610-notes--ab-note}

![Note variants and API preview](/assets/images/design-standards/admin/ds-notes-code.svg)

Explanatory or policy text below the main content ("Rules in this prototype").

- `--ab-surface-2`, 1px border, `--ab-radius-sm`, padding `14px 16px`, muted text at 1.55 line height, `max-width: 70ch`, 22px top margin. `<b>` and `<code>` inside use `--ab-fg`.
- Variants add a 3px left bar: `--info` (primary), `--warn` (warn colour and tint), `--danger` (danger colour and tint).
- A note is for things the user should know, not something they must act on now. For that, use inline validation or a dialog.

# 6.11 Code and API preview {#611-code-and-api-preview}

| Class | Spec |
|---|---|
| `.ab-endpoint` | Mono 12px. `.ab-endpoint__method` in `--ab-ok`, 500, 6px right margin. `GET /api/content/get?id=1042` |
| `.ab-code` (`pre`) | `--ab-code-bg`, `--ab-code-fg`, mono 12px, line height 1.6, padding 14px, `--ab-radius-sm`, scrolls horizontally, `white-space: pre`. Keys `<span class="k">`, strings `<span class="s">` |

- Previews reflect the **saved** state, not unsaved edits, so they show what other systems really see. Say so in the overline ("Returned by content/get").
- Elide unrelated fields with `…`.
- Escape everything you interpolate into a preview.

# 6.12 Status flag — `.ab-flag` {#612-status-flag--ab-flag}

A row explaining the effect of the current settings ("Export to IF tab: shown").

- 1px border, `--ab-radius-sm`, padding `12px 14px`, 10px gap.
- `.ab-flag__dot` 10px circle: muted by default, `--ab-ok` with `.is-on`, `--ab-danger` with `.is-error`.
- `.ab-flag__title` 500; `.ab-flag__desc` 12px muted, explains **why** ("The front end finds ExportToIFTab = true in the saved properties, so the tab appears.").
{% endraw %}
