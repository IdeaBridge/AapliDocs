"""Draws the annotated visuals for the Aapli Admin design system (AapliAdmin docs/DESIGN_SYSTEM.md).
Run: python3 gen_ds_svgs.py <out_dir>
Every value comes from src/scss/design-system/_tokens.scss and the specs in DESIGN_SYSTEM.md.
All names and data are fictional."""
import sys, os, html

OUT = sys.argv[1] if len(sys.argv) > 1 else 'svg'
os.makedirs(OUT, exist_ok=True)

# --ab-* tokens (tints pre-blended on white so the SVGs need no alpha)
C = dict(bg='#F4F6F9', surface='#FFFFFF', surface2='#F8F8F8', line='#E2E6EC', strong='#CFD5DD',
         fg='#2B2F36', muted='#5F6670', ph='#8A919B',
         primary='#0062B5', phover='#00539A', tint='#E6EFF8', tint2='#D6E6F4', hov='#F2F7FB', on='#FFFFFF',
         danger='#C62828', dtint='#FBEDED', ok='#2E7D32', oktint='#EAF2EA', warn='#8A5300', wtint='#FDF5E0',
         codebg='#0F1B2A', codefg='#D6E4F5', codekey='#7CC4FF', codestr='#A5D6A7',
         note='#7A3E9D', scrim='#0F1B2A', mark='#FFF3B0')
FONT = "Roboto, system-ui, 'Segoe UI', Arial, sans-serif"
MONO = "'Roboto Mono', Consolas, Menlo, monospace"

def esc(s): return html.escape(str(s), quote=True)
def svg(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" '
            f'aria-label="{esc(title)}" font-family="{FONT}">\n<title>{esc(title)}</title>\n'
            f'<rect width="{w}" height="{h}" fill="{C["bg"]}"/>\n{body}\n</svg>\n')
def R(x, y, w, h, r=0, fill='none', stroke=None, sw=1, dash=None, op=None):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}"'
    if stroke: s += f' stroke="{stroke}" stroke-width="{sw}"'
    if dash: s += f' stroke-dasharray="{dash}"'
    if op is not None: s += f' opacity="{op}"'
    return s + '/>'
def T(x, y, s, size=14, fill=None, weight=400, anchor='start', mono=False, ls=None, upper=False):
    fam = f' font-family="{MONO}"' if mono else ''
    l = f' letter-spacing="{ls}"' if ls else ''
    s = str(s).upper() if upper else s
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill or C["fg"]}" font-weight="{weight}" text-anchor="{anchor}"{fam}{l}>{esc(s)}</text>'
def OV(x, y, s, fill=None, anchor='start'): return T(x, y, s, 11, fill or C['muted'], 500, anchor, ls='0.66', upper=True)
def L(x1, y1, x2, y2, stroke=None, sw=1, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke or C["line"]}" stroke-width="{sw}"{d}/>'
def Cc(cx, cy, r, fill, stroke=None, sw=1):
    s = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"'
    if stroke: s += f' stroke="{stroke}" stroke-width="{sw}"'
    return s + '/>'
def P(d, stroke=None, fill='none', sw=1.7):
    return f'<path d="{d}" fill="{fill}" stroke="{stroke or C["muted"]}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>'

# ---- icons in a 20px box (x,y top-left) ----
def ic(name, x, y, c=None, s=20):
    c = c or C['muted']; k = s/20
    def p(d, sw=1.7): return f'<g transform="translate({x},{y}) scale({k})">' + P(d, c, sw=sw) + '</g>'
    def raw(inner): return f'<g transform="translate({x},{y}) scale({k})">{inner}</g>'
    if name == 'search': return raw(Cc(8.5, 8.5, 5.2, 'none', c, 1.8) + P('M12.5 12.5 L17 17', c, sw=1.8))
    if name == 'close': return p('M5 5 L15 15 M15 5 L5 15', 1.8)
    if name == 'chev': return p('M5 8 L10 13 L15 8')
    if name == 'chevup': return p('M5 12 L10 7 L15 12')
    if name == 'right': return p('M8 5 L13 10 L8 15')
    if name == 'add': return p('M10 4 L10 16 M4 10 L16 10', 2)
    if name == 'save': return raw(R(3.5, 3.5, 13, 13, 1.5, 'none', c, 1.7) + R(6.5, 3.5, 7, 4.5, 0, 'none', c, 1.5) + Cc(10, 12, 2, 'none', c, 1.5))
    if name == 'check': return p('M4 10.5 L8 14.5 L16 6', 2.2)
    if name == 'more': return raw(Cc(10, 4.5, 1.7, c) + Cc(10, 10, 1.7, c) + Cc(10, 15.5, 1.7, c))
    if name == 'menu': return p('M3.5 6 L16.5 6 M3.5 10 L16.5 10 M3.5 14 L16.5 14', 1.8)
    if name == 'menu_open': return p('M3.5 6 L12 6 M3.5 10 L10 10 M3.5 14 L12 14 M16.5 7.5 L14 10 L16.5 12.5', 1.8)
    if name == 'delete': return p('M4.5 6 L15.5 6 M8 6 L8.5 4 L11.5 4 L12 6 M6 6 L6.8 16 L13.2 16 L14 6', 1.6)
    if name == 'edit': return p('M4 16 L4.5 12.5 L13 4 L16 7 L7.5 15.5 Z', 1.6)
    if name == 'lock': return raw(R(5, 9, 10, 8, 1.5, 'none', c, 1.6) + P('M7 9 L7 6.5 Q10 2.5 13 6.5 L13 9', c, sw=1.6))
    if name == 'group': return raw(Cc(7.5, 7, 2.6, 'none', c, 1.6) + Cc(13.5, 7.5, 2.2, 'none', c, 1.5) + P('M2.5 16 Q7.5 9.5 12.5 16 M12 12 Q15.5 10.5 18 15', c, sw=1.5))
    if name == 'apps': return raw(''.join(R(3 + i*5.5, 3 + j*5.5, 3.5, 3.5, .8, c) for i in range(3) for j in range(3)))
    if name == 'domain': return raw(R(3, 7, 7, 10, .5, 'none', c, 1.5) + R(10, 3, 7, 14, .5, 'none', c, 1.5))
    if name == 'web': return raw(R(2.5, 4, 15, 12, 1.5, 'none', c, 1.5) + L(2.5, 8, 17.5, 8, c, 1.5))
    if name == 'shield': return p('M10 3 L16 5.5 L16 10 Q16 15 10 17.5 Q4 15 4 10 L4 5.5 Z', 1.6)
    if name == 'settings': return raw(Cc(10, 10, 2.6, 'none', c, 1.6) + Cc(10, 10, 6.3, 'none', c, 1.6) + ''.join(L(10 + 6.3*a, 10 + 6.3*b, 10 + 8.3*a, 10 + 8.3*b, c, 2) for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1), (.7, .7), (-.7, .7), (.7, -.7), (-.7, -.7)]))
    if name == 'tune': return p('M3.5 6 L16.5 6 M3.5 14 L16.5 14 M7 3.5 L7 8.5 M13 11.5 L13 16.5', 1.7)
    if name == 'info': return raw(Cc(10, 10, 7, 'none', c, 1.6) + L(10, 9, 10, 14, c, 1.8) + Cc(10, 6.3, 1, c))
    if name == 'star': return p('M10 3 L12 8 L17 8.3 L13 11.5 L14.4 16.5 L10 13.6 L5.6 16.5 L7 11.5 L3 8.3 L8 8 Z', 1.4)
    if name == 'robot': return raw(R(4, 6.5, 12, 9, 2, 'none', c, 1.5) + Cc(8, 11, 1.2, c) + Cc(12, 11, 1.2, c) + L(10, 3.5, 10, 6.5, c, 1.5))
    if name == 'data': return p('M7 5 Q4 5 4 8 L4 9 Q4 10 3 10 Q4 10 4 11 L4 12 Q4 15 7 15 M13 5 Q16 5 16 8 L16 9 Q16 10 17 10 Q16 10 16 11 L16 12 Q16 15 13 15', 1.5)
    if name == 'person_add': return raw(Cc(8, 7, 3, 'none', c, 1.6) + P('M2.5 16.5 Q8 9.5 13.5 16.5 M15.5 6 L15.5 11 M13 8.5 L18 8.5', c, sw=1.6))
    if name == 'upload': return p('M10 14 L10 4 M6 8 L10 4 L14 8 M4 16.5 L16 16.5', 1.7)
    if name == 'download': return p('M10 4 L10 14 M6 10 L10 14 L14 10 M4 16.5 L16 16.5', 1.7)
    if name == 'key': return raw(Cc(6.5, 10, 3.2, 'none', c, 1.6) + P('M9.7 10 L17 10 M14 10 L14 13 M16.5 10 L16.5 12.5', c, sw=1.6))
    if name == 'chat': return p('M3.5 4.5 L16.5 4.5 L16.5 13 L8 13 L4.5 16 L4.5 13 L3.5 13 Z', 1.5)
    if name == 'chart': return raw(R(4, 10, 2.8, 6, .5, c) + R(8.6, 6, 2.8, 10, .5, c) + R(13.2, 3.5, 2.8, 12.5, .5, c))
    if name == 'api': return p('M6 6 L2.5 10 L6 14 M14 6 L17.5 10 L14 14 M11.5 4.5 L8.5 15.5', 1.6)
    if name == 'design': return p('M4 16 L4.5 12.5 L13 4 L16 7 L7.5 15.5 Z M11 6 L14 9', 1.5)
    if name == 'tree': return raw(R(3, 3, 5, 4, 1, 'none', c, 1.4) + R(12, 9, 5, 4, 1, 'none', c, 1.4) + R(12, 14.5, 5, 3.5, 1, 'none', c, 1.4) + P('M5.5 7 L5.5 16 L12 16 M5.5 11 L12 11', c, sw=1.4))
    if name == 'assign': return raw(R(4, 3.5, 12, 14, 1.5, 'none', c, 1.5) + P('M7 8 L13 8 M7 11 L13 11 M7 14 L11 14', c, sw=1.4))
    if name == 'dash': return raw(R(3, 3, 6, 8, 1, 'none', c, 1.4) + R(11, 3, 6, 4.5, 1, 'none', c, 1.4) + R(3, 13, 6, 4, 1, 'none', c, 1.4) + R(11, 9.5, 6, 7.5, 1, 'none', c, 1.4))
    if name == 'visibility': return raw(P('M2 10 Q10 2.5 18 10 Q10 17.5 2 10 Z', c, sw=1.5) + Cc(10, 10, 2.5, 'none', c, 1.5))
    if name == 'check_circle': return raw(Cc(10, 10, 8, c) + P('M6 10.3 L8.8 13 L14 7.5', '#ffffff', sw=2))
    if name == 'warning': return raw(P('M10 3 L18 17 L2 17 Z', c, sw=1.6) + L(10, 8, 10, 12.5, c, 1.8) + Cc(10, 14.8, 1, c))
    if name == 'error': return raw(Cc(10, 10, 7.5, 'none', c, 1.6) + L(10, 6, 10, 11, c, 1.8) + Cc(10, 13.8, 1, c))
    if name == 'drag': return raw(''.join(Cc(7.5 + i*5, 5 + j*5, 1.3, c) for i in range(2) for j in range(3)))
    if name == 'reset': return p('M5 6 L5 10 L9 10 M5.5 10 Q6 4.5 11 4.5 Q16 4.5 16 10 Q16 15.5 10.5 15.5', 1.6)
    if name == 'block': return raw(Cc(10, 10, 7, 'none', c, 1.6) + L(5, 15, 15, 5, c, 1.6))
    return ''

