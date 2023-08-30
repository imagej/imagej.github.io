import ij.plugin.filter.ExtendedPlugInFilter;
import ij.plugin.filter.PlugInFilterRunner;
import ij.plugin.filter.MaximumFinder;
import ij.plugin.filter.Analyzer;
import ij.plugin.filter.EDM;
import ij.measure.Calibration;
import ij.measure.ResultsTable;
import ij.*;
import ij.process.*;
import ij.gui.*;
import java.awt.*;
import java.awt.event.*;
import java.util.Vector;

/**
 * A template matching plugin, finds features equal or similar to a prototype (template).
 * "Similarity" means that the mean square deviation between the image
 * and the translated prototype should be low.
 *
 * Features:
 * - After a (slow) initial calculation, preview provides a fast way to determine the similarity threshold
 * - Subpixel accuracy
 * - During preview, possibility to refine the prototype by averaging over features found
 *
 *
 * Limitations:
 * - Works with grayscale images only; any calibration of pixel values is ignored.
 * - Only searches for unrotated (or circular) and unscaled features.
 * - Features should have the same gray level contrast as the prototype.
 * - Slow except for very small prototypes (brute-force algorithm).
 * - During preview, while the prograss bar is active: don't change any input in the
 *   dialog box, otherwise it will restart and take even longer.
 * - Does not process stacks

 * Dialog Options:
 *
 * 'Prototype from' selects the prototype. This can be a ROI of the current image or a different image.
 *
 * 'Output Type' can be:
 *  - Point Selection: A Point ROI of the centers of all features
 *  - Count: The number of features found is written to the Results Table
 *  - List: A list of x and y coordinates of the centers is written to the Results Table
 *  - Point Map: A separate binary image with one pixel=255 at the center of each feature
 *  - Deviation Map: A separate float (32-bit) image. The value at each point indicates
 *    how much the surroundings of this position in the original image deviate from the
 *    prototype. The Deviation Map is independent of the 'Tolerance' settings.
 *  - Average of Features: A separate float (32-bit) output image with the average of all
 *    features shifted to the same position.
 *
 * With 'Subtract Background', features are considered the same independent of
 * any constant (additive) background.
 *
 * 'Soft Edges' gives less weight to the near-edge pixels of the prototype than to those
 * near the center.
 *
 * If features are close together, closer than 'Distance Min', then only the one with the
 * best match is kept.
 *
 * 'Tolerance' determines how much a feature may deviate from the prototype. A value of 0
 * means an exact match, 100 means that the deviation equals the variance of the prototype.
 * With 'Subtract Background' on, at a tolerance of 100% also image areas with a constant
 * value over the prototype area qualify as features.
 *
 * During preview, after setting the tolerance you may press the 'Refine' button. This
 * calculates a new prototype from the average of all features currently selected.
 * 'Refine' is useful, e.g., if the prototype suffers from noise.
 *
 * During preview, the dialog also displays a histogram of the number of features vs.
 * deviation from the prototype and a message with the number of features found.
 *
 *
 * Version 2010-Dec-28 Michael Schmid: added spatial calibration of output images
 * Version 2011-Jan-27 Michael Schmid: no point labels on preview (unless multi-point tool is active)
 *                                     added help button
 * Version 2012-Dec-23 Michael Schmid: multithreading for deviation map, no exception if no features
 * Version 2020-Mar-13 Michael Schmid: adds list of calibrated coordinates
 */
public class Feature_Finder implements ExtendedPlugInFilter, DialogListener, ActionListener {
    /** Output type: point selection */
    public final static int OUTTYPE_POINTS = 0;
    /** Output type: count and add to Roi Manager */
    public final static int OUTTYPE_COUNT = 1;
    /** Output type: list of x, y, variance into ROI Manager */
    public final static int OUTTYPE_LIST = 2;
    /** Output type: list of x, y, variance into ROI Manager */
    public final static int OUTTYPE_LIST_CAL = 3;
    /** Output type: point image */
    public final static int OUTTYPE_POINT_IMAGE = 4;
    /** Output type: deviation map */
    public final static int OUTTYPE_MAP = 5;
    /** Output type: average of all features found */
    public final static int OUTTYPE_AVERAGE = 6;
    //
    private final static String[] outTypes = new String[]
            {"Point Selection", "Count", "List", "List (calibrated)", "Point Map", "Deviation Map", "Average of Features"};
    //filter parameters
    private static int outType;         // what type of output to produce
    private static boolean subtractBackground = true; //ignore a constant offset between image and prototype
    private static boolean softEdges;   // prototype weighting function tapering off at edges
    private static double tolerance=30; // in % of variance of kernel
    private static double minDistance=2;// min distance between features, in pixels
    private static int protoImageIndex; // index of default prototype in protoImages
    //dialog
    private boolean previewing;         // true during preview
    private Checkbox previewCheckbox;
    private PlugInFilterRunner pfr;
    private boolean doRefine;           // triggers refine
    private Button refineButton;
    private Label messageArea;          // reference to the textmessage area (number of maxima)
    private HistogramPlot histogramPlot;
    private int[] histogram;
    //other
    private int flags = DOES_8G|DOES_16|DOES_32|CONVERT_TO_FLOAT|NO_CHANGES|NO_UNDO;
    private ImagePlus imp;              // we search for features here
    private ImagePlus[] protoImages;    // suitable prototype images
    private Roi roi;                    // roi containing the prototype
    private boolean roiSaved;           // whether the filter has changed the roi and saved the original
    private int xOffset, yOffset;       // center of kernel
    private FloatProcessor deviationMap;
    private boolean deviationMapOK;     // whether the deviation map and pointList are up to date
    private float[][] pointList;        // contains x, y, value
    private boolean[] pointOKlist;      // true if a point dominates within minDistance
    private boolean minDistanceOK;      // whether the pointOKlist is up to date

