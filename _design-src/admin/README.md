# Admin design system pages: sources

The pages under `docs/design-standards/admin/` are generated. Jekyll ignores folders starting with `_`, so
nothing here is published.

| File | Purpose |
|---|---|
| `gen_ds_svgs.py` | Draws the `ds-*.svg` diagrams from the `--ab-*` tokens (AapliAdmin `src/scss/design-system/_tokens.scss`) |
| `build_admin_ds.py` | Splits AapliAdmin `docs/DESIGN_SYSTEM.md` into pages, adds the diagrams, writes the single-file copy |

The source of truth is AapliAdmin `docs/DESIGN_SYSTEM.md` (branch `redesign`). After it changes:

```bash
cd _design-src/admin
python3 gen_ds_svgs.py ../../assets/images/design-standards/admin
python3 build_admin_ds.py "../../../AapliAdmin/docs/DESIGN_SYSTEM.md" ../..
cp ../../../AapliAdmin/docs/design-system/*.png ../../assets/images/design-standards/admin/
cp ../../../AapliAdmin/docs/design-system/*.html ../../assets/design-standards/admin/prototypes/
```

If a token or a component spec changes, update the matching figure in `gen_ds_svgs.py` too.