def marker(n, x, y): return Cc(x, y, 10, C['note']) + T(x, y+4, n, 11, '#fff', 700, 'middle')
def callout(n, x, y, tx, ty): return L(x, y, tx, ty, C['note'], 1, '3 2') + Cc(x, y, 2.5, C['note']) + marker(n, tx, ty)
def H(x, y, s): return T(x, y, s, 15, C['fg'], 500)
def S(x, y, s): return T(x, y, s, 12, C['fg'], 500)
def hint(x, y, s, anchor='start'): return T(x, y, s, 12, C['muted'], 400, anchor)
def lines(x, y, rows, size=12.5, step=19, fill=None):
    return ''.join(T(x, y + i*step, r, size, fill or C['fg']) for i, r in enumerate(rows) if r)
def legend(items, x, y, step=46):
    o = []
    for n, a, b in items:
        o.append(marker(n, x+10, y) + T(x+28, y+4, a, 12.5, C['fg'], 500))
        for j, seg in enumerate(b): o.append(T(x+28, y+21+j*16, seg, 11.5, C['muted']))
        y += max(step, 30 + 16*len(b))
    return ''.join(o)
def tw(s, size=14, w=500, mono=False):
    return len(str(s)) * size * (0.6 if mono else (0.56 if w >= 500 else 0.53))

# ---- components ----
def btn(x, y, label, kind='primary', state=None, icon=None, small=False):
    h = 28 if small else 34; fs = 12 if small else 14; px = 10 if small else 14
    iw = (16 if small else 20) + 6 if icon else 0
    w = 2*px + iw + (tw(label, fs) if label else 0) + (24 if state == 'loading' else 0)
    if kind == 'icon': w, h = 34, 34
    fill, stroke, fg = C['primary'], None, C['on']
    if kind == 'stroked': fill, stroke, fg = C['surface'], C['line'], C['primary']
    if kind == 'text': fill, stroke, fg = 'none', None, C['muted']
    if kind == 'danger': fill, stroke, fg = 'none', None, C['muted']
    if kind == 'dsolid': fill, stroke, fg = C['danger'], None, C['on']
    if kind == 'icon': fill, stroke, fg = 'none', None, C['muted']
    o = []
    if state == 'hover':
        if kind == 'primary': fill = C['phover']
        if kind == 'stroked': stroke, fill = C['strong'], C['hov']
        if kind in ('text', 'icon'): fill = C['surface2']
        if kind == 'danger': fill, fg = C['dtint'], C['danger']
        if kind == 'dsolid': fill = '#A71F1F'
    if state == 'focus': o.append(R(x-3, y-3, w+6, h+6, 6, 'none', C['primary'], 2))
    op = .45 if state == 'disabled' else None
    g = []
    g.append(R(x, y, w, h, 4, fill, stroke, 1))
    tx = x + px
    if kind == 'icon':
        g.append(ic(icon or 'close', x+7, y+7, fg))
    else:
        if icon:
            g.append(ic(icon, tx, y + h/2 - (8 if small else 10), fg, 16 if small else 20)); tx += iw
        if state == 'loading':
            g.append(f'<circle cx="{x+px+9}" cy="{y+h/2}" r="7" fill="none" stroke="{fg}" stroke-width="2" stroke-dasharray="30 14"/>')
        g.append(T(tx + (24 if state == 'loading' else 0), y + h/2 + fs*0.36, label, fs, fg, 500))
    o.append(f'<g opacity="{op}">' + ''.join(g) + '</g>' if op else ''.join(g))
    return ''.join(o), w

def field(x, y, w, label=None, value='', ph='', state='default', icon=None, req=False, hint_=None, err=None, h=34, mono=False):
    o = []
    if label:
        star = f'<tspan fill="{C["danger"]}"> *</tspan>' if req else ''
        o.append(f'<text x="{x}" y="{y-6}" font-size="12" fill="{C["fg"]}" font-weight="500">{esc(label)}{star}</text>')
    fill, stroke, sw = C['surface'], C['line'], 1
    if state == 'hover': stroke = C['strong']
    if state == 'focus': stroke = C['primary']; o.append(R(x-1, y-1, w+2, h+2, 5, 'none', C['primary'], 1))
    if state == 'invalid': stroke, fill = C['danger'], C['dtint']
    if state == 'disabled': fill = C['surface2']
    o.append(R(x, y, w, h, 4, fill, stroke, sw))
    tx = x + 9 + (26 if icon == 'search' else 0)
    if icon == 'search': o.append(ic('search', x+8, y + h/2 - 10, C['muted']))
    ty = y + h/2 + 5 if h <= 36 else y + 21
    fs = 13 if mono else 14
    if value: o.append(T(tx, ty, value, fs, C['muted'] if state == 'disabled' else C['fg'], mono=mono))
    elif ph: o.append(T(tx, ty, ph, fs, C['ph'], mono=mono))
    if state == 'focus' and value:
        cx = tx + tw(value, fs, 400, mono) + 2; o.append(L(cx, y+9, cx, y+h-9, C['fg'], 1.2))
    if icon == 'chev': o.append(ic('chev', x+w-27, y + h/2 - 10))
    if icon == 'clear': o.append(ic('close', x+w-25, y + h/2 - 8, C['muted'], 16))
    if err: o.append(T(x, y+h+16, err, 12, C['danger']))
    elif hint_: o.append(T(x, y+h+16, hint_, 12, C['muted']))
    return ''.join(o)

def chip(x, y, label, tone='neutral', dot=True):
    fg, bg, br = {'neutral': (C['muted'], C['surface2'], C['line']), 'ok': (C['ok'], C['oktint'], None), 'warn': (C['warn'], C['wtint'], None),
                  'danger': (C['danger'], C['dtint'], None), 'primary': (C['primary'], C['tint'], None)}[tone]
    w = (16 if dot else 0) + 16 + len(label)*6.4
    o = R(x, y, w, 20, 10, bg, br) + (Cc(x+10, y+10, 3, fg) if dot else '') + T(x + (18 if dot else 8), y+14, label, 12, fg)
    return o, w

def avatar(cx, cy, ini, r=15):
    return Cc(cx, cy, r, C['tint']) + T(cx, cy+4, ini, 12, C['primary'], 500, 'middle')

def checkbox(x, y, on=False, state=None, ind=False, label=None):
    o = []
    if state == 'focus': o.append(Cc(x+9, y+9, 16, C['tint2']))
    if state == 'disabled': o.append(R(x, y, 18, 18, 2, C['surface2'], C['strong'], 2))
    else: o.append(R(x, y, 18, 18, 2, C['primary'] if on or ind else C['surface'], C['primary'] if on or ind else C['muted'], 2))
    if on: o.append(ic('check', x+1, y+1, '#fff', 16))
    if ind: o.append(L(x+5, y+9, x+13, y+9, '#fff', 2))
    if label: o.append(T(x+28, y+14, label, 14, C['ph'] if state == 'disabled' else C['fg']))
    return ''.join(o)

def radio(x, y, on=False, label=None, state=None):
    o = [Cc(x+9, y+9, 8.5, C['surface'], C['strong'] if state == 'disabled' else (C['primary'] if on else C['muted']), 2)]
    if on: o.append(Cc(x+9, y+9, 4.5, C['primary']))
    if label: o.append(T(x+28, y+14, label, 14, C['ph'] if state == 'disabled' else C['fg']))
    return ''.join(o)

def toggle(x, y, on, label):
    o = [R(x, y+3, 34, 14, 7, C['tint2'] if on else '#C9CED6')]
    o.append(Cc(x+25 if on else x+9, y+10, 9, C['primary'] if on else C['surface'], None if on else C['strong']))
    o.append(T(x+46, y+15, label, 14))
    return ''.join(o)

def icontile(x, y, name, s=32, danger=False):
    return R(x, y, s, s, 4, C['dtint'] if danger else C['tint']) + ic(name, x + (s-20)/2, y + (s-20)/2, C['danger'] if danger else C['primary'])

FIGS = {}
def fig(name):
    def deco(fn): FIGS[name] = fn; return fn
    return deco

# ===================================================================== foundations
@fig('ds-colour')
def _():
    W, H_ = 1040, 470
    o = [H(16, 30, 'Colour tokens')]
    groups = [
        ('Surfaces and lines', [('--ab-bg', '#F4F6F9', 'Page background'), ('--ab-surface', '#FFFFFF', 'Shell, panes, cards, inputs'), ('--ab-surface-2', '#F8F8F8', 'Nav, rail, table header, notes'),
                                ('--ab-line', '#E2E6EC', 'Every border and divider'), ('--ab-line-strong', '#CFD5DD', 'Hover border')]),
        ('Text', [('--ab-fg', '#2B2F36', 'Body text, headings · 13.4:1'), ('--ab-muted', '#5F6670', 'Secondary, hints · 5.8:1'), ('--ab-placeholder', '#8A919B', 'Placeholders only')]),
        ('Brand', [('--ab-primary', '#0062B5', 'Primary, active, focus · 6.2:1'), ('--ab-primary-hover', '#00539A', 'Primary button hover'), ('--ab-primary-tint', C['tint'], 'rgba(0,98,181,.10) active fill'),
                   ('--ab-primary-tint-strong', C['tint2'], 'rgba(0,98,181,.16) pressed')]),
        ('State', [('--ab-danger', '#C62828', 'Errors, destructive'), ('--ab-ok', '#2E7D32', 'Success, “on”'), ('--ab-warn', '#8A5300', 'Warnings that don’t block')]),
        ('Code', [('--ab-code-bg', '#0F1B2A', 'Code block background'), ('--ab-code-key', '#7CC4FF', 'Keys'), ('--ab-code-str', '#A5D6A7', 'Strings')])]
    cols = [(16, [0, 1]), (360, [2, 3]), (704, [4])]
    for x, gi in cols:
        y = 60
        for g in gi:
            name, sw = groups[g]
            o.append(OV(x, y, name)); y += 12
            for n, col, use in sw:
                o.append(R(x, y, 30, 30, 4, col, C['line']))
                o.append(T(x+40, y+13, n, 12, C['fg'], 500, mono=True)); o.append(T(x+40, y+27, f'{col.upper() if col.startswith("#") else col} · {use}', 11, C['muted']))
                y += 38
            y += 18
    o.append(R(704, 260, 320, 190, 4, C['surface'], C['line']))
    o.append(S(720, 284, 'Rules'))
    o.append(lines(720, 306, ['Admin blue is fixed: it never takes the', 'tenant colour. Inside .ab-theme the legacy', '--primaryColor points at --ab-primary.', '',
                              'Text on surface uses fg or muted only.', 'Status is never colour alone: add text.', 'Tints are backgrounds, never text colours.'], 12, 18))
    return svg(W, H_, ''.join(o), 'Admin colour tokens')

