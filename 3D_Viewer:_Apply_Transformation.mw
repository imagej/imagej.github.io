(Return to the [[3D_Viewer:_Developer_Documentation|Developer Documentation]] page)<br>
(Return to the main [[3D_Viewer]] page)



== How to apply a specific transformation to a Content ==

You can download example source code for this HowTo [[3D_Viewer:_Example_code|here]].


Each Content may be transformed separately. In the application, this is for example done by the user by selecting a content and dragging with the mouse.

Transformations can also be applied very easy through the API. It is important to keep in mind that there are two distinct types of transformations: '''Local transformations''', which are individual for each Content, and '''global transformations''', which do not apply to individual Contents, but to the view of the universe.

Here, local transformations are discussed. How to change global transformations is shown in a later HowTo.

It is straightforward to apply a transformation to a Content; after creating the universe and adding a Content (see previous HowTo's), the following code shows how to create a transformation representing a 45 degree rotation around
the Y axis:
<source lang="java" first-line="31">
	// Add the image as an isosurface
	Content c = univ.addVoltex(imp);


	// Create a new Transform3D object
	Transform3D t3d = new Transform3D();

	// Make it a 45 degree rotation around the local y-axis
	t3d.rotY(45 * Math.PI / 180);

	// Apply the transformation to the Content. This concatenates
	// the previous present transformation with the specified one
	c.applyTransform(t3d);
</source>

<code>applyTransform()</code> concatenates a transformation with a previously existing transformation. So if the call to <code>applyTransformation()</code> in the above code is repeated, it results in an overall 90 degree rotation.

There exists another method, <code>setTransform()</code>, which does not concatenate transformations, but sets it fixed to the specified one:
<pre class="brush: java; first-line: 51; font-size: '100%';">
	// setTransform() does not concatenate, but sets the specified
	// transformation:
	c.setTransform(t3d);
</pre>

To reset the transformation of a Content to its initial transformation, which is just the identity, do the following:
<pre class="brush: java; first-line: 56; font-size: '100%';">
	// reset the transformation to the identity
	t3d.setIdentity();
	c.setTransform(t3d);
</pre>

There exists another method, <code>lock()</code>, which can be called for a Content and prevents further transformations.


=== Important methods of Content.java, regarding transformation ===
<pre class="brush: java; first-line: 1; font-size: '100%';">
	public void toggleLock();

	public void setLocked(boolean b);
	
	public void applyTransform(Transform3D transform);
	
	public void setTransform(Transform3D transform);
</pre>
