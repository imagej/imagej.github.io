---
mediawiki: DHM_Utilities/Multi-Image_Landmark_Correspondences
title: DHM Utilities/Multi-Image Landmark Correspondences
project: /plugins/dhm-utilities
name: Multi-Image Landmark Correspondences
source-url: https://github.com/sudgy/multi-landmark
license-url: /licensing/lgpl
license-label: LGPLv3
dev-status: Active
support-status: Active
team-founders: David Cohoe | mailto:dcohoe@pdx.edu
team-leads: David Cohoe | mailto:dcohoe@pdx.edu
team-developers: David Cohoe | mailto:dcohoe@pdx.edu
team-debuggers: David Cohoe | mailto:dcohoe@pdx.edu
team-reviewers: David Cohoe | mailto:dcohoe@pdx.edu
team-support: David Cohoe | mailto:dcohoe@pdx.edu
team-maintainers: David Cohoe | mailto:dcohoe@pdx.edu
---

Multi-Image Landmark Correspondences is a plugin that extends mpicbg's [Landmark Correspondences](/plugins/landmark-correspondences) plugin to multiple images. It takes in any number of images that have point ROIs and aligns them all. It is included with DHM Utilities because we have used it to deal with some of the effects of chromatic aberration.

## Usage

To run the plugin, run the command {% include bc path="Plugins | Transform | Multi-Image Landmark Correspondences" %}. A dialog will pop up with the following options:

-   Interpolation Type: What type of interpolation to use when transforming.
-   Suppress interpolation at discontinuities: If interpolation is enabled, this parameter will appear. Enabling this option will disable interpolation at points on the image where there are discontinuities, but will still allow interpolation to happen elsewhere. It is useful when dealing with phase images, because discontinuities need to be sharp if an unwrapping algorithm is to be used.
-   Discontinuity threshold: If suppressing interpolation, this parameter will appear. It is the lowest pixel value difference that is considered to be a discontinuity, and for any differences greater than or equal to this value, no interpolation will happen.
-   Scale to...: Which image to scale to. There are three options:
    -   Biggest Image: Scale such that everything scales up.
    -   Smallest Image: Scale such that everything scales down.
    -   Specific Image: Scale all images to a particular image. If this option is selected, another parameter will appear to be the image to scale to.
-   Transform Type: Which kind of transform you wish to use.
-   Show Transform Matrices: Whether or not you wish to see the transformation matrices being used.
