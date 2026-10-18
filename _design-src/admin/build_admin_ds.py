"""Builds the AapliDocs pages for the Aapli Admin design system, with visuals.

Source of truth: AapliAdmin docs/DESIGN_SYSTEM.md (branch redesign). This script never edits it.
Usage: python3 build_admin_ds.py <path to DESIGN_SYSTEM.md> <AapliDocs root>

Writes:
  docs/design-standards/design-standards.md            section landing page
  docs/design-standards/admin/*.md                     one Jekyll page per section / component
  docs/design-standards/admin/DESIGN_SYSTEM.md          single-file copy with the visuals (no front matter)
Images are expected in assets/images/design-standards/admin/ (ds-*.svg from gen_ds_svgs.py plus the
screenshots copied from AapliAdmin docs/design-system/)."""
import re, sys, os

SRC, ROOT = sys.argv[1], sys.argv[2]
IMG = '/assets/images/design-standards/admin/'
PROTO = '/assets/design-standards/admin/prototypes/'
BASE = '/design-standards/admin/'
SEC, PARENT = 'Design Standards', 'Admin (AapliAdmin)'

src = open(SRC, encoding='utf-8').read().replace('\r\n', '\n')
# known broken link in the source (heading is '6.7 Cards — `.ab-card`')
src = src.replace('](#67-cards)', '](#67-cards--ab-card)')
lines = src.split('\n')

def anchor(text):
    a = text.strip().lower()
    a = re.sub(r'[^\w\- ]', '', a)
    return a.replace(' ', '-')

# ---- headings
heads = []
in_code = False
for i, ln in enumerate(lines):
    if ln.startswith('```'): in_code = not in_code
    m = None if in_code else re.match(r'^(#{1,6}) (.+)$', ln)
    if m: heads.append((i, len(m.group(1)), m.group(2)))

def line_of(prefix):
    for i, lvl, t in heads:
        if t.startswith(prefix): return i
    raise KeyError(prefix)

# ---- page plan: (slug, nav title, first heading prefix, heading prefix where the next page starts)
PLAN = [
    ('admin', PARENT, 'Aapli Admin design system', '2. Foundations'),
    ('foundations', 'Foundations', '2. Foundations', '3. Layout'),
    ('layout', 'Layout', '3. Layout', '4. Left navigation'),
    ('left-navigation', 'Left navigation', '4. Left navigation', '5. Section rail'),
    ('section-rail', 'Section rail', '5. Section rail', '6. Components'),
    ('headings-text', 'Headings and text', '6. Components', '6.2 Buttons'),
    ('buttons', 'Buttons', '6.2 Buttons', '6.3 Form fields'),
    ('form-fields', 'Form fields', '6.3 Form fields', '6.4 Selection controls'),
    ('selection-controls', 'Selection controls', '6.4 Selection controls', '6.5 Tables'),
    ('tables', 'Tables and data table', '6.5 Tables', '6.6 Chips and badges'),
    ('chips-cards', 'Chips, badges and cards', '6.6 Chips and badges', '6.8 Settings section'),
    ('settings-section', 'Settings section', '6.8 Settings section', '6.9 Feature list'),
    ('right-panel', 'Feature list and right panel', '6.9 Feature list', '6.10 Notes'),
    ('notes-code-flag', 'Notes, code and status flag', '6.10 Notes', '6.13 Toast'),
    ('feedback', 'Toast, empty, loading and error', '6.13 Toast', '6.15 Dialogs'),
    ('dialogs', 'Dialogs', '6.15 Dialogs', '6.16 Stats'),
    ('stats', 'Stats', '6.16 Stats', '6.17 Accordions'),
    ('accordions', 'Accordions', '6.17 Accordions', '7. Patterns'),
    ('patterns', 'Patterns', '7. Patterns', '8. Content and copy'),
    ('content-copy', 'Content and copy', '8. Content and copy', '9. Accessibility'),
    ('accessibility', 'Accessibility', '9. Accessibility', '10. Implementing in Angular'),
    ('angular', 'Implementing in Angular', '10. Implementing in Angular', '11. Pull request checklist'),
    ('pr-checklist', 'Pull request checklist', '11. Pull request checklist', '12. Adoption status'),
    ('adoption', 'Adoption status', '12. Adoption status', '13. Changelog'),
    ('changelog', 'Changelog', '13. Changelog', None),
]

