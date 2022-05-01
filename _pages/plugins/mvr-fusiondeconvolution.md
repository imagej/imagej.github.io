---
mediawiki: MVR-FusionDeconvolution
title: MVR-FusionDeconvolution
categories: [Uncategorized]
---

Firstly, it is not trivial to find the right bounding box for the fusion. By default (select "define manually") it will take the entire dataset, which might contain a lot of background space around your sample that you actually do not want to fuse. To make it right, you have several choices:

a\) Fuse manually first (maybe choose downsampling) pushing the min sliders all the way to the left and the max sliders all the way to the right. Then find in the fused image the min/max coordinates in x,y,z of the area you are interested in - this is called the **bounding box**. The coordinates are displayed in the ImageJ/Fiji status bar - they are corrected for the global coordinates asked for in the fusion dialog. *Important: Do not use the slice number in z as displayed in the image window, use the coordinates in the ImageJ/Fiji status bar.*

b\) Try "estimate automatically (experimental)". What it does is to fuse a down sampled version of the registered dataset. In that one it tries to remove beads using a minimal filter and threshold the object of interest. Around this one it makes the bounding box (min/max in x,y,z) itself. If you play with the parameters you might get it right for your sample.

c\) Use "automatically reorientate and estimate based on sample features". This is the best option, as it does not only find the bounding box automatically, but also reorients the sample so that the size of the bounding box becomes minimal. For that to work properly, you need to detect interest points in the sample itself (not beads around the sample) and ideally use them in a second registration step after matching the beads so that there are corresponding points within the sample. It will use those detections to find the bounding box and if you want, to re-orient the sample.

Once you have the right bounding box, you can either fuse or deconvolve your dataset, these are different strategies to combine all views (angles/illuminations) into one image volume. Deconvolution is pretty straight forward if you used beads, as the PSF can be extracted from the matched beads.
