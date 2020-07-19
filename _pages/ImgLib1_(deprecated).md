{{ComponentStats:sc.fiji:legacy-imglib1}}{{ImgLib1_Deprecation_Notice}}

= Citation =
Please note that the ImgLib, as well as other plugins available through Fiji, is based on a publication. If you use it successfully for your research please be so kind to cite our work:
* S. Preibisch, P. Tomancak, S. Saalfeld (2010) "Into ImgLib – Generic Image Processing in Java", ''ImageJ User and Developer Conference 2010'' (1):72-76. [http://imagejconf.tudor.lu/program/workshops/preibisch/start Webpage] [http://fly.mpi-cbg.de/preibisch/pubs/imagejpaper2010.pdf PDF]

= Introduction =

In ImageJ, images can have a number of types (''8-bit gray'', ''8-bit with lookup table'', ''16-bit'', ''32-bit floating point'', ''RGB packed into a 32-bit int''), and up to 5 dimensions. Internally, every image is stored as an array of ''channels * slices * frames'' instances of the class ''ImageProcessor'', which in turn stores the pixel values as arrays of ''width * height'' values which have the native types ''byte'', ''short'', etc

When implementing an image processing algorithm, typically this has to be done with every native type separately, for performance reasons, and for the same reason, there is a lot of code repeated between different plugins.

In C++, this problem is solved by using ''templates'', e.g. in the [http://www.itk.org/ ITK library]. The idea is to implement the algorithm generically, i.e. independent of data type.

The corresponding technique in Java is called ''generics'' and is available since Java version 1.5. Due to technical issues, Java cannot optimize specializations of generics fully at compile-time, and generics have other limitations, such as not being able to use basic types (which are used for ImageJ's pixel values) as parameters.

In ''imglib'', these issues have been addressed, in a way compatible with Java.


= Vocabulary =

<b>Type</b>: The Type class wraps a value, in the same way that the java.lang Integer, Double, Float, etc. wrap a value. The value is not necessarily a primitive (like int, short, long, char, float, double ...) but can be a complex number, base pair, boolean, label, and other non-numerical types.

<b>Outside Strategy</b>: The OutsideStrategy is a method to handle values when requested at a position beyond the boundaries of the image. Typical outside strategies may be to return a constant value, or to mirror the values of the image.

= Core ideas of the architecture =

Since basic types cannot be passed as parameters to Java generics, and operators cannot be overloaded, all values must be accessed via ''Type'' instances. ''Type'' is the base interface for all data types handled by imglib. If you need a new data type to be handled, just make a new class implementing the ''Type'' interface. There is a convenient abstract class "TypeImpl" that provides default implementations for some common methods.

To access pixel values, ''imglib'' provides ''Cursor'' classes. The simplest ''Cursor'' just iterates over all pixels of the image. This cursor is guaranteed to traverse the pixels in an optimal fashion, regardless of the way the pixels are stored in memory. There are other cursors, implementing the ''Localizable'' interface, which report their position. The most specific cursor is the ''LocalizableByDimCursor'', which allows to set the position to a specified one.

Especially for large images, which become more and more prevalent, it is interesting to have different storage strategies. Plain ImageJ provides only one storage strategy: every XY slice of a (possibly 5-dimensional) stack is stored as a one-dimensional basic type array which is a linearized version of the 2-dimensional slice (i.e. each pixel is addressed using an index which is calculated as ''x + y * width'').

In addition to adapters wrapping ImageJ's ImagePlus, ''imglib'' currently supports two container types: a container wrapping an image as a linearized array of a basic type (available in the ''mpicbg.imglib.array'' package) and a container wrapping the image as so-called ''cells'', which are sort of n-dimensional "tiles" (in 3D, would be a cube). The latter container is available in the package ''mpicbg.imglib.container.cell'' and has the advantage to be "pageable", i.e. not the complete image has to be loaded into memory at the same time, allowing for images larger than the available RAM. This is comparable, but more powerful, than ImageJ's VirtualStack concept.

= Example =

Let's look at a simple function multiplying every pixel value with a given constant.

=== Using  ''imglib'' ===

No matter what kind of image (a single image, a stack, a 4D stack, with one color channel or three...), the algorithm is  implemented cleanly and clearly:

<source lang="java">
public <T extends NumericType<T>> void mul( Image<T> input, T factor )
{
        for ( final T value : input )
          value.mul( factor );
}
</source>

=== Using ImageJ ===

In plain ImageJ, the same function looks like the following. Notice how we have to litter the code with special cases, and we have to know before hand the number of channels, slices, and pixels per slice. We even need a helper function to simplify operations a bit!

<source lang="java">
 final static public void multiply( final ImagePlus input, final double factor )
 {
         final int nPixels = input.getWidth() * input.getHeight();
         
         // iterate through all channels, frames and timepoints (might be just one)
         for ( int c = 1; c <= input.getNChannels(); ++c )
                 for ( int z = 1; z <= input.getNSlices(); ++z )
                         for ( int t = 1; t <= input.getNFrames(); ++t )
                         {
                                 input.setPosition( c, z, t );
                                 final ImageProcessor ip = input.getChannelProcessor();
                                 
                                 // RGB images are special
                                 if ( input.getType() == ImagePlus.COLOR_RGB )
                                 {
                                         for ( int i = 0; i < nPixels; ++i )
                                         {
                                                 final int rgb = ip.get( i );
                                                 final int r = doubleTo8Bit( Math.round( ( (
                                                         rgb >> 16 ) & 0xff ) * factor ) );
                                                 final int g = doubleTo8Bit( Math.round( ( (
                                                         rgb >> 8 ) & 0xff ) * factor ) );
                                                 final int b = doubleTo8Bit( Math.round( (
                                                         rgb & 0xff ) * factor ) );
                                                 ip.set( i, ( r << 16 ) | ( g << 8 ) | b );
                                         }
                                 }
                                 else
                                 {
                                         for ( int i = 0; i < nPixels; ++i )
                                         {
                                                 ip.setf( i, ip.getf( i ) * ( float )factor );
                                         }
                                 }
                         }
 }
 
 final static int doubleTo8Bit( final double value ) {
         return Math.max( 0, Math.min( 255, (int) value ) );
 }
</source>

The performance is better in the ''ImgLib'' version, as there is no need for two type conversions in every iteration: the Type instance implements the native operation ''mul()'', and since the implementation is labeled using the Java keyword ''final'', it will be inlined and optimized pretty quickly by Java's Just-In-Time compiler. Furthermore it will work on any ComplexType (even for example real numbers) that are available or will be implemented in the future.

= Tutorials and howtos =

* [[Using Imglib in a plugin]]
* [[Imglib: iterating through pixel data]]
* [[Imglib FAQ]]
* [[Developing Imglib]]

[[Category:ImgLib]]
[[Category:Citable]]
