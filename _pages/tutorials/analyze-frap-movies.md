---
mediawiki: Analyze_FRAP_movies_with_a_Jython_script
title: Analyze FRAP movies with a Jython script
---

Here is a [Jython](/scripting/jython) script that does the analysis of a FRAP movie. It was developed during the [Image Processing School Pilsen 2009](/events/image-processing-school-pilsen-2009), and updated to modern Fiji.

Once the user has loaded a good FRAP movie, [well aligned with no drift](/tutorials/correcting-drift-in-frap-experiments), and has specified the ROI for the FRAP zone and another for the control zone, it should be possible to automate the analysis of the FRAP curve. This is what this script aims to do:

-   Load a movie
-   Draw a ROI for the FRAP zone, and store it as the **first** ROI in the ROI manager (by pressing the {% include key key='T' %} key)
-   Do the same for a control zone, out of the FRAP zone

Then load this script in the [Script Editor](/scripting/script-editor), choose {% include bc path='Language | Python'%}, and run it. It will measure the FRAP intensity for all frames, try to find the FRAP frame (by finding the one with the minimal FRAP ROI intensity), and fit the FRAP curve by an increasing exponential. The parameters of the fit can be then read in the log window, and the FRAP curve and its fit are plotted. Careful:the background is taken as the intensity in the FRAP region just after the FRAP pulse.

This script uses only ImageJ functions for everything, but could be tuned to use more fancy Fiji-included plotting library, such as JFreeChart.

```java
import java.awt.Color as Color
from ij import WindowManager as WindowManager
from ij.plugin.frame import RoiManager as RoiManager
from ij.process import ImageStatistics as ImageStatistics
from ij.measure import Measurements as Measurements
from ij import IJ as IJ
from ij.measure import CurveFitter as CurveFitter
from ij.gui import Plot as Plot
from ij.gui import PlotWindow as PlotWindow
import math

# Get ROIs
roi_manager = RoiManager.getInstance()
roi_list    = roi_manager.getRoisAsArray()

# We assume first one is FRAP roi, the 2nd one is normalizing roi.
roi_FRAP    = roi_list[0];
roi_norm    = roi_list[1];

# Specify up to what frame to fit and plot.
n_slices = 30

# Get current image plus and image processor
current_imp  = WindowManager.getCurrentImage()
stack        = current_imp.getImageStack()
calibration  = current_imp.getCalibration()

#############################################

# Collect intensity values

# Create empty lists of number
If = []  # Frap values
In = []  # Norm values

# Loop over each slice of the stack
for i in range(0, n_slices):
 
    # Get the current slice 
    ip = stack.getProcessor(i+1)
 
    # Put the ROI on it
    ip.setRoi(roi_FRAP)
 
    # Make a measurement in it
    stats = ImageStatistics.getStatistics(ip, Measurements.MEAN, calibration);
    mean  = stats.mean
 
    # Store the measurement in the list
    If.append( mean  )

    # Do the same for non-FRAPed area
    ip.setRoi(roi_norm)
    stats = ImageStatistics.getStatistics(ip, Measurements.MEAN, calibration);
    mean = stats.mean
    In.append( mean  )
 
# Gather image parameters
frame_interval = calibration.frameInterval
time_units = calibration.getTimeUnit()
IJ.log('For image ' + current_imp.getTitle() )
IJ.log('Time interval is ' + str(frame_interval) + ' ' + time_units)
 
# Find minimal intensity value in FRAP and bleach frame
min_intensity = min( If )
bleach_frame = If.index( min_intensity )
IJ.log('FRAP frame is ' + str(bleach_frame+1) + ' at t = ' + str(bleach_frame * frame_interval) + ' ' + time_units )
 
# Compute mean pre-bleach intensity
mean_If = 0.0
mean_In = 0.0
for i in range(bleach_frame):         # will loop until the bleach time
    mean_If = mean_If + If[i]
    mean_In = mean_In + In[i]
mean_If = mean_If / bleach_frame
mean_In = mean_In / bleach_frame
 
# Calculate normalized curve
normalized_curve = []
for i in range(n_slices):
    normalized_curve.append( (If[i] - min_intensity) / (mean_If - min_intensity)   *   mean_In / In[i] )
    
x = [i * frame_interval for i in range( n_slices ) ] 
y = normalized_curve

xtofit = [ i * frame_interval for i in range( n_slices - bleach_frame ) ]
ytofit = normalized_curve[ bleach_frame : n_slices ]
 
# Fitter
fitter = CurveFitter(xtofit, ytofit)
fitter.doFit(CurveFitter.EXP_RECOVERY_NOOFFSET)
IJ.log("Fit FRAP curve by " + fitter.getFormula() )
param_values = fitter.getParams()
IJ.log( fitter.getResultString() )
 
# Overlay fit curve, with oversampling (for plot)
xfit = [ (t / 10.0  + bleach_frame) * frame_interval for t in range(10 * len(xtofit) ) ]
yfit = []
for xt in xfit:
    yfit.append( fitter.f( fitter.getParams(), xt - xfit[0]) )

 
plot = Plot("Normalized FRAP curve for " + current_imp.getTitle(), "Time ("+time_units+')', "NU", [], [])
plot.setLimits(0, max(x), 0, 1.2 );
plot.setLineWidth(2)


plot.setColor(Color.BLACK)
plot.addPoints(x, y, Plot.LINE)
plot.addPoints(x,y,PlotWindow.X);

 
plot.setColor(Color.RED)
plot.addPoints(xfit, yfit, Plot.LINE)

plot.setColor(Color.black);
plot_window =  plot.show()


# Output FRAP parameters
thalf = math.log(2) / param_values[1]
mobile_fraction = param_values[0]

str1 = ('Half-recovery time = %.2f ' + time_units) % thalf
IJ.log( str1 )
str2 = "Mobile fraction = %.1f %%" % (100 * mobile_fraction)
IJ.log( str2 )
```
