---
title: VisBio Ortho Stack
categories: [Visualization]
source-url: https://github.com/uw-loci/visbio-imagej
pom-url: https://raw.githubusercontent.com/uw-loci/visbio-imagej/master/pom.xml
update-site: LOCI
---

The VisBio Ortho Stack plugin is a simple 3D visualization plugin for Fiji that displays a stack of image planes in a parallel or perspective projection along the z plane. The plugin can control several common operations, such as specifying distance between cross sections, rotating and zooming the RD view, and saving a snapshot of the current image to a file.

## Updating the VisBio Plugin

The VisBio Plugin is part of the LOCI update site:

-   Select {% include bc path='Help | Update Fiji'%}
-   Once the ImageJ Updater is presented, select "Manage Update sites"
-   Select the "/orgs/loci" site to update all LOCI plugins, including VisBio
-   Close "Manage Update Sites" and select "Apply changes"
-   Restart ImageJ and the update will be in effect

## Using VisBio

To use the VisBio Ortho Stack plugin, you must first open an image stack. For example, you could use {% include bc path='File | Import | Image Sequence' %} and select the folder of images you wish to use.

After you have your image stack imported, follow the following directions:

-   Select the imported image sequence
-   Select {% include bc path='Plugins | VisBio | Ortho Stack' %}
-   To display every individual image within the view, unselect "Parallel projection"
-   To compact the images, decrease the amount of stretch within the stack

{% include img src="top-of-stack" caption="The first image within the Ortho Stack" width=296 %}
{% include img src="bottom-of-stack" caption="Last image in the Ortho Stack" width=249 %}
{% include img src="stack-cross-section" caption="A cross sectional view of the Ortho Stack" width=350 %}
