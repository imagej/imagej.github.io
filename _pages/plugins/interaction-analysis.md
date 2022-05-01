---
mediawiki: Interaction_Analysis
title: Interaction Analysis
categories: [Particle Analysis,Colocalization]
---


{% capture maintainer%}
{% include person id='krzysg' %}
{% endcapture %}
{% include info-box software='ImageJ' name='MosaicIA - Interaction Analysis' author=' [MOSAIC Group](http://mosaic.mpi-cbg.de/) , [Center for Systems Biology Dresden (CSBD)](http://www.mpg-sysbio.de) , [Max Planck Institute of Molecular Cell Biology and Genetics (MPI-CBG)](http://www.mpi-cbg.de/research/research-groups/ivo-sbalzarini.html) , Dresden, Germany.' maintainer=maintainer update-site='MOSAIC ToolSuite' source=' [MPI-CBG git](https://git.mpi-cbg.de/mosaic/MosaicSuite)' released='2013' status='active' category='Particle Analysis, Colocalization' website=' [MosaicSuite](http://mosaic.mpi-cbg.de/?q=downloads/imageJ)' %}

**Interaction Analysis** is a tool to analyze the spatial distribution of objects in images. It estimates from an observed particle or object distribution what hypothetical interaction between the objects is most likely to have created this distribution. Detection of the objects (particles) can also be directly done in the plugin. It is part of the [MOSAICsuite](http://mosaic.mpi-cbg.de/?q=downloads/imageJ), which also offers 3D particle tracking, image segmentation, colocalization analysis, and much more. The best way to install it is via the MOSAIC Fiji Update site, as described on the [MOSAIC web page](http://mosaic.mpi-cbg.de/?q=downloads/imageJ). The algorithm is described in Helmuth, Paul, and Sbalzarini (2010[^1]). The tool and its use are described in Shivanandan, Radenovic, and Sbalzarini (2013[^2]).

Documentation is available as [pdf](http://mosaic.mpi-cbg.de/downloads/IAPManual.pdf)

## References

[^1]: J. A. Helmuth, G. Paul, and I. F. Sbalzarini. [Beyond co-localization: inferring spatial interactions between sub-cellular structures from microscopy images](http://dx.doi.org/10.1186/1471-2105-14-349), BMC Bioinformatics., 11:372, 2010

[^2]: A. Shivanandan, A. Radenovic, and I. F. Sbalzarini. [MosaicIA: an ImageJ/Fiji plugin for spatial pattern and interaction analysis](http://dx.doi.org/10.1186/1471-2105-11-372), BMC Bioinformatics., 14:349, 2013
