import ij.*;
import ij.plugin.filter.ExtendedPlugInFilter;
import ij.plugin.filter.PlugInFilterRunner;
import ij.gui.GenericDialog;
import ij.gui.NonBlockingGenericDialog;
import ij.gui.DialogListener;
import ij.process.*;
import ij.plugin.filter.GaussianBlur;
import ij.measure.Calibration;
import ij.gui.Roi;
import java.awt.*;

/** This plugin-filter provides a Highpass command, it subtracts
 * the Gaussian blurred input image from the input image.
 *<p>
 * "Radius (Sigma)" is the standard deviation (blur length) of the Gaussian
 * that will be subtracted.
 *<p>
 * "Scaled Units" (spatially calibrated images only) should be selected if
 * "Radius (Sigma)" is not in pixels but in physical units (e.g., micrometers).
 *<p>
 * "Shift Values to Display Range" adds an offset so that the output will fit
 * into the curently displayed data range. This option should be selected when
 * processing only a selection of a 32-bit (float) image that does not have
 * its pixel values around zero. This option is also useful for most 16-bit images.
 * If "Shift Values to Display Range" is unchecked, the offset, i.e. the output
 * resulting from flat portions of the image, will be 0 for 32-bit float, 32768
 * for 16-bit and 128 for 8-bit (grayscale or RGB) images.
 *<p>
 * If the full image is processed, for grayscale 8-bit and 16-bit images, the
 * grayscale (pixel value) calibration will be set to have zero value at this
 * level. Thus, one can use, e.g., Process>Math>Square after highpass filtering
 * to highlight all pixels deviating from their surrounding.
 *<p>
 * Note that Undo will revert only the image contents, not the calibration.
*/
 /*
 * Version 2020-Jan-03 M. Schmid with nonblocking dialog
 */
public class High_pass implements ExtendedPlugInFilter, DialogListener {

    /** the standard deviation of the Gaussian*/
    private static double sigma = 2.0;
    /** whether sigma is given in units corresponding to the pixel scale (not pixels)*/
    private static boolean sigmaScaled = false;
    /** whether to use the middle of the displayed pixels range as zero for the output */
    private static boolean shiftToDisplay = false;
    /** the ImagePlus of the setup call */
    private ImagePlus imp = null;
    /** the flags specifying the capabilities and needs of the filter */
    private int flags = DOES_ALL|CONVERT_TO_FLOAT|SUPPORTS_MASKING|SNAPSHOT|FINAL_PROCESSING|KEEP_PREVIEW|PARALLELIZE_STACKS;
    /** whether the image has spatial calibration */
    boolean hasScale;
    /** the output level corresponding to zero*/
    private float offset = 0f;
    /** the accuracy of the Gaussian */
    private double accuracy;
     /** The GaussianBlur used for subtracting */
    private GaussianBlur gb;

    public int setup(String arg, ImagePlus imp) {
        if (IJ.versionLessThan("1.52t"))    // generates an error message for older versions
            return DONE;
        if (arg.equals("final")) {
            setCalibration();               //at the very end: calibration (only when processing the full image)
            return DONE;
        } else {
            if (IJ.versionLessThan("1.38u")) // also generates an error message for older versions
                return DONE;
            this.imp = imp;
            return flags;
        }
    }

    /** Ask the user for the parameters
     */
    public int showDialog(ImagePlus imp, String command, PlugInFilterRunner pfr) {
        GenericDialog gd = NonBlockingGenericDialog.newDialog(command, imp);
        sigma = Math.abs(sigma);
        gd.addNumericField("Radius (Sigma)", sigma, 2);
        hasScale = false;
        if (imp.getCalibration()!=null && !imp.getCalibration().getUnits().equals("pixels")) {
            hasScale = true;
            gd.addCheckbox("Scaled Units ("+imp.getCalibration().getUnits()+")", sigmaScaled);
        } else
            sigmaScaled = false;
        gd.addCheckbox("Shift Values to Display Range", shiftToDisplay);
        gd.addPreviewCheckbox(pfr);
        gd.addDialogListener(this);
        gd.showDialog();                    //input by the user (or macro) happens here
        if (gd.wasCanceled()) return DONE;
        IJ.register(this.getClass());       //protect static class variables (filter parameters) from garbage collection
        return IJ.setupDialog(imp, flags);  //ask whether to process all slices of stack (if a stack)
    }

