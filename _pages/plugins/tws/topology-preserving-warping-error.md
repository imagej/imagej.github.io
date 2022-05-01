---
mediawiki: Topology_preserving_warping_error
title: Topology preserving warping error
extensions: ["mathjax"]
---

{% include thumbnail src='/media/plugins/tws/warping-error-comparison.png' title='Application of the topology-preserving warping error. Example A and B have almost the same amount of pixel error with respect to the ground truth, however, example B has no topological error.'%} The **warping error** is a [segmentation](/imaging/segmentation) metric that tolerates disagreements over boundary location, penalizes topological disagreements, and can be used directly as a cost function for learning boundary detection[^1].

In other words, instead of focusing on the geometric differences (pixel disagreement) between two segmentations, the **warping error** focuses on the objects and measures the topological error between them.

## Pixel error

{% include thumbnail src='/media/plugins/tws/pixel-error-description.png' title='Pixel error between two different segmentations labels (A and B) with respect to the original labels (\*, ground truth).'%} The simplest way of evaluating a segmentation is by measuring the pixel error between the original labels and the segmented ones. Let $$l_i$$ denote the value of the boundary labeling *L* at image location *i*. The pixel error of *L* with respect to another binary labeling *L*<sup>\*</sup> is the number of pixel locations at which the two labelings disagree. This can also be written as the squared {% include wikipedia title='Euclidean distance' text='Euclidean distance'%} $$\parallel L - L^*\parallel^2$$, which is equivalent to the {% include wikipedia title='Hamming distance' text='Hamming distance'%} since the labels are binary-valued.

The pixel error is appealing because of its simplicity, but suffers from a serious defect. It is **overly sensitive to minor displacements in the location of a boundary** that are ubiquitous even when comparing one human boundary labeling to another. These disagreements cause no qualitative differences in the interpretation of the image, but can lead to large quantitative differences in pixel error.

## Digital topology and the warping error

Jain *et al.* [^1] introduced the **warping error**, another metric for comparing boundary labelings based on concepts from the field of {% include wikipedia title='Digital topology' text='digital topology'%}.

If *L*<sup>\*</sup> can be transformed into *L* by a sequence of pixel flips that each

1.  preserve a set of desired topological properties
2.  occur only at locations within a mask *M*,

then we will say *L* is a *warping of* *L*<sup>\*</sup>, or $$L \triangleleft L^*$$. The first condition constrains *L* and *L*<sup>\*</sup> to be **topologically equivalent**. The second condition can be used to constrain *L* to be geometrically similar to *L*<sup>\*</sup>. Both conditions will be explained in more detail below.

Now consider the pixel error of *T* relative to warpings of *L*<sup>\*</sup>. The *warping error* between some candidate labeling *T* and a reference labeling *L*<sup>\*</sup> is the {% include wikipedia title='Hamming distance' text='Hamming distance'%} (or equivalently squared {% include wikipedia title='Euclidean distance' text='Euclidean distance'%}) between *L* and the "best warping" of *L*<sup>\*</sup> onto *T*:

$$D(T \parallel L^*) = \underset{L \triangleleft L^*}{min} \parallel T-L \parallel ^2 $$ (Eq. 1)

In other words, the warping error between two segmentations is the **minimum mean square error between the pixels of the target segmentation and the pixels of a topology-preserving warped source segmentation**.

### Topological constraints

{% include thumbnail src='/media/plugins/tws/simple-points-example.png' title='Label relaxation is only allowed at simple points. The black pixels in the top circle and the white pixels in the bottom circle are not simple points, because flipping them would cause a merger or a split. Figure courtesy of [Viren Jain](http://www.hhmi.org/research/fellows/jain_bio.html).'%} To impose topological constraints on the warping, we use concepts from {% include wikipedia title='Digital topology' text='digital topology'%}, a field that extends the concepts of continuous-space topology to digital images. One of the most fundamental principles of this field is that complementary definitions of adjacency must be used for foreground ("1") and background ("0") pixels, so that a digital analog of the {% include wikipedia title='Jordan Curve Theorem' text='Jordan Curve Theorem'%} holds. We use the 4-adjacency for foreground and the 8-adjacency for background, and calculate {% include wikipedia title='Connected-component labeling' text='connected components'%} based on these adjacencies.

A major practical goal of digital topology is to identify methods of altering the *geometry* of objects within a digital image without altering any topological properties of the image. A **simple point** is defined as a **location in a binary image at which the pixel can be flipped to its complementary value without changing any topological properties** of the image. These properties include, for example, the number of $$\kappa$$-connected components of the foreground and the number of $$\bar{\kappa}$$-connected components of the background.

Although flipping a single simple point is guaranteed to preserve topology, it is not true that simultaneously flipping an arbitrary set of *multiple* simple points will preserve topology. Hence, many algorithms that deform digital images by altering simple points instead perform a sequence of flips, where any particular flip is made at a point that is simple relative to the current state of the image. Since all flips preserve topology, such a sequence of flips is a topology-preserving deformation of the original image (sometimes called a {% include wikipedia title='Homotopy' text='homotopic deformation'%}). The converse has also been proven: two images that are topologically equivalent in the sense of sharing isomorphic adjacency trees can always be transformed into each other by a sequence of changes in the values of simple pixels.

