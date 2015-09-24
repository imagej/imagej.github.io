{{ImgLib1_Deprecation_Notice}}


The [[Imglib]] library makes extensive use of [[wikipedia:Generics in Java|Java generics]]. Generics appeared in Java from version 1.5, and they introduce new semantic items that can be puzzling if you never used them before. The programming techniques associated are quite new to the ImageJ world, and using Imglib inside your plugins will change their typical layout.

This short page does not aim at being an introduction on generics, but rather is a quick and dirty introduction on how to tune your java files to use Imglib. The deep meaning of semantics is skipped, and we will try to provide a quick template to start with. However, we will attempt to be quite pedestrian when ImageJ itself is involved, and try to display the code and the commands needed to generate a plugin from scratch.  

== Importing <code>imglib</code> ==

We will work on a dummy plugin that takes an image and sum the pixel value over all pixels. As an exercise, we choose to use imglib classes internally. It will turn out to be quite convenient, even for a dummy plugin. 

A plugin skeleton looks like this:
<source lang="java">
import ij.IJ;

import ij.plugin.PlugIn;

public class Pixel_Summation implements PlugIn {
  
  public void run(String arg) {
    IJ.write("Ciao, bella.");
  }
} 
</source>
If you work from within the [[Script Editor]], you can save it anywhere and Compile & Run it with ''Run>Compile & Run''.

Otherwise you have to save this in a file named <tt>Pixel_Summation.java</tt> in the Fiji plugins folder. You can either {{bc | Help | Update Menus}} and find the new plugin in the ''Plugins'' menu, or compile it from the command line with:

<source lang="bash">
./fiji --javac plugins/Pixel_Summation.java
</source>
(assuming that you are in the Fiji source tree).

Now we want to import the imglib library, and use its <tt>Image</tt> class as an internal field. We write:

<source lang="java">
import ij.IJ;

import ij.plugin.PlugIn;

import mpicbg.imglib.image.Image;

public class Pixel_Summation implements PlugIn {
  
  protected Image img;

  public void run(String arg) {
    IJ.write("Ciao, bella.");
  }
} 
</source>
Fiji will already know where to pick up ''imglib.jar''.

Now, there is already quite a few things we can stumble on:
* If you put this code in Eclipse IDE, for instance, it will generate a warning about unused fields, and a warning about <tt>Image</tt> being a raw type. We will come back to that later.
* If you try to compile this code using <tt>javac</tt> from the command line, it will fail unless you use a java 1.6 compiler, for the <tt>imglib.jar</tt> is compiled with this java version.

But anyway, let us move on.

== Converting from <tt>ImagePlus</tt> to Imglib ==

As we use this plugin from within Fiji, we will receive images in form of an <tt>ImagePlus</tt>. Since we want to use Imglib internally, we need to convert it. This is done using the class <tt><b>ImagePlusAdapter</b></tt> that has various static utilities to do so.

This is how a minimally converted class would look like:
<source lang="java">
import ij.IJ;
import ij.ImagePlus;
import ij.WindowManager;

import ij.plugin.PlugIn;

import mpicbg.imglib.image.Image;
import mpicbg.imglib.image.ImagePlusAdapter;

import mpicbg.imglib.type.numeric.RealType;

public class Pixel_Summation<T extends RealType<T>> implements PlugIn {
  
  protected Image<T> img;

  public void run(String arg) {
	  ImagePlus imp = WindowManager.getCurrentImage();
	  img = ImagePlusAdapter.wrap(imp);
  }
}
</source>

Note that we use generics that provide compile-time type-safety, we cannot leave the field <tt>img</tt> be an image of unknown type. We must explicitly state that it is going to be an image containing a certain generic type: 

<source lang="java">
protected Image<T> img;
</source>

We must also detail what <tt>T</tt> can be. This is done by modifying the class signature. We add a type variable to it, that specifies what the plugin operates on:
<source lang="java">
public class Pixel_Summation<T extends RealType<T>> implements PlugIn {
</source>
This is like saying: "this plugin operates on <tt>T</tt>", whatever <tt>T</tt> is.
In our specific case, <tt>T</tt> can't be anything. If you inspect the source of <tt>Image</tt>, you will see that we need to use a subclass of <tt>mpicbg.imglib.type.Type</tt> (we can't have images made of koalas, yet). 

Here, we want to access the ''real'' pixel value (note that ''complex'' values are more general, so if you implement an algorithm on ''complex'' types, it will work on ''real'' ones, too, but not vice versa), so we will use <tt>RealType</tt>. It defines an interesting method <tt>getReal()</tt> that will allow us to retrieve a <tt>float</tt> representation of the pixel value.

== Making something out of it ==

Now that we vanquished the semantics, we would like to wrap up this tutorial by doing something with the plugin. In Imglib, we iterate over the data within an image using <b>Cursors</b>. They are the subject of [[Imglib:_iterating_through_pixel_data|another tutorial]], we will not present them thoroughly. But briefly:

* A plain cursor can be generated by the <tt>createCursor()</tt> method of an <tt>Image<T></tt> instance. It will have the same type variable as that of the <tt>Image</tt> object it originates from.

* It is made to iterate through the underlying data, and in the above particular case, it will do it in a memory-optimized fashion. You want to use the <tt>hasNext()</tt> and <tt>fwd()</tt> methods of the cursor.

* The actual data can be retrieved using the <tt>getType()</tt> method, that will return - oh surprise - an object of class <tt>T</tt>.

* Since in our case <tt>T</tt> extends <tt>RealType</tt>, we can use the <tt>getRealFloat()</tt> or <tt>getRealDouble()</tt> method to convert to a basic java <tt>float</tt> or <tt>double</tt>, respectively.

Which leads to:

<source lang="java">
import ij.IJ;
import ij.ImagePlus;
import ij.WindowManager;

import ij.plugin.PlugIn;

import mpicbg.imglib.cursor.Cursor;

import mpicbg.imglib.image.Image;
import mpicbg.imglib.image.ImagePlusAdapter;

import mpicbg.imglib.type.numeric.RealType;

public class Pixel_Summation<T extends RealType<T>> implements PlugIn {
  
  protected Image<T> img;

  public void run(String arg) {
	  ImagePlus imp = WindowManager.getCurrentImage();
	  img = ImagePlusAdapter.wrap(imp);  
	  Cursor<T> cursor = img.createCursor();
	  float sum = 0f;
	  float val;
	  T type; // This is the generic type of the image. 
          // Note we actually don't have squat idea about what it is actually at the present time,
          // but our plugin will still work whatever it will be.
	  while (cursor.hasNext()) {
		  cursor.fwd();
		  type = cursor.getType();
		  val = type.getRealFloat();
		  sum = sum + val;
	  }
	  IJ.write("Sum on all pixels: "+sum);
  }
} 
</source>

And this is it!

You can test this plugin on all possible image types ImageJ supports, and it will still yield a result. <b>And you did not have to write code for each particular data type.</b>

[[Category:ImgLib]]
[[Category:Tutorials]]
[[Category:Development]]
