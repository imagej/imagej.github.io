---
mediawiki: Register_Virtual_Stack_Slices
title: Register Virtual Stack Slices
project: /software/fiji
categories: [Registration,TrakEM2]
artifact: sc.fiji:register_virtual_stack_slices
---

{\| \|style="vertical-align:top" \|<img src="/media/rvs-scheme.png" title="fig:Register Virtual Stack scheme - All images are transformed to match the reference" width="380" alt="Register Virtual Stack scheme - All images are transformed to match the reference" /> \|}

This plugin takes a sequence of image slices stored in a folder, and delivers a list of registered image slices (with enlarged canvas). One of the images in the sequence can be selected by the user as **reference** and it will remain intact.

The plugin can perform*' 6 types of image registration techniques*':

-   Translation
-   Rigid (translation + rotation)
-   Similarity (translation + rotation + isotropic scaling)
-   Affine
-   Elastic (via [ bUnwarpJ](/plugins/bunwarpj) with cubic B-splines)
-   Moving least squares

All models are aided by automatically extracted [ SIFT features](/plugins/feature-extraction).

## User Manual

<b>Premises</b>:  

-   **Source folder**: You have a folder with an ordered list of image files in it that ImageJ can open.
-   Each image represents a slice in a sequence.
-   **Output folder**: You have or create a folder to store the resulting virtual stack with the aligned images.

Images may have different dimensions and be of different type.

<b>Step 1</b>: launch the "Plugins - Registration - Register Virtual Stack Slices" plugin.

{% include img src="rvs-main-window" width="400" caption="Register Virtual Stack main window" %}

<b>Step 2</b>: choose the appropriate options:  

