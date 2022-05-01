---
mediawiki: ImgLibProcessor
title: ImgLibProcessor
---

{% include notice icon="warning" content='The following article describes a method of ImageJ 1.x/ImageJ2 integration we explored in 2010, revolving around an `ij.process.ImageProcessor` extension called `ImgLibProcessor` which would enable additional transparent usage of [ImgLib2](/libs/imglib2) from within ImageJ 1.x, thus greatly expanding the available pixel types and storage strategies. However, after discussion with [Wayne Rasband](/people/rasband), we settled on a different method of backwards compatibility known as [ImageJ Legacy](/libs/imagej-legacy). The text below is preserved only for historical reasons.' %} 

## Design

As much as possible `ImgLibProcessor` utilizes operations to implement its functionality. Operation is not a class here but just a concept. If you imagine a processor class the operations are really the methods that act upon the processor's data and live as separate classes rather than within the processor class methods. This was done to reduce the complexity of `ImgLibProcessor`. Originally there was a motivation of having operations that could be chained together. (Not sure how well this motivation was realized)

An operation ties together the concept of iteration and action on data over a user specified region. As an example of a typical operation I'll discuss `imagej.process.operation.SingleCursorRoiOperation`. This abstract class is responsible for managing the iteration over a single imglib Image. Here is its main iteration loop:

```java
/** runs the operation. does the iteration and calls subclass methods as appropriate */
public void execute()
{
    if (this.observer != null)
        observer.init();
         
    final LocalizableByDimCursor<T> imageCursor =
        this.image.createLocalizableByDimCursor();
 
    final RegionOfInterestCursor<T> imageRoiCursor =
        new RegionOfInterestCursor<T>( imageCursor, this.origin, this.span );
         
    beforeIteration(imageRoiCursor.getType());
         
    //iterate over all the pixels, of the selected image plane
    for (T sample : imageRoiCursor)
    {
        // note that the include() method call below passes null as position. This
        // operation is not positionally aware for efficiency. Use a positional
        // operation in the imagej.process.operation package if needed.
             
        if ((this.selector == null) ||
            (this.selector.include(null, sample.getRealDouble())))
            insideIteration(sample);
 
        if (this.observer != null)
            observer.update();
    }
         
    afterIteration();
         
    imageRoiCursor.close();
    imageCursor.close();
 
    if (this.observer != null)
        observer.done();
}
```

The key ideas include:

