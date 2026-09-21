# Deploying to a GitHub Pages site

Instructions for whoever publishes this - a person or another Claude Code session.

## What this folder is

A **self-contained static site**. No build step, no server code, no dependencies to
install. It needs only a static host and, in the visitor's browser, internet access for
one library (three.js from unpkg.com).

- 1360 files, 124 MB total; largest single file 9.6 MB
  (GitHub rejects files over 100 MB and recommends repos under 1 GB - both fine)
- All paths are **relative**, so it works in a subfolder

## Steps

1. Pick a subfolder of the Pages repo, e.g. `colon/`, so the viewer lives at
   `https://<user>.github.io/colon/`. (If an older version already lives in `c3vd/`,
   replace that folder's contents instead.)
2. Copy **the contents of this folder** into it (so `colon/index.html` exists).
   Do not rename any file under `seq/` - the manifest refers to them by name.
3. **Jekyll check.** Pages runs Jekyll by default, and Jekyll silently drops files and
   folders whose names start with `_`. Nothing in this bundle does, so no action is
   needed. If the site's `_config.yml` has an `exclude:` list, make sure it doesn't
   match `seq` or `*.bin`/`*.glb`.
4. Commit and push. Pages usually publishes within a couple of minutes.
5. **Verify on the live URL** (not locally):
   - six buttons in the top-left panel (four C3VD segments, two whole colons), none
     with a dashed outline
   - the browser console shows no errors
   - clicking the wall opens a panel with a frame
   - switching between *Clarity* and *Seen or not* recolours the model
   - on *ACRIN patient 0233*, the polyp search band checkbox paints a yellow band

## Updating later

Rebuild with `build_web.py` (C3VD) or `build_realsyncol_web.py` (CT colons), rerun
`package_site.py`, and **replace the whole folder**
rather than copying over individual files. Every data file URL carries a content
fingerprint from `manifest.json` (`?v=...`), so returning visitors pick up the new
files instead of cached old ones - but only if the manifest and data files are
published together.

## Licence obligations

Three datasets, three licences (details in `README.md`): C3VD is CC BY-NC-SA 4.0,
RealSynCol CC BY 4.0 per its Zenodo record, ACRIN/TCIA CC BY 3.0. Keep the credit
panel in the page, keep `README.md`, and don't use the bundle commercially (C3VD's
terms). If you link to the viewer from elsewhere on the site, credit C3VD (Bobrow et
al., 2023), RealSynCol, and the ACRIN 6664 trial / TCIA next to the link.