    public int setup (String arg, ImagePlus imp) {
       if (IJ.versionLessThan("1.52t")) // generates an error message for older versions
            return DONE;
        this.imp = imp;
        return flags;
    }

    public int showDialog (ImagePlus imp, String command, PlugInFilterRunner pfr) {
        this.pfr = pfr;
        protoImages = getPrototypeImages(imp);
        if (protoImages == null) {
            IJ.error(command+" Error", "No prototype feature.\n"+
                    "Create a selection with the prototype or supply\n"+
                    "a separate grayscale image with a prototype.");
            return DONE;
        }
        String[] protoChoices = new String[protoImages.length];
        for (int i=0; i<protoImages.length; i++) {
            protoChoices[i] = protoImages[i].getTitle();
            if (protoImages[i] == imp) protoChoices[i] += " (this one)";
        }
        if (protoImageIndex >= protoImages.length) protoImageIndex = 0;
        GenericDialog gd = NonBlockingGenericDialog.newDialog(command, imp);
        gd.addChoice("Prototype From", protoChoices, protoChoices[protoImageIndex]);
        gd.addChoice("Output Type", outTypes, outTypes[outType]);
        gd.addCheckbox("Subtract Background", subtractBackground);
        gd.addCheckbox("Soft Edges", softEdges);
        gd.addNumericField("Distance Min.", minDistance, 1, 6, "pixels");
        gd.addSlider("Tolerance (%)", 0, 100, tolerance);
        gd.addPreviewCheckbox(pfr, "Preview Point Selection");
        previewCheckbox = gd.getPreviewCheckbox();
        gd.addMessage("                        "); //space for number of maxima
        messageArea = (Label)gd.getMessage();
        histogramPlot = new HistogramPlot();
        Panel panel = new Panel();
        panel.add(histogramPlot);
        gd.addPanel(panel);
        refineButton = new Button("Refine");
        refineButton.setEnabled(false);
        panel = new Panel();
        panel.add(refineButton);
        gd.addPanel(panel);
        gd.addDialogListener(this);
        refineButton.addActionListener(this);
        gd.addHelp("http://imagejdocu.tudor.lu/doku.php?id=plugin:analysis:feature_finder:start");
        previewing = true;
        boolean saveNoPointLabels = Prefs.noPointLabels;
        Prefs.noPointLabels = true;
        gd.showDialog();                    // input by the user (or macro) happens here
        previewing = false;
        Prefs.noPointLabels = saveNoPointLabels;
        if (gd.wasCanceled()) {
            if (roiSaved) imp.restoreRoi();
            return DONE;
        }
        return flags;
    } //public int showDialog

    public boolean dialogItemChanged(GenericDialog gd, AWTEvent e) {
        int iTemp = gd.getNextChoiceIndex();
        if (iTemp != protoImageIndex) {     // new calculation required if new prototype
            doRefine = false;
            protoImageIndex = iTemp;
            deviationMapOK = false;
        }
        outType = gd.getNextChoiceIndex();
        subtractBackground = gd.getNextBoolean();
        softEdges = gd.getNextBoolean();
        double minDistanceTemp = gd.getNextNumber();
        tolerance = gd.getNextNumber();
        if (minDistanceTemp < 0 || tolerance < 0 || gd.invalidNumber())
            return false;
        if (minDistanceTemp != minDistance) {
            minDistance = minDistanceTemp;
            minDistanceOK = false;
        }
        //new calculation required if 'softEdges' or 'subtractBackground' changed:
        Object src = e==null ? null : e.getSource();
        if ((src instanceof Checkbox) && src!=previewCheckbox)
            deviationMapOK = false;
        return true;
    }

    /** "refine" Button callback */
    public void actionPerformed(ActionEvent e) {
            if (!deviationMapOK || pointList==null) {
                IJ.error("Refinement requires a ");
            }
            doRefine = true;
            deviationMapOK = false;
            if (previewCheckbox.getState())
                pfr.dialogItemChanged(null, e);     //trigger preview thread
    }

    /** unused, we don't process stacks or RGB image channels */
    public void setNPasses(int nPasses) {
    }


