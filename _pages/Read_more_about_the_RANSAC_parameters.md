Ransac finds segments in the data using the model chosen for doing the fitting. In order to constrain the form of segments it finds there are certain parameters that user may have to choose to suit to their data. They are enumerated here.

* Max Error (in pixels) : This measure provides the distance between the data points and the model for classifying the inliers, data points that are within this distance from the fit model are included in the fit else they are considered as outliers and the line for determining rates is obtained by fitting a line model to the inliers.

* Minimum number of time points : This measures the minimum length of segments in time points for the growth events. As an example if a value of 50 is chosen for this parameter that implies that only the growth events that last for more than 50 time points are considered in the fit. The shrinkage events on the other hand proceed much quickly and the program has a preset number of just 3 time points for them.

* Maximum gap : This measures the gap in time points between two segments to be considered  as separate segments.
