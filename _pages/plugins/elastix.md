---
mediawiki: Elastix
title: Elastix
categories: [Uncategorized]
---


{% capture source%}
{% include github org='embl-cba' repo='fiji-plugin-elastixWrapper' %}
{% endcapture %}
{% include info-box name='Elastix' software='Fiji' update-site='EMBL-CBA' author='Christian Tischer' maintainer='Christian Tischer' source=source %}

## Overview

Elastix is a Fiji plugin that wraps [elastix](http://elastix.isi.uu.nl/) into a graphical user interface. elastix is a collection of algorithms that are commonly used to solve image registration problems. Both 2D and 3D as well as multi-channel registrations are supported. Several rigid (translation, Euler, similarity, and affine) as well as locally deformable (BSpline) registrations are supported. For more information please visit the GitHub [README](https://github.com/embl-cba/fiji-plugin-elastixWrapper#fiji-plugins-for-running-elastix-and-transformix).

## Installation

Elastix is available from the ImageJ update site: http://sites.imagej.net/EMBL-CBA.

For details on how to install an update site click [here](/update-sites/following).

To use this plugin you also need to install elastix itself, as described [here](https://github.com/embl-cba/fiji-plugin-elastixWrapper/blob/master/README.md#install-elastix-binary).

To start Elastix in ImageJ, select {% include bc path="Plugins | Registration | Elastix | Elastix" %} from the main menu.

## Citation

You can cite this plugin like this:

\- C. Tischer (2019). ElastixWrapper: Fiji plugin for 3D image registration with elastix. Zenodo. http://doi.org/10.5281/zenodo.2602549

Please also cite the original elastix software:

\- S. Klein, M. Staring, K. Murphy, M.A. Viergever, J.P.W. Pluim, "elastix: a toolbox for intensity based medical image registration," IEEE Transactions on Medical Imaging, vol. 29, no. 1, pp. 196 - 205, January 2010.

\- D.P. Shamonin, E.E. Bron, B.P.F. Lelieveldt, M. Smits, S. Klein and M. Staring, "Fast Parallel Image Registration on CPU and GPU for Diagnostic Classification of Alzheimer's Disease", Frontiers in Neuroinformatics, vol. 7, no. 50, pp. 1-15, January 2014.
