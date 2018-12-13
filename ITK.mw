{{Infobox
| name                   = ITK
| software               = ITK
| logo                     = [[File:Itk-logo.png|96px]]
| author                 = [http://itk.org/ Insight Software Consortium]
| maintainer             = [http://itk.org/ Insight Software Consortium]
| source                 = {{GitHub | org=InsightSoftwareConsortium | repo=ITK}}
| status                 = Active
| website                = http://itk.org/
}}The Insight Toolkit (ITK) is a cross-platform, [[open-source]] application development framework widely used for the development of image [[segmentation]] and image registration programs.

=ITK integration with ImageJ=

Although ITK is a C++ application, many ITK functions are available in ImageJ through the [http://www.simpleitk.org/ SimpleITK] Java compatibility layer.

Enabling this functionality in ImageJ is simply a matter of turning on the {{ListOfUpdateSites|ImageJ-ITK update site}}. Note that this will trigger a large download, as it requires the SimpleITK native library (up to a few hundred MB).

==What's on the update site?==

SimpleITK 0.90 is distributed with this update.  After update all SimpleITK classes can be called from the script editor. 

When using <code>@itkImage</code> [[Script_parameters|parameters]] in scripts, ImageJ <code>Dataset</code> objects will be automatically converted to SimpleITK <code>Image</code> objects.

There are several templates in the [[Script Editor]] demonstrating ITK use. The following example shows how to perform Otsu multilevel threshold using SimpleITK.

<source lang="python">
# @itkImage image
# @OUTPUT Dataset output

from org.itk.simple import OtsuMultipleThresholdsImageFilter

otsu = OtsuMultipleThresholdsImageFilter()

# call otsu using simple itk wrapper
output = otsu.execute(image, 2, 0, 255, True)
</source>

==Developer resources==
* [https://github.com/imagej/imagej-itk/ GitHub (we welcome pull requests)]
* [https://github.com/imagej/imagej-itk/tree/master/src/main/java/net/imagej/itk/ops An ImageJ2 Op that uses SimpleITK]
* [https://github.com/imagej/imagej-itk/tree/master/src/main/java/net/imagej/itk/commands An ImageJ2 command (plugin that adds a menu item) for the Op.]

== Publication ==

To cite ITK, please use the following publication:
* {{Publication|ITK}}

See also:
* [https://itk.org/Wiki/ITK/FAQ#How_do_I_cite_the_use_of_ITK_in_a_publication.3F How do I cite the use of ITK in a publication?]

[[Category:Related Software]]
[[Category:Citable]]
