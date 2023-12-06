---
mediawiki: ITK
name: "ITK"
title: ITK
section: Explore:Software
doi: 10.3233/978-1-60750-929-5-586
website: "http://itk.org/"
dev-status: "Active"
icon: /media/logos/itk.png
source-url: https://github.com/InsightSoftwareConsortium/ITK
team-maintainer: "Insight Software Consortium | http://itk.org/"
forum-tag: itk
---

The Insight Toolkit (ITK) is a cross-platform, [open-source](/licensing/open-source) application development framework widely used for the development of image [segmentation](/imaging/segmentation) and image registration programs.

# ITK integration with ImageJ

Although ITK is a C++ application, many ITK functions are available in ImageJ through the [SimpleITK](http://www.simpleitk.org/) Java compatibility layer.

Enabling this functionality in ImageJ is simply a matter of turning on the [ImageJ-ITK update site](/list-of-update-sites). Note that this will trigger a large download, as it requires the SimpleITK native library (up to a few hundred MB).

## What's on the update site?

SimpleITK 0.90 is distributed with this update. After update all SimpleITK classes can be called from the script editor.

When using `@itkImage` [parameters](/scripting/parameters) in scripts, ImageJ `Dataset` objects will be automatically converted to SimpleITK `Image` objects.

There are several templates in the [Script Editor](/scripting/script-editor) demonstrating ITK use. The following example shows how to perform Otsu multilevel threshold using SimpleITK.

```java
# @itkImage image
# @OUTPUT Dataset output

from org.itk.simple import OtsuMultipleThresholdsImageFilter

otsu = OtsuMultipleThresholdsImageFilter()

# call otsu using simple itk wrapper
output = otsu.execute(image, 2, 0, 255, True)
```

## Developer resources

-   [GitHub (we welcome pull requests)](https://github.com/imagej/imagej-itk/)
-   [An ImageJ2 Op that uses SimpleITK](https://github.com/imagej/imagej-itk/tree/-/src/main/java/net/imagej/itk/ops)
-   [An ImageJ2 command (plugin that adds a menu item) for the Op.](https://github.com/imagej/imagej-itk/tree/-/src/main/java/net/imagej/itk/commands)

## Publication

To cite ITK, please use the following publication:

{% include citation %}

See also:

-   [How do I cite the use of ITK in a publication?](https://itk.org/Wiki/ITK/FAQ#how-do-i-cite-the-use-of-itk-in-a-publication)
