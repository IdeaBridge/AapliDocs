---
layout: default
title: "Content and copy"
parent: "Admin (AapliAdmin)"
grand_parent: Design Standards
has_children: false
nav_order: 19
permalink: /design-standards/admin/content-copy/
---

{% raw %}
# 8. Content and copy {#8-content-and-copy}

- **British English**: colour, organisation, licence (noun), customise, cancelled.
- **Sentence case** for everything: titles, tabs, buttons, nav items, column headers (the overline style uppercases them visually; write them in sentence case in the source).
- **Dates** DD/MM/YYYY. Times 24-hour. Numbers with thousands separators (1,000).
- **Plain verbs** for actions: Select (not "Click"), Add, Remove, Save, Discard.
- **Second person, present tense**: "Add key/value pairs to this application."
- **Subtitles explain consequences**: what the setting changes and where.
- **Avoid jargon** in labels; put the technical name in mono where it helps admins connect it to the system (`content/get`, `ExportToIFTab`).
- **Errors** follow "what to do" + "the constraint" ([7.2](/design-standards/admin/patterns/#72-validation)).
- **Messages set in code** (toasts, dialog titles and buttons in `.ts` files) follow the same rules as the markup:

| Kind | Rule | Example |
|---|---|---|
| Dialog title | Sentence case, the action or question, no full stop | "Delete banner?", "Change entity", "Weightage required" |
| Dialog buttons | The verb, never "OK" / "Yes" | "Delete banner", "Change type" |
| Success toast | Short past tense, full stop, no "successfully", no "!" | "Banner deleted.", "Teams app package downloaded." |
| Error toast | What happened, then what to do; no "Please" | "We couldn't load the form. Try again.", "Fill in all required fields." |
| Validation toast | The fix | "Choose a ZIP file.", "Choose a JPG, PNG, GIF or WEBP image." |

  When a spec asserts a message, change the spec with the message.
- Don't put real people's names, emails or other personal data in examples, placeholders or screenshots. Use clearly fictional data.
{% endraw %}
