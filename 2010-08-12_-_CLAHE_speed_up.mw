We implemented the fast version of the [[CLAHE|Contrast Limited Adaptive Histogram Equalization]].

From user perspective, the only difference to the old implementation is a new checkbox in the parameter dialog to toggle between fast and slow version.  Default is fast.  In the faster implementation, the local contrast adjustment is not calculated for each single pixel independently but for adjacent cells of the given block-size only.  The transfer function for locations in between is interpolated.  This is the approach as described in the original publication for close to real time video enhancement.

You will notice, that the result is not exactly the same as in the exact per-pixel evaluation but relatively close.  It is convenient to find appropriate parameters with the fast version and finally apply it with the accurate version.

[[Update Fiji]] to get the new version immediately.

There is also a [http://fly.mpi-cbg.de/saalfeld/download/clahe_.jar standalone plugin] for [https://imagej.net/ ImageJ] available.

[[Category:News]]
