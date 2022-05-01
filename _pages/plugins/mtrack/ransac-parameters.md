---
mediawiki: MTrack-RANSAC_parameters
title: MTrack-RANSAC parameters
---

RANSAC is a non-deterministic algorithm that fits a function to data points by maximizing the number of data points that support the function fit (inliers), given an error epsilon. In order to constrain the form of segments it finds there are certain parameters that user may have to choose to suit to their data. They are enumerated here.

-   Max Error (in pixels) : This determines the maximum tolerance of RANSAC fits on both events, growth (red) and shrinkage (blue) events. A high maximum error value will classify more data points as inliers, a low maximum error will classify more data points as outliers.

<!-- -->

-   Minimum number of time points : This determines the minimum number of data points that define a growth event. If you choose 20, only events that last for 20 time points will be considered to be a growth event. Shrinkage events, on the opposite, are much shorter and are allowed to last only 2 data points.

<!-- -->

-   Maximum gap : This determines the number of time points to define two consecutive events as independent events.

Function for inlier detection:

-   Regularized polynomial of mixed order are used to determine inliers, the options are either a straight line or a second or a third order polynomial regularized with a straight line. After the inliers are determined a straight line fit in the inliers is done in order to obtain growth and shrinkage velocity.
