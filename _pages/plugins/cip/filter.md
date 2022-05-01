---
title: CIP Filter
---

This page provides user documentation for the filter functions of the [CIP](/plugins/cip) package

{% include cip/nav %}

# **gauss**

<span style="font-size:110%">**Description**</span>  
gauss creates a gaussian blurred image. it convolves the image with a gaussian weighted window. Gaussian blurring is commonly used for image denoising as it smoothes out small details.

<span style="font-size:110%">**Signature**</span>  

`outputImage = cip.gauss( inputImage* , radius* , boundary , pixelSize)`

<span style="font-size:110%">**Input**</span>

**inputImage\*** : the image to process  
**radius\*** : a scalar or list of scalar representing the standard deviation ofthe gaussian kernel standard deviation along the image axis  
**boundary** : a string in {'min', 'max', 'same', 'zero', '<u>mirror</u>','periodic'}, default is mirror  
**pixelSize** : a scalar or list of scalar along image dimension. Default is 1.

<span style="font-size:110%">**Output**</span>  
    
**outputImage**: the processed image. it always as the same size as the input image.

<span style="font-size:110%">**Example**</span>  
    
`img2 = cip.gauss( img1 , 5 )`

<img src="/media/plugins/cip/cip-gauss.png" title="fig:CIP_gauss.PNG" width="400" alt="CIP_gauss.PNG" />

