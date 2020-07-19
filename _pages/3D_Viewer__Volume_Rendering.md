(Return to the [[3D_Viewer:_Developer_Documentation|Developer Documentation]] page)<br>
(Return to the main [[3D_Viewer]] page)



== How to work with volume renderings ==

You can download example source code for this HowTo [[3D_Viewer:_Example_code|here]].

Before reading this HowTo, it may be helpful to read [[3D_Viewer:_Content_Structure|The relation between Content and Universe]].


It is possible to edit a volume rendering. <code>VoltexGroup</code> provides a method <code>fillRoi()</code>, which takes as input parameters a ROI and a fill value. The ROI (in canvas coordinates) is projected onto the volume, and the covered part of the volume is filled with the specified fill value.

Because <code>fillRoi()</code> is a method which only applies to volume renderings (orthoslices being an exception), this method is not located in Content.java, but in VoltexGroup.java.

<code>VoltexGroup</code> is a subclass of <code>ContentNode</code>, and can be retrieved from a <code>Content</code> (one which is displayed as a volume rendering) with <code>getContent()</code>:
<source lang="java" first-line="33">
	// Add the image as a volume
	Content c = univ.addVoltex(imp);


	// Retrieve the VoltexGroup
	VoltexGroup voltex = (VoltexGroup)c.getContent();

	// Define a ROI
	Roi roi = new OvalRoi(240, 220, 70, 50);

	// Define a fill color
	byte fillValue = (byte)100;

	// Fill the part of the volume which results from the
	// projection of the polygon onto the volume:
	voltex.fillRoi(univ.getCanvas(), roi, fillValue);
</source>

One thing worth to keep in mind is that also the original image is changed, and can in this form be saved, if desired.
