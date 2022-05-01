---
mediawiki: VisBio_Fiji_plugin
title: VisBio Fiji plugin
categories: [Uncategorized]
---


{% capture maintainer%}
{% include person id='ctrueden' %}
{% endcapture %}

{% capture source%}
{% include github org='uw-loci' repo='visbio-imagej' %}
{% endcapture %}
{% include info-box name='VisBio- orthogonal projection plugin' software='ImageJ - Fiji - ImgLib' author='Curtis Rueden, Melissa Linkert, Eric Kjellman' maintainer=maintainer filename='visbio.jar' source=source latest-version='Jan 2014' website='Fiji' status='Beta. Under development, but stable enough for real work.' %}

## What is the VisBio Plugin?

The VisBio Ortho Stack plugin is a simple 3D visualization plugin for Fiji that displays a stack of image planes in a parallel or perspective projection along the z plane. The plugin can control several common operations, such as specifying distance between cross sections, rotating and zooming the RD view, and saving a snapshot of the current image to a file.

## Updating the VisBio Plugin

The VisBio Plugin is located within the LOCI updates. To learn more on how to update plugins, visit the update fiji page. To update the VisBio Plugin:

-   Select {% include bc path='Help | Update Fiji'%}
-   Once the ImageJ Updater is presented, select "Manage Update sites"
-   Select the "/orgs/loci" site to update all LOCI plugins, including VisBio
-   Close "Manage Update Sites" and select "Apply changes"
-   Restart ImageJ and the update will be in effect

## Using VisBio

To use VisBio you must first import an Image Sequence. To do so, Select {% include bc path='File | Import | Image Sequence'%} and select the file of images you wish to use.

After you have your images imported, follow the following directions: 

-   Select the imported image sequence
-   Select {% include bc path='Plugins | VisBio | Ortho Stack'%}
-   To display every individual image within the view, unselect "Parallel projection"
-   To compact the images, decrease the amount of stretch within the stack

%GALLERY% Top_of_stack.png|The first image within the Ortho Stack Bottom_of_stack.png| Last image in the Ortho Stack Stack_cross_section.png| A cross sectional view of the Ortho Stack %GALLERY%
