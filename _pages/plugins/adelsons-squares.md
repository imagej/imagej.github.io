---
mediawiki: Adelson's_Squares
title: Adelson's Squares
categories: [Uncategorized]
---
Similar to the [spirals](/plugins/spirals) sample,
{% include github label="Adelson's squares"
  org="fiji" repo="fiji" branch='master'
  path="plugins/Scripts/File/Open_Samples/Adelsons_Squares.ijm" %}
demonstrate that human vision and perception is error prone for quantitative
measurements. In the natural context in which humans evolved, it makes sense to
compensate for shadows. However, this makes us believe that the two squares
with the black diamonds have a different shade of grey, yet they are identical
in brightness (RGB values). Since one is part of the "whites", and the other
the "blacks", our brains, recognising the checkerboard pattern, fool our
perception to believe the "white" square is lighter than the "black" square,
because we unconciously correct for the darker shadow cast by the cylinder.

{% include img align="left" src="adelsons-squares" %}
