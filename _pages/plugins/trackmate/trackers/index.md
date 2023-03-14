---
title: TrackMate Trackers
description: Documentation of the trackers available in TrackMate.
extensions: ["mathjax"]
---

Trackers are the [TrackMate](/plugins/trackmate) modules that can build tracks from individual objects. 
In TrackMate, tracking happens after the detection steps (from the objects given by the detection algorithms) and the spot filtering steps (so that we only perform tracking on filtered spots).
Tracking is an active field of Research with innovations every year.
TrackMate ships establied tracking algorithms, sometimes simplified from the original paper, with the aim at being general.
The pages below document the algorithms available in TrackMate.


## Tracking algorithms

- The [LAP trackers](lap-trackers): the tracking algorithms based on the Linear Assignment Problem algorithm, pioneered in [^1].
- The [Kalman tracker](kalman-tracker): a tracking algorithm suitable for objects that move with a nearly constant velocity.
- The [Overlap tracker](overlap-tracker): a tracker based on overlapping object contours, suitable for object with complex shapes and limited movements.
- The [Nearest-Neighbor tracker](nearest-neighbor-tracker): the simplest tracker.


## Evaluating tracking accuracy

TrackMate took part in the ISBI 2012 Grand Challenge on Single Particle Tracking.
This [page](accuracy) relates the challenge results for TrackMate and from it gives advice at how to choose a tracking algorithm for different use cases.


## References

{% include citation fn=1 doi="10.1038/nmeth.1237" %}
