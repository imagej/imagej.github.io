---
title: Fiji Z-Spacing Correction
categories: [TrakEM2,Transform]
artifact: sc.fiji:z_spacing
doi: 10.1109/ISBI.2015.7163922
---

Estimate the positions and spacing between sections (or at local points) of three dimensional image data. This method may be applied to any imaging modality that acquires 3-dimensional data as a stack of 2-dimensional sections. We provide plugins for both [Fiji](/software/fiji) and [TrakEM2](/plugins/trakem2).

## Citation

Please note that the z-spacing correction plugin available through Fiji, is based on a publication. If you use it successfully for your research please cite our work:

{% include citation %}

## Introduction

Serial section microscopy, using either optical or physical sectioning, is an established method for volumetric anatomy reconstruction. Section series imaged with Electron Microscopy are currently vital for the reconstruction of the synaptic connectivity of entire animal brains such as that of *Drosophila melanogaster*. The process of removing ultrathin layers from a solid block containing the specimen, however, is a fragile procedure and has limited precision with respect to section thickness. Optical sectioning techniques often suffer from increasing distortion as sections deeper inside the tissue are imaged. On summary, section thickness that is supposed to be constant, in practice is not and has to be corrected where precise measurement is desired. We have developed a method to estimate the relative *z*-position of each individual section as a function of signal change across the section series. The Fiji plugin {% include bc path="Transform | Z-Spacing Correction" %} and the [TrakEM2](/plugins/trakem2) plugin {% include bc path="Plugins | LayerZPosition" %} implement this method.

## Parameters

* **Neighborhood range:** Specifies the neighborhood around each section for which pairwise similarities are calculated.

* **Outer iterations:** Specifies the number of iterations in the outer loop of the optimizer.

* **Outer regularization:** Specifies the amount of regularization in the outer loop of the optimizer. 0 means no regularization, 1 means full regularization (no change). The regularizer in the outer loop damps the updates during each iteration by the specified fraction.

* **Inner Iterations:** Specifies the number of iterations in inner loops of the optimizer.

* **Inner Regularization:** Specifies the amount of regularization in the outer loop of the optimizer. 0 means no regularization, 1 means full regularization (no change). The per-section quality weight requires regularization to avoid trivial solutions. We use a Tikhonov regularizer towards 1.0 weight.

* **Allow reordering:** Specifies whether layers/ sections can change their relative order in the series.
