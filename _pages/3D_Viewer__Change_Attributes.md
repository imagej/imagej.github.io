(Return to the [[3D_Viewer:_Developer_Documentation|Developer Documentation]] page)<br>
(Return to the main [[3D_Viewer]] page)



== How to change color, transparency etc of a Content ==

You can download example source code for this HowTo [[3D_Viewer:_Example_code|here]].

Changing attributes like color and transparency of a Content is very easy. First, an image stack is opened, and a universe is created:
<source lang="java" first-line="22">
	// Open an image
	String path = "/home/bene/PhD/brains/template.tif";
	ImagePlus imp = IJ.openImage(path);
	new StackConverter(imp).convertToGray8();

	// Create a universe and show it
	Image3DUniverse univ = new Image3DUniverse();
	univ.show();
</source>

The stack is than displayed in the universe as an isosurface. Calling the <code>addXXX()</code> method returns a reference to the created Content:
<pre class="brush: java; first-line: 31; font-size: '100%';">
	// Add the image as an isosurface
	Content c = univ.addMesh(imp);
</pre>

This reference can now be used to change color and transparency, for example:
<pre class="brush: java; first-line: 35; font-size: '100%';">
	// Display the Content in purple
	c.setColor(new Color3f(0.5f, 0, 0.5f));
</pre>
<pre class="brush: java; first-line: 39; font-size: '100%';">
	// Make it transparent
	c.setTransparency(0.5f);
</pre>


=== Attributes of contents and their meanings ===

Each Content has the following list of attributes. Not all the attributes have a meaning for all display types; this is explained below:

* '''resampling factor:''' A factor specifying by which factor an image is downsampled before displaying. Downsampling will speed up rendering, and makes it possible for otherwise too large images to be displayed at all. As a side-effect, downsampling often results in smoothing.
* '''color:''' This is the color of Content. Null means, that the default color is used. The default color of a volume rendering and of orthoslices is the color taken from the image, that of an isosurface is the color of the isovalue. The default color of a surface plot is a gradient from red (intensity 0) to blue (intensity 255).
* '''transparency:''' The transparency of a Content.
* '''threshold:''' For isosurfaces, this is the iso-value (threshold) of the surface, which is assumed to be the value which separates the object from its background. For volumes and orthoslices, the threshold defines the lowest pixel intensity which is displayed. However, this may change in the future, so that is has no effect on orthoslices and volumes. For surface plots, the threshold has no meaning.
* '''channels:''' The color channels to be displayed. If displaying a greyscale image, the this attribute has no meaning. If, however, displaying color images, this attribute specifies which of the red, blue and/or green channel is displayed.
* '''shaded:''' This attribute has no effect for volume renderings and orthoslices, but for all surface types it defines whether the surfaces are shaded or shown in wireframe.


=== Important methods of Content.java for changing attributes ===
<pre class="brush: java; first-line: 1; font-size: '100%';">
	public void setChannels(boolean[] channels);

	public void setThreshold(int th);

	public void setShaded(boolean b); 
	
	public void setColor(Color3f color); 
	
	public void setTransparency(float transparency);
</pre>

For all the methods show here exist also getters.