@fig('ds-type')
def _():
    W, H_ = 1040, 330
    o = [H(16, 30, 'Type scale')]
    rows = [('Workspace title', 18, 500, False, '--ab-text-page · 18 / 500 · app bar h1'), ('Admin page title', 17, 500, False, '--ab-text-section · 17 / 500 · h2.ab-title'),
            ('Body and description', 14, 400, False, '--ab-text-body · 14 / 400 · line height 1.5'), ('Sub-heading', 14, 500, False, '.ab-subtitle · 14 / 500'),
            ('ExportToIFTab', 13, 400, True, '--ab-text-mono · 13 · keys, IDs, expressions'), ('Hints, errors, counts, chips', 12, 400, False, '--ab-text-sm · 12 / 400'),
            ('Overline · table headers', 11, 500, 'ov', '--ab-text-overline · 11 / 500 · caps .06em'), ('Badge', 10, 500, 'badge', '10 / 500 · caps · primary fill')]
    y = 66
    for n, s, w, kind, spec in rows:
        if kind == 'ov': o.append(OV(16, y, n, C['muted']))
        elif kind == 'badge': o.append(R(16, y-11, 52, 15, 7.5, C['primary']) + T(42, y-1, 'NEW', 10, '#fff', 500, 'middle', ls='0.6'))
        else: o.append(T(16, y, n, s, C['fg'], w, mono=bool(kind)))
        o.append(T(360, y, spec, 12, C['muted'], mono=True)); y += 32
    o.append(R(760, 50, 264, 250, 4, C['surface'], C['line']))
    o.append(S(776, 74, 'Rules'))
    o.append(lines(776, 96, ['500 is the only emphasis weight.', '700 only inside prose (<b> in notes).', 'Never 300 or 100.', '', 'Sentence case everywhere.', 'Headings: text-wrap: balance.', '',
                             'Mono only for machine values.', '', 'Roboto + Roboto Mono, loaded', 'in src/index.html.'], 12, 18))
    return svg(W, H_, ''.join(o), 'Admin type scale')

@fig('ds-spacing-shape')
def _():
    W, H_ = 1040, 330
    o = [H(16, 30, 'Spacing, shape and icons')]
    sp = [(0, 2, 'nav or rail item gap'), (1, 4, 'label → input'), (2, 8, 'between toolbar buttons'), (3, 12, 'cell padding x, app bar y'), (4, 16, 'page gutter, field → field'),
          (5, 20, 'app bar and action bar x'), (6, 24, 'pane top padding'), (7, 28, 'pane sides, pane → aside'), (8, 32, 'large separations')]
    for i, (k, v, u) in enumerate(sp):
        y = 54 + i*28
        o.append(R(16, y, v*4, 16, 2, C['primary'], op=.8))
        o.append(T(150, y+12, f'--ab-space-{k}', 12, C['fg'], 500, mono=True)); o.append(T(270, y+12, f'{v}px · {u}', 12, C['muted']))
    x = 560
    o.append(OV(x, 60, 'Radius'))
    for i, (r, n, use) in enumerate([(4, '--ab-radius-sm 4px', 'inputs, buttons, tables, cards'), (6, '--ab-radius-md 6px', 'framed shell'), (10, '--ab-radius-pill 10px', 'chips')]):
        y = 74 + i*44
        o.append(R(x, y, 56, 32, r, C['surface'], C['strong'])); o.append(T(x+70, y+14, n, 12, C['fg'], 500, mono=True)); o.append(T(x+70, y+29, use, 11.5, C['muted']))
    o.append(OV(x, 226, 'Icons'))
    o.append(ic('settings', x, 238, C['fg'])); o.append(T(x+28, 253, '--ab-icon 20px (default)', 12)); o.append(ic('settings', x+220, 240, C['fg'], 16)); o.append(T(x+242, 253, '--ab-icon-sm 16px', 12))
    o.append(T(x, 284, 'Material Icons (filled). Icons inherit the text colour.', 12, C['muted']))
    o.append(T(x, 302, 'Borders always 1px --ab-line. No shadows except Material overlays.', 12, C['muted']))
    return svg(W, H_, ''.join(o), 'Admin spacing, shape and icons')

# ===================================================================== layout
def nav_panel(o, x, y, w, h, active='User properties', collapsed=False):
    o.append(R(x, y, w, h, 0, C['surface2'])); o.append(L(x+w, y, x+w, y+h))
    if collapsed:
        o.append(ic('menu', x+22, y+16, C['muted']))
        o.append(ic('search', x+22, y+56, C['muted']))
        for i, n in enumerate(['domain', 'apps', 'group', 'shield', 'web', 'data']):
            yy = y + 100 + i*44
            if n == 'group': o.append(R(x+10, yy-9, w-20, 38, 4, C['tint']))
            o.append(ic(n, x+22, yy, C['primary'] if n == 'group' else C['muted']))
        return
    o.append(T(x+16, y+28, 'Admin settings', 18, C['fg'], 500)); o.append(ic('menu_open', x+w-38, y+12))
    o.append(field(x+12, y+46, w-24, None, '', 'Search settings', icon='search'))
    rows = [('domain', 'Organisation', False, []), ('apps', 'Applications', False, []), ('group', 'People', True, ['Users', 'User properties', 'User import mapping', 'SSO settings']),
            ('shield', 'Roles', False, []), ('web', 'Content', False, [])]
    yy = y + 98
    for icn, lab, open_, kids in rows:
        grp_active = active in kids
        col = C['primary'] if grp_active else C['muted']
        o.append(ic(icn, x+20, yy+9, col)); o.append(T(x+50, yy+24, lab, 14, col, 500 if grp_active else 400))
        o.append(ic('chevup' if open_ else 'chev', x+w-36, yy+9, col))
        yy += 40
        if open_:
            o.append(L(x+29, yy-2, x+29, yy + 36*len(kids) - 4, C['line']))
            for k in kids:
                if k == active: o.append(R(x+8, yy, w-16, 34, 4, C['tint']))
                o.append(T(x+50, yy+22, k, 13.5, C['primary'] if k == active else C['muted'], 500 if k == active else 400))
                yy += 36
    o.append(L(x, y+h-50, x+w, y+h-50)); o.append(ic('settings', x+20, y+h-36)); o.append(T(x+50, y+h-21, 'General', 14, C['muted']))

@fig('ds-layout-shell')
def _():
    W, H_ = 1040, 620
    o = [H(16, 30, 'Workspace layout (form builder)')]
    x0, y0 = 16, 48
    o.append(R(x0, y0, 1008, 556, 6, C['surface'], C['line']))
    # app bar
    o.append(ic('design', x0+20, y0+18, C['primary'])); o.append(T(x0+50, y0+33, 'Innovation challenge', 18, C['fg'], 500))
    c, cw = chip(x0+250, y0+18, 'Content type: Idea', 'neutral', False); o.append(c)
    b, bw = btn(x0+1008-20-34-10-120, y0+11, 'Preview', 'stroked', icon='visibility'); o.append(b)
    o.append(btn(x0+1008-20-34, y0+11, '', 'icon', icon='close')[0])
    o.append(L(x0, y0+56, x0+1008, y0+56))
    # main tabs
    tabs = [('settings', 'Settings'), ('design', 'Form'), ('tree', 'Request workflow'), ('assign', 'Tasks'), ('dash', 'Dashboard')]
    tx = x0+12
    for i, (icn, lab) in enumerate(tabs):
        w = 14 + 20 + 8 + tw(lab, 14, 500) + 14
        col = C['primary'] if i == 0 else C['muted']
        o.append(ic(icn, tx+14, y0+70, col)); o.append(T(tx+42, y0+85, lab, 14, col, 500 if i == 0 else 400))
        if i == 0: o.append(R(tx, y0+102, w, 2, 0, C['primary']))
        tx += w + 4
    o.append(L(x0, y0+104, x0+1008, y0+104))
    # rail
    ry = y0+104
    o.append(R(x0, ry, 260, 392, 0, C['surface2'])); o.append(L(x0+260, ry, x0+260, ry+392))
    for i, (icn, lab) in enumerate([('tune', 'Application settings'), ('info', 'Information'), ('dash', 'Views'), ('shield', 'Roles and permissions'), ('settings', 'Other settings'), ('star', 'Points'), ('robot', 'AI features'), ('data', 'Custom properties')]):
        yy = ry + 16 + i*40
        if i == 7: o.append(R(x0+8, yy, 244, 38, 4, C['tint']))
        col = C['primary'] if i == 7 else C['muted']
        o.append(ic(icn, x0+20, yy+9, col)); o.append(T(x0+50, yy+24, lab, 14, col, 500 if i == 7 else 400))
    # pane
    px = x0+288
    o.append(T(px, ry+44, 'Custom properties', 17, C['fg'], 500))
    o.append(T(px, ry+68, 'Key and value pairs the API returns with this application.', 14, C['muted']))
    o.append(T(px, ry+102, '2 properties', 12, C['muted'])); o.append(btn(px+380-tw('Add property')-48, ry+82, 'Add property', 'stroked', icon='add')[0])
    o.append(R(px, ry+124, 380, 116, 4, C['surface'], C['line'])); o.append(R(px, ry+124, 380, 36, 0, C['surface2'])); o.append(OV(px+12, ry+146, 'Key')); o.append(OV(px+200, ry+146, 'Value'))
    for i, (k, v) in enumerate([('ExportToIFTab', 'true'), ('ReportCode', 'R-114')]):
        yy = ry+160 + i*40
        o.append(L(px, yy, px+380, yy)); o.append(T(px+12, yy+25, k, 13, mono=True)); o.append(T(px+200, yy+25, v, 13, mono=True)); o.append(ic('delete', px+346, yy+10))
    # aside
    ax = x0+1008-28-270
    o.append(ic('api', ax, ry+30, C['muted'], 16)); o.append(OV(ax+22, ry+43, 'Returned by content/get'))
    o.append(R(ax, ry+56, 270, 120, 4, C['codebg']))
    o.append(T(ax+14, ry+80, '"CustomProperties": {', 12, C['codefg'], mono=True)); o.append(T(ax+30, ry+100, '"ExportToIFTab": "true",', 12, C['codekey'], mono=True)); o.append(T(ax+30, ry+120, '"ReportCode": "R-114"', 12, C['codestr'], mono=True)); o.append(T(ax+14, ry+140, '}', 12, C['codefg'], mono=True))
    # action bar
    ay = y0+556-60
    o.append(L(x0, ay, x0+1008, ay))
    o.append(btn(x0+20, ay+13, 'Back', 'text')[0])
    _, wsave = btn(0, 0, 'Save', icon='save'); _, wnext = btn(0, 0, 'Next', 'stroked'); _, wcan = btn(0, 0, 'Cancel', 'stroked')
    xs = x0+1008-20-wsave
    o.append(btn(xs, ay+13, 'Save', icon='save')[0]); o.append(btn(xs-8-wnext, ay+13, 'Next', 'stroked')[0]); o.append(btn(xs-16-wnext-wcan, ay+13, 'Cancel', 'stroked')[0])
    o.append(T(xs-24-wnext-wcan, ay+35, 'Unsaved changes', 12, C['muted'], anchor='end'))
    # callouts
    o.append(callout('1', x0+600, y0+28, x0+640, y0+28)); o.append(callout('2', x0+700, y0+86, x0+740, y0+86))
    o.append(marker('3', x0+236, ry+350)); o.append(callout('4', px+200, ry+246, px+200, ry+272))
    o.append(callout('5', ax+150, ry+180, ax+150, ry+206)); o.append(callout('6', x0+500, ay+30, x0+560, ay+30))
    o.append(lines(px, ry+300, ['1 App bar: icon, title, chips, Preview, close   2 Main tabs: 3–8, icon + label', '3 Section rail 260px   4 Pane, padding 24px 28px   5 Aside 340px', '6 Action bar (sticky): Back · Cancel · Next · Save last'], 12, 18, C['muted']))
    return svg(W, H_, ''.join(o), 'Admin workspace layout')

