---
mediawiki: BigStitcher_Define_new_dataset
title: BigStitcher › Define New Dataset
nav-links: true
nav-title: Define New Dataset
---

When clicking {% include bc path='Plugins|BigStitcher| BigStitcher'%} in the the Fiji menu, it will open a macro-scriptable dialog that looks as following:

![](/media/plugins/bigstitcher/bigstitcher-import-exisitng-0.png)

{% include thumbnail src='/media/plugins/bigstitcher/bigstitcher-importer-1.png' title='Select the importer and the name of the xml file to save the metadata to.'%} In order to **define a new dataset**, please click the respective button on the left side of the dialog. This will open a new window in which you can define how to import the image data. Since there is huge variety of data formats produced by various microscopy companies and self-built setups, we developed multiple types of importers:

-   **[Automatic Loader (Bioformats)](/plugins/bigstitcher/autoloader)**

The Automatic Loader is a comprehensive importer that should work with most of image data. We highly suggest using this importer as a first choice, and just if you experience any problems to continue with one of the other options.

-   **[Manual Loader (Bioformats)](/plugins/bigstitcher/stackloader)**

The **Manual Loader (Bioformats)** can be used to import datasets that consist of several stacks that can be opened using LOCI Bioformats. Manual assignment of the stacks to Angles, Tiles or Illuminations according to patterns in the filename is necessary.

-   **[Manual Loader (TIFF only, ImageJ Opener)](/plugins/bigstitcher/stackloader)**

The **Manual Loader (TIFF only, ImageJ Opener))** can be used to import datasets that consist of several stacks that can be opened directly by ImageJ. Manual assignment of the stacks to Channels, Illuminations, Angles, Tiles or Illuminations according to patterns in the filename is necessary.

-   **[Zeiss Lightsheet Z.1 Dataset (Bioformats)](/plugins/bigstitcher/specialloaders)**

A single-purpose loader to import CZI-files produced by the **Zeiss Lightsheet Z.1 microscope**.

-   **[MicroManager diSPIM Dataset](/plugins/bigstitcher/specialloaders)**

A single-purpose loader to import **diSPIM** datasets produced by MicroManager.

*Note: Only one xml per directory is supported right now, even if they have a different filename.*

Go back to the [main page](/plugins/bigstitcher#documentation)
