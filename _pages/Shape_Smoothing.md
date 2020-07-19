{{Infobox
| software               = Fiji
| name                   = Shape Smoothing Plugin
| author                 = Undral Erdenetsogt, {{Person|Twagner}}
| maintainer             = Undral Erdenetsogt (erdenetsogt@biomedical-imaging.de), {{Person|Twagner}}
| filename               = [https://github.com/thorstenwagner/ij-shape-smoothing/releases/latest shape-smoothing.jar]
| source                 = [https://github.com/thorstenwagner/ij-shape-smoothing Github]
| latest version         = v1.2 (06 October 2016)
| status                 = maintaining 

}}

= General Purpose =
The plugin smoothens contours of objects in binary images. The Fourier transformation combined with filtering of Fourier descriptors (FDs) are applied to conduct the smoothing.  The user can define the measure of contour smoothing by setting the amount of FDs – either relative or absolute. All FDs up to the selected threshold are scale-, rotation- and translation-invariant.

= Background =
The plugin at first extracts the contours of all objects found in the input image. Object recognition and contour extraction are both performed by using  [https://github.com/thorstenwagner/ij-blob IJBlob]. Then the contours are processed one at a time in the following way:
# Discrete Fourier transformation is applied to contour data (coordinates of contour points) to gain FDs
# FDs are filtered according to user input – only the ones, which are close to the zero frequency (from both sides), are retained. The other ones are cut off, meaning they are set to 0+0i.
# Filtered (or “kept”) FDs are inverse Fourier transformed to obtain the points of the smoothed contour.

For implementing the Fourier transformations [https://github.com/wendykierp/JTransforms JTransforms] was used.

Some theoretical background of FD-filtering: the result of step 1 is a series of FDs with the zero frequency (ZF) in its middle. ZF is essential for reconstruction spatial information of the contour. A frequency or a FD contains the more information the nearer it is to ZF (regardless of the side). Therefore in step 2 the FDs on the ends of the obtained series are set to 0+0i to achieve the smoothing.

= Parameters =
[[File:Shape_smoothing_GUI.png|320px|thumb|Shape-Smoothing parameters]]

At first users have to choose on how they want to define the smoothing: via relative or absolute number of FDs to be “kept”.

'''Relative proportion FDs (%):'''	The relativ number of FDs (relativ to the number of available FDs) will be used for smoothing the contours.

'''Absolute number FDs:'''		The absolute number of FDs will be used for smoothing the contours.

'''Draw only contours:'''		If selected, only the smoothed contours of objects will be draw (without filling them).

'''Output Descriptors:'''		If selected, a table, containing all FDs, will be shown after processing. (Filtered FDs will all have the value 0+0i.)

'''Black Background:'''		Select this option, if the background in the input image is black and the objects are white. (The plugin prefills this parameter according to a rudimentary background detection)

= Examples =
<div><ul> 
<li style="display: inline-block;">[[File:shape-smoothing-original-image.png|thumb|none|300px|Original image]]</li>
<li style="display: inline-block;">[[File:shape-smoothing-smoothed-object.png|thumb|none|300px|Smoothed object (4% of FDs retained)]]</li>
<li style="display: inline-block;">[[File:shape-smoothing-smoothed-contour.png|thumb|none|300px|Smoothed contour (2% of FDs retained)]]</li>
</ul></div>

= Installation =
You could simply use our update site [http://sites.imagej.net/Biomedgroup biomedgroup] to install the plugin.

If you use ImageJ just copy the ij_shape_smoothing-1.0.1.jar file in your plugins folder and copy IJBlob and JTransforms jars into the plugins/jars folder.
