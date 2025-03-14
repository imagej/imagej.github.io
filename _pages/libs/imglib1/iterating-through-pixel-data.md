---
mediawiki: ImgLib1:_iterating_through_pixel_data
title: "ImgLib1: Iterating through pixel data"
nav-links: true
nav-title: Iterating Pixels
---

{% include warning/deprecated old="[ImgLib1](/libs/imglib1)" new="[ImgLib2](/libs/imglib2)" %}

The architecture of [Imglib](/libs/imglib1) aims at completely separating the image - which can be seen as a data container - from the concrete basic data type it encapsulates. In practice, this means that you can write "blind" algorithms, which can safely ignore whether they operate on a `uint8` image, a RGB image or a `uint16` stack of 15 slices.

This in turn imposes a certain gymnastic when accessing the underlying data is involved. Here, we will make a brief introduction on how to do this with Imglib. We assume you want to use Imglib in a Java plugin, and that you are already familiar with Java itself.

## The `Image` objects

Let us suppose we want to access the data in an arbitrary image `img`. The *a priori* data type is unknown, which translates in declaring the variable `img` using generics:

```java
Image<T> img;
```

where `T` is a type variable, representing the 'generic type of your image.

The <u>`mpicbg.imglib.image.Image`</u> is the mother object for your actual image; it contains all the information needed to display it and operate on it.

Imglib is built such that it is possible to have different ways to store the same underlying data in an `Image`, or storage strategies. This is done through the <u>`mpicbg.imglib.container.Container`</u> implementations, which is not the subject of this tutorial. Every `Image` object has a field that implements the `Container` interface, and deals with data storage.

The responsibility of retrieving, iterating over and modifying the data is implemented in a separate object hierarchy, all inheriting from the <u>`mpicbg.imglib.cursor.Cursor`</u> interface. As for data storage, multiple strategies are implemented for iterating. The goal of this page is to play with some of them and demonstrate their capabilities.

## The `Cursor` model

### Creating a plain cursor

You can create a plain cursor that will iterate over the pixels of an image very simply, by calling the `createCursor()` method over an `Image` object:

```java
final Image<T> img;
final Cursor<T> cursor = img.createCursor();

// we set all pixels to a certain value
final T value;

// Cursor implements java.lang.Iterable<T>
for ( final T pixel : cursor )
    pixel.set( value ); 

cursor.close();
```
Note that the cursor object has a type variable <T> identical to `img`'s type.

### Iterating using a plain cursor

What can we do with it? Briefly, it behaves like a specialized iterator. To move over the data we will use:

-   `public void fwd()` to move to the next position;
-   `public boolean hasNext()` to report if we finished iterating over all the data;
-   `public void reset()` to put back the cursor before the first data element;
-   `public void close()` to mark this cursor has not being use anymore.

Other methods are available, but these four ones are enough to build a basic loop iterating over all the data. Here is an example that does so, using the bat cochlea example within ImageJ.

```java
import ij.plugin.PlugIn;
import ij.IJ;
import ij.ImagePlus;
import mpicbg.imglib.cursor.Cursor;
import mpicbg.imglib.image.Image;
import mpicbg.imglib.image.ImagePlusAdapter;
import mpicbg.imglib.type.numeric.RealType;
 
public class Example_Cursors<T extends RealType<T>> implements PlugIn {
 
    public void run(String arg) {

        // Open the bat-cochlea example
                String name = "https://imagej.net/ij/images/bat-cochlea-volume.zip";
        ImagePlus imp = IJ.openImage(name);
        imp.show();

        // Convert it to Imglib image
        Image<T> img = ImagePlusAdapter.wrap(imp);  
        
        // Create a plain cursor for it
        Cursor<T> cursor = img.createCursor();

        // Iterate over all the image
        int pixel_count = 0;
        while (cursor.hasNext()) {
            cursor.fwd();
            pixel_count++;
        }
        cursor.close();

        IJ.write("Iterated over "+pixel_count+" pixels.");
    }
}
```

