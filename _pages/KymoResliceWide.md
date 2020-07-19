{{Infobox
| software               = ImageJ
| name                   = KymoResliceWide
| author                 = [http://katpyxa.info Eugene Katrukha] and Laurie Young
| maintainer             = [mailto:katpyxa_at_gmail.com Eugene Katrukha]
| filename               = [https://github.com/ekatrukha/KymoResliceWide/blob/master/KymoResliceWide_.jar?raw=true KymoResliceWide_.jar]
| source                 = [https://github.com/ekatrukha/KymoResliceWide github]
| released               = 24 September 2014
| latest version         = 1 April 2017
| status                 = stable 
| category               = [[:Category:Stacks|Stacks]]
| website                = [https://github.com/ekatrukha/KymoResliceWide/wiki wiki_page]
}}


This plugin builds [[Generate_and_exploit_Kymographs|kymographs]] using straight line, polyline or freehand selection of variable thickness (and using either average or maximum intensity across the line). So it is extended implementation of ImageJ's ''Reslice'' function. Here are some thought on "[http://katpyxa.info/feedbacks/?p=26 Why another kymograph plugin?]".

== Using plugin == 

Open the stack/movie to be analyzed in ImageJ. Draw a line along the area where you want to make a kymograph.<br />You can use ImageJ’s ''native'' '''embedded''' characteristics of the line/curve, like: 

=== Line type === 

Plugin automatically picks up your choice of line selection from ImageJ and corrects for its length.<br />Just use the one you need.

http://katpyxa.info/software/KymoResliceWide/line_selection2.png


=== Line width ===

Define the width of line using double click on the line selection tool in ImageJ 

http://katpyxa.info/software/KymoResliceWide/line_width2.png

=== Parameters ===

After that the window showing kymograph parameters will pop-up:

http://katpyxa.info/software/KymoResliceWide/choice2.png

Where following options are available (in order): 
* whether to take average or maximum intensity transverse to line; 
* (unchecked) time as y-axis, distance as x-axis, (checked) time as x-axis, distance as y-axis; 
* (checked) curve will be added and displayed in the overlay of original movie/stack to mark already analyzed region;
* ignore original image/stack calibration, i.e. don't add its calibration to the final kymograph image (width, height, vortex size and frame rate)

== Other kymograph plugins == 

As alternative, there is very well documented [[Multi Kymograph]] plugin and its updated version [http://biop.epfl.ch/TOOL_KYMOGRAPH.html Kymograph tool].

== Version history ==

version 0.5 (2017/04/01): hyperstacks reslice fixed (now time, not Z) and image calibration handling is improved (with option to ignore it).  

version 0.4 (2015/10/21): now it works with hyperstacks and RGB images.

[[Category:Stacks]]
[[Category:Plugins]]
