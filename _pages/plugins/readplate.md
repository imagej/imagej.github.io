---
title: ReadPlate
description: Measure absorbance values from photographs of 6-, 12-, 24-, 48-, or 96-well plates.
categories: [Analysis, Color Processing]
doi: 10.1002/bmb.21139

name: ReadPlate
initial-release-date: "2015"
team-founder: "José María Delfino"
team-maintainer: "José María Delfino"
support-status: Active
source-label: GitHub
source-url: https://github.com/ghanerka/ReadPlate
---

ReadPlate is an ImageJ macro for measuring light intensity and calculating
uncorrected, blank, and blank-corrected absorbance values from a color
photograph of a multi-well plate. ReadPlate 3.0 supports 6 (3x2), 12 (4x3),
24 (6x4), 48 (8x6), and 96 (12x8) well plates.

## Installation

ReadPlate is distributed through this Fiji update site:

{% include link-banner url="https://ghanerka.github.io/ReadPlate/" %}

In Fiji, choose {% include bc path='Help|Update...' %}, open **Manage update
sites**, and enable **ReadPlate**. If the canonical registry still shows the
older unavailable URL, use **Add Unlisted Site** with the URL above. Apply the
changes and restart Fiji. The command is then available at {% include bc path='Plugins|ReadPlate 3.0' %}.

The update site installs the macro together with its original HTML
documentation and sample 96-well plate image.

## Requirements

- ImageJ 1.43h or newer
- A 24-bit RGB plate image

Version 3.0 was tested with ImageJ 1.53c and Java 8. Before running it, choose
{% include bc path='Analyze|Set Measurements...' %} and enable Area, Standard
Deviation, Min & Max Gray Value, Mean Gray Value, Modal Gray Value, and Add to
Overlay. Set Redirect to None and Decimal Places to 3.

## Use

1. Open a color photograph of a plate whose borders are aligned with the image.
2. Run {% include bc path='Plugins|ReadPlate 3.0' %}.
3. Select the plate format.
4. Draw a center-to-center rectangular selection from the upper-left to the
   lower-right corner well.
5. Select the red, green, blue, or gray measurement channel.
6. Adjust the main and ancillary circle-grid parameters, verify the overlay,
   and collect measurements.
7. Inspect and optionally save the Results table. Corrected absorbance is
   reported as `Acorr`.

The full original documentation, macro, sample image, release checksums, and
citation metadata are available from the [ReadPlate source
repository](https://github.com/ghanerka/ReadPlate) and its [3.0
release](https://github.com/ghanerka/ReadPlate/releases/tag/v3.0.0).

## Citation

Angelani CR, Carabias P, Cruz KM, Delfino JM, *et al.* (2018). “A Metabolic
Control Analysis Approach to Introduce the Study of Systems in Biochemistry:
the Glycolytic Pathway in the Red Blood Cell.” *Biochemistry and Molecular
Biology Education* 46(5): 502–515. [doi:10.1002/bmb.21139](https://doi.org/10.1002/bmb.21139)