Note that this plugin does not do anything useful at all. However, it shows that such a cursor will iterate over <b>all</b> the data, not caring if there are multiple slices or frames. It reports having moved across 2 124 276 pixels, which is indeed the result of the product of all the dimension of the images: 121 × 154 × 114.

Now, we could do something useful with the data itself, using the `public `<T>` getType()` method that returns a `mpicbg.imglib.type.Type` object, responsible for making operations on the data itself. That is the subject of another tutorial, we limit ourselves here to iterate over the data.

### The plain cursor perks

In the preceding example, we know that every pixel has been traversed by the cursor. However, we do not know in which order. <b>In the general case, where no assumption is made on the storage strategy, it is not possible to predict what will be the traversal order. Imglib just ensures that the traversal is made in an optimized fashion.</b>

So with a plain cursor iterating, you don't know how it is made, but you are sure that it is the best way.

## The localizable cursor

Another limitation of the plain cursor exemplified above, is that it does not report where it is at a given iteration step. If you need this information, you must create another cursor type from the image, called a `LocalizableCursor`. This is made through the call:

```java
LocalizableCursor<T> loc_cursor = img.createLocalizableCursor();
```

It adds the following method to the plain cursor:

-   `public int[] getPosition()` returns an array specifying the current position for each dimension; <span style="color:#FF0000;">Warning: this methods creates a new int\[\] array every time and is therefor inefficient if called very often</span>
-   `public int getPosition( int dim )` returns the index of the position for the specified dimension number;
-   `public void getPosition( int[] position )` store the position in the given array.

It does not allow to specify the position, it just reports its current position, whatever way it changes from one iteration to another. Just to demonstrate its usage, let us write a plugin that crawls through an image, and report the position of the brightest pixel (whatever this means).

```java
import ij.plugin.PlugIn;
import ij.IJ;
import ij.ImagePlus;
import mpicbg.imglib.cursor.LocalizableCursor;
import mpicbg.imglib.image.Image;
import mpicbg.imglib.image.ImagePlusAdapter;
import mpicbg.imglib.type.numeric.RealType;
import mpicbg.imglib.algorithm.math.MathLib;

public class Localizable_Cursors<T extends RealType<T>> implements PlugIn {
 
    public void run(String arg) {
 
        // Open the M51 galaxy example
                String name = "https://imagej.net/ij/images/m51.tif";
        ImagePlus imp = IJ.openImage(name);
        imp.show();
 
        // Convert it to Imglib image
        final Image<T> img = ImagePlusAdapter.wrap( imp );  
 
        // Create a localizable cursor for it
        final LocalizableCursor<T> loc_cursor = img.createLocalizableCursor();
 
        // Create a Type variable to store the max value.
        // We create it from the Image object so that they have compatible types
                // As we cannot initialize it with the minimum value we have to init it with
                // the first value later
        T max = null; // consequently, it has the type <T>
 
                // create an int[] array with correct dimensionality
        final int[] max_position = img.createPositionArray();
 
        // Iterate over all the image
        while ( loc_cursor.hasNext() ) 
                {
            loc_cursor.fwd();
            T current_value = loc_cursor.getType();
                        if ( max == null )
                                 max = current_value.clone();
 
                        // RealType implements java.lang.Comparable
            if ( current_value.compareTo( max ) > 0 ) 
                        {
                                // save the max position, giving a pre-instantiated array is the fastest way 
                loc_cursor.getPosition( max_position );
                                // we cannot simply copy references, this would cause a mess
                max.set( current_value ); 
            }
        }
        loc_cursor.close();
 
        // Make a nice string for position
        String pos_str = MathLib.printCoordinates( max_position );
                // every Type has a .toString() method (as has every Cursor)
        IJ.write( "Maximal pixel value of " + max + " found at position " + pos_str );
    }
}
```

Even for a dummy plugin, this is far from perfect. Indeed, it reports the position of the *first* maximum, in case there is multiple pixels that have the same maximal value. Since in the general case we do not know in which order the data is traversed, this might be of importance.

## Imposing the iteration order

