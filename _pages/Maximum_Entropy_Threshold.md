{{Infobox
| software               = ImageJ
| name                   = Maximum Entropy Threshold
| author                 = Jerek Sacha
| filename               = [https://imagej.net/plugins/download/Entropy_Threshold.class Entropy_Threshold.class] (1,418 Bytes)
| source                 = [https://imagej.net/plugins/download/Entropy_Threshold.java Entropy_Threshold.java] (2,755 Bytes)
| released               = 13 February 2004 
| status                 = unknown
| category               = [[:Category:Segmentation|Segmentation]]
| website                = [https://imagej.net/plugins/entropy.html]
}}

== Purpose ==

This plugin threshold an image using the Maximum Entropy algorithm, which is similar to [[Otsu Thresholding]] technique. Here, rather than maximizing the inter-class variance (equivalently, minimizing the within-class variance), the inter-class ''entropy'' is maximized. 

== Documentation == 

The plugin requires a 8-bit image to process. It outputs directly the thresholded image, replacing the original one. 

It processes stacks correctly, by operating on the whole stack histogram to determine the threshold. A new, thresholded stack replace the original one.

[[Category:Plugins]]
[[Category:Segmentation]]