    /** Called by the PlugInFilterRunner to process the image or one frame of a stack */
    public void run (ImageProcessor ip) {
        int width = ip.getWidth();
        int height = ip.getHeight();
        boolean doHistogram = false;
        if (!deviationMapOK) {
            deviationMapOK = true;
            doHistogram = true;
            minDistanceOK = false;
            if (previewing) messageArea.setText("wait...");
            ImagePlus protoImage = protoImages[protoImageIndex];
            roi = protoImage.getRoi();
            ImageProcessor protoIp;
            if (protoImage == imp) {
                protoIp = ip;
                if (roiSaved && !doRefine) {
                    imp.restoreRoi();   //we need the original roi for the prototype
                    roiSaved = false;
                }
            } else
                protoIp = protoImage.getProcessor().toFloat(0, null);
            if (doRefine && pointList!=null) {
                ImageProcessor avgIp = makeAverage(ip, pointList, pointOKlist,
                        tolerance, roi, xOffset, yOffset, 0);
                if (avgIp == null) {
                    IJ.beep();
                    IJ.error("Feature Finder Error", "Cannot refine: No features inside image");
                    return;
                } else {
                    protoIp = avgIp;
                    roi = (Roi)roi.clone();
                    roi.setLocation(0,0);
                }
            }
            Kernel kernel = new Kernel(protoIp, roi, subtractBackground, softEdges);
            xOffset = kernel.getXoffset();
            yOffset = kernel.getYoffset();
            if ((Thread.currentThread().isInterrupted())) {
                deviationMapOK=false;
                if (!previewing) {IJ.beep(); IJ.showStatus("interrupted");}
                return;
            }
            deviationMap = kernel.deviationMap(ip);
            if (deviationMap == null) { deviationMapOK=false; return; }; //interrupted
            if (previewing || outType!=OUTTYPE_MAP) {
                invertSign(deviationMap);       //we search for minima of deviation
                ByteProcessor maxIp = new MaximumFinder().findMaxima(deviationMap, 0.01,
                    ImageProcessor.NO_THRESHOLD, MaximumFinder.SINGLE_POINTS, true, false);
                if (maxIp==null) { deviationMapOK=false; return; };
                invertSign(deviationMap);
                pointList = makeList(maxIp, deviationMap, 2.0f);
            }
            if ((Thread.currentThread().isInterrupted())) { deviationMapOK=false; return; };
        }
        if (!minDistanceOK && (previewing || outType!=OUTTYPE_MAP)) {
            minDistanceOK = true;
            doHistogram = true;
            pointOKlist = makePointOKlist(pointList, minDistance);
        }
        if (previewing && doHistogram) {
            if (histogram == null)
                histogram = new int[101];
            else
                for (int i=0; i<histogram.length; i++)
                    histogram[i] = 0;
            for (int i=0; i<pointList[2].length; i++) if (pointOKlist[i]) {
                int bin = (int)(0.99999+100*pointList[2][i]);
                if (bin < histogram.length) histogram[bin]++;
            }
            histogramPlot.setHistogram(histogram);
            if (!refineButton.isEnabled()) refineButton.setEnabled(true);
        }

        if ((previewing || outType == OUTTYPE_POINTS) && !roiSaved) {
            imp.saveRoi(); // save previous selection so the user can restore it
            roiSaved = true;
        }
        if (!previewing && outType==OUTTYPE_MAP) {
            deviationMap.setMinAndMax(0,1);
            if (!Prefs.blackBackground) deviationMap.invertLut();
            ImagePlus outImp = new ImagePlus(WindowManager.makeUniqueName("Deviation Map of "+imp.getTitle()), deviationMap);
            calibrateAndShow(outImp);
            return;
        }
        float[] devPixels = (float[])deviationMap.getPixels();
        double tolerance = this.tolerance;  //a local copy that does not change asynchronously
        int nPoints = 0;            //count matches better than tolerance
        for (int i=0; i<pointList[2].length; i++) if (pointOKlist[i]) {
            if (pointList[2][i]<(0.01*tolerance+1e-6))
                nPoints++;
        }
        if (previewing) {
            messageArea.setText(nPoints+" Features");
            histogramPlot.setThreshold(tolerance+1e-9);
            histogramPlot.repaint();
        }
        if (previewing || outType==OUTTYPE_POINTS) {
            int[] xpoints = new int[nPoints];
            int[] ypoints = new int[nPoints];
            for (int i=0, n=0; i<pointList[0].length; i++) if (pointOKlist[i]) {
                if (pointList[2][i]<(0.01*tolerance+1e-6)) {
                    xpoints[n] = (int)Math.round(pointList[0][i]);
                    ypoints[n] = (int)Math.round(pointList[1][i]);
                    n++;
                }
            }
            imp.setRoi(new PointRoi(xpoints, ypoints, nPoints));
            return;
        }
        if (roiSaved)
            imp.restoreRoi();
        if (outType==OUTTYPE_COUNT) {
            ResultsTable rt = ResultsTable.getResultsTable();
            rt.incrementCounter();
            String label = imp.getTitle();
            if (imp.getStackSize() > 1) label += " ("+imp.getCurrentSlice()+")";
            rt.addLabel(label);
            rt.setValue("Count", rt.getCounter()-1, nPoints);
            rt.show("Results");
        } else if (outType==OUTTYPE_LIST || outType==OUTTYPE_LIST_CAL) {
            Analyzer.resetCounter();
            ResultsTable rt = ResultsTable.getResultsTable();
            Calibration cal = imp.getCalibration();
            if (cal.pixelWidth == 1 && cal.pixelHeight == 1)
				outType = OUTTYPE_LIST;
            for (int i=0, n=0; i<pointList[2].length; i++) if (pointOKlist[i]) {
                if (pointList[2][i]<(0.01*tolerance+1e-6)) {
                    rt.incrementCounter();
                    float x = pointList[0][i];
                    float y = pointList[1][i];
                    if (outType==OUTTYPE_LIST_CAL) {
                        x = (float)cal.getX(x);
                        y = (float)cal.getY(y, height);
                    }
                    rt.addValue("X", x);
                    rt.addValue("Y", y);
                }
            }
            rt.show("Results");
        } else if (outType==OUTTYPE_POINT_IMAGE) {
            ByteProcessor outIp = new ByteProcessor(width, height);
            byte[] outPixels = (byte[])outIp.getPixels();
            for (int i=0, n=0; i<pointList[2].length; i++) if (pointOKlist[i]) {
                if (pointList[2][i]<(0.01*tolerance+1e-6))
                    outPixels[(int)Math.round(pointList[0][i]) +
                            (int)Math.round(pointList[1][i])*width] = -1;
            }
            if (!Prefs.blackBackground) outIp.invertLut();
            ImagePlus outImp = new ImagePlus(WindowManager.makeUniqueName("Features in "+imp.getTitle()), outIp);
            calibrateAndShow(outImp);
        } else if (outType==OUTTYPE_AVERAGE) {
            int border = 20;
            FloatProcessor outIp = makeAverage(ip, pointList, pointOKlist, tolerance,
                    roi, xOffset, yOffset, border);
            if (outIp==null) {
                IJ.error("No features with border "+border+" pixels\nfully inside the image");
                return;
            }
            outIp.resetMinAndMax();
            outIp.setColorModel(ip.getColorModel());
            ImagePlus outImp = new ImagePlus(
                    WindowManager.makeUniqueName("Feature Avg of "+imp.getTitle()),
                    outIp);
            Roi outRoi = (Roi)roi.clone();
            outRoi.setLocation(border, border);
            outImp.setRoi(outRoi);
            calibrateAndShow(outImp);
        }

    } //public void run

