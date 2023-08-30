import ij.plugin.filter.*;
import ij.*;
import ij.process.*;
import ij.macro.*;
import ij.measure.CurveFitter;
import ij.measure.Calibration;
import ij.gui.*;
import ij.io.*;
import java.awt.*;

/**
This plugin fits the slice-dependent data for each (x,y) pixel of a stack and creates a new stack with the fit parameters.
Input data are calibrated pixel values.

TODO: checking for macro error in DialogItemChanged

M. Schmid 2016-11-29
*/

public class Stack_Fitter implements ExtendedPlugInFilter, DialogListener {
    ImagePlus       imp;                    // the input image
    // Dialog Parameters
    static int      fitTypeI;               // remembers the fit type, sorted index, actual type is CurveFitter.sortedTypes[fitTypeI]
    static boolean  previousAsStartParams;  // use previous result as starting params
    static String   outputChannels = "";
    //
    private static int FLAGS = STACK_REQUIRED|DOES_ALL|NO_CHANGES;
    private static int MAX_FIT_PARAMS = 8;

    public int setup(String arg, ImagePlus imp) {
        if (IJ.versionLessThan("1.51i")) return DONE;
        this.imp = imp;
        return FLAGS;
    }

    public int showDialog(ImagePlus imp, String command, PlugInFilterRunner pfr) {
        String[] fitFunctions = new String[CurveFitter.fitList.length];
        for (int i=0; i<fitFunctions.length; i++)
            fitFunctions[i] = CurveFitter.fitList[CurveFitter.sortedTypes[i]];
        GenericDialog gd = new GenericDialog("Stack Fitter...");
        gd.addChoice("Fit function for z profiles:", fitFunctions, fitFunctions[fitTypeI]);
        gd.addCheckbox("Use previous pixel for initial fit params", previousAsStartParams);
        gd.addStringField("Output channels*", outputChannels, 30);
        gd.addMessage("* Leave blank for all fit params. Otherwise:\n"+
                "  Comma separated list. Variables are fit params a,b,...;\n"+
                "  R2 (R squared), D2 (sum of squared residuals)\n"+
                "  Variable 'v' (if used) is output pixel value.\n"+
                "  E.g. 'a, -b/(2*c), R2' or 'if (a>0) v=sqrt(a); else v=-sqrt(-a);, b'");
        gd.addDialogListener(this);
        gd.showDialog();                            // user input (or reading from macro) happens here
        if (gd.wasCanceled())                       // dialog cancelled?
            return DONE;
		return FLAGS;
    }

    public boolean dialogItemChanged(GenericDialog gd, AWTEvent e) {
        fitTypeI = gd.getNextChoiceIndex();
        int fitType = CurveFitter.sortedTypes[fitTypeI];
        previousAsStartParams = gd.getNextBoolean();
        outputChannels = gd.getNextString();
        // consistency checking
        int nFitParams = CurveFitter.getNumParams(fitType);
        outputChannels = outputChannels.trim();
        if (outputChannels.length() > 0) {
            String[] channelStrings = outputChannels.split(",");
            for (int i=0; i<channelStrings.length; i++) {
                Program pgm = (new Tokenizer()).tokenize(channelStrings[i]);
                for (int j=nFitParams; j<=MAX_FIT_PARAMS; j++) {
                    if (pgm.hasWord(Character.toString((char)('a'+j)))) {
                        IJ.showStatus("Undefined parameter '"+(char)('a'+j)+"'");
                        return false;
                    }
                }
            }
        }
        IJ.showStatus("");
        return true;
    }