    public boolean dialogItemChanged(GenericDialog gd, AWTEvent e) {
        sigma = gd.getNextNumber();
        if (sigma < 0 || gd.invalidNumber())
            return false;
        if (hasScale)
            sigmaScaled = gd.getNextBoolean();
        shiftToDisplay = gd.getNextBoolean();
        setOffset();                        //offset and accuracy of Gaussian
        return true;
    }

    private void setOffset() {
        ImageProcessor ip = imp.getProcessor();
        if (shiftToDisplay) {
            offset = (float)(ip.getMin() + ip.getMax())/2;
        } else {
            offset = 0f;
            if (ip instanceof ByteProcessor || ip instanceof ColorProcessor)
                offset = 128f;
            else if (ip instanceof ShortProcessor)
                offset = 32768f;
        }
        accuracy = (ip instanceof ByteProcessor || ip instanceof ColorProcessor) ?
            0.002 : 0.0002;
    }

    private void setCalibration() {
        ImageProcessor ip = imp.getProcessor();
        Roi roi = imp.getRoi();
        boolean isFullImage = (roi == null || !roi.isArea() ||(roi.getType()==Roi.RECTANGLE &&
                roi.getBoundingRect().width==ip.getWidth() && roi.getBoundingRect().height==ip.getHeight()));
        /* When processing the full image, calibrate the image to reflect zero level*/
        if (isFullImage && !(ip instanceof FloatProcessor) && !(ip instanceof ColorProcessor)) {
            Calibration cal = imp.getCalibration();
            double slope = 1;
            String valueUnit = "Gray Value";
            if (cal != null && cal.calibrated() && cal.getFunction()== Calibration.STRAIGHT_LINE) {
                slope = cal.getCoefficients()[1];
                valueUnit = cal.getValueUnit();
            }
            double[] coefficients = new double[] {-offset*slope, slope};
            cal.setFunction(Calibration.STRAIGHT_LINE, coefficients, valueUnit);
        }
        if (isFullImage && !shiftToDisplay && (ip instanceof ShortProcessor || ip instanceof FloatProcessor)) {
            double range = ip.getMax() - ip.getMin();
            ip.setMinAndMax(offset-range/2, offset+range/2);
        }
    }

    /** This method is invoked for each slice and color channel during execution.
     * It filters an image by enhancing high-frequency components.
     * @param ip The image subject to filtering.
     * Since the CONVERT_TO_FLOAT flag is set, <code>ip</code> is always a FloatProcessor.
     * The SNAPSHOT flag guarantees that <code>ip</code> has a valid snapshot,
     * which is needed by this plugin for processing.
     */
    public void run(ImageProcessor ip) {
        if (gb==null) gb = new GaussianBlur();
        double sigmaX = sigmaScaled ? sigma/imp.getCalibration().pixelWidth : sigma;
        double sigmaY = sigmaScaled ? sigma/imp.getCalibration().pixelHeight : sigma;
        if (!(sigmaX >= 0 && sigmaY >= 0)) return;
        gb.blurGaussian(ip, sigmaX, sigmaY, accuracy);
        float[] pixels = (float[])ip.getPixels();
        float[] snapshotPixels = (float[])ip.getSnapshotPixels();
        int width = ip.getWidth();
        Rectangle roi = ip.getRoi();
        for (int y=roi.y; y<roi.y+roi.height; y++)
            for (int x=roi.x, p=width*y+x; x<roi.x+roi.width; x++,p++)
                pixels[p] = snapshotPixels[p] - pixels[p] + offset;
    }

    /** Since most computing time is spent in GaussianBlur, forward the
     * information about the number of passes to Gaussian Blur. The
     * ProgressBar will be handled by GaussianBlur. */
    public void setNPasses(int nPasses) {
        if (gb == null) gb = new GaussianBlur();
        gb.setNPasses(2*nPasses); //factor 2 because of blurring in 2 directions
    }
}
