# Deploying to a GitHub Pages site

Instructions for whoever publishes this - a person or another Claude Code session.

## What this folder is

A **self-contained static site**. No build step, no server code, no dependencies to
install. It needs only a static host and, in the visitor's browser, internet access for
one library (three.js from unpkg.com).

- 2023 files, 144 MB total; largest single file 9.6 MB
  (GitHub rejects files over 100 MB and recommends repos under 1 GB - both fine)
- All paths are **relative**, so it works in a subfolder

## Steps

0. **If this arrived as several `-partNN.zip` files**, extract them all into the same
   place first. The order does not matter and no file is split across archives - each
   part holds whole files. After extracting all of them you should have one
   `colon-coverage/` folder; check it has `index.html`, `manifest.json` and a `seq/`
   folder before going on. The parts exist only because the bundle is too big for some
   upload limits; there is nothing to merge by hand.
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
   - **nine** buttons in the top-left panel (four C3VD segments, five whole colons from
     CT), none with a dashed outline
   - the browser console shows no errors
   - switching between *Clarity*, *Seen or not* and *Flythrough* recolours the model
   - in *Flythrough*: the transport bar appears at the bottom, the frame the scope is
     looking at appears on the right, and Space plays it
   - *Side view* (bottom right of the transport) turns the eye to look at the scope
     from beside it, showing the lens's 195-degree cone
   - **N** toggles the numbers panel (collapsed by default), **L** the legend
   - on the CT colons, the *ACRIN record* checkbox paints a yellow band; on
     *ACRIN patient 0233* and *0516 prone* a purple candidate marker also appears

## Updating later

Rebuild with `build_web.py` (C3VD) or `build_realsyncol_web.py` (CT colons), rerun
`package_site.py`, and **replace the whole folder**
rather than copying over individual files. Every data file URL carries a content
fingerprint from `manifest.json` (`?v=...`), so returning visitors pick up the new
files instead of cached old ones - but only if the manifest and data files are
published together.

## Licence obligations

Three sources, three licences (details in `README.md`): C3VD is CC BY-NC-SA 4.0,
the HQColon masks CC BY 4.0 per their OSF record, ACRIN/TCIA CC BY 3.0. Keep the credit
panel in the page, keep `README.md`, and don't use the bundle commercially (C3VD's
terms). If you link to the viewer from elsewhere on the site, credit C3VD (Bobrow et
al., 2023), HQColon (Finocchiaro et al., Sci Data 2026), and the ACRIN 6664 trial /
TCIA next to the link.

Note the HQColon *article* is CC BY-NC-ND 4.0 while the *masks* on OSF are CC BY 4.0 —
it is the masks this bundle is derived from.