Now of course, you would want to determine the way in which the data is traversed. There, a third kind of cursor comes at help, which extends the preceding ones. It is the `LocalizableByDimCursor` cursor. Is is created as before:

```java
LocalizableByDimCursor<T> locdim_cursor = img.createLocalizableByDimCursor();
```

It is flexible and complete, and have even options to specify how to create neighborhood and deal with neighborhood close to the image borders. We will just limit ourselves to its basic features, which are:

-   The ability to set the absolute current position:
    -   `public void setPosition( int position[] )`
    -   `public void setPosition( int position, int dim )`
    -   `public void setPosition( LocalizableCursor<?> cursor )`

<!-- -->

-   The ability to move relatively from the current position:
    -   `public void fwd( int dim )`
    -   `public void bck( int dim )`
    -   `public void move( int steps, int dim )`
    -   `public void moveRel( int position[] )`

We can use them to create a very basic Z maximal projection plugin, that will create a 2D image from a 3D stack by taking the maximal pixel value along the Z dimension for all X,Y. The following version is devoid of subtleties.
```java
import ij.plugin.PlugIn;
import ij.IJ;
import ij.ImagePlus;
import ij.WindowManager;
import mpicbg.imglib.cursor.LocalizableByDimCursor;
import mpicbg.imglib.cursor.LocalizableCursor;
import mpicbg.imglib.image.Image;
import mpicbg.imglib.image.ImagePlusAdapter;
import mpicbg.imglib.image.display.imagej.ImageJFunctions;
import mpicbg.imglib.type.numeric.RealType;
 
public class LocalizableByDim_Cursors<T extends RealType<T>> implements PlugIn {
 
	public void run(String arg) {
 
		// Open the Confocal series example
				final String name = "https://imagej.net/ij/images/mri-stack.zip";
		final ImagePlus imp = IJ.openImage(name);
		imp.show();
 
		// Convert it to Imglib image. It must be a 3D image.
		final Image<T> img = ImagePlusAdapter.wrap(imp);  
		final int z_size = img.getDimension( 2 ); // Z is the 3rd dimension, with index 2
 
		// Create a Type variable to store the max value, and another 
		// to deal with current pixel.
		T max;
		T current_value;
 
		// Create a new 2D image of the same type
		// 2D images have still 3 dimensions, but the 3rd one has 1 size
		final Image<T> proj = img.createNewImage(new int[] {img.getDimension(0), img.getDimension(1), 1});
		proj.setName("Z max. proj. of "+img.getName());
 
		// Create a positionable cursor for the input
		final LocalizableByDimCursor<T> input_cursor = img.createLocalizableByDimCursor();
 
		// .. and a localizable one for the output
		final LocalizableCursor<T> output_cursor = proj.createLocalizableCursor();
 
		// Now we will iterate through all X and Y positions, using the output
		// cursor to dictate to the input cursor where to go.
		while (output_cursor.hasNext()) 
				{
			 output_cursor.fwd();
			 input_cursor.setPosition(output_cursor); // The output dictate the position of the input
 
			 //Now we crawl through Z to compute the max value along this column.
			 max = null;
						 // Go to (X,Y,0), in this case this call is not necessary but good for illustration
						 input_cursor.setPosition( 0, 2 ); // Set the dimension 2 (ie: Z) at position 0
			 for ( int i=1; i<z_size; ++i )
						 {
				current_value = input_cursor.getType();
								if ( max == null )
										max = current_value.clone();
				else if ( current_value.compareTo(max) > 0 ) 
					max.set( current_value );
								// move forward in z direction
				input_cursor.fwd( 2 );
			 }
 
			 // Then we set the ouput value with the max we have found
			 output_cursor.getType().set(max);
		}
 
		// Done iterating
		output_cursor.close();
		input_cursor.close();
 
		// Display result in ImageJ
		ImagePlus imp_result = ImageJFunctions.copyToImagePlus(proj);
		imp_result.show();
	}
}
```

## Moving outside of images - Outside Strategies

## Comparing performances

## Advanced dimension independent iterating
