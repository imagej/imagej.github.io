---
mediawiki: Read_more_about_MSER_parameters
title: Read more about MSER parameters
---

## MSER parameters

The default algorithm to identify the seeds as objects is called Maximally Stable Extremal Regions (MSER) (Ref 1). In short, it computes all possible intensity thresholds of an image, which is called a component tree (e.g. it creates a 3d image from a 2d image). Subsequently MSER tries to identify "stable regions" in this space. Regions in the component tree are considered stable if an object has a certain size and preserves its shape over a given range of thresholds without merging with other objects.

MSER detected regions as shown as red ellipses. The line along which each of the Microtubules lie is assumed to be the semi-major axis of the MSER ellipse. Optimization using Gaussian line models is done in order to localize the end points of the seeds vertical extent of the box shows the grey-level life span of each component. The MSER is computed on an unsigned byte image where intensity levels are integers between 0-255 and several parameters can be adjust to find as many microtubules as possible:

-   Threshold difference defines the resolution of the component tree, i.e. every how many intensity values a threshold is computed. A low value should be used when low intensity objects are to be recognized. Increasing the parameter value will only allow higher intensity objects to be recognized.
-   Stability Score: is a threshold for the minimal stability of a region in the component space. For values close to 0 many regions will be deemed stable and for values close to 1 only very few extremely stable regions will be found.
-   Min \#of pixels: Minimum number of pixels contained in a region to be considered being stable.
