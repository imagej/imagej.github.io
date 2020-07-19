{{Component
| project = ImageJ
| name    = Phase Unwrapping
| source = {{GitHub | org=sudgy | repo=phase-unwrapping}}
| license = [[LGPLv3]]
| devStatus = {{DevStatus | developer=yes | incubating=no | obsolete=no}}
| supportStatus = {{SupportStatus | debugger=yes | reviewer=yes | support=yes}}
| founders = {{Person|David Cohoe}} ([mailto:dcohoe@pdx.edu])
| leads = {{Person|David Cohoe}}
| developers = {{Person|David Cohoe}}
| debuggers = {{Person|David Cohoe}}
| reviewers = {{Person|David Cohoe}}
| support = {{Person|David Cohoe}}
| maintainers = {{Person|David Cohoe}}
}}

Phase Unwrapping is a plugin to perform phase unwrapping on a phase image, with a focus on unwrapping images produced by DHM (possibly created using [[DHM Utilities/Reconstruction]]).  It currently has support for two different algorithms.  The first is a quality-guided unwrapping method, and the second is a double-wavelength unwrapping method.

== Quality-Based Unwrapping ==

The quality-based unwrapping algorithm works on the principle that some pixels should be considered "better" than others when it comes to how well they represent the true phase value of the image.  To determine these values, the algorithm uses a "quality" mapping which assigns a quality value to every pixel in the image.  Several quality types come built in to the plugin, and it is possible to create your own in your own plugins.

To unwrap the image, the algorithm starts with the center pixel.  It then looks at the four adjacent pixels and picks the one with the highest quality, unwrapping it relative to itself.  It then looks at the six adjacent pixels and picks the one with the highest quality, unwrapping it relative to an adjacent pixel that has already been unwrapped with the highest quality.  This process repeats until the entire image has been unwrapped.

To perform quality-based unwrapping, run the command "Plugins > DHM > Phase Unwrapping > Quality Guided".  Here is a description of all of the parameters:
* Phase Image: The phase image that you want to unwrap.
* Quality: What algorithm you wish to use to compute the quality mapping.  Depending on the quality type, it may add additional parameters that will appear directly after this one.
* Single Frame: If the phase image is a stack, select this if you do not want to unwrap the whole stack.
* Pixel Phase Value: The pixel value difference that represents one period in the phase.
* Output Type: Image type for the output.  If 32-bit is selected, the scale will be the same as the original image.  If 32-bit radians is selected, the original scale will be scaled down to [0, 2π].
* Show Progress: Show the progress during unwrapping.  This algorithm can take some time, especially with larger images, so this can be used to alleviate boredom while waiting.

It is also possible to unwrap a single image or a stack of images programmatically using the <code>QualityUnwrappingOp</code> and <code>QualityUnwrappingStackOp</code> Ops.  See the documentation for more details on how to do this.

=== Pre-defined Quality Types ===

==== None ====

This assigns every pixel a quality value of zero.  The exact result this produces is unspecified, and should only be used if you have no residues (a closed curve whose line integral is not zero) whatsoever in your original image.

==== Fringe Visibility ====

Calculates the quality based on the [https://en.wikipedia.org/wiki/Interferometric_visibility Interferometric Visibility].  Higher visibility values correspond to higher quality values.  This quality type requires the hologram as an extra parameter.

==== Gradient ====

This calculates the quality based on the magnitude of the gradient of an arbitrary image.  A lower gradient value corresponds to a higher quality value.

==== Phase Gradient ====

This is similar to the gradient quality, but it uses the phase image and considers the wrapping of phase values in its calculations.  It is what the author has found to produce the best results out of all of the current quality types.

=== Creating a Custom Quality Type ===

To create a custom quality type, you must first include this plugin as a dependency and then create a Scijava Plugin whose type is <code>Quality.class</code> and implements the <code>Quality</code> interface (or, preferably, extends <code>AbstractQuality</code>).  Once you have created the plugin class, it will automatically show up in the quality-guided unwrapping command.  The name of the plugin will be the string that shows up in the dialog.  The priority of the plugin will dictate where on the list it goes.

The <code>Quality</code> interface includes several default methods that you may want to override.  For more information on what you need to do, please check the javadocs, which you can build from the github repository.

<code>Quality</code> uses our custom [https://github.com/sudgy/dynamic-parameters Dynamic Parameters] to process inputs, because some of the parameters may change.  If you do not require any extra inputs in your quality type, you do not need to worry about using this.  However, if you do require extra inputs, you must override <code>param()</code> with your dynamic parameter.  If you require multiple parameters, you should use a <code>HoldingParameter</code> that has all of your parameters.

== Double Wavelength Unwrapping ==

The double wavelength unwrapping algorithm is based off of the double wavelength algorithm described in many places in the literature.  Given two images of the same thing in different wavelengths, the two images are subtracted, than anything less than zero is increased by one wavelength.  This result is called the coarse map.  This, in effect, changes the phase image into a phase image of a longer "beat frequency".  The idea is that sometimes the shortness of the wavelengths is an issue when it comes to unwrapping, and by producing a phase image of a longer wavelength, those issues can be avoided.  The algorithm is also much faster than other unwrapping algorithms.

However, there are a few issues with the algorithm.  The first is that it amplifies the noise present in the original images.  To compensate for this, the algorithm can be extended.  The coarse map can be rounded to one of the individual wavelengths, and then the original image of that wavelength can be added.  This result is called the fine map.  In theory, this works well, but in practice, the coarse map never really lines up with one of the original images, and doing this process causes the whole image to be rounded and have sudden small jumps.

Another issue is that the algorithm doesn't work that well in complicated situations.  We have not determined any exact reasons for why this is the case, but it might be due to how different wavelengths propagate differently near objects.  It has never worked in a place that a single-wavelength algorithm would have worked, so the only real advantage that this algorithm has after these issues is that it is faster.  It still has the problems of extra noise or extra rounding.

There is still another issue: the final image can still be wrapped.  You can always use a single-wavelength unwrapping algorithm afterwards, but at that point, you might as well just use the single-wavelength algorithm in the first place.

If you can find ways to improve our implementation of the algorithm, please let us know.

To use this algorithm in ImageJ, run the command "Plugins > DHM > Phase Unwrapping > Double Wavelength".  Here is a description of all of the parameters:
* Phase Image 1: The first phase image to use.
* Wavelength 1: The wavelength of light used to create the first image.  There are no units on it because the actual value of the wavelength is not important, only the difference between it and the other wavelength is important.
* Phase Image 2: The second phase image to use.
* Wavelength 2: The wavelength of light used to create the second image.
* Pixel Phase Value: The pixel value difference that represents one period in the phase.
* Show Intermediate Steps: Whether or not to show all of the steps taken during the process.  It is mainly used for debug purposes, but it might help when trying to determine what is going on.  If it is off, only the coarse map and the fine map are shown.

It is also possible to unwrap a single image or a stack of images programmatically using the DoubleWavelengthOp and DoubleWavelengthStackOp Ops. See the documentation for more details on how to do this.

[[Category:Plugins]]