    /** Transfers spatial calibration to output image and displays it */
    private void calibrateAndShow(ImagePlus outImp) {
            Calibration cal = imp.getCalibration().copy();
            cal.disableDensityCalibration();
            outImp.setCalibration(cal);
            outImp.show();
    }

    /** Creates a list of nozero pixels in maxIp, where corresponding pixels in
     *  deviationMap are <= maxValue. The list contains 3 arrays with x, y, value.
     *  x and y have subpixel accuracy if a 3x3 neighborhood has values below
     *  maxForInterpolation; then the value is interpolated using a square polynomial
     *
     *  Note that maxIp is modified!
     */
    private float[][] makeList(ByteProcessor maxIp, FloatProcessor deviationMap, float maxValue) {
        int width = maxIp.getWidth();
        int height = maxIp.getHeight();
        byte[] bPixels = (byte[])maxIp.getPixels();
        float[] fPixels = (float[])deviationMap.getPixels();
        int n=0;
        for (int y=1; y<height-1; y++)
            for (int x=1, p=y*width+x; x<width-1; x++, p++)
                if (bPixels[p] != 0) {
                    if (fPixels[p] <= maxValue)
                        n++;            //count maxima
                    else
                        bPixels[p] = 0; //reset maxima that don't qualify
                }
        float [][] list = new float[3][n];
        n=0;
        // Interpolate log(deviation map+constant) in a 3x3 neighborhood with a
        // 2nd-order polynomial in x, y for all points that we have not eliminated.
        // The constant is a compromise - high values get better interpolation, but
        // more false hits; lower values tend to suppress interpolation
        // Offsets to surrounding pixels are
        //   dx = {-1, 0, 1, -1, 0, 1, -1, 0, 1}
        //   dy = {-1, -1, -1, 0, 0, 0, 1, 1, 1}
        // Polynomial is
        //   a00 + a01*dx + a10*dy + a02*dx^2 + a11*dx*dy  + a20*dy^2
        final float addConst = 3f;
        for (int y=1; y<height-1; y++)
            for (int x=1; x<width-1; x++) {
                int p = x + y*width;
                if (bPixels[p] != 0) {
                    int xInt = x, yInt = y;
                    float xList = x, yList = y;
                    float value = (float)Math.log(fPixels[p] + addConst);
                    boolean tryNeighbor;
                    //try to find minimum of log(deviation) map with subpixel accuracy
                    do {
                        float v0 = (float)Math.log(fPixels[p-width-1] + addConst);
                        float v1 = (float)Math.log(fPixels[p-width] + addConst);
                        float v2 = (float)Math.log(fPixels[p-width+1] + addConst);
                        float v3 = (float)Math.log(fPixels[p-1] + addConst);
                        float v4 = (float)Math.log(fPixels[p] + addConst);
                        float v5 = (float)Math.log(fPixels[p+1] + addConst);
                        float v6 = (float)Math.log(fPixels[p+width-1] + addConst);
                        float v7 = (float)Math.log(fPixels[p+width] + addConst);
                        float v8 = (float)Math.log(fPixels[p+width+1] + addConst);
                        /* The following is a polynomial fit without weights
                        float a00= (1f/9f)*(5*v4 + 2*(v1 + v3 + v5 + v7) - (v0 + v2 + v6 + v8));
                        float a01= (1f/6f)*(v2-v0 + v5-v3  + v8-v6);
                        float a10= (1f/6f)*(v6-v0 + v7-v1  + v8-v2);
                        float a02= (1f/6f)*(v0 + v2 + v3 + v5 + v6 + v8 - 2*(v1 + v4 + v7));
                        float a20= (1f/6f)*(v0 + v1 + v2 + v6 + v7 + v8 - 2*(v3 + v4 + v5));
                        float a11= (1f/4f)*(v0- v2 - v6 + v8);
                        */
                        // We use weights, 1 for the central pixel, 1/2 for its 4-connected
                        //neighbors, 1/4 for its remaining 8-connected neighbors
                        float a00= (1f/36f)*(32*v4 + 2*(v1 + v3 + v5 + v7) - (v0 + v2 + v6 + v8));
                        float a01= (1f/12f)*(v2-v0 + 4*(v5-v3)  + v8-v6);
                        float a10= (1f/12f)*(v6-v0 + 4*(v7-v1)  + v8-v2);
                        float a02= (1f/12f)*(v0 + v2 + v6 + v8 + 4*(v3+v5) - 2*(v1+v7) - 8*v4);
                        float a20= (1f/12f)*(v0 + v2 + v6 + v8 + 4*(v1+v7) - 2*(v3+v5) - 8*v4);
                        float a11= (1f/4f) *(v0 - v2 - v6 + v8);
                        float denominator = 4*a02*a20 - a11*a11;
                        //if (value<1.5) IJ.log("denom="+denominator+" a00,a01,a10="+a00+","+a01+","+a10);
                        //if (value<1.5) IJ.log("a02,a11,a20="+a02+","+a11+","+a20);
                        // continue only if all curvatures are positive (i.e., a minimum)
                        if (a02<=0 || a20<=0 || denominator<1e-6) break;
                        float dx = (a10*a11 - 2*a01*a20) / denominator;
                        float dy = (a01*a11 - 2*a10*a02) / denominator;
                        float deltaAbs = Math.max(Math.abs(dx), Math.abs(dy));
                        //if (value<1.5) IJ.log("dx,dy="+dx+","+dy);
                        int newXint = 0, newYint = 0;
                        tryNeighbor = (deltaAbs > 0.55); //minimum well outside pixel area,
                        if (tryNeighbor) {               // then we move to a neighboring pixel
                            newXint = xInt + Math.round( (deltaAbs>1) ? dx/deltaAbs : dx);
                            newYint = yInt + Math.round( (deltaAbs>1) ? dy/deltaAbs : dy);
                            //IJ.log("x,y="+x+","+y+" v="+value+" dx,dy="+dx+","+dy+" move to:"+newXint+","+newYint);
                            if (newXint<1 || newXint>=width-1 || newYint<1 || newYint>=height-1) {
                                value = Float.MAX_VALUE;
                                break;              // edge minimum reached, ignore it
                            }
                            dx *= 0.5f/deltaAbs;    // before moving, consider point at pxl boundary
                            dy *= 0.5f/deltaAbs;
                        }
                        float newValue = a00 + dx*(a01 + dx*a02 +dy*a11) + dy*(a10 + dy*a20);
                        //if (value<1.5) IJ.log("dx,dy="+dx+","+dy+" old,newValue="+value+","+newValue);
                        //if (value<1.5) IJ.log("lin="+(a00 + dx*a01 + dy*a10));
                        if (newValue >= value)      // subpixel attempt did not improve it?
                            break;
                        xList = xInt + dx;          // otherwise remember the better minimum
                        yList = yInt + dy;
                        value = newValue;
                        if (tryNeighbor) {
                            xInt = newXint;
                            yInt = newYint;
                            p = xInt +yInt*width;
                        }
                    } while (tryNeighbor);
                    float v = (float)Math.exp(value) - addConst;
                    //if (value<1.5) IJ.log("x,y="+x+","+y+" list x,y,v="+xList+","+yList+","+v);
                    if (v < 0) v = 0;
                    list[0][n] = xList;
                    list[1][n] = yList;
                    list[2][n] = v;
                    n++;
                }
            }
        return list;
    }

