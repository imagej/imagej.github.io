---
title: CIP Format
---

This page provides user documentation for the Format category of the [CIP](/plugins/cip) scripting package.

{% include cip/nav %}

# **create**

<span style="font-size:110%">**Description**</span>  
this function allows to create image specifying their size, value, pixel type and name.

<span style="font-size:110%">**Signatures**</span>

`outputImage = cip.create( size*, value, type, name)`  
will create an image of size extent initialized with the specified value, pixel type and name.

`outputImage = cip.create( inputImage*, value, type, name)`  
will create an image of the same size as inputImage, initialized with the specified value, pixel type and name.

<span style="font-size:110%">**Input**</span>

**inputImage\*** : an image which size will be used to create an the image process  
**size\*** : a list of scalars specifying the dimensions of the image to create  
**value** : value a scalar which value is used to initialize the new image  
**type** : a string in {'bit', 'uint8', 'int8', 'uint16', 'int16', 'uint32', 'int32', 'uint64', 'int64', '<u>float</u>', 'double'} defining the pixel type of the output. denomination such as'short' or 'ushort' or 'unsignedshort' can also be used.  
**name** : a string used for the new image name.

<span style="font-size:110%">**Output**</span>

**outputImage** : an image with the specified size, value, pixel type and name.

<span style="font-size:110%">**Implementation**</span>  
the function wraps the ops img function in the namespace create

# **duplicate**

<span style="font-size:110%">**Description**</span>  
The function duplicate an input image or a crop if the input image

<span style="font-size:110%">**Signature**</span>

`outputImage = cip.duplicate( inputImage*, origin, size, method)`  
will duplicate the input image within the specified boundary.

<span style="font-size:110%">**Input**</span>

**inputImage\*** : the image to duplicate  
**origin** : a list of scalar specifying the origin of the region to duplicate. if not provided the input image origin is used  
**size** : a list of scalar specifying the extent of the region to duplicate. if not provided the max minus the origin is choosen for each dimension  
**method** : a string in {'deep', '<u>shallow</u>'} specifying whether the output will copy the data or have a reference to the input data.

<span style="font-size:110%">**Output**</span>

**outputImage\*** : the duplicated image

<span style="font-size:110%">**Example**</span>

`img2 = cip.duplicate( img1 , 'origin', [300,200], 'size', [150,150] )`

<img src="/media/plugins/cip/cip-duplicate.png" title="fig:CIP_duplicate.PNG" width="400" alt="CIP_duplicate.PNG" />

<span style="font-size:110%">**Implementation**</span>  
the shallow copy is done with Views.offsetInterval in ImgLib2 and the deep copy is done with the ops function copy().rai().

# **slice**

<span style="font-size:110%">**Description**</span>  
This function reduce input image dimensionality by duplicating a region of the same size as the input except along a selected dimension where the input is duplicated only at a particular position.

<span style="font-size:110%">**Signature**</span>

`outputImage = cip.slice( inputImage*, dimension, position, method)`  
will duplicate the input at the specified position along the specified dimension(s).

<span style="font-size:110%">**Input**</span>

**inputImage\*** : the image to process  
**dimension** : a scalar or a list of scalars specifying the dimension(s) to slice  
**position** : a scalar or list of scalars the same size as dimensions indicating the position to duplicate along the specified dimension(s).  
**method** : a string in {'deep', '<u>shallow</u>'} specifying whether the output will copy the data or have a reference to the input data.

<span style="font-size:110%">**Output**</span>

**outputImage\*** : the duplicated image. The singleton dimension(s) are dropped so the image dimensionnality is effectively smaller than the input dimensionnality.

<span style="font-size:110%">**Example**</span>

`img2 = cip.slice( img1 , 'dimension', 2, 'position', 0 )`

<img src="/media/plugins/cip/cip-slice.png" title="fig:CIP_slice.PNG" width="400" alt="CIP_slice.PNG" />

<span style="font-size:110%">**Implementation**</span>  
The shallow copy is done with Views.offsetInterval in ImgLib2 and the deep copy also apply the ops function copy().rai().

# **project**

<span style="font-size:110%">**Description**</span>  
This function reduce input image dimensionality by applying an operation to all the pixel along user specified dimension(s). sum, max and ,min operation are currently implemented.

<span style="font-size:110%">**Signature**</span>

`valMap, argMap = cip.project( inputImage*, dimension, method, output)`  
create a projected image along the specified dimension(s) with the specified method.

<span style="font-size:110%">**Input**</span>

**inputImage\*** : the image to process  
**dimensions** : a scalar or a list of scalars specifying the dimension(s) to slice  
**position** : a scalar or list of scalars the same size as dimensions indicating the position to duplicate along the specified dimension(s).  
**output** : a string in {'<u>projection</u>', 'argument', 'both'} specifying whether the output should be the projected image, the argument of the projection or both. if the argumentconstruction is not applicable the argument has the value of the number of slice.

<span style="font-size:110%">**Output**</span>

**valMap** : the projected image. The singleton dimension(s) are dropped so the image dimensionnality is effectively smaller than the input dimensionnality.  
**argMap** : the argument of the projection. that is for a max projection for instance the postions at the pixel value was maximum along the projection dimension.

<span style="font-size:110%">**Example**</span>

`img2 = cip.project( img1 , 'dimension',2 )`

<img src="/media/plugins/cip/cip-project.png" title="fig:CIP_project.PNG" width="400" alt="CIP_project.PNG" />  

<span style="font-size:110%">**Implementation**</span>  
The [projection](https://github.com/benoalo/CIP/blob/master/src/main/java/invizio/cip/misc/Project2CIP.java) is implemented as part of CIP.

# **concatenate**

To be implemented
