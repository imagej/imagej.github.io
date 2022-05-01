---
mediawiki: Vessel_Analysis
title: Vessel Analysis
categories: [Uncategorized]
---


{% capture author%}
Nivetha Govindaraju, {% include person id='mfarna' %}
{% endcapture %}

{% capture maintainer%}
{% include person id='mfarna' %} (<mai.elfarnawany@gmail.com>)
{% endcapture %}
{% include info-box name='Vessel Analysis' software='Fiji' author=author maintainer=maintainer filename=' [Vessel Analysis.zip](/media/plugins/vessel-analysis.zip)' released='June 14<sup>th</sup>, 2016' latest-version='1.1' status='stable' category='Plugins, Analysis' %}

## **Description:**

Vessel Analysis is a plugin to automatically calculate vascular density metrics: - vascular density = vessel area/total area \* 100% - vascular length density = skeletonized vessel area/total area \* 100%)

as well as making diameter measurements for multiple vessels in RGB images of vascular networks. It can also be used on any images of branching structures.

## **Installation:**

Vessel Analysis can be added to Fiji (version 1.47g or higher required).

Download the [Vessel Analysis.zip](/media/plugins/vessel-analysis.zip) package and save an unzipped copy in Fiji's Plugins folder. Open a new session in Fiji and you should now see Vessel Analysis listed near the bottom of the Plugins drop down menu.

Before using the plugin, make sure your version of Fiji comes pre-downloaded with the Auto Threshold and Geometry to Distance plugins. They should be listed under:
* {% include bc path="Image | Adjust | Auto Threshold" %}
* {% include bc path="Analyze | Local Thickness | Geometry to Distance Map" %}

Also make sure you install [Mexican Hat Filter](https://imagej.nih.gov/ij/plugins/mexican-hat/index.html) plugin

## **Usage:**

Detailed Instructions [HERE](/media/plugins/vessel-analysis-user-manual.pdf)

Open a multi-channel image in Fiji and execute the Vessel Analysis plugin via {% include bc path="Plugins | Vessel Analysis | Vessel Analysis (complete)" %}. The "complete" program will guide you through preprocessing steps to prepare the image for vascular density and diameter measurements.

*Using the Plugin: Pre-processing*

You may skip directly to {% include bc path="Vessel Analysis | Vascular Density or Vessel Analysis | Diameter Measurements" %} if you already have the appropriate pre-processed image.

As the image is processed, new images will be generated and automatically saved in the source directory of the original image. You may re-use these images for future processing.

*Vessel Analysis (complete)* Using the rectangular selection tool, you will be asked to select the image area you would like to analyze. Once complete, click OK. A cropped image will be generated, followed by its binary version. The following measurements will be collected using this binary image.

*Choose a metric...*

You will now be prompted to perform either vascular density or diameter measurements. At the end of each individual program, you can choose to analyze the other metric as well.

![](/media/plugins/vessel-analysis-rgb.png) ![](/media/plugins/vessel-analysis-binary.png) ![](/media/plugins/vessel-analysis-diameterm.png)

## **Recommended Citation:**

Elfarnawany, Mai H., "Signal Processing Methods for Quantitative Power Doppler Microvascular Angiography" (2015). Electronic Thesis and Dissertation Repository. 3106.

## **Other Studies Used and Cited Vessel Analysis:**

Teplyi V, Grebchenko K, Evaluation of the scars' vascularization using computer processing of the digital images., Skin Res Technol. 2019 Mar;25(2):194-199.

Yvette Zarb et al, Ossified blood vessels in primary familial brain calcification elicit a neurotoxic astrocyte response, Brain, Volume 142, Issue 4, April 2019, Pages 885–902.

Said SS et al., Fortifying Angiogenesis in Ischemic Muscle with FGF9-Loaded Electrospun Poly(Ester Amide) Fibers., Adv Healthc Mater. 2019 Apr;8(8):e1801294.