    /** Returns a list where all points of pointList dominating within minDistance
      * are marked as true.  */
    private boolean[] makePointOKlist (float[][] pointList, double minDistance) {
        float[] xList = pointList[0], yList = pointList[1];
        if (xList.length==0) return new boolean[0];
        boolean[] pointOK = new boolean[yList.length];
        // the list is roughly sorted by y; determine how much it deviates
        float yRegression = 0, maxY = yList[0];
        for (int i=1; i<yList.length; i++) {
            if (yList[i] > maxY)
                maxY = yList[i];
            else if (maxY - yList[i] > yRegression)
                yRegression = maxY - yList[i];
        }
        float minDist2 = (float)(minDistance*minDistance);
        float dyRange = (float)minDistance + yRegression;
        int firstJ = 0;
        for (int i=0; i<pointOK.length; i++) {
            pointOK[i] = true;
            for (int j=firstJ; j<yList.length && yList[j]-yList[i]<=dyRange; j++) {
                if (i==j) continue;
                if (yList[j]-yList[i] < -dyRange)
                    firstJ = j;     //too low in y, we need not search here any more
                else {
                    float dx = xList[j] - xList[i];
                    float dy = yList[j] - yList[i];
                    if (dx*dx + dy*dy < minDist2 &&
                            (pointList[2][i]>pointList[2][j] || //equal ones: eliminate one
                            (pointList[2][i]==pointList[2][j] && pointOK[j])))
                        pointOK[i] = false;    // dominated by a better minimum
                }
            }
        }

        return pointOK;
    }

