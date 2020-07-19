{{Learn | scripting}}This page is meant to provide small code snippets as a starting point for writing scripts.

{{Notice
| message = '''See also:'''
* Language-specific scripting pages in the right-hand menu.
* [[Scripting comparisons]] to compare and contrast the languages.
* [[BAR|Broadly Applicable Routines]], a curated collection of snippets.
* Albert Cardona's comprehensive [http://www.ini.uzh.ch/~acardona/fiji-tutorial/ Fiji Jython tutorial] (please note that it is better idea to contribute tutorials to the ImageJ/Fiji wiki directly).
}}

'''Note:''' To copy the snippets, just double-click somewhere into the code. If Javascript is enabled, this will automatically select the complete snippet.

== Opening an image using ImageJ ==

==== Macro ====

<source lang="java">
path = "/path/to/file";
open(path);
</source>

==== Javascript ====

<source lang="javascript">
importClass(Packages.ij.IJ);

var path = "/path/to/file";
var imp = IJ.openImage(path);
imp.show();
</source>

==== Python ====

<source lang="python">
from ij import IJ

path = "/path/to/file"
imp = IJ.openImage(path)
imp.show()
</source>

==== Ruby ====

<source lang="ruby">
include_class 'ij.IJ'

path = "/path/to/file"
imp = ij.IJ.openImage(path)
imp.show
</source>

==== Clojure ====

