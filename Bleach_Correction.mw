{{ComponentStats:sc.fiji:CorrectBleach_}}The plugin was made available by {{Person|Miura}} and Jens Rietdorf and the full documentation is available [http://cmci.embl.de/downloads/bleach_corrector at EMBL's site].

This plugin contains three different methods for correcting the intensity decay due to photobleaching. They all work with either 2D or 3D time series. In case of 3D time series, image properties should be appropriately set. If you are not sure, check your image header by [Image → Properties].

* Simple Ratio Method:
** Plugin version of [http://www.embl.de/eamnet/html/bleach_correction.html Jens Rietdorf's macro], extended further with 3D time series
* Exponential Fitting Method:
** Similar to the [[T-functions#Correcting_for_bleaching|description on the T-functions page]]. Additionally, this plugin also works with 3D time series.
** [[MBF ImageJ]] suggests to use “Exponential” equation for fitting, whereas this plugin uses “Exponential with Offset”
* Histogram Matching Method:
** A brand-new method for bleach correction.
** This algorithm first samples the histogram of initial frame, and for the successive frames, [[wikipedia:Histogram matching|histograms are matched]] to the first frame. This avoids the increase in noise in the latter part of the sequence which is a problem in the above two methods.
** This method does much better restoration of bleaching sequence for segmentation but not appropriate for intensity quantification.
** See the blog entry, [http://cmci.embl.de/blogtng/2010-05-04/photobleaching_correction_3d_time_series a bit more detail on this issue]

[[Category:Plugins]]
