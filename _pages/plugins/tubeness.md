---
mediawiki: Tubeness
name: "Tubeness"
title: Tubeness
categories: [Uncategorized]
dev-status: "stable"
team-founders: ['@mhl', '@StephanPreibisch']
team-maintainer: '@mhl'
---


{% capture source%}
{% include github org='fiji' repo='VIB' branch='master' source='features/Tubeness_.java' %}
{% endcapture %}
{% include info-box filename='VIB\_.jar' source=source %}


{% capture text%}
A multithreaded implementation of the original IJ1 Tubeness plugin has been [developed](https://github.com/imagej/imagej-ops/pull/527) by {% include person id='tinevez' %} in the context of [ImageJ\_Ops](/libs/imagej-ops).
{% endcapture %}
{% include notice icon="info" content=text %}

The original documentation for the IJ1 Tubeness plugin can be found at http://homepages.inf.ed.ac.uk/s9808248/imagej/tubeness/.