@fig('ds-page-frame')
def _():
    W, H_ = 1040, 560
    o = [H(16, 30, 'Page frame and title (admin console)')]
    x0, y0 = 16, 48
    o.append(R(x0, y0, 744, 496, 6, C['surface'], C['line']))
    nav_panel(o, x0, y0, 216, 496, 'Users')
    cx, cy = x0+216, y0
    o.append(R(cx+1, cy+1, 28, 494, 0, C['tint'], op=.6)); o.append(R(cx+29, cy+1, 498, 24, 0, C['tint'], op=.6))
    o.append(T(cx+14, cy+260, '28', 10.5, C['primary'], 500, 'middle')); o.append(T(cx+290, cy+16, '24', 10.5, C['primary'], 500, 'middle'))
    tx, ty = cx+28, cy+24
    o.append(R(tx, ty, 400, 21, 0, 'none', C['note'], 1, '3 2'))
    o.append(T(tx, ty+17, 'Users', 17, C['fg'], 500))
    o.append(T(tx, ty+42, 'Add users and manage their roles and privileges.', 14, C['muted']))
    o.append(field(tx, ty+64, 230, None, '', 'Search users', icon='search')); o.append(T(tx+240, ty+86, '1,248 users', 12, C['muted']))
    _, wa = btn(0, 0, 'Add user', icon='person_add'); o.append(btn(cx+528-28-wa, ty+64, 'Add user', icon='person_add')[0])
    o.append(R(tx, ty+112, 472, 330, 4, C['surface'], C['line'])); o.append(R(tx, ty+112, 472, 36, 0, C['surface2']))
    for i in range(7): o.append(L(tx, ty+148+i*40, tx+472, ty+148+i*40)); o.append(R(tx+12, ty+162+i*40, 140, 10, 2, C['surface2']))
    o.append(callout('1', tx+60, ty+10, tx+130, cy+10)); o.append(callout('2', tx+330, ty+37, tx+440, ty+37)); o.append(callout('3', tx+100, ty+80, tx+100, ty+102))
    o.append(legend([('1', 'h2.ab-title', ['17px / 500, line height 1.25', 'top 24px, left 28px from the nav', 'no top margin, 4px below']),
                     ('2', 'p.ab-sub', ['14px / 400 muted, full width', '18px below']),
                     ('3', 'Then toolbar → content', ['the screen adds no outer padding', 'one h2 per screen; h3 for sections'])], 760, 70, 76))
    return svg(W, H_, ''.join(o), 'Admin page frame and title')

# ===================================================================== left nav & rail
@fig('ds-left-nav')
def _():
    W, H_ = 1040, 560
    o = [H(16, 30, 'Left navigation')]
    nav_panel(o, 16, 48, 264, 496, 'User properties')
    o.append(callout('1', 140, 76, 320, 66)); o.append(callout('2', 250, 70, 320, 100)); o.append(callout('3', 200, 112, 320, 134))
    o.append(callout('4', 220, 228, 320, 228)); o.append(callout('5', 200, 296, 320, 296)); o.append(callout('6', 46, 330, 320, 360))
    o.append(callout('7', 200, 520, 320, 520))
    o.append(legend([('1', 'Heading', ['18 / 500 · hidden when collapsed']), ('2', 'Collapse toggle', ['32×32 · menu_open / menu · aria-expanded']),
                     ('3', 'Search', ['.ab-input, search icon, clear (×)', 'filters label, description, keywords']),
                     ('4', 'Group header', ['<button> · icon + label + chevron', 'primary text when it holds the page']),
                     ('5', 'Active page', ['primary tint, primary text, 500', 'aria-current="page"']),
                     ('6', 'Second level', ['13.5px, indented 42px, no icon', '1px guide line at 21px']),
                     ('7', 'Pinned footer', ['General · outside the scroll'])], 350, 66, 52))
    # collapsed
    o.append(S(780, 66, 'Collapsed (64px)'))
    nav_panel(o, 780, 80, 64, 360, collapsed=True)
    o.append(R(856, 186, 132, 30, 4, C['fg'])); o.append(T(866, 206, 'People', 12.5, '#fff'))
    o.append(lines(780, 466, ['Top-level icons with tooltips.', 'Choosing a group expands the', 'nav first, then opens it.'], 12, 18, C['muted']))
    return svg(W, H_, ''.join(o), 'Admin left navigation anatomy')

@fig('ds-left-nav-states')
def _():
    W, H_ = 1040, 330
    o = [H(16, 30, 'Navigation item states')]
    states = [('Rest', None, C['muted'], 400, None), ('Hover', C['hov'], C['fg'], 400, None), ('Focus (keyboard)', None, C['muted'], 400, 'focus'),
              ('Active page', C['tint'], C['primary'], 500, None), ('Group holding the page', None, C['primary'], 500, 'group'), ('Disabled', None, C['muted'], 400, 'disabled')]
    for i, (n, bgc, fg, w, k) in enumerate(states):
        col, row = i % 3, i // 3
        x, y = 16 + col*340, 62 + row*120
        o.append(S(x, y, n))
        bx, by = x, y+14
        o.append(R(bx, by, 300, 60, 4, C['surface2']))
        g = []
        if bgc: g.append(R(bx+8, by+11, 284, 38, 4, bgc))
        if k == 'focus': g.append(R(bx+9, by+12, 282, 36, 4, 'none', C['primary'], 2))
        g.append(ic('group' if k == 'group' else 'apps', bx+20, by+20, fg))
        g.append(T(bx+50, by+35, 'People' if k == 'group' else ('Billing' if k == 'disabled' else 'Applications'), 14, fg, w))
        if k == 'group': g.append(ic('chevup', bx+262, by+20, fg))
        if k == 'disabled': g.append(ic('lock', bx+262, by+20, fg))
        o.append(f'<g opacity=".5">' + ''.join(g) + '</g>' if k == 'disabled' else ''.join(g))
        notes = {'Rest': 'muted text, no fill', 'Hover': 'rgba(primary,.05) fill, fg text', 'Focus (keyboard)': '2px primary outline, inset (offset -2px)',
                 'Active page': 'tint fill · primary · 500', 'Group holding the page': 'primary text, no fill (fill belongs to the page)', 'Disabled': '50% · lock · tooltip gives the reason'}
        o.append(hint(x, y+94, notes[n]))
    o.append(S(16, 316, 'Search match:'))
    o.append(R(111, 302, 33, 20, 2, C['mark'])); o.append(f'<text x="112" y="317" font-size="14" fill="{C["muted"]}"><tspan fill="{C["fg"]}" font-weight="500">User</tspan> import mapping</text>')
    o.append(T(300, 317, 'Third-level results read “Settings › Currencies”. No results: “No settings match “sso”.” + Clear search.', 12, C['muted']))
    return svg(W, H_, ''.join(o), 'Admin navigation item states')

@fig('ds-section-rail')
def _():
    W, H_ = 1040, 380
    o = [H(16, 30, 'Section rail')]
    x0, y0 = 16, 48
    o.append(R(x0, y0, 620, 316, 6, C['surface'], C['line']))
    o.append(R(x0, y0, 260, 316, 0, C['surface2'])); o.append(L(x0+260, y0, x0+260, y0+316))
    items = [('tune', 'Application settings'), ('info', 'Information'), ('dash', 'Views'), ('shield', 'Roles and permissions'), ('settings', 'Other settings'), ('star', 'Points'), ('robot', 'AI features')]
    for i, (icn, lab) in enumerate(items):
        yy = y0+16 + i*40
        if i == 3: o.append(R(x0+8, yy, 244, 38, 4, C['tint']))
        if i == 1: o.append(R(x0+8, yy, 244, 38, 4, C['hov']))
        col = C['primary'] if i == 3 else (C['fg'] if i == 1 else C['muted'])
        o.append(ic(icn, x0+20, yy+9, col)); o.append(T(x0+50, yy+24, lab, 14, col, 500 if i == 3 else 400))
        if i == 6: o.append(R(x0+200, yy+11, 40, 15, 7.5, C['primary']) + T(x0+220, yy+22, 'NEW', 10, '#fff', 500, 'middle', ls='0.6'))
    o.append(T(x0+288, y0+48, 'Roles and permissions', 17, C['fg'], 500)); o.append(T(x0+288, y0+72, 'Choose who can see and change records.', 14, C['muted']))
    for i in range(4): o.append(R(x0+288, y0+100+i*40, 300, 28, 4, C['surface2']))
    o.append(marker('1', x0+236, y0+16+3*40+19)); o.append(marker('2', x0+236, y0+16+40+19))
    o.append(marker('3', x0+186, y0+16+6*40+19)); o.append(marker('4', x0+590, y0+44))
    o.append(legend([('1', 'Active item', ['tint fill · primary · 500 · aria-selected="true"']), ('2', 'Hover', ['rgba(primary,.05) · fg text']),
                     ('3', 'Badge', ['“New” for one release, then remove']), ('4', 'Pane', ['role="tabpanel", labelled by the active item'])], 670, 66, 50))
    o.append(lines(670, 300, ['260px · surface-2 · sticky · 3–10 sections', 'ul[role=tablist][aria-orientation=vertical]', '↑ ↓ Home End move between sections', '≤ 760px: horizontal scrolling row'], 12, 17, C['muted']))
    return svg(W, H_, ''.join(o), 'Admin section rail')

@fig('ds-tabs')
def _():
    W, H_ = 1040, 270
    o = [H(16, 30, 'Main tabs and in-page tabs')]
    x0, y0 = 16, 56
    o.append(R(x0, y0, 640, 60, 4, C['surface'], C['line']))
    tabs = [('settings', 'Settings', 'active'), ('design', 'Form', 'error'), ('tree', 'Request workflow', 'hover'), ('assign', 'Tasks', None)]
    tx = x0+12
    for icn, lab, st in tabs:
        w = 14 + 20 + 8 + tw(lab, 14, 500) + 14 + (14 if st == 'error' else 0)
        col = C['primary'] if st == 'active' else (C['fg'] if st == 'hover' else C['muted'])
        o.append(ic(icn, tx+14, y0+20, col)); o.append(T(tx+42, y0+35, lab, 14, col, 500 if st == 'active' else 400))
        if st == 'error': o.append(Cc(tx+42+tw(lab, 14, 400)+10, y0+30, 3, C['danger']))
        if st == 'active': o.append(R(tx, y0+56, w, 2, 0, C['primary']))
        tx += w + 4
    o.append(L(x0, y0+58, x0+640, y0+58))
    o.append(callout('1', x0+60, y0+57, x0+60, y0+92)); o.append(callout('2', x0+210, y0+30, x0+210, y0+92)); o.append(callout('3', x0+320, y0+36, x0+330, y0+92))
    o.append(legend([('1', 'Active', ['primary text + 2px underline, 500']), ('2', 'Has an error', ['6px danger dot; reason inside the tab']), ('3', 'Hover', ['fg text'])], 680, 66, 48))
    o.append(lines(16, 190, ['Padding 12px 14px · icon 20px + label · bottom border · scrolls, never wraps · 3–8 tabs.', 'Material: <mat-tab-group class="ab-mat-tabs" animationDuration="0ms" [stretchTabs]="false" disableRipple>.',
                             'In-page tabs (third level) use the same look but are links: <a class="ab-tab" routerLink routerLinkActive="is-active">.'], 12.5, 20))
    return svg(W, H_, ''.join(o), 'Admin tabs')

