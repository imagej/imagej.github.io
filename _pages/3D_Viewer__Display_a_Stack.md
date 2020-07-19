(Return to the [[3D_Viewer:_Developer_Documentation|Developer Documentation]] page)<br>
(Return to the main [[3D_Viewer]] page)



== How to create a universe and display an image stack as volume rendering, orthoslices, isosurface or surface plot ==

You can download example source code for this HowTo [[3D_Viewer:_Example_code|here]].

Creating a virtual universe and displaying an image stack in it is only a matter of a few steps.

The first thing to do is to open an image stack:
<source lang="java">
      // Open an image
      String path = "/home/bene/PhD/brains/template.tif";
      ImagePlus imp = IJ.openImage(path);
      new StackConverter(imp).convertToGray8();
</source>

Then a virtual universe is created and displayed in a window:
<pre class="brush: java; first-line: 25; font-size: '100%';">
      // Create a universe and show it
      Image3DUniverse univ = new Image3DUniverse();
      univ.show();
</pre>

A 3D object (=Content) is created and added to the universe by the following line of code:
<pre class="brush: java; first-line: 29; font-size: '100%';">
      // Add the image as a volume rendering
      Content c = univ.addVoltex(imp);
</pre>

In this case, the stack is displayed as a volume rendering. Volume renderings are created here by putting 2D slices of the stack one behind another. Different planes are thereby separated according to the pixel dimensions of the image. To each voxel, a transparency value is assigned, depending on its intensity. Black voxels are thereby fully transparent, whereas white ones are fully opaque.

There exist 4 types of Contents: Volume Renderings, Orthoslices, Isosurfaces and Surface Plots. Contents which were created from an ImagePlus can be transferred from one display type into another:
<pre class="brush: java; first-line: 33; font-size: '100%';">
      // Display the image as orthslices
      c.displayAs(Content.ORTHO);
</pre>

Orthoslices are three orthogonal slices through the volume.

Contents can be removed from the universe, identified by their name:
<pre class="brush: java; first-line: 37; font-size: '100%';">
      // Remove the Content
      univ.removeContent(c.getName());
</pre>

Here we add the stack as an isosurface:
<pre class="brush: java; first-line: 41; font-size: '100%';">
      // Add an isosurface
      c = univ.addMesh(imp);
</pre>
Isosurfaces are surfaces which are generated here by applying the marching cubes algorithm. This algorithm assumes that there is one intensity value in the stack which separates a 3D object from its background. Therefore,
the generated surface has theoretically everywhere the same (iso-)value. This value, also called the threshold of the surface, is adjustable, as will be seen later.

Finally, a Content can be displayed as a surface plot. A surface plot is a 3D representation of a 2D slide, where the 3rd dimension is formed by the image intensity;
<pre class="brush: java; first-line: 48; font-size: '100%';">
      c = univ.addSurfacePlot(imp);
</pre>

It is possible to remove all the contents of the universe together and to close the universe:
<pre class="brush: java; first-line: 51; font-size: '100%';">
      // remove all contents
      univ.removeAllContents();

      // close
      univ.close();
</pre>


=== Important methods of the universe class for handling Contents ===

The following methods exist for '''adding new Contents''':
In general, the methods exist in 2 forms, one short form and one long form;
the long form takes as parameters:
* '''image:''' the image to display
* '''color:''' a color for the newly created Content
* '''name:''' a (unique) name
* '''threshold:''' a threshold, which defines the isovalue of the surface
* '''resampling factor:''' downsampling factor, to speed up rendering.


In the short form, the missing parameters are set to their default values, which are:
* '''color:''' null
* '''name:''' the title of the image
* '''threshold:''' defined by the return value of <code>Content.getDefaultThreshold()</code>
* '''resampling factor:''' defined by the return value of <code>Content.getDefaultResamplingFactor()</code>

<pre class="brush: java; first-line: 1; font-size: '100%';">
      public Content addContent(ImagePlus image, int type);
      public Content addContent(ImagePlus image, Color3f color, String name,
            int thresh, boolean[] channels, int resf, int type);

      public Content addVoltex(ImagePlus image);
      public Content addVoltex(ImagePlus image, Color3f color,
            String name, int thresh, boolean[] channels, int resamplingF);

      public Content addOrthoslice(ImagePlus image);
      public Content addOrthoslice(ImagePlus image, Color3f color,
            String name, int thresh, boolean[] channels, int resamplingF);

      public Content addSurfacePlot(ImagePlus image);
      public Content addSurfacePlot(ImagePlus image, Color3f color,
            String name, int thresh, boolean[] channels, int resamplingF);

      public Content addMesh(ImagePlus img);
      public Content addMesh(ImagePlus image, Color3f color, String name,
            int threshold, boolean[] channels, int resamplingF);

      public Content addContent(Content c);
</pre>

The important methods for '''removing Contents''' are:
<pre class="brush: java; first-line: 1; font-size: '100%';">
      public void removeAllContents();
      public void removeContent(String name);
</pre>

And for '''retrieving Contents''', there exist:
<pre class="brush: java; first-line: 1; font-size: '100%';">
      public Iterator contents();
      public Collection getContents();
      public Content getContent(String name);
</pre>
