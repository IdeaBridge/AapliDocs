---
layout: default
title: "Dialogs"
parent: "Admin (AapliAdmin)"
grand_parent: Design Standards
has_children: false
nav_order: 15
permalink: /design-standards/admin/dialogs/
---

{% raw %}
# 6.15 Dialogs — modal confirmation {#615-dialogs--modal-confirmation}

![Modal confirmation with its spacing](/assets/images/design-standards/admin/ds-dialog.svg)

Every confirmation and small form in a modal uses the shared `app-default-dialog` (`DefaultDialogService`), which implements this pattern. Dialogs and select panels get `.ab-theme` by default (`MAT_DIALOG_DEFAULT_OPTIONS`, `MAT_SELECT_CONFIG` in `app.module.ts`).

| Modal attribute | Value |
|---|---|
| Heading | Roboto, 18px / 500, line height 24px, `--ab-fg` |
| Body | Roboto, 14px / 400, line height 21px |
| Outer padding | 24px, all sides (one white box, 8px corners; no header band, no footer rule) |
| Heading → body | 16px |
| Body → action row | 24px |
| Between buttons | 8px |
| Actions | Right aligned: **Cancel** (stroked), then the primary action (primary) or a destructive action (danger-solid) |
| Heading wording | Sentence case, action-based: "Discard changes?", "Delete property?" |
| Close | Optional round icon button top right (`ab-btn--icon`), same as Cancel |
| Status icon | Optional 24px icon before the heading or message: info (primary), warning (warn), delete (danger) |

- Body says what will happen and whether it can be undone.
- The action button repeats the verb ("Discard", "Delete property"), never "OK" / "Yes".
- Width: `small` 20vw, `medium` 40vw (default), `large` 60vw, `x-large` 80vw; full width at ≤ 768px. Minimum 360px.
- A dialog that edits several fields uses the normal [form fields](/design-standards/admin/form-fields/#63-form-fields) in the body; anything longer than a short form belongs in a [right panel](/design-standards/admin/right-panel/#69-feature-list-and-detail-panel), not a modal.
{% endraw %}
