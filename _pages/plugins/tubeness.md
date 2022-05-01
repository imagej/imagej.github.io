---
mediawiki: Tubeness
title: Tubeness
categories: [Uncategorized]
---


{% capture source%}
{% include github org='fiji' repo='VIB' branch='master' source='features/Tubeness_.java' %}
{% endcapture %}
{% include info-box software='ImageJ' name='Tubeness' author='Mark Longair, Stephan Preibisch' maintainer='Mark Longair' filename='VIB\_.jar' source=source status='stable' %}


{% capture text%}
A multithreaded implementation of the original IJ1 Tubeness plugin has been [developed](https://github.com/imagej/imagej-ops/pull/527) by {% include person id='tinevez' %} in the context of [ImageJ\_Ops](/libs/imagej-ops).
{% endcapture %}
{% include notice icon="info" content=text %}

The original documentation for the IJ1 Tubeness plugin can be found at http://homepages.inf.ed.ac.uk/s9808248/imagej/tubeness/.


