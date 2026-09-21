# Where the colonoscope never looked

An interactive viewer of colonoscope **coverage**: which parts of the colon wall a
colonoscope captured, how clearly, and the frames behind each spot.

## What is in it

| Button | Colon | Source |
|---|---|---|
| Cecum, Transverse, Descending, Sigmoid | segments of a sculpted silicone phantom, real colonoscope video | C3VD |
| RealSynCol colon | a whole human colon segmented from CT colonography | RealSynCol (from ACRIN 6664) |
| ACRIN patient 0233 | a whole human colon from the raw CT scan: TotalSegmentator identifies the colon, the CT's gas edge gives the wall | TCIA CT COLONOGRAPHY (ACRIN 6664) |

- **Clarity** (default): the pixels that covered 1 mm of wall in the clearest frame of
  each spot. The 10 px/mm "clear" threshold is **provisional**; where "clear enough"
  sits is a clinical call.
- **Seen or not**: whether any frame saw the spot at all.
- **Click the wall** to see the frames that captured that spot.
- **Polyp search band** (ACRIN patient 0233 only): the colon wall within +/-10 CT
  slices of where ACRIN recorded an 18 mm polyp.

Blue on the CT colons marks colon cut off from the camera in that scan (a collapsed or
fluid-filled stretch); it is shown but left out of every percentage.

For the C3VD segments the frames are the real colonoscope video. For the two CT colons
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
