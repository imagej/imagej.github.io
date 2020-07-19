(Return to the [[3D_Viewer:_Developer_Documentation|Developer Documentation]] page)<br>
(Return to the main [[3D_Viewer]] page)



== How to highlight named points of a Content ==

You can download example source code for this HowTo [[3D_Viewer:_Example_code|here]].


Each <code>Content</code> owns a list of named points, which may e.g. be used to mark specific positions. By default, the point list is not shown, but it can be switched on, which displays the points as spheres in the universe and opens a dialog showing a list of the points.

The following example shows how to retrieve the point list of a <code>Content</code> and add a few points:
<source lang="java" first-line="31">
	// Add the image as a volume
	Content c = univ.addVoltex(imp);


	// Make the point list visible
	c.showPointList(true);

	// Retrieve the point list
	PointList pl = c.getPointList();

	// Add a few points
	pl.add(190, 450, 170);

	pl.add(330, 370, 300);

	pl.add(430, 90, 150);
</source>

The coordinates specified to create a new point are local coordinates of the corresponding <code>Content</code>.

Sometimes, it's convenient to select a point on the surface of a <code>Content</code> at a specific canvas position. This is also possible, by using the <code>Picker</code> class. A reference to a <code>Picker</code> object can be obtained from the universe:
<pre class="brush: java; first-line: 49; font-size: '100%';">
	// Add a point at a specific canvas position
	univ.getPicker().addPoint(c, 256, 256);
</pre>

The points have a default size, which can be changed:
<pre class="brush: java; first-line: 51; font-size: '100%';">
	// Change the size of the points
	float curr = c.getLandmarkPointSize();
	c.setLandmarkPointSize(curr * 2);
</pre>

To delete the first point in the list;
<pre class="brush: java; first-line: 58; font-size: '100%';">
	// delete the first point
	pl.remove(0);
</pre>

To rename a point:
<pre class="brush: java; first-line: 62; font-size: '100%';">
	// rename the now first point
	pl.rename(pl.get(0), "newName");
</pre>

To change the position of a point:
<pre class="brush: java; first-line: 66; font-size: '100%';">
	// change the position of the now first point
	pl.placePoint(pl.get(0), 190, 450, 170);
</pre>


=== Important methods regarding landmark points ===
Important methods are found in <code>Content.java</code> and <code>PointList.java</code>.

<b><code>Content.java:</code></b>
<pre class="brush: java; first-line: 1; font-size: '100%';">
	public void showPointList(boolean b);

	public PointList getPointList();

	public void loadPointList();

	public void savePointList();

	public float getLandmarkPointSize();

	public void setLandmarkPointSize(float r);
</pre>

<b><code>PointList.java</code>:</b>
<pre class="brush: java; first-line: 1; font-size: '100%';">
	public void add(BenesNamedPoint point);

	public void add(String name, double x, double y, double z);

	public void add(double x, double y, double z);

	public void remove(BenesNamedPoint point);

	public void remove(int i);

	public void clear();

	public void rename(BenesNamedPoint point, String name);

	public void up(BenesNamedPoint point);

	public void down(BenesNamedPoint point);

	public void highlight(BenesNamedPoint p);

	public void placePoint(BenesNamedPoint point,
				double x, double y, double z);

	public BenesNamedPoint get(int index);

	public int indexOf(BenesNamedPoint p);

	public int indexOfPointAt(double x, double y, double z, double tol);

	public BenesNamedPoint pointAt(double x, double y, double z, double tol);

	public int size();

	public BenesNamedPoint get(String name);

	public Iterator iterator();
</pre>

Both <code>Content.java</code> and <code>PointList.java</code> provide a <code>save()</code> and <code>load()</code> method, but it is highly recommended to use that of <code>Content.java</code>.
