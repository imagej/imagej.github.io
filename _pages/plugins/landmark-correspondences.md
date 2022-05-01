---
mediawiki: Landmark_Correspondences
title: Landmark Correspondences
categories: [Transform,Registration]
---


{% capture author%}
{% include person id='axtimwalde' %} ([1](mailto:saalfeld@mpi-cbg.de))
{% endcapture %}

{% capture maintainer%}
{% include person id='axtimwalde' %}
{% endcapture %}

{% capture source%}
{% include github org='axtimwalde' repo='mpicbg' branch='master' path='mpicbg_/src/main/java/Transform_Roi.java' %}
{% endcapture %}
{% include info-box name='(Transform by) Landmark Correspondences' software='Fiji' author=author maintainer=maintainer source=source released='August 7<sup>th</sup>, 2008' latest-version='October 19<sup>th</sup>, 2010' status='stable, active' category='Plugins, Transform,Registration' %} The plugin **Landmark Correspondences** calculates a transformation between two corresponding landmark clouds and renders a transformed image. The landmarks are read from point selections over two images. The transformation is estimated by a least squares or Moving Least Squares fit for the available models.

The non-linear non-invertible transformations as estimated using the Moving Least Squares method are rendered through a mesh of triangles whose resolution is a parameter of the plugin, see [Interactive Moving Least Squares](/plugins/interactive-moving-least-squares) for an intuitive explanation.

{% include thumbnail src='/media/plugins/transform-roi-linear.jpg' title='Two snapshots from the ImageJ Conference 2008 registered into each other using an affine transformation as estimated from automatically extracted Feature Correspondences.'%} {% include thumbnail src='/media/plugins/transform-roi-mls.jpg' title='A photograph and a cartoon registered into each other using the Moving Least Squares method and a similarity transformation as estimated from manually set landmark correspondences.'%}

  
