{{ComponentStats:sc.fiji:Skeletonize3D_}}2D and 3D skeletonization of binary images.

{|
|style="vertical-align:top" |[[Image:Smoothed-bat-cochlea-volume.gif|thumb|Smoothed bat cochlea volume]]
|style="vertical-align:top" |[[Image:Skeleton-bat-cochlea-volume.gif|thumb|3D skeleton from bat cochlea volume]]
|}

== General Description ==
Skeletonize3D is a Fiji and ImageJ plugin that performs the [[wikipedia:Topological skeleton|skeletonization]] of 2D and 3D binary images (8-bit images). In Fiji, you can find it under {{bc | Plugins | Skeleton | Skeletonize (2D/3D)}}. If you need to analyze a 2D/3D skeleton image, you may be interested on having a look at [[AnalyzeSkeleton]].

== Video tutorial ==
For a fast introduction to [[Skeletonize3D]] and [[AnalyzeSkeleton]] and an example of a real application, you can have a look at this [[Skeleton analysis video tutorial | video tutorial]].

The tutorial describes step by step how to:

* Pre-process a 3D image to extract the relevant morphological information by
** removing the noise 
** and binarizing
* Extract the skeleton of a binary image with [[Skeletonize3D]]
* Analyze the resulting skeletons in the 3D image with [[AnalyzeSkeleton]]

== Related work ==
This work is an implementation by Ignacio Arganda-Carreras of the '''3D thinning algorithm''' from Lee et al. [http://portal.acm.org/citation.cfm?id=202862.202867 ''"Building skeleton models via 3-D medial surface/axis thinning algorithms. Computer Vision, Graphics, and Image Processing, 56(6):462–478, 1994."''] Based on the ITK version from Hanno Homann: [http://hdl.handle.net/1926/1292 http://hdl.handle.net/1926/1292]
It works with 8-bit images and stacks. It expects the images to be binary. If not, all pixel values above 0 will be considered white. The resulting skeleton image will have '''pixel value 255 at the skeleton and 0 at the background''' (black) pixels.

As Hanno Homman explains in his paper, […] ''binary thinning is used for finding the centerlines (”skeleton”) of objects in the input image. The general idea is to erode the object’s surface iteratively until only the skeleton remains. Erosion has to be performed symmetrically in order to the guarantee medial position of the skeleton lines and such that the connectedness of the object is preserved. Care has to be taken in order not to create holes or cavities in the object.''

''There are two major approaches to image thinning: a) kernel-based filters and b) decision trees. Kernel-based filters apply a structuring element to the image and can generally be extended to dimensions higher than 3D, to find computationally efficient solutions for 4D and higher dimensions is subject of ongoing research. Methods based on decision trees are thus far limited to 2D and 3D, but are potentially faster than morphological filters, if they are well designed and can find more deletable points at each iteration.''

''In 3D there are 2²⁶ = 67,108,864 possible binary combinations of object and background voxels in a 26-neighborhood, which cannot be completely captured by kernel-based filters. Lee et al. have demonstrated in their work that their solution, based on a decision tree, can handle all these cases correctly and find all deletable surface points at each iteration. Thus their algorithm allows for a very fast iterative erosion process'' […].

== Changelog ==
'''2008/11/19''': Update: changed skeleton pixel values to 255.

'''2008/11/15''': First release.

== License ==
This program is '''free software'''; you can redistribute it and/or modify it under the terms of the '''GNU General Public License''' as published by the Free Software Foundation ([http://www.gnu.org/licenses/gpl.txt http://www.gnu.org/licenses/gpl.txt]).

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.  

== See also ==
* [http://imagejdocu.tudor.lu/doku.php?id=plugin:morphology:skeletonize3d:start Skeletonize3D at ImageJ documentation wiki]

----

[[Category:Plugins]]
[[Category:Skeleton]]
