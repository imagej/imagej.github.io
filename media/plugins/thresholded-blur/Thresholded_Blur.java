import ij.plugin.filter.ExtendedPlugInFilter;
import ij.plugin.filter.PlugInFilterRunner;
import ij.*;
import ij.gui.GenericDialog;
import ij.gui.NonBlockingGenericDialog;
import ij.gui.DialogListener;
import ij.process.*;
import ij.measure.Calibration;
import java.awt.*;
import java.awt.event.*;

/** This plugin-Filter provides an edge-preserving averaging
* (smoothing) algorithm. Depending on the parameters and the
* image type, the filter can even sharpen blurred edges.

* The algorithm is a selective mean filter with a circular kernel.
* "Radius" determines the kernel size included in averaging;
* see Process>Filters>Show Circular Masks.
*
* Pixels that deviate from the current pixel by more than a given
* threshold are not included in the averaging process.
*
* The filter behaves like a usual mean filter if the threshold
* is larger than the range of the pixels (e.g. 255 for 8-bit images).
* No filtering is done if threshold = 0.
* The threshold should be smaller than the pixel difference across
* edges that should be preserved, but larger than the noise.
*
* The threshold can be soft. In this case, if the difference between
* the neighbor and the pixel is close to the threshold, i.e., within
*   threshold * (1 - softness)   and   threshold * (1 + softness)
* it contributes with a weight between 0 and 1. For strength > 1,
* the equation uses the softness multiplied by the strength value.
* A soft threshold produces softer edges.
*
* For stronger smoothing, use a value of "Strength" > 1. Then,
* filtering is applied as many times as given by that parameter.
*
* For RGB images, the difference between two pixels can be calculated
* as the distance between the points (r,g,b) in a cartesian system
* or as the difference of brightness (brightness-based). In both cases,
* the weights of the colors can be set in Edit>Options>Conversions.
* "Brightness-based" is advisable for images that have stronger color
* noise than brightness noise.
*
* 2007-11-27, Michael Schmid: first version
* 2023-08-30, Michael Schmid: nonblocking dialog
* 
*/
public class Thresholded_Blur implements ExtendedPlugInFilter, DialogListener {
    // Filter parameters
    private static double radius = 2.;          // The kernel radius, see Process>Filters>Show Circular Masks
    private static double threshold = 10.;      // Blur only over pixels within the threshold
    private static double softness = 0.5;       // softness of the threshold
    private static int howOften = 1;            // Strength: how often to apply the filter
    private static boolean brightnessBased = false;  // Whether to compare only the brightness with the threshold
    // Further class variables
    int flags = DOES_ALL|SUPPORTS_MASKING|SNAPSHOT|KEEP_PREVIEW|PARALLELIZE_STACKS;
    private int nPasses = 1;                    // The number of passes (color channels * stack slices)
    private int pass;                           // Current pass
    protected int kRadius;                      // kernel radius. Size is (2*kRadius+1)^2
    protected int kNPoints;                     // number of points in the kernel
    protected int[] lineRadius;                 // the length of each kernel line is 2*lineRadius+1
    private boolean isRGB;                      // true for RGB images

    /** Setup of the PlugInFilter. Returns the flags specifying the capabilities and needs
     * of the filter.
     *
     * @param arg   Defines type of filter operation
     * @param imp   The ImagePlus to be processed
     * @return      Flags specifying further action of the PlugInFilterRunner
     */    
    public int setup(String arg, ImagePlus imp) {
        return flags;
    }

    public int showDialog(ImagePlus imp, String command, PlugInFilterRunner pfr) {
        String thresholdUnit = "";
        if (imp.getCalibration() != null && imp.getCalibration().getFunction() != Calibration.NONE)
            thresholdUnit = "(uncalibrated)";      // to notify the user that we have uncalibrated units
        isRGB = imp.getProcessor() instanceof ColorProcessor;
        if (!command.endsWith("..."))
            command += "...";
        GenericDialog gd = new NonBlockingGenericDialog(command);
        gd.addNumericField("Radius", radius, 1, 6, "Pixels");
        gd.addNumericField("Threshold", threshold, 2, 6, thresholdUnit);
        gd.addNumericField("Softness", softness, 2, 6, "(0-2)");
        gd.addNumericField("Strength", (double)howOften, 0, 6, "(1-5)");
        if (isRGB) gd.addCheckbox("Brightness-based", brightnessBased);
        gd.addPreviewCheckbox(pfr);             // passing pfr makes the filter ready for preview
        gd.addDialogListener(this);             // the DialogItemChanged method will be called on user input
        gd.showDialog();                        // display the dialog; preview runs in the background now
        if (gd.wasCanceled()) return DONE;
        IJ.register(this.getClass());           // protect static class variables (filter parameters) from garbage collection
        return IJ.setupDialog(imp, flags);      // ask whether to process all slices of stack (if a stack)
    }

