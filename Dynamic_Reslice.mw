{{Infobox
| name                   = Dynamic Reslice
| software               = [[Fiji_Plugins]]
| author                 = Jean-Yves Tinevez & Albert Cardona from an ImageJ class
| maintainer             = Jean-Yves Tinevez ([mailto:tinevez_at_mpi-cbg_dot_de tinevez_at_mpi-cbg_dot_de])
| filename               = [https://fiji.sc/tinevez/Dynamic_Reslice.jar Dynamic_Reslice.jar]
| source                 = {{GitHub|org=fiji|repo=Fiji_Plugins|source=fiji/stacks/Dynamic_Reslice.java}}
| released               = 22 April 2009
| latest version         = v1.2 (23 April 2009)
| status                 = active 
}}


== Purpose ==


This plugin is simply a dynamic version of the Reslice command as it is in
ImageJ version 1.42l, by Patrick Kelly, Harvey Karten, {{Person|Rasband}}, Julian
Cooper and Adrian Deerr. It draws an orthogonal slice through the volume
represented by the stack it is applied on along its ROI, and update
dynamically this slice as the ROI is displaced or deformed. 


== Installation ==

=== ImageJ ===

Download the jar file [https://fiji.sc/tinevez/Dynamic_Reslice.jar Dynamic_Reslice.jar] 
and drop it into the ''plugins'' menu. The plugin will appear in the {{bc | Plugins | Dynamic_Reslice}} menu.

=== Fiji ===

The plugin is part of the Fiji distribution, as a member of the [[Fiji_Plugins]] package. You can find it in the {{bc | Image | Stacks}} menu.


== Usage ==

Open a stack and draw a line roi on it (any line roi will do it: straight line, poly-line, freehand line). When you call the plugin you are asked for two parameters.

* ''Flip vertically'' will cause the source slices to be processed from bottom to top.
* ''Rotate 90º'' will cause the result display to be rotated by 90º.

The reslice window is drawn. Now change the roi shape or move it with the mouse. The result window refreshes automatically. Is is possible to change roi type on the fly.


== Scripting ==

It is possible to call and control this plugin from other plugin or scripts. Here is a script example for use with [[Fiji]].

<source lang="python">
'''
This jython script intends at demonstrating how to script the 
Dynamic_Reslice plugin. It will open the t1-head sample stack
in Fiji, draw a ROI on it, and animate it while updating the 
Reslice image.

Created on Apr 23, 2009

@author: Jean-Yves Tinevez
'''

import fiji
import time

xstart = 40
ystart = 50


# Fetch the t1-head stack from URL
source_imp = IJ.openImage('https://imagej.net/images/t1-head.zip')
source_imp.show()

# Select middle slice (does not matter)
source_imp.setSlice(60)

# Instantiate the Dynamic_Reslice plugin
dr = fiji.stacks.Dynamic_Reslice(source_imp)

# Set up the plugin so that it will rotate the resulting image, and will 
# parse slices from bottom to top
dr.setRotate(True)
dr.setFlip(True)

# Get the destination ImagePlus
dest_imp = dr.getImagePlus()

# Now move the roi and update the image
for dx in range(170):
    
    IJ.showStatus('Moving the Roi by '+str(dx))
    
    # Draw a line ROI on the source imp
    roi = Line(xstart+dx, ystart, xstart+dx, ystart+170)
    source_imp.setRoi(roi)
    
    # Update the reslice. We have to call it manually in the script.
    dr.update();
    
    # Wait a bit so that we can see what is happening
    time.sleep(0.03)
    
IJ.showStatus('Done')
</source>

== Example ==

[[Image:DynamicresliceROI.gif|left]]
[[Image:Dynamicreslice.gif]]




== Version history ==

<ul>
<li>1.0 - 22 April 2009 - First working version.
<li>1.1 - 22 April 2009 - Albert Cardona added the separate thread for
updating
<li>1.2 - 23 April 2009 -
<ul>
<li>Window size automatically changes when Roi length changes
<li>Can now be called and managed from scripts
<li>Major refactoring
</ul>
</ul>


== License: GPL ==

This program is free software; you can redistribute it and/or modify it under
the terms of the GNU General Public License 2 as published by the Free
Software Foundation.
<p>
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
details.
<p>
You should have received a copy of the GNU General Public License along with
this program; if not, write to the Free Software Foundation, Inc., 59 Temple
Place - Suite 330, Boston, MA 02111-1307, USA.


[[Category:Plugins]]
