---
layout: default
title: "Toast, empty, loading and error"
parent: "Admin (AapliAdmin)"
grand_parent: Design Standards
has_children: false
nav_order: 14
permalink: /design-standards/admin/feedback/
---

{% raw %}
# 6.13 Toast — `.ab-toast` {#613-toast--ab-toast}

![Toast, empty, loading and error states](/assets/images/design-standards/admin/ds-feedback.svg)

Confirmation that something finished.

- Fixed, centred, 20px above the bottom (plus safe area), `--ab-fg` background with `--ab-surface` text, `10px 16px`, `--ab-radius-sm`, `check_circle` icon (18px).
- Short past-tense sentence: "Custom properties saved". Disappears after about 2.2 seconds; never the only place an error is reported.
- In Angular use the existing snackbar/toastr service, configured to this look, rather than hand-rolling `.ab-toast` per screen. Errors use the danger colour and stay until dismissed.

# 6.14 Empty, loading and error states {#614-empty-loading-and-error-states}

- **Empty**: `.ab-empty` (centred muted text, 28px padding). Say what would be here and how to add it.
- **Loading**: skeletons (`ngx-skeleton-loader`) shaped like the content for first load; a 44px `mat-spinner` overlay only for full-panel waits (the admin console overlay); an inline 18px spinner in the button for save. Don't show a spinner for under 250ms.
- **Error loading**: a `.ab-note--danger` in the pane with what failed and a **Try again** stroked button.
{% endraw %}