    public boolean dialogItemChanged(GenericDialog gd, AWTEvent e) {
        radius = gd.getNextNumber();
        threshold = gd.getNextNumber();
        softness = gd.getNextNumber();
        howOften = (int)gd.getNextNumber();
        if (isRGB) brightnessBased = gd.getNextBoolean();
        if (gd.invalidNumber() || radius<0.5 || threshold<0. || softness<0. || howOften <1 || howOften >5)
            return false;
        makeKernel(radius);                     // determine the kernel size once for all channels&slices
        return true;
    }

    public void run(ImageProcessor ip) {
        //copy class variables to local ones - this is necessary for preview
        int[] lineRadius;
        int kRadius, kNPoints, minPixNumber;
        synchronized(this) {                    //the two following items must be consistent
            lineRadius = (int[])(this.lineRadius.clone()); //cloning also required by doFiltering method
            kRadius = this.kRadius;             //kernel radius
            kNPoints = this.kNPoints;           //number of pixels in the kernel
        }
        if (Thread.currentThread().isInterrupted()) return;
        if (ip instanceof FloatProcessor || ip instanceof ColorProcessor)
            doFiltering(ip, kRadius, lineRadius, threshold, softness, howOften, brightnessBased);
        else {                                  //convert 8-bit & 16-bit data to float
            FloatProcessor fp = ip.toFloat(0,null);
            doFiltering(fp, kRadius, lineRadius, threshold, softness, howOften, brightnessBased);
            ip.setPixels(0,fp);
        }
    }

