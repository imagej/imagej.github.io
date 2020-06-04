
LoopBuilder is part of ImgLib2. It provides a very simple way to implement a pixel wise operation. LoopBuilder can operate on one, two, three, ... up to six images. Simplest case is an operation on one image. LoopBuilder will perform the given operation for every pixel of the image.

Example: Multiply every pixel by a factor of two 2.

<source lang="java">// "image" should be a RandomAccessibleInterval<FloatType>. (IntType, UnsignedByteType, etc. would work as well.)
LoopBuilder.setImages(image).forEachPixel(pixel -> pixel.mul(2));</source>
Slightly more complex is the case with two images. LoopBuilder will iterate simultaneously over both given images. The given operation is executed for each pair of corresponding pixels. "Corresponding" means that the pixels are at the same location in both images. Lets use this to copy the content of image. The value of the source pixel must be copied to the corresponding target pixel:

<source lang="java">// "sourceImage" and "targetImage" should be RandomAccessibleIntervals with the same pixel type.
LoopBuilder.setImages(sourceImage, targetImage).forEachPixel((s, t) -> t.set(s));</source>
It's the same story for three images. LoopBuilder iterates simultaneously over the three images. The operation is executed each triplet of corresponding pixel. This can be used, for example, to add two images.

<source lang="java">// "imageA", "imageB", "imageSum" should be RandomAccessibleInterval<FloatType>. (Any other RealType would work as well.)
LoopBuilder.setImages(imageA, imageB, imageSum).forEachPixel(
    (a, b, s) -> s.setReal(a.getRealFloat() + b.getRealFloat()
);</source>
Or for a pixel wise comparison of two images:

<source lang="java">// "imageA", "imageB", "imageSum" should be RandomAccessibleInterval<FloatType>. (Any other RealType would work as well.)
LoopBuilder.setImages(imageA, imageB, resultImage).forEachPixel(
    (a, b, r) -> {
        if(a.getRealFloat() > b.getRealFloat())
            r.set(1);
        else
            r.set(2);
    }
);</source>
For LoopBuilder images must be <code>RandomAccessibleIntervals</code>. All images must have the same size / dimensions.

LoopBuilder works for for 1D, 2D, 3D, 4D and any other number of dimensions. There is no restriction on pixel types, any pixel typs are supported.

(<code>Img</code>, <code>ArrayImg</code>, <code>PlanarImg</code>, etc. work as well because the implement the <code>RandomAccessibleInterval</code> interface.)

== Tips ==

=== Coordinates ===

LoopBuilder, does not provide a direct way to access the position or coordinates of a pixel in an image. What you can do instead is use <code>Intervals.positions(...)</code>. This will return an image where the pixel values are the positions of the pixel itself. Here is an example:

<source lang="java">LoopBuilder.setImages(Intervals.positions(image), image).forEachPixel(
    (position, pixel) -> {
        long x = position.getLongPosition(0);
        long y = position.getLongPosition(1);
        pixel.setRealDoubel(2 * x * x + 4 * y * y);
    }
);</source>
=== Flat Iteration Order ===

In most cases, LoopBuilder will use flat iteration order. Hence the image is processed line by line, slice by slice, frame by frame... . But that's not guarantied. For example, if all images are <code>CellImg</code> with matching cell sizes, than LoopBuilder will use better suited iteration order. So if your code depends on the flat iteration order, specify <code>.flatIterationOrder()</code> like in the following example. Don't use multi-threading, as for multi threading iteration order is unspecified.

<source lang="java">int[] counter = { 0 };
LoopBuilder.setImages(image).flatIterationOrder().forEachPixel(
    pixel ->  pixel.setInteger(counter[0]++)
);</source>
=== More Than 6 Images ===

LoopBuilder only works with up to six images. This is not because any technical reason, but because the code would become rather clunky. When you have many images, changes are high, that some of the images are similar. These images have the same pixel type, and somehow belong together.

Lets look at an example again. Let's calculate the maximum over 8 images. That are to many images for LoopBuilder. But we can combine the 8 images, using <code>Views.collapse(Views.stack(...))</code>. This will fuse the images into one image, where each pixel is a vector of size 8. The vector contains all the pixel values of the 8 corresponding pixels.

<source lang="java">// ... Initialize all images ...

// Combine image1, ..., image8 into a combined image, where each pixel is a vector.
RandomAccessibleInterval< ? extends GenericComposite< FloatType > > combined =
    Views.collapse( Views.stack( image1, image2, image3, image4, image5, image6, image7, image8 ) );
        
LoopBuilder.setImages( combined, resultImage ).forEachPixel( (vector, r) -> {
    float max = Float.NEGATIVE_INFINITY;
    for ( int i = 0; i < 8; i++ )
    {
        max = Math.max( max, vector.get(i).getRealFloat() );
    }
    r.setReal( max );
} );</source>
== Alternatives ==

LoopBuilder provides nothing, that is otherwise impossible to achieve. It is just a nice way, to write otherwise complex loops. But you could achieve the same results with ImgLib2 <code>Cursor</code> or <code>RandomAccess</code>. Lets add two images using <code>Cursor</code>:

<source lang="java">Cursor<FloatType> cursorA = Views.flatIterable(imageA).cursor();
Cursor<FloatType> cursorB = Views.flatIterable(imageB).cursor();
Cursor<FloatType> cursorSum = Views.flatIterable(imageSum).cursor();
while(sourceCursor.hasNext()) {
    FloatType a = cursorA.next();
    FloatType b = cursorB.next();
    FloatType s = cursorS.next();
    s.setReal(a.getRealFloat() + b.getRealFloat());
}</source>
The example above is actually still quite simple. And a <code>Cursor</code> is fast for basic image containers like <code>ArrayImg</code>, <code>PlanarImg</code> and sometimes <code>CellImg</code>. But it's faster to use <code>RandomAccess</code> when you use views like <code>View.extendBorder(...)</code>, <code>Views.interval(...)</code>, <code>Views.rotate(...)</code> etc. Writing a loop that uses no Cursors at all is much harder. Here is an example that sets all pixels of an image to 1.

<source lang="java">RandomAccess< IntType > ra = image.randomAccess();
ra.setPosition( image.min( 2 ), 2 );
for ( long z = image.min( 2 ); z <= image.max( 2 ); z++ )
{
    ra.setPosition( image.min( 1 ), 1 );
    for ( long y = image.min( 1 ); y <= image.max( 1 ); y++ )
    {
        ra.setPosition( image.min( 0 ), 0 );
        for ( long x = image.min( 0 ); x <= image.max( 0 ); x++ )
        {
            IntType pixel = ra.get();
            pixel.setInteger( 1 );
            ra.fwd( 0 );
        }
        ra.fwd( 1 );
    }
    ra.fwd( 2 );
}
</source>
== Multi Threading ==

If your images are big, than multithreading might speed up the operation. And it's super easy if you use LoopBuilder. Let's calculate the sum using multiple threads. The only thing you need to do is write <code>.multiThreaded()</code> before the call to <code>forEachPixel(...)</code>.

<source lang="java">// calculate sum, using multiple threads:
LoopBuilder.setImages(imageA, imageB, imageS).multiThreaded().forEachPixel(
                                              ///////////////
    (pixelA, pixelB, pixelS) -> {
        pixelS.set(pixelA.getRealFloat() + pixelB.getRealFloat());
    }
);</source>
This should run about four times faster, on a CPU with four CPU cores. (Your image needs two be big enough.) What LoopBuilder internally does, is the following: It splits the images into chunks, and the chunks are than distributed to a pool of threads.

But be careful, multi-threading works well as long as your operation is thread-safe. This is the case for simple operations like "pixelS = pixelA + pixelB". An per pixel operation is NOT thread-safe if it changes a object, field or variable outside the of operation. Let's take a look at the following example: It calculates the sum over the squared pixel values:

<source lang="java">FloatType squareSum = new FloatType(0);
LoopBuilder.setImages(image).forEachPixel(
   pixel -> {
      squaredSum.setReal(squaredSum.getRealFloat() + Math.pow(pixel.getRealFloat, 2));
   }
)</source>
Here the per pixel operation (line 3-5) changes the <code>squaredSum</code>, which is defined in line 1, outside of the per pixel operation. Only adding <code>.multiThreaded()</code> will cause wrong results. This is because the operation is simultaniously executed by mutliple threads. All the threads simultaniously changing the <code>squaredSum</code> causes choas. The wrong result is the consequence.

Luckily LoopBuilder provides a solution to this problem. LoopBuilder devides the image into chunks, and destributes the chunks to a pool of threads. A chunk is always only processed by one thread. That's why there are no multi-threading problems as long as we have one <code>squaredSum</code> variable per chunk. This can be done using LoopBuilders <code>.forEachChunk(...)</code> method:

<source lang="java">// For each chunk calculate an individual squared sum.
List<FloatType> listOfSquaredSums = LoopBuilder.setImages(image).multithreaded().forEachChunk( chunk -> {
   FloatType squaredSum = new FloatType(0);
   chunk.forEachPixel( pixel -> {
      squaredSum.setReal(squaredSum.getRealFloat() + Math.pow(pixel.getRealFloat, 2));    
   } );
   return squaredSum;
})

// Calculate the sum about all the individual squared sums.
FloatType totalSquaredSum = new FloatType(0);
for(FloatType squareSum : listOfSquaredSums) {
   totalSquaredSum.add(squaredSum);
}</source>
In the example above the per pixel operation (in line 5) can access variables and objects that belong to the chunk (in line 3 - 7) without causing any thread safety issues.

Another use case for the <code>forEachChunk</code> mappens, happens if your per pixel operation needs some resources. The following examples swaps the content of two images A and B. The temporary variable <code>tmp</code> is used to swap the pixel value. But creating a <code>new FloatType()</code> for each pixel would be very slow, but creating one temporary variable per chunk, is fine:

<source lang="java">LoopBuilder.setImages(imageA, imageB).multiThreaded().forEachChunk( chunk -> {
    FloatType tmp = new FloatType(); // create require resource
    chunk.forEach((a, b) -> {
        tmp.set(a);   // operation using the resource
        a.set(b);
        b.set(tmp);
    });
    // Optional: free your resource if needed.
    return null; // Optional: return some results.
})</source>
Disclaimer: Please always measure the execution time if you use multi-threading. Sometimes the simgle threaded code is better optimized by the compiler and runs even faster than the multi-threaded code. Also check that you don't have thread-safety issues, make sure your results are correct. Thread-safety problem are hard to debug!

== Performance ==

Disclaimer: LoopBuilder achieves good perfomance in Java, but it is slow when used in scripting languages like Groovy or Jython. (This is because LoopBuilder relies on Lambda expression, and using them in scripting languages is rather complicated and slow.)

LoopBuilder has been heavily benchmarked and designed to give good perfance. This performance advantage compared to for example <code>Cursor</code> loops is most noticible for methods that are used with different image types (For example <code>ArrayImg</code>, <code>PlanarImg</code>, <code>Views.interval(...)</code>, etc. ). Because LoopBuilder will execute the loop in a way, that promises good performance for the particular image type. The strategies that are used to provide the best performance are discribed below.

Still, if you write a piece of very specialized code that always runs on only one image type (maybe <code>ArrayImg<BoolType></code>). Then writing your own loop using <code>Cursor</code> or <code>RandomAccess</code> might give better performance. But always carefully measure the execution time.

[https://gist.github.com/maarzt/19167a5019c1d685c483441b7322b986 Benchmark comparing LoopBuilder and Cursor]

=== Cursor vs. RandomAccess ===

LoopBuilder either uses a loop that uses <code>Cursor</code>s. That's the case if all the images have fast <code>Cursor</code>s like <code>ArrayImg</code>, <code>PlanarImg</code>, <code>CellImg</code> and for slices of <code>ArrayImg</code>. But in all other cases <code>RandomAccess</code>es are used. The <code>RandomAccess</code> are moved simultaneously along the image. The methods <code>RandomAccess.fwd(int d)</code> and <code>RandomAccess.move(long offset, int d)</code> are used, which happens to be faster than <code>setPosition(long[] pos)</code>.

=== Iteration Order ===

Usually flat iteration order is used. Currently the only exception happens, when all images are 'CellImg' of matching cell size. Than the <code>CellImg</code> specific iteration order will be used.

=== Byte Code Copying for JIT-Optimization ===

The loops that are used for image processing are usually very tight. (A few number of operations per cycle) The performance of these tight loops heavily depends on the byte-code optimizations done by Java's just-in-time-compiler. Sadly the JIT-compiler de-optimizes byte-code that is used with different implementations of the same interface.

Hence writing a loop that performs a simple image processing step, like adding two images, will runs very fast only if used with <code>ArrayImg</code>. But using it with <code>ArrayImg</code>, <code>CellImg</code> and <code>IntervalView</code> will cause the byte-code to be de-optimized and to dramatically reduce performance.

LoopBuilder circumvents this problem, by loading a new copy of the class running the loop, for every new combination of images (<code>ArrayImg</code>s, <code>CellImg</code>s, etc.) Each copy of the class, has a it's own copy of the byte-code. And these individual copies of the byte-code are individually optimized byte the JIT-compiler to the particular image classes used. Hence avoiding the de-optimization.
