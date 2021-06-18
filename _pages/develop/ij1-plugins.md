---
title: Developing Plugins for ImageJ 1.x
section: Extend:Development:Guides
---

{% include notice icon="imagej-1.x" content='This page explains how to develop plugins with the ImageJ 1.x API. If you start developing a new plugin today, it is highly recommended to [develop for ImageJ2](/develop/plugins).' %}

{% include project content='ImageJ 1.x' %}

# Plugin, script or macro?

If you want to add a new feature to ImageJ, you can either [write a script or macro](/scripting), or do it as a plugin. Scripts and macros are easier to learn, and hence often faster to develop. However, Java offers numerous advantages including better performance in many cases, as well as compile-time safety of the code.

If you are not sure which to choose, take a look at the [Scripting Help](/scripting) and try your hand at a script in a language that appeals to you. You can always convert it to a Java plugin later if the execution speed becomes an issue.

If you are certain that you want to write a plugin in Java, keep on reading!

# Plugins

## What are plugins (in terms of files)?

-   Plugins are a dedicated mechanism for extending ImageJ/Fiji
-   A plugin consists of one or more Java classes living inside a `.jar` file in `plugins/` (exception: a single `.class` file)
-   All plugin `.jar` (or `.class`) files must contain an underscore in their name
-   Plugins can use 3rd party libraries; in Fiji, store them in the `jars/` directory (in ImageJ you have to put them into the `plugins/` directory, and to avoid funny menu entries in the {% include bc path="Plugins" %} menu, you should rename them if their name contains an underscore)

## Updating plugins

-   After storing the `.jar` file(s) into the `plugins/` (or `jars/`) directory, call {% include bc path='Help | Refresh Menus'%} or restart Fiji
-   If the respective plugin is in-use, you might get funny results when refreshing the menus, due to limitations in Sun Java's handling of `.jar` files.

## What are plugins (in terms of menu entries)?

-   If the `.jar` file contains a file called `plugins.config`, it determines what menu items are provided by the plugin
-   If the `.jar` file does not contain a file called `plugins.config`, all contained classes containing an underscore in their name are added to the {% include bc path="Plugins" %} menu

A `plugins.config` file looks like this:

```shell
# Comments (such as title, author, etc)
#
# The other lines have this format:
#  Menu, "Menu Item", ClassName
# Example:

Plugins > Analyze, "Plot", fiji.Plot
```

A class can be reused for multiple menu entries, by passing an optional argument in the `plugins.config` file:

```shell
# Example how to reuse a Java class

Help, "Bug report", fiji.Send("bug")
Help, "Contact", fiji.Send("contact")
```

## What are plugins (in terms of Java code)?

There are two different types of plugins:

-   Plugins which operate on one image
-   All other plugins (including plugins which require more than one input images, or image format loaders)

A filter plugin looks like this:

```java
public class My_Plugin implements PlugInFilter {
    public int setup(String arg, ImagePlus image) {
        return DOES_ALL;
    }
    public void run(ImageProcessor ip) {
        // Here is the action
    }
}

```
A general plugin looks like this:

```java
public class My_Plugin implements PlugIn {
    public void run(String arg) {
        // Here is the action
    }
}
```

{% include notice icon="note" content="It is of course possible to implement a filter plugin using the `PlugIn` interface, but ImageJ will perform more convenience functions if you use the `PlugInFilter` interface, such as verifying that there is an image and that it is of the correct type, and error handling." %}

## Limitations

-   Plugins can only implement menu entries (in particular, they cannot provide tools in the toolbar)
-   Some functions which are easy to call via macros are not available via the public Java API (e.g. {% include bc path='Image | Stacks | Plot Z-axis profile...'%})
-   It is often quicker to write macros

# Getting started with Maven

The {% include github org='imagej' repo='example-legacy-plugin' label='example-legacy-plugin project' %} provides a working example, and documentation, illustrating how an ImageJ plugin should be structured from a "best practices in Maven" point of view.

Using this project requires a basic understanding of [Git](/develop/git) and [Maven](/develop/maven); thus if you are already familiar with the ImageJ 1.x API, this is a reasonable starting point to learn the [project management](/develop/project-management) tools used in [ImageJ2 development](/develop/plugins).

# Basic workflow

All plugin development tends to follow a consistent "Design - Build - Test" workflow. Practically, this looks like:

