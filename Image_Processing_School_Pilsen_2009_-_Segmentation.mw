== Introduction ==

This tutorial is designed to give you a first impression of the segmentation tools available in Fiji. It covers basic thresholding and morphology operations (erode, dilate, open, close), [[Level Sets]], the [[Simple Neurite Tracer]] and the [[Segmentation Editor]].

== Thresholding and Morphology ==
Thresholding is a very simple segmentation method. You just specify a gray value and all pixels in the image are classified according to their value being larger or smaller than the threshold.

* open the blobs sample image (this image is so popular that it got a hotkey: ctrl+shift b)

[[Image:blobs.jpg]]

* now try to segment the blobs with a threshold: Image - Adjust - Threshold
* play a bit with different possible values: 
** What do you notice? 
** Which value do you choose and why? 
** Imagine you would like to measure the size of the blobs after the segmentation. What do you need to take into account?
** What would be different if you would segment the blobs by hand?

It is hard to segment the image without a very small blobb in the center. We will have a look now on how to get rid of such small blobs.
The following image shows a possible segmentation and the small annoying blob and some others we do not want to have:

[[Image:thresholdSegmentation.jpg]]

We now want to filter these small blobs using morphology operations. You can find these under Process - Binary
Besides the basic four operations (erode, dilate, open, close) there is also an options dialog:

[[Image:morphOptions.jpg]]

Here you can specify how often (iterations) the operator (choose in Do drop down menu) should be applied and how big the template is (count).
Try to play a bit with the parameters. You should at least notice two things:

* It is fairly easy to get rid of the small blobs
* It is also possible to change the shape of the blobs. 
** Which shape do they change into?
** Why, do you think, is it this shape?
** Again what does this imply for measurements?

If you want to read more about morphology, I these pages might be useful:
http://homepages.inf.ed.ac.uk/rbf/HIPR2/morops.htm

As you have seen, thresholding is a fairly simple method. Let's move on to something more sophisticated.

== Level Set Plugin ==

The Fiji plugin provides two PDE based methods, the more basic fast marching and the advanced active contour algorithm.

Fast marching works similar to a standard flood fill but is more sensitive in the boundary detection. While growing the region it constantly calculates the difference of the current selection to the newly added pixels and either stops if it exceeds a pre selected gray value difference or if it would exceed a certain pre-selected rate of growth. This algorithm is sensitive to leaking - if the object has a gap in the boundary, the selection may leak to the outside of the object.

Level sets advance a contour like a rubber band until the contour hits an object boundary. The rubber band like nature (= curvature) prevents the contour from leaking if there are gaps in the boundary. The strength of the rubber band and a gray level difference can be pre-selected.

The speedy fast marching can be used as input for the slower active contours. If the image is very large, starting with Fast Marching and using the contour from the fast marching to refine the object with Level Sets can significantly speed up the object detection.

For our test we are going to generate our testimage ourselves.

* create a new small image (100x100 pixels)
* Now draw a filled black circle on the white background (The fill command is in the Edit menu) 

[[Image:levelSetCircle.jpg]]

Okay, this image basically is already segmented. But lets just try the rubberband levelset look for a sanity check.
Open the level set plugin under Plugins - Segmentation (gives an error)
Seems we have to specify a region first. This is because the level sets need an initial contour that is then refinded. So draw something crude in the circle

[[Image:levelSetCircleSelection.jpg]]

Now we can open the plugin (Plugins - Segmentation - Level Sets)

You will see the following dialog appear:

[[Image:LevelSet_Dialog.jpg]]

The fast marching method is not very interesting for our purpose at the moment. You are free to play with it later. For now please uncheck that box.

As you can see there are four parameters to adjust (Advection, Propagation, Curvature, Grayscale tolerance). The good news is that you only have to worry about the last two. 
For our very simple image the default parameter should work. Just make sure, that you set the "Region expands to" option to outside, if you drew something inside the circle.

* Hit that okay button and look at the result
* You can also try to specify a contour outside the circle and let it shrink (remember to choose Region expands to outside then in the dialog)

So far not very impressive. Let's make this a bit more complicated.

* Cut a part out of the black circle by drawing a white ellipse onto it:

[[Image:LevelSets_CirclePackman.jpg]]

Now again try to segment this shape with level sets:
* Try to grow a contour from the inside
* And from the outside
* What do you have to do to get a segmentation that fills the gap?

[[Image:LevelSets_Packman_closed.jpg]]

Now take the same image and add some noise (Process - Noise - Add noise)

* Can you still get a good segmentation?
* What difficulties arrise?

If you want to know more about the plugin, you can look at the [[Level_Sets|documentation]].

== Simple Neurite Tracer ==
This is a very nice plugin for semi automatic segmentation of thin elongated structures. It is designed to work with fluorecent images of neurons, but I am sure you can find other applications for it too!
Fortunately Mark has already written a very nice documentation about the plugin. So there is little use in me writing everything again.
You can find an example data set at: [https://fiji.sc/cgi-bin/gitweb.cgi?p=VIB.git;a=blob;f=test-images/c061AG-small-section.tif c061AG-small-section.tif];
So please have a look at the [http://homepages.inf.ed.ac.uk/s9808248/imagej/tracer/instructions.html documentation]
I especially like the [http://homepages.inf.ed.ac.uk/s9808248/imagej/tracer/step-by-step/ step-by-step guide]

In order to try the plugin yourself you can use the sample data provided or try one of the channels of the Neuron example image, that is linked in the File - Open Samples menu.

== Segmentation Editor ==
A nice all purpose 3d manual segmentation plugin is the segmentation editor. It even is able to interpolate over sections where you did not provide manual tracks. You can find it under Plugins - Segmentation.
Also for this plugin there already exists very good [http://132.187.25.13/home/?category=Download&page=SegmentationEditor documentation]

As you can see, the newer version has two additional buttons:

[[Image:segmentationEditor_update.jpg]]

They are labeled O and C like open and close. Sounds familiar :-)

In order to have some fun, I recommend to use the head sample file from the File - Open samples menu. 
You can segment the brain of that guy and afterwards make a nice animation with the volume viewer:

[[Image:manWithBrain.jpg]]

Hope you had fun!

[[Category:Tutorials]][[Category:Segmentation]]