    /** Create an average of the features within tolerance.
      * The image created has the size of the roi plus the border.
      * Features are used only if the feature + border is fully inside
      * the original image. Returns null if there are no such features. */
    private FloatProcessor makeAverage (ImageProcessor ip, float[][] pointList, boolean[] pointOKlist,
            double tolerance, Roi roi, int xOffset, int yOffset, int border) {
        int width = ip.getWidth();
        int height = ip.getHeight();
        Rectangle roiRect = roi.getBounds();
        int rWidth = roiRect.width;
        int rHeight = roiRect.height;
        int newWidth = rWidth+2*border;
        int newHeight = rHeight+2*border;
        int newXoffset = xOffset + border;
        int newYoffset = yOffset + border;
        FloatProcessor avgIp = new FloatProcessor(newWidth, newHeight);
        float[] avgPixels = (float[])avgIp.getPixels();
        int n=0;
        for (int i=0; i<pointList[2].length; i++) if (pointOKlist[i]) {
            if (pointList[2][i]<(0.01*tolerance+1e-6) &&
                    pointList[0][i]-newXoffset>=0 && pointList[0][i]-newXoffset+newWidth<=width-1 &&
                    pointList[1][i]-newYoffset>=0 && pointList[1][i]-newYoffset+newHeight<=height-1) {
                double y = pointList[1][i] - newYoffset;
                for (int yn=0; yn<newHeight; yn++, y++) {
                    double x = pointList[0][i] - newXoffset;
                    for (int xn=0, pn=xn+yn*newWidth; xn<newWidth; xn++, pn++, x++)
                        avgPixels[pn] += (float)ip.getInterpolatedPixel(x, y);
                }
                n++;
            }
        }
        if (n==0) return null;
        for (int i=0; i<avgPixels.length; i++)
            avgPixels[i] *= (1f/n);
        return avgIp;
    }

    private void invertSign (FloatProcessor fp) {
        int width = fp.getWidth();
        int height = fp.getHeight();
        float[] fPixels = (float[])fp.getPixels();
        for (int i=0; i<width*height; i++)
            fPixels[i] = -fPixels[i];
    }

     /** Returns the list of <code>ImagePlus</code>es suitable as prototype for the current imp
      *  Suitable images are:
      *  - The current one if it has a selection
      *  - Other grayscale (non-RGB) images that have a selection or as a whole image
      *     if they do not exceed the width or height of the current image.
      */
    ImagePlus[] getPrototypeImages(ImagePlus imp) {
        int width = imp.getWidth();
        int height = imp.getHeight();
        int nImages = WindowManager.getImageCount();
        Vector protoVec = new Vector();
        if (imp.getRoi()!=null && imp.getRoi().isArea()) protoVec.add(imp);    //put the current image first
        for (int i=1; i<=nImages; i++) {                //other suitable images?
            ImagePlus imp2 = WindowManager.getImage(i);
            if (imp2==null) continue; //does not happen except in case of asynchronous deletion
            if (imp2==imp) continue;
            if (imp2.getType() == ImagePlus.COLOR_RGB) continue;
            if ((imp2.getRoi()==null || !imp2.getRoi().isArea()) &&
                    (imp2.getWidth()>width || imp2.getHeight()>height))
                continue;
            protoVec.add(imp2);
        }
        if (protoVec.isEmpty()) return null;
        else return (ImagePlus[])protoVec.toArray(new ImagePlus[0]);
    }

    /** The kernel, i.e., the pattern we are searching for */
    private class Kernel {
        boolean subtractBackground;
        boolean softEdges;
        int kWidth, kHeight;                //size of kernel (pixels)
        FloatProcessor kernelIp, weightIp;  //kernel data and weights (if softEdges)
        float[] kernelData, weightData;
        double sumWeight;                   //sum of all weights (if softEdges)
        byte[] maskArray;                   //mask for non-rectangular rois, null if rectangular roi
        int xOffset, yOffset;               //kernel center (w.r.t kernel coordinates x=0, y=0)
        double variance;                    //of all pixel in the kernel
        boolean calcInterrupted;            //calculating deviation map was interrupted
        int lastY;                          //multithreading: the highest y that is handled already

