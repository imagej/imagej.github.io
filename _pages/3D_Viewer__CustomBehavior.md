(Return to the [[3D_Viewer:_Developer_Documentation|Developer Documentation]] page)<br>
(Return to the main [[3D_Viewer]] page)



== How to catch and handle events on the 3D canvas ==

You can download example source code for this HowTo [[3D_Viewer:_Example_code|here]].


This howto shows how to catch and handle mouse or key events:

Where you set up the universe, call <code>setInteractiveBehavior(...)</code>:
<source lang="java" first-line="40">
	univ = new Image3DUniverse();
	univ.show();
	Content c = univ.addCustomMesh(...);

	// this is necessary for catching the mouse events
	univ.setInteractiveBehavior(new CustomBehavior(univ, c));
</source>

Then create a new (maybe inner) class that extends <code>ij3d.behaviors.InteractiveBehavior</code>.
<pre class="brush: java; first-line: 51; font-size: '100%';">
private class CustomBehavior extends InteractiveBehavior {

	private Content c;
	
	CustomBehavior(Image3DUniverse univ, Content c) {
		super(univ);
		this.c = c;
	}

	public void doProcess(MouseEvent e) {
		if(!e.isControlDown() ||
			e.getID() != MouseEvent.MOUSE_PRESSED) {
			super.doProcess(e);
			return;
		}
		// Get the point on the geometry where the mouse
		// press occurred
		Point3d p = univ.getPicker().
			getPickPointGeometry(c, e.getX(), e.getY());
		if(p == null)
			return;

		IJ.showMessage("Picked " + new Point3f(p));
	}
}
</pre>

In the example shown above, mouse presses with hold-down control key are captured. The universe's Picker object is used to obtain the picked point (i.e. the point where the mouse ray intersects the object). In the example, the point's coordinates are just displayed on the screen then.

'''Important:'''<br>
Be careful to call <code>super.process(...)</code> when necessary to retain normal (rotating, translating) behavior as desired.
