(Return to the [[3D_Viewer:_Developer_Documentation|Developer Documentation]] page)<br>
(Return to the main [[3D_Viewer]] page)



== How to work with surface plots ==

You can download example source code for this HowTo [[3D_Viewer:_Example_code|here]].


Before reading this HowTo, it may be helpful to read [[3D_Viewer:_Content_Structure|The relation between Content and Universe]].


Surface plots show a 2D image as a 3D plot, where the 3rd dimension is given by the intensity.

Because only one slice of an image stack can be displayed a time, <code>SurfacePlot2D</code> offers a method to set the displayed slice:
<source lang="java" first-line="36">
	// Add the image as a volume
	Content c = univ.addSurfacePlot(imp);


	// Retrieve the SurfacePlotGroup
	SurfacePlotGroup splot = (SurfacePlotGroup)c.getContent();

	// Scroll through the slices
	for(int i = 0; i &lt; 15; i++) {
		splot.setSlice(i + 1);

	}
</source>