# ---- visuals: inserted straight after the heading that starts with the key
VISUALS = {
    '2.1 Colour': [('ds-colour', 'Colour tokens with their values and uses')],
    '2.2 Typography': [('ds-type', 'Type scale')],
    '2.3 Spacing': [('ds-spacing-shape', 'Spacing scale, radius and icon sizes')],
    '3. Layout': [('ds-layout-shell', 'Workspace layout: app bar, main tabs, section rail, pane, aside and action bar')],
    '3.4 Main tabs': [('ds-tabs', 'Main tabs: active, error and hover states')],
    '3.6 Page frame and title': [('ds-page-frame', 'Page frame: title 24px from the top and 28px from the nav')],
    '3.8 Action bar': [('ds-action-bar', 'Sticky action bar, button order and status text')],
    '4.1 Anatomy': [('ds-left-nav', 'Left navigation anatomy, expanded and collapsed')],
    '4.2 States': [('ds-left-nav-states', 'Navigation item states')],
    '5. Section rail': [('ds-section-rail', 'Section rail with active, hover and badge')],
    '6.2 Buttons': [('ds-buttons', 'Button variants in every state')],
    '6.3 Form fields': [('ds-text-box-anatomy', 'Text box anatomy'), ('ds-text-box-states', 'Text box states'), ('ds-dropdown', 'Dropdown: closed, selected, invalid and open')],
    '6.4 Selection controls': [('ds-selection', 'Checkbox, radio and slide toggle')],
    '6.5 Tables': [('ds-table', 'Table anatomy and row height')],
    'Row actions': [('ds-row-menu', 'Row actions: one always-visible menu per row')],
    '6.5.1 Data table': [('ds-data-table', 'Data table: toolbar, person cell, status chips, footer and bulk bar')],
    '6.6 Chips and badges': [('ds-chips-cards', 'Chips, badge, cards and status flag')],
    '6.8 Settings section': [('ds-settings-section', 'Settings section in view and edit mode')],
    '6.9 Feature list': [('ds-feature-list', 'Feature list anatomy'), ('ds-right-panel', 'Right-hand panel anatomy'), ('ds-panel-variants', 'Panel widths and variants')],
    '6.10 Notes': [('ds-notes-code', 'Note variants and API preview')],
    '6.13 Toast': [('ds-feedback', 'Toast, empty, loading and error states')],
    '6.15 Dialogs': [('ds-dialog', 'Modal confirmation with its spacing')],
    '6.16 Stats': [('ds-stats', 'Stats tiles')],
    '6.17 Accordions': [('ds-accordion', 'Accordion groups')],
    '7.4 Search and filter': [('ds-search', 'Search field, highlighted matches and no results')],
}

PROTOTYPES = [('points-prototypes.html', 'Points'), ('roles-permissions-prototypes.html', 'Roles and permissions'), ('settings-value-prototypes.html', 'Settings values'),
              ('table-actions-prototypes.html', 'Table row actions'), ('tasks-prototypes.html', 'Assign tasks')]

# anchor -> page slug
starts = [(line_of(p[2]), p[0]) for p in PLAN]
def slug_for_line(i):
    s = PLAN[0][0]
    for st, sl in starts:
        if i >= st: s = sl
    return s
anchor_page = {anchor(t): slug_for_line(i) for i, lvl, t in heads}

def visual_md(key, img_prefix):
    out = []
    for k, items in VISUALS.items():
        if key.startswith(k):
            for name, alt in items:
                out.append(f'![{alt}]({img_prefix}{name}.svg)')
            break
    return out

def transform(chunk_start, chunk_end, mode, slug=None, img_prefix=IMG):
    """mode 'page' (Jekyll page) or 'single' (one file)."""
    out = []
    in_code = False
    shift = None
    for i in range(chunk_start, chunk_end):
        ln = lines[i]
        if ln.startswith('```'): in_code = not in_code
        if not in_code:
            m = re.match(r'^(#{1,6}) (.+)$', ln)
            if m:
                lvl, text = len(m.group(1)), m.group(2)
                if mode == 'page':
                    if shift is None: shift = lvl - 1
                    nl = max(1, lvl - shift)
                    ln = '#' * nl + ' ' + text + ' {#' + anchor(text) + '}'
                out.append(ln)
                vis = visual_md(text, img_prefix)
                if vis:
                    out.append('')
                    for v in vis: out.extend([v, ''])
                continue
            # existing screenshots
            ln = re.sub(r'\]\(design-system/([\w\-]+\.png)\)', lambda mm: f']({img_prefix}{mm.group(1)})', ln)
            if mode == 'page':
                def fix(mm):
                    a = mm.group(1)
                    pg = anchor_page.get(a)
                    if pg is None: return mm.group(0)
                    if pg == slug: return f'](#{a})'
                    return f']({BASE}{"" if pg == "admin" else pg + "/"}#{a})' if pg != 'admin' else f']({BASE}#{a})'
                ln = re.sub(r'\]\(#([\w\-]+)\)', fix, ln)
        out.append(ln)
    # trim trailing rules / blank lines
    while out and out[-1].strip() in ('', '---'): out.pop()
    while out and out[0].strip() in ('', '---'): out.pop(0)
    return out