# ===================================================================== buttons
@fig('ds-buttons')
def _():
    W, H_ = 1040, 430
    o = [H(16, 30, 'Buttons (.ab-btn)')]
    kinds = [('Primary', 'primary', 'Save', 'save'), ('Stroked', 'stroked', 'Add property', 'add'), ('Text', 'text', 'Clear search', None),
             ('Danger', 'danger', 'Remove', 'delete'), ('Danger solid', 'dsolid', 'Delete property', None)]
    cols = [('Rest', None), ('Hover', 'hover'), ('Focus (keyboard)', 'focus'), ('Disabled', 'disabled')]
    for j, (c, _) in enumerate(cols): o.append(T(170 + j*210, 64, c, 12, C['muted'], 500))
    for i, (n, k, lab, icn) in enumerate(kinds):
        y = 78 + i*52
        o.append(T(16, y+22, n, 13, C['fg'], 500))
        for j, (_, s) in enumerate(cols): o.append(btn(170 + j*210, y, lab, k, s, icn)[0])
    y = 352
    o.append(T(16, y+22, 'Icon · Small · Loading', 13, C['fg'], 500))
    o.append(btn(170, y, '', 'icon', icon='close')[0]); o.append(btn(214, y, '', 'icon', 'hover', icon='more')[0])
    o.append(btn(380, y+3, 'Add', 'stroked', icon='add', small=True)[0])
    b_, _w = btn(590, y, 'Saving…', 'primary', 'loading'); o.append(b_.replace('rx="4" fill="#0062B5"', 'rx="4" fill="#0062B5"', 1))
    o.append(lines(16, 412, ['34px · padding 7px 14px · radius 4px · 14 / 500 · icon 20px, 6px gap. Small 28px, 12px. Icon 34×34 with aria-label + tooltip. One primary per view; labels are verbs.'], 12, 18, C['muted']))
    return svg(W, H_, ''.join(o), 'Admin buttons')

# ===================================================================== form fields
@fig('ds-text-box-anatomy')
def _():
    W, H_ = 1040, 200
    o = [H(16, 30, 'Text box anatomy (.ab-field)')]
    x, y, w = 80, 86, 400
    o.append(field(x, y, w, 'Key', 'ExportTo', state='focus', req=True, hint_='Letters, numbers, _ - or . Up to 100 characters.', mono=True))
    o.append(callout('1', x+2, y-12, x-40, y-24)); o.append(callout('2', x+30, y-12, x+80, y-40)); o.append(callout('3', x+40, y+17, x+230, y-30))
    o.append(callout('4', x+w, y+17, x+w+30, y-6)); o.append(callout('5', x+60, y+46, x-20, y+80))
    o.append(legend([('1', 'Label · .ab-label 12 / 500, visible <label for>', []), ('2', 'Required · <span class="ab-required">*</span> in danger', []),
                     ('3', 'Input · .ab-input 34px, padding 7px 9px, 14px (mono 13px)', []), ('4', 'Border 1px line, radius 4px · focus = primary + 1px ring', []),
                     ('5', 'Hint .ab-hint 12px muted · error .ab-error replaces it', [])], 560, 66, 24))
    return svg(W, H_, ''.join(o), 'Admin text box anatomy')

@fig('ds-text-box-states')
def _():
    W, H_ = 1040, 390
    o = [H(16, 26, 'Text box states')]
    st = [('Placeholder', 'default', '', 'e.g. ExportToIFTab', None, None, True), ('Hover', 'hover', '', 'e.g. ExportToIFTab', None, None, True), ('Focus', 'focus', 'Export', '', None, None, True),
          ('Filled', 'default', 'ExportToIFTab', '', None, None, True), ('Invalid', 'invalid', 'Export To', '', None, 'Use letters, numbers, _ - or . only.', True),
          ('Disabled', 'disabled', 'R-114', '', 'Set by the template.', None, True), ('Plain text', 'default', 'Innovation challenge', '', None, None, False), ('Textarea', None, '', '', None, None, False)]
    for i, (n, s, v, ph, hp, er, mono) in enumerate(st):
        col, row = i % 4, i // 4
        x, y = 16 + col*256, 90 + row*150
        o.append(S(x, y-36, n))
        if s is None:
            o.append(T(x, y-6, 'Description', 12, C['fg'], 500)); o.append(R(x, y, 230, 80, 4, C['surface'], C['line']))
            o.append(T(x+9, y+21, 'Shown to people who', 14)); o.append(T(x+9, y+39, 'submit an idea.', 14)); o.append(hint(x+230, y+96, '38 / 500', 'end'))
            o.append(P(f'M{x+222} {y+74} L{x+226} {y+70} M{x+218} {y+74} L{x+226} {y+66}', C['ph'], sw=1.2))
        else:
            o.append(field(x, y, 230, 'Key' if mono else 'Application name', v, ph, s, req=(i < 6), hint_=hp, err=er, mono=mono))
    o.append(lines(16, 368, ['Placeholder is an example, never the label. Invalid: red border + danger tint + aria-invalid; show it after touch or Save. Disabled: surface-2, muted text.'], 12, 18, C['muted']))
    return svg(W, H_, ''.join(o), 'Admin text box states')

@fig('ds-dropdown')
def _():
    W, H_ = 1040, 410
    o = [H(16, 30, 'Dropdown (select.ab-input and mat-select)')]
    x, y = 16, 92
    o.append(S(x, y-34, 'Closed')); o.append(field(x, y, 230, 'Category', '', 'Select a category', icon='chev', req=True))
    o.append(S(x, y+56, 'Selected')); o.append(field(x, y+90, 230, 'Category', 'Sustainability', icon='chev', req=True))
    o.append(S(x, y+146, 'Invalid')); o.append(field(x, y+180, 230, 'Category', '', 'Select a category', 'invalid', icon='chev', req=True, err='Choose a category.'))
    x2 = 290
    o.append(S(x2, y-34, 'Open list (mat-select)')); o.append(field(x2, y, 230, 'Date format', 'DD/MM/YYYY', 'focus', icon='chev'))
    o.append(f'<rect x="{x2}" y="{y+40}" width="230" height="{4*36+12}" rx="4" fill="#000" opacity=".06" transform="translate(0,3)"/>')
    o.append(R(x2, y+40, 230, 4*36+12, 4, C['surface'], C['line']))
    for i, lab in enumerate(['DD/MM/YYYY', 'MM/DD/YYYY', 'YYYY-MM-DD', 'D MMM YYYY']):
        yy = y+46 + i*36
        if i == 0: o.append(R(x2+1, yy, 228, 36, 0, C['tint']))
        if i == 2: o.append(R(x2+1, yy, 228, 36, 0, C['surface2']))
        o.append(T(x2+14, yy+23, lab, 13, C['primary'] if i == 0 else C['fg'], 500 if i == 0 else 400, mono=True))
    o.append(T(x2+238, y+46+23, '← selected', 11.5, C['muted'])); o.append(T(x2+238, y+46+2*36+23, '← hover', 11.5, C['muted']))
    x3 = 600
    o.append(S(x3, y-34, 'Radio instead (2–5 visible options)'))
    o.append(T(x3, y+4, 'Who can use AI chat', 12, C['fg'], 500))
    o.append(radio(x3, y+16, True, 'Everyone')); o.append(radio(x3, y+46, False, 'People with the AI Assistant role'))
    o.append(R(x3, y+96, 424, 204, 4, C['surface'], C['line']))
    o.append(S(x3+16, y+120, 'Rules'))
    o.append(lines(x3+16, y+142, ['select.ab-input draws its own chevron. mat-select is fine where it', 'exists: 36px, white, 1px line-strong border, no fill, no underline.', 'Put the label above (.ab-label); a floating label overlaps at 36px.',
                                  'Open lists: white, 1px border, soft shadow, panelClass="ab-theme".', 'More than 5 options → select. 2–5 that should all be seen → radio.', 'Placeholder “Select a category”, never a default that looks chosen.',
                                  'Options sort A→Z unless the order means something (keepOrder).'], 12, 19))
    return svg(W, H_, ''.join(o), 'Admin dropdown')

@fig('ds-selection')
def _():
    W, H_ = 1040, 270
    o = [H(16, 30, 'Selection controls')]
    o.append(S(16, 64, 'Checkbox'))
    o.append(checkbox(16, 78, False, label='Off')); o.append(checkbox(16, 110, True, label='On')); o.append(checkbox(16, 142, ind=True, label='Some (select all)'))
    o.append(checkbox(190, 78, True, 'focus', label='Focus')); o.append(checkbox(190, 110, False, 'disabled', label='Disabled'))
    o.append(hint(16, 196, 'Independent options; opting a card in or out.'))
    o.append(S(380, 64, 'Radio'))
    o.append(radio(380, 78, True, 'Everyone')); o.append(radio(380, 110, False, 'Selected roles')); o.append(radio(380, 142, False, 'Nobody', 'disabled'))
    o.append(hint(380, 196, '2–5 mutually exclusive options, all visible.'))
    o.append(S(700, 64, 'Slide toggle'))
    o.append(toggle(700, 78, True, 'Show judging summary')); o.append(toggle(700, 114, False, 'Allow comments'))
    o.append(hint(700, 166, 'Only for a setting that takes effect at once.')); o.append(hint(700, 184, 'If the page has Save, use a checkbox.'))
    o.append(lines(16, 228, ['Angular Material mat-checkbox, mat-radio-button, mat-slide-toggle. Label on the right, sentence case, says what “on” means.', 'Checked = --ab-primary, unchecked outline = --ab-muted.'], 12, 18, C['muted']))
    return svg(W, H_, ''.join(o), 'Admin selection controls')

# ===================================================================== search
@fig('ds-search')
def _():
    W, H_ = 1040, 380
    o = [H(16, 30, 'Search and filter')]
    o.append(S(16, 62, 'Empty')); o.append(field(16, 72, 320, None, '', 'Search by name, email, role or status', icon='search'))
    o.append(S(16, 132, 'With a query')); o.append(field(16, 142, 320, None, 'alex admin', '', 'focus', icon='search')); o.append(ic('close', 312, 151, C['muted'], 16))
    o.append(hint(16, 200, '320px in a toolbar · leading search icon · clear (×)')); o.append(hint(16, 218, 'once there is text · Esc clears · no search button'))
    x = 380
    o.append(S(x, 62, 'Matches highlighted, count announced'))
    o.append(R(x, 72, 300, 128, 4, C['surface'], C['line']))
    rows = [('Alex', ' Morgan', 'Administrator'), ('Alexis', ' Rowe', 'Contributor')]
    o.append(R(x, 72, 300, 36, 0, C['surface2'])); o.append(OV(x+12, 94, 'Name')); o.append(OV(x+180, 94, 'Role'))
    for i, (a, b, r) in enumerate(rows):
        yy = 108 + i*40
        o.append(L(x, yy, x+300, yy)); o.append(R(x+11, yy+11, tw('Alex', 14, 500)+2, 19, 2, C['mark']))
        o.append(f'<text x="{x+12}" y="{yy+25}" font-size="14" fill="{C["fg"]}" font-weight="500">{esc(a)}<tspan font-weight="400">{esc(b)}</tspan></text>')
        o.append(T(x+180, yy+25, r, 14))
    o.append(hint(x, 222, '“alex admin”: each word must match a field')); o.append(hint(x, 240, 'aria-live: “2 users match”'))
    x = 720
    o.append(S(x, 62, 'No results'))
    o.append(R(x, 72, 304, 128, 4, C['surface'], C['line']))
    o.append(T(x+152, 126, 'No users match “alxe”.', 14, C['muted'], anchor='middle')); o.append(btn(x+100, 144, 'Clear search', 'text')[0])
    o.append(hint(x, 222, 'Query in quotes, plus a way to clear it.'))
    o.append(R(16, 270, 1008, 92, 4, C['surface'], C['line']))
    o.append(S(32, 294, 'Rules'))
    o.append(lines(32, 316, ['Filter as you type. Placeholder names what is searched (“Search users”, “Search by name, email, role or status”), never just “Search”.',
                             'Highlight matches with .ab-mark (soft yellow). Lists whose rows are data have their own search box; the nav search finds screens and third-level pages.'], 12, 20))
    return svg(W, H_, ''.join(o), 'Admin search and filter')

