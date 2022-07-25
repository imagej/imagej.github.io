---
mediawiki: ROI_Picker
name: "ROI Picker"
title: ROI Picker
categories: [Uncategorized]
release-date: "22 October 2013"
initial-release-date: "30 August 2013"
dev-status: "second version"
team-founder: '@hinerm'
team-maintainer: '@hinerm'
---


{% capture source%}
{% include github org='fiji' repo='Stitching' branch='master' source='tools/RoiPicker.java' %}
{% endcapture %}
{% include info-box source=source  %}

## Purpose

{% include thumbnail src='/media/plugins/roi-picker.png' title='The ROI Picker tool selected.'%}

This tool allows clicking to select existing ROIs. Clicking within the bounds of a ROI will select it in the ROI Manager. If multiple ROIs overlap over the clicked area, the union of the ROIs will be selected. Repeated clicks with the tool will then cycle through all individual ROIs in the union.


