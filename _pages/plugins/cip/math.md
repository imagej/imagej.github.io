---
title: CIP Math
---

This page provides user documentation for the Math category of the [CIP](/plugins/cip) scripting package

{% include cip/nav %}

# binary operator

<span style="font-size:110%">**Description**</span>  
the binary operators receive 2 inputs and produce one output applying the mathematical operation to the inputs. input can be a scalar or an image if one of the input is an image the operation is applied pixelwise. The output is an image is one of the input is an image or a scalar is both input are a number

<span style="font-size:110%">**Signatures**</span>

`c = cip.add( a* , b* )` assigns a + b to c

`c = cip.sub( a* , b* )` assigns a - b to c

`c = cip.mul( a* , b* )` assigns a . b to c

`c = cip.div( a* , b* )` assigns a / b to c

`c = cip.pow( a* , b* )` assigns a<sup>b</sup> to c

`c = cip.min( a* , b* )` assigns the minimum of a and b to c

`c = cip.max( a* , b* )` assigns the maximum of a and b to c

<span style="font-size:110%">**Implementation**</span>  
The function implementation rely on ops map and math operation. Further more the pixelor scalar type is updated to avoid any clipping of the resulting number in the operation. for instance a division between 2 integer image will create a float image.

# unary operator

<span style="font-size:110%">**Description**</span>  
the unary operator receive one input and produces one ouput, applying the specified operation to the input. Input can be an image or a scalar. output is of the same type as the input.

<span style="font-size:110%">**Signatures trigonometry**</span>

`b = cip.sin( a )` calculate the trigonometric sinus function. a is in radian

`b = cip.cos( a )` calculate the trigonometric cosinus function. a is in radian

`b = cip.tan( a )` calculate the trigonometric tangent function. a is in radian

`b = cip.asin( a )` calculate the trigonometric arcsinus function. b is in radian

`b = cip.acos( a )` calculate the trigonometric arccosinus function. b is inradian

`b = cip.atan( a )` calculate the trigonometric arctangent function. b is in radian

<span style="font-size:110%">**Signatures rounding**</span>

`b = cip.floor( a )` replace a by the closest integer such that abs(a)&gt;abs(b)

`b = cip.ceil( a )` replace a by the closest integer such that abs(a)&lt;abs(b)

`b = cip.round( a )` replace a by to the closest integer

<span style="font-size:110%">**Other Signatures**</span>

`b = cip.sqrt( a )` calculate the sqare root of a

`b = cip.log( a )` calculates the neperian logarithm of a

`b = cip.exp( a )` calculates the exponential of a

`b = cip.abs( a )` calculates absolute value of a

`b = cip.sign( a )` replace a 1 if a&gt;0, 0 if a=0 and -1 if a&lt;0

<span style="font-size:110%">**Implementation**</span>  
The function implementation rely on ops map and java Math implementation. Further more the pixel or scalar type is updated to avoid any clipping of the resulting number in the operation. for instance the logarithm of an integer will be a float value.
