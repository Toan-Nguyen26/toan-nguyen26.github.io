# Where the colonoscope never looked

An interactive viewer of colonoscope **coverage** on the C3VD dataset: which parts of
the colon wall a real colonoscope captured, how clearly, and the actual frames behind
every spot.

Open `index.html` through a web server (it loads its data with `fetch`, which browsers
block for pages opened straight from disk).

## What is shown

- **Four colon segments** (cecum, transverse, descending, sigmoid), one recorded exam each.
- **Clarity colouring** (default): red = never seen; grey from dark to light = seen
  blurry to seen sharp. Clarity is the number of pixels that covered 1 mm of wall in
  that spot's clearest frame, counting only pixels visible in the video.
- **Seen or not**: C3VD's own per-face coverage flag.
- **Click the wall** to see the real frames that captured that spot.

The 2 / 10 / 20 px-per-mm clarity thresholds are **provisional** - where "clear enough
to spot a lesion" sits is a clinical judgement that has not been made yet.

## Data and licence

Built from **C3VD** - Bobrow, T. L., et al. *Colonoscopy 3D video dataset with paired
depth from 2D-3D registration.* Medical Image Analysis, 2023. https://durrlab.github.io/C3VD/

C3VD is licensed **CC BY-NC-SA 4.0** (https://creativecommons.org/licenses/by-nc-sa/4.0/).
This viewer and its derived data files are shared under the same licence:
**non-commercial use only, with attribution, share-alike.**

The mesh, coverage flags, frames and camera poses are C3VD ground truth. Which frames
saw each spot, and each spot's clarity, were computed here by ray casting the registered
poses through the calibrated camera model; the computed coverage agrees with C3VD's on
99.79-99.96% of faces.