-   **Select a source folder** containing the slices, at one slice per image file.
-   **Select the output folder** where resulting registered slices are automatically stored as TIFF files.
-   **Feature extraction model**. The expected transformation model finding inliers (i.e. correspondences or landmarks between images) in the feature extraction: translation, rigid, similarity or affine.
-   **Registration model**. The image transformation model: translation, rigid, similarity, affine, elastic or moving least squares.
-   **Advanced setup**. The advanced checkbox: whether to see the [ feature extraction parameters](/plugins/feature-extraction#parameters) setup dialog, and if elastic, the [ bUnwarpJ](/plugins/bunwarpj) dialog. Otherwise the plugin operates on reasonable, default parameters.
-   **Shrinkage constrain**. Option to regularize the registration in order to avoid section shrinking.
-   **Save transforms**. Option to save the resulting transforms into files, that can be loaded using [Transform Virtual Stack Slices](/plugins/transform-virtual-stack-slices).

<b>Step 3</b>: choose the **reference** image (only if the "Shrinkage constraint" checkbox was not marked):  

-   Select one of the images from the source folder as the reference image.

On success, a virtual stack will open showing all the registered images contained in the target folder. The virtual stack can be closed with no ill effect: images are saved in the target folder.

### Shrinkage constrain

{% include thumbnail src='/media/plugins/rvs-shrink-option.png' title='Shrinkage constrain checkbox'%} Since the 09/13/2009 version and thanks to [Daniel Berger](http://hebb.mit.edu/), Register Virtual Stack Slices has the option of constraining the registration to avoid section shrinking for large sets of images.

If this option is used, **no reference image needs to be selected**. All images will be transformed into the same common space by initializing first the system with a rigid transformation and then relaxing it based on the desired registration model.

To do so, in the main dialog, you have to check the "Shrinkage constrain" option (see attached window).

If you check as well the "Advance setup" checkbox from the same dialog, then a new window will appear to select the corresponding parameters to regularize the section shrinkage based on the properties of the transformation. If we choose "affine" as registration model, then we will be able to regularize: {% include thumbnail src='/media/plugins/rvs-regularization-params.png' title=' Shrinkage regularization parameters'%}

-   the {% include wikipedia title='Shear mapping' text='shear'%},
-   the {% include wikipedia title='Scaling (geometry)' text='scaling'%},
-   and the {% include wikipedia title='Isotropy' text='isotropy'%} or aspect ratio.

For the registration models "translation" and "rigid", no regularization is needed since these linear transformations don't apply. In the case of the "similarity" registration model, only the shearing and scaling will be regularized.

**TODO**: the "elastic" and "moving least squares" registration models do not have a proper shrinkage regularization implementation yet.

In the case of the "elastic" model, only a rigid registration will be performed. If you need to regularize the elastic transformation between the sections, you better do it through the bUnwarpJ paramters (see [ Notes](/plugins/register-virtual-stack-slices#notes) below).

For the "moving least squares" model, the maximal warping will still take place with no regularization.

We can visualize the relaxation of the system into the desired registration model by checking the option "Display relaxation graph". In this graph the average mean squared error (MSE) between the correspondences of the whole sequence of slices is displayed for each relaxation iteration.

### Save Transforms

Since the 09/24/2009 version, the plugin has the option to store the resulting transforms into files. This way, the results can be reproduce later on the same images or on a difference sequence by using the plugin [Transform Virtual Stack Slices](/plugins/transform-virtual-stack-slices).

To save the transforms, you just have to click on the "Save transforms" check-box of the main dialog. Then, after selecting the source and output directories, a new dialog will pop up to select the folder to store the transforms in.

The transforms are saved as **.XML** files, following [TrakEM2](/plugins/trakem2) format.

### Notes

1.  The plugin is multithreaded: more CPU cores means faster execution.
2.  The two most relevant parameters in the [ SIFT feature extraction](/plugins/feature-extraction) are:  
    -   <b>maximum image size</b>, which limits the low-end size of the features (i.e. decrease maximum image size to increase the size of the smallest features to extract.)
    -   <b>inlier ratio</b>, which determines when to reject the intersection set of feature correspondences between two images (ratio between correspondent features vs. all extracted features.)
3.  All types of images are accepted (8-bit, 16-bit, 32-bit and RGB) but only in .tif, .jpg, .png, .gif, .tiff, .jpeg, .bmp, .pgm, or .ima format. Output images are saved as TIFF.
4.  If you selected the "Advanced setup" and "Elastic" as registration model, another window to adjust the elastic registration parameters will be shown.

{% include img src="rvs-elastic-options-351x446" width="280" caption="Elastic registration options" %}

This is actually a reduced version of the [ bUnwarpJ](/plugins/bunwarpj) main window.

Briefly, the options are:

-   **Registration mode**: "Mono", "Accurate" or "Fast". "Mono" means unidirectional registration and its actually the fastest of the three modes. "Accurate" and "Fast" perform bidirectional registration and take more time.
-   **Image Subsampling factor**: the image scaling factor from 2⁰ (1) to 2⁷ (128). We recommend to use it if the images are very large.
-   **Initial and Final deformations**: from "Very Coarse" to "Very Fine" or "Super Fine". They define the number of B-spline coefficients in the deformation grid (from 2x2 to 16x16). More coefficients mean more precision but also the possibility of over-registering.
-   **Divergence and curl weights**. They regularize the deformation to make it smooth.
-   **Landmark weight**: relevance of adjusting the correspondences found in the feature extraction.
-   **Image weight**: relevance of the similarity between source and target image in the energy function.
-   **Consistency weight**: relevance of the consistency error between the direct and inverse deformations (only for "Accurate" or "Fast" modes).
-   **Stop threshold**: difference between the last and previous algorithm iterations that makes the registration to end.

For a complete description of the elastic parameters, please visit the [FAQ of the original website](http://biocomp.cnb.csic.es/~iarganda/bUnwarpJ/faq.html).

</ol>

## Examples

Example of registration results using the shrinking constraint:

<table>
<tr>
<td>

<b>Raw:</b>

</td>
<td>

<b>Registered:</b>

</td>
</tr>
<tr>
<td>

![input data](/media/plugins/rvs-tem-example.gif)

</td>
<td>

![output data](/media/plugins/rvs-registered-tem.gif)

</td>
</tr>
</table>

Even this sequence of rather noisy transmission electron microscopy images, with considerable variations from slice to slice, got registered properly:

  

<table>
<tr>
<td>

<b>Raw:</b>

</td>
<td>

<b>Registered:</b>

</td>
</tr>
<tr>
<td>

![](/media/plugins/stack4.gif)

</td>
<td>

![](/media/plugins/stack4-2.gif)

</td>
</tr>
</table>

## API documentation

The latest documentation of the package can be found here:

[https://fiji.sc/javadoc/register_virtual_stack/package-summary.html](https://fiji.sc/javadoc/register_virtual_stack/package-summary.html)

## Scripting / PlugIn

You can call the plugin in a non-interactive fashion from a jython script:

    from register_virtual_stack import Register_Virtual_Stack_MT

    # source directory
    source_dir = "/path/to/source/"
    # output directory
    target_dir = "/path/to/target/"
    # transforms directory
    transf_dir = "/path/to/transforms/"
    # reference image
    reference_name = "reference_image"
    # shrinkage option (false)
    use_shrinking_constraint = 0

    p = Register_Virtual_Stack_MT.Param()
    # The "maximum image size":
    p.sift.maxOctaveSize = 1024
    # The "inlier ratio":
    p.minInlierRatio = 0.05

    Register_Virtual_Stack_MT.exec(source_dir, target_dir, transf_dir, 
    reference_name, p, use_shrinking_constraint)

## See also

-   [Transform Virtual Stack Slices](/plugins/transform-virtual-stack-slices), to see how to load the saved transforms.
-   [FloatArray2DSIFT.java](https://fiji.sc/cgi-bin/gitweb.cgi?p=mpicbg.git;a=blob;f=mpicbg/imagefeatures/FloatArray2DSIFT.java;hb=HEAD) which contains the subclass Param which is the 'sift' member of the `Register_Virtual_Stack_Slices.Param` subclass.
-   {% include github org='fiji' repo='register_virtual_stack_slices' branch='master' source='register_virtual_stack/Register_Virtual_Stack_MT.java' label='Register\_Virtual\_Stack\_MT.java' %}, including the Param subclass.
-   [Elastic Alignment and Montage plugin](/plugins/elastic-alignment-and-montage), for elastic registration/montage of large datasets using spring meshes (local deformations).

## References

The algorithm implemented for elastic registration ([bUnwarpJ](/plugins/bunwarpj)) and its technical explanations are detailed on the paper:

-   I. Arganda-Carreras, C. O. S. Sorzano, R. Marabini, J.-M. Carazo, C. Ortiz-de Solorzano, and J. Kybic, ["Consistent and Elastic Registration of Histological Sections using Vector-Spline Regularization,"](http://biocomp.cnb.uam.es/~iarganda/bUnwarpJ/downloads/arganda_carreras_CVAMIA06.pdf) Lecture Notes in Computer Science, Springer Berlin / Heidelberg, volume 4241/2006, CVAMIA: Computer Vision Approaches to Medical Image Analysis, pages 85-95, 2006.

## License

This program is **free software**; you can redistribute it and/or modify it under the terms of the **GNU General Public License** as published by the Free Software Foundation ([http://www.gnu.org/licenses/gpl.txt](http://www.gnu.org/licenses/gpl.txt)).

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

------------------------------------------------------------------------

  