        /** create kernel from the roi (or all) of an ImageProcessor */
        Kernel (ImageProcessor ip, Roi roi, boolean subtractBackground, boolean softEdges) {
            this.subtractBackground = subtractBackground;
            this.softEdges = softEdges;
            int ipWidth = ip.getWidth();
            int ipHeight = ip.getHeight();
            float[] ipData = (float[])ip.getPixels();
            Rectangle roiRect = (roi == null) ? new Rectangle(ipWidth, ipHeight) : roi.getBounds();
            kWidth = roiRect.width;
            kHeight = roiRect.height;
            if (roiRect.x<0 || roiRect.y<0 || roiRect.x+kWidth>ipWidth || roiRect.y+kHeight>ipHeight)
                throw new RuntimeException("Error: Selection reaches out of image");
            ImageProcessor mask = (roi == null) ? null : roi.getMask();
            maskArray = (mask==null) ? null : (byte[])mask.getPixels();
            kernelIp = new FloatProcessor(kWidth, kHeight);
            kernelData = (float[])kernelIp.getPixels();
            //get center and check for minimum roi size
            int roiSize = 0;
            double xCenter = 0., yCenter = 0.; //center of kernel w.r.t. kernel coordinates x=0,y=0
            for (int y=0,i=0; y<kHeight; y++)
                for (int x=0; x<kWidth; x++,i++)
                    if (maskArray==null || maskArray[i]!=0) {
                    xCenter += x;
                    yCenter += y;
                    roiSize++;
                    }
            xCenter /= roiSize;
            yCenter /= roiSize;
            xOffset = (int)Math.round(xCenter);
            yOffset = (int)Math.round(yCenter);
            if (roiSize < 2) throw new RuntimeException("Error: Selection must be at least 2 pixels");
            //xCenter /= roiSize;
            //yCenter /= roiSize;
            //get data
            for (int y=0,i=0; y<kHeight; y++)
                for (int x=0,p=(y+roiRect.y)*ipWidth+roiRect.x; x<kWidth; x++,i++,p++)
                    kernelData[i] = ipData[p];
            //weight function for soft edges
            if (softEdges) {
                ImageProcessor maskIp = ip.getMask();
                if (maskIp == null) {
                    maskIp = new ByteProcessor(kWidth, kHeight);
                    maskIp.setValue(255.);
                    maskIp.fill();
                }
                weightIp = new EDM().makeFloatEDM (maskIp, 0, true);
                weightData = (float[])weightIp.getPixels();
                double sum = 0.;
                int count = 0;
                for (int i=0; i<kWidth*kHeight; i++) {
                    sum += weightData[i]; count++;
                }
                float average = (float)(sum/count);
                for (int i=0; i<kWidth*kHeight; i++) {
                    float normalized = weightData[i]/average;
                    weightData[i] = normalized>1 ? 1 : (float)(0.5-0.5*Math.cos(normalized*Math.PI));
                }
            //new ImagePlus("weights", weightIp).show();
            }
            //get variance
            double sum = 0.;
            double sum2 = 0.;
            sumWeight = 0.;
            for (int i=0; i<kWidth*kHeight; i++)
                if (maskArray==null || maskArray[i]!=0) {
                    if (softEdges) {
                        sum +=   weightData[i] * kernelData[i];
                        sum2 +=  weightData[i] * kernelData[i]*kernelData[i];
                        sumWeight += weightData[i];
                    } else {
                        sum +=  kernelData[i];
                        sum2 += kernelData[i]*kernelData[i];
                        sumWeight ++;
                    }
                }
            variance = (sum2 - sum*sum/sumWeight)/sumWeight;
            //IJ.log("sums="+(float)sum+","+(float)sum2+"variance="+(float)variance);
            //IJ.log("sumWeight="+(float)sumWeight+" offset:"+xOffset+","+yOffset);
            if (variance==0 || variance/sum2<1e-10)
                throw new RuntimeException("Error: no features in ROI");
            if (subtractBackground) {
                float mean = (float)(sum/sumWeight);
                for (int i=0; i<kWidth*kHeight; i++)
                    kernelData[i] -= mean;
            }
        } //Kernel (creator)

        /** Returns a map of the square deviation between image (FloatProcessor) and kernel */
        FloatProcessor deviationMap (final ImageProcessor ip) {
            int width = ip.getWidth();
            int height = ip.getHeight();
            FloatProcessor outIp = new FloatProcessor(width, height);
            final float[] outData = (float[]) outIp.getPixels();
            lastY = 0;
            final int nThreads = Math.min(Prefs.getThreads(), height);
            final Thread[] threads = new Thread[nThreads-1];    //thread number 0 is this one, not in the array
            for (int t=1; t<nThreads; t++) {
                final int yStart = t;//(height*t)/nThreads;
                final Thread thread = new Thread(
                    new Runnable() {
                        final public void run() {
                            makeDeviationMapThread(ip, outData);
                        }
                    } ,
                    "Feature_Finder-"+t);
                thread.setPriority(Thread.currentThread().getPriority());
                thread.start();
                threads[t-1] = thread;
            }
            makeDeviationMapThread(ip, outData);//, 0, progressArray);
            for (final Thread thread : threads)
                try {
                    thread.join();
                } catch (InterruptedException e) {
                    calcInterrupted = true;
                }
            if (calcInterrupted) {
                for (final Thread thread : threads)
                    thread.interrupt();
                for (final Thread thread : threads) try {
                    thread.join();
                } catch (InterruptedException e) {}
                Thread.currentThread().interrupt();      //keep interrupted status (PlugInFilterRunner needs it)
                outIp = null;
                calcInterrupted = false;
            }
            return outIp;
        } //FloatProcessor deviationMap

