---
layout: default
title: "Accordions"
parent: "Admin (AapliAdmin)"
grand_parent: Design Standards
has_children: false
nav_order: 17
permalink: /design-standards/admin/accordions/
---

{% raw %}
# 6.17 Accordions {#617-accordions}

![Accordion groups](/assets/images/design-standards/admin/ds-accordion.svg)


Collapsible groups in the form builder and entity builder palettes and property columns (`cdk-accordion`).

- **Open by default:** every group starts expanded (`[multi]="true"`, `[expanded]="true"`); people collapse what they don't need.
- Header: 11px / 500 uppercase `.06em`, muted, with an expand / collapse chevron; the header is a real button.
- **No hover background** on the header (a global rule in `_components.scss` clears it); focus still shows the focus ring.
{% endraw %}
