---
mediawiki: KNIME
title: KNIME
section: Explore:Software
icon: /media/icons/knime.svg
project-blurb: the KNIME Analytics Platform
doi:
- 10.3389/fcomp.2020.00008
- 10.1016/j.jbiotec.2017.07.028
- 10.1007/978-3-319-28549-8_7
- 10.1007/978-3-540-78246-9_38
---


{% capture logo%}
{% include icon name='KNIME' size='78px' %}
{% endcapture %}

{% capture source%}
{% include github org='knime-ip' repo='knip' %}
{% endcapture %}
{% include notice icon="info" content='Plugin' software='KNIME' name='KNIME Image Processing' logo=logo author=' [KNIME team](http://www.knime.org/team)' maintainer=' [KNIME team](http://www.knime.org/team)' source=source status='active' website='http://tech.knime.org/community/image-processing' %}[KNIME](http://knime.org/), the **K**o**n**stanz **I**nformation **M**in**e**r, is an open source data analytics, reporting and integration platform. KNIME integrates various components for machine learning and data mining through its modular data pipelining concept. A graphical user interface allows assembly of nodes for data preprocessing (ETL: Extraction, Transformation, Loading), for modeling and data analysis and visualization.

The [**KN**IME **I**mage **P**rocessing](http://tech.knime.org/community/image-processing) extension, KNIP, provides ca. 100 nodes for (pre)-processing, filtering, segmentation, feature extraction, various views (2D, 3D), etc. and integrations for various other image processing tools are available.

As part of the KNIP extension, there is an [ImageJ extension for KNIME](http://tech.knime.org/community/imagej) consisting of two basic parts: the support for [ImageJ](/software/imagej) macro execution and the integration of [ImageJ2](/software/imagej2) plugins as KNIME nodes. Both approaches are available as KNIME plugin (currently beta status).

## See also

-   The [ImageJ Ops](/libs/imagej-ops) framework for image-processing algorithms, which is developed as a collaboration between the [ImageJ2](/software/imagej2) and KNIME teams.

## Publications

{% include citation %}
