---
mediawiki: Statistical_Region_Merging
title: Statistical Region Merging
project: /software/fiji
categories: [Tutorials,Segmentation]
artifact: sc.fiji:Statistical_Region_Merging
doi: 10.1109/TPAMI.2004.110
---

Statistical Region Merging[^1] is a fast and robust algorithm to segment an image into regions of similar intensity or color.

The idea is to start with one region per pixel and then applying a statistical test on neighboring regions (in ascending order of intensity differences) whether the mean intensities are sufficiently similar enough to be merged.

## Tutorial

For the moment, the plugin handles only grayscale images:

![](/media/plugins/statistical-region-merging-boats.jpg)

It asks for a value for *Q*, which is a rough estimate of the number of regions in the image. You can also choose whether you want the regions to be marked by the mean gray value, or by the index of the region:

![](/media/plugins/statistical-region-merging-dialog.jpg)

This is a result for a low value of *Q*:

![](/media/plugins/statistical-region-merging-result.jpg)

## References

{% include citation fn=1 %}
