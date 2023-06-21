import ij.plugin.filter.PlugInFilter;
import ij.plugin.filter.ExtendedPlugInFilter;
import ij.plugin.filter.PlugInFilterRunner;
import ij.plugin.filter.MaximumFinder;
import ij.plugin.filter.EDM;
import ij.*;
import ij.gui.GenericDialog;
import ij.gui.NonBlockingGenericDialog;
import ij.gui.DialogListener;
import ij.process.*;
import java.awt.*;

/** This ImageJ plugin does Watershed segmentation of the EDM, similar to
  * Process>Binary>Watershed but with adjustable sensitivity.
  * The ImageJ Process>Binary>Watershed algorithm has a tolerance of 0.5.
  *
  * 2022-12-15 Michael Schmid: preview bugs fixed, nonblocking dialog
  */

public class Adjustable_Watershed implements ExtendedPlugInFilter, DialogListener {
    private final static int FLAGS = DOES_8G | PARALLELIZE_STACKS;
    private static double toleranceS = 1.;
    private double tolerance = 1.;
    private int nPasses = 1;
    private int pass = 0;
    private boolean background255;
    private volatile boolean interrupted; /* whether watershed segmentation has been interrupted by the user */
    private MaximumFinder maxFinder =
            new MaximumFinder();          /* we use only one MaximumFinder (nicer progress bar) */
    int width, height, xmax, ymax;

    /** Setup of the PlugInFilter. Returns the flags specifying the capabilities and needs
     * of the filter.
     *
     * @param arg	Defines type of filter operation
     * @param imp	The ImagePlus to be processed
     * @return		Flags specifying further action of the PlugInFilterRunner
     */
    public int setup(String arg, ImagePlus imp) {
        if (imp!=null && !imp.getProcessor().isBinary()) {
            IJ.error("Binary Image required");
            return DONE;
        }
        return FLAGS;
    }

    public int showDialog(ImagePlus imp, String command, PlugInFilterRunner pfr) {
        boolean invertedLut = imp.isInvertedLut();
        background255 = (invertedLut && Prefs.blackBackground) ||
                (!invertedLut && !Prefs.blackBackground);
        width = imp.getWidth();
        height = imp.getHeight();
        xmax = width - 1;
        ymax = height - 1;
        
        NonBlockingGenericDialog gd = new NonBlockingGenericDialog(command+"...");
        gd.addNumericField("Tolerance", toleranceS, 1, 5, "(0.5 is ImageJ standard)");
            gd.addPreviewCheckbox(pfr);     /* passing pfr makes the filter ready for preview */
            gd.addDialogListener(this);     /* the DialogItemChanged method will be called on user input */
            gd.showDialog();                /* display the dialog; preview runs in the  now */
            if (gd.wasCanceled()) return DONE;
            toleranceS = tolerance;
        return IJ.setupDialog(imp, FLAGS);
    }

    public boolean dialogItemChanged(GenericDialog gd, AWTEvent e) {
        tolerance = gd.getNextNumber();
        if (gd.invalidNumber() || tolerance<=0)
            return false;
        // interrupted = false;
        return true;
    }

    public void run(ImageProcessor ip) {
//IJ.log("run "+tolerance+" interr="+interrupted);
        // if (interrupted) return;
        int backgroundValue = background255 ? (byte)255 : 0;
        FloatProcessor floatEdm = new EDM().makeFloatEDM(ip, backgroundValue, false);
        ByteProcessor newIp = floatEdm == null ? null :
                maxFinder.findMaxima(floatEdm, tolerance,
                ImageProcessor.NO_THRESHOLD, MaximumFinder.SEGMENTED, false, true);
        if (newIp == null) {  //segmentation cancelled by user?
        //    interrupted = true;
//IJ.log("interrupted");
            return;
        }
        drawSegmentationLines(ip, backgroundValue, newIp);
        ip.setBinaryThreshold();
    }

    /** Draw the segmentation lines in the original image.
     *  Note that segmentation has eliminated particles with radius less than
     *  the tolerance.  Leave these small particles untouched. */
    private void drawSegmentationLines(ImageProcessor ip, int backgroundValue, ByteProcessor segmentedIp) {
        byte[] origPixels = (byte[])ip.getPixels();
        byte[] segmPixels = (byte[])segmentedIp.getPixels();
        for (int p=0; p<origPixels.length; p++)
            if (segmPixels[p] == 0) origPixels[p] = (byte)backgroundValue;
    }

    /** This method is called by ImageJ to set the number of calls to run(ip)
     *	corresponding to 100% of the progress bar. We transfer it to the
     *  MaximumFinder since it will need most of the processing time */
    public void setNPasses (int nPasses) {
        maxFinder.setNPasses(nPasses);
    }

}
