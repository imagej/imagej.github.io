---
title: Tips for developers
section: Extend:Development:Guides
---

An unsorted list of hints that you might find useful.

# Compile & Execute a Class

You do not need to call `javac` yourself with a long *classpath*:

```shell
$ ./fiji --javac YourClass.java
```

and you can call its `main()` method just as easy:

```shell
$ ./fiji YourClass.class argument1 argument2
```

# Rapidly Prototype a Plugin

It is often easier to start out with a Jython, JRuby or BeanShell script, as you do not have to care about strict typing, exceptions or recompiling. Just place your script (with the correct extension -- .py, .rb or .bsh) into the plugins/ folder and execute the script. Fiji will always execute the current version of the script, so you can edit and run the script without restarting Fiji.

Of course, it is even more convenient to use the [Script Editor](/scripting/script-editor)...

Once you have working code, you can turn it into a proper plugin (this is easiest with BeanShell, as its syntax is closest to Java already), adding strict typing and exception handling as needed.

# Find the .jar File Containing a Certain Class

Sometimes, the compiler complains about a class not having a certain method or interface, but you *know* it must contain it. More often than not, that class exists in different versions in your classpath. Find out with

```shell
$ ./fiji bin/find-jar-for-class.py the.class.youre.looking.For
```

If you want to do that with an installed Fiji (i.e. when bin/ is missing), you can start the [Script Editor](/scripting/script-editor) and execute a BeanShell like this:

```java
 import ij.IJ;

 print(IJ.getClassLoader()
         .loadClass("the.class.youre.looking.For")
         .getResource("For.class").toString());
```

This will output the URL to the *.class* file, including the path to the enclosing *.jar* file.

# Using ImageJ Effectively

ImageJ has a simple API, but it is also big, so here are a few pointers to some useful parts.

## How to read a file into an ImagePlus

```java
 ImagePlus image = IJ.openImage(path);
```

## How to get the current image

```java
ImagePlus img = WindowManager.getCurrentImage();  // current image
ImageProcessor ip = img.getProcessor();  // current slice
```

## Making a new image stack -- quickly!

```java
ImagePlus image = IJ.createImage("my image", "RGB", 640, 480, 20);
```

## How to display an exception in a window

This is especially useful on Windows, where you usually do not see the console:

```java
IJ.handleException(exception);
```

This is available since ImageJ 1.43g, as well as the option to set a different exception handler using

```java
 IJ.setExceptionHandler(new IJ.ExceptionHandler() {
    public void handle(Throwable exception) {
       // do something
    }
 });
```

## How to show a plot

ImageJ offers the `ij.gui.Plot` class to make a window showing a plot. Use it like this:

```java
Plot plot = new Plot("The window title", "labels on the x-axis", "labels on the y-axis",
    float_array_of_x_values, float_array_of_y_values);
plot.show();
```

Instead of *float* arrays, you can also use *double* arrays.

If you need to update the plot at some stage, you need to save the return value of *show()*:

```java
Plot plot = new Plot("The window title", "labels on the x-axis", "labels on the y-axis",
    float_array_of_x_values, float_array_of_y_values);
PlotWindow window = plot.show();
// ...
Plot update = new Plot("Dummy", "x labels", "y labels", x_values, y_values);
window.drawPlot(update);
```

To add another plot to the same window, use the `addPoints()` method:

```java
plot.addPoints(float_array_of_x_values, float_array_of_y_values, Plot.LINE);
```

The plots can be drawn in different colors like this:

```java
Plot plot = new Plot("The window title", "labels on the x-axis", "labels on the y-axis",
    float_array_of_x_values, float_array_of_y_values);
plot.setColor(Color.RED);
plot.draw();
plot.addPoints(float_array_of_x_values, another_float_array_of_y_values, Plot.LINE);
plot.setColor(Color.BLUE);
plot.draw();
```

You might need to adjust the bounding box if the second plot does not match the bounding box of the first one by using the `setLimits()` method before the call to `plot.draw();`

## Duplicate, or convert between, `ImageProcessor` types

