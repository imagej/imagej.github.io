---
title: ImgLib2 - Getting Started
section: Explore:Libraries:ImgLib2
---




## Creating and Displaying an Image

Before you dive into ImgLib2 for real, you should know how to create and display an image, so that you can visually enjoy the fruits of your labor.

The following piece of code creates and displays an 400x320 8bit gray-level image:

```java
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
```

When you run this example, you should get a window showing a black 400x320 image. In lines *10-11*, the image is created. In line *12* it is displayed. Now, that is one awfully long line just to create a black image. Let's break it down into smaller parts.

```java
final ImgFactory< UnsignedByteType > factory = new ArrayImgFactory< UnsignedByteType >();
final long[] dimensions = new long[] { 400, 320 };
final UnsignedByteType type = new UnsignedByteType();
final Img< UnsignedByteType > img = factory.create( dimensions, type );
```

Pixel images in ImgLib2 are created using an [`ImgFactory`](http://javadoc.scijava.org/ImgLib2/net/imglib2/img/ImgFactory.html). There are different ImgFactories, that create pixel containers with different memory layouts. Here, we create an [`ArrayImgFactory`](http://javadoc.scijava.org/ImgLib2/net/imglib2/img/array/ArrayImgFactory.html). This factory creates in containers that map to a single flat Java array:

```java
final ImgFactory< UnsignedByteType > factory
        = new ArrayImgFactory< UnsignedByteType >();
```

The type parameter of the factory that specifies the value type of the image we want to create. We want to create a 8-bit gray-level image, thus we use [`UnsignedByteType`](http://javadoc.scijava.org/ImgLib2/net/imglib2/type/numeric/integer/UnsignedByteType.html).

Next we create a `long[]` array that specifies the image size in every dimension. The length of the array specifies the number of dimensions. Here, we state that we want to create 400x320 2D image:

```java
final long[] dimensions = new long[] { 400, 320 };
```

Finally, we need to provide a type variable, that is a variable having the type that is to be stored in the image. This must match the generic type parameter of the `ImgFactory`. Thus we create an `UnsignedByteType`:

```java
final UnsignedByteType type = new UnsignedByteType();
```

Then we can create the image, using the factory, dimensions, and type variable:

```java
final Img< UnsignedByteType > img = factory.create( dimensions, type );
```

We store the result of the `create()` method in an [`Img`](http://javadoc.scijava.org/ImgLib2/net/imglib2/img/Img.html) variable. `Img` is a convenience interface that gathers properties of pixel image containers such as having a number of dimensions, being able to iterate it's pixels, etc.

This image is then displayed using:

```java
ImageJFunctions.show( img );
```

[`ImageJFunctions`](http://javadoc.scijava.org/ImgLib2/net/imglib2/img/display/imagej/ImageJFunctions.html) provides convenience methods to wrap ImgLib2 constructs into ImageJ containers and display them. It works with 2D and 3D images and can handle most of the pixel types supported by ImgLib2. ImgLib2 provides more sophisticated ways of getting image data to your screen, but we will not go into that now. As a rule of thumb, if you have something remotely resembling a pixel grid, usually you can `ImageJFunctions.show()` it.

## Opening And Displaying Image Files

You can open image files with [`ImgOpener`](http://javadoc.scijava.org/SCIFIO/io/scif/img/ImgOpener.html) which is using [LOCI Bio-Formats](http://loci.wisc.edu/software/bio-formats). The following opens and displays an image file:

```java
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
```

The image is loaded in lines *14-15*. Lets look the steps in more detail. We create an [`ImgOpener`](http://javadoc.scijava.org/SCIFIO/io/scif/img/ImgOpener.html):

```java
final ImgOpener opener = new ImgOpener();
```

When opening an image, we can specify which memory layout to use and as which value type we want to load the image. We want to use the `ArrayImg` layout again, and we want to have `UnsignedByteType` values again.

Similar to the [ above example](/libs/imglib2/getting-started#creating-and-displaying-an-image) we need an `ImgFactory` and an instance of the value type:

```java
final ImgFactory< UnsignedByteType > factory = new ArrayImgFactory< UnsignedByteType >();
final UnsignedByteType type = new UnsignedByteType();
```

Then we can use the `openImg()` method, giving a filename, `ImgFactory`, and type instance:

```java
final Img< UnsignedByteType > img = opener.openImg( "graffiti.tif", factory, type );
```

If there is a problem reading the image, `openImg()` throws an [`ImgIOException`](http://javadoc.scijava.org/SCIFIO/io/scif/img/ImgIOException.html). If all goes well, we store the result in an [`Img`](http://javadoc.scijava.org/ImgLib2/net/imglib2/img/Img.html) variable for convenience. (Actually the result is an [`ImgPlus`](http://javadoc.imagej.net/ImageJ1/ij/ImagePlus.html) wrapping an `ArrayImg`.)

## Notes

-   Note that `Img` is just convenience interface. When you get more proficient with ImgLib2 you will find yourself using it less and less. You will either be more concrete or more general than that. In the above example, we could be more concrete -- the result of the `ArrayImgFactory< UnsignedByteType >.create()` is actually an `ArrayImg< UnsignedByteType, ByteArray >`. In algorithm implementations, you want to be as generic as possible to not constrain yourself to specific image types. You will specify only the super-interfaces of `Img` that you really need. For instance, if you need something which has boundaries and can be iterated you would use `IterableInterval`.
-   There are more [ImgLib2 Examples](/libs/imglib2/examples) on [ Opening, creating and displaying images](/libs/imglib2/examples#example-1---opening-creating-and-displaying-images).
