---
title: Temporal-Color Code
categories: [Color Processing]
name: Temporal-Color Code
project: /software/fiji
icon: /media/icons/fiji.svg
source-url: https://github.com/fiji/fiji/blob/master/plugins/Scripts/Image/Hyperstacks/Temporal-Color_Code.ijm
release-date: 29 Nov 2010
dev-status: beta
team-maintainers: Kota Miura | /people/cmci
team-contributors: Johannes Schindelin | /people/dscho
---

{% include img src="k-listeria-animated" width=256 caption="Stack of Listeria Movement" %}

## Temporal-Color Code

Generates a temporal-color coded XY 2D image (above right) from HyperStack (above left). Works with both 2D time series and 3D time series.

Be sure to set the dimensional sizes (especially Z and T) properly with {% include bc path="Image|Properties" %}.

# Work Flow

With a hyperstack window activated (at the most front among other images), select {% include bc path="Image|Hyperstacks|Temporal-Color" %} Code.

In dialog window, select a LUT from drop down menu. Selected LUT will be used for color coding the time. You could also set the range of frames to be coded. Default is full frames. There is also an option check-box for generating color-scale bar in separate window. This will show correspondence between color and frame number in the color coded image.
