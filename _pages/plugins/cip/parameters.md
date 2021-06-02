---
title: CIP Parameters
---

{% include cip/nav %}

<h1><span class="mw-headline" id="Types">Types</span></h1>
<ul><li><b>Image</b>:any image type in: IJ1 ImagePlus, IJ2 Dataset, IJ2 ImgPlus, ImgLib2 Img, ImgLib2 RandomAccessInterval (RAI), CIP image which implements RAI and adds a thin layer of metadata (units, pixel size, axes names). output image are always a CIP image. Converters allows to get back to IJ1 or IJ2 format if needed.</li>
<li><b>Region</b>:any type in: IJ1 Roi, ImgLib2 IterableRegion, or CIP regions which implement IterableRegion and a thin layer of metadata.</li>
<li><b>Table</b>: a a dictionnary that maps strings to object, most likely string or scalar but possibly Region or Image too</li>
<li><b>Scalar(s)</b>: a numeric value (or a list of numeric values) as available in script langage.</li>
<li><b>String(s)</b>: a string of character or list of string as available in script langage</li>
<li><b>Logic</b>: a boolean (i.e. true or false value).</li></ul>
<p><br />
</p>
<h1><span class="mw-headline" id="Required_and_Optionnal_Parameters">Required and Optionnal Parameters</span></h1>
<p>In CIP each function has <b>required parameters that must be provided</b> for the function to run. This parameters are indicated by an <b>*</b> in the documentation.
</p><p>Each function als has some <b>optionnal parameter that can be skipped</b> if you don't need them. If an optionnal parameters is not provided it will be replaced by a sensible default value described in the documentation
</p><p>There are different ways of skiping an optionnal parameters:
</p>
<ul><li> if they are at the end of the signature you can just drop them and the function will work using defaults value for them. <br /> <code>out = cip.gauss(myImage, myRadius,myBoundary)</code> or even <br /> <code>out = cip.gauss(myImage, myRadius)</code></li>
<li> if they are in the middle of the signature you can either
<ul><li> replace them by the null value of your scripting langage. <br /> <code>cip.gauss(myImage, myRadius, None, myPixelSize)</code> where None is the null value in Jython</li>
<li> drop the parameter and used named parameter for the remaining parameter you need <br /> <code>cip.gauss(myImage, myRadius, 'pixelsize', myPixelSize)</code> that is maybe easier to read.</li></ul></li></ul>
<p><br />
</p>
<h1><span class="mw-headline" id="Positional_and_Named_Parameters">Positional and Named Parameters</span></h1>
<p>There are 2 ways to pass the parameters to a CIP function:
</p>
<ul><li> by passing in the same position and order as the example signature provided in the documentation. If we take the gauss function as example it would write as follows using only the required parameters: <br /> <code> out = gauss(in , myRadius )</code></li>
<li> by passing a string/value <br /> <code>out = gauss(in , 'radius', myRadius) </code>  or even <br /><code>out = gauss('radius', myRadius, 'inputImage', in )</code></li></ul>
