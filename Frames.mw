{{Infobox
| software               = ImageJ1
| name                   = Frames
| author                 = Fred Damen
| maintainer             = Fred Damen
| filename               = Frames.jar
| source                 = [https://imagej.net/_images/3/3d/Frames.zip Frames.zip]
| released               = 1 April 2019
| latest version         = 1 April 2020
| status                 = stable 
| category               = [[:Category:Analysis‏‎‏‎|Analysis‏‎‏‎]]
| website                = 
}}

These are a set of plugins that are used to work with data in the frame direction.  The F_Project plugin projects the images in the frame direction into a lower dimension using different methods. The F_Profiler pulgin plots the contents of an ROI through the frame direction.  The Frame_Slider provides sliders to step though the frames of a hyperstacks based on the variable/values in the slice labels.

== F_Project ==
[[File:F_Project_ScreenShot.jpg|400px]]

When run as a plugin from the gui the image used is identified on the top line.  A subset of the slices and frames can be used as the source data; see syntax for ''Make Substacks...''. When the identified frames is 'label', the frames are grouped by identical labels. When the frames are identified by 'repeats var', where var is the name of the variable in the slice label, these frames are treated as repeats of data.
<br>'''Transpose?''' Swap frames for slices.

The following summary methods as provided:
<br>'''Sum''' Arithmetic Sum
<br>'''Mean''' Arithmetic Mean (μ)
<br>'''StdDev''' Standard Deviation (σ) - computed using the slow method for numerical accuracy
<br>'''ZScore''' Z Score (μ/σ) - akin to Signal to Noise (SNR)
<br>'''CV''' Coefficient of Variation (σ/μ)
<br>'''Minimum''' Minimum
<br>'''Maximum''' Maximum
<br>'''Median''' Median
<br>'''Center''' Weighted arithmetic mean around the median - resilient to outliers
<br>'''Product''' Product (Π s<sub>i</sub><sup>-n</sup>)<sup>n</sup>
<br>'''GeoMean''' Geometric Mean - prescaled product (Π s<sub>i</sub><sup>-n</sup>)
<br>'''SumSq''' Sum of Squares
<br>'''Magnitude''' Pythagoras
<br>'''LinReg''' Linear least squares regression - frames returned m, b, r<sup>2</sup>
<br>'''TheilSen''' Theil Sen linear regression with Center estimator - frames m, b
<br>'''Theilsen2''' Theil Sen quadratic regression with with Center estimator - a,b,c
<br>'''Centroid''' Centroid
<br>'''Fit''' CurveFitter fitting - frames are model parameters, r<sup>2</sup>, Ψ<sup>2</sup>
<br>'''Deviation''' Appends a frame with the appropriate deviation from an appropriate selected summary.
<br>If the first slice of every frame has a Short Label that can be split by the regex " = |=| ", e.g., var = fval, and the list has unique elements, the float fval values will be used in the fittings instead of the frame number.

There are also static methods provided, with the same names, albeit, all lower case, with two syntaxis: <code>method(ImagePlus,slices,frames)</code>, <code>method(ImagePlus)</code>, <code>save fit(..., int), fit(..., String)</code>. 

<br><code>TreeMap<String,Double> getVars(ImagePlus imp, int f)</code>
<br>Extract variable/value pairs from frame's slice label.
<br><code>TreeMap<String,TreeMap<Double,Double>> getVars(ImagePlus imp)</code>
<br>Extract variable/values from all frames' slice labels.
<br><code>LinkedHashMap<String,String> overRepeats(ImagePlus imp, String var)</code>
<br>Determine the subsets (keys) that exist and the associated comma separated frames (values), where var is the repeater.
<br>see 'repeats var'
<br><code>TreeMap<Double,String> sortFramesByLabel(ImagePlus imp) </code>
<br>returns comma separated list of frames for each unique label.
<br><code>void removeVarFromLabels(ImagePlus imp, String var)</code>
<br>Remove superfluous variable var from all slice labels
<br><code>void replaceVarValWithInLabel(ImagePlus imp, String var, String val)</code>
<br>Replace all the values for var with val in all the slice labels.
<br><code>int findVarInLabel(ImagePlus imp, String var)</code>
<br>Determines position of var in the slice label variables. -1 not found or error.
<br><code>TreeMap<Double,String> sortFramesByLabel(ImagePlus imp, String var)</code>
<br>Determine frames (values - comma separated) that corrosponds to each var values (keys).
<br><code>ImagePlus extractFramesByVar(ImagePlus imp, String var, double val)</code>
<br>Extract all frames that have the variable / value pair var/val.
<br><code>TreeMap<Double,ImagePlus> extractFramesByVar(ImagePlus imp, String var)</code>
<br>Extract the frames (as an ImagePlus) that corresponds to each value (key) for slice label
<br><code>ImagePlus sortFramesByVar(ImagePlus imp, String var)</code>
<br>Rearrange frame order to that of increasing var values.
<br><code>double center(double[] a)</code>
<br>weighted mean weighted to the median
<br><code>double[] theilsen(double[] ... _x)</code>
<br>theilsen regressor for linear.
<br>can be called as x[],y[] or xy[][] but only the first pair computed
<br><code>double[] theilsen2(double[] ... _x)</code>
<br>theilsen regressor for quadradic.
<br>can be called as x[],y[] or xy[][] but only the first pair computed
<br><code>double[] linreg(double[] x, double[] y)</code>
<br>linear least squares regressor
<br>can be called as x[],y[] or xy[][] but only the first pair computed
<br><code>double centroid(double[] x, double[] y)</code>
<br>Centroid
<br><code>
<br>public interface Compute {
<br>public double[] compute(double[] x, double[] y);
<br>&nbsp;&nbsp;&nbsp;return (x == null) ? new double[NV] : process(x,y);
<br>&nbsp;&nbsp;&nbsp;}
<br>ImagePlus compute(ImagePlus imp, Compute fp)
<br>ImagePlus compute(ImagePlus imp, String slices, String frames, Compute fp)
<br>ImagePlus compute(ImagePlus imp, Compute fp, ImagePlus mask)
<br>ImagePlus compute(ImagePlus imp, String slices, String frames, Compute fp, ImagePlus mask)
</code>

<br><code>ImagePlus[] split(ImagePlus imp)</code>
<br>fit and compute have <code>ImagePlus[] method(..., ImagePlus[] imps);</code>
<br><code>imps</code> is syntactic sugar.
'''Nota bene''': Works even when there is only one slice in the Z direction.

=== Uses ===

==== ASL - MRI ====
<code>ImagePlus aslAcquired = . . .
<br>ImagePlus tag = F_Project.mean(aslAcquired,"all","1-100-2");
<br>ImagePlus ctl = F_Project.mean(aslAcquired,"all","2-100-2");
<br>ImagePlus asl = ctl.duplicate();
<br>(new ImageCaculator()).run("Subtract 32-bit stack", asl, tag);
<br>(new ImageCaculator()).run("Divide 32-bit stack", asl, ctl);
</code>
==== ADC - MRI ====
<code>/* Assuming many b-values (slicelabels = "b=%f") */
<br>ImagePlus dwiAcquired = . . .
<br>ImagePlus dwi = dwiAcquired.duplicate();
<br>ImagePlus dwib0 = SubHyperstackMaker.makeSubhyperstack(dwi,"1-"+dwi.getNSlices(),"1",dwiAcquired);
<br>for(int f=0; f<dwiAcquired.getNFrames(); f++)
<br>&nbsp;&nbsp;&nbsp;(new ImageCalculator()).run("Divide 32-bit stack", dwi, dwib0);
</code>
<br><code>ImagePlus adc_etal = F_Project.fit(dwi,"Exponential");''</code>
<br>OR with more resilience to outliers . . .
<code>
<br>IJ.run(dwi, "Log", "");
<br>ImagePlus adc_etal = F_Project.theilsen(dwi);
</code>

==== Arbitrary proccessing ====
<code>IJ.run(mask,"Convert to Mask", "method=Huang background=Default calculate");
<br>ImagePlus[] pimp = F_Project.compute(imp, new F_Project.Compute() {
<br>&nbsp;&nbsp;&nbsp;@Override
<br>&nbsp;&nbsp;&nbsp;public double[] compute(double[] x, double[] y) {
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if (x == null) return new double[10]
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return nonlinearFit(x,y);
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}
<br>&nbsp;&nbsp;&nbsp;}, mask, new ImagePlus[0]);
</code>
== F_Profilier ==
[[File:F_Profiler_Screenshot.jpg|400px]]
<br>Given a Hyperstack image, draw an ROI and start plugin. Manipulate the ROI and the plot changes. Check out Interactive_Fitting plugin.
== Frame_Slider ==
[[File:Frame_Slider_Screenshot.jpg|400px]]
<br>When you have one or more Hyperstacks open and want to step though the images per the variables in the slice labels, start the Frame_Slider with the dataset with the most variables, select the other datasets, and step through them using the sliders.  The datasets should all be governed by the same set of variables, i.e., The two left images are the raw data with repeats and the two right images are the mean and SNR projections, to see why click the scrollbars.
== Install ==
Unzip [https://imagej.net/_images/3/3d/Frames.zip Frames.zip] into ImageJ1 plugins (File>Show Folder>Plugins) or plugins/jars directories.  Source code in jar file.

== ChangeLog ==
  * 1 April 2018 - Initial Version.
  * 1 April 2019 - Updated.

[[Category:Import-Export‏‎]]
[[Category:Plugins]]
