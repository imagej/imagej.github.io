{{ImgLibMenu}}__TOC__
== Creating and Displaying an Image ==
Before you dive into ImgLib2 for
real, you should know how to create and display an image, so that you can
visually enjoy the fruits of your labor.

The following piece of code creates and displays an 400x320 8bit gray-level image:
<source lang="java">
import net.imglib2.img.Img;
import net.imglib2.img.array.ArrayImgFactory;
import net.imglib2.img.display.imagej.ImageJFunctions;
import net.imglib2.type.numeric.integer.UnsignedByteType;

public class CreateAndDisplay
{
	public static void main( final String[] args )
	{
		final Img< UnsignedByteType > img = new ArrayImgFactory< UnsignedByteType >()
			.create( new long[] { 400, 320 }, new UnsignedByteType() );
		ImageJFunctions.show( img );
	}
}
</source>

When you run this example, you should get a window showing a black 400x320 image.
In lines ''10-11'', the image is created. In line ''12'' it is displayed.
Now, that is one awfully long line just to create a black image.  Let's break it down into smaller parts.
<source lang="java">
final ImgFactory< UnsignedByteType > factory = new ArrayImgFactory< UnsignedByteType >();
final long[] dimensions = new long[] { 400, 320 };
final UnsignedByteType type = new UnsignedByteType();
final Img< UnsignedByteType > img = factory.create( dimensions, type );
</source>

Pixel images in ImgLib2 are created using an [http://javadoc.scijava.org/ImgLib2/net/imglib2/img/ImgFactory.html <code>ImgFactory</code>].
There are different ImgFactories, that create pixel containers with different memory layouts.
Here, we create an [http://javadoc.scijava.org/ImgLib2/net/imglib2/img/array/ArrayImgFactory.html <code>ArrayImgFactory</code>].
This factory creates in containers that map to a single flat Java array:
<source lang="java">
final ImgFactory< UnsignedByteType > factory
		= new ArrayImgFactory< UnsignedByteType >();
</source>
The type parameter of the factory that specifies the value type of the image we want to create.
We want to create a 8-bit gray-level image, thus we use [http://javadoc.scijava.org/ImgLib2/net/imglib2/type/numeric/integer/UnsignedByteType.html <code>UnsignedByteType</code>].

Next we create a <code>long[]</code> array that specifies the image size in every dimension.
The length of the array specifies the number of dimensions.
Here, we state that we want to create 400x320 2D image:
<source lang="java">
final long[] dimensions = new long[] { 400, 320 };
</source>

Finally, we need to provide a type variable, that is a variable having the type that is to be stored in the image.
This must match the generic type parameter of the <code>ImgFactory</code>.
Thus we create an <code>UnsignedByteType</code>:
<source lang="java">
final UnsignedByteType type = new UnsignedByteType();
</source>

Then we can create the image, using the factory, dimensions, and type variable:
<source lang="java">
final Img< UnsignedByteType > img = factory.create( dimensions, type );
</source>
We store the result of the <code>create()</code> method in an [http://javadoc.scijava.org/ImgLib2/net/imglib2/img/Img.html <code>Img</code>] variable.
<code>Img</code> is a convenience interface that gathers properties of pixel image containers
such as having a number of dimensions, being able to iterate it's pixels, etc.

This image is then displayed using:
<source lang="java">
ImageJFunctions.show( img );
</source>
[http://javadoc.scijava.org/ImgLib2/net/imglib2/img/display/imagej/ImageJFunctions.html <code>ImageJFunctions</code>] provides convenience methods
to wrap ImgLib2 constructs into ImageJ containers and display them.
It works with 2D and 3D images and can handle most of the pixel types supported by ImgLib2.
ImgLib2 provides more sophisticated ways of getting image data to your screen, but we will not go into that now.
As a rule of thumb, if you have something remotely resembling a pixel grid, usually you can <code>ImageJFunctions.show()</code> it.

== Opening And Displaying Image Files ==
You can open image files with [http://javadoc.scijava.org/SCIFIO/io/scif/img/ImgOpener.html <code>ImgOpener</code>] which is using [http://loci.wisc.edu/software/bio-formats LOCI Bio-Formats].
The following opens and displays an image file:
<source lang="java">
import net.imglib2.img.Img;
import net.imglib2.img.array.ArrayImgFactory;
import net.imglib2.img.display.imagej.ImageJFunctions;
import io.scif.img.ImgIOException;
import io.scif.img.ImgOpener;
import net.imglib2.type.numeric.integer.UnsignedByteType;

public class OpenAndDisplay
{
	public static void main( final String[] args )
	{
		try
		{
			final Img< UnsignedByteType > img = new ImgOpener().openImg( "graffiti.tif",
				new ArrayImgFactory< UnsignedByteType >(), new UnsignedByteType() );
			ImageJFunctions.show( img );
		}
		catch ( final ImgIOException e )
		{
			e.printStackTrace();
		}
	}
}
</source>
The image is loaded in lines ''14-15''. Lets look the steps in more detail.
We create an [http://javadoc.scijava.org/SCIFIO/io/scif/img/ImgOpener.html <code>ImgOpener</code>]:
<source lang="java">
final ImgOpener opener = new ImgOpener();
</source>
When opening an image, we can specify which memory layout to use and as which value type we want to load the image.
We want to use the <code>ArrayImg</code> layout again, and we want to have <code>UnsignedByteType</code> values again.

Similar to the [[ImgLib2 - Getting Started#Creating and Displaying an Image | above example]] we need an <code>ImgFactory</code> and an instance of the value type:
<source lang="java">
final ImgFactory< UnsignedByteType > factory = new ArrayImgFactory< UnsignedByteType >();
final UnsignedByteType type = new UnsignedByteType();
</source>

Then we can use the <code>openImg()</code> method, giving a filename, <code>ImgFactory</code>, and type instance:
<source lang="java">
final Img< UnsignedByteType > img = opener.openImg( "graffiti.tif", factory, type );
</source>
If there is a problem reading the image, <code>openImg()</code> throws an [http://javadoc.scijava.org/SCIFIO/io/scif/img/ImgIOException.html <code>ImgIOException</code>].
If all goes well, we store the result in an [http://javadoc.scijava.org/ImgLib2/net/imglib2/img/Img.html <code>Img</code>] variable for convenience.
(Actually the result is an [http://javadoc.imagej.net/ImageJ1/ij/ImagePlus.html <code>ImgPlus</code>] wrapping an <code>ArrayImg</code>.)

== Notes ==
* Note that <code>Img</code> is just convenience interface.  When you get more proficient with ImgLib2 you will find yourself using it less and less.  You will either be more concrete or more general than that.  In the above example, we could be more concrete -- the result of the <code>ArrayImgFactory< UnsignedByteType >.create()</code> is actually an <code>ArrayImg< UnsignedByteType, ByteArray ></code>.  In algorithm implementations, you want to be as generic as possible to not constrain yourself to specific image types.  You will specify only the super-interfaces of <code>Img</code> that you really need. For instance, if you need something which has boundaries and can be iterated you would use <code>IterableInterval</code>.
* There are more [[ImgLib2 Examples]] on [[ImgLib2 Examples#Example 1 - Opening, creating and displaying images | Opening, creating and displaying images]].
