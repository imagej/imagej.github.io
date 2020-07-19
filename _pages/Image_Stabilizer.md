{{Infobox
| software               = ImageJ
| name                   = Image Stabilizer
| maintainer        =  [mailto:christophe_dot_leterrier_at_gmail_dot_com Christophe Leterrier]
| author                 =  [mailto:kangli_at_cs_dot_cmu_dot_edu Kang Li] & [mailto:skang_at_andrew_dot_cmu_dot_edu Steven Kang]
| filename               = [http://www.cs.cmu.edu/~kangli/code/Image_Stabilizer.class Image_Stabilizer.class] and [http://www.cs.cmu.edu/~kangli/code/Image_Stabilizer_Log_Applier.class Image_Stabilizer_Log_Applier.class]
| source                 =[http://www.cs.cmu.edu/~kangli/code/Image_Stabilizer.java Image_Stabilizer.java] and [http://www.cs.cmu.edu/~kangli/code/Image_Stabilizer_Log_Applier.java Image_Stabilizer_Log_Applier.java]
| released               = 07/02/2008
| latest version         = 06/12/2009
| status                 = unknown
| category               = [[:Category:Registration|Registration]]
| website                = http://www.cs.cmu.edu/~kangli/code/Image_Stabilizer.html
}}

== What does it do? ==

This plugin stabilizes jittery image stacks using the Lucas-Kanade algorithm. It supports both grayscale and color images.

[[File:Image_Stabilizer_example.gif]]
[[File:Image_Stabilizer_examplecolor.gif]]

== How does it work? ==

It uses the currently shown slice in an image stack as the initial reference, or "template";
It estimates the geometrical transformation needed to best align each of the other slices with the "template". The estimation and alignment are performed using the Lucas-Kanade algorithm;
Once a slice is aligned, the "template" will be updated on the fly using the formula: new_template = a * old_template + (1 - a) * newly_aligned_slice, where "a" is the "template update coefficient" that can be adjusted when the plugin is run.

Hint: To process very large image stacks, import the stack with the "Use Virtual Stack" option enabled. The plugin will prompt you for an output directory to store the stabilized image sequence.

== Change log ==
2008/02/07: First version

2008/02/10: Optimized for speed using gradient pyramids

2008/02/12: Performed further speed optimizations and bug fixes

2008/02/14: Added support for affine transformation

2008/03/15: Made user interface improvements

2008/05/02: Added support for macro recordering (thanks to Christophe Leterrier at univmed.fr)

2009/01/11: Added support for logging transformation coefficients (can be reapplied to another stack using Image Stabilizer Log Applier)

2009/01/11: The stabilization process can be interrupted by pressing 'ESC' or by closing the image

2009/01/20: Fixed a runtime error when the user does not select the Log_Transformation_Coefficients checkbox (thanks to Nico Stuurman at UCSF)

2009/06/12: Fixed a bug that affected 32-bit float input images (thanks to Derek Bailey)

== Reference ==
K. Li, "The image stabilizer plugin for ImageJ," http://www.cs.cmu.edu/~kangli/code/Image_Stabilizer.html, February, 2008.

== License ==
Copyright (C) 2008-2009 Kang Li. All rights reserved.

Permission to use, copy, modify, and distribute this software for any purpose without fee is hereby granted, provided that this entire notice is included in all copies of any software which is or includes a copy or modification of this software and in all copies of the supporting documentation for such software. Any for profit use of this software is expressly forbidden without first obtaining the explicit consent of the author.

THIS SOFTWARE IS BEING PROVIDED "AS IS", WITHOUT ANY EXPRESS OR IMPLIED WARRANTY. IN PARTICULAR, THE AUTHOR DOES NOT MAKE ANY REPRESENTATION OR WARRANTY OF ANY KIND CONCERNING THE MERCHANTABILITY OF THIS SOFTWARE OR ITS FITNESS FOR ANY PARTICULAR PURPOSE.



[[Category:Plugins]]
[[Category:Registration]]
