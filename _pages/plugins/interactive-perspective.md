---
mediawiki: Interactive_Perspective
title: Interactive Perspective
categories: [Transform]
---


{% capture source%}
{% include github org='axtimwalde' repo='mpicbg' branch='master' path='mpicbg_/src/main/java/Transform_Perspective.java' %}
{% endcapture %}
{% include info-box name='Interactive Perspective' software='Fiji' author='Stephan Saalfeld' maintainer='Stephan Saalfeld' source=source released='November 9<sup>th</sup>, 2008' latest-version='February 13<sup>th</sup>, 2015' status='stable' category='Transform, Plugins' %}

This plugin allows to apply a **perspective transformation** to a 2D image in an interactive way.

**Premises**: You need an image to be open.

**Use**:

1.  When calling the plugin, **four points** (represented as yellow PointRois) will be displayed on the image.
2.  Drag and drop the points to interactively transform the image with a **perspective model**.
3.  If you are satisfied with the result, press ENTER, otherwise, press ESC.

## License

This program is **free software**; you can redistribute it and/or modify it under the terms of the **GNU General Public License** as published by the Free Software Foundation ([http://www.gnu.org/licenses/gpl.txt](http://www.gnu.org/licenses/gpl.txt)).

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

------------------------------------------------------------------------

 