    /** Filter a FloatProcessor or ColorProcessor
     * @param ip The image subject to filtering, may be a FloatProcessor or a ColorProcessor
     * @param kRadius The kernel radius. The kernel has a side length of 2*kRadius+1
     * @param lineRadius The radius of the lines in the kernel. Line length of line i is 2*lineRadius[i]+1.
     * Note that the array <code>lineRadius</code> will be modified, thus call this method
     * with a clone of the original lineRadius array if the array should be used again.
     * @param threshold Threshold of the filtering algorithm. For a hard threshold, pixels
     * deviating by more are not used for averaging.
     * @param softness Softness of the threshold
     * @param howOften Number of passes. The softness of the threshold and the softening
     * function are modified for howOften > 1 to avoid changing the apparent thereshold and softness.
     */
    //
    // Data handling: The area needed for processing a line, i.e. a stripe of width (2*kRadius+1)
    // is written into the array 'cache'. This array is padded at the edges of the image so that
    // a surrounding with radius kRadius for each pixel processed is within 'cache'. Out-of-image
    // pixels are set to the value of the neares edge pixel. When adding a new line, the lines in
    // 'cache' are not shifted but rather the smaller array with the line lengths of the kernel is
    // shifted.
    //
    public void doFiltering(ImageProcessor ip, int kRadius, int[] lineRadius,
            double threshold, double softness, int howOften, boolean brightnessBased) {
        softness *= howOften;                   // more repetitions need a softer threshold
        float lowerThreshold = (float)(threshold*(1.-softness));
        float upperThreshold = (float)(threshold*(1.+softness));
        float thresholdRange = (float)(2*threshold*softness);
        boolean isFloat = ip instanceof FloatProcessor; // otherwise a ColorProcessor
        float[] pixelsF = null;
        int[] pixelsC = null;
        float rWeight=0, bWeight=0, gWeight=0;  // weights of the colors for brightness determination
        if (isFloat) {                          // get array of the pixel values of the input image
            pixelsF = (float[])ip.getPixels();
        } else {
            pixelsC = (int[])ip.getPixels();    // ColorProcessor pixels
            double[] weights = ColorProcessor.getWeightingFactors();
            rWeight = (float)weights[0];
            gWeight = (float)weights[1];
            bWeight = (float)weights[2];
        }
        int width = ip.getWidth();
        int height = ip.getHeight();
        Rectangle roi = ip.getRoi();
        int xmin = roi.x - kRadius;
        int xEnd = roi.x + roi.width;
        int xmax = xEnd + kRadius;
        int kSize = 2*kRadius + 1;
        int cacheWidth = xmax - xmin;
        int xminInside = xmin>0 ? xmin : 0;
        int xmaxInside = xmax<width ? xmax : width;
        int widthInside = xmaxInside - xminInside;
        float[] cacheF = null;                  // a stripe of the image with height=2*kRadius+1
        int[] cacheC = null;                    // (both float and color versions)
        if (isFloat)
            cacheF = new float[cacheWidth*kSize];
        else
            cacheC = new int[cacheWidth*kSize];
        for (int repetition=howOften; repetition>0; repetition--) {
            for (int y=roi.y-kRadius, iCache=0; y<roi.y+kRadius; y++)
                for (int x=xmin; x<xmax; x++, iCache++) { // fill the cache for filtering the first line
                    if (isFloat)
                        cacheF[iCache] = pixelsF[(x<0 ? 0 : x>=width ? width-1 : x) + width*(y<0 ? 0 : y>=height ? height-1 : y)];
                    else
                        cacheC[iCache] = pixelsC[(x<0 ? 0 : x>=width ? width-1 : x) + width*(y<0 ? 0 : y>=height ? height-1 : y)];
                }
            int nextLineInCache = 2*kRadius;            // where the next line should be written to
            Thread thread = Thread.currentThread();     // needed to check for interrupted state
            long lastTime = System.currentTimeMillis();
            for (int y=roi.y; y<roi.y+roi.height; y++) {
                long time = System.currentTimeMillis();
                if (time-lastTime > 100) {
                    lastTime = time;
                    if (thread.isInterrupted()) return;
                    showProgress(y-roi.y,roi.height);
                }
                int ynext = y+kRadius;                      // C O P Y   N E W   L I N E  into cache
                if (ynext >= height) ynext = height-1;
                int iCache = cacheWidth*nextLineInCache;    //where in the cache we have to copy to
                if (isFloat) {
                    float leftpxl = pixelsF[width*ynext];   //edge pixels of the line replace out-of-image pixels
                    float rightpxl = pixelsF[width-1+width*ynext];
                    for (int x=xmin; x<0; x++, iCache++)
                        cacheF[iCache] = leftpxl;
                    System.arraycopy(pixelsF, xminInside+width*ynext, cacheF, iCache, widthInside);
                    iCache += widthInside;
                    for (int x=width; x<xmax; x++, iCache++)
                        cacheF[iCache] = rightpxl;
                } else {
                    int leftpxl = pixelsC[width*ynext];     //edge pixels of the line replace out-of-image pixels
                    int rightpxl = pixelsC[width-1+width*ynext];
                    for (int x=xmin; x<0; x++, iCache++)
                        cacheC[iCache] = leftpxl;
                    System.arraycopy(pixelsC, xminInside+width*ynext, cacheC, iCache, widthInside);
                    iCache += widthInside;
                    for (int x=width; x<xmax; x++, iCache++)
                        cacheC[iCache] = rightpxl;
                }
                nextLineInCache = (nextLineInCache + 1) % kSize;
                //                                          // F I L T E R   the line
                for (int x=roi.x, p=x+y*width, xCache0=kRadius;  x<xEnd; x++, p++, xCache0++) {
                    if (isFloat) {
                        float value = pixelsF[p];           //the current pixel
                        float sum = 0;
                        float count = 0;
                        for (int y1=0; y1<kSize; y1++) {    // for y1 within the cache stripe
                            for (int x1=xCache0-lineRadius[y1], iCache1=y1*cacheWidth+x1; x1<=xCache0+lineRadius[y1]; x1++, iCache1++) {
                                float v = cacheF[iCache1];  // a point within the kernel
                                float diff = v - value;
                                if (diff < 0) diff = -diff;
                                if (diff <= lowerThreshold) {
                                    sum += v;
                                    count++;
                                } else if (diff < upperThreshold) {
                                    float weight = (upperThreshold - diff) / thresholdRange;
                                    if (howOften >1) {
                                        if (howOften == 2) weight = weight*weight;
                                        else if (howOften == 3) weight = weight*weight*weight;
                                        else if (howOften == 4) weight = (weight*weight)*(weight*weight);
                                        else if (howOften == 5) weight = weight*(weight*weight)*(weight*weight);
                                    }
                                    sum += v*weight;
                                    count += weight;
                                }
                            }
                        }
                        pixelsF[p] = sum/count;
                    } else {    //color
                        int c = pixelsC[p];                 //the current pixel
                        int valueR = (c&0xff0000)>>16;
                        int valueG = (c&0xff00)>>8;
                        int valueB = c&0xff;
                        float sumR = 0, sumG = 0, sumB = 0;
                        float count = 0;
                        for (int y1=0; y1<kSize; y1++) {    // for y1 within the cache stripe
                            for (int x1=xCache0-lineRadius[y1], iCache1=y1*cacheWidth+x1; x1<=xCache0+lineRadius[y1]; x1++, iCache1++) {
                                c = cacheC[iCache1];        // a point within the kernel
                                int vR = (c&0xff0000)>>16;
                                int vG = (c&0xff00)>>8;
                                int vB = c&0xff;
                                float diff;
                                if (brightnessBased) {
                                    diff = valueR*rWeight+valueG*gWeight+valueB*bWeight - (vR*rWeight+vG*gWeight+vB*bWeight);
                                    if (diff < 0) diff = -diff;
                                    if (diff >= upperThreshold) continue;
                                } else {
                                    diff = (float)((vR-valueR)*(vR-valueR)*rWeight+(vG-valueG)*(vG-valueG)*gWeight+(vB-valueB)*(vB-valueB)*bWeight);
                                    if (diff >= upperThreshold*upperThreshold) continue;
                                    diff = (float)Math.sqrt(diff);
                                }
                                float weight = 1;
                                if (diff > lowerThreshold) {
                                    weight = (upperThreshold - diff) / thresholdRange;
                                    if (howOften >1) {
                                        if (howOften == 2) weight = weight*weight;
                                        else if (howOften == 3) weight = weight*weight*weight;
                                        else if (howOften == 4) weight = (weight*weight)*(weight*weight);
                                        else if (howOften == 5) weight = weight*(weight*weight)*(weight*weight);
                                    }
                                }
                                sumR += (float)vR*weight;
                                sumG += (float)vG*weight;
                                sumB += (float)vB*weight;
                                count += weight;
                            }
                        }
                        int iR = (int)(sumR/count+0.5);
                        int iG = (int)(sumG/count+0.5);
                        int iB = (int)(sumB/count+0.5);
                        pixelsC[p] = (((iR<<8)+iG)<<8)+iB;
                    } // else color
                } // for x
                int newLineRadius0 = lineRadius[kSize-1];   //shift kernel lineRadii one line
                System.arraycopy(lineRadius, 0, lineRadius, 1, kSize-1);
                lineRadius[0] = newLineRadius0;
            } // for y
            if (repetition >1) for (int i=0; i<kSize-(roi.height%kSize); i++) { //move kernel back to original position
                int newLineRadius0 = lineRadius[kSize-1];   //shift kernel lineRadii one line
                System.arraycopy(lineRadius, 0, lineRadius, 1, kSize-1);
                lineRadius[0] = newLineRadius0;
            }
            pass++;
        } // for repetition
    }

