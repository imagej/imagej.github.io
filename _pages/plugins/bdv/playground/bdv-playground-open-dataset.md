---
title: 1 - Create/open
artifact: sc.fiji:bigdataviewer-playground
nav-links: true
toc: true
---

Several options are available. Note that there's a difference between opening and visualising an image. Images opened in bigdataviewer-playground are not visualized directly, but are sorted into a hierarchical tree displayed into an extra window. From this tree, images can be displayed using the right click contextual menu (see next section).

## Open a XML BDV Dataset

A BigDataViewer dataset is an xml file which links to raw data and which contains additional metadata (positions, voxel size, channel descriptions etc.). These datasets can be generated by other BigDataViewer plugins such as BigStitcher, and bigdataviewer playground also provides a way to generate an xml bdv dataset. 

Such datasets can be opened in bigdataviewer playground either via the command:

`Plugins › BigDataViewer-Playground › BDVDataset › Open XML BDV Datasets` 

(type *open xml bdv* into the search bar) or can be directly dragged and dropped into the bigdataviewer playground window (this window can be made visible with `Plugins › BigDataViewer-Playground › Show Bdv Playground Window`).

An xml bdv dataset contains the information used to load the images ([the backend](https://youtu.be/LHI7vXiUUms?t=521)). The most used backend for bigdataviewer is the [XML/HDF5](/plugins/bdv/#exporting-datasets-for-the-bigdataviewer) backend, but others exist ([N5](https://github.com/bigdataviewer/bigdataviewer-core/blob/-/src/main/java/bdv/img/n5/XmlIoN5ImageLoader.java), Tiff, [Remote](https://github.com/bigdataviewer/bigdataviewer-core/blob/-/src/main/java/bdv/img/remote/XmlIoRemoteImageLoader.java), [Imaris](https://github.com/bigdataviewer/bigdataviewer-core/blob/-/src/main/java/bdv/img/imaris/XmlIoImarisImageLoader.java)...). BigDataViewer Playground actually adds several backends which can facilitates the definitation of bio-formats, omero images, and QuPath projects into a bdv xml dataset.

## Open a set of Bio-Formats supported files as a BDV Dataset

Files (multi-series, multi-resolution) can be opened via the plugin:

`Plugins › BigDataViewer-Playground › BDVDataset › Open [BioFormats Bdv Bridge (Basic) (Legacy)]`

(to avoid going through all the hierarchy of Fiji's menu, you can directly type *bridge* into Fiji's search bar)

Many files can be included in a single dataset.

{% include img name="open with bioformats bdv bridge" src="/media/plugins/bdv/playground/bdvpg-bioformats-bridge-basic-open.png" %}

Note that this WSI dataset demo-ed in this documentation is [accessible from Zenodo](https://zenodo.org/record/6553641#.YuD7ioRBxD8).

## Open a QuPath project as a BDV Dataset

As long as the QuPath project uses Bio-Formats image server, the project can be translated into a BigDataViewer dataset and be opened directly with the plugin: 

` Plugins › BigDataViewer-Playground › BDVDataset › Create BDV Dataset [QuPath]`

## Open images from a BigDataServer as a BDV Dataset

You can use:

`Plugins › BigDataViewer-Playground › BDVDataset › BDVDataset [BigDataServer]`

## Open an Imaris file as a BDV Dataset

You can use:

`Plugins › BigDataViewer-Playground › BDVDataset › Create BDV Dataset [Imaris]`

## Open OMERO images as a BDV Dataset

You can use:
`Plugins › BigDataViewer-Playground › BDVDataset › Create BDV Dataset [OMERO]`

You will be asked for your credentials. Note that there is a limitation currently which [prevents the opening of images that are not located in your default group](https://github.com/imagej/imagej-omero/issues/117). 

## Import the current ImageJ image as a BDV Dataset

Similar to the command ` Plugins>BigDataViewer>Open Current Image`, it is possible to import the current ImageJ image as an image in the bigdataviewer playground hierarchical tree via the command:

`Plugins › BigDataViewer-Playground › Sources › Import › Make BDVDataset from current IJ1 image`

It is possible to save it as an XML BDV dataset as well.

## Save a BDV Dataset as an XML BDV Dataset

Any dataset created using the functions above can be saved as an XML BDV Dataset. No image data will be written, but a XML File containing the dataset information can be written and re-used as explained in the next paragraph.

To save a BDV Dataset, first you need to open it, using one of the options above. Then you can save it (or resave it) via:

`Plugins › BigDataViewer-Playground › BDVDataset › Save BDVDataset`

Specify the sources to save and a xml file path. If the sources you selected belong to a BDV dataset, this command will be able to save it.













