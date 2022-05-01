---
mediawiki: DS4H_Image_Alignment
title: DS4H Image Alignment
categories: [Tutorials,Registration]
---


{% capture source%}
{% include github org='Luxor001' repo='DS4H-Image-Alignment' %}
{% endcapture %}
{% include info-box software='ImageJ' name='DS4H Image Alignment' maintainer='DS4H' author='Stefano Belli; Antonella Carbonaro; Filippo Piccinini' source=source released='08/06/2019' latest-version='13/08/2019' status='stable' category='Registration' %}

## Goal of the plugin

Align (i.e. co-register) 2D images

![](/media/plugins/ds4h-ia-modified-tsujikawacellreports2017.png)

## Description

"Data Science for Health (DS4H) Image Alignment" is a user-friendly tool freely provided as an ImageJ/Fiji plugin. With DS4H Image Alignment, 2D images can be easily aligned (i.e. co-registered) by defining with a few clicks some well visible reference marks.

The implemented least-squares method automatically approximates the solution of the mathematical overdetermined system, so to define the registration matrix then used for aligning the different images. It also considers rotations and scale changes in case of object dilation/shrink. Finally, it provides an iterative subroutine for a fine alignment, to easily reach a very good image co-registration quality.

## Implementation

DS4H Image Alignment has been implemented in Java as a plugin for ImageJ/Fiji. It works with ".svs" files, but also all the medical imaging formats included in the [Bio-formats](/formats/bio-formats) library.

## Download

DS4H Image Alignment is freely available, together with a sample dataset and a video tutorial.

To install DS4H Image Alignment follow the instructions reported on the Video Tutorial. Basically, you have to copy the DS4H Image Alignment ".jar" file in the plugins folder of Imagej/Fiji.

\- [ImageJ/Fiji plugin](https://sites.imagej.net/DS4H/plugins/jars/) (".jar" file), to be copied in the plugins folder of Imagej/Fiji.

\- [Sample dataset](http://filippopiccinini.altervista.it/TestAlignment_SameSampleDifferentChannels.zip) (1 MB), with a few images useful to test DS4H Image Alignment.

\- Video tutorial, to learn how to use DS4H Image Alignment.

{% include video platform='youtube' id='GliVW-g34EQ'%}

## Reference

Please, when using/referring to "DS4H Image Alignment" in a scientific work, cite:

"Jenny Bulgarelli, Marcella Tazzari\*, Anna Maria Granato, Laura Ridolfi, Serena Maiocchi, Francesco De Rosa, Massimiliano Petrini, Elena Pancisi, Giorgia Gentili, Barbara Vergani, Filippo Piccinini, Antonella Carbonaro, Biagio Eugenio Leone, Giovanni Foschi, Valentina Ancarani, Massimo Framarini, Massimo Guidoboni, "Dendritic cell vaccination in metastatic melanoma turns "non-T cell inflamed" into "T-cell inflamed" tumors". 2019."

## License

Copyright (C) 2019, the Data Science for Health (DS4H) group. All rights reserved.

Image Alignment and the material available on the Image Alignment website is licensed under the: GNU General Public License version 3

\- This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

\- This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

## Acknowledgments

We thanks all the University Students that helped in this project. In particular:

\- (2019) Stefano Belli, Master's Degree Student in Computer Sciences, University of Bologna, Italy, email: stefano.belli4@studio.unibo.it

## Contact Us

The Data Science for Health (DS4H) group:

\- Antonella Carbonaro, Department of Computer Science and Engineering (DISI), University of Bologna, Bologna, Italy, email: antonella.carbonaro@unibo.it

\- Filippo Piccinini, Istituto Scientifico Romagnolo per lo Studio e la Cura dei Tumori (IRST) IRCCS, Meldola (FC), Italy, email: filippo.piccinini@irst.emr.it

  
