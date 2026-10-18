---
layout: default
title: "Patterns"
parent: "Admin (AapliAdmin)"
grand_parent: Design Standards
has_children: false
nav_order: 18
permalink: /design-standards/admin/patterns/
---

{% raw %}
# 7. Patterns {#7-patterns}

## 7.1 Editing and saving {#71-editing-and-saving}

- Changes are held locally until **Save**. Show `.ab-status` beside the buttons:
  - "All changes saved" (nothing to save, Save disabled),
  - "Unsaved changes" (Save enabled),
  - "N rows need fixing before you can save" (Save disabled, problems highlighted).
- **Discard changes** (stroked) restores the last saved state.
- After saving, show a toast and update any preview from the saved data.
- Leaving with unsaved changes asks for confirmation (route `canDeactivate` guard).

## 7.2 Validation {#72-validation}

- Validate as the user types, but only show an error once a field has been touched or Save has been attempted.
- The error appears directly under the field (`.ab-error`) and the field gets `.is-invalid` / `aria-invalid="true"`.
- Messages say what to do, not what went wrong: "Enter a key.", "Use letters, numbers, _ - or . only.", "This key is already used above.", "Keys can be up to 100 characters."
- Uniqueness checks are case-insensitive unless the backend says otherwise.
- A tab with an error shows the red dot on its tab ([3.4](/design-standards/admin/layout/#34-main-tabs--ab-tabs--ab-mat-tabs)).

## 7.3 Destructive actions {#73-destructive-actions}

- Removing a row in an unsaved list needs no confirmation: it can be undone with Discard changes.
- Deleting something already saved, or anything that cannot be undone, needs a dialog ([6.15](/design-standards/admin/dialogs/#615-dialogs--modal-confirmation)).

## 7.4 Search and filter {#74-search-and-filter}

![Search field, highlighted matches and no results](/assets/images/design-standards/admin/ds-search.svg)

- Filter as you type; no search button.
- Search field: `.ab-input` with a leading `search` icon and a clear button once there is text. `Esc` clears.
- Highlight matches with `.ab-mark`. Announce the result count to screen readers.
- No results: say so with the query in quotes and offer a way to clear it.
{% endraw %}
