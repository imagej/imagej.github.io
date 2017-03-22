{{BigNotice | See [[:Category:Deconvolution]] for pages about deconvolution.}}
__FORCETOC__ {{CookbookMenu}}{{Learn | techniques}}[[wikipedia:Deconvolution|Deconvolution]] corrects the systematic error of blur (loss of contrast in smaller features)  in optical systems such as fluorescence microscopy images.

== The problem, and the solution ==

Any optical image forming system, such as a microscope objective lens, has the nasty property of killing more and more contrast of smaller and smaller features, up to the resolution (diffraction) limit, after which there is no contrast (and thus no resolution). Large features are bright, but small features appear less contrasted and dimmer than they should. This is a systematic error, characterized by the Point Spread Function (PSF) of the optical system, which makes the image intensity information non-quantitative. If we can measure the PSF, or guess it, we can correct the raw image for it. Since it's possible to correct such a systematic error, we should! 

Image contrast restoration by deconvolution is a way to correct the systematic error of contrast loss in an image recording system, such as a microscope objective lens or telescope mirror or lens. We try to reverse the effects of blur in the recorded image, caused by convolution (blur, smearing, loss of contrast of small features) of the real image due to the imaging point spread function (PSF). 

Image contrast restoration by deconvolution is an important systematic error correction step for quantitative measurement of image pixel intensities in analysis workflows. If we don't correct this systematic error, the results of the image intensity analysis could be very much more wrong than if we correct the images before analysis. It's the same as zeroing a scale before weighing something.

== Introduction to the practical method ==

Two plugins from Bob Dougherty can be used together to perform this systematic error correction in a 2D or 3D image. Other plugins are also available. The Diffraction-PSF-3D plugin generates a z-stack of the theoretical point-spread function (PSF). Alternatively, an empirical, measured PSF could be used. The Iterative Deconvolution 3D plugin uses a PSF image z-stack to correct the image contrast vs. feature size in your sample image z-stack. The image below is a single slice taken from a stack before and after deconvolution using these plugins. 

[[File:deconvoluted_data.png]]

''See the plugins' homepages for more details:'' [http://www.optinav.info/Diffraction-PSF-3D.htm Diffraction PSF 3D] & [http://www.optinav.info/Iterative-Deconvolve-3D.htm Iterative Deconvolution 3D]
 
== Generating a PSF image stack ==

The Diffraction PSF 3D plugin can be used to generate theoretical PSFs assuming they arise only from diffraction. These PSFs may be used with other deconvolution plugins later.

To use, run the "Diffraction PSF 3D" plugin. A dialog will appear; most of the fields are self explanatory. The width, height and depth values are for the PSF image, not your image stack. The desired values will need to be empirically determined. Try to match the parameters used to capture the raw image.

[[File:diffraction_psf_window1.png|377x317px]]

== Constrained Iterative Deconvolution ==
Non negative constrained (non linear), iterative deconvolution algorithms greatly outperform simple inverse filters and Wiener filters on noisy real life fluorescence microscopy (and other) image data.

Run the Iterative Deconvolve 3D plugin, then select the image and PSF. For a 2D image, use a 2D (single plane) PSF. For 3D images, use a 3D PSF (z stack). Start with the default values and set iterations to 10 initially. Be careful not to run out of memory when processing large 3D images. Crop them if they are too large.

[[File:iterative_deconvolve_window.png|411x272px]]

== An interactive Convolution / Deconvolution / Contrast Restoration demo in ImageJ ==

For an educational interactive ImageJ javascript demo of convolution, inverse filtering and image contrast restoration by iterative constrained deconvolution (using the above plugins), see this [https://github.com/chalkie666/imagejMacros/blob/master/DeconvolutionDemos/Convolution_Deconvolution_Demo.js Convolution / Deconvolution / Contrast Restoration demo script] 

== Video presentations ==
<div style="float: left; padding-right: 1em">{{#widget:Vimeo|id=140098821|caption=Flexible deconvolution using ImageJ Ops (Brian Northan)}} by {{Person|Bnorthan}}, ([https://imagej.github.io/presentations/2015-09-04-imagej2-deconvolution/ slides])</div>
<div style="float: left">{{#widget:Vimeo|id=140098826|caption=Real-time multi-view deconvolution of time-lapse data on the GPU (Bene Schmid)}} by {{Person|Bene}}</div>
{{Clear|left}}
[[Category:Cookbook]]
[[Category:Tutorials]]
