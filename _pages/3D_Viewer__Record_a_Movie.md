(Return to the [[3D_Viewer:_Developer_Documentation|Developer Documentation]] page)<br>
(Return to the main [[3D_Viewer]] page)



== How to animate the universe and create movies ==

You can download example source code for this HowTo [[3D_Viewer:_Example_code|here]].


It is very easy to animate the virtual universe and to record the animation, so that it can be stored as a video file and as such easily embedded into presentations.

The following lines show an easy example:
<source lang="java" first-line="28">
	// Add the image as a volume
	univ.addVoltex(imp);


	// animate the universe
	univ.startAnimation();


	// record a 360 degree rotation around the y-axis
	ImagePlus movie = univ.record360();
	movie.show();
	univ.pauseAnimation();
</source>

The call to the universe's <code>record()</code> method returns an <code>ImagePlus</code>, which consists of a stack of successive frames of a full 360 degree animation.

ImageJ provides methods to save such a stack for example as AVI file or as animated GIF.
