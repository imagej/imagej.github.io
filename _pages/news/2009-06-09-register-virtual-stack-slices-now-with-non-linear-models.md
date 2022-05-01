---
title: 2009-06-09 - Register Virtual Stack Slices now with non-linear models
---

### Register Virtual Stack Slices now with non-linear models

The plugin [Register Virtual Stack Slices](/plugins/register-virtual-stack-slices) has been updated to work with the new generic image transformation library by {% include person id='axtimwalde' %} and with [bUnwarpJ](http://biocomp.cnb.uam.es/~iarganda/bUnwarpJ/) by Ignacio Arganda. As a result, stack slices may be now registered using:

-   Translation model
-   Rigid model: rotation and translation
-   Similarity model: rotation, translation and isometric scaling
-   Affine model
-   Elastic model: with splines, interfacing with bUnwarpJ
-   Moving Least Squares model: allows maximal local deformation.


