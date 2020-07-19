{{ComponentStats:sc.fiji:Arrow_}}
[[Image:Arrow example.png|center]]


This version replaces the old <code>Arrow_.class</code> tool that was present in Fiji before. The main changes are the ability to draw the arrow as a floating selection, and to tune its shape. 

Warning: Since <code>ImageJ version 1.43n</code>, a similar tool, made by {{Person|Rasband}}, does a similar thing from the ImageJ core, see {{GitHub|org=imagej|repo=ImageJA|path=ij/gui/Arrow.java|label=here}}.

== Usage ==

[[Image:Arrow example2.png|right]]

Launch the plugin from the menu. A tool appear in ImageJ toolbar:
If there is no space for a spare tool in the toolbar, an error message is displayed. 


Select the arrow tool and start drawing it in an image. To burn in its outline, select "Draw" (shortcut: d); to fill it, select "Fill" (shortcut "f") as for any other roi tool.

You can change the color and line width via {{bc | Edit | Options | Line Width}} and {{bc | Edit | Options | Colors}}. The ''Foreground'' option in the latter will change the color of the arrow.

The user can drag the arrow head, base or he whole arrow by clicking and dragging near respectively its head, base or body. 

If the shift key is pressed while dragging the head, only direction multiple of 45º will be allowed. 

[[Image:Arrow example3.png|right]]
To customize the arrow shape and type, double click the arrow tool. A dialog is displayed that allow to select the line thickness, the arrow head length and the arrow type. Changes made to the configuration panel are reflected to the arrow immediately. 

It is possible to change the arrow shape using the mouse wheel. To change its thickness or the arrow head length, press shift and rotate the mouse wheel respectively near the arrow body and head. To change the arrow style, press {{key|Ctrl}}+{{key|Shift}} and rotate the mouse wheel near the arrow.

[[Image:Arrow example4.png|right]]
So far, 4 types of arrow head are implemented:
* Delta
* Thick
* Thin
* Circle 



== Legacy mode ==

To be compatible with the previous Arrow_ tool, this plugin has a legacy mode that behaves as previous version. To use it:

* In an image, draw a line roi
* Launch the Arrow_ plugin
* The Arrow_ tool does not appear in the toolbar, but an arrow is burned in the image from the line selection.




== Further developments ==

If you need this tool to do something more, do not hesitate to mail the maintainer. He will be pleased to implement it. 





[[Category:Plugins]]
[[Category:Image annotation]]