        /** Make part of the deviation map in a thread.
         *  All threads work on nearby lines to optimize CPU cache utilization.
         *  In rare cases, one line may be processed by two threads. This is faster
         *  than the overhead of a 'synchronized' section for each line. */
        void makeDeviationMapThread(ImageProcessor ip, float[] outData) {
            final int width = ip.getWidth();
            final int height = ip.getHeight();
            final float[] pixels = (float[])ip.getPixels();
            final int pOffset = -yOffset*width-xOffset; //point offset in ip for (0,0) of kernel

            for (int y=lastY; y<height; y=lastY) {
                lastY = y + 1;
                if (y%10==0) {
                    if ((Thread.currentThread().isInterrupted()) || IJ.escapePressed()) {
                        calcInterrupted=true;
                        return;
                    }
                    IJ.showProgress(y/(double)height);
                }
                int p = y*width;
                boolean yInside = (y>=yOffset) && (y<height-kHeight+yOffset);
                for (int x=0; x<width; x++,p++) {
                    boolean xInside = (x>=xOffset) && (x<width-kWidth+xOffset);
                    //get difference squared between image data and prototype (kernel).
                    if (xInside && yInside) {
                        //if (y==5) IJ.log("x,y="+x+","+y+" inside="+xInside+yInside+"offs0="+(p+pOffset));
                        double sumX = 0, sumDiff = 0, sumDiff2 = 0;
                        for (int kPtr=0, iPtr=p+pOffset; kPtr<kWidth*kHeight; iPtr+=width-kWidth)
                            for (int x2=0; x2<kWidth; x2++,kPtr++,iPtr++)
                                if (maskArray==null || maskArray[kPtr]!=0) {
                                    double diff = pixels[iPtr]-kernelData[kPtr];
                                    if (softEdges) {
                                        sumDiff2 += weightData[kPtr] * diff*diff;
                                        if (subtractBackground) {
                                            sumX += weightData[kPtr] * pixels[iPtr];
                                            sumDiff += weightData[kPtr] * diff;
                                        }
                                    } else {
                                        sumDiff2 += diff*diff;
                                        if (subtractBackground) {
                                            sumX += pixels[iPtr];
                                            sumDiff += diff;
                                        }
                                    }
                                }
                        // With background, we have to subtract the mean of the data xmean:
                        // sum (x-xmean-k)^2 = sum (x-k)^2 - 2*sum (x-k)*xmean + sum xmean^2
                        // where x = pixel data, k = kernel (prototype) data
                        // note that xmean is constant, xmean = sumX/sumWeight
                        if (subtractBackground) {
                            sumDiff2 += (-2*sumDiff*sumX + sumX*sumX)*(1./sumWeight);
                        }
                        outData[p] = (float)(sumDiff2*(1./variance/sumWeight));
                    } else { //near-border pixels
                        double sumX = 0, sumK = 0, sumW = 0, sumDiff = 0, sumDiff2 = 0;
                        int x2min = (x>=xOffset) ? 0 : xOffset - x;
                        int x2end = (x<width-kWidth+xOffset) ? kWidth : width - x + xOffset;
                        int y2min = (y>=yOffset) ? 0 : yOffset - y;
                        int y2end = (y<height-kHeight+yOffset) ? kHeight : height - y + yOffset;
                        for (int y2=y2min; y2<y2end; y2++) {
                            int kPtr = y2*kWidth + x2min;
                            int iPtr = (y-yOffset+y2) * width + (x-xOffset+x2min);
                            for (int x2=x2min; x2<x2end; x2++,kPtr++,iPtr++)
                                if (maskArray==null || maskArray[kPtr]!=0) {
                                    double diff = pixels[iPtr]-kernelData[kPtr];
                                    if (softEdges) {
                                        sumW += weightData[kPtr];
                                        sumDiff2 += weightData[kPtr] * diff*diff;
                                        if (subtractBackground) {
                                            sumX += weightData[kPtr] * pixels[iPtr];
                                            sumDiff += weightData[kPtr] * diff;
                                        }
                                    } else {
                                        sumW ++;
                                        sumDiff2 += diff*diff;
                                        if (subtractBackground) {
                                            sumX += pixels[iPtr];
                                            sumDiff += diff;
                                        }
                                    }
                                }
                        }
                        // With background, we have to subtract the mean of the data xmean,
                        // but also the mean of the kernel kmean (it is not zero if only part
                        // ot the kernel is used
                        // sum (x-xmean-(k-kmean))^2 =
                        // sum (x-k + kmean-xmean)^2 =
                        // sum (x-k)^2 + sum xmean^2 + sum kmean^2 -
                        //   + 2*sum (x-k)*(kmean-xmean) - 2 * sum kmean*xmean
                        // note that xmean is constant, sumX/sumW (sum of weights or # of points)
                        if (subtractBackground) {
                            sumDiff2 +=
                                    (sumX*sumX + sumK*sumK + 2*sumDiff*(sumK-sumX) - 2*sumK*sumX )
                                    *(1./sumW);
                        }
                        outData[p] = (float)(sumDiff2*(1./variance/sumW));
                        //if (x==0&&y==0) IJ.log("x,y="+x+","+y+" sumW="+sumW+" sumDiff2="+sumDiff2+" p="+p);
                    } //else near-border pixels
                } //for x
            } //for y
        }

        int getXoffset() { return xOffset; }

        int getYoffset() { return yOffset; }

    } //class Kernel
}

class HistogramPlot extends Canvas {
    static final int WIDTH = 202, HEIGHT=48;
    int[] histogram;
    int maxValue;
    double threshold;

    HistogramPlot() {
        setSize(WIDTH+2, HEIGHT+2);
    }

    void setHistogram (int[] histogram) {
        this.histogram = histogram;
        maxValue = 1;
        for (int i=0; i<histogram.length; i++)
            if (maxValue< histogram[i]) {
                if (i>0.8*histogram.length && histogram[i]>HEIGHT)
                    maxValue = HEIGHT;  //allow for some clipping at high tolerance values
                else
                    maxValue = histogram[i];
            }
    }

    void setThreshold (double threshold) {
        this.threshold = threshold;
    }

    public void update(Graphics g) {
        paint(g);
    }

    public void paint(Graphics g) {
        if (g==null || histogram==null) return;
        g.setColor(Color.white);
        g.fillRect(0, 0, WIDTH, HEIGHT);
        g.setColor(Color.black);
        g.drawRect(0, 0, WIDTH, HEIGHT);
        g.setColor(Color.red);
        for (int i=0; i<histogram.length; i++) {
            if (i>threshold) g.setColor(Color.black);
            if (histogram[i] > 0) {
                int barLength = ((HEIGHT-2)*histogram[i]+(maxValue-1))/maxValue;
                g.fillRect(2*i+1, HEIGHT-barLength, 2, barLength);
            }
        }


    }

    public Dimension getPreferredSize() {
        return new Dimension(WIDTH+1, HEIGHT+1);
    }

}