# ===================================================================== tables
@fig('ds-table')
def _():
    W, H_ = 1040, 400
    o = [H(16, 30, 'Table (.ab-table) and row height')]
    x, y, w = 56, 50, 620
    o.append(R(x, y, w, 36+40*3+40, 4, C['surface'], C['line']))
    o.append(R(x, y, w, 36, 0, C['surface2'])); o.append(L(x, y+36, x+w, y+36))
    o.append(OV(x+12, y+23, 'Key')); o.append(OV(x+260, y+23, 'Value'))
    rows = [('ExportToIFTab', 'true', None), ('ReportCode', 'R-114', None), ('Export To', 'x', 'This key is already used above.')]
    for i, (k, v, err) in enumerate(rows):
        ry = y+36 + i*40
        if i == 1: o.append(R(x+1, ry, w-2, 40, 0, '#FAFCFE'))
        if i: o.append(L(x, ry, x+w, ry))
        o.append(R(x+12, ry+6, 230, 28, 4, C['dtint'] if err else C['surface'], C['danger'] if err else C['line']))
        o.append(T(x+20, ry+25, k, 13, mono=True))
        o.append(R(x+260, ry+6, 300, 28, 4, C['surface'], C['line'])); o.append(T(x+268, ry+25, v, 13, mono=True))
        o.append(ic('delete', x+w-36, ry+10))
    ey = y+36+120
    o.append(L(x, ey, x+w, ey)); o.append(T(x+w/2, ey+25, 'No custom properties yet. Select Add property to create one.', 13, C['muted'], anchor='middle'))
    # dimension annotations
    o.append(L(x-14, y, x-14, y+36, C['note'])); o.append(T(x-20, y+22, '36', 10.5, C['note'], 500, 'end'))
    o.append(L(x-14, y+36, x-14, y+76, C['note'])); o.append(T(x-20, y+60, '40', 10.5, C['note'], 500, 'end'))
    o.append(T(x+w/2, ey+50, 'Empty state: one row, colspan, .ab-empty, says how to add the first item', 11.5, C['muted'], anchor='middle'))
    o.append(callout('1', x+w-2, y+18, x+w+24, y+18)); o.append(callout('4', x+w-2, y+56, x+w+24, y+56)); o.append(callout('2', x+w-26, y+96, x+w+24, y+96)); o.append(callout('3', x+w-2, y+136, x+w+24, y+136))
    o.append(legend([('1', 'Header 36px', ['11 / 500 caps · surface-2 · 8px 12px']), ('2', 'Actions column 48px', ['remove: .ab-btn--danger', 'aria-label="Remove ReportCode"']),
                     ('3', 'Row with an error', ['the cell grows; the row stays centred']), ('4', 'Body row 40px', ['6px 12px cells · content fits 28px', 'hover rgba(primary,.02)'])], 720, 60, 58))
    o.append(lines(16, 384, ['One row height everywhere: --ab-row-h 40px, --ab-row-h-head 36px, --ab-cell-py 6px, --ab-cell-px 12px. Wrap in .ab-table-wrap (border, radius, overflow-x: auto).'], 12, 18, C['muted']))
    return svg(W, H_, ''.join(o), 'Admin table and row height')

@fig('ds-row-menu')
def _():
    W, H_ = 1040, 340
    o = [H(16, 30, 'Row actions (one ⋮ menu)')]
    x, y = 16, 50
    o.append(R(x, y, 600, 36+40*3, 4, C['surface'], C['line'])); o.append(R(x, y, 600, 36, 0, C['surface2'])); o.append(OV(x+12, y+23, 'Name')); o.append(OV(x+300, y+23, 'Status'))
    for i, (n, st, tone) in enumerate([('Sam Okafor', 'Active', 'ok'), ('Priya Shah', 'Active', 'ok'), ('Jordan Blake', 'Awaiting approval', 'warn')]):
        ry = y+36 + i*40
        if i == 0: o.append(R(x+1, ry, 598, 40, 0, C['tint']))
        o.append(L(x, ry, x+600, ry)); o.append(T(x+12, ry+25, n, 14, C['fg'], 500)); o.append(chip(x+300, ry+10, st, tone)[0])
        if i == 0: o.append(R(x+556, ry+4, 32, 32, 4, C['surface2']))
        o.append(ic('more', x+562, ry+10))
    mx, my = x+600-260, y+36+40
    o.append(f'<rect x="{mx}" y="{my+3}" width="260" height="168" rx="6" fill="#000" opacity=".07"/>')
    o.append(R(mx, my, 260, 168, 6, C['surface'], C['line']))
    items = [('edit', 'Edit details', None), ('reset', 'Reset password', None), (None, None, 'div'), ('block', 'Suspend', 'd'), ('delete', 'Delete user', 'd')]
    yy = my+6
    for icn, lab, k in items:
        if k == 'div': o.append(L(mx, yy+4, mx+260, yy+4)); yy += 9; continue
        if lab == 'Edit details': o.append(R(mx+1, yy, 258, 38, 0, C['surface2']))
        col = C['danger'] if k == 'd' else C['muted']
        o.append(ic(icn, mx+14, yy+9, col)); o.append(T(mx+46, yy+24, lab, 14, C['danger'] if k == 'd' else C['fg'])); yy += 38
    o.append(callout('1', x+572, y+56, x+640, y+40)); o.append(callout('2', mx+130, my+25, x+640, my+20)); o.append(callout('3', mx+20, my+92, x+640, my+100))
    o.append(callout('4', x+200, y+56, x+200, y+250))
    o.append(legend([('1', '⋮ always visible', ['32×32 · aria-label “Actions for Sam Okafor”', 'last column 56px, right aligned']),
                     ('2', 'Menu .ab-menu', ['200–280px · items 38px · icon + label', 'focus first item; ↑ ↓ Home End; Esc returns']),
                     ('3', 'Destructive last', ['after a divider, in danger red']),
                     ('4', 'Row click', ['opens details only (no actions in the panel)', 'nothing appears on hover'])], 670, 64, 62))
    return svg(W, H_, ''.join(o), 'Admin row actions menu')

@fig('ds-data-table')
def _():
    W, H_ = 1040, 450
    o = [H(16, 30, 'Data table (app-ab-data-table)')]
    x, y, w = 44, 50, 732
    o.append(field(x, y, 300, None, '', 'Search users', icon='search')); o.append(T(x+312, y+22, '1,248 users', 12, C['muted']))
    _, wa = btn(0, 0, 'Add user', icon='person_add'); _, wb = btn(0, 0, 'Bulk add', 'stroked', icon='upload')
    o.append(btn(x+w-wa, y, 'Add user', icon='person_add')[0]); o.append(btn(x+w-wa-42, y, '', 'icon', icon='more')[0]); o.append(btn(x+w-wa-50-wb, y, 'Bulk add', 'stroked', icon='upload')[0])
    ty = y+46
    o.append(R(x, ty, w, 36+4*48, 4, C['surface'], C['line'])); o.append(R(x, ty, w, 36, 0, C['surface2']))
    o.append(checkbox(x+12, ty+9, ind=True))
    o.append(OV(x+56, ty+23, 'Name')); o.append(ic('chevup', x+100, ty+9, C['fg'], 16)); o.append(OV(x+330, ty+23, 'Role')); o.append(OV(x+450, ty+23, 'Status')); o.append(OV(x+600, ty+23, 'Last sign-in'))
    rows = [('AM', 'Alex Morgan', 'alex.morgan@example.com', 'Administrator', 'Active', 'ok', 'Today, 09:12', True),
            ('PN', 'Priya Natarajan', 'priya.n@example.com', 'Contributor', 'Active', 'ok', 'Yesterday', True),
            ('JB', 'Jordan Blake', 'jordan.blake@example.com', 'Reviewer', 'Awaiting approval', 'warn', '02/10/2026', False),
            ('SO', 'Sam Okafor', 'sam.okafor@example.com', 'Contributor', 'Suspended', 'danger', '13/09/2026', False)]
    for i, (ini, n, e, r, st, tone, last, sel) in enumerate(rows):
        ry = ty+36 + i*48
        if sel: o.append(R(x+1, ry, w-2, 48, 0, C['tint']))
        o.append(L(x, ry, x+w, ry))
        o.append(checkbox(x+12, ry+15, sel))
        o.append(avatar(x+71, ry+24, ini)); o.append(T(x+94, ry+21, n, 14, C['fg'], 500)); o.append(T(x+94, ry+37, e, 12, C['muted']))
        o.append(T(x+330, ry+29, r, 14)); o.append(chip(x+450, ry+14, st, tone)[0]); o.append(T(x+600, ry+29, last, 12.5, mono=True)); o.append(ic('more', x+w-30, ry+14))
    fy = ty+36+4*48
    o.append(T(x, fy+28, '1–20 of 1,248 users', 12, C['muted'])); o.append(T(x+w, fy+28, 'Rows per page 20 ▾     ‹  Page 1 of 63  ›', 12, C['muted'], anchor='end'))
    # bulk bar
    by = fy+56
    o.append(S(x, by, 'While rows are ticked, the bulk bar replaces the toolbar:'))
    o.append(R(x, by+12, w, 44, 4, C['tint']))
    o.append(T(x+16, by+39, '2 selected', 14, C['primary'], 500)); o.append(btn(x+110, by+17, 'Export', 'text', icon='download')[0].replace(C['muted'], C['primary']))
    o.append(btn(x+220, by+17, 'Suspend', 'text', icon='block')[0].replace(C['muted'], C['danger'])); o.append(ic('close', x+w-34, by+24, C['primary']))
    o.append(legend([('1', 'Toolbar', ['search 320px · count · actions right', 'main action last, primary + icon', 'rare actions in a ⋮ “More” menu']),
                     ('2', 'Person cell', ['30px avatar (initials on tint)', 'name 500 · email 12px muted']),
                     ('3', 'Status cell', ['chip with dot: Active ok,', 'pending warn, Suspended danger']),
                     ('4', 'Mono cell', ['DD/MM/YYYY, “Today, 09:12”']),
                     ('5', 'Footer', ['range · rows per page', '10/20/50/100 · Page 1 of 63']),
                     ('6', 'Bulk bar', ['“N selected” · text actions', 'clear (×)'])], 800, 64, 54))
    for n, py_ in zip('123456', [y+17, ty+60, ty+108, ty+156, fy+24, by+34]):
        o.append(marker(n, 22, py_))
    return svg(W, H_, ''.join(o), 'Admin data table')

# ===================================================================== chips, cards, sections
@fig('ds-chips-cards')
def _():
    W, H_ = 1040, 330
    o = [H(16, 30, 'Chips, badges and cards')]
    o.append(S(16, 64, 'Chips (.ab-chip) — read only, not buttons'))
    xx = 16
    for lab, tone, dot in [('Content type: Idea', 'neutral', False), ('Published', 'primary', False), ('Active', 'ok', True), ('Draft', 'warn', True), ('Failed', 'danger', True)]:
        c, w = chip(xx, 76, lab, tone, dot); o.append(c); xx += w + 10
    o.append(S(600, 64, 'Badge (.ab-badge)'))
    o.append(R(600, 78, 40, 15, 7.5, C['primary']) + T(620, 89, 'NEW', 10, '#fff', 500, 'middle', ls='0.6')); o.append(hint(652, 90, 'one word, remove after a release'))
    o.append(S(16, 136, 'Card (.ab-card)'))
    o.append(R(16, 148, 300, 90, 4, C['surface'], C['line'])); o.append(T(32, 176, 'Idea template', 14, C['fg'], 500)); o.append(T(32, 198, 'Title, description and attachments.', 13, C['muted']))
    o.append(S(340, 136, 'Selectable card, selected'))
    o.append(R(340, 148, 300, 90, 4, '#F7FAFD', C['primary'])); o.append(R(340, 148, 3, 90, 0, C['primary']))
    o.append(checkbox(358, 164, True)); o.append(T(388, 178, 'Challenge template', 14, C['fg'], 500)); o.append(T(388, 200, 'Adds judging and stages.', 13, C['muted']))
    o.append(S(664, 136, 'Status flag (.ab-flag)'))
    o.append(R(664, 148, 360, 90, 4, C['surface'], C['line'])); o.append(Cc(684, 172, 5, C['ok']))
    o.append(T(698, 177, 'Export to IF tab: shown', 14, C['fg'], 500)); o.append(T(698, 198, 'The front end finds ExportToIFTab = true', 12, C['muted'])); o.append(T(698, 214, 'in the saved properties, so the tab appears.', 12, C['muted']))
    o.append(lines(16, 270, ['Chips 12px, 2px 8px, 10px radius. Status chips: tinted background, full-strength text, no border. Cards: white, 1px line, 4px radius, 14px 16px, no shadow.',
                             'Selected card: primary border, faint tint, 3px inset bar; ticking the card ticks its checkbox. Flag: 10px dot (muted / ok / error) + title 500 + why, 12px muted.'], 12, 20, C['muted']))
    return svg(W, H_, ''.join(o), 'Admin chips, badges and cards')

