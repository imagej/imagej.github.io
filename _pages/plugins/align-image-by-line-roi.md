---
mediawiki: Align_Image_by_line_ROI
title: Align Image by line ROI
categories: [Tutorials,Registration]
---


{% capture maintainer%}
{% include person id='dscho' %}
{% endcapture %}

{% capture source%}
{% include github org='fiji' repo='VIB' source='Align\_Image.java' %}
{% endcapture %}
{% include info-box software='ImageJ' name='Align Image by line ROI' maintainer=maintainer author='Johannes Schindelin' source=source released='28/09/2006' latest-version='28/09/2006' status='stable, handles only gray images' category='Registration' %}

This plugin aligns an image to another image. You have to provide two landmarks per image by selecting a line.

Example: Load the template (the image you want to align to) and specify the landmarks by a line selection:

![](/media/plugins/shortnosed-sturgeon.jpg)

Then load the image you want to align with the template, and select a line (the order of the points is relevant: the first point will correlate with the first point of the other image's line selection):

![](/media/plugins/blue-parrot-fish.jpg)

Now, start the plugin. If there was more than one other image with an active line selection, you would be asked which one is the template. Since there is only one, the plugin does not ask, but starts to work right away. The result looks like this:

![](/media/plugins/aligned-blue-parrot-fish.jpg)

  
