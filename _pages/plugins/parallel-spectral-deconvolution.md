---
mediawiki: Parallel_Spectral_Deconvolution
title: Parallel Spectral Deconvolution
categories: [Deconvolution]
---

{% include info-box software='ImageJ' name='Parallel Spectral Deconvolution 2D and 3D' author='Piotr Wendykier' filename=' [parallel\_spectral\_deconvolution-1.9-bin.zip](http://sourceforge.net/project/downloading.php?group_id=260514&filename=parallel_spectral_deconvolution-1.9-bin.zip)' source=' [parallel\_spectral\_deconvolution-1.9-src.zip](http://sourceforge.net/project/downloading.php?group_id=260514&filename=parallel_spectral_deconvolution-1.9-src.zip)' released='27 September 2007' latest-version='11 April 2009' category='Deconvolution' website='http://sites.google.com/site/piotrwendykier/software/deconvolution/parallelspectraldeconvolution' %}

## Purpose

Parallel Spectral Deconvolution is an ImageJ plugin for spectral deblurring. This plugin takes advantage of multi-core processors.

## Documentation

The plugin code is based on the following book:

{% include citation doi='10.1137/1.9780898718874' %}

Please refer to the [website](http://sites.google.com/site/piotrwendykier/software/deconvolution/parallelspectraldeconvolution) for detail and examples.

## Introduction

### What is Deconvolution?

In applications such as astronomy, medicine, physics and biology, scientists use digital images to record and analyze results from experiments. Environmental effects and imperfections in the imaging system can cause the recorded images to be degraded by blurring and noise. Image deconvolution (sometimes known as image deblurring) is the process of reconstructing or estimating the true image from the degraded one. Image deblurring algorithms can be classified into two classes: spectral filtering methods and iterative methods. Other classification divides the algorithms into methods that do not require any information about the blur (also called blind deconvolution) and the methods that need that information. The information about the blur is usually given in the form of a point spread function (PSF). A PSF is an image that describes the response of an imaging system to a point object. A theoretical PSF can be obtained based on the optical properties of the imaging system. The main advantage of this approach is that the obtained PSF is noise-free. The experimental technique, on the other hand, relies on taking a picture of a point object, for example a distant star. In this work we assume that the PSF is known and given in the form of an image.

### What is Parallel Spectral Deconvolution?

The spectral filtering algorithms include many well known techniques for image deblurring such as Wiener filter and the pseudo inverse filter. But general approaches, such as truncated spectral decompositions and Tikhonov regularization also belong to this group. The key is to exploit the special structure of a PSF. For example, if fast Fourier transform (FFT) based methods are used (e.g., Wiener filter), then there is an implicit assumption that the blur is spatially invariant and that the original image scene is periodic (the so-called periodic boundary conditions). Other fast transforms, such as the discrete cosine transform (DCT) and the discrete sine transform (DST) can be used for other boundary conditions, but again these approaches only make sense if the blur is spatially invariant. Furthermore, in the case of using DCT and DST based methods, the PSF should be symmetric (as in the case of atmospheric turbulence). The advantage of using spectral filtering algorithms is that they can be very efficient, and they are fairly easy to implement. However, it is not possible to include additional constraints, such as nonnegativity, in this type of reconstruction methods.

Parallel Spectral Deconvolution is an ImageJ plugin for spectral image deblurring. The code is based on methods described in Deblurring Images: Matrices, Spectra, and Filtering by Per Christian Hansen, James G. Nagy, and Dianne P. O'Leary, SIAM, 2006. The current version implements Tikhonov- and TSVD-based image deblurring assuming either periodic of reflexive boundary conditions. Although the plugin can handle arbitrary-sized 2- and 3-dimensional images, its usage is limited to grayscale images. To deconvolve a color image, you would have to split the channels and deblur each channel separately.

## How to use

<figure><img src="/media/plugins/parallelspectraldeconvolutiondialog.jpg" title="ParallelSpectralDeconvolutionDialog.jpg" width="500" alt="ParallelSpectralDeconvolutionDialog.jpg" /><figcaption aria-hidden="true">ParallelSpectralDeconvolutionDialog.jpg</figcaption></figure>

There are seven drop-down lists (combo-boxes) available in the GUI. From the Image list, you can choose a blurred image. PSF list is for selection of a point spread function image. The content of these two lists depends on what is currently open in ImageJ - if no image windows are displayed then both lists are empty. The next two lists (Method and Stencil) allow you to choose an algorithm used for deconvolution (Generalized Tikhonov, Tikhonov or TSVD) and a stencil (for Generalized Tikhonov only). The stencil is used for creating a regularization matrix (an approximation of a derivative operator). A detailed explanation of all algorithms can be found in Deblurring Images: Matrices, Spectra, and Filtering. In the Resizing combo-box you can choose whether the blurred image will be padded to the next power-of-two size before processing. This feature is available mainly for performance reasons (FFT works faster when the size of the data is a power-of-two number). Note that if the size of each dimension of a blurred image is already a power-of-two number, then the image will not be padded even if the Next power of two option is selected. To display a padded image, the Show padded image check-box needs to be selected. The Output list is used to specify the type of an output (reconstructed image). Finally, in the Precision combo-box you can choose a floating-point precision used in computations. Practice shows that a single precision is sufficient for most problems.

There are few other important options in the GUI that require some explanation. The Threshold check-box and text field are used to remove a negative values from the solution (reconstructed image). Since it is not possible to impose nonnegativity constraints in the spectral algorithms, the threshold option is the only way to get a nonnegative solution. When the threshold option is enabled, then all values in the reconstructed image are that are less than the value specified in the threshold text field are replaced by zero. In the Max number of threads (power of 2) text field you can specify how many computational threads will be used. By default this value is equal to the number of CPUs available on your machine.

When deblurring an image, certain regularity conditions have to be enforced on the solution. The degree of regularization is determined by a regularization parameter that should be chosen carefully. Parallel Spectral Deconvolution has an option to automatically compute the value of a regularization parameter (Auto regularization parameter check-box). If this box is selected then the Generalized Cross-Validation algorithm is used (for details refer to Deblurring Images: Matrices, Spectra, and Filtering). Unfortunately, no parameter choice method is perfect, therefore it is possible to manually adjust the automatically computed value (Regularization parameter text field and slider). Once the initial deconvolution is finished, the Regularization parameter text field and slider, as well as the Update button are enabled. At this point, you can change the value of a regularization parameter either by using the slider or by entering a new value in the text field. The Update button is used to recompute the solution with the new value of a regularization parameter.

### How to Obtain a Theoretical PSF?

There are several ImageJ plugins for generating a theoretical point spread function:

-   [PSF Tool for ImageJ](http://www.mosaic.ethz.ch/downloads/psftool) by the ETH Computationnal Biophysics Lab
-   [Diffraction PSF 3D](/plugins/diffraction-psf-3d) by Robert Dougherty
-   [Deconvolution3D](http://bigwww.epfl.ch/demo/deconvolution3D/) by Pierre Besson.

To use these tools you need to know some parameters of your microscope setup and sample like NA, RI of mounting medium, wavelength, etc.

## 2D Example

After opening the image to deconvolve and the image of the PSF, start {% include bc path='Plugins | Deconvolution | 2D Spectral Deconvolution...'%}

<figure><img src="/media/plugins/parallelspectraldeconvolution2dexample.jpg" title="ParallelSpectralDeconvolution2DExample.jpg" width="800" alt="ParallelSpectralDeconvolution2DExample.jpg" /><figcaption aria-hidden="true">ParallelSpectralDeconvolution2DExample.jpg</figcaption></figure>

Clicking on the Deconvolve button results in this:

<figure><img src="/media/plugins/parallelspectraldeconvolution2dexampleresult.jpg" title="ParallelSpectralDeconvolution2DExampleResult.jpg" width="800" alt="ParallelSpectralDeconvolution2DExampleResult.jpg" /><figcaption aria-hidden="true">ParallelSpectralDeconvolution2DExampleResult.jpg</figcaption></figure>

## 3D Example

After opening the image to deconvolve and the image of the PSF, start {% include bc path='Plugins | Deconvolution | 3D Spectral Deconvolution...'%}

<figure><img src="/media/plugins/parallelspectraldeconvolution3dexample.jpg" title="ParallelSpectralDeconvolution3DExample.jpg" width="800" alt="ParallelSpectralDeconvolution3DExample.jpg" /><figcaption aria-hidden="true">ParallelSpectralDeconvolution3DExample.jpg</figcaption></figure>

Clicking on the Deconvolve button results in this:

<figure><img src="/media/plugins/parallelspectraldeconvolution3dexampleresult.jpg" title="ParallelSpectralDeconvolution3DExampleResult.jpg" width="800" alt="ParallelSpectralDeconvolution3DExampleResult.jpg" /><figcaption aria-hidden="true">ParallelSpectralDeconvolution3DExampleResult.jpg</figcaption></figure>

## See also

-   [Parallel Iterative Deconvolution](/plugins/parallel-iterative-deconvolution) by the same author, for another set of methods.

## Version history

-   1.0: September 28, 2007
    -   Initial release.

<!-- -->

-   1.1: January 6, 2008
    -   Fixed bug causing poor results in all 3D methods with reflexive boundary conditions.
    -   The plugin is updated to use Parallel Colt 0.2.
    -   Added benchmarks.

<!-- -->

-   1.2: February 15, 2008
    -   Added single precision.
    -   Added exceptions handling.

<!-- -->

-   1.3: February 27, 2008
    -   Memory optimization (all methods require less memory now).
    -   Added info displayed in the status bar.
    -   Changed the title of a deblurred image.

<!-- -->

-   1.4: March 1, 2008
    -   Added threshold option.

<!-- -->

-   1.5: March 11, 2008
    -   From now on Deconvolve, Update and Cancel buttons are disabled while deconvolution is in progress.
    -   From now on the main GUI window cannot be closed by using the button from the title bar.

<!-- -->

-   1.6: April 17, 2008
    -   The plugin is updated to use Parallel Colt 0.4.

<!-- -->

-   1.7: August 26, 2008
    -   Added support for macros.
    -   Memory optimization for single precision methods.
    -   Added javadoc distribution.
    -   Bzip2 is used to compress tar archives.
    -   The plugin is updated to use Parallel Colt 0.5.

<!-- -->

-   1.8: November 21, 2008
    -   Fixed bug in all FFT-based methods: a blurred image was padded reflexive instead of periodic.
    -   Added resizing option (an image does not need to be padded to the next power of two size).
    -   Added output option (a deblurred image is automatically converted to the chosen type).
    -   The plugin is updated to use Parallel Colt 0.6.

<!-- -->

-   1.9: April 11, 2009
    -   Added SpectralDeconvolver interfaces and abstract classes for 2D and 3D spectral algorithms.
    -   Default stencil for Generalized Tikhonov changed from Identity to Laplacian.
    -   Fixed bug causing NullPointerExceptinon when a blurred image or a PSF was renamed.
    -   Refactoring and cosmetic changes.
    -   The plugin is updated to use Parallel Colt 0.7.2.

 
