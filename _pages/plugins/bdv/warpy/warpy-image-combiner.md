---
title: Warpy Image Combiner
artifact: ch.epfl.biop:bigdataviewer-biop-tools
nav-links: true
toc: true
---

**ImageCombinerWarpy** is a QuPath extension for the non-linear overlay of whole slide images.

It is based on the [ImageCombiner](https://forum.image.sc/t/qupath-scripting-4-image-combiner-register-images-and-create-project-entry/50484).
In addition to the affine transformation used in the ImageCombiner, the ImageCombinerWarpy uses the [Warpy extension](/plugins/bdv/warpy/warpy-extension) to combine registered whole slide images.

Whole slide images aligned with Warpy can be combined to a new QuPath image entry.

Multiple images can be selected and overlaid.
The only condition is that Warpy transform files exist for all overlay images, and that all overlay images have been transformed to the same base image.

(Combinations of affine transformations and Warpy transformations are not possible.)

{% include notice icon="warning"
  content="Please read the notes at the end of the document carefully!" %}

# Installation
      
**ImageCombinerWarpy** is included in the BIOP EPFL QuPath Warpy extension.

Please look at the installation instructions in the [warpy-extension](/plugins/bdv/warpy/warpy-extension)

# Usage / Application

In the QuPath menu you will find the new entry `Analyze>ImageCombinerWarpy` .


{% include img name="Warpy image combiner menu" src="/media/plugins/bdv/warpy/warpy_ic_menu.png" %}

Open your QuPath project for which you created the Warpy transform.
Open your fixed/base image in the viewer.

Before starting ImageCombinerWarpy, **make sure that your base image viewer is selected!** (The image used as **fixed** image in the Warpy procedure **MUST** be the **base** image in ImageCombiner!)

{% include img name="Fixed image selected" src="/media/plugins/bdv/warpy/warpy_ic_fixed_image_selected.png" %}

Open ImageCombinerWarpy and choose an overlay image from your project.

{% include img name="Images to include" src="/media/plugins/bdv/warpy/warpy_ic_images_to_include.png" %}

Select the overlay image in the image list.
In the ‘Warpy Info’ section you should see the ID of the image and - if present in the project data folder - the Warpy transform file.

{% include img name="Transform file is visible" src="/media/plugins/bdv/warpy/warpy_ic_transform_file.png" %}

Click the ‘Warpy’ command to create the new, permanent project entry with the image overlay.
(The Warpy command is **ONLY** active if Warpy transform file exists for all overlay images.)

{% include notice icon="info"
  content="It is possible to combine only certain image channels in the warped image.
To do this, adjust the Brightness&Contrast settings as well as the channel selection for all images (base or overlay image) displayed in a separate viewer before using the ‘Warpy’ command.
Further information is described in [Additional Information](/plugins/bdv/warpy/warpy-image-combiner-additional-info)." %}

{% include img name="Combined image visible" src="/media/plugins/bdv/warpy/warpy_ic_combined_image_view.png" %}

Use the Brightness&Contrast dialog to select the color channels and display settings of the new image.

{% include img name="Combined image visible and contrast adjusted" src="/media/plugins/bdv/warpy/warpy_ic_combined_image_bc_adjusted.png" %}

{% include notice icon="warning"
  content="**I** - The ImageCombinerWarpy is thought as an experimental tool.
It is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE." %}

{% include notice icon="warning"
  content="**II** - Images in QuPath project entries, created with ImageCombinerWarpy, may not show the pixel contents of the original images! The pixel difference between the original and the transformed image depends on the transformation, the used interpolation as well as the downsampling used in the current viewer.
This must be taken into account in all analysis steps performed on such transformed images." %}

{% include notice icon="warning"
  content="**III** - The Warpy transformation is based on a special TransformingImageServer class provided via a QuPath Extension package.
Additionally, the Warpy transformation is based on slide-specific information regarding spatial deformation in Json format.
Should the extension or format of the transformation information change in future versions, or should one of these two important components not be present, old projects may no longer load or may not load correctly.
It is therefore strongly recommended to save the images created with ImageCombinerWarpy and thus make them independent of the ImageCombinerWarpy extension and the Warpy transformation." %}

# Additional information

[Additional Information](/plugins/bdv/warpy/warpy-image-combiner-additional-info) 