    /** Prepares and runs the fits */
    public void run(ImageProcessor ip) {
        int fitType = CurveFitter.sortedTypes[fitTypeI];
        int nFitParams = CurveFitter.getNumParams(fitType);

        // Prepare user-defined output channels
        int nOutChannels = nFitParams;
        outputChannels = outputChannels.trim();
        String[] channelStrings = null;
        Interpreter[] macro = null;
        int macroStartProgramCounter = 27; //counting tokens till after 'function dummy'
        if (outputChannels.length() > 0) {
            channelStrings = outputChannels.split(",");
            nOutChannels = channelStrings.length;
            macro = new Interpreter[nOutChannels];
            for (int i=0; i<channelStrings.length; i++) {
                Program pgm = (new Tokenizer()).tokenize(channelStrings[i]);
                if (!pgm.hasWord("v"))
                    channelStrings[i] = "v="+channelStrings[i];
                String code = "var a,b,c,d,e,f,g,h, R2, D2;\nfunction dummy() {}\n";
                code += channelStrings[i]+";\n";
                macro[i] = new Interpreter();
                try {                               // check for invalid macro code
                    macro[i].run(code, null);
                } catch (Exception e) {
                    if (!Macro.MACRO_CANCELED.equals(e.getMessage()))
                        IJ.handleException(e);
                }
                if (macro[i].wasError()) return;
            }
        }

        // Make data accessible
        int width = imp.getWidth();
        int height = imp.getHeight();
        ImageStack stack = imp.getStack();
        int nSlices = stack.getSize();
        ImageProcessor[] inIps = new ImageProcessor[nSlices];
        for (int i=0; i<nSlices; i++)
            inIps[i] = stack.getProcessor(i+1);
        Calibration cal = imp.getCalibration();
        double[] zData = new double[nSlices];
        for (int i=0; i<nSlices; i++)
            zData[i] = cal.getZ(i);
        
        ImageProcessor[] outIPs = new ImageProcessor[nOutChannels];
        ImageStack outStack = new ImageStack(width, height);
        for (int i=0; i<nOutChannels; i++) {
            String label = macro == null ? Character.toString((char)('a'+i))
                    : channelStrings[i];
            outIPs[i] = new FloatProcessor(width, height);
            outStack.addSlice(label, outIPs[i]);
        }

        // Fitting
        double[] fitData = new double[nSlices];
        for (int y=0; y<height; y++) {
            IJ.showProgress((double)y/height);
            for (int x=0; x<width; x++) {
                double[] params = null;
                for (int i=0; i<nSlices; i++)
                    fitData[i] = inIps[i].getPixelValue(x, y);
                CurveFitter cf = new CurveFitter(zData, fitData);
                if (fitType == CurveFitter.POLY2 || fitType == CurveFitter.EXPONENTIAL
                        || fitType == CurveFitter.POWER || fitType == CurveFitter.LOG)
                    cf.setRestarts(0);              // for one-parameter fits (not counting regression params): only one try
                if (params != null && previousAsStartParams)
                    cf.setInitialParameters(params);
                cf.doFit(fitType, false);
                params = cf.getParams();
                
                for (int i=0; i<nOutChannels; i++) {
                    double outPixelValue = 0;
                    if (macro==null) {
                        outPixelValue = params[i];
                    } else {
                        try {
                            for (int j=0; j<nFitParams; j++)
                                macro[i].setVariable(Character.toString((char)('a'+j)), params[j]);
                            macro[i].setVariable("R2", cf.getRSquared());
                            macro[i].setVariable("D2", cf.getSumResidualsSqr());
                            macro[i].run(macroStartProgramCounter);
                            outPixelValue = macro[i].getVariable("v");
                        } catch (Exception e) {
                            IJ.handleException(e);
                            return; //avoids leaving a locked input image
                        }
                    }
                    outIPs[i].putPixelValue(x, y, outPixelValue);
                }
            }
        }
        IJ.showProgress(1.0);
        
        // Output
        String title = WindowManager.getUniqueName(imp.getTitle()+"-fit");
        ImagePlus outImp = new ImagePlus(title, outStack);
        outImp.setCalibration(cal);
        Calibration outCal = outImp.getCalibration();
        outCal.disableDensityCalibration();         // keep spacial calibration only
        outCal.zOrigin = 0;
        outCal.pixelDepth = 1.0;
        outCal.setZUnit(null);
        outImp.show();
    }

    /** Not needed because stacks are not handled slice by slice */
    public void setNPasses(int nPasses) {}
}
