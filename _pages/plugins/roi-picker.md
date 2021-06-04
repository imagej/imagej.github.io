---
mediawiki: ROI_Picker
title: ROI Picker
categories: [Uncategorized]
---


{% capture source%}
{% include github org='fiji' repo='Stitching' branch='master' source='tools/RoiPicker.java' %}
{% endcapture %}
{% include info-box software='Fiji' name='ROI Picker' author='Mark Hiner' maintainer='Mark Hiner' source=source released='30 August 2013' latest-version='22 October 2013' status='second version' category='[Plugins](/plugin-index)' %}

## Purpose

{% include thumbnail src='/media/plugins/roi-picker.png' title='The ROI Picker tool selected.'%}

This tool allows clicking to select existing ROIs. Clicking within the bounds of a ROI will select it in the ROI Manager. If multiple ROIs overlap over the clicked area, the union of the ROIs will be selected. Repeated clicks with the tool will then cycle through all individual ROIs in the union.


