---
mediawiki: Xlib
title: Xlib
categories: [Analysis,Filtering,MATLAB,Particle Analysis,Segmentation,Skeleton]

name: Xlib
team-founders: Beat Münch
team-leads: Beat Münch
team-maintainers: Beat Münch
release-date: 06-December-2021
support-status: maintained actively as of December 2021
---

{% include info-box software='ImageJ' name='Xlib' author='Beat Münch' maintainer='Beat Münch' source='[https://drive.switch.ch/index.php/s/WOVSIPMky2JsXsp](https://drive.switch.ch/index.php/s/WOVSIPMky2JsXsp)' released='1 June 2015' latest-version='6 December 2021' status='stable' category='Any' %}

## Overview of 'Xlib'

A set of prospective ImageJ plugins is maintained by the group for 3D-Microscopy, Analysis and Modeling of the Laboratory for Concrete and Construction Chemistry at Empa Dübendorf, Switzerland. The plugins include automated imaging tools for filtering, data reconstruction, quantitative data evaluation and data import, as well as tools for interactive segmentation, visualization and management of image data.

Since the research focus of our group is on 3D imaging, all of our plugins are able to deal with either 2D or 3D image data. 3D image data is always represented by image stacks. 3D processing may include slice-wise 2D processing of all images in the stack or, sometimes more important, true 3D processing.

Each one of the new plugins includes a help button where basic remarks about the functionality and a description of the parameters is provided. This feature does not correspond with the ImageJ philosophy assuming the help documentation to be available on the internet only. However, we consider the help button as a handy feature.

