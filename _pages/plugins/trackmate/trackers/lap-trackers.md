---
title: TrackMate LAP Trackers
description: Linear Assignment Problem tracking algorithms in TrackMate.
extensions: ["mathjax"]
---


The Linear Assignment Problem (LAP) trackers implemented here follow a stripped down version of the renowned method contributed by Jaqaman and colleagues[^1]. We repeat here the ideas found in the reference paper, then stresses the differences with the nominal implementation.

In [TrackMate](/plugins/trackmate), the LAP framework backs up two instances of a tracker (four if you count the old ones, prior to v2.5.z):

-   the Simple LAP tracker;
-   the LAP tracker.

The first one is simply a simplified version of the second: it has less settings and only deal with particle that do not divide nor merge, and ignores any feature penalty (see below).

All the linking costs for these two trackers are based on the particle-to-particle square distance. If this tracker had to be summarized in one sentence, it would be the following: <b>The Simple LAP tracker and the LAP tracker are well suited for particle undergoing Brownian motion.</b> Of course, they will be fine for a non-Brownian motion as long as the particles are not too dense.

Particle-linking happens in two step: track segments creation from frame-to-frame particle linking, then track segments linking to achieve gap closing. The mathematical formulation used for both steps is linear assignment problem (LAP): a cost matrix is assembled contained all possible assignment costs. Actual assignments are retrieved by solving this matrix for minimal total cost. We describe first how cost matrices are arranged, then how individual costs are calculated.

### Cost matrix for frame-to-frame linking

In the first step, two consecutive frames are inspected for linking. Each spot of the first frame is offered to link to any other spot in the next frame, or not to link. This takes the shape of a (*n*+*m*) x (*n*+*m*) matrix (n is the number of spots in the frame t, m is the number of spots in the frame t+1), that can be divided in 4 quadrants.

-   The top-left quadrant (size *n* x *m*) contains the costs for linking a spot *i* in the frame *t* to any spot *j* in the frame *t+1*.
-   The top-right quadrant (size *n* x *n*) contains the costs for a spot *i* in the frame *t* not to create a link with next frame (yielding a segment stop).
-   The bottom-left quadrant (size *m* x *m*) contains the costs for a spot *j* in the frame *t+1* not to have any link with previous frame (yielding a segment start).
-   The bottom-right quadrant (size *m* x *n*) is the auxiliary block mathematically required by the LAP formalism. A detailed explanation for its existence is given in the supplementary note 3 of [^2]. This quadrant is built by taking the transpose of the top-left quadrant, and replacing all non-blocking costs by the minimal cost.

### Solving LAP

To solve this LAP, we rely on the Munkres & Kuhn algorithm[^2], that solves the problem in polynomial time (*O(n<sup>3</sup>)*). The algorithm returns the assignment list that minimizes the sum of their costs.

The frame-to-frame linking described above is repeated first for all frame pairs. This yields a series of non-branching track segments. A track segment may be start or stop because of a missing detection, or because of a merge or split event, which is not taken into account at this stage. A second step where track segments are offered to link between each other (and not only spots) is need, and described further down.

### Calculating linking costs

In calculating costs, we deviate slightly from the original paper from Jaqaman *et al.*[^1]. In the paper, costs depend solely on the spot-to-spot distance, possibly weighted by the difference in spot intensity. Here, we offer to the user to tune costs by adding penalties on spot features, as explained below.

The user is asked for a maximal allowed linking distance (entered in physical units), and for a series of spot features, alongside with penalty weights. These parameters are used to tune the cost matrices. For two spots that may link, the linking cost is calculated as follow:

