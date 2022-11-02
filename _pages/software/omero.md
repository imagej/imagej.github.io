---
title: OMERO
section: Explore:Software
doi:
- 10.1038/nmeth.1896
- 10.1016/j.ymeth.2015.10.006
- 10.1007/s00335-015-9587-6
name: OMERO
icon: /media/logos/omero.png
team-developers: OME | https://www.openmicroscopy.org/
team-maintainers: OME | https://www.openmicroscopy.org/
source-url: https://github.com/ome/openmicroscopy
website: https://www.openmicroscopy.org/info/omero
---

OMERO is client-server software for visualization, management and analysis of biological microscope images.

## Interacting with OMERO from ImageJ

There are several different ImageJ-based tools for working with data from an OMERO database:

### OMERO plugin for Fiji/ImageJ

The [OME project](https://openmicroscopy.org/) has developed the **OMERO plugin for Fiji/ImageJ**. Read about it at:

{% include link-banner url="https://omero-guides.readthedocs.io/en/latest/fiji/docs/" %}

For versions of OMERO prior to 5.5, OME's plugin for ImageJ was known as **OMERO.insight-ij**.

### ImageJ-OMERO

The [ImageJ2 team](/people) has developed [ImageJ-OMERO](https://github.com/imagej/imagej-omero), a SciJava-based library for bidirectional interoperability between [ImageJ2](/software/imagej2) and OMERO, with plugins to upload and download images, tables, and regions of interest to and from OMERO, and support for running ImageJ scripts on the OMERO server side.

ImageJ-OMERO is accessed via a collection of `OMERO x.x` [update sites](/list-of-update-sites) specific to the OMERO server version you are connecting to.

### GReD/MICA plugins

The [GReD](https://www.gred-clermont.fr/) research center and [Microscopie Imagerie Côtes d'Azur](https://univ-cotedazur.fr/mica) have collaboratively developed some tools for interacting with OMERO from ImageJ:

1. [omero\_batch-plugin](https://github.com/GReD-Clermont/omero_batch-plugin): a plugin to batch process images from OMERO with a script or macro
2. [omero\_macro-extensions](https://github.com/GReD-Clermont/omero_macro-extensions): a plugin to interface with OMERO directly from macros through macro-extensions
3. [simple-omero-client](https://github.com/GReD-Clermont/simple-omero-client): a wrapper library which can be called from scripts in Fiji, but can mostly be used in Maven projects to wrap calls to the underlying [OMERO Java Gateway](https://github.com/ome/omero-gateway-java) (API available [here](https://api.igred.fr/simple-omero-client/))

The omero\_batch-plugin plugin gives users a GUI to help them process images from OMERO or a local folder (with bio-formats) with a script of their choosing, and save results locally or on OMERO.

![batch-omero-plugin dialog](https://aws1.discourse-cdn.com/business4/uploads/imagej/optimized/3X/e/f/ef69a367bcccb225e2428a38600d71d77eee2ee4_2_1380x872.gif){:width="600px"}

The omero\_macro-extensions plugin adds new [macro](/scripting/macro) functions to access data on OMERO directly from macros. For example:

```javascript
run("OMERO Extensions");
Ext.connectToOMERO(host, port, username, password);
images = Ext.list("images", "dataset", dataset_id);
image_ids = split(images,",");
imageplusID = Ext.getImage(image_ids[0]);
```

The simple-omero-client is a [Maven](/develop/maven) library, on which the omero\_batch-plugin and omero\_macro-extensions are built. It is therefore required to run these. However, once installed in Fiji, its API then becomes available for modern scripts.

Instructions for the plugins installation are on their respective release page, and their READMEs should describe how to use them, although this could be improved.

See the [publication preprint](https://f1000research.com/articles/11-392/v1) for further details.

## Publications

{% include citation %}
