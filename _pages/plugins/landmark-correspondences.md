---
title: Landmark Correspondences
categories: [Transform, Registration]

name: Landmark Correspondences
initial-release-date: "2008-08-07"
team-founders: "@axtimwalde"
team-maintainer: "@axtimwalde"
artifact: mpicbg:mpicbg_
source-url: https://github.com/axtimwalde/mpicbg/blob/-/mpicbg_/src/main/java/Transform_Roi.java
---

The plugin **Landmark Correspondences** calculates a transformation between two corresponding landmark clouds and renders a transformed image. The landmarks are read from point selections over two images. The transformation is estimated by a least squares or Moving Least Squares fit for the available models.

The non-linear non-invertible transformations as estimated using the Moving Least Squares method are rendered through a mesh of triangles whose resolution is a parameter of the plugin, see [Interactive Moving Least Squares](/plugins/interactive-moving-least-squares) for an intuitive explanation.

{% include img src='transform-roi-linear' caption='Two snapshots from the ImageJ Conference 2008 registered into each other using an affine transformation as estimated from automatically extracted Feature Correspondences.' %}
{% include img src='transform-roi-mls' caption='A photograph and a cartoon registered into each other using the Moving Least Squares method and a similarity transformation as estimated from manually set landmark correspondences.' %}