@fig('ds-settings-section')
def _():
    W, H_ = 1040, 420
    o = [H(16, 30, 'Settings section (.ab-section): view and edit')]
    x, y = 16, 50
    o.append(R(x, y, 490, 190, 4, C['surface'], C['line']))
    o.append(T(x+20, y+30, 'Company address', 14, C['fg'], 500)); o.append(btn(x+490-20-70, y+12, 'Edit', 'stroked', icon='edit', small=True)[0])
    for i, (k, v) in enumerate([('Street address', '12 Market Lane'), ('Town or city', 'Leeds'), ('County or state', None), ('Postcode', 'LS1 4AB'), ('Country', 'United Kingdom'), ('Phone', '+44 113 496 0000')]):
        cx, cy = x+20 + (i % 2)*230, y+60 + (i//2)*40
        o.append(T(cx, cy, k, 12, C['muted'])); o.append(T(cx, cy+18, v or 'Not set', 14, C['fg'] if v else C['ph']))
    o.append(T(x, y+214, 'View: every value the form can change, read only. Empty = “Not set”.', 12, C['muted']))
    x2 = 530
    o.append(R(x2, y, 494, 290, 4, C['surface'], C['primary'])); o.append(R(x2, y, 3, 290, 0, C['primary']))
    o.append(T(x2+20, y+30, 'Company address', 14, C['fg'], 500))
    o.append(field(x2+20, y+66, 220, 'Street address', '12 Market Lane', req=True))
    o.append(field(x2+254, y+66, 220, 'Town or city', 'Leeds'))
    o.append(field(x2+20, y+130, 220, 'Postcode', 'LS1', 'invalid', req=True, err='Enter a full postcode.'))
    o.append(field(x2+254, y+130, 220, 'Country', 'United Kingdom', icon='chev'))
    _, wc = btn(0, 0, 'Cancel', 'stroked')
    o.append(btn(x2+20, y+222, 'Cancel', 'stroked')[0]); o.append(btn(x2+28+wc, y+222, 'Save', 'primary', 'disabled', icon='save')[0])
    o.append(T(x2+28+wc+90, y+244, 'Fix the highlighted fields to save.', 12, C['muted']))
    o.append(T(x2, y+314, 'Edit: primary border + 3px bar, two-column .ab-form-grid, inline action bar.', 12, C['muted']))
    o.append(lines(16, 386, ['Card 16px 20px, max 960px, 16px apart. Each section saves on its own; one in edit at a time. Values: dl.ab-dl, dt 12px muted, dd 14px. Machine values in mono.'], 12, 18, C['muted']))
    return svg(W, H_, ''.join(o), 'Admin settings section view and edit')

# ===================================================================== right panel / feature list
@fig('ds-feature-list')
def _():
    W, H_ = 1040, 450
    o = [H(16, 30, 'Feature list')]
    x, y, w = 16, 50, 700
    o.append(T(x, y+16, 'Features', 17, C['fg'], 500)); o.append(T(x, y+40, 'Turn features on or off for your organisation. Select a feature to see what it does.', 14, C['muted']))
    o.append(field(x, y+58, 320, None, '', 'Search features', icon='search')); o.append(T(x+332, y+80, '24 features', 12, C['muted']))
    ty = y+104
    o.append(R(x, ty, w, 36 + 30 + 52*2 + 30 + 52, 4, C['surface'], C['line'])); o.append(R(x, ty, w, 36, 0, C['surface2']))
    o.append(OV(x+12, ty+23, 'Name')); o.append(OV(x+250, ty+23, 'Description')); o.append(OV(x+w-12, ty+23, 'Status', anchor='end'))
    yy = ty+36
    for grp, rows in [('Authentication and access', [('key', 'Sign-in methods', 'Choose how people sign in.', 'On', False), ('lock', 'Single session', 'Allow one device at a time.', 'Off', False)]),
                      ('AI', [('chat', 'AI chat', 'Let people ask questions in a chat panel.', 'On', True)])]:
        o.append(R(x+1, yy, w-2, 30, 0, C['bg'])); o.append(L(x, yy, x+w, yy)); o.append(OV(x+12, yy+20, grp)); yy += 30
        for icn, n, d, st, sel in rows:
            if sel: o.append(R(x+1, yy, w-2, 52, 0, C['tint']))
            o.append(L(x, yy, x+w, yy)); o.append(icontile(x+12, yy+10, icn)); o.append(T(x+56, yy+31, n, 14, C['fg'], 500))
            o.append(T(x+250, yy+31, d, 13, C['muted'])); o.append(chip(x+w-12-(52 if st == 'On' else 50), yy+16, st, 'ok' if st == 'On' else 'neutral', False)[0]); yy += 52
    o.append(legend([('1', 'Group row', ['overline on --ab-bg; hidden with no matches']), ('2', 'Name cell', ['32px icon tile + name 14 / 500', '<button aria-expanded aria-controls>']),
                     ('3', 'Description', ['13px muted, one line, ellipsis']), ('4', 'Status', ['“On” ok / “Off” neutral; text, not colour']),
                     ('5', 'Open row', ['--ab-primary-tint while its panel is open'])], 740, 64, 56))
    for n, (px_, py_) in zip('12345', [(x+w-24, ty+51), (x+90, ty+18), (x+366, ty+18), (x+w-70, ty+18), (x+w-90, ty+250)]): o.append(marker(n, px_, py_))
    o.append(T(x, 434, 'The list never changes a setting by itself: no switches in rows. Everything happens in the panel and is committed with Save.', 12, C['muted']))
    return svg(W, H_, ''.join(o), 'Admin feature list')

@fig('ds-right-panel')
def _():
    W, H_ = 1040, 600
    o = [H(16, 30, 'Right-hand panel (.ab-panel)')]
    fx, fy, fw, fh = 16, 50, 660, 534
    o.append(R(fx, fy, fw, fh, 6, C['surface'], C['line']))
    for i in range(9): o.append(R(fx+20, fy+30+i*50, 260, 30, 4, C['surface2']))
    o.append(R(fx, fy, fw, fh, 6, C['scrim'], op=.32))
    pw = 380; px = fx+fw-pw
    o.append(R(px, fy, pw, fh, 0, C['surface'])); o.append(L(px, fy, px, fy+fh))
    o.append(R(px+1, fy, pw-1, 96, 0, C['tint']))
    o.append(T(px+24, fy+42, 'AI chat', 22, C['fg'], 500)); o.append(btn(px+pw-24-34, fy+16, '', 'icon', icon='close')[0])
    o.append(T(px+24, fy+72, 'Let people ask questions about applications', 14, C['fg'])); o.append(T(px+24, fy+90, 'in a chat panel.', 14, C['fg']))
    o.append(checkbox(px+24, fy+122, True, label='Turn on AI chat'))
    o.append(L(px+24, fy+164, px+pw-24, fy+164))
    o.append(OV(px+24, fy+192, 'Settings')); o.append(T(px+24, fy+218, 'Who can use AI chat', 12, C['fg'], 500))
    o.append(radio(px+24, fy+230, True, 'Everyone')); o.append(radio(px+24, fy+260, False, 'People with the AI Assistant role'))
    o.append(L(px+24, fy+304, px+pw-24, fy+304))
    o.append(OV(px+24, fy+332, 'Daily limit')); o.append(field(px+24, fy+350, 160, None, '50', hint_='Questions per person per day'))
    o.append(L(px, fy+fh-64, px+pw, fy+fh-64))
    _, ws = btn(0, 0, 'Save', icon='save')
    o.append(btn(px+24, fy+fh-48, 'Save', icon='save')[0]); o.append(btn(px+32+ws, fy+fh-48, 'Cancel', 'stroked')[0])
    o.append(callout('1', px+120, fy+48, px+300, fy+48+0) if False else '')
    marks = [('1', px-4, fy+260), ('2', px+pw-80, fy+28), ('3', px+pw-60, fy+130), ('4', px+pw-40, fy+234), ('5', px+pw-60, fy+fh-31), ('6', fx+150, fy+500)]
    for n, mx, my in marks: o.append(marker(n, mx, my))
    o.append(legend([('1', 'Panel', ['fixed right, full height, min(520px, 100vw)', '--wide 720px · --xwide 960px', 'role="dialog" aria-modal, labelled by title']),
                     ('2', 'Header band', ['primary tint · title 22 / 500 · description', 'close icon button top right']),
                     ('3', 'On / off', ['checkbox “Turn on {feature}”, not a switch:', 'nothing happens until Save']),
                     ('4', 'Groups', ['no box; split by hairlines, 20px either side', 'shown only while the feature is on']),
                     ('5', 'Footer', ['pinned · Save (primary) then Cancel, left', 'the one exception to “primary last”']),
                     ('6', 'Scrim', ['rgba(15,27,42,.32) · click closes · Esc closes'])], 700, 64, 56))
    return svg(W, H_, ''.join(o), 'Admin right-hand panel')

@fig('ds-panel-variants')
def _():
    W, H_ = 1040, 300
    o = [H(16, 30, 'Panel widths and variants')]
    def mini(x, w, title, sub_, footer):
        out = [R(x, 52, 240, 170, 4, C['surface2'], C['line']), R(x+240-w, 52, w, 170, 0, C['surface'], C['line']), R(x+241-w, 52, w-1, 34, 0, C['tint'])]
        out.append(R(x+250-w, 64, 50, 8, 2, C['fg']))
        for i in range(3): out.append(R(x+250-w, 100+i*22, w-20, 10, 2, C['surface2']))
        if footer == 'save': out.append(R(x+250-w, 196, 30, 16, 3, C['primary'])); out.append(R(x+286-w, 196, 34, 16, 3, C['surface'], C['line']))
        if footer == 'done': out.append(R(x+250-w, 196, 30, 16, 3, C['primary'])); out.append(T(x+288-w, 208, 'Saved with app.', 8.5, C['muted']))
        out.append(T(x, 244, title, 13, C['fg'], 500)); out.append(T(x, 262, sub_, 11.5, C['muted']))
        return ''.join(out)
    o.append(mini(16, 120, '.ab-panel · 520px', 'checkbox and a few fields', 'save'))
    o.append(mini(272, 160, '.ab-panel--wide · 720px', 'two-column forms, lists', 'save'))
    o.append(mini(528, 210, '.ab-panel--xwide · 960px', 'a table (Currencies, row log)', None))
    o.append(mini(784, 120, 'Inside an editor', 'Done + “Saved with the application.”', 'done'))
    o.append(T(16, 288, 'Settings sections inside a panel have their own Edit / Save, so that panel has no footer. One panel at a time; another row replaces its content.', 12, C['muted']))
    return svg(W, H_, ''.join(o), 'Admin panel widths and variants')

# ===================================================================== notes, code, toast, states
@fig('ds-notes-code')
def _():
    W, H_ = 1040, 330
    o = [H(16, 30, 'Notes and API preview')]
    for i, (k, col, bgc, t) in enumerate([('', None, C['surface2'], 'Keys are case-insensitive and must be unique.'), ('--info', C['primary'], C['surface2'], 'Only a Points Admin can change this.'),
                                          ('--warn', C['warn'], C['wtint'], 'Turning this off resets everyone’s points.'), ('--danger', C['danger'], C['dtint'], 'We couldn’t load the features. Try again.')]):
        y = 52 + i*62
        o.append(R(16, y, 480, 50, 4, bgc, C['line']))
        if col: o.append(R(16, y, 3, 50, 0, col))
        o.append(T(32, y+30, t, 13, C['muted'])); o.append(T(510, y+30, f'.ab-note{k}', 12, C['muted'], mono=True))
    x = 640
    o.append(OV(x, 60, 'Returned by content/get'))
    o.append(T(x, 86, 'GET', 12, C['ok'], 500, mono=True)); o.append(T(x+32, 86, '/api/content/get?id=1042', 12, C['fg'], mono=True))
    o.append(R(x, 100, 384, 130, 4, C['codebg']))
    for i, (a, b, c_) in enumerate([('{', '', ''), ('  "Id": ', '1042', 's'), ('  "CustomProperties": {', '', ''), ('    "ExportToIFTab": ', '"true"', 's'), ('  }, …', '', '')]):
        o.append(f'<text x="{x+14}" y="{124+i*20}" font-size="12" font-family="{MONO}" fill="{C["codekey"] if i == 3 or i == 1 else C["codefg"]}">{esc(a)}<tspan fill="{C["codestr"]}">{esc(b)}</tspan></text>')
    o.append(lines(x, 256, ['Preview shows the saved state, not unsaved edits.', 'Elide unrelated fields with “…”. Escape everything.'], 12, 18, C['muted']))
    o.append(T(16, 312, 'Notes: surface-2, 1px border, 14px 16px, muted, 1.55 line height, max 70ch. For things to know, not things to act on now.', 12, C['muted']))
    return svg(W, H_, ''.join(o), 'Admin notes and API preview')

@fig('ds-feedback')
def _():
    W, H_ = 1040, 330
    o = [H(16, 30, 'Toast, empty, loading and error')]
    def card(x, t): return R(x, 66, 240, 170, 4, C['surface'], C['line']) + S(x, 56, t)
    o.append(card(16, 'Empty (.ab-empty)'))
    o.append(T(136, 142, 'No users yet.', 14, C['muted'], anchor='middle')); o.append(T(136, 162, 'Select Add user to invite someone.', 12, C['muted'], anchor='middle'))
    o.append(card(272, 'Loading'))
    o.append(R(273, 67, 238, 2, 0, C['tint2'])); o.append(R(273, 67, 90, 2, 0, C['primary']))
    for i in range(4): o.append(R(288, 90 + i*30, 120, 12, 3, C['surface2'])); o.append(R(420, 90 + i*30, 70, 12, 6, C['surface2']))
    o.append(T(392, 256, 'Skeletons first load · 2px bar on refresh', 11.5, C['muted'], anchor='middle'))
    o.append(card(528, 'Error loading'))
    o.append(R(544, 82, 208, 92, 4, C['dtint'], C['line'])); o.append(R(544, 82, 3, 92, 0, C['danger']))
    o.append(T(558, 108, 'We couldn’t load users.', 13, C['fg'], 500)); o.append(T(558, 128, 'Check your connection.', 12, C['muted']))
    o.append(btn(558, 138, 'Try again', 'stroked', small=True)[0])
    o.append(S(784, 56, 'Toast (.ab-toast)'))
    o.append(R(784, 70, 240, 42, 4, C['fg'])); o.append(ic('check_circle', 798, 82, '#7FC383', 18)); o.append(T(824, 96, 'Custom properties saved.', 13, '#fff'))
    o.append(R(784, 124, 240, 42, 4, C['danger'])); o.append(T(800, 150, 'We couldn’t save. Try again.', 13, '#fff')); o.append(ic('close', 998, 137, '#fff', 16))
    o.append(lines(784, 190, ['Bottom centre, 20px up · ~2.2s', 'Errors stay until dismissed', 'Past tense, full stop, no “!”'], 11.5, 17, C['muted']))
    o.append(T(16, 312, 'No spinner for waits under 250ms. Inline 18px spinner in the Save button; 44px overlay only for full-panel waits.', 12, C['muted']))
    return svg(W, H_, ''.join(o), 'Admin feedback states')

@fig('ds-dialog')
def _():
    W, H_ = 1040, 330
    o = [H(16, 30, 'Modal confirmation (app-default-dialog)')]
    o.append(R(16, 50, 520, 260, 4, C['scrim'], op=.32))
    x, y, w = 76, 80, 400
    o.append(R(x, y, w, 196, 8, C['surface']))
    o.append(ic('delete', x+24, y+24, C['danger'], 24)); o.append(T(x+58, y+43, 'Delete property?', 18, C['fg'], 500))
    o.append(btn(x+w-24-34, y+18, '', 'icon', icon='close')[0])
    o.append(T(x+24, y+84, 'ReportCode is removed from this application and', 14)); o.append(T(x+24, y+105, 'from the API. You can’t undo this.', 14))
    _, wd = btn(0, 0, 'Delete property', 'dsolid'); _, wc = btn(0, 0, 'Cancel', 'stroked')
    o.append(btn(x+w-24-wd, y+138, 'Delete property', 'dsolid')[0]); o.append(btn(x+w-24-wd-8-wc, y+138, 'Cancel', 'stroked')[0])
    # spacing marks
    for (yy1, yy2, lab) in [(y, y+24, '24'), (y+52, y+68, '16'), (y+112, y+138, '24')]:
        o.append(L(x-12, yy1, x-12, yy2, C['note'])); o.append(T(x-16, (yy1+yy2)/2+4, lab, 10.5, C['note'], 500, 'end'))
    o.append(T(x+w-24-wd-4, y+190, '8', 10.5, C['note'], 500, 'middle'))
    o.append(R(570, 50, 454, 260, 4, C['surface'], C['line']))
    o.append(S(586, 74, 'Spec'))
    o.append(lines(586, 98, ['Heading 18 / 500, line 24 · body 14 / 400, line 21', 'Padding 24 · heading → body 16 · body → actions 24', 'Buttons right aligned, 8 apart: Cancel (stroked),',
                             'then primary or danger-solid repeating the verb', 'Optional 24px status icon; optional round close', 'Width small 20vw · medium 40vw (default) · large 60vw', 'x-large 80vw · min 360px · full width ≤ 768px', '',
                             'Body: what happens and whether it can be undone.', 'Longer than a short form → right panel, not a modal.'], 12, 19))
    return svg(W, H_, ''.join(o), 'Admin modal confirmation')

@fig('ds-stats')
def _():
    W, H_ = 1040, 200
    o = [H(16, 30, 'Stats (.ab-stats)')]
    tiles = [('group', 'Users on the licence', '1,248 / 1,500', False, False), ('block', 'Suspended users', '37', True, False), ('person_add', 'Administrator', 'Alex Morgan', False, True)]
    for i, (icn, lab, val, d, txt) in enumerate(tiles):
        x = 16 + i*262
        o.append(R(x, 50, 250, 64, 4, C['surface'], C['line'])); o.append(icontile(x+16, 66, icn, danger=d))
        o.append(T(x+60, 74, lab, 12, C['muted'])); o.append(T(x+60, 98, val, 14 if txt else 22, C['fg'], 500))
    o.append(R(806, 50, 218, 64, 4, C['surface'], C['line'])); o.append(T(822, 74, 'Loading', 12, C['muted'])); o.append(T(822, 98, '…', 22, C['fg'], 500))
    o.append(lines(16, 144, ['2–4 tiles between the title and the actions. Label 12px muted; value 22 / 500 with tabular figures; words 14px. “…” while loading, “–” when missing.',
                             'Danger tile for figures that need attention. A figure that links to a filtered list makes the whole tile the link. Never a substitute for the table.'], 12, 20, C['muted']))
    return svg(W, H_, ''.join(o), 'Admin stats')

@fig('ds-action-bar')
def _():
    W, H_ = 1040, 300
    o = [H(16, 30, 'Action bar and saving')]
    x, w = 16, 1008
    o.append(S(x, 64, 'Sticky (.ab-actionbar--sticky) — multi-tab workspaces'))
    o.append(R(x, 76, w, 60, 0, C['surface'], C['line']))
    o.append(btn(x+20, 89, 'Back', 'text', icon=None)[0])
    _, ws = btn(0, 0, 'Save', icon='save'); _, wn = btn(0, 0, 'Next', 'stroked'); _, wc = btn(0, 0, 'Discard changes', 'stroked')
    xs = x+w-20-ws
    o.append(btn(xs, 89, 'Save', icon='save')[0]); o.append(btn(xs-8-wn, 89, 'Next', 'stroked')[0]); o.append(btn(xs-16-wn-wc, 89, 'Discard changes', 'stroked')[0])
    o.append(T(xs-28-wn-wc, 111, 'Unsaved changes', 12, C['muted'], anchor='end'))
    o.append(S(x, 170, 'Status text (.ab-status) beside the buttons'))
    for i, (s, en) in enumerate([('All changes saved', False), ('Unsaved changes', True), ('2 rows need fixing before you can save', False)]):
        y = 184 + i*38
        o.append(btn(x, y, 'Save', 'primary', None if en else 'disabled', icon='save')[0]); o.append(T(x+ws+12, y+22, s, 12, C['muted']))
    o.append(R(560, 170, 464, 112, 4, C['surface'], C['line']))
    o.append(lines(576, 194, ['Order: Back far left → spacer → Cancel / Discard → Next →', 'Save last, far right. Exactly one primary.', 'Inline variant (.ab-actionbar--inline): under a single form, 18px above.',
                              'Leaving with unsaved changes asks first (canDeactivate).', 'After saving: toast, and previews update from saved data.'], 12, 19))
    return svg(W, H_, ''.join(o), 'Admin action bar and saving')

@fig('ds-accordion')
def _():
    W, H_ = 1040, 220
    o = [H(16, 30, 'Accordions (cdk-accordion)')]
    x = 16
    o.append(R(x, 50, 300, 150, 4, C['surface'], C['line']))
    for i, (lab, open_) in enumerate([('Basic fields', True), ('Advanced fields', False)]):
        y = 50 + i*96
        o.append(OV(x+14, y+24, lab)); o.append(ic('chevup' if open_ else 'chev', x+270, y+10, C['muted'], 18))
        if open_:
            for j, f in enumerate(['Single line input', 'Paragraph']):
                o.append(R(x+14, y+36+j*26, 272, 22, 4, C['surface2'])); o.append(T(x+24, y+51+j*26, f, 12.5))
        if i == 0: o.append(L(x, y+96, x+300, y+96))
    o.append(lines(360, 70, ['Every group starts expanded ([multi]="true", [expanded]="true"); people collapse what they don’t need.', 'Header: 11 / 500 caps .06em, muted, with a chevron; the header is a real button.',
                             'No hover background on the header; focus still shows the ring.', 'Used in the form builder and entity builder palettes and property columns.'], 12.5, 22))
    return svg(W, H_, ''.join(o), 'Admin accordions')

if __name__ == '__main__':
    for name, fn in FIGS.items():
        with open(os.path.join(OUT, f'{name}.svg'), 'w', encoding='utf-8') as f: f.write(fn())
    print(len(FIGS), 'figures written to', OUT)
