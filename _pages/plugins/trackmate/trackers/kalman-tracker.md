---
title: TrackMate Kalman tracker
description: The Kalman tracking algorithm in TrackMate.
extensions: ["mathjax"]
---



Starting from TrackMate v2.7.z, we shipped a new tracker that can deal specifically with linear motion, or particle moving with a roughly constant velocity. This velocity does not need to be the same for all particles. You can find it in TrackMate tracker selection under the name <b>Linear motion LAP tracker</b>.

Though it deals with a completely different motion model compared to the LAP trackers in TrackMate, it reuses the Jaqaman LAP framework, and it is similar to a tracker proposed in the Jaqaman paper as well: See the CD36 tracking, in the supplementary note 7 of the paper[^1]. But again, the version in TrackMate is simplified compared to what you can find in <b>u-track</b>.

### Principle

The linear motion tracker relies on the {% include wikipedia title="Kalman filter" %} to <i>predict</i> the most probable position of a particle undergoing constant velocity movement.

Tracks are initiated from the first two frames, using the classical LAP framework with the Jaqaman cost matrix (see above), using the square distance as cost. The user can set what is the maximal distance allowed for the initial search with the <b>Initial search radius</b> setting.

Each track initiated from a pair of spots is used to create an instance of a Kalman filter. There are as many Kalman filters as tracks. In the next frames, each Kalman filter is used to generate a prediction of the most probable position of the particle. All these predictions are stored.

Then, all the predicted positions are linked against the actual spot positions in the frame, using again the Jaqaman LAP framework, with the square distance as costs. The user can set how far can be an actual position from a predicted position for linking with the <b>Search radius</b> setting.

{% include img src='/media/plugins/trackmate/trackmate-kalman-tracker-principle.png' %}

Now of course, after linking, some Kalman filters might not get linked to a found spot. This event is called an occlusion: the predicted position did not correspond to an actual measurement (spot). The good thing with Kalman filters is that they are fine with this, and are still able to make a prediction for the next frame even with a missing detection. If the number of successive occlusions is too large, the track is considered terminated. The user can set the maximal number of successive occlusions allowed before a track is terminated with the <b>Max frame gap</b> setting.

Conversely, some spots might not get linked to a track. They will be used to initiate a new track in the next frame, as for the tracker initiation described above.

It is important to note here that the cost functions we use is the square distance, like for the Brownian motion, but from the predicted positions to the actual detections. Because the prediction positions are made assuming constant velocity, we are indeed dealing with an adequate cost function for linear motion. But since we are linking predicted positions to measured positions with the square distance cost function, we do as if the predicted positions deviate from actual particle position with an error that follows the gaussian distribution. This is a reasonable assumption and this is why this tracker will be robust.

### Implementation

The code can be found on {% include github org='fiji' repo='TrackMate' branch='master' path='/src/main/java/fiji/plugin/trackmate/tracking/kalman/KalmanTracker.java' %}. We now repeat the section above in pseudo-language. When you see the word <b>link</b> below, this means:

1.  Take all the source detections in frame t and the target detections in frame t+1.
2.  Compute the costs for all possible physical assignment (potential links) between source and target detections and store them in the cost matrix.
3.  Solve the LAP associated to this matrix.
4.  Create a link for each assignment found.

The particle linking algorithm would read as follow:

#### Initialization

1.  Link all the detections of frame 0 to the detections of frame 1, just based on the square distance costs (for instance).
2.  From each of the *m* links newly created, compute a velocity. This velocity is enough to initialize *m* Kalman filters.
3.  Initialize *m* tracks with the found detections and links, and store the associated Kalman filters.

#### Track elongation

1.  For each Kalman filter, run the prediction step. This will generate m predicted positions.
2.  Link the m predicted positions to the n detections in frame 2, based on square distance.
3.  Target detection that have been linked to a predicted position are added to the corresponding track.
4.  The accepted target detection is used to run the update step of the Kalman filter.
5.  Loop to next frame.

#### Track termination

1.  Some of the *m* predicted position might not find an actual detection to link to. In that case, we have an occlusion. The algorithm must decide whether it has to terminate the track or to bridge over a gap.
2.  If the number of successive occlusions for a Kalman filter is below a certain limit (typically 2 to 10), the track is not terminated, and the filter goes back to the track elongation step. Hopefully, from the new prediction a target particle will be found, and the detection in frame t will be linked to a detection in frame *t*+2 (or *t*+3 etc).
3.  Otherwise, the track is terminated and the Kalman filter object is dropped.

#### Track initiation

1.  Conversely, some detections in frame *t*+1 might not be linked to a predicted position. In this case, these orphan detections are stored to initiate a new track. But for this, other orphans detections are needed in frame *t*+2.
2.  This step is identical to the initiation step, but for subsequent frames. It requires to store orphan detections in current and previous frames.
3.  In frame *t*+2, priority must be given to detections linked to the predicted positions by the Kalman filters over orphan detections of frame *t*+1. So when you deal with frame *t*+2, you perform first the track elongation step, get a list of orphan detections in frame *t*+2, and then combine it to the orphan detections in frame *t*+1 to initiate new Kalman filters.


## References

{% include citation fn=1 doi="10.1038/nmeth.1237" %}