<source lang="lisp">
(import 'ij.IJ)

(let [path "/path/to/file"
      imp (IJ/openImage path)]
  (.show imp))
</source>

==== Beanshell ====

<source lang="java">
import ij.IJ;

path = "/path/to/file";
imp = IJ.openImage(path);
imp.show();
</source>

== Opening an image using Bio-Formats ==

==== Macro ====

<source lang="java">
path = "/path/to/file";
run("Bio-Formats Importer", "open=" + path + " autoscale color_mode=Default view=Hyperstack stack_order=XYCZT");
</source>

==== Javascript ====

<source lang="javascript">
importClass(Packages.loci.plugins.BF);

var path = "/path/to/file";
var imps = BF.openImagePlus(path);

imps[0].show();
</source>

or, with more options:

<source lang="javascript">
importClass(Packages.loci.plugins.BF);
importClass(Packages['loci.plugins.in.ImporterOptions']); // 'in' is a reserved word, hence the different syntax
importClass(Packages.loci.common.Region);


var path = "/path/to/file";
var options = new ImporterOptions();
options.setId(path);
options.setAutoscale(true);
options.setCrop(true);
options.setCropRegion(0, new Region(x, y, w. h));
options.setColorMode(ImporterOptions.COLOR_MODE_COMPOSITE);
var imps = BF.openImagePlus(options);

imps[0].show();
</source>

==== Python ====
See also [https://gist.github.com/ctrueden/6282856 this python example script]


* Ruby

* Clojure

* Beanshell

== Opening, processing, and saving a sequence of files in a folder ==

==== Macro ====

<source lang="java">
input = getDirectory("Input directory");
output = getDirectory("Output directory");

Dialog.create("File type");
Dialog.addString("File suffix: ", ".tif", 5);
Dialog.show();
suffix = Dialog.getString();

processFolder(input);

function processFolder(input) {
	list = getFileList(input);
	for (i = 0; i < list.length; i++) {
		if(File.isDirectory(list[i]))
			processFolder("" + input + list[i]);
		if(endsWith(list[i], suffix))
			processFile(input, output, list[i]);
	}
}

function processFile(input, output, file) {
	// do the processing here by replacing
	// the following two lines by your own code
	print("Processing: " + input + file);
	open(input + file);
	print("Saving to: " + output);
	saveAs("TIFF", output+file);
	close();
}</source>

See also the tutorial ''[[How to apply a common operation to a complete directory]]''.

==== Python ====

<source lang="python">
import os
from ij import IJ, ImagePlus
from ij.gui import GenericDialog
 
def run():
  srcDir = IJ.getDirectory("Input_directory")
  if not srcDir:
    return
  dstDir = IJ.getDirectory("Output_directory")
  if not dstDir:
    return
  gd = GenericDialog("Process Folder")
  gd.addStringField("File_extension", ".tif")
  gd.addStringField("File_name_contains", "")
  gd.addCheckbox("Keep directory structure when saving", True)
  gd.showDialog()
  if gd.wasCanceled():
    return
  ext = gd.getNextString()
  containString = gd.getNextString()
  keepDirectories = gd.getNextBoolean()
  for root, directories, filenames in os.walk(srcDir):
    for filename in filenames:
      # Check for file extension
      if not filename.endswith(ext):
        continue
      # Check for file name pattern
      if containString not in filename:
        continue
      process(srcDir, dstDir, root, filename, keepDirectories)

def process(srcDir, dstDir, currentDir, fileName, keepDirectories):
  print "Processing:"
  
  # Opening the image
  print "Open image file", fileName
  imp = IJ.openImage(os.path.join(currentDir, fileName))
  
  # Put your processing commands here!
  
  # Saving the image
  saveDir = currentDir.replace(srcDir, dstDir) if keepDirectories else dstDir
  if not os.path.exists(saveDir):
    os.makedirs(saveDir)
  print "Saving to", saveDir
  IJ.saveAs(imp, "Tiff", os.path.join(saveDir, fileName));
  imp.close()

run()
</source>

* Javascript

* Ruby

* Clojure

* Beanshell

== Wait a given amount of time, or until user presses OK ==

==== Macro ====

<source lang="java">
wait(100);
</source>

or

<source lang="java">
waitForUser();
</source>

==== Javascript ====

<source lang="javascript">
Thread.sleep(100);
</source>

or

<source lang="javascript">
new WaitForUserDialog("Action required", "Please press OK when done.").show();
</source>

* Python

* Ruby

* Clojure

* Beanshell

== Select multiple ROIs from ROI manager and combine them ==

==== Macro ====
<source lang="java">
roiManager("select", newArray(0,2,4));
roiManager("AND");
</source>

==== Javascript ====
<source lang="javascript">
importClass(Packages.ij.plugin.frame.RoiManager);

rm = RoiManager.getInstance();
rm.setSelectedIndexes([0,2,4]);
rm.runCommand("AND");
</source>

==== Python ====
<source lang="python">
from ij.plugin.frame import RoiManager

rm = RoiManager.getInstance()
rm.setSelectedIndexes([0, 2, 4])
rm.runCommand("AND")
</source>

==== Beanshell ====
<source lang="java">
import ij.plugin.frame.RoiManager;

rm = RoiManager.getInstance();
rm.setSelectedIndexes(new int[] { 0, 2, 4});
rm.runCommand("AND");
</source>

* Ruby

* Clojure

== Unlocking an image ==

Sometimes things go wrong and all you see is "blabla.jpg is locked" when you try to process the image in some way. Then all you can do is to force-unlock the image, like so:

==== Beanshell ====
<source lang="java">
IJ.getImage().unlock();
</source>

== Scripting [[Feature Extraction|SIFT]] ==

The ''Scale-Invariant Feature Transform'' poses a relatively powerful way to reduce the complexity when trying to find matching parts of large images. Fiji has an implementation of this algorithm which you can use like so:

==== Beanshell ====
<source lang="java">
import java.util.ArrayList;

import mpicbg.ij.SIFT;
import mpicbg.imagefeatures.Feature;
import mpicbg.imagefeatures.FloatArray2DSIFT;

param = new FloatArray2DSIFT.Param();
sift = new SIFT(new FloatArray2DSIFT(param));
features = new ArrayList();
// ''ip'' refers to an ImageProcessor
sift.extractFeatures(ip, features);

// print coordinates
for (Feature feature : features)
    print("x: " + feature.location[0] + ", y: " + feature.location[1]);
</source>

For more information, please browse the [http://javadoc.imagej.net/MPI-CBG/index.html?mpicbg/imagefeatures/Feature.html Javadoc of the Feature class].

== Plotting charts with JFreeChart ==

[http://www.jfree.org/jfreechart/ JFreeChart] is a Java library for creating various charts. You can create charts as interactive JFrames, display them as an ImagePlus, or write them to SVG format.

==== Javascript ====
<source lang="javascript">
/* Javascript to test JFreeChart functionality */

importPackage(Packages.org.jfree.chart);
importPackage(Packages.org.jfree.chart.plot);
importPackage(Packages.org.jfree.chart.axis);
importPackage(Packages.org.jfree.chart.encoders);
importPackage(Packages.org.jfree.chart.renderer.category);

importPackage(Packages.java.awt);
importPackage(Packages.java.awt.geom);
importPackage(Packages.java.io);

importPackage(Packages.org.jfree.ui);
importPackage(Packages.org.jfree.data.category);
importPackage(Packages.org.jfree.data.statistics);

importPackage(Packages.org.apache.batik.dom);
importPackage(Packages.org.apache.batik.svggen);

var dataset = new DefaultStatisticalCategoryDataset();

// dataset.add(Mean, StdDev, "Series", "Condition")
dataset.add(15.0, 2.4, "Row 1", "Column 1");
dataset.add(15.0, 4.4, "Row 1", "Column 2");
dataset.add(13.0, 2.1, "Row 1", "Column 3");
dataset.add(7.0, 1.3, "Row 1", "Column 4");
dataset.add(2.0, 2.4, "Row 2", "Column 1");
dataset.add(18.0, 4.4, "Row 2", "Column 2");
dataset.add(28.0, 2.1, "Row 2", "Column 3");
dataset.add(17.0, 1.3, "Row 2", "Column 4");

var chart = ChartFactory.createLineChart(
	null,					// chart title
	"Treatment",				// domain axis label
	"Measurement",				// range axis label
	dataset,				// data
	PlotOrientation.VERTICAL,		// orientation
	false,					// include legend
	true,					// tooltips
	false					// urls
);

// set the background color for the chart...
chart.setBackgroundPaint(Color.white);

var plot = chart.getPlot();
plot.setBackgroundPaint(Color.white);
plot.setRangeGridlinesVisible(false);
plot.setAxisOffset(RectangleInsets.ZERO_INSETS);

// customise the range axis...
var rangeAxis = plot.getRangeAxis();
rangeAxis.setStandardTickUnits(NumberAxis.createIntegerTickUnits());
rangeAxis.setAutoRangeIncludesZero(true);
rangeAxis.setRange(0, 40);

// customise the renderer...
var renderer = new StatisticalBarRenderer();
renderer.setErrorIndicatorPaint(Color.black);
renderer.setSeriesOutlinePaint(0,Color.black);
renderer.setSeriesOutlinePaint(1,Color.black);
renderer.setSeriesPaint(0,Color.black);
renderer.setSeriesPaint(1,Color.white);
renderer.setItemMargin(0.0);
plot.setRenderer(0,renderer);

renderer.setDrawBarOutline(true);

bi = chart.createBufferedImage(600, 400);

imp = new ImagePlus("Chart Test", bi);
imp.show();

// Create SVG image
// Get a DOMImplementation and create an XML document
var domImpl = GenericDOMImplementation.getDOMImplementation();
var document = domImpl.createDocument(null, "svg", null);

// Create an instance of the SVG Generator
var svgGenerator = new SVGGraphics2D(document);

// draw the chart in the SVG generator
var bounds = new Rectangle(600, 400);
chart.draw(svgGenerator, bounds);

var dir = IJ.getDirectory("Where should the svg file be saved?");
// Write svg file
var svgFile = new File(dir + "test.svg");
var outputStream = new FileOutputStream(svgFile);
var out = new OutputStreamWriter(outputStream, "UTF-8");
svgGenerator.stream(out, true /* use css */);
outputStream.flush();
outputStream.close();
</source>

== Writing out movie files with JavaCV ==

[https://github.com/bytedeco/javacv JavaCV] is a Java wrapper around OpenCV and FFMPEG. You will have to unpack the libraries into <tt>ImageJ.app/lib/<platform>/</tt> (or <tt>Fiji.app/lib/<platform>/</tt>) to let JavaCV find the native libraries (e.g. unpack ffmpeg-macosx-x86_64.jar's <tt>.dylib</tt> files directly into <tt>ImageJ.app/lib/macosx/</tt>) '''before''' starting ImageJ/Fiji.

==== Beanshell ====

<source lang="java">
/*
 * A simple example how to write out a movie from a possibly virtual
 * image stack using JavaCV.
 * 
 * Licensed under CC-BY-SA 4.0 
 * by Johannes Schindelin on September 16th, 2014
 */

path = "/tmp/change-this-name.flv";
frameRate = 25.0;
videoBitrate = 400 * 1000;

// if you have not installed JavaCV into your jars/ directory:
import java.io.File;
binDir = new File(System.getProperty("user.home")
	+ "/Downloads/javacv-bin/");
if (binDir.isDirectory()) {
	jars = binDir.list();
	for (String jar : jars) {
		if (jar.endsWith(".jar")) {
			addClassPath(new File(binDir, jar).getPath());
		}
	}
}

// use JavaCV to write out the currently active 3D image
import ij.IJ;
import org.bytedeco.javacv.FFmpegFrameRecorder;
import org.bytedeco.javacpp.opencv_core.IplImage;

void saveImageAsMovie(image, path, frameRate, videoBitrate) {
	if (image == null) {
		IJ.error("No active image!");
		return;
	}

	width = image.getWidth();
	height = image.getHeight();
	stack = image.getStack();

	recorder = FFmpegFrameRecorder.createDefault(path,
		(int) width, (int) height);
	recorder.setFormat("flv");
	recorder.setFrameRate(frameRate);
	recorder.setVideoBitrate(videoBitrate);
	recorder.start();

	for (slice = 1; slice <= stack.getSize(); slice++) {
		ip = stack.getProcessor(slice);
		recorder.record(IplImage.createFrom(ip.getBufferedImage()));
	}

	recorder.stop();
	recorder.release();
}

try {
	saveImageAsMovie(IJ.getImage(), path, frameRate, videoBitrate);
} catch (Throwable t) {
	IJ.handleException(t);
}
</source>

[[Category:Scripting]]