    /** Create a circular kernel of a given radius. Radius = 0.5 includes the 4 neighbors of the
     *  pixel in the center, radius = 1 corresponds to a 3x3 kernel size.
     *  The output is written to class variables kNPoints (number of points inside the kernel) and
     *  lineRadius, which is an array giving the radius of each line. Line length is 2*lineRadius+1.
     */
    protected synchronized void makeKernel(double radius) {
        if (radius>=1.5 && radius<1.75) //this code creates the same sizes as the previous RankFilters
            radius = 1.75;
        else if (radius>=2.5 && radius<2.85)
            radius = 2.85;
        int r2 = (int) (radius*radius) + 1;
        kRadius = (int)(Math.sqrt(r2+1e-10));
        lineRadius = new int[2*kRadius+1];
        lineRadius[kRadius] = kRadius;
        kNPoints = 2*kRadius + 1;
        for (int y=1; y<=kRadius; y++) {
            int dx = (int)(Math.sqrt(r2-y*y+1e-10));
            lineRadius[kRadius+y] = dx;
            lineRadius[kRadius-y] = dx;
            kNPoints += 4*dx + 2;
        }
    }

    /** This method is called by ImageJ to set the number of calls to run(ip)
     *  corresponding to 100% of the progress bar */
    public void setNPasses (int nPasses) {
        this.nPasses = nPasses;
        pass = 0;
    }

    private void showProgress(int done, int todo) {
        if (nPasses*howOften == 0) return;
        double percent = (double)(pass*todo+done)/(nPasses*howOften*todo);
        IJ.showProgress(percent);
    }
}
