{{Project|ImgLib2}}ImgLib2 is a major redesign of ImgLib, and [[Changes from ImgLib1 to ImgLib2|much has changed]]. This page attempts to provide a "how-to" guide for bringing existing ImgLib1 code up to date with ImgLib2. It is intended as a "quick start" guide—for more details, see the [[Changes from ImgLib1 to ImgLib2]] page.

== Rename packages ==

All packages have changed prefix to avoid a name clash, and to conform to convention ([http://imglib2.net/ imglib2.net] now points to us):
* <code>mpicbg.imglib</code> → <code>net.imglib2</code>

Hence, it is easiest to perform a global search and replace for all instances of the old string with the new. This holds for all renames listed below.

Some core packages have also changed further:
* <code>mpicbg.imglib.image</code> → <code>net.imglib2.img</code>

== Rename classes ==

In general, the Image class has been replaced with Img. Many classes with "Image" in the name have thus been changed to "Img" instead:
* <code>Image</code> → <code>Img</code>
* <code>ImageFactory</code> → <code>ImgFactory</code>
* <code>ImageOpener</code> → <code>ImgOpener</code>

Please note that there are cases where using Img is not appropriate, and a better alternative exists; see the [[Changes from ImgLib1 to ImgLib2]] page for a more complete explanation.

== Use long for dimensional lengths ==

All dimensional lengths are now long (and long[]) instead of int (and int[]). 

== Rename dimensional length accessor methods ==

In addition, core methods for querying dimensional lengths have changed names:
* <code>getNumDimensions()</code> → <code>numDimensions()</code>
* <code>getDimension(int)</code> → <code>dimension(int)</code>
* <code>getDimensions()</code> → <code>dimensions(long[])</code>

For dimensions(long[]), note that it only populates an existing array. There is no method to allocate and return a new dimensional array. Instead, use the following code:

<source lang="java">
final long[] dims = new long[img.numDimensions()];
img.dimensions(dims);
</source>

== Remove references to Container and ContainerFactory ==

Containers are now built in to the Img. For instance, PlanarImg (an implementation of Img) replaces PlanarContainer. Essentially, ContainerFactory and ImageFactory have been combined into ImgFactory. If you have code that creates a Container or ContainerFactory, it is no longer necessary—just create the correct kind of Img or ImgFactory instead (e.g., PlanarImgFactory).

== Update cursor logic ==

There were previously three types: Cursor, LocalizableCursor and LocalizableByDimCursor. This is still true, but the terminology has changed: a cursor can now be "localizable"—meaning you can tell where it is in the dimensional structure—and/or "positionable"—meaning you can move the cursor to somewhere else. Essentially, the three kinds of cursors are now:
# <code>img.cursor()</code> – returns a Cursor with "read-only" access to the dimensional position which is calculated on demand which might be an expensive calculation. Use when you don't care where you are in the structure (or only sparsely need this information), and want the most efficient path.
# <code>img.localizingCursor()</code> – returns a Cursor with "read-only" access to the dimensional position.  Such Cursors track their position at each fwd() call and thus can calculate it more efficiently than the above.  Use when you always or often need to know where the cursor currently sits, but don't need to change the position other than normal iteration.
# <code>img.randomAccess()</code> – returns a RandomAccess with "read-write" access to the dimensional position. Use when you need to change the position.

Another way of looking at it is that Cursors are similar to InputStreams and must go forward, whereas RandomAccesses are similar to RandomAccessFiles and can seek back and forth at will.

== Update out of bounds code ==

Out of bounds access is now handled differently. Previously you could pass an out of bounds strategy factory to a localizable cursor constructor. In a similar fashion now you extend an interval with an out of bounds strategy factory.

Here is an example:
<source lang="java">
ExtendedRandomAccessibleInterval< IntType, Img< IntType> > extendedInterval =
  new ExtendedRandomAccessibleInterval< IntType, Img< IntType > >(
      myIntImg,
      new OutOfBoundsMirrorFactory< IntType, Img< IntType > >( Boundary.DOUBLE ) );
RandomAccess< IntType > randomAccess = extendedInterval.randomAccess();
</source>

== Rename RGBLegacyType to ARGBType ==

If you were using <code>RGBALegacyType</code>, note that it has changed to <code>ARGBType</code>, but serves the same purpose.

== Use net.imglib2.display.Projector instead of mpicbg.imglib.image.display.Display ==

The Display class and corresponding packages are no longer applicable to ImgLib2. Instead, create a Projector.

== Additional issues ==

The RegionOfInterestCursor class is no longer available and its replacement is not yet in place. You'll need to work around this in the short term.

The <code>Image.clone()</code> method has been now named <code>Img.copy()</code>.