os.makedirs(os.path.join(ROOT, 'docs', 'design-standards', 'admin'), exist_ok=True)

with open(os.path.join(ROOT, 'docs', 'design-standards', 'design-standards.md'), 'w', encoding='utf-8') as f:
    f.write(f"""---
layout: default
title: {SEC}
has_children: true
nav_order: 5
permalink: /design-standards/
---

# Design Standards

UI standards for developers building Aapli screens: tokens, layout, components and their states, copy,
accessibility and a pull-request checklist, with a diagram for each pattern.

| Standard | Applies to |
|---|---|
| [{PARENT}]({BASE}) | The admin console (left navigation) and the form builder in AapliAdmin |
""")

ver = re.search(r'\*\*Status:\*\*\s*(.+)', src).group(1).strip()
page_links = '\n'.join(f'| [{t}]({BASE}{s}/) |' for s, t, a, b in PLAN[1:])

for idx, (slug, title, first, nxt) in enumerate(PLAN):
    a = line_of(first)
    b = line_of(nxt) if nxt else len(lines)
    body = transform(a, b, 'page', slug)
    if slug == 'admin':
        # replace the source's table of contents with links to the pages
        txt = '\n'.join(body)
        txt = re.sub(r'## Contents \{#contents\}.*?(?=\n## )', '## Contents {#contents}\n\n| Page |\n|---|\n' + page_links + '\n', txt, flags=re.S)
        txt = txt.replace('# Aapli Admin design system {#aapli-admin-design-system}', '# Aapli Admin design system {#aapli-admin-design-system}', 1)
        note = (f'\n> This is the developer copy of `docs/DESIGN_SYSTEM.md` in the AapliAdmin repository (branch `redesign`), '
                f'split into pages and illustrated with a diagram for each pattern. The AapliAdmin file is the source of truth: '
                f'change it first, then regenerate these pages with `_design-src/admin/build_admin_ds.py`.\n')
        txt = txt.replace('\n---\n', note + '\n---\n', 1)
        protos = '\n'.join(f'- [{t}]({PROTO}{fn})' for fn, t in PROTOTYPES)
        txt += f'\n\n## Reference prototypes {{#reference-prototypes}}\n\nClickable design options that were used to choose the current patterns. They use fictional data.\n\n{protos}\n'
        body = txt.split('\n')
        fm = f"---\nlayout: default\ntitle: \"{PARENT}\"\nparent: {SEC}\nhas_children: true\nnav_order: 1\npermalink: {BASE}\n---\n\n"
    else:
        fm = (f"---\nlayout: default\ntitle: \"{title}\"\nparent: \"{PARENT}\"\ngrand_parent: {SEC}\nhas_children: false\n"
              f"nav_order: {idx}\npermalink: {BASE}{slug}/\n---\n\n")
    with open(os.path.join(ROOT, 'docs', 'design-standards', 'admin', f'{slug}.md'), 'w', encoding='utf-8') as f:
        f.write(fm + '{% raw %}\n' + '\n'.join(body) + '\n{% endraw %}\n')

# single file copy: the whole source, visuals added, image paths relative to docs/design-standards/admin/
rel = '../../../assets/images/design-standards/admin/'
single = transform(0, len(lines), 'single', img_prefix=rel)
single_txt = '\n'.join(single)
single_txt = single_txt.replace('\n---\n', ('\n> Illustrated copy of AapliAdmin `docs/DESIGN_SYSTEM.md` (branch `redesign`). The diagrams are drawn from the '
                                            '`--ab-*` tokens; regenerate with `_design-src/admin/`. Edit the AapliAdmin file, not this one.\n\n---\n'), 1)
with open(os.path.join(ROOT, 'docs', 'design-standards', 'admin', 'DESIGN_SYSTEM.md'), 'w', encoding='utf-8') as f:
    f.write(single_txt + '\n')

# report
missing = sorted({a for a in re.findall(r'\]\(#([\w\-]+)\)', src) if a not in anchor_page})
print('pages:', len(PLAN) + 1, '| visuals placed:', sum(len(v) for v in VISUALS.values()), '| unresolved source links:', missing)
