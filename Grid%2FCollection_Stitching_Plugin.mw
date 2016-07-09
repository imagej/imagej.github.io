{{Infobox
| name                   = Stitching
| software               = ImageJ
| author                 = Stephan Preibisch
| maintainer             = Stephan Preibisch<br/>Mark Hiner<br/>Curtis Rueden
| filename               = Stitching_.jar
| source                 = {{GitHub|org=fiji|repo=Stitching|source=plugin/Stitching_Grid.java}}
| released               = October 2008
| status                 = active
| category               = [[:Category:Stitching|Stitching]]
| website                = [http://fly.mpi-cbg.de/~preibisch Stephan Preibisch's homepage]
}}{{TOC}}
= What is Grid/Collection Stitching? =
When a large biological specimen must be pictured in high resolution, it must be done in tiles as the entire thing could not fit into the field view of the microscope. Once the entire specimen has been imaged, the tiles must be fit or stitched together to form one coherent image. Some overlap will be present between each tile and its neighbors to verify its location in the image.

The Grid/Collection stitching plugin allows several tiles placed in varying dimensions to be stitched together. 

To learn more about Stitching, please read the [[Stitching]] section of [[Techniques]]. 


= How to use the Grid/Collection Stitching plugin =
*Launch the stitching plugin from the menu item {{bc | Plugins | Stitching | Grid/Collection stitching}}
**Launch the stitching plugin from the menu item {{bc | Plugins | Stitching | Grid/Collection stitching}}
*In the plugin's graphical user interface (GUI), choose the position type as Positions from file from the first dropbox menu. Then choose the order as Defined by image metadata. With this choice, the images within your file do not need to be in any particular order. Click ok. 
*When a second GUI appears, select a file from your dataset. 
**If Prairie was used for data collection, ensure that the file selected is a .xml or .cfg
*Select a fusion method.
**Linear blending will obscure the seams between tiles, but will take a longer amount of time. Without it, tile lines will be clearly seen if the image is to be blown up. To save time, only use linear blending for presentation pieces. 
***To learn about other fusion methods, please visit the [[Image Stitching#Pairwise Stitching|Stitching]] page. 
*if Prairie or Wiscan are used, uncheck “compute overlap.” Both softwares calculate fairly accurate coordinates beforehand. 
*Reduce “Increase overlap” to 0 and uncheck subpixel accuracy
*If the data computed is too large for computer memory, check “use virtual memory.” This will be considerably slower, but will save RAM
**Alternatively, [[Grid/Collection Stitching Plugin#Memory Allocation|more memory can be allocated]] to the Fiji operation 
*Click ok and the images will begin to be stitched together.

= Troubleshooting with the Grid/Collection Stitching plugin =
== Inversion of Coordinates ==
Certain data sets have caused an inversion of coordinates when stitched together. The plugin is unable to discern the inversion without human intervention. After stitching, if the output image appears incorrect, redo the stitch. Depending on which axis the image has been inverted upon(the user will need to know this) select the corresponding option within the second dialog box. This will invert the selected coordinates before stitching the image create the correct image. 

== Speed ==
=== Memory Allocation ===
If "use virtual memory" has been selected but the stitching plugin is still taking a considerable amount of time, try allocating more memory to the process. 
*Open Memory from the menu item {{bc | Edit | Options | Memory & Threads}}
*Enter the amount of memory you would like to be allocated to the Fiji application in megabytes
**Check the amount of installed RAM on your computer to ensure you do not try to allocate more memory than exists.

=== Image Dimensions === 
Another speed reduction will occur if the tiles used have varying z coordinates. This will cause the stitching program to include tiles of black space wherever a tile has a z coordinate less than the maximum z coordinate within the file. To check if this could be a problem with your dataset, use the menu title to access {{bc | Plugins | Stitching | Visualize Tiles}}. If the computed image does NOT show up as one large square with a patchwork of squares, your data set has varying z-values. To alleviate the slower speeds, select "ignore Z position" within the second GUI.

[[Image:out_of_memory.png|thumb|right|250px|Out of memory error message.]]

== Memory == 
Even using virtual memory with maximum memory allocation can still be too much for some computers to handle, especially given the size of larger image files. The limited amount of memory available to most computers means that during the stitching of a large image file, the plugin will be trying to store more pixels within memory than there is space for. When this event occurs, Fiji will either stall and need to be
force closed, or will display the message "<Out of Memory>." To fix this issue, select "Downsampling" in the Stitching GUI to allow for the image to be stitched in pieces. Please see the [[Downsample |Downsampling]] page for more information. 
[[Image:Z_variance.png|thumb|right|250px|Example of a dataset with z-variance.]]

= Other Pitfalls = 
Please see the [[Image Stitching]] page for other precautions.

[[Category:Registration]]
[[Category:Stitching]]
