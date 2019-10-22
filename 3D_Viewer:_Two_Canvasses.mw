(Return to the [[3D_Viewer:_Developer_Documentation|Developer Documentation]] page)<br>
(Return to the main [[3D_Viewer]] page)



== How to create two canvasses displaying the same universe ==

You can download example source code for this HowTo [[3D_Viewer:_Example_code|here]].


This howto shows how to create two windows showing the same universe:

<source lang="java" first-line="21"; font-size: '100%';">
	// Open a hyperstack
	String path = "/home/bene/PhD/brains/template.tif";
	ImagePlus imp = IJ.openImage(path);

	// Create a universe and show it
	Image3DUniverse univ = new Image3DUniverse();
	univ.addVoltex(imp);
	univ.show();

	// retrieve some info about the 1st canvas
	int w = univ.getCanvas().getWidth();
	int h = univ.getCanvas().getHeight();

	// Create a new canvas and add it
	ImageCanvas3D canvas2 = new ImageCanvas3D(w, h);
	univ.getViewer().getView().addCanvas3D(canvas2);

	// create a new window, add the canvas and show it
	Frame f = new Frame();
	f.add(canvas2);
	f.pack();
	f.show();
</source>

After creating the universe as usual, a new <code>ImageCanvas3D</code> is created. To make it display the existing universe, it has to be registered with it. This is done with <code>univ.getViewer().getView().addCanvas3D(...)</code>.

All what is left to do is to create a new frame, add the canvas to it and finally show it.
