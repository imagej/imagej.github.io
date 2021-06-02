---
mediawiki: FlowJ
title: FlowJ
description: Core optic flow algorithms for 2D images.
section: 
categories: [Optic Flow]
artifact: sc.fiji:FlowJ_
---

FlowJ is a plugin that implements the main gradient-based optical flow techniques, such as Lucas and Kanade, Uras, Fleet and Jepson and Singh algorithms.
It is authored by Dr. Michael D. Abramoff, as part of his tool collection, the Bio-medical Imaging in Java.
Since the end of 2020, the original website of the collection is offline. 
This page therefore contains a copy of its content prior to removal. 
All credits for it should go to Dr. Abramoff.

## Documentation

FlowJ - Optical Flow in Java
FlowJ is part of BIJ and the Bio-medical Imaging in Java site.
Version 1.29: Faster rendering.

This page is a companion to:
IEEE Transactions in Medical Imaging , M.D. Abràmoff, W.J. Niessen and M.A. Viergever: [Objective Quantification of the Motion of Soft Tissues.](https://ieeexplore.ieee.org/document/887614) IEEE TMI. 2000;  19 (10): 986-995.

### Description

FlowJ is a collection of popular 2D optical flow algorithms, Lucas and Kanade, Uras, Fleet and Jepson, and Singh, in Java. It has been interfaced to ImageJ, the Java  image processing program developed by Wayne Rasband at the National Institutes of Health. If properly installed, FlowJ appears as an extra command in ImageJ under the Plugins menu. It can measure and visualize the image flow (related to motion) in any open stack such as new_square2.tif to the right. The test image sequence is available at ftp.csd.uwo.ca/pub/vision).

The images under it show the flow field in different formats. 
Formats available in FlowJ include the DC format (a pseudocolor format developed by myself), the common quiver (also called arrow) format (detail only because it requires enlargement) and spotnoise (a thermal flow rendering format developed by J.J. van Wijk). 
The flow field is always shown as a grayscale (float) stack with separated x and y flows.

### Features

- Lucas and Kanade, Uras, Fleet and Jepson and Singh algorithms.
- Choice of 4 point central difference, Gaussian derivative and Sobel gradient estimation.
- Choice of Dynamic color, Quiver and Spotnoise flow field mappings, which show individual flow vectors and regions. Also puts flow fields into stacks with slices for flow in the x- and in the y-direction for convenient quantitative analysis.
- Reads and writes the common Burkitt format optical flow files (as in the Barron et al. paper).
- Most parameters accessible.
- Extensive angular error estimation, so that estimated flow can be compared to true flow field.
- Sources available

### Usage.

You can run the plugin from the following menu location: _Plugins > BIJ > FlowJ_. 

A dialog will open with the following options:

![FlowJ dialog](/media/plugins/FlowJ_dialog.png)


####  Buttons:

- `Compute flow field` - starts the computation of optical flow for the slice set in Frame, using the Algorithm. The flow field will be displayed in DC format at scale = 1.
- `Display` - redisplays the flow field in a separate window. The size of the window is determined by Scale, and the visualization format by Mapping type.
- `Open flow field` - opens an existing flow field in the Burkitt format.
- `Save flow field` - saves a flow field in the Burkitt format
- `Error vs. file` - loads a true flow field (in Burkitt format), and computes the angular error as defined in the Barron et al. paper.
- `Errors to clipboard` - copies angular error data including deviations to the clipboard
- `Copy central frame` - shows the stack slice for which the flow was computed.
- `Graph` - opens a window that shows a graph of measured versus true flow. A true flow field needs to be loaded for this to work.

#### Parameters:

- `Frame` - sets the slice for which the flow is computed. The frame is set to the central slice in the stack by default.
- `Mapping type` - selects the visualization algorithm used by Display
- `Rho` - sets the flow magnitude (in pixels/frame) at which color mappings (DC)  saturate.
- `Scaling` - sets the enlargement for Display. Bilinear interpolation.
- `Algorithm` - sets the estimation algorithm
- `Tau` - sets the thresholds for Lucas-Kanade and Uras algorithms
- `Gradient method` - sets how the gradient is computed. You can choose central difference, Gaussian (usually the best results) and nearest neighborhood (fastest and smallest support)
- `Sigma S / T` - Spatial and temporal scale at which the estimates are computed. These are dimensionless and set the standard deviation for the probability function associated with the Gaussian kernel
- `Regularization` for Uras only, sets the scale in pixels at which the flow vectors are regularized.
- `Sigma W` for the Lucas-Kanade algorithm: the scale of the local region W in which flow vectors are constrained to be regular.

The parameters refer to the differing algorithms (LK = Lucas and Kanade, U = Uras, FJ = Fleet and Jepson, S = Singh). The parameters not mentioned above are very specific to each algorithm. The best explanation for these is found in my TMI or the Barron _et al_. paper:

Barron, J.L., Fleet, D.J. & Beauchemin, S.S. [Performance of optical flow techniques](https://doi.org/10.1007/BF01420984). Int J Comput Vision 12, 43–77 (1994). 

- Recently discovered the Carnegie Mellon University image database with many good motion sequences, available at http://vasc.ri.cmu.edu/idb/html/motion/index.html

### References.

- Barron, J. L., Fleet D.J., and Beauchemin S.S., "Performance of Optical Flow Techniques," Int J Comp Vis, vol. 12, no. 1, pp. 43-77, 1994. **The best reference overall.**
- Niessen, W. J., Duncan, J. S., Nielsen, M., Florack, L. M. J., and ter Haar Romeny, B. M., "A Multiscale Approach to Image Sequence Analysis," Comp Vis Imag Understand, vol. 65, no. 2, pp. 259-268, 1997.
- Lucas, B. and Kanade T., " An Iterative Image Registration Technique with an Application to Stereo Vision", in Proc. DARPA Image Understanding Workshop, 1981.
- Fleet, D. J. and Jepson, A. D., "Hierarchical Construction of Orientation and Velocity Selective Filters," IEEE Trans Patt Anal Mach Intell, vol. 11, no. 3, pp. 315-325, 1989.
- Fleet, D. J. and Jepson, A. D., "Computation of Component Image Velocity From Local Phase Information," Int J Comp Vis, vol. 5, no. 1, pp. 77-104, 1990.
- Uras, S., Girosi, F., Verri, A., and Torre, V., "A Computational Approach to Motion Perception," Biol Cybern, vol. 60 pp. 79-87, 1988.
- Singh, A., " An estimation-theoretic framework for image-flow computation", in Proc. 3rd Intern. Conf Comput Vis., 1990.
- M.D. Abràmoff, W.J. Niessen and M.A. Viergever: Objective Quantification of the Motion of Soft Tissues. IEEE TMI. 2000;  19 (10): 986-995.
- Wijk, J.J. van. Spot noise - Texture Synthesis for Data Visualization.
- Computer Graphics, 25(4), (Proceedings SIGGRAPH'91), 1991, 309-318.

If you have ftp, look at ftp.csd.uwo.ca/pub/vision (anonymous login with your password)  to find the C-sources for all optical flow algorithms that accompanied the Barron et al. article and that were a major source of inspiration for me. You can also find example image sequences to test with there.

## ChangeLog

Since FlowJ is maintained inside Fiji, the following changes have been made:

-   When you compute all flow fields and then display them, the "Display static background" box is now properly handled (noticed by Christina Eugster).
-   There is a "Display magnitude" button now to get the magnitudes of the flow vectors (i.e. the local "speed" in pixels per frame).

## Menu path

{% include bc path='Plugins | BIJ | FlowJ'%}