The user might be surprised to realize that some of the tools are apparently already existing in other plugins of ImageJ or Fiji. Those tools are for instance ["FFT 2D 3D"](#fft-2d-3d), ["Image Calculator"](#image-calculator), ["Distance Transform"](#distance-transform), ["Transform 2D 3D"](#transform-2d-3d) and others. The reason for this apparent redundancy is that the original tools incorporate major restrictions which are elimintated in the new plugins. Each one of the available tools and its advantage is shortly being presented below.

The following plugins are included:

**Data Analysis:**

-   ["Closest Cluster"](#closest-cluster): Engine for finding the closest candidate to a list of chemical substances
-   ["Import DMP"](#import-dmp): Import elementary image data from ".dmp" files (e.g. originating from [MATLAB](/scripting/matlab))

**Filtering:**

-   ["Anisotropic Diffusion"](#anisotropic-diffusion): Anisotropic diffusion
-   ["Canny Edge"](#canny-edge): Canny edge detection
-   ["Cluster Image"](#cluster-image): Clustering of images
-   ["Disconnect Particles"](#disconnect-particles): Particle disconnection
-   ["Distance Transform"](#distance-transform): Distance transform
-   ["FFT 2D 3D"](#fft-2d-3d): Fast Fourier transform of arbitrary sized images
-   ["Image Calculator"](#image-calculator): Utterly generalized image calculator
-   ["Labeling 2D 3D"](#labeling-2d-3d): Labeling of disconnected binary mask objects
-   ["Median 2D 3D"](#median-2d-3d): Conventional and multidimensional median filtering
-   ["Remove Background"](#remove-background): Remove background from image by polynomial approximation
-   ["Roundness 2D 3D"](#roundness-2d-3d): Roundness filter
-   ["Skeletonization 2D 3D"](#skeletonization-2d-3d): Skeletonization of binary masks
-   ["Stripe Filter"](#stripe-filter): Removal of horizontal and vertical stripes
-   ["Transform 2D 3D"](#transform-2d-3d): Generalized image transforms
-   ["Wavelets 2D"](#wavelets-2d): Wavelet decomposition and reconstruction

**Reconstruction:**

-   ["Filtered Backprojection"](#filtered-backprojection): Filtered backprojection of projections
-   ["Projections Sinograms"](#projections-sinograms): Conversion of sets of projections into sinograms and vice versa
-   ["Reconstruct 3D from 2D"](#reconstruct-3d-from-2d): Reconstruct virtual 3D structures from given 2D structures

**Evaluation:**

-   ["Particle Size Distribution"](#particle-size-distribution): Calculate particle size distribution of binary particle structures
-   ["Phase Image Evaluation"](#phase-image-evaluation): Evaluate images consisting of a number of homogeneous phases
-   ["Pore Size Distribution"](#pore-size-distribution): Calculate pore size distribution of binary pore structures

**Editors and Viewers:**

-   ["Display Volume"](#display-volume): Interactively visualize 3D volume by an orthogonal slicer
-   ["Edit Label Region"](#edit-label-region): Engine for interactive editing of labeled binary 2D or 3D particle structures
-   ["Segment Phases 3D"](#segment-phases-3d): Engine for basic interactive segmentation of images and volumes
-   ["View 3D Mask"](#view-3d-mask): Rendering of 3D image masks

## Data Analysis

Plugins of this section offer importing, handling or analysis of special data formats that are unknown to ImageJ, but interesting for special purposes.

### Closest Cluster

This plugin provides an engine for finding the most probable chemical compositions of some given energy dispersive spectroscopy (EDS) data. From a set of proposed chemical formula, a ranking of the probability of matching with the candidate EDS data is calculated.

A step by step tutorial for the clustering and phase identification of EDS maps is provided in the manual entitled ["Instructions for the Phase Clustering and Identification Using the Plugins for ImageJ"](/media/plugins/xclusteringphaseidentification.pdf).

The program can be used in combination with the ["Cluster Image"](#cluster-image) plugin. Thereby for a resulting set of cluster centers, the program provides the most probable cluster membership.

{% include citation doi='10.1111/jmi.12309' %}

### Import DMP

DMP is a simple data format for the storage of 2D images. It is used at IBT from the ETH and University of Zürich. The first two short integer entries of the data file are reserved for providing the width and the heigth of the image. The next short integer is reserved. Thereafter (i.e. after the first 6 bytes) follows the image data itself, each pixel given by a 32-bit floating number.

A short [MATLAB](/scripting/matlab) code for writing such an image variable "image" with the size "width" and "heigth" is given below:

```java
fid=fopen(file,'w');
fwrite(fid,size(image,2),'uint16');
fwrite(fid,size(image,1),'uint16');
fwrite(fid,0,'uint16');
fwrite(fid,image','float32');
fclose(fid);
```

Reading the a DMP image with [MATLAB](/scripting/matlab) can be achieved like this:

```java
fid=fopen(filename);
dim=fread(fid,3,'uint16');
width=dim(1);
height=dim(2);
data=zeros(height,width);
for ii=1:height
    data(:,ii)=fread(fid,width,'float32');
end
fclose(fid);
```

## Filtering

The filtering functions accept one or more images or stacks of images where some filtering techniques are applied to. Generally, the following filtering functions work on 2D images, slice-wise 2D, as well as in true 3D mode if it is applied to image stacks.

### Anisotropic Diffusion

{% include img align="left" name="spiral left" src="/media/plugins/xfig6-1.jpg" caption="CT slice after strong alcali aggregate reactions (top) and edge preserving / smoothing filtering with a 4x4 median (bottom left) and anisotropic diffusion (bottom right)." %} The mechanism of heat diffusion has been used as the basics for image filtering. Thereby, the image values are understood as temperature values and image blurring represents the process of heat transport blurring. The key idea is the introduction of anisotropy, i.e. of diffusion characteristics that are depending on the pixel environment and the transfer direction. The local anisotropy is assigned according to the direction and magnitude of the image gradient, introducing high diffusion rates at low gradients and low diffusion rates at high gradients. Hence, the anisotropic diffusion characteristics are defined according to an ellipse in 2D or an ellipsoid in 3D perpendicular to the gradient vector.

The corresponding partial differential equation had first been numerically approached in 1990 by a fast algorithm of Perona and Malik [Perona1990] by defining the elliptic diffusion shapes by means of simple box filtering. Way better results can be obtained with the technique of Tschumperlé and Deriche [Tschmperlé2005] from 2005 by setting the tensor field according to the Eigenvalues and Eigenvectors in order to drive the diffusion. As expected, this approach is however more time consuming.

The filter is a brilliant edge preserving / smoothing filter for intelligent noise reduction. In particular, the implementation of Tschumperlé and Deriche outperforms other approaches in respect of the distinction between coherent edges and noise. The figure above shows a comparison between anisotropic diffusion (bottom right) and median filtering (bottom left) of a CT slice from concrete after strong alcali aggregate reactions (top). Anisotropic diffusion filtering is outstanding by better preserving the cracks while flattening inhomogeneities due to noise (please note center regions).

The filter works in 2D as well as in 3D.

-   {% include citation doi='10.1109/34.56205' %}

-   {% include citation doi='10.1109/TPAMI.2005.87' %}

### Canny Edge

{% include thumbnail align="right" src='/media/plugins/xfig6-2.jpg' title='Valve image (left) and the results from the Canny filter. Top: original image, 2nd row: magnitudes of gradient vectors, angles of gradient vectors, 3rd row: magnitudes after non-maxima suppression, and the connected regions after double thresholding the maximal magnitudes.' %} In 1986, J. Canny has proposed an excellent edge detection filter [Canny1986] that due to its performance became famous. The filter is based on a fast numeric approach for the calculation of the direction-dependent first derivative, i.e. the gradient vector function of an image. The Canny filter is well known for 2D imaging, yet it is barely supported in 3D. This plugin supports both, the 2D and the 3D implementation. It additionally supports preceding Gauss filtering, optional non-maxima suppression for the extraction of the edges, as well as a function for double thresholding and joining the connected regions. Double thresholding means that an upper threshold is used for extracting the relevant edges, while a lower threshold is provided for adding residing connections between the extracted edges. The plugin returns the magnitudes and the angles of the gradient vector functions.

The results of a Canny filtered image of a valve image is shown in the upper figure (top: original image). The gradient magnitude and angles are presented (2nd row), as well as the magnitudes after non-maxima suppression and also after joining the connected regions (3rd row).

-   {% include citation doi='10.1109/TPAMI.1986.4767851' %}

### Cluster Image

{% include thumbnail src='/media/plugins/xfig6-3-1.jpg' title='Image acquired by BSE and EDX maps at the same local position showing the amounts of Ca, C (1st row), Al, Cl, Fe, K (2nd row), Mg, Mn, Na, O (3rd row), P, Si, S, Ti (4th row).'%} Cluster analysis is a technique of statistical data analysis for grouping sets of objects. It is used in machine learning, data mining, pattern recognition, information retrieval, bio-informatics and can also be applied to image analysis. Different clustering definitions and algorithms have been proposed using connectivity, distance to the cluster center, statistical distribution, or density rates as optimization parameters for building clusters.

In image analysis, mainly two algorithms are prominent: the k-means algorithm and the mean shift algorithm. They have been implemented together with a third one, fuzzy c-means clustering.

The k-means algorithm [Kanungo2002] minimizes the square sum of the distances of each data point to its assigned cluster center. It starts with a random association of the data points to an initially determined number of clusters. Using an iterative optimization procedure it converges quickly to stable data assignments to clusters. K-means clustering is popular because it is very fast.

The mean shift clustering method [Funkunaga1975] optimizes the cluster centers such that the data densities within the clusters which are maximized. Within kernels of a given size around each data point, the centeroid of all points inside of the kernel is determined and the sphere shifted accordingly. After iterative repetition of this process, the sphere remains stationary. The data point is then assigned to this final cluster center. The algorithm can be understood as like the walk to the closest peak in a mountain landscape. Within a certain perimeter, the highest target is being located and reached. From thereon, the next target within the same perimeter is located and reached again. This process is iteratively carried on until the top within the selected perimeter is reached. Depending on the perimeter size, different hills or sub-hills will be achieved. If the perimeter is larger than 400km, you will reach the Mont Blanc from anywhere in Switzerland. If it is larger than 20'000km, the Mount Everest will be reached from any point in the world. If its size is only a some meters, you will probably end up on the top of a building.

Fuzzy c-means clustering [Bezdek1984] allows a data point to be assigned to more than one clusters. The affiliation to a cluster is given by a membership value ranging from zero to one. The sum of all memberships for a data point is unity. Hence, the assignment of a data point to a class is not unequivocal but relative. The degree of belonging to a class is related inversely to the distance from the data point to the cluster. It also depends on a parameter that controls how much weight is given to the winning cluster. With fuzzy c-means, the centroid of a cluster is the mean of all points, weighted by their degree of belonging to the cluster. The finally winning class is the one with the highest ranking. The process of the fuzzy c-means algorithm is very similar to the k-means algorithm.

Expectation-maximization (EM) clustering [Dempster1977] iteratively finds the maximum likelyhood estimation of a Gaussian distribution fit of the original N-dimensional distribution of pixel values. The EM iteration alternates between performing an expectation (E) step, which creates a function for the expectation of the log-likelihood evaluated using the current estimate for the parameters, and a maximization (M) step, which computes parameters maximizing the expected log-likelihood found on the E step.

The plugin also allows clustering by using <img src="/media/plugins/xfig6-3-3.jpg" title="fig:xFig6-3-3.jpg" width="50" alt="xFig6-3-3.jpg" /> [ELKI](http://elki.dbs.ifi.lmu.de) (Environment for Developing KDD-Applications Supported by Index-Structures, developed by the [ELKI](http://elki.dbs.ifi.lmu.de) team [http://elki.dbs.ifi.lmu.de/wiki/Team](http://elki.dbs.ifi.lmu.de/wiki/Team)). [ELKI](http://elki.dbs.ifi.lmu.de) is an open source data mining software written in Java. In addition to multiple features, [ELKI](http://elki.dbs.ifi.lmu.de) offers various ways for clustering. An [ELKI](http://elki.dbs.ifi.lmu.de) wrapper for the clustering of images is included into the ["Image Clustering"](#image-clustering) plugin. As soon as the respective elki.jar bundle is copied to the "plugins" directory of the current ImageJ version, image clustering with [ELKI](http://elki.dbs.ifi.lmu.de) is possible. The required specification parameters for the [ELKI](http://elki.dbs.ifi.lmu.de) clustering algorithm together with its parameters (details see [ELKI](http://elki.dbs.ifi.lmu.de) documentation) can be defined by the user.

{% include thumbnail src='/media/plugins/xfig6-3-2.jpg' title='Results from clustering of the 15-dimensional image data space displayed in the figure above. First row: k-means for 2 (left), 3, 5 and 16 (right) clusters. Second row: mean shift for the seeking perimeters 100 (left), 70, 60 and 50 (right). Third row: fuzzy c-means clustering for 5 clusters at fuzziness 1.1 (left) and 4.0, 16 clusters at fuzziness 2.0, and its fuzziness membership values (right).'%} As an example, ESEM images of a natural cement analogue (Maqarin, Jordania) is provided in the figure to the upper right. A backscatter electron microscope (BSE) image (top left) and image maps acquired from energy-dispersive X-ray spectroscopy (EDX) at the same location forked into 14 different elements (see figure above) are used as the basis for clustering. Thus together with the BSE image, the clustering is achieved from a 15-dimensional vector space. In the figure below, some results from different clustering algorithms and parameter settings are displayed. The first row shows results from the k-means, the second one from the mean shift, and the third one from fuzzy c-means clustering. K-means clustering (1st row) requires the number of clusters as an input parameter. The results for 2 (left), 3, 5 and 16 (right) clusters are provided. Slightly different results provides mean shift clustering (2nd row) which requires the size of the seeking perimeter as input parameter. It is determined at 100 (left), 70, 60 and at 50 (right). Fuzzy c-means clustering (3rd row) requires the number of clusters and the fuzziness as input parameters. The results are displayed for 5 clusters at fuzziness 1.1 (left) and 4.0, for 16 clusters at fuzziness 2.0, as well as an image showing its fuzziness membership to the cluster with the highest respective ranking at each location (right).

Clustering can also be applied to one dimensional spaces (i.e. from a single gray level image), or for color images where the R, G, B color channels provide a 3-dimensional vector space. Clustering thus provides an elegant way for automatic segmentation of 2D images or 3D image volumes containing different phases.

-   {% include citation doi='10.1109/TPAMI.2002.1017616' %}

-   {% include citation doi='10.1109/TIT.1975.1055330' %}

-   {% include citation doi='10.1016/0098-3004(84)90020-7' %}

-   {% include citation doi='10.1111/j.2517-6161.1977.tb01600.x' %}

### Disconnect Particles

{% include thumbnail align="right" src="/media/plugins/xfig6-4.jpg" title="3D FIB-nanotomography of cement grains (left), subsequent thresholding (center), disconnected (k=0.7) and labeled particles (right)." %}

In particle analysis from imaging due to the resolution limits, the particles might be wrongly connected at various locations if they are located too close to each other. To remedy such connections, an algorithm for disconnecting them at their bottle necks has been implemented [Münch2006]. If requires a parameter k ranking from [0...1] controlling the disconnection. At k=1, particle separation occurs at any bottle necks while at k=0, no separation at all is being performed. The optimum depends on the data and is usually somewhere around k=0.7 inducing marked bottle necks to be carved and small bottle necks to be left unchanged.

Results from cement grains acquired by 3D FIB-nanotomography are displayed in the figure above. To the left, the original data volume is visualized. The center image shows the mask after image thresholding. Particles close to each other are erroneously interconnected at various locations. The image to the right shows the volume disconnected at k=0.7 and labeled subsequently.

-   {% include citation doi='10.1111/j.1551-2916.2006.01121.x' %}

### Distance Transform

{% include thumbnail align="right" src="/media/plugins/xfig6-5-1.jpg" title="Binary mask from cement particles (left) and Euclidian distance transform of it (center) and of its reversed mask (right)." %}

Fast distance transform of image masks is useful for many morphological imaging applications. In an age of increasing data size, processing speed is of ultimate priority. A modern approach [Saito1994,Meijster2000] allows the generation of the distance transform even in linear time. The implementation in this plugin allows the calculation of Euclidian, Chessboard, or Citymap distance transform in both, 2D and 3D.

{% include thumbnail align="left" src="/media/plugins/xfig6-5-2.jpg" title="Mask containing 3 black dots only (left) and its Euclidian, Chessboard and Citymap (right) distance transform." %}

{% include thumbnail align="right" src='/media/plugins/xfig6-6.jpg' title='FIB-nt image (427x768 pixels) from cement paste (left) and the magnitudes (center) and angles (right) of its Fourier transform.'%}

In the upper figure, a binary mask from cement particles (left) is processed by using the Euclidian distance transform (center). The transform of the inverse mask is also given (right). The distances are visualized by using a color lookup table from blue (low values) to red (high values). The effect of different distance metrics is displayed in the lower figure. A simple mask consisting of 3 single black dots is provided (left). Next to it, the results of the Euclidian, Chessboard and Citymap (right) distance transform is shown.

-   {% include citation doi='10.1016/0031-3203(94)90133-3' %}

-   {% include citation doi='10.1007/0-306-47025-X_36' %}

### FFT 2D 3D

The fast, well known and widely used Cooley-Tukey radix-2 algorithm for the calculation of the discrete fast Fourier transform (FFT) only works on data whose size is equal to a power of two. In order to provide FFT on data of different size, the data is usually extended to the next higher power of two. In many cases, this approach is sufficient, in particular if the periodical nature of the transformed data function is not relevant. However, if the period length is important and must be left unchanged, FFT on the original data size is required. This can be achieved by using the Bluestein algorithm [Bluestein1968,Rabiner1969]. Since to our best knowledge, there is no ImageJ plugin available that permits FFT for non-radix-2 sized periods, this plugin has been built. It correctly calculates the complex FFT on 2D and 3D images of arbitrary size. It optionally provides the real and the imaginary part, or the magnitude and the angle images. Moreover, it allows a logarithmic or square-root based scaling to be introduced in order to lower the contrast among the FFT coefficients. This feature is useful if the FFT function is used for display purpose. The reversibility of the FFT transform is supported for all these options.

The figure to the right shows a sample FIB-nt image from cement paste (left) with a width of 427 and a height of 768 pixels. The magnitudes and angles of its Fourier transform is scaled by a logarithmic funcion for improving the visibility of the small coefficients. The inverse FFT transform of the center and right images reconstructs the original function (left) again without any loss of precision.

-   {% include citation doi='10.1109/TAU.1970.1162132' %}
-   {% include citation doi='10.1109/TAU.1969.1162034' %}

### Image Calculator

Many image calculators allowing various arithmetic operations are already implemented in ImageJ, including the "Image Calculator", the "Calculator Plus" as well as the entire list of functions in "math", all of them under "Process". So why "yet another image calculator", you might ask. The reason is that our image calculator is easily able to perform the possible tasks of all of the above listed plugins and much more. The conceptual idea is to provide a list of all the images and image stacks that are currently opened in ImageJ and assign them to symbolic names (i0, i1, i2,...). In a text field, the user can then provide his own code he wants to be applied to the images.

{% include thumbnail align="right" src='/media/plugins/xfig6-7-01.jpg' title='left: image i0, 2nd: image i1, 3nd: image i2, right: mean value of the images i0, i1 and i2' %}
```python
(i0 + i1 + i2) / 3
```

Make sure there are three images loaded on ImageJ such that i0, i1, and i2 are the ones to be processed.  Subsequently, the above command will return an image providing the mean value of images i0, i1 and i2 (see rightmost image to the right).  

The command

{% include thumbnail align="right" src='/media/plugins/xfig6-7-02.jpg' title='left: image i0, right: mask where regions higher than 170 are colored in red' %}
```python
(i0 > 170)? 
	java.awt.Color.red.getRGB() : java.awt.Color.black.getRGB()
```

displays a mask where regions higher than 170 are red.  

{% include thumbnail align="right" src='/media/plugins/xfig6-7-03.jpg' title='left: image i0, 2nd: image i1, 3rd: image i2, right: colored mask out of images i0, i1, i2' %} The operation
```python
(i0==255)? -16711936 : 
	((i1==255)? -16776961 : ((i2==255)? -16777216 : -65536))    
```

takes three binary images i0, i1, i2 and creates a colored mask out of it (see rightmost image to the right).  
  
  
  
  
{% include thumbnail align="right" src='/media/plugins/xfig6-7-04.jpg' title='left: image i0, right: power of two of image i0' %} The operation
```java
Math.pow(i0, 2.)
```

yields the power of two of the image i0.  
  
  
  
  
  
  
{% include thumbnail align="right" src='/media/plugins/xfig6-7-05.jpg' title='left: image i0, right: copy of the image i0 overlayed by a horizontal ramp' %} Or the operation
```python
i0 + x
```
will calculate a copy of the image i0 overlayed by a horizontal ramp.  
  
  
  
  
  
  
  
{% include thumbnail align="right" src='/media/plugins/xfig6-7-06.jpg' title='left: image i0, right: ramp with the same size as image i0' %} And the code line
```python     
x // i0
```

creates the ramp only.

In this case, instead of a simple command "x" (which would create no image), a comment "i0" is attached to the command ("//" means a comment in java). The reason for why this is necessary is to provide a clue about the size of the resulting image which now turns out to be equal to the size of image i0. Hence, the content of the image i0 is actually not being used, it serves as a template for the resulting size only.  
  
  
  
{% include thumbnail align="right" src='/media/plugins/xfig6-7-07.jpg' title='left: image i0 defining image size, right: halo centered at (100, 200)' %} The code
```python     
Math.sqrt(Math.pow(100 - x, 2) + Math.pow(200 - y, 2)) // i0
```

calculates an image of the same size as image i0, but containing only a halo centered at (100, 200).  
  
  
  
  
  
  
{% include thumbnail align="right" src='/media/plugins/xfig6-7-08.jpg' title='left: image i0, right: binary thresholding of i0 by value 128' %} The line
```python
(i0 >= 128)? 255 : 0
```

creates a binary image mask by thresholding the image i0 with the value 128.  
  
  
  
  
  
  
  
{% include thumbnail align="right" src='/media/plugins/xfig6-7-09.jpg' title='left: image i0, right: circular mask around (100, 200)' %} The command
```python
(Math.sqrt(Math.pow(150 - x, 2) + 
 Math.pow(200 - y, 2)) < 100)? 255 : 0 // i0
```
creates an image of the same size as i0 containing a circular mask around point (100, 200). The comment "// i0" is necessary for the definition of the image size to the size of i0.  
  
  
  
  
  
{% include thumbnail align="right" src='/media/plugins/xfig6-7-10.jpg' title='left: image i3, right: content of image i3 inside of a circle only' %}
The code

```python
(Math.sqrt(Math.pow(mx / 2 - x, 2) + 
 Math.pow(my / 2 - y, 2)) < mx / 2)? i3 : 0
```
takes the content of the image inside of a circle only and removes the regions outside (please note: this code fragment makes use the variables mx and my which are holding the image size).  
  
  
  
  
  
{% include thumbnail align="right" src='/media/plugins/xfig6-7-11.jpg' title='left: image i0, center: image i1, right: exclusive OR of images i0 and i1' %}
Finally,

```python   
(((int)i0 ^ (int)i1) > 0)? 255 : 0
```

performs an exclusive OR operation of image i0 and image i1.

The above examples show that any pixel- or voxel-wise operation can be provided in a single command line as soon as it follows the Java notation. The plugin is however able to do much more. Instead of pixelwise operation mode, image-wide Java code fragments can be provided. For example,

```java
float[] out = new float[i0.length];
for (int ii = 0; ii < out.length; ii++) 
	out[ii] = (i0[ii] + i1[ii] + i2[ii]) / 3f;
return new Object[] { m0, out };
```

performs the same operation as the pixelwise operation "(i0 + i1 + i2) / 3" above. {% include thumbnail align="right" src='/media/plugins/xfig6-7-13.jpg' title='left: image i0, right: message box with number of pixel values &gt;= 10' %} The code fragment
```java
float value = 10f;
int[] mm = m0;
int anz = 0;
for (int ii = 0; ii < i0.length; ii++) 
	if (i0[ii] >= value) anz++;
IJ.showMessage(" ", "Number of pixels: " + anz);
return new Object[] { mm, null };
```

{% include thumbnail align="right" src='/media/plugins/xfig6-7-14.jpg' title='left: image i3, center: image i5, right: image i5 embedded at the center area of image i3' %} Counts all pixels (or voxels) in the image (or volume) with a value larger or equal 10.  
  
  
  
  
Or the code

```java
int offx = (m3[0] - m5[0]) / 2;
int offy = (m3[1] - m5[1]) / 2;
float[] out = (float[])i3.clone();
for (int jj = 0; jj < m5[1]; jj++) 
	for (int ii = 0; ii < m5[0]; ii++) 
	out[ii + offx + (jj + offy) * m3[0]] = 
		(i3[ii+offx + (jj+offy) * m3[0]] + 
		 i5[ii + jj * m5[0]]) / 2f;
return new Object[] { m3, out };
```

takes the smaller image i5 and adds it to the center of the larger image i3.  
  
{% include thumbnail align="right" src='/media/plugins/xfig6-7-15.jpg' title='left: image i0, center: image mask i1, right: message box with mean value of i0 within mask i1' %} The code fragment

```java     
double mean = 0;
int anz = 0;
for (int ii = 0; ii < m0[0] * m0[1]; ii++) 
	if (i1[ii] > 127) {
		mean += i0[ii];
		anz++;
	}
mean /= anz;
IJ.showMessage("mean value: " + mean);
return null;
```

just calculates the overall mean value of image i0 within the ROI defined by i1 and displays it in a check box.

<img src="/media/plugins/xfig6-7-16.jpg" width="200"/>  
  
Moreover, it is even possible to create your own images without any input image:

```java     
int mx = 256;
int my = 200;
float[] out = new float[mx * my];
for (int jj = 0; jj < my; jj++) 
	for (int ii = 0; ii < mx; ii++) out[ii + jj * mx] = ii;
return new Object[] { new int[] { mx, my }, out };
```

creates an image containing a ramp (see image to the right), or

<img src="/media/plugins/xfig6-7-17.jpg" width="200"/>

```java     
int mx = 256;
int my = 200;
float[] out = new float[mx * my];
for (int jj = 0; jj < my; jj++) 
	for (int ii = 0; ii < mx; ii++) {
		if (Math.sqrt(Math.pow(ii - mx / 2, 2) + 
					  Math.pow(jj - my / 2, 2)) < 80) 
			out[ii + jj * mx] = 255;
	}
return new Object[] { new int[] { mx, my }, out };
```

<img src="/media/plugins/xfig6-7-18.jpg" title="fig:xfig6-7-18.jpg" width="380" alt="xfig6-7-18.jpg" /> creates an image containing a circle mask in the center (see image to the right). For more information about the syntax, please consult the help function of the plugin itself.

As a final example, we show that it is also possible to create even more 'cute' images with that tool:

```java
int max = 255;
int mx = 512;
int my = 512;
float[] out = new float[mx * my];
for (int jj = 0; jj < my; jj++) 
	for (int ii = 0; ii < mx; ii++) {
		double px = -2. + (double)ii / 200.;
		double py = -1. + (double)jj / 255.;

		double zx = 0.0, zy = 0.0;
		double zx2 = 0.0, zy2 = 0.0;
		int value = 0;
		while (value < max && zx2 + zy2 < 4.0) {
			zy = 2.0 * zx * zy + py;
			zx = zx2 - zy2 + px;
			zx2 = zx * zx;
			zy2 = zy * zy;
			value++;
		}
		out[ii + jj * mx] = 50f * (float)Math.log(value);
	}
return new Object[] { new int[] { mx, my }, out };
```
This code fragment creates the image to the right showing a well-known Mandelbrot fractal!