-   The iteration is encapsulated in this class. Subclasses of this class implement `beforeIteration()`, `insideIteration()`, and `afterIteration()`. (I'll discuss inheritance later)
-   The iteration can be constrained by a function that uses the current value and position of the sample pointed to by the iterator to determine whether to call `insideIteration()`.
-   The iteration can be observed by other classes

As an example we'll look at `imagej.process.operation.MinMaxOperation`. Here is its entire implementation:

```java
public class MinMaxOperation<T extends RealType<T>> extends SingleCursorRoiOperation<T>
{
    private double min, max, negInfinity, posInfinity;
     
    public MinMaxOperation(Image<T> image, int[] origin, int[] span)
    {
        super(image,origin,span);
    }
     
    public double getMax() { return this.max; }
    public double getMin() { return this.min; }
     
    @Override
    protected void beforeIteration(RealType<T> type)
    {
        this.min = type.getMaxValue();
        this.max = type.getMinValue();
        // CTR: HACK: Workaround for compiler issue with instanceof and generics.
        //if (type instanceof FloatType)
        if (FloatType.class.isAssignableFrom(type.getClass()))
        {
            this.posInfinity = Float.POSITIVE_INFINITY;
            this.negInfinity = Float.NEGATIVE_INFINITY;
        }
        else
        {
            this.posInfinity = Double.POSITIVE_INFINITY;
            this.negInfinity = Double.NEGATIVE_INFINITY;
        }
    }
     
    @Override
    protected void insideIteration(RealType<T> sample)
    {
        double value = sample.getRealDouble();
         
        if (value >= this.posInfinity) return;
        if (value <= this.negInfinity) return;
         
        if ( value > this.max )
            this.max = value;
 
        if ( value < this.min )
            this.min = value;
    }
     
    @Override
    protected void afterIteration()
    {
    }
}
```

You can see that a `MinMaxOperation` is pretty simple. It finds the current min and max values of the iterated values. Defining operations in this way is simple and they end up being well encapsulated. However, striving for composition over inheritance I've tried to minimize the number of operation classes.

Using composition to enhance the capabilities of the various operations becomes possible with the definition of `SelectionFunctions`. Recall from the `execute()` method of `SingleCursorRoiOperation` that you can constrain which samples will have further processing done on them using a selector. The selector in the loop is a `SelectionFunction`. Its signature is defined in `imagej.selection.SelectionFunction`:

```java
public interface SelectionFunction
{
    boolean include(int[] position, double sample);
}
```

You can define any function you like that discriminates samples based upon their value and position within their parent `Image`. `SelectionFunctions` are then attached to an operation via `operation.setSelector(selectionFunction)`.

Note that `SelectionFunction` is not in the `imagej.process` package. I view the ability to discriminate samples based upon their value and position as a broad need in ImageJ. I can see how this would be useful in the support of Rois. There is currently code for composing composite selection functions in the `imagej.selection` package. So arbitrarily complex selections can be made.

Once we define selection functions we can utilize them with operations in powerful ways. For example define this selection function:

```java
class Selector implements SelectionFunction
{
    public boolean include(int[] position, double sample)
    {
        if (sample value in range I desire)
            if (position within a rotated ellipse centered at x,y with params z)
                return true;
        return false;
    }
}
```

Create a `MinMaxOperation` and attach this selection function. When you run `operation.execute()` you can get the min and max values found within your selection criteria.

There are operations that change the underlying data as well. `Imagej.process.operation.UnaryTransformOperation` is one example. It will change an underlying Image's data by replacing the data with the computation of a function using the current `Image` as input. The function is defined as a `UnaryFunction` and is passed in to the `UnaryTransformOperation`. `Imagej.process.function.unary.UnaryFunction` looks like this:

```java
public interface UnaryFunction {
    double compute(double input);
}
```

An example of a UnaryFunction would be a `sqr()` function whose `compute()` method would return the square of its input. To square the values of an image you would create a `UnaryTransformOperation` passing it a `sqr()` UnaryFunction and then run `operation.execute()`. It is important to note that a `UnaryFunction` can be arbitrarily complex with its own sets of parameters provided it relies on one input value from an Image.

There are operations defined that do not change data. Imagej.process.operation.QueryOperation is such an operation. A `QueryOperation` applies an `InfoCollector` function to the user specified data. `Imagej.process.query.InfoCollector` looks like this:

```java
/** the InfoCollector interface is used to define queries that can be passed to an
 *  imagej.process.operation.QueryOperation.*/
public interface InfoCollector
{
    /** this method called before the actual query takes place allowing the InfoCollector to initialize itself */
    void init();
     
    /** this method is called at each position of the original dataset allowing data to be collected */
    void collectInfo(int[] position, double value);
     
    /** this method is called when the query is done allowing cleanup and tabulation of results */
    void done();
}
```

When one uses a `QueryOperation` one can then collect information in whatever way desired.

Note that all operations (transforms, queries, etc.) can be modified to only work on a user defined region and then further constrained by value and position selection functions. Any function a user can define can be applied.

Operations are not limited to one dataset. There are operation classes defined that work with various combinations of synchronized datasets (1, 2, and N).

These concepts are utilized throughout the implementation of `ImgLibProcessor`:

A simple unary transform operation -

```java
public void abs()
{
    AbsUnaryFunction function = new AbsUnaryFunction();
 
    nonPositionalTransform(function);  // a private method that does quickest SingRoiOp
}
```

A more complex example that uses a selection function -

```java
/** fills the current ROI area of the current plane of data with the fill color wherever the input mask is nonzero */
@Override
public void fill(ImageProcessor mask)
{
    if (mask==null) {
        fill();
        return;
    }
 
    int[] origin = originOfRoi();
 
    int[] span = spanOfRoiPlane();
 
    byte[] byteMask = (byte[]) mask.getPixels();
 
    FillUnaryFunction fillFunction = new FillUnaryFunction(this.fillColor);
 
    UnaryTransformPositionalOperation<T> transform =
        new UnaryTransformPositionalOperation<T>(this.imageData, origin, span,
                                fillFunction);
 
    SelectionFunction selector = new MaskOnSelectionFunction(origin, span, byteMask);
 
    transform.setSelectionFunction(selector);
 
    transform.execute();
}
```

A two Image operation that uses a `SelectionFunction` -

```java
/** sets the current ROI area data to that stored in the snapshot wherever the mask is nonzero */
@Override
public void reset(ImageProcessor mask)
{
    if (mask==null || this.snapshot==null)
        return;
 
    Rectangle roi = getRoi();
 
    if ((mask.getWidth() != roi.width) || (mask.getHeight() != roi.height))
        throw new IllegalArgumentException(maskSizeError(mask));
 
    Image<T> snapData = this.snapshot.getStorage();
 
    int[] snapOrigin = Index.create(roi.x, roi.y,
                        new int[snapData.getNumDimensions()-2]);
 
    int[] snapSpan = Span.singlePlane(roi.width, roi.height,
                        snapData.getNumDimensions());
 
    int[] imageOrigin = originOfRoi();
    int[] imageSpan = spanOfRoiPlane();
 
    CopyInput2BinaryFunction copyFunction = new CopyInput2BinaryFunction();
 
    BinaryTransformPositionalOperation<T> resetOp =
        new BinaryTransformPositionalOperation<T>(this.imageData, imageOrigin,
                imageSpan, snapData, snapOrigin, snapSpan, copyFunction);
 
    MaskOffSelectionFunction maskOff =
        new MaskOffSelectionFunction(imageOrigin, imageSpan, (byte[])mask.getPixels());
 
    resetOp.setSelectionFunctions(maskOff, null);
 
    resetOp.execute();
 
    if (!this.isUnsignedByte)
    {
        this.min = this.snapshotMin;
        this.max = this.snapshotMax;
    }
}
```

`ImgLibProcessor` also exposes a functional API for further use. Specifically the various `assign()` and `transform()` methods allows one to change an `ImgLibProcessor`'s Image data passing functions as needed.

This can all be tied together in a plugin demo. The following code works on a float image whose values  range between 0 and 1. When the plugin is run the data of the current window image is transformed. Someone who knows more of what a user would really like to do on an image can extend this as desired.

```java
import ij.IJ;
import ij.ImagePlus;
import ij.WindowManager;
import ij.plugin.PlugIn;
import imagej.function.UnaryFunction;
import imagej.ij1bridge.process.ImgLibProcessor;
import imagej.selection.SelectionFunction;
 
import java.util.Random;
  
public class FunctionalPlugin implements PlugIn {
  
    private class MyFunction implements UnaryFunction
    {
        Random rng = new Random();
          
        public double compute(double value)
        {
            return rng.nextDouble();
        }
    }
  
    private class MySelector implements SelectionFunction
    {
        public boolean include(int[] position, double sample)
        {
            if (sample < 0.2) return false;
            if (sample > 0.8) return false;
            if (position[0] % 3 != 0) return false;
            if (position[1] % 2 != 0) return false;
            return true;
        }
    }
  
    public void run(String arg) {
        ImagePlus imp = WindowManager.getCurrentImage();
        ImgLibProcessor<?> proc = (ImgLibProcessor<?>)imp.getProcessor();
        MyFunction function = new MyFunction();
        MySelector selector = new MySelector();
        proc.transform(function, selector);
        imp.updateAndDraw();
    }
 
}
```

## Miscellaneous notes

-   if desired we can likely eliminate inheritance from the operations (in `SingleCursorRoiOperation` for example) by passing it a class that implements an interface that does `before()`, `inside()`, and `after()`. This is similar to `Observer` and `InfoCollector` and we may be able to do some simplification here
-   there are a number of different operations based upon how you are iterating and how many datasets you are simultaneously working with. There is also the built in limitation that iterators are synchronized. I have written proof of concept code to generalize iteration, allowing composition of iterators into either synchronized or nested iterators, eliminating the split between Unary/Binary/NAry functions, etc. Unfinished/untested but close to working.
-   We may want to break out SelectionFunction into `ValueFunction` and `PositionFunction`. Need to think about more

# Required changes to IJ1 to accommodate ImgLibProcessor

This document describes changes required to ImageJ 1.x source code that will faciitate correct behavior when passed ImgLib-backed data. It is divided into 5 sections.

Section 1 outlines changes we've already made to our local copy of IJ 1.44l9 source code. These changes can be integrated into baseline ImageJ as needed.  
Section 2 outlines further changes needed to fully support the new Image type `ImagePlus.OTHER`.  
Section 3 outlines further changes needed to compatibly support a new processor type.  
Section 4 outlines further changes needed related to case logic switching on `ImagePlus::getBitDepth()`.  
Section 5 contains miscellaneous notes  
  

## CHANGES ALREADY MADE to allow ImgLib data to be correctly updated by IJ1

Reflects source code changes as of 12-17-10  
  
### Package ij:
- ImagePlus
    Added another image type : `ImagePlus.OTHER` 
    Updated `getBitDepth()` to calc bits per pixel for OTHER type images  
    Updated `getBytesPerPixel()` to calc number of bytes per pixel for OTHER type images  
    Added double `getActualBytesPerPixel()` to support non-byte-aligned pixel types  
    Updated `setType()` to allow OTHER type  
    Updated `getFileInfo()` to populate self when dealing with OTHER type images  
    Updated `copy(boolean cut)` to use `getActualBytesPerPixel()` in data byte use calculations  
    Updated `getPixel()` to encode pixel data for OTHER type images  

### Package ij.gui:
- ImageCanvas  
    Updated `setDrawingColor()` to have a subcase for OTHER type images  

- ImageWindow  
    Updated `createSubtitle()` to calc bit depth and image size from ImagePlus rather than by type  

- Wand  
    Change code to not use primitive array access for obtaining pixel values. To do so needed to make  
    minor changes to constructor, minor change to `autoOutline()`, and rewrote `getPixel()`.  

### Package ij.io:

- FileInfo  
    Added file type `GRAY64_SIGNED`  
    Modified `getBytesPerPixel()` to support `GRAY64_SIGNED` and `GRAY12_UNSIGNED`  
    Modified `getType()` to return values for `GRAY64_SIGNED` and `GRAY12_UNSIGNED`  

- ImportDialog  
    Added "12-bit Unsigned" to static class variable "types".  
    Updated `getFileInfo()` to identify `GRAY12_UNSIGNED` type files  

### Package ij.measure:
- Calibration  
    Added a method called `isSameAs(Calibration other)`. We rely on this for numerous tests.  

### Package ij.plugin:
- FolderOpener  
    Made minor change to the `run()` method to support OTHER type images  
    Modified `setStackInfo()` to use new `bytesPerPixel` calculation methods  

- ListVirtualStack  
    Updated `showDialog()` to use new `bytesPerPixel` calculation methods  
  
### Package ij.plugin.filter:
- ImageMath  
    Many small edits to use `setf()`/`getf()` rather than direct `float[]` access. Also rather than `instanceof`  
    `FloatProcessor` use `ip.isFloatingType()`.  
    Modify `applyMacro` case logic to test `instanceof SomeProcessor` rather than using `getBitDepth()`

- ParticleAnalyzer  
    Added a type called OTHER. Made many small edits to support.  
    Moved away from direct primitive array access for pixel values and rather use `getf()`/etc. as needed.  
    There some places tagged with "WAYNE PLEASE CHECK" for further review  
    Changed `setThresholdLevels()` to identify images of OTHER type and also set `fillColor` correctly  
    Changed `getStatistics()` to delegate to `ip.getStatistics()` rather than checking image type

- PluginFilterRunner  
    Updated `checkImagePlus()` to have a switch case for images of type OTHER  

### Package ij.plugin.frame:
- ContrastAdjuster
    Minor edit of `setupNewImage()` case logic to support OTHER type images  
    Minor edit of `reset()` case logic to support OTHER type images  
    Update the calculation of decimal places to display for OTHER type images in `setMinAndMax()`
    Update the calculation of decimal places to display for OTHER type images in `setWindowLevel()`

### Package ij.process:
- ImageProcessor  
    Changed visibility of showProgress to public. We have a ProgressTracker class in IJ2 that updates an ip's progress indicator.  
    Changed visibility of `getBilinearInterpolatedPixel()` to public  
    Changed visibility of `resetPixels()` to protected  
    Changed visibility of `create8BitImage()` to protected  
    Added abstract methods for all processors to support:  
     ```java
     int getBitDepth();  
     double getBytesPerPixel();  
     ImageStatistics getStatistics(int mOptions, Calibration cal);  
     boolean isFloatingType();  
     boolean isUnsignedType();  
     double getMinimumAllowedValue();  
     double getMaximumAllowedValue();  
     String getTypeName();  
     double getd(int x, int y);  
     double getd(int index);
     ```

Added a couple set/get methods so our new `ImageProcessor` type can manipulate instance variables as needed  
  protected boolean `getSnapshotCopyMode()` 
  public int `getFgColor()` 
  public void `setFgColor()`
  public Color `getDrawingColor()`

Added a method that is only called on processors of OTHER type by `ImagePlus::getPixel()` 
  `public void encodePixelInfo(int[] destination, int x, int y)` 
  
- ByteProcessor  
    `implementation of the new abstract methods of the ImageProcessor interface` 

- ColorProcessor  
    implementation of the new abstract methods of the ImageProcessor interface  

- FloatProcessor
    implementation of the new abstract methods of the ImageProcessor interface  

- ShortProcessor  
    implementation of the new abstract methods of the ImageProcessor interface  


- ImageStatistics 
    Made a few methods with package access into protected methods  
      `calculateStdDev()`, `setup()`, `fitEllipse()`, `calculateMedian()`
    Changed `getStatistics()` to delegate to passed in ImageProcessor's `getStatistics()` method rather than  
      switching on processor type and hatching a type appropriate ImageStatistics   

- TypeConverter  
    Added support for OTHER image types with new package level access methods:
    ```java  
    ByteProcessor convertOtherToByte()  
    ShortProcessor convertOtherToShort()  
    FloatProcessor convertOtherToFloat().  
    ```

## PLACES WHERE ImagePlus::getType() USES NEED UPDATING

-   `ij.gui.Roi` - `showStatus()` number of decimal places of display would be incorrect for some `Imglib` types without a simple fix.
-   `ij.io.FileOpener` - `setCalibration()` minor change needed to make sure min and max set correctly for the processor.
-   `ij.io.FileSaver` – `saveAsJpeg()`, and `getDescriptionString()` need minor case logic changes. Should check that the various `saveAsXXX()` plugins work for `ImgLibProcessor` backed types.
-   `ij.macro.Functions` - `setPixel()` and `getpixel()` - need minor changes to case logic to support OTHER type
-   `ij.measure.Calibration` - `setImage()` needs minor case logic change to support OTHER type
-   `ij.plugin.filter.Calibrator` - `run()`, `calibrate()`, and `doCurveFitting()` - minor changes to case logic needed to support OTHER type
-   `ij.plugin.filter.Filters` - `setup()` has minor case logic change needed to support OTHER type
-   `ij.plugin.filter.Info` - `getInfo()` needs a subcase for `ImagePlus::OTHER`. Small localized change.
-   `ij.plugin.filter.RankFilters` - `showDialog()` needs minor case logic change for setting number of decimal places if image is a float type
-   `ij.plugin.frame.ContrastAdjuster` – `updatelabels()`, `plotHistogram()`, maybe `apply()` need small case logic adjustments
-   `ij.plugin.filter.ThresholdAdjuster` - `setup()` - minor change to determine not an 8 bit image
-   `ij.plugin.Concatenator` needs more thorough type checking to support OTHER type images. As it stands now it is possible to try and concat two images of type OTHER who have totally different pixel formats. Also cannot concat a `ImagePlus::GRAY16` and a `ImagePlus::OTHER` with backing data that is 16 bit.
-   `ij.plugin.GelAnalyzer` - `plotLanes()` has one line that needs to be changed to support OTHER types
-   `ij.plugin.RGBStackConverter` – `run()` needs some nontrivial changes to support OTHER types
-   `ij.plugin.Slicer` – `run()` needs a float check rather than `GRAY32`. Simple fix.
-   `ij.plugin.StackCombiner` has issues similar to `Concatenator`.
-   `ij.plugin.StackInserter` has issues similar to `Concatenator`
-   `ij.plugin.Thresholder` – `applyThreshold()` needs minor change to support OTHER types
-   `ij.plugin.XYCoordinates` – `run()` tests `GRAY32` rather than `isFloat()`. Simple to fix.
-   `ij.process.ImageConverter` needs a good amount of work to support OTHER types
-   `ij.process.StackConverter` needs a good amount of work to support OTHER types
-   `ij.IJ`: - `doWand()` needs minor change (from `GRAY32` test to `isFloatingType()` test)
-   `ij.Menus` – menu entries needed for OTHER types. And `addWindowMenuItem()` should use new byte use calculation routines.

## PLACES WHERE instanceof SomeProcessor USES NEED UPDATING

-   `ij.io.TextEncoder` – minor change needed (use `!ip.isFloatingType()`) to support OTHER types
-   `ij.macro.Functions` – `getStatistics()` assumes you only have 8 & 16 bit images/histograms. Needs some reworking to support OTHER types.
-   `ij.plugin.filter.BackgroundSubtracter` – needs some substantial work to be extended to support processors of OTHER type
-   `ij.plugin.Convolver` – various methods make assumptions about which kinds of processors can exist. Also seems to rely on `FloatProcessor`. Needs some nontrivial work to support OTHER types
-   `ij.plugin.filter.ImageMath` – in `run()` method there is an unsafe check for signed data. Simple fix. There are also a couple unsafe checks for floating point data. Again a simple fix.
-   `ij.plugin.filter.MaximumFinder` – simple fix needed for determing whether data is floating type
-   `ij.plugin.filter.ParticleAnalyzer` – makes unsafe assumptions. I have mostly updated it already. Wayne may need to make bigger changes. Will talk to Wayne about this one.
-   `ij.plugin.filter.PluginFilterRunner` – tests versus `FloatProcessor`. May not need any changes. May just work but may be inefficient for `ImgLibProcessors` of float type. Study more.
-   `ij.plugin.frame.ContrastAdjuster` – makes some type assumptions. I think I've fixed it in already `\_ij1-patches`.
-   `ij.plugin.frame.ThresholdAdjuster` – `updateLabels()` does a test on `ShortProcessor`. May need to be fixed. `DoSet()` needs to replace instanceof `FloatProcessor` with `ip.isFloatingType()`. `setHistogram()` needs to replace instanceof FloatProcessor with `ip.isFloatingType()`.
-   `ij.plugin.ContrastEnhancer` – makes a few type assumptions. May need some larger rework.
-   `ij.plugin.FITS_Writer` – setup of header relies on either `Short` or `Float`. May need to ask what is needed for OTHER types. `WriteData()` only does float and short. Will not support OTHER type images backed by floats and shorts.
-   `ij.plugin.OrthogonalViews` – makes many assumptions on processor type. Needs nontrivial updates to support OTHER types.
-   `ij.plugin.ZProjector` – makes assumptions that only the current processors will ever exist. Needs nontrivial updating to work.
-   `ij.process.FloodFiller` – simple change needed to constructor to use `ip.isFloatingType()`
-   `ij.process.ImageStatistics` – I think I already made all changes needed and in `\_ij1-patches`
-   `ij.process.TypeConverter` – I think I already made all changes needed and in `\_ij1-patches`
-   `ij.ImagePlus` - I think I already made all changes needed and in `\_ij1-patches`

## PLACES WHERE ImagePlus::getBitDepth() USES NEED UPDATING

-   `ij.io.FileSaver` – `okForFits()` should test `imp.getType()` rather than `imp.getBitDepth()`. Simple.
-   `ij.io.ImportDialog` – rather than test `bitDepth()` it should test `getType()` not `Byte` or `Color`. Simple.
-   `ij.macro.Functions` – `setColor()` needs minor case logic change for 16-bit signed data to avoid throwing an exception unneccesarily. `GetHistogram()`, `setLut()` and `setMinAndMax()` should test `getType()` and not `getBitDepth()`. Simple.
-   `ij.plugin.filter.FFTCustomFilter` – `doInverseTransform()` makes some assumptions about bit depth implying certain types of processors. Needs a closer look.
-   `ij.plugin.filter.FFTFilter` – `filter()` makes some assumptions about bit depth implying certain types of processors. Needs a closer look.
-   `ij.plugin.filter.ImageMath` – "div" case of `run()` assumes 32-bit implies Floating type data. Simple fix. `ApplyMacro()` and `showDialog()` should test versus `imp.getType()` rather than `getBitDepth()`. Simple.
-   `ij.plugin.filter.Info` – `getInfo()` should test `ip.isFloatingType()` rather than `imp.getBitDepth()`. Simple.
-   `ij.plugin.filter.ParticleAnalyzer` – `setup()` tests bit depth when it should test `imp.getType()`. Simple.
-   `ij.plugin.filter.RankFilters` - `run()` tests bit depth when it should test `imp.getType()`. Simple.
-   `ij.plugin.filter.RGBStackSplitter` - `setup()` tests bit depth when it should test `imp.getType()`. Simple.
-   `ij.plugin.filter.Rotator` – uses bitDepth when it should use `getType()` in a few places. Simple fixes.
-   `ij.plugin.frame.Channels` – `itemStateChanged()` assumes 24-bit implies `Color`. Simple fix.
-   `ij.plugin.frame.ColorThresholder` – `sample()`, `checkImage()`, `windowActivated()`, `RGBTpLab()`, and `RGBToYUV()` test bit depth when they should test `imp.getType()`. Simple.
-   `ij.plugin.frame.ContrastAdjuster` – `setMinAndMax()` and `setWindowLevel()` assume 32-bit is Float. Simple fixes to use `isFloatingType()`.
-   `ij.plugin.frame.ThresholdAdjuster` – constructor should test `getType()`. `DoSet()` and `apply()` assume 32-bit is float. Use `isFloatingType()` instead. Simple.
-   `ij.plugin.AVI_Reader` – `run()` has some very minor special case logic for 16-bit. Not sure why. Will need to investigate further.
-   `ij.plugin.BatchConverter` – `run()` uses `getBitDepth()` when it should use `getType()`. Simple.
-   `ij.plugin.BatchProcessor` – `processVirtualStack()` and `processFolder()` use `getBitDepth()` when they should use `getType()`. Simple.
-   `ij.plugin.BMP_Writer - writeImage()` uses `getBitDepth()` when it should use `getType()`. Simple.
-   `ij.plugin.CompositeConverter - run()` uses `getBitDepth()` when it should use `getType()`. Simple.
-   `ij.plugin.ContrastEnhancer` – some issues. investigate further
-   `ij.plugin.FFT - doInverseTransform()` uses `getBitDepth()` when it should use `getType()`. Still a bit more broken as it uses `fht.bitDepth` which is copied from elsewhere. We want to remove reliance on bit depth determining what kind of processor we have.
-   `ij.plugin.FITS_Writer – run()` uses `bitDepth` when it could use `getType()`. This method documented problems with instanceof. Method requires closer inspection.
-   `ij.plugin.FolderOpener – run()` relies on bitDepth numerous times. Need to investigate further.
-   `ij.plugin.Histogram` – `run()` relies on bitdepth when it should use `getType()`. Simple to fix.
-   `ij.plugin.HyperStackConverter` – `convertStackToHS()` relies on bitdepth when it should use `getType()`. Simple to fix.
-   `ij.plugin.HyperStackReducer` – will not work for images of type OTHER as it relies on `IJ.createImage()` which only knows the few predefined image types. Might need way to override the IJ that is in place so we can hook in our own `createImage()`. Also relies on `ImagePlus::createHyperStack()` which also has limited bit depth support. Otherwise `bitDepth` use is fine for this class.
-   `ij.plugin.ImageCalculator` – `calculate()` relies on bit depth rather than `getProcessor().isFloatingType()`. Simple to fix.
-   `ij.plugin.ImagesToStack` – a lot of reliance on bit depth. As is won't work with OTHER type images. Look at this more closely.
-   `ij.plugin.ListVirtualStack` – a lot of reliance on bit depth. Assumes only a few processor types exist. Needs to create processors. We might need Wayne to create a processor factory that we can override. Look at this more closely.
-   `ij.plugin.LUT_Editor` – `run()` uses bit depth when it can be pretty simply avoided.
-   `ij.plugin.PNM_Writer` – `run()` uses bit depth when it can be pretty simply avoided.
-   `ij.plugin.Resizer` – `zScale()` uses bit depth unnecessarily. Simple. `ResizeZ()` and `zScaleHyperStack()` both use bit depth to call `IJ.createImage()`. So again we'll need to override somehow.
-   `ij.plugin.RGBStackMerge` – `mergeStacks()` and `mergeHyperStacks()` need some bit depth access. But also assumes 24-bit is RGB. Simple to remove this assumption.
-   `ij.plugin.Scaler` – `showDialog()` uses bit depth when it could use `getType()`. Simple.
-   `ij.plugin.Slicer` – `resliceHyperStack()` calls `createHyperStack()` with bit depth. Need an override. `CreateOutputStack()` calls `NewImage.createImage()` with bit depth. Again an override needed. `GetOutputStackSize()` uses `bitDepth` to calculate data use sizes. Can use new byte calc methods.
-   `ij.plugin.Straightener` – `straighten()`, `straightenLine()`, and `rotateLine()` all assume 24 bit == RGB. Simple to fix.
-   `ij.plugin.SurfacePlotter – drawAndLabelAxis()` uses `bitDepth` where it could use `getType()`. Simple.
-   `ij.plugin.Thresholder – convertSTackToBinary()` uses `bitDepth` where it could use `getType()`. Simple.
-   `ij.plugin.WandToolsOptions - run()` uses `bitDepth` where it could use `getType()`. Simple.
-   `ij.plugin.XYCoordinates - run()` uses `bitDepth` where it could use `getType()`. Simple.
-   `ij.plugin.ZProjector - doHyperStackProjection()` uses `bitDepth` where it could use `getType()`. Simple.
-   `ij.process.StackStatistics` – constructor and `doCalculations()` rely on bit depth. The 24 bit stuff can use `getType` instead. But the 8 & 16 cases may be fine. Investigate further.
-   `ij.CompositeImage` – constructor assumes 24-bit == RGB. Simple fix.
-   `ij.ImagePlus` – `revert()` and `show()` use bit depth but 8 bit cases. So may be safe but best to replace. Simple fix.
-   `ij.VirtualStack` – `getProcessor` switches on bit depth. Can only support 8, 16, 24, and 32. This is probably okay from the looks of it.

## MISCELLANEOUS NOTES

###   Additional methods desired in `ImageProcessor` and subclasses:

-   double support: setting via `setd()` by (x,y) or by index
-   long support: getting/setting via `getl()`/`setl()` by (x,y) or by index

### Further changes:

-   replace use of `ImagePlus::getBytesPerPixel()` with `ImagePlus::getActualBytesPerPixel()` where needed

 
