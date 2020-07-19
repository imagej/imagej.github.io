(Return to the [[3D_Viewer:_Developer_Documentation|Developer Documentation]] page)<br>
(Return to the main [[3D_Viewer]] page)



== How to display and show custom surfaces ==

You can download example source code for this HowTo [[3D_Viewer:_Example_code|here]].


Before reading this HowTo, it may be helpful to read [[3D_Viewer:_Content_Structure|The relation between Content and Universe]].


=== Simple meshes: lines, triangles, points, ... ===
One strength of the viewer is to make displaying custom meshes very straightforward. User-defined points, lines, triangle or quadrangle meshes can be displayed very easily:
<source lang="java" first-line="26">
	// Create a set of points
	List&lt;Point3f&gt; mesh = new ArrayList&lt;Point3f&gt;();
	mesh.add(new Point3f(-100, -100, 50));
	mesh.add(new Point3f(100, -100, 50));
	mesh.add(new Point3f(0, 100, 50));

	// Create a universe and show it
	Image3DUniverse univ = new Image3DUniverse();
	univ.showAttribute(
			Image3DUniverse.ATTRIBUTE_COORD_SYSTEM, false);
	univ.show();

	// Add the mesh as points
	CustomPointMesh cm = new CustomPointMesh(mesh);
	cm.setColor(new Color3f(0, 1, 0));
	univ.addCustomMesh(cm, "points");
	cm.setPointSize(10);

	// Add the mesh as a triangle
	CustomTriangleMesh tm = new CustomTriangleMesh(mesh);
	tm.setColor(new Color3f(0, 0, 1));
	Content c = univ.addCustomMesh(tm, "triangle");

	// Add the mesh as a triangle
	mesh.add(new Point3f(mesh.get(0))); // to close the path
	CustomLineMesh lm = new CustomLineMesh(
			mesh, CustomLineMesh.CONTINUOUS);
	lm.setColor(new Color3f(1, 0, 0));
	univ.addCustomMesh(lm, "lines");
	lm.setLineWidth(5);
	lm.setPattern(CustomLineMesh.DASH);

	// after adding the CustomMesh to the universe, we have a
	// reference to the Content, which can be used for further
	// modification
	c.setTransparency(0.5f);
</source>


=== More complex meshes, like spheres, tubes, etc ===
There exist also convenience methods in <code>ImageJ3DUniverse</code> for adding custom meshes, so that it is not necessary create the <code>CustomMesh</code> oneself. The corresponding methods can be found below.

To create more complex meshes, one can use the helper methods of the class <code>Mesh_Maker</code>:
<pre class="brush: java; first-line: 63; font-size: '100%';">
	// Use Mesh_Maker to create more complex surfaces like spheres,
	// tubes or discs:

	// define a sphere with center at the origin and radius 50
	double x = 0, y = 0, z = 30, r = 50;
	int meridians = 24;
	int parallels = 24;
	mesh = Mesh_Maker.createSphere(x, y, z, r, meridians, parallels);
	Color3f color = null;
	univ.addTriangleMesh(mesh, color, "sphere");
</pre>


=== Display many surfaces efficiently ===
Assume for example that one would wish to display 1000 spheres together. One could of course add each sphere individually, but there is a more efficient way:

One can use <code>Mesh_Maker</code> to create a mesh for each of these spheres, and concatenate the resulting lists, so that one obtains one big list, which can then be added as one <code>CustomMesh</code> (in case of spheres this would be a <code>CustomTriangleMesh</code>).

This works only if the type of all the meshes is the same; one can not combine line meshes with point meshes, for example.

There is also another disadvantage; adding each sphere individually means that each sphere is represented as an individual <code>Content</code>, whose attributes can be changed separately. Adding all the spheres as a combined mesh will result in only one <code>Content</code>, whose attributes will affect all the spheres.


=== The class hierarchy of the <code>customnode</code> package ===
[[Image:3DViewer-class-diagram-customnode.png|thumb|center|590px|Relation between classes in the <code>customnode</code> package.]]


<code>CustomMeshNode</code> extends <code>ContentNode</code>, and therefore implements all the abstract methods in <code>ContentNode</code>. It has a reference to <code>CustomMesh</code>, which is an abstract class, implemented by <code>CustomPointMesh</code>, <code>CustomLineMesh</code>, <code>CustomTriangleMesh</code> and <code>CustomQuadMesh</code>.


=== Full control over custom nodes ===
<code>CustomMesh</code> implements the basic functions, as well as a default Java3D <code>Appearance</code> object, which is used in the subclasses. Since <code>CustomMesh</code> extends the <code>Shape3D</code> class, it provides a methods <code>setAppearance()</code> and <code>setGeometry()</code>, which give Java3D-experienced users full control over the content of their <code>CustomMeshNode</code>.



=== Important methods ===
<code><b>Image3DUniverse:</b></code>
<source lang="java" first-line="1">
public Content addCustomMesh(CustomMesh mesh, String name);

public Content addLineMesh(List&lt;Point3f&gt; mesh, Color3f color, String name,
		boolean strips);

public Content addPointMesh(List&lt;Point3f&gt; mesh, Color3f color, String name);

public Content addQuadMesh(List&lt;Point3f&gt; mesh, Color3f color, String name);

public Content addTriangleMesh(List&lt;Point3f&gt; mesh, Color3f color, String name);
</source>

<code><b>CustomMesh:</b></code><br>
The methods of <code>CustomMesh</code> are inherited by <code>CustomLineMesh</code>, <code>CustomPointMesh</code>,<code>CustomTriangleMesh</code> and <code>CustomQuadMesh</code>. They can be used next to similar functions which are provided by the <code>Content</code> class, once the wrapping <code>Content</code> is created, however, it is recommended to use the methods there.
<pre class="brush: java; first-line: 1; font-size: '100%';">
	public Color3f getColor();

	public void setColor(Color3f color);

	public float getTransparency();

	public void setTransparency(float transparency);

	public boolean isShaded();

	public void setShaded(boolean b);
</pre>

<code><b>CustomLineMesh:</b></code>
<pre class="brush: java; first-line: 1; font-size: '100%';">
	public void setPattern(int pattern);
	
	public void setAntiAliasing(boolean b);
	
	public void setLineWidth(float w);
</pre>

<code><b>CustomPointMesh:</b></code>
<pre class="brush: java; first-line: 1; font-size: '100%';">
	public void setPointSize(float pointsize);
	
	public void setAntiAliasing(boolean b);
</pre>

<code><b>CustomTriangleMesh:</b></code><br>
no additional methods.

<code><b>CustomQuadMesh:</b></code><br>
no additional methods.

<code><b>Mesh_Maker:</b></code>
<pre class="brush: java; first-line: 1; font-size: '100%';">
	static public List createSphere(double x, double y, double z, double r);

	static public List createSphere(double x, double y, double z, double r,
				int meridians, int parallels);

	static public List createTube(double[] x,  double[] y,  double[] z,
				double[] r,  int parallels,  boolean do_resample);

	static public List createDisc(double x, double y, double z,
				double nx, double ny, double nz,
				double radius,
				int edgePoints );
</pre>