1.  The distance between the two spots D is calculated
2.  If the spots are separated by more than the max allowed distance, the link is forbidden, and the cost is set to [infinity](http://docs.oracle.com/javase/6/docs/api/java/lang/Double.html#positive-infinity) (*i.e* the blocking value). If not,
3.  For each feature in the map, a penalty p is calculated as  
    $$ p = 3 \times W \times \frac{ | f_1-f_2|}{f_1+f_2} $$  
    where W is the weight associated to the feature in the map. This expression is such that:
    -   there is no penalty if the 2 feature values f1 and f2 are the same;
    -   with a weight of 1, the penalty is 1 if one feature value is the double of the other;
    -   the penalty is 2 if one feature value is 5 times largerr than the other one.
4.  All penalties are summed, to form P = (1 + ∑ p )
5.  The cost is set to the square of the product: C = ( D × P )²

If the user feeds no penalty, the costs are simply the distances squared.

### Calculating non-linking costs

The top-right and bottom-left quadrant of the frame-to-frame linking matrix contain costs associated with track segment termination or initiation (a spot is not linking to a spot in the next or previous frame). Each of these two blocks is a square matrix with blocking value everywhere, except along the diagonal for which an alternative cost is computed. Following Jaqaman[^2], this cost is set to be

$$C_{alt} = 1.05 × max( C )$$

where *C* is the costs of the top-left quadrant.

### Cost calculation & Brownian motion

Without penalties and with a maximal linking allowed distance, the returned solution is the one that minimizes the sum of squared distances. This actually corresponds to the case where the motion of spots is governed by {% include wikipedia title="Brownian motion" %}. See for instance Crocker and Grier[^3].

By adding feature penalties, we aim at favoring linking particles that "resemble" each other. In brute single particle linking problems, spots are generally all the same, and they only differ by position. However, there is a variety of problems for which these feature penalties can add robustness to the tracking process.

For instance, we originally developed [TrackMate](/plugins/trackmate) for semi-automated lineaging of *C.elegans* embryos, using a strain fluorescent in the nucleus. Cells that are dividing have a fluorescence distribution which is very different from non-dividing cells, and this can be exploited for robust tracking.

### Track segment linking

In a second step, the track segments built above are offered to link between each other. Jaqaman and colleagues proposes to exploit again the LAP framework for this step. A new cost matrix is generated, but this time the following events are considered:

-   The end of a track segment is offered to link to any other track segment start. This corresponds to <u>gap-closing</u> events, where a link is created typically over two spots separated by a missed detection.
-   The start of a track segment is offered to link to the spots in the central part (not start, not end) of any other track segment. This corresponds to <u>splitting</u> events, where a track branches in two sub-tracks.
-   The end of a track segment is offered to link to the spots in the central part of any other track segment. This corresponds to <u>merging</u> events, where two tracks merges into one. I yet did not meet this case in Life-Sciences.
-   A spot part of any track segment is offered not to create any link.

The second cost matrix has a shape that resembles the first cost matrix, calculated for frame-to-frame linking, and which is best described in the original article.

As before, we modified the way costs are calculated, and re-used the feature penalties framework described above. Also, the user must provide on top a maximal time-difference to link, over which linking will be provided. Careful: this maximal time is expressed in physical units and not in number of frames.

### Main differences with the Jaqaman paper

The nominal implementation of the paper remains the one developed under [MATLAB](/scripting/matlab) by Khuloud Jaqaman <i>et al.</i> and published in Nature Methods. The software is called u-track and can be found on [Khuloud Jaqaman homepage](http://www.utsouthwestern.edu/labs/jaqaman/software/).

TrackMate was initially developed to simplify <i>C.elegans</i> lineaging. It therefore just bundles a stripped down version of this framework.

The notable differences are:

1.  The LAP framework is generic: Jaqaman and colleagues proposed a framework to approximate multiple-hypothesis tracking solutions using linear assignment problems. One just need to provide the link cost matrix. <b>TrackMate</b> properly implements the LAP framework, but the cost matrix calculation - which is specific to each problem - is much more simpler than in <b>u-track</b>.  
    For instance, in TrackMate all link costs are based on the square distance between two spots (weighted or not by feature differences, see above), which make it tailored for Brownian motion. In <b>u-track</b>, the user is proposed with different motion types, including a linear motion whose parameters are determined on the fly. See for instance CD36 tracking, in the supplementary note 7 of the paper[9].
2.  In <b>u-track</b>, merging and splitting of tracks are used to describe two particles that temporally overlap spatially. These events' costs are weighted by the two particle intensities to properly catch the apparent increase in intensity due to the overlap. In <b>TrackMate</b>, we use splitting events to describe cell divisions, as we developed it initially to deal with <i>C.elegans</i> lineages. However is seems than Jaqaman and colleagues used it the same way to investigate CD36 dissociation and re-association.
3.  In <b>TrackMate</b>, distance and time cutoffs are specified manually by the user. In <b>u-track</b> they are derived for each particle automatically, providing self adaptation.


## References

{% include citation fn=1 doi="10.1038/nmeth.1237" %}

[^2]: J. Munkres, "Algorithms for the Assignment and Transportation Problems", Journal of the Society for Industrial and Applied Mathematics, 5(1):32–38, 1957 March

{% include citation fn=3 doi="10.1006/jcis.1996.0217" %}