<span style="font-size:110%">**Implementation**</span>  
CIP gauss implementation wraps the gauss ops, itself relying on the [imglib2 gauss3 implementation](https://github.com/imglib/imglib2-algorithm/tree/master/src/main/java/net/imglib2/algorithm/gauss3).

# **erode**

<span style="font-size:110%">**Description**</span>  
Erosion shrinks the region in an image by a certain radius. It works both with binary and graylevel images. This effect is obtained by replacing each pixel value by the minimum value found in a window surrounding that pixel.

<span style="font-size:110%">**Signature**</span>  
    
`outputImage = cip.erode( inputImage*, radius*, shape, boundary, pixelSize)`

<span style="font-size:110%">**Input**</span>  
    
**inputImage\*** : the image process  
**radius\*** : a integer or list of integer representing the half size of thefilter window along the image axis.  
**shape** : a string in {'<u>rectangle</u>', 'disk'} describing the shape of thewindow used for the processing.  
**boundary** : a string in {'min', 'max', 'same', '<u>mirror</u>', 'periodic'},default is mirror  
**pixelSize** : a scalar or list of scalar along image dimension. Default is 1.

<span style="font-size:110%">**Output**</span>  
    
**outputImage**: the processed image.

<span style="font-size:110%">**Example**</span>  
    
`img2 = cip.erode( img1 , 2 )` 
    
<img src="/media/plugins/cip/cip-erode.png" title="fig:CIP_erode.PNG" width="400" alt="CIP_erode.PNG" />  

<span style="font-size:115%">**Implementation**</span>  
CIP function wraps the [imglib2 Erosion class](https://github.com/imglib/imglib2-algorithm/blob/master/src/main/java/net/imglib2/algorithm/morphology/Erosion.java) from the morphology package.

# **dilate**

<span style="font-size:110%">**Description**</span>  
this filter dilate the region in an image by a certain radius. It works both with binary and graylevel images. This effect is obtained by replacing each pixel value by the maximum value found in a window surrounding that pixel.

<span style="font-size:110%">**Signature**</span>  

`outputImage = cip.dilate( inputImage* , radius*, shape, boundary, pixelSize)`

<span style="font-size:110%">**Input**</span>

**inputImage\*** : the image process  
**radius\*** : a integer or list of integer representing the half size of thefilter window along the image axis.  
**shape** : a string in {'<u>rectangle</u>', 'disk'} describing the shape of thewindow used for the processing.  
**boundary** : a string in {'min', 'max', 'same', '<u>mirror</u>', 'periodic'},default is mirror  
**pixelSize** : a scalar or list of scalar along image dimension. Default is 1.

<span style="font-size:110%">**Output**</span>  
    
**outputImage**: the processed image.

<span style="font-size:110%">**Example**</span>  
    
`img2 = cip.dilate( img1 , 2 )`

<img src="/media/plugins/cip/cip-dilate.png" title="fig:CIP_dilate.PNG" width="400" alt="CIP_dilate.PNG" />

<span style="font-size:110%">**Implementation**</span>

CIP function wraps the [imglib2 Dilation class](https://github.com/imglib/imglib2-algorithm/blob/master/src/main/java/net/imglib2/algorithm/morphology/Dilation.java) from the morphology package.

# **opening**

<span style="font-size:110%">**Description**</span>  
This filter performs an erosion followed by a dilation. It erases small and thin objects.

<span style="font-size:110%">**Signature**</span>  
    `outputImage = cip.opening( inputImage* , radius* , shape, boundary, pixelSize)`

<span style="font-size:110%">**Input**</span>  
    
**inputImage\*** : the image process  
**radius\*** : a integer or list of integer representing the half size of thefilter window along the image axis.  
**shape** : a string in {'<u>rectangle</u>', 'disk'} describing the shape of thewindow used for the processing.  
**boundary** : a string in {'min', 'max', 'same', '<u>mirror</u>', 'periodic'},default is mirror  
**pixelSize** : a scalar or list of scalar along image dimension. Default is 1.

<span style="font-size:110%">**Output**</span>  
    
**outputImage**: the processed image.

<span style="font-size:110%">**Example**</span>  
    
`img2 = cip.opening( img1 , 5 )` 
    
<img src="/media/plugins/cip/cip-opening.png" title="fig:CIP_opening.PNG" width="400" alt="CIP_opening.PNG" />

<span style="font-size:110%">**Implementation**</span>  
CIP function wraps the [imglib2 Opening class](https://github.com/imglib/imglib2-algorithm/blob/master/src/main/java/net/imglib2/algorithm/morphology/Opening.java) from the morphology package.

# **closing**

<span style="font-size:110%">**Description**</span>  
This filter performs a dilation followed by an erosion. It closes small holes and thin gaps between or inside objects.

<span style="font-size:110%">**Signature**</span>  
    
`outputImage = cip.closing( inputImage* , radius* , shape, boundary, pixelSize)`

<span style="font-size:110%">**Input**</span>

**inputImage\*** : the image process  
**radius\*** : a integer or list of integer representing the half size of thefilter window along the image axis.  
**shape** : a string in {'<u>rectangle</u>', 'disk'} describing the shape of thewindow used for the processing.  
**boundary** : a string in {'min', 'max', 'same', '<u>mirror</u>', 'periodic'},default is mirror  
**pixelSize** : a scalar or list of scalar along image dimension. Default is 1.

<span style="font-size:110%">**Output**</span>  
    
**outputImage**: the processed image.

<span style="font-size:110%">**Example**</span>  
    
`img2 = cip.closing( img1 , 16, 'disk' )`

<img src="/media/plugins/cip/cip-closing.png" title="fig:CIP_closing.PNG" width="600" alt="CIP_closing.PNG" />

<span style="font-size:110%">**Implementation**</span>  
The implementation successively applies CIP erosion and dilation functions.

# **tophat**

<span style="font-size:110%">**Description**</span>  
This filter subtract an opening of the input image to the input image. It removes object larger than the user selected radius in image while keeping smaller scale details.

<span style="font-size:110%">**Signature**</span>

`outputImage = cip.closing(inputImage*, radius*, shape, boundary, pixelSize)`

<span style="font-size:110%">**Input**</span>

**inputImage\*** : the image process  
**radius\*** : a integer or list of integer representing the half size of thefilter window along the image axis.  
**shape** : a string in {'<u>rectangle</u>', 'disk'} describing the shape of thewindow used for the processing.  
**boundary** : a string in {'min', 'max', 'same', '<u>mirror</u>', 'periodic'},default is mirror  
**pixelSize** : a scalar or list of scalar along image dimension. Default is 1.

<span style="font-size:110%">**Output**</span>

**outputImage**: the processed image.

<span style="font-size:110%">**Example**</span>

`img2 = cip.tophat( img1 , 5, 'disk' )`

<img src="/media/plugins/cip/cip-tophat.png" title="fig:CIP_tophat.PNG" width="500" alt="CIP_tophat.PNG" />

<span style="font-size:110%">**Implementation**</span>  
The function relies on ops for subtraction and CIP for the opening.

# **distance**

<span style="font-size:110%">**Description**</span>  
this function create an image where each pixel value correspond between the distance of that pixel to the closest background object in the input image

<span style="font-size:110%">**Signature**</span>

`outputImage = cip.distance(inputImage*, threshold, pixelSize)`

<span style="font-size:110%">**Input**</span>

**inputImage\*** : the image process  
**threshold** : if the input image is not binary that value can be used tothreshold the image. if the input image is binary that value is ignored  
**pixelSize** : a scalar or a list of scalar representing pixel size along imagedimension. Default is 1.

<span style="font-size:110%">**Output**</span>

**outputImage**: the processed image.

<span style="font-size:110%">**Example**</span>

`img2 = cip.distance( img1 , 500 )` or `img2 = cip.distance( img1 , 'threshold', 500 )` 
    
<img src="/media/plugins/cip/cip-distance1.png" title="fig:CIP_distance1.PNG" width="400" alt="CIP_distance1.PNG" />  

`img2 = cip.distance( img1 )` will build the distance map for a binary image. 

<img src="/media/plugins/cip/cip-distance2.png" title="fig:CIP_distance2.PNG" width="400" alt="CIP_distance2.PNG" />

<span style="font-size:110%">**Implementation**</span>  
The function relies on ops distance function implementation.

# **median**

<span style="font-size:110%">**Description**</span>  
This filter is used to denoise image. It is well suited to remove impulse noise.Compare to the gaussian filter it preserve edges better but has higher computationnal cost. Its basic principle is to replace a pixel value with the median value in a window surrounding that pixel.

<span style="font-size:110%">**Signature**</span>

`outputImage = cip.median(inputImage*, radius*, shape, boundary, pixelSize)`

<span style="font-size:110%">**Input**</span>

**inputImage\*** : the image process  
**radius\*** : a integer or list of integer representing the half size of thefilter window along the image axis.  
**shape** : a string in {'<u>rectangle</u>', 'disk'} describing the shape of thewindow used for the processing.  
**boundary** : a string in {'min', 'max', 'same', '<u>mirror</u>', 'periodic'},default is mirror  
**pixelSize** : a scalar or list of scalar along image dimension. Default is 1.

<span style="font-size:110%">**Output**</span>

**outputImage**: the processed image.

<span style="font-size:110%">**Example**</span>

`img2 = cip.median( img1 , 5 )`

<img src="/media/plugins/cip/cip-median.png" title="fig:CIP_median.PNG" width="400" alt="CIP_median.PNG" />

<span style="font-size:110%">**Implementation**</span>  
The function relies on ops that implement a brute force approach of the median filtering. It would be possible to implement more efficient approach using histogram and cord decomposition such ImageJ 1.x implementation for 2D image.

# **invert**

<span style="font-size:110%">**Description**</span>  
This function invert the gray value of the input image such that each pixel value I is replaced by max+min-I , where are min (resp max) are the minimum (resp maximum) intensity in the input image.

<span style="font-size:110%">**Signature**</span>

`outputImage = cip.invert(inputImage*)`

<span style="font-size:110%">**Input**</span> 

**inputImage\*** : the image to process

<span style="font-size:110%">**Output**</span>

**outputImage**: the processed image.

<span style="font-size:110%">**Example**</span>

`img2 = cip.invert( img1 )`

<img src="/media/plugins/cip/cip-invert.png" title="fig:CIP_invert.PNG" width="400" alt="CIP_invert.PNG" />
  
<span style="font-size:110%">**Implementation**</span>  
The function implementation uses ops map function