In short, by definition **flipping a simple point is a topology-preserving operation and flipping a non-simple point is not topology-preserving**. Non-simple points can be classified by the nature of the topological change they would cause by being flipped. The possible topological changes are

-   splitting,
-   merging,
-   hole addition/deletion,
-   or object addition/deletion.

We may wish to allow some of these types of changes, and therefore flipping of some types of non-simple pixels.

We will write simple(*L*) to denote the set of simple points of *L*.

### Geometric constraints

There are many ways to define the **mask**, depending on the exact nature of the desired geometric constraints. For example, in the original paper implementation, they choose *M* to be the set of all pixels within {% include wikipedia title='Euclidean distance' text='Euclidean distance'%} 5 from the background of *L*. This allows the foreground of *L* to expand arbitrarily, as long as topology is preserved. But the foreground can shrink by only a limited amount. Note that basing *M* on *L* makes warping an asymmetric relation.

### Descent algorithm for warping

{% include thumbnail src='/media/plugins/tws/warping-error-animation.gif' title='Example of the topology-preserving warping of one (binary) source image onto a target one.'%} As described by the authors, there is not an efficient algorithm for finding the global minimum in Eq. (1), and indeed this is likely to be an {% include wikipedia title='NP-hard' text='NP-hard'%} problem. However, there is a very simple descent algorithm for finding local minima. During warping, we are allowed to flip simple points of *L* that lie inside the mask *M*, i.e., points in the set $$simple(L) \cap M$$. Flipping any such pixel *j* of *L* satisfying $$ \mid t_j - l_j \mid &gt; 0.5 $$ produces a new warping with smaller error. The descent algorithm greedily picks the pixel for which this error reduction is the largest, breaking ties randomly.

Descent algorithm for warping the binary image *L*<sup>\*</sup> onto the binary image *T*, under geometric constraints set by the mask image *M*:

  
$$warp(L^* \in B,T \in A,M \in B)$$

$$L$$ := $$L^*$$

do

  
$$S := simple(L) \cap M$$

$$i := argmax_{j \in S} \mid t_j - l_j \mid$$ , breaking ties randomly

if $$\mid t_i - l_i \mid &gt; 0.5$$

  
$$l_i := 1 - l_i$$

else

  
return $$L$$

end

Since $$\parallel T-L \parallel ^2$$ is decreasing, the algorithm is guaranteed to converge to a local minimum of the warping error. How problematic is the lack of an efficient algorithm for finding a global minimum? It does not seem a problem in practice. The warpings found by this descent algorithm look reasonable to the eye. In spite of the random choice of flipped pixels, the results are highly reproducible in practice.

### Warping error versus Rand error

At first glance, it may seem that the **warping error** measures only boundary detection performance. But it is also a good measure of segmentation performance. This is because digital topology tells us how any single pixel affects the global topology of an image. The **warping error** is an upper bound on the number of topologically-relevant boundary labeling errors in *T* (if a geometric mask is used, then the **warping error** also includes labeling errors of a geometric nature). Therefore, if segmentations are generated from *T* and *L*<sup>\*</sup> by finding their connected components, then the **warping error** should be a reasonable measure of the topological disagreements between the segmentations.

The [Rand error](/plugins/tws/rand-error) can be used to compare segmentations in which regions are noncontiguous clusters of pixels. Such segmentations are not equivalent to boundary labelings, so the **warping error** cannot be applied. In many applications, this is not a significant limitation.

The **warping error** can be distinguished from the [Rand error](/plugins/tws/rand-error) in other respects. The **warping error** can penalize all kinds of topological errors, including the presence of holes and handles, but the [Rand error](/plugins/tws/rand-error) penalizes only connectivity errors. In certain medical imaging situations, control of such aspects of topology is especially important. The [Rand error](/plugins/tws/rand-error) mildly penalizes shifts in boundary location, while the **warping error** ignores them altogether. The **warping error** weights a topological error by the number of pixels involved in the error itself, while the [Rand error](/plugins/tws/rand-error) weights a split or merger by the number of pixels in the objects associated with the errors.

## 2D implementation in Fiji

The warping error metric is implemented for 2D images in the [Trainable Weka Segmentation](/plugins/tws) library. Here is an example of how to use it in a [Beanshell script](/scripting/beanshell):

```python
import trainableSegmentation.metrics.WarpingError;
import ij.IJ;

// original labels
originalLabels = IJ.openImage("/path/original-labels.tif");

// proposed (new) labels
proposedLabels = IJ.openImage("/path/proposed-labels.tif");

// mask with geometric constraints
mask = IJ.openImage("/path/mask.tif");

// threshold to binarize labels (just in case they are not binary)
threshold = 0.5;

metric = new WarpingError( originalLabels, proposedLabels, mask );

warpingError = metric.getMetricValue( threshold );

IJ.log("Warping error between source image " + originalLabels.getTitle() + " and target image " 
+ proposedLabels.getTitle() + " = " + warpingError);
```

## See also

-   [Rand error](/plugins/tws/rand-error).

## References

{% include citation fn=1 doi='10.1109/CVPR.2010.5539950' %}
