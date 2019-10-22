(Return to the [[3D_Viewer:_Developer_Documentation|Developer Documentation]] page)<br>
(Return to the main [[3D_Viewer]] page)



== How to work with orthoslices ==

You can download example source code for this HowTo [[3D_Viewer:_Example_code|here]].


Before reading this HowTo, it may be helpful to read [[3D_Viewer:_Content_Structure|The relation between Content and Universe]].


When displaying a <code>Content</code> as orthoslices, the corresponding <code>ContentNode</code> of the <code>Content</code> is of type <code>OrthoGroup</code>.

<code>OrthoGroup</code> extends <code>VoltexGroup</code>, and therefore also shares its functionality regarding volume editing. Additionally, <code>OrthoGroup</code> provides functions for adjusting the displayed slices (planes) and hiding them:
<source lang="java" first-line="31";>
// Add the image as a volume
Content c = univ.addOrthoslice(imp);


// Retrieve the OrthoGroup
OrthoGroup ortho = (OrthoGroup)c.getContent();

for(int i = 0; i &lt; 10; i++) {
	ortho.increase(AxisConstants.Z_AXIS);
	sleep(1);
}

// Hide the x-axis
ortho.setVisible(AxisConstants.X_AXIS, false);


// Show it again and hide the z-axis
ortho.setVisible(AxisConstants.X_AXIS, true);
ortho.setVisible(AxisConstants.Z_AXIS, false);


// Show it again
ortho.setVisible(AxisConstants.Z_AXIS, true);
</source>

'''Important methods of <code>OrthoGroup</code>'''
<pre class="brush: java; first-line: 1; font-size: '100%';">
	public void setSlice(int axis, int v);

	public int getSlice(int axis);

	public void decrease(int axis);

	public void increase(int axis);

	public boolean isVisible(int axis);

	public void setVisible(int axis, boolean b);
</pre>
