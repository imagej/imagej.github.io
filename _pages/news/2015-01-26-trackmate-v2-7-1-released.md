---
mediawiki: 2015-01-26_-_TrackMate_v2.7.1_released
title: 2015-01-26 - TrackMate v2.7.1 released
---

We just release [TrackMate](/plugins/trackmate) v2.7.1 today. The unusual jumps in version number correspond again to internal changes in the core libraries that support the Fiji project.

This version ships a new tracker algorithm for TrackMate, that can deal specifically with particles with a roughly constant velocity, the **linear motion LAP tracker**.

The LAP trackers previously available in TrackMate had a cost calculation based on the square distance between two particles. This kind of costs dealt specifically with Brownian motion. TrackMate allowed to tune these costs with numerical features differences to better deal with motion model that were not brownian or dense particles.

But a tracker that deals specifically with a new motion model is welcome, in particular when it is as common as linear motion. Its principles are detailed [here](/plugins/trackmate/algorithms#linear-motion-tracker).

<figure><img src="/media/plugins/trackmate/trackmate-kalman-tracker-principle.png" title="TrackMate_KalmanTrackerPrinciple.png" width="600" alt="TrackMate_KalmanTrackerPrinciple.png" /><figcaption aria-hidden="true">TrackMate_KalmanTrackerPrinciple.png</figcaption></figure>

To assess the performance of the new and old trackers, we re-run the ISBI tracking challenge from 2012[^1]. We put all the results on a single page: [TrackMate Accuracy](/plugins/trackmate/accuracy) that should help you decide what is the algorithm that suits your problem best. For instance:

<figure><img src="/media/plugins/trackmate/trackmate-receptor-lap-brownian-motion-linear-motion-tracker-nearest-neighbor.png" title="TrackMate_RECEPTOR_LAP_Brownian_motion,_Linear_motion_tracker_&amp;amp;_Nearest_neighbor.png" width="300" alt="TrackMate_RECEPTOR_LAP_Brownian_motion,_Linear_motion_tracker_&amp;amp;_Nearest_neighbor.png" /></figure>


[^1]: [Chenouard *et al.*, "Objective comparison of particle tracking methods", Nature Methods, 2014](http://www.nature.com/nmeth/journal/v11/n3/full/nmeth.2808.html)
