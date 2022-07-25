---
mediawiki: Temporal_Median
name: "Temporal Median"
title: Temporal Median
categories: [Tracking,Filtering]
release-date: "2013"
website: "https://github.com/graemeball/IJ_Temporal"
dev-status: "active"
team-founder: Graeme Ball
---


{% capture source%}
{% include github org='graemeball' repo='IJ_Temporal' %}
{% endcapture %}
{% include info-box filename=' [Temporal\_plugins.jar](http://www.micron.ox.ac.uk/microngroup/software/Temporal_plugins.jar)' source=source category='Filtering' %}

**Temporal Median** can be used to find moving foreground features, which can be be a powerful way to suppress false background detections in subsequent tracking steps.
