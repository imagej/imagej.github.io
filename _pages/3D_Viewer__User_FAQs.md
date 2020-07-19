(Return to the main [[3D Viewer]] page)





== Basic Usage ==



=== How to display a stack ===
After you have started the 3D viewer, click on '->File->Add content'. A
dialog window opens, asking for some information:

* '''Image:''' The image which should be displayed in the viewer. The user can select from a list of all open images.
* '''Name:''' A name for the 3D object. The default is the image title.
* '''Display as:''' Stacks can be displayed as volume renderings, orthoslices, surfaces or surface plots.
* '''Color:''' The color of the 3D object.
* '''Threshold:''' For surfaces, this is the isovalue of the surface. For all other display modes, this value is the lower threshold of displayed values.
* '''Resampling factor:''' Large images require downsampling before displaying, to be rendered interactively. A value of 2 means here that the image is downsampled by a factor of 2 in x-, y- and z-direction.
* '''Channels:''' If displaying color images, this specifies the color channels which are to be displayed.

After clicking OK, the 3D object appears in the viewer window. [[#top|Top]]



=== How to interact with the viewer (rotate, shift, zoom) ===
The user can rotate, translate and zoom in the 3D space: Two sorts of transformations are distinguished:

==== 1. Transformation of the view: ====
* '''Rotation:''' Select the 'Hand' tool in ImageJ's tool bar. If no 3D object is selected, dragging with the left mouse button rotates the view around the universe center.
* '''Translation:''' Dragging while pressing the 'Shift' key shifts the view.
* '''Zooming:''' Zooming is done by selecting the 'Glas' tool in ImageJ's tool bar and drag with the left mouse button. On many platforms, it is alternatively possible to scroll (while the 'Hand' tool is selected) for zooming.

==== 2. Transformation of objects: ====
Individual objects can be transformed with the same key/mouse combinations. To transform a specific object, that object needs to be selected. An object
is selected by a single left mouse click. Selection is indicated by a red bounding box. [[#top|Top]]

=== How to change the color, transparency... of a 3D object ===

Color, transparency, threshold and displayed channels of color images are so-called attributes of 3D objects. These attributes have the following meaning:
* '''Color:''' The color of the 3D object. If 'None' is selected, the color is taken from the stack image.
* '''Transparency:''' The transparency of the 3D object: A value of 0 means fully transparent, a value of 1 means fully opaque.
* '''Threshold:''' In case of surfaces, the threshold specifies the isovalue of the surface. Otherwise, it specifies the lower threshold of displayed pixels.
* '''Channels:''' In color images, the channels attribute specifies the channels to be displayed. In greyscale images, this attribute has no effect.

The attributes can be changed by
# Select the corresponding object by clicking on it
# Click on -> Edit -> Attributes and select the attribute you want to change.

[[#top|Top]]



=== How to make animations and movie recordings ===

To animate the view, click on ->View->Start animation. The view begins immediately to rotate around the y-axis. If you now want to record such an animation, click on ->View->Start recording. The animation is now recorded for one full 360° rotation. The result is displayed in a stack.

If you want to include the recording in a presentation, save it via ImageJ's 'Save as AVI' function. You can incorporate the resulting movie file in powerpoint presentations.

To stop an animation, click on ->View->Stop animation.  [[#top|Top]]



=== How to reset the view ===
You can reset the 3D universe to its initial view by clicking on ->View->Reset View. This resets the view.

Note however, that this does not change the transformation of individual 3D objects. To reset them, too, select each object and click on ->Transformation->Reset transformation. [[#top|Top]]



=== How to hide the coordinate system ===
There are two types of coordinate systems: One global coordinate system, which indicates the origin of the universe, and one local coordinate system for each object.

For hiding the global coordinate system, have a look at "How to general view settings"

For hiding the local coordinate system, select the object and click on ->Edit->Hide/Show and disable 'Show coordinate system'.

See [[#How to general view settings]] for how you can avoid to show local coordinate systems in general. [[#top|Top]]



=== How to change the background color ===
To change the background color of the 3D world, click on ->View->Change background color. A dialog opens, which lets you interactively adjust the background color.

To use the current background color by default, see [[#How to change general view settings]]. [[#top|Top]]





== Surfaces ==

=== What is the idea of a surface ===
Intuitively, the surface of an object is understood as the border between the object and the background. One common way to find a surface is to choose a threshold which divides object and background: Values above the threshold are assumed to belong to the object, values below are assumed to belong to the background. To construct a surface, an algorithm like the marching cubes algorithm can be utilized. [[#top|Top]]



=== How to change the color, transparency... of a surface ===
See [[#How to change the color, transparency... of a 3D object]]



=== How to change the isovalue of a surface ===
See [[#How to change the color, transparency... of a 3D object]]



=== How to smooth a surface ===
In order to smooth the surface of a 3D object, select the object and click on ->Edit->Smooth surface.

You can also smooth all displayed surfaces by clicking on ->Edit->Smooth all surfaces [[#top|Top]]



=== How to export surfaces ===
The displayed surfaces can be exported to files in different surface file formats. Currently supported is Wavefront (.obj) and Drawing Interchange Format (.dxf). [[#top|Top]]





== Volumes ==

=== What are volumes/volume renderings ===
A volume rendering generates the 3D effect by putting the slices of a stack one behind another, separated by a certain distance. To each pixel in each slice a transparency value is assigned, which depends on the pixel's brightness. [[#top|Top]]



=== How to change the color, transparency, ... of a volume ===
See [[#How to change the color, transparency... of a 3D object]]



=== How to edit volumes ===
The 3D viewer offers the possibility to edit volumes. To crop volumes,
# Select an object by clicking on it.
# Use one of ImageJ's selection tools to draw a region of interest (ROI).
# Click on ->Edit->Fill selection to erase the volume which is covered by the ROI. (Erasing means actually filling it with black).

[[#top|Top]]





== Orthoslices: ==

=== What are orthoslices ===
Orthoslices are three orthogonal slices through the volume. The three slices show one xy-plane, one xz-plane and one yz-plane. [[#top|Top]]



=== How to change the color, transparency, ... of orthoslices ===
See [[#How to change the color, transparency... of a 3D object]]



=== How to change the displayed slice ===
The position of the three slices can be changed. To do so, click on -> Edit -> Adjust slices. A dialog opens, which lets you adjust interactively the position of each of the three slices.

There exist also keyboard shortcuts to adjust the slices: hold one of the x, y, and z key pressed and use either the arrow keys or mouse scrolling to adjust the slices.

To hide a slice, hold one of the x, y or z key pressed and hit the 'space' bar. [[#top|Top]]



=== How to hide a slice ===
See [[#How to change the displayed slice]]





== 2D Surface Plots ==

=== What are surface plots ===
A surface plot displays a 2D slice as a 3D plot: The x- and y-coordinate correspond to the x- and y-coordinate in the 2D slice, the z-coordinate is the pixel value at (x, y).

A 3D surface plot always shows one slice a time. When a 3D surface plot is opened in the viewer, the currently selected slice is displayed. When changing the slice of the original image stack, the view is automatically updated. [[#top|Top]]



=== How to change the color, transparency, ... of surface plots ===
See [[#How to change the color, transparency... of a 3D object]]



=== How to interactively change the displayed slice ===
A 3D surface plot always shows one slice a time. When a 3D surface plot is opened in the viewer, the currently selected slice is displayed. When changing the slice of the original image stack, the view is automatically updated. [[#top|Top]]





== View Settings ==

=== How to reset the view ===
See [[#How to reset the view]]



=== How to center a 3D object in the view ===
In case you have several 3D objects in the 3D window, it is desirable to center the view on one specific object. This is possible by selecting an object (by clicking on it) and click on ->View -> Center selected. [[#top|Top]]



=== How to hide the coordinate system ===
There are two types of coordinate systems, one global and one locally for each individual 3D object. To hide the local coordinate system of one specific 3D object, see [[#How to hide the coordinate system]]. To hide the global coordinate system, see [[#How to change general view settings]]. [[#top|Top]]



=== How to change the background color ===
see [[#How to change the background color]]



=== How to show a scalebar ===
To show or edit a scalebar to the 3D view, click on ->View->Edit scalebar. A dialog opens, which allows you to adjust scalebar settings:

* '''x position:''' The x coordinate of the scalebar in realworld coordinates.
* '''y position:''' The y coordinate of the scalebar in realworld coordinates.
* '''length:''' The length of the scalebar, also in realworld units.
* '''units:''' An additional string which is displayed together with the length.
* '''Color:''' The color of the scalebar.
* '''show:''' Check/Uncheck this box to show/hide the scalebar.

Clicking OK applies the changes. [[#top|Top]]



=== How to change the center of rotation of global rotations ===
See [[#How to change general view settings]]



=== How to change general view settings ===
Some general view settings can be changed and made permanent by clicking on ->View->View settings. A dialog window opens, asking the user for settings. There are two types of settings, startup options and options which are applied immediately.

# Startup options:
#* '''Width and Height''' The window dimensions of the 3D viewer.
#* '''Show global coordinate system''' Show a coordinate system which indicates the origin of the 3D world.
#* '''Use current color as default background''' Activate this option to reload the current background color at each start of the viewer.
#* '''Show scalebar''' Activate this option to show the scalebar by default. (See also [[#How to show a scalebar]].
#* '''Apply changes now''' If activated, the changes in the settings above are immediately applied, otherwise, they are first applied at the next application start.
# Immediately applied options:
#* '''Show local coordinate system by default''' If activated, the local coordinate system of 3D objects is shown when new objects are loaded in the 3D viewer. If inactivated, the coordinate system is omitted. Note: This only affects newly added 3D objects. Already displayed objects are not affected.
#* '''Global rotation around Center/Origin''' Global rotations (see [[#How to interact with the viewer (rotate, shift, zoom)]]) can have two possible centers:
#** '''Origin:''' The origin of the virtual world. This is in most cases the lower left corner of 3D objects. You can make the origin visible by showing the global coordinate system (see above).
#** '''Center:''' The center of the virtual world. The center is automatically calculated from the displayed 3D objects.

[[#top|Top]]





== Transformations ==

=== The concept of transformations ===
There are two types of transformations in the 3D viewer: Global transformations and local transformations. Global transformations refer to transformations of the whole view, no individual objects are transformed, but the whole 3D world together. Local transformations refer to transformations of individual objects.

Transformations can be made interactively with the mouse. See [[#How to interact with the viewer (rotate, shift, zoom)]] for more information.

Alternatively, transformations of individual objects can be altered more exactly, by specifying transformations matrices. Transformations can be set for 3D objects, or applied (concatenated with the current transformation) to 3D objects. Transformations can be saved and reloaded. And finally, it is possible to export a transformed object to a stack image. [[#top|Top]]



=== How to apply a specific transformation to a 3D object ===
Applying a transformation to a 3D object means to concatenate the specified transformation with the current transformation of the object.

To apply a transformation, select an object and click on ->Transformation->Apply transform. A window opens, which asks you for a transformation matrix. The matrix is supposed to be given as a (3x4) matrix, row by row. All the individual values should be separated by a space character.

Example:
         |  a11 a12 a13 a14 |
         |  a21 a22 a23 a24 |
         |  a31 a32 a33 a34 |
         |    0   0   0   1 |


should be specified as "a11 a12 a13 a14 a21 a22 a23 a24 a31 a32 a33 a34" (without the '"').

The window also allows you to load a transformation from a file. [[#top|Top]]



=== How to set a specific transformation for a 3D object ===
Setting a transformation of a 3D object does not concatenate transformations. See [[#How to apply a specific transformation to a 3D object]] to concatenate transformations.

To set a transformation, select an object and click on ->Transformation->Set transform. A window opens, which asks you for a transformation matrix. The matrix is supposed to be given as a (3x4) matrix, row by row. All the individual values should be separated by a space character.

Example:
         |  a11 a12 a13 a14 |
         |  a21 a22 a23 a24 |
         |  a31 a32 a33 a34 |
         |    0   0   0   1 |


should be specified as "a11 a12 a13 a14 a21 a22 a23 a24 a31 a32 a33 a34" (without the '"').

The window also allows you to load a transformation from a file. [[#top|Top]]



=== How can I see the current transformation of a 3D object ===
To see the current transformation matrix of a 3D object, select that object and click for example on -> Transformation -> Set Transform. The window which opens shows the current transformation of the object. A (3x4) matrix is shown, row by row in one line.

Example:
         |  a11 a12 a13 a14 |
         |  a21 a22 a23 a24 |
         |  a31 a32 a33 a34 |
         |    0   0   0   1 |


is shown as "a11 a12 a13 a14 a21 a22 a23 a24 a31 a32 a33 a34" (without the '"').

Click 'Cancel' if you don't want to change the transformation. [[#top|Top]]



=== Can I save/reload the current transformation of a 3D object ===
To save the current transformation of a 3D object, select that object and click on ->Transformation->Save transform. You can specify a file to which the current transformation is stored.

To load a transformation, click on ->Transformation->Set transform. In the opening window, you can choose a previously stored transformation file. [[#top|Top]]



=== How to save a transformed object ===
The 3D viewer allows to load an image stack and display it as a 3D object. This object can be transformed. See e.g.

* [[#How to interact with the viewer (rotate, shift, zoom)]]
* [[#How to apply a specific transformation to a 3D object]]
* [[#How to set a specific transformation for a 3D object]]

Now such a transformed object can be exported to a stack image again. To do so, click on ->Transformation->Export transformed image. The resulting stack image can of course also be saved via ImageJ's 'Save as' commands. [[#top|Top]]





== Point Lists ==

=== What is meant by 'point list' and why can they be useful ===
Point lists represent a list of named points. They can be used for marking regions in/on 3D objects, for example. One particular usage of point lists is the landmark based registration. (See [[#How can two 3D objects be registered]]). Each 3D object owns a point list. This list is not shown by default, however. [[#top|Top]]



=== How to show the point list of an object ===
There are two ways to show the point list of a 3D object:
* Click on ->Edit->Point list->Show Point list or
* Select ImageJ's point tool and click on a selected object.

In both cases, a window opens which shows a list of named points for the selected object. [[#top|Top]]



=== How to add/remove points ===
To add  points, do the following:
* Select a 3D object by clicking on it
* Select ImageJ's 'POINT' tool
* Click somewhere on the selected object.
    
The point is added and appears in the point list window.

To remove a point, either
* Press shift and click on the point you want to remove. ImageJ's 'POINT' tool has to be selected for that operation or
* Right-click on the point in the point list window and click on 'Remove'.

The point disappears. [[#top|Top]]



=== How to change the position of a point ===
You can interactively drag the point of interest. ImageJ's 'POINT' tool has to be selected. Click with the left mouse button on the point and drag it to the desired position. [[#top|Top]]



=== How to save a point list to file and how to reload it ===
Point lists can be stored to file and be reloaded. To do so, select an object and click on -> Edit -> Point list -> Save Point list or on ->Edit->Point list->Load Point list respectively. Choose the file containing the point lists. [[#top|Top]]



=== How to highlight a point from the list in the 3D view ===
Sometimes, one wishes to know where a particular point from the point list window is located in the 3D world. To highlight a point from the point list window, just left-click on it. It gets animated then. [[#top|Top]]



=== How to hide the points ===
To hide the points, click on ->Edit->Point List->Hide Point list. The point list window is closed automatically. [[#top|Top]]



=== How to close the list window ===
To hide the points, click on ->Edit->Point List->Hide Point list. The point list window is closed automatically. [[#top|Top]]





== Registration ==

=== Which kinds of registration is supported ===
At the moment, only rigid landmark-based registration is supported. [[#top|Top]]



=== How can two 3D objects be registered ===
To initiate registration, load at least two objects into the viewer and click on ->Edit->Register

You are now guided step by step through landmark selection of model and reference image and through the registration process.

Please note that the images are locked after registration, to prevent unintended user interaction. To be able to transform the objects again, select each of them and inactivate ->Transformation->Lock [[#top|Top]]



=== How can the results be saved ===
See [[#How to save a transformed object]]

[[#top|Top]]
