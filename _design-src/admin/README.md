# Admin design system pages: sources

The pages under `docs/design-standards/admin/` are generated. Jekyll ignores folders starting with `_`, so
nothing here is published.

| File | Purpose |
|---|---|
| `gen_ds_svgs.py` | Copy of the generator that draws the `ds-*.svg` diagrams. The master copy is AapliAdmin `docs/design-system/diagrams/gen_ds_svgs.py` |
| `build_admin_ds.py` | Splits AapliAdmin `docs/DESIGN_SYSTEM.md` into pages and writes the single-file copy |

The source of truth is AapliAdmin `docs/DESIGN_SYSTEM.md` (branch `redesign`). Since v2.7.2 it carries the
diagrams itself (`docs/design-system/diagrams/`). After it changes, run this from the repository root:

```bash
cp ../AapliAdmin/docs/design-system/diagrams/*.svg assets/images/design-standards/admin/
cp ../AapliAdmin/docs/design-system/*.png assets/images/design-standards/admin/
cp ../AapliAdmin/docs/design-system/*.html assets/design-standards/admin/prototypes/
python3 _design-src/admin/build_admin_ds.py ../AapliAdmin/docs/DESIGN_SYSTEM.md .
```

To change a diagram, edit AapliAdmin's `gen_ds_svgs.py`, then run it into `docs/design-system/diagrams/`.
