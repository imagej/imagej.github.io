---
mediawiki: Region_Competition
title: Region Competition
categories: [Segmentation,Deconvolution]
---


{% capture maintainer%}
{% include person id='krzysg' %}
{% endcapture %}
{% include info-box software='ImageJ' name='Region Competition' author=' [MOSAIC Group](http://mosaic.mpi-cbg.de/) , [Center for Systems Biology Dresden (CSBD)](http://www.mpg-sysbio.de) , [Max Planck Institute of Molecular Cell Biology and Genetics (MPI-CBG)](http://www.mpi-cbg.de/research/research-groups/ivo-sbalzarini.html) , Dresden, Germany.' maintainer=maintainer update-site='MOSAIC ToolSuite' source=' [MPI-CBG git](https://git.mpi-cbg.de/mosaic/MosaicSuite)' released='2013' status='active' category='Segmentation, Deconvolution' website=' [MosaicSuite](http://mosaic.mpi-cbg.de/?q=downloads/imageJ)' %}

**Region Competition** is a 2D and 3D multi-region image segmentation tool. It can segment arbitrary (and not priorly known) numbers of objects in fluorescence microscopy images. The objects can have either constant or varying internal intensity. The segmentation computed by Region Competition can optionally correct for the PSF of the microscope, hence providing deconvolved segmentations as described in Helmuth et al. (2009[^1]) and in Helmuth and Sbalzarini (2009[^2]). Region Competition is part of the [MosaicSuite](http://mosaic.mpi-cbg.de/?q=downloads/imageJ), which also offers 3D particle tracking, co-localization analysis, interaction analysis, and much more. The best way to install it is via the MOSAIC Fiji Update site, as described on the [MOSAIC web page](http://mosaic.mpi-cbg.de/?q=downloads/imageJ). The algorithm is described in Cardinale, Paul, and Sbalzarini (2012[^3]).

Documentation is available as [html](http://mosaic.mpi-cbg.de/MosaicToolboxSuite/Region_Competition.html).

## References

[^1] J. A. Helmuth, C. J. Burckhardt, U. F. Greber, and I. F. Sbalzarini. [Shape reconstruction of subcellular structures from live cell fluorescence microscopy images](http://dx.doi.org/10.1016/j.jsb.2009.03.017), Journal of Structural Biology, 167:1–10, 2009

[^2] J. A. Helmuth and I. F. Sbalzarini. [Deconvolving active contours for fluorescence microscopy images](http://mosaic.mpi-cbg.de/docs/Helmuth2009a.pdf), In Proc. Intl. Symp. Visual Computing (ISVC), volume 5875 of Lecture Notes in Computer Science, pages 544–553, Las Vegas, USA, November 2009. Springer.

[^3] J. Cardinale, G. Paul, and I. F. Sbalzarini. [Discrete region competition for unknown numbers of connected regions](http://dx.doi.org/10.1109/TIP.2012.2192129), IEEE Trans. Image Process., 21(8): 3531–3545, 2012
