---
mediawiki: Average_Images
name: "Average Images"
title: Average Images
categories: [Uncategorized]
dev-status: "stable"
team-founder: '@mhl'
team-maintainer: '@mhl'
---


{% capture source%}
{% include github org='fiji' repo='VIB' branch='master' source='vib/Average_Images.java' %}
{% endcapture %}
{% include info-box filename='VIB\_.jar' source=source %}

Create an averaged image, in that each point in the result image is the mean of the values at that point in all the source images. You can drag files into the file list in order to add them.

FIXME: complete this documentation, add screenshots, etc.
