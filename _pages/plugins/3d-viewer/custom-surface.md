---
mediawiki: 3D_Viewer:_Custom_Surface
title: 3D Viewer › Custom Surface
nav-links: true
nav-title: Custom Surface
---

## How to display and show custom surfaces

You can download example source code for this HowTo [here](/plugins/3d-viewer/example-code).

Before reading this HowTo, it may be helpful to read [The relation between Content and Universe](/plugins/3d-viewer/content-structure).

### Simple meshes: lines, triangles, points, ...

One strength of the viewer is to make displaying custom meshes very straightforward. User-defined points, lines, triangle or quadrangle meshes can be displayed very easily:

```java
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
```
### More complex meshes, like spheres, tubes, etc

There exist also convenience methods in `ImageJ3DUniverse` for adding custom meshes, so that it is not necessary create the `CustomMesh` oneself. The corresponding methods can be found below.

To create more complex meshes, one can use the helper methods of the class `Mesh_Maker`:

```java
// Use Mesh_Maker to create more complex surfaces like spheres,
// tubes or discs:

// define a sphere with center at the origin and radius 50
double x = 0, y = 0, z = 30, r = 50;
int meridians = 24;
int parallels = 24;
mesh = Mesh_Maker.createSphere(x, y, z, r, meridians, parallels);
Color3f color = null;
univ.addTriangleMesh(mesh, color, "sphere");
```
### Display many surfaces efficiently

Assume for example that one would wish to display 1000 spheres together. One could of course add each sphere individually, but there is a more efficient way:

One can use `Mesh_Maker` to create a mesh for each of these spheres, and concatenate the resulting lists, so that one obtains one big list, which can then be added as one `CustomMesh` (in case of spheres this would be a `CustomTriangleMesh`).

This works only if the type of all the meshes is the same; one can not combine line meshes with point meshes, for example.

There is also another disadvantage; adding each sphere individually means that each sphere is represented as an individual `Content`, whose attributes can be changed separately. Adding all the spheres as a combined mesh will result in only one `Content`, whose attributes will affect all the spheres.

### The class hierarchy of the `customnode` package

{% include thumbnail src='/media/plugins/3d-viewer/3dviewer-class-diagram-customnode.png' title='Relation between classes in the `customnode` package.'%}

`CustomMeshNode` extends `ContentNode`, and therefore implements all the abstract methods in `ContentNode`. It has a reference to `CustomMesh`, which is an abstract class, implemented by `CustomPointMesh`, `CustomLineMesh`, `CustomTriangleMesh` and `CustomQuadMesh`.

### Full control over custom nodes

`CustomMesh` implements the basic functions, as well as a default Java3D `Appearance` object, which is used in the subclasses. Since `CustomMesh` extends the `Shape3D` class, it provides a methods `setAppearance()` and `setGeometry()`, which give Java3D-experienced users full control over the content of their `CustomMeshNode`.

### Important methods

<b>`Image3DUniverse:`</b>

    public Content addCustomMesh(CustomMesh mesh, String name);

    public Content addLineMesh(List&lt;Point3f&gt; mesh, Color3f color, String name,
            boolean strips);

    public Content addPointMesh(List&lt;Point3f&gt; mesh, Color3f color, String name);

    public Content addQuadMesh(List&lt;Point3f&gt; mesh, Color3f color, String name);

    public Content addTriangleMesh(List&lt;Point3f&gt; mesh, Color3f color, String name);

<b>`CustomMesh:`</b>  
The methods of `CustomMesh` are inherited by `CustomLineMesh`, `CustomPointMesh`,`CustomTriangleMesh` and `CustomQuadMesh`. They can be used next to similar functions which are provided by the `Content` class, once the wrapping `Content` is created, however, it is recommended to use the methods there.

        public Color3f getColor();

        public void setColor(Color3f color);

        public float getTransparency();

        public void setTransparency(float transparency);

        public boolean isShaded();

        public void setShaded(boolean b);

<b>`CustomLineMesh:`</b>

        public void setPattern(int pattern);
        
        public void setAntiAliasing(boolean b);
        
        public void setLineWidth(float w);

<b>`CustomPointMesh:`</b>

        public void setPointSize(float pointsize);
        
        public void setAntiAliasing(boolean b);

<b>`CustomTriangleMesh:`</b>  
no additional methods.

<b>`CustomQuadMesh:`</b>  
no additional methods.

<b>`Mesh_Maker:`</b>

        static public List createSphere(double x, double y, double z, double r);

        static public List createSphere(double x, double y, double z, double r,
                    int meridians, int parallels);

        static public List createTube(double[] x,  double[] y,  double[] z,
                    double[] r,  int parallels,  boolean do_resample);

        static public List createDisc(double x, double y, double z,
                    double nx, double ny, double nz,
                    double radius,
                    int edgePoints );
