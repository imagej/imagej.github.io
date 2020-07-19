(Return to the [[3D_Viewer:_Developer_Documentation|Developer Documentation]] page)<br>
(Return to the main [[3D_Viewer]] page)



== How to visualize 4D data ==

You can download example source code for this HowTo [[3D_Viewer:_Example_code|here]].



Sometimes, 3D data are recorded over time, and it is desirable to visualize those data, i.e. show it in a time line, being able to animate it, etc. This is possible with the viewer. The following lines of code show how to do it programmatically:
<source lang="java" first-line="22">
// Open a hyperstack
ImagePlus imp = IJ.openImage(
      Prefs.getImagesURL() + "Spindly-GFP.zip");

// Create a universe and show it
Image3DUniverse univ = new Image3DUniverse();
univ.show();

// load the stack in the viewer
univ.addVoltex(imp);

// get the Timeline object
Timeline tl = univ.getTimeline();

// start playback
tl.play();

// wait a bit
try {
        Thread.sleep(5000);
} catch(InterruptedException e) {}


// Stop animation
tl.pause();
</source>

The 3D viewer automatically recognizes hyperstacks and shows a control panel on demand, providing buttons for playback, pause, etc.

<code>Image3DUniverse</code> allows to retrieve a <code>Timeline</code> object, which allows to call the corresponding functions programmatically.


=== Important methods of Viewer4D ===

Next to <code>play()</code> and <code>pause()</code>, the <code>Timeline</code> class provides several methods for stepping through the time frames of the 4D data:
<pre class="brush: java; first-line: 22; font-size: '100%';">
/** Set bounce-back or repeat */
public void setBounceBack(boolean bounce);
public boolean getBounceBack();

/** Speed up the animation. */
public void faster();

/** Slows the animation down. */
public void slower();

/** Record the whole timeline */
public ImagePlus record();

/** Start animation.  */
public synchronized void play();

/** Stop/pause animation */
public synchronized void pause();

/** Display next timepoint. */
public void next();

/** Display previous timepoint. */
public void previous();

/** Display first timepoint. */
public void first();

/** Display last timepoint. */
public void last();
</pre>
