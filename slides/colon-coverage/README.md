# Where the colonoscope never looked

An interactive viewer of colonoscope **coverage**: which parts of the colon wall a
colonoscope captured, how clearly, and what the scope was looking at as it went.

## What is in it

| Button | Colon | Source |
|---|---|---|
| Cecum, Transverse, Descending, Sigmoid | segments of a sculpted silicone phantom, real colonoscope video | C3VD |
| ACRIN patient 0233 | a whole human colon from the raw CT scan: TotalSegmentator identifies the colon, the CT's gas edge gives the wall | TCIA CT COLONOGRAPHY (ACRIN 6664) |
| 0516 supine / prone, 0639 supine / prone | two more patients, each scanned in both positions | HQColon masks over ACRIN 6664 |

CT colonography is done in **two positions** in the same session. It is the same colon
both times, but gas and fluid move with gravity and collapsed stretches open up, so the
two scans do not show the same thing — patient 0639 reads 69.6 % of the wall seen supine
and 78.7 % prone. Where both are published, both are here.

- **Clarity** (default): the pixels that covered 1 mm of wall in the clearest frame of
  each spot. The 10 px/mm "clear" threshold is **provisional**; where "clear enough"
  sits is a clinical call.
- **Seen or not**: whether any frame saw the spot at all.
- **Flythrough**: the scope runs down the colon frame by frame. Bright = in view in
  that frame, grey = already passed and seen, red = the scope has not seen it yet.
  Red left behind the scope is the miss the headline percentage counts. Same ray
  cast as the coverage number, kept per frame instead of summed.
  The frame the scope is looking at is shown beside it, and the numbers panel
  collapses (**N**) to leave it the room. **Side view** turns the eye to look at the
  scope from beside it, where the lens's 195-degree field is drawn as a cone: past
  90 degrees it opens backwards, which is why so much of a short segment lights at once.
- **ACRIN record**: a yellow band marks the CT slices where the ACRIN 6664 trial recorded
  a polyp for that patient. It is a slice number, not a location — one axial slice cuts a
  folded colon in several places.
- **Candidate marker**: purple marks a cap-shaped cluster found by a blind scan of the
  whole colon, **not read by a radiologist**. On *0516 prone* it lands on slice 257,
  exactly the slice ACRIN gives, and measures 19.7 mm against ACRIN's recorded 20 mm.

Blue on the CT colon marks colon cut off from the camera in that scan (a collapsed or
fluid-filled stretch); it is shown but left out of every percentage.

For the C3VD segments the frames are the real colonoscope video. For the CT colon
there is no video: the camera path is a centreline generated here, and the frames are
ray-cast from the mesh under a headlight. They show shape only, because CT records
no mucosa. Coverage for every colon is computed through the real colonoscope lens
(C3VD's calibrated fisheye); the method agrees with C3VD's own coverage on 99.79 to
99.96 % of faces.

## Data, credits and licences

Each dataset keeps its own licence. The page's credit panel changes with the colon
shown; keep it, and keep this file.

- **C3VD** - Bobrow, T. L., et al. *Colonoscopy 3D video dataset with paired depth from
  2D-3D registration.* Medical Image Analysis, 2023. https://durrlab.github.io/C3VD/
  Licence **CC BY-NC-SA 4.0**: non-commercial, share-alike.
- **RealSynCol** - Lena, C., et al. *RealSynCol: a high-fidelity synthetic colon dataset
  for 3D reconstruction applications*, 2026. https://zenodo.org/records/19705803
  The Zenodo record lists **CC BY 4.0** (the paper's text says CC BY-SA 4.0; if in
  doubt, treat it as share-alike). Only the mesh is used; the dataset's own trajectory
  does not line up with its mesh, so the path here is generated.
- **ACRIN 6664 / TCIA CT COLONOGRAPHY** - Johnson, C. D., et al. *Accuracy of CT
  colonography for detection of large adenomas and cancers.* NEJM, 2008.
  doi:10.1056/NEJMoa0800996. Images from The Cancer Imaging Archive,
  doi:10.7937/K9/TCIA.2015.NWTESAY1. Licence **CC BY 3.0**.
- **TotalSegmentator** - Wasserthal, J., et al. *TotalSegmentator: robust segmentation of
  104 anatomic structures in CT images.* Radiology: Artificial Intelligence, 2023. Used to
  decide which gas in the ACRIN scan is colon.

Because the C3VD parts are non-commercial, do not use this bundle commercially.
