---
mediawiki: Squassh
title: Squassh
categories: [Segmentation,Colocalization,Deconvolution]
---


{% capture maintainer%}
{% include person id='krzysg' %}
{% endcapture %}
{% include info-box software='ImageJ' name='Squassh' author=' [MOSAIC Group](http://mosaic.mpi-cbg.de/) , [Center for Systems Biology Dresden (CSBD)](http://www.mpg-sysbio.de) , [Max Planck Institute of Molecular Cell Biology and Genetics (MPI-CBG)](http://www.mpi-cbg.de/research/research-groups/ivo-sbalzarini.html) , Dresden, Germany.' maintainer=maintainer update-site='MOSAIC ToolSuite' source=' [MPI-CBG git](https://git.mpi-cbg.de/mosaic/MosaicSuite)' released='2014' status='active' category='Particle Analysis, Filtering, Colocalization, Deconvolution, Segmentation' website=' [MosaicSuite](http://mosaic.mpi-cbg.de/?q=downloads/imageJ)' %}

**Squassh** is a tool for 2D and 3D segmentation and quantification of subcellular shapes in fluorescence microscopy images. It provides globally optimal detection and segmentation of objects with constant internal intensity distribution, followed by object-based colocalization analysis. The segmentation computed by Region Competition can optionally correct for the PSF of the microscope, hence providing optimally deconvolved segmentations as described in Helmuth et al. (2009[^1]) and in Helmuth and Sbalzarini (2009[^2]). The tool was specifically developed to analyze image-based high-content screening data as described in the Squassh protocol. It is part of the [MosaicSuite](http://mosaic.mpi-cbg.de/?q=downloads/imageJ), which also offers 3D particle tracking, image segmentation, interaction analysis, and much more. The best way to install it is via the MOSAIC Fiji Update site, as described on the [MOSAIC web page](http://mosaic.mpi-cbg.de/?q=downloads/imageJ). The algorithm is described in Paul, Cardinale, and Sbalzarini (2013[^3]). The Squassh protocol and the use of the plugin are described in Rizk et al. (2014[^4]).

Documentation is available as [pdf](http://mosaic.mpi-cbg.de/downloads/SplitBregmanSeg.pdf).

## References

[^1]: J. A. Helmuth, C. J. Burckhardt, U. F. Greber, and I. F. Sbalzarini. [Shape reconstruction of subcellular structures from live cell fluorescence microscopy images](http://dx.doi.org/10.1016/j.jsb.2009.03.017), Journal of Structural Biology, 167:1–10, 2009

[^2]: J. A. Helmuth and I. F. Sbalzarini. [Deconvolving active contours for fluorescence microscopy images](http://mosaic.mpi-cbg.de/docs/Helmuth2009a.pdf), In Proc. Intl. Symp. Visual Computing (ISVC), volume 5875 of Lecture Notes in Computer Science, pages 544–553, Las Vegas, USA, November 2009. Springer.

[^3]: G. Paul, J. Cardinale, and I. F. Sbalzarini. [Coupling image restoration and segmentation: A generalized linear model/Bregman perspective](http://dx.doi.org/10.1007/s11263-013-0615-2), Int. J. Comput. Vis., 104(1): 69-93, 2013

[^4]: A. Rizk, G. Paul, P. Incardona, M. Bugarski, M. Mansouri, A. Niemann, U. Ziegler, P. Berger, and I. F. Sbalzarini. [Segmentation and quantification of subcellular structures in fluorescence microscopy images using Squassh](http://dx.doi.org/doi:10.1038/nprot.2014.037) Nature Protocols., 9(3): 586-596, 2014
