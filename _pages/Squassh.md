{{Infobox
| software               = ImageJ
| name                   = Squassh
| author                 = [http://mosaic.mpi-cbg.de/ MOSAIC Group], [http://www.mpg-sysbio.de Center for Systems Biology Dresden (CSBD)], [http://www.mpi-cbg.de/research/research-groups/ivo-sbalzarini.html Max Planck Institute of Molecular Cell Biology and Genetics (MPI-CBG)], Dresden, Germany.
| maintainer     = {{Person|Krzysztof.Gonciarz}}
| update site = MOSAIC ToolSuite
| source                 = [https://git.mpi-cbg.de/mosaic/MosaicSuite MPI-CBG git]
| released               = 2014
| status                 = active
| category               = [[:Category:Particle analysis|Particle analysis]], [[:Category:Filtering|Filtering]], [[:Category:Colocalization|Colocalization]], [[:Category:Deconvolution|Deconvolution]], [[:Category:Segmentation|Segmentation]]
| website                = [http://mosaic.mpi-cbg.de/?q=downloads/imageJ MosaicSuite]
}}

'''Squassh''' is a tool for 2D and 3D segmentation and quantification of subcellular shapes in fluorescence microscopy images. It provides globally optimal detection and segmentation of objects with constant internal intensity distribution, followed by object-based colocalization analysis. The segmentation computed by Region Competition can optionally correct for the PSF of the microscope, hence providing optimally deconvolved segmentations as described in Helmuth et al. (2009<ref>J. A. Helmuth, C. J. Burckhardt, U. F. Greber, and I. F. Sbalzarini. [http://dx.doi.org/10.1016/j.jsb.2009.03.017 Shape reconstruction of subcellular structures from live cell fluorescence microscopy images], Journal of Structural Biology, 167:1–10, 2009</ref>) and in Helmuth and Sbalzarini (2009<ref>J. A. Helmuth and I. F. Sbalzarini. [http://mosaic.mpi-cbg.de/docs/Helmuth2009a.pdf Deconvolving active contours for fluorescence microscopy images], In Proc. Intl. Symp. Visual Computing (ISVC), volume 5875 of Lecture Notes in Computer Science, pages 544–553, Las Vegas, USA, November 2009. Springer.</ref>). The tool was specifically developed to analyze image-based high-content screening data as described in the Squassh protocol. It is part of the [http://mosaic.mpi-cbg.de/?q=downloads/imageJ MosaicSuite], which also offers 3D particle tracking, image segmentation, interaction analysis, and much more. The best way to install it is via the MOSAIC Fiji Update site, as described on the [http://mosaic.mpi-cbg.de/?q=downloads/imageJ MOSAIC web page].
The algorithm is described in Paul, Cardinale, and Sbalzarini (2013<ref>G. Paul, J. Cardinale, and I. F. Sbalzarini. [http://dx.doi.org/10.1007/s11263-013-0615-2 Coupling image restoration and segmentation: A generalized linear model/Bregman perspective], Int. J. Comput. Vis., 104(1): 69-93, 2013</ref>).
The Squassh protocol and the use of the plugin are described in Rizk et al. (2014<ref>A. Rizk, G. Paul, P. Incardona, M. Bugarski, M. Mansouri, A. Niemann, U. Ziegler, P. Berger, and I. F. Sbalzarini. [http://dx.doi.org/doi:10.1038/nprot.2014.037 Segmentation and quantification of subcellular structures in fluorescence microscopy images using Squassh] Nature Protocols., 9(3): 586-596, 2014</ref>).

Documentation is available as [http://mosaic.mpi-cbg.de/Downloads/SplitBregmanSeg.pdf pdf].

== References ==
G. Paul, J. Cardinale, and I. F. Sbalzarini. Coupling image restoration and segmentation: A generalized linear model/Bregman perspective. Int. J. Comput. Vis., 104(1):69–93, 2013. 

A. Rizk, G. Paul, P. Incardona, M. Bugarski, M. Mansouri, A. Niemann, U. Ziegler, P. Berger, and I. F. Sbalzarini. Segmentation and quantification of subcellular structures in fluorescence microscopy images using Squassh. Nature Protocols, 9(3):586–596, 2014. 
<references />

[[Category:Plugins]]
[[Category:Segmentation]]
[[Category:Colocalization]]
[[Category:Deconvolution]]