-   Make changes to the source code (e.g. in [Eclipse](/develop/eclipse))
-   Build your plugin's .jar from the source code (e.g. with [Maven](/develop/maven))
-   Move the plugin to the [plugins directory](/plugins#installing-plugins-manually) of an existing ImageJ installation
-   (Re)start ImageJ and run the plugin to test the behavior

... and repeat until your plugin is working as intended.

# ImageJ's API

The source of the various Fiji-related projects is spread over several source code repositories, and so is their API documentation. An overview of all the javadoc resources can be found on [this page with javadoc links](http://javadoc.imagej.net/).

## The class *IJ*

The class {% include github org='imagej' repo='ImageJA' branch='master' path='src/main/java/ij/IJ.java' label='ij.IJ' %} is a convenience class with many static functions. Two of them are particularly useful for debugging:

```java
// output into the Log window
IJ.log("Hello, World!");

// Show a message window
IJ.showMessage("Hello, World!");
```

## The class *ImageJ*

The class {% include github org='imagej' repo='ImageJA' branch='master' path='src/main/java/ij/ImageJ.java' label='ij.ImageJ' %} implements the main window of ImageJ / Fiji, and you can access it via *ij.IJ*'s static method *getInstance()*:

```java
// check if ImageJ is used interactively
if (IJ.getInstance() != null)
    IJ.showMessage("Interactive!");
```

Typically, all you do with that instance is to test whether ImageJ is used as a library (in which case the instance is *null*).

## The class *WindowManager*

Use the class {% include github org='imagej' repo='ImageJA' branch='master' path='src/main/java/ij/WindowManager.java' label='ij.WindowManager' %} to access the ImageJ windows / images:

```java
// how many windows / images are active?
IJ.log("There are "
    + WindowManager.getNonImageWindows().length
    + " windows and "
    + WindowManager.getImageCount()
    + " images!");

```

When implementing a filter plugin, you usually do not need to access *WindowManager* directly.

## The hierarchy of the classes representing an image

All images are represented as instances of {% include github org='imagej' repo='ImageJA' branch='master' path='src/main/java/ij/ImagePlus.java' label='ij.ImagePlus' %}. This class wraps an {% include github org='imagej' repo='ImageJA' branch='master' path='src/main/java/ij/ImageStack.java' label='ij.ImageStack' %} of slices. Slices are data-type dependent instances of {% include github org='imagej' repo='ImageJA' branch='master' path='src/main/java/ij/process/ImageProcessor.java' label='ij.process.ImageProcessor' %}: {% include github org='imagej' repo='ImageJA' branch='master' path='src/main/java/ij/process/ByteProcessor.java' label='ij.process.ByteProcessor' %}, {% include github org='imagej' repo='ImageJA' branch='master' path='src/main/java/ij/process/ShortProcessor.java' label='ij.process.ShortProcessor' %}, {% include github org='imagej' repo='ImageJA' branch='master' path='src/main/java/ij/process/FloatProcessor.java' label='ij.process.FloatProcessor' %}, and {% include github org='imagej' repo='ImageJA' branch='master' path='src/main/java/ij/process/ColorProcessor.java' label='ij.process.ColorProcessor' %}. Or graphically:

<figure><img src="/media/image-class-hierarchy.png" title="Image_Class_Hierarchy.png" width="600" alt="Image_Class_Hierarchy.png" /><figcaption aria-hidden="true">Image_Class_Hierarchy.png</figcaption></figure>

Example usage:
```java
// get the current image
ImagePlus image = WindowManager.getCurrentImage();

// get the current slice
ImageProcessor ip = image.getProcessor();

// duplicate the slice
ImageProcessor ip2 = ip.duplicate();
```
## Beyond 3D: Hyperstacks

In ImageJ, you can represent more than 3 dimensions in an image: *X, Y, Z, channels, frames (time)*. Internally, these 5-dimensional images are still represented as stacks of images (essentially, a one-dimensional array of *ImageProcessor* instances). The *ImagePlus* class knows how to transform *(channel, z-slice, frame)* triplets into the corresponding index in the *ImageStack*, though:

```java
// get the n'th slice (1 <= n <= N!)
ImageStack stack = image.getStack();
int size = stack.getSize();
ImageProcessor ip = stack.getProcessor(size);

// get the ImageProcessor for a given
// (channel, slice, frame) triple
int index = image.getStackIndex(channel, slice, frame);
ImageProcessor ip = stack.getProcessor(index);
```

{% include notice icon="note" content="For historical reasons, slice indices (and channel and frame indices as well) start at *1*. This is in contrast, e.g. to the x, y coordinates, which start at *0* (as one might be used to from other computer languages except BASIC, Pascal and [MATLAB](/scripting/matlab))." %}

## Working with the pixels' values

The subclasses of the *ImageProcessor* class implement 2-dimensional images for specific data types (8-bit, 16-bit, 32-bit floating point, and RGB color). Let's start with the grayscale ones:

```java
// get one pixel's value (slow)
float value = ip.getf(0, 0);
```

This would get you the value of the top left pixel of an object *ip* of type *ImageProcessor*, as a 32-bit floating point value.

Since the original data type might be 8-bit, that operation can require a *cast* (type conversion), which can be quite costly when done very often. Therefore, if you know the data type of your images, you can write more efficient (but data type depednent) code:

```java
// get all type-specific pixels (fast)
// in this example, a ByteProcessor
byte[] pixels = (byte[])ip.getPixels();
int w = ip.getWidth(), h = ip.getHeight();
for (int j = 0; j < h; j++)
	for (int i = 0; i < w; i++) {
		// Java has no unsigned 8-bit data type, so we need to perform Boolean arithmetics
		int value = pixels[i + w * j] & 0xff;
		...
	}
```

{% include notice icon="note" content="The previous example assumes that your images are 8-bit (unsigned, i.e. values between 0 and 255) images. Since Java has no data type for unsigned 8-bit integers, we have to use the `& 0xff` dance (a *Boolean AND* operation) to make sure that the value is treated as unsigned integer." %}

Accessing the pixels' values gets trickier when it comes to RGB images. These use the native data type *int* (32-bit signed integer) to encode 3 color channels à 8-bit, packed into the lower 24 bits (note that ImageJ might store things in the upper 8 bits, so you cannot assume them to be 0). Therefore, the *getf()* method of the *ImageProcessor* class does not make sense on color images. You have to access the pixels like this:

```java
// get all pixels of a ColorProcessor
int[] pixels = (int[])ip.getPixels();
int w = ip.getWidth(), h = ip.getHeight();
for (int j = 0; j < h; j++)
	for (int i = 0; i < w; i++) {
		int value = pixels[i + w * j];
		// value is a bit-packed RGB value
		int red = value & 0xff;
		int green = (value >> 8) & 0xff;
		int blue = (value >> 16) & 0xff;
}
```

## Making new images

To make a new image - be it 2, 3, 4 or 5 dimensional - you have to create instances of *ImageProcessor* first. Example:

```java
ImageProcessor gradient(double angle, int w, int h) {
	float c = (float)Math.cos(angle);
	float s = (float)Math.sin(angle);
	float[] p = new float[w * h];
	for (int j = 0; j < h; j++)
		for (int i = 0; i < w; i++)
			p[i + w *j] = (i – w / 2) * c + (j – h / 2) * s;
	return new FloatProcessor(w, h, p, null);
}
```

This example implements a method that shows a gradient along a given angle. You can use this method to build a 3-dimensional image:

```java
// make a stack of gradients
int w = 512, h = 512;
ImageStack stack = new ImageStack(w, h);
for (int i = 0; i < 180; i++)
	stack.addSlice("", gradient(i / 180f * 2 * Math.PI, w, h));
ImagePlus image = new ImagePlus("stack", stack);
// you do not need to show intermediate images
image.show();
```

## Informing the user about the progress

This code snippet shows you how to update the progress bar and the status text:

```java
// show a progress bar
for (int i = 0; i < 100; i++) {
	// do something
	IJ.showProgress(i + 1, 100);
}

// show something in the status bar
IJ.showStatus("Hello, world!");
```

{% include notice icon="note" content="Calling `IJ.showProgress(n, n);` will hide the progress bar; Therefore, it makes sense to update the progress bar at the *end* of a loop iteration, so that after the last iteration, the progress bar is hidden." %}

## Frequently used operators

The [ImageProcessor](http://javadoc.scijava.org/ImageJ1/ij/ij/process/ImageProcessor.html) class has a few methods such as *smooth()*, *sharpen()*, *findEdges()*, etc

**Tip:** use the Script Editor's functions in the *Tools* menu:

-   *Open Help for Class...* (opens the JavaDoc for a class in a browser),
-   *Open .java file for class...* (requires the respective source files to be present in the Fiji directory, such as after [Downloading and Building Fiji From Source](/software/fiji/building-from-source), or
-   *Open .java file for menu item...* (also needs the source files).

## Plots

You can show a plot window very easily using the [Plot](http://javadoc.scijava.org/ImageJ1/ij/ij/gui/Plot.html) class:

```java
void plot(double[] values) {
	double[] x = new double[values.length];
	for (int i = 0; i < x.length; i++)
		x[i] = i;
	Plot plot = new Plot("Plot window", "x", "values", x, values);
	plot.show();
}
```

It is almost as easy to put multiple plots into one window:

```java
void plot(double[] values, double[] values2) {
	double[] x = new double[values.length];
	for (int i = 0; i < x.length; i++)
		x[i] = i;
	Plot plot = new Plot("Plot window", "x", "values", x, values);
	plot.setColor(Color.RED);
	plot.draw();
	plot.addPoints(x, values2, Plot.LINE);
	plot.show();
}
```

To update the contents of a plot window, remember the return value of *plot.show()* which is a [PlotWindow](http://javadoc.scijava.org/ImageJ1/ij/ij/gui/PlotWindow.html), and use its *drawPlot()* method:

```java
void plot(double[] values) {
	...
	PlotWindow plotWindow = plot.show();
	...
	Plot plot = new Plot("Plot window", "x", "values", x, values);
	plotWindow.drawPlot(plot);
}
```

## The results table

Whenever your plugin quantifies things in the images, you might want to output the values in a results table:

```java
ResultsTable rt = Analyzer.getResultsTable();
if (rt == null) {
	rt = new ResultsTable();
	Analyzer.setResultsTable(rt);
}
for (int i = 1; i <= 10; i++) {
	rt.incrementCounter();
	rt.addValue("i", i);
	rt.addValue("log", Math.log(i));
}
rt.show("Results");
```

## Regions of interest

You can access the ROIs in the following fashion:

```java
// testing ROI type
if (roi != null && roi.getType() == Roi.POLYGON)
	IJ.log("This is a polygon!");
showCoordinates((PolygonRoi)roi);

...

// get ROI coordinates
void showCoordinates(PolygonRoi polygon) {
	PolygonRoi polygon = (PolygonRoi)roi;
	int[] x = polygon.getXCoordinates();
	int[] y = polygon.getYCoordinates();
	Rectangle bounds = polygon.getBounds();
	for (int i = 0; i < x.length; i++)
		// x, y are relative to the bounds' origin
		IJ.log("point " + i + ": " + (x[i] + bounds.x) + (y[i] + bounds.y));
}
```

{% include notice icon="note" content="If the image has no ROI set, then `getRoi()` will return `null`, so you *must* check whether `roi != null` before accessing fields or methods on the object." %}

Of course, you can also set ROIs programmatically:

```java
// rectangular ROI
Roi roi = new Roi(10, 10, 90, 90);
image.setRoi(roi);

// oval ROI
Roi roi = new OvalRoi(10, 10, 90, 90);
image.setRoi(roi);
```

## Calling ImageJ2 from ImageJ 1.x

You can use ImageJ2-specific functionality from within an ImageJ 1.x plugin. For example, ImageJ2 provides a spreadsheet-like results table that supports string cells. You can write an ImageJ 1.x plugin that produces such a spreadsheet, displaying it onscreen.

See the {% include github org='imagej' repo='tutorials' branch='master' path='howtos/src/main/java/howto/adv/ModernFromLegacy.java' label='ModernFromLegacy.java' %} example from the ImageJ tutorial code.

## Further tips

Please see also the developers tips how to [use ImageJ's API effectively](/develop/tips#using-imagej-effectively).

# Next steps

See guides on:

-   [Developing in Eclipse](/develop/eclipse#create-the-eclipse-projects)
-   [Plugin distribution](/contribute/distributing)
-   [Development lifecycle](/develop/releasing)
-   [Debugging practice](/develop/debugging-exercises)
-   [ImageJ1-ImageJ2 cheat sheet](/develop/ij1-ij2-cheat-sheet)