The `ImageProcessor` class has several useful methods: [`duplicate()`](https://javadoc.scijava.org/ImageJ1/ij/process/ImageProcessor.html#duplicate>()), [`convertToByte()`](https://javadoc.scijava.org/ImageJ1/ij/process/ImageProcessor.html#convertToByte(boolean)), [`convertToFloat()`](https://javadoc.scijava.org/ImageJ1/ij/process/ImageProcessor.html#convertToFloat), [`convertToRGB()`](https://javadoc.scijava.org/ImageJ1/ij/process/ImageProcessor.html#convertToRGB()), and [`convertToShort()`](https://javadoc.scijava.org/ImageJ1/ij/process/ImageProcessor.html#convertToShort(boolean)).

This [class](https://javadoc.scijava.org/ImageJ1/ij/process/ImageProcessor.html) also has some other goodies, such as methods for convolution.

## How to store settings persistently

ImageJ (and therefore Fiji, too) has a way to store key/value pairs persistently, i.e. they are available even after a restart. The settings are stored in a file called *IJ\_Prefs.txt* in the subdirectory called *.imagej/* in your home directory (on Windows, directly in your home directory; on Mac, in *\~/Library/Preferences*).

{% include notice icon="note" content="The settings are only saved upon *regular* exit of Fiji; If you kill the process, or if the Java Runtime crashes, they are *not* saved. You can ask for the settings to be saved explicitly, though." %}

Example:

```java
import ij.Prefs;

...

    // save key/value pairs
    Prefs.set("my.persistent.name", "Grizzly Adams");
    Prefs.set("my.persistent.number", 10);

    ....

    // retrieve the values (with default values)
    int myNumber = Prefs.get("my.persistent.number", 0);

    // explicitly save the preferences _now_
    Prefs.savePreferences();

{% include notice icon="note" content="Do *not* use the `getString()` or `getInt()`; These methods do not have any setter methods, and they do *not* access the same values as the `get()` method (`get()` actually prefixes the keys with a dot)!" %}
```

## How to turn a number into a string, using a given number of decimal places

Use the `d2s()` method of the `ij.IJ` class:

```java
String message = "The current temperature is " + IJ.d2s(degrees, 1) + "° Celsius";
```

## How to abort a plugin completely

Sometimes, you want to abort a plugin without catching an exception at the highest level(s), without having ImageJ show an exception window. You can do that:

```java
throw new RuntimeException(Macro.MACRO_CANCELED);
```

The special message *Macro.MACRO\_CANCELED* will tell ImageJ not to show the exception message and stack trace in a text window.

## Interact with the ROI manager

To add ROIs to the ROI manager, do something like this:

```java
RoiManager manager = RoiManager.getInstance();
if (manager == null)
    manager = new RoiManager();
manager.addRoi(roi);
```

If you want to add the ROI with a slice label, you have to jump through a hoop:

```java
int currentSlice = image.getCurrentSlice();
RoiManager manager = RoiManager.getInstance();
if (manager == null)
    manager = new RoiManager();
// the first slice is 1 (not 0)
image.setSliceWithoutUpdate(slice);
manager.add(image, rois[i], slice);
image.setSlice(currentSlice);
```

To retrieve all ROIs from the ROI manager, do this:

```java
RoiManager manager = RoiManager.getInstance();
if (manager != null) {
    Hashtable<String, Roi> table =
        (Hashtable<String, Roi>)manager.getROIs();
    for (String label : table.keySet()) {
        int slice = manager.getSliceNumber(label);
        Roi roi = table.get(label);
        ... <do something with the ROI and the slice> ...
    }
}
```

If you need to preserve the order of the ROIs in the ROI manager, unfortunately you'll have to access the AWT listbox:

```java
import java.awt.List;
...
RoiManager manager = RoiManager.getInstance();
if (manager != null) {
    List labels = manager.getList();
    Hashtable<String, Roi> table = (Hashtable<String, Roi>)manager.getROIs();
    for (int i = 0; i < labels.getItemCount(); i++) {
        String label = labels.getItem(i);
        int slice = manager.getSliceNumber(label);
        Roi roi = table.get(label);
        ... <do something with the ROI and the slice> ...
    }
}
```

To get just the selected ROIs, use code similar to this:

```java
import java.awt.List;
...
RoiManager manager = RoiManager.getInstance();
if (manager != null) {
    String[] labels = manager.getList().getSelectedItems();
    Hashtable<String, Roi> table = (Hashtable<String, Roi>)manager.getROIs();
    for (String label : labels) {
        int slice = manager.getSliceNumber(label);
        Roi roi = table.get(label);
        ... <do something with the ROI and the slice> ...
    }
}
```

## Show a results table

First you need to get the results table instance (or create one):

```java
ResultsTable rt = Analyzer.getResultsTable();
if (rt == null) {
        rt = new ResultsTable();
        Analyzer.setResultsTable(rt);
}
```

Then you can add a new row:

```java
rt.incrementCounter();
```

... and add entries by column label:

```java
rt.addValue("slice", slice);
rt.addValue("bratwurst", -1);
```

**Finally** make sure that the result table is displayed/updated:

```java
rt.show("Results");
```

## How to find equivalent API commands between ImageJ 1.x and ImageJ2?

[ImageJ1-ImageJ2 cheat sheet](/develop/ij1-ij2-cheat-sheet) is available.

# Tips for Graphical User Interface (GUI) programming

## Programming with Swing components

When programming with Swing, beware that Swing is not thread safe. Swing's golden rule states that:


*Once a Swing component has been realized, all code that might affect or depend on the state of that component should be executed in the event-dispatching thread.*

When has a Swing component been realized? When it is visible inside Window or *JFrame* that got a call to `setVisible(true)`. This implies that its `paint(Graphics)` method has been called or will be called soon.

These are the methods that can realize a component, or rather, methods called on a *Window* or *Frame* or *JFrame* that will realize all its children components:

```java
setVisible(true)
show()
pack() // this might surprise you
```

There is a class which helps you with all this: [SwingUtilities](http://download.oracle.com/javase/6/docs/api/javax/swing/SwingUtilities.html). Example: to call `pack()` from within the constructor (which might or might not be called from the Event Dispatch Thread):

```java
if (SwingUtilities.isEventDispatchThread())
    pack();
else try {
    SwingUtilities.invokeAndWait(new Runnable() { public void run() {
        pack();
    }});
} catch (Exception e) { /* ignore */ }
```

Information extracted from the [Swing guide](http://web.archive.org/web/20120801194837/http://java.sun.com/products/jfc/tsc/articles/threads/threads1.html) (now only available from via web.archive.org as Oracle removed the original docs), additional information can be found in the [Concurrency in Swing](http://docs.oracle.com/javase/tutorial/uiswing/concurrency/index.html) lesson of *The Java Tutorials*.

# Arcane Quirks

## SoftReference and OutOfMemoryError

We have recently learned an interesting fact about Java's [SoftReference](http://docs.oracle.com/javase/6/docs/api/java/lang/ref/SoftReference.html) and the potential occurence of an [OutOfMemoryError](http://docs.oracle.com/javase/6/docs/api/java/lang/OutOfMemoryError.html). The result first: An [OutOfMemoryError](http://docs.oracle.com/javase/6/docs/api/java/lang/OutOfMemoryError.html) may be thrown in a situation where [SoftReferences](http://docs.oracle.com/javase/6/docs/api/java/lang/ref/SoftReference.html) can be released after which enough memory would be available. The reason is that normal garbage collection happens in an independent thread and does not halt other threads when they allocate memory. Only an explicit [System.gc()](http://docs.oracle.com/javase/6/docs/api/java/lang/System.html#gc%28%29) waits until the memory is freed . The consequence is that whenever you allocate memory then you should do that with the following clause:

```java
final MyObject o;
try {
  o = new MyObject();
}
catch (OutOfMemoryError e) {
  System.gc();
  o = new MyObject();
}
```

We found this by implementing a simple cache using a [HashMap](http://docs.oracle.com/javase/6/docs/api/java/util/HashMap.html) of [SoftReferences](http://docs.oracle.com/javase/6/docs/api/java/lang/ref/SoftReference.html) to an object that on finalize removes the corresponding key in the [HashMap](http://docs.oracle.com/javase/6/docs/api/java/util/HashMap.html). That cache is used to store image tiles for an [ImgLib2](/libs/imglib2) backend that uses a [CATMAID](http://fly.mpi-cbg.de/~saalfeld/catmaid/) stack ({% include github repo='imglib' tag='9f38afca3f0a4aa7b3ddc77160430a710a20501a' path='imglib2/tests/src/test/java/catmaid/CATMAIDRandomAccessibleInterval.java' label='GitHub' %}). It turned out that the painter thread in an interactive viewer was fetching new tiles quicker than the garbage collector would finalize [SoftReferences](http://docs.oracle.com/javase/6/docs/api/java/lang/ref/SoftReference.html) and stopped with an [OutOfMemoryError](http://docs.oracle.com/javase/6/docs/api/java/lang/OutOfMemoryError.html). We could solve that with the the above construct.
