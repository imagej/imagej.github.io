---
title: 2014-04-21 - Multiview deconvolution
---

**Stephan Preibisch's** multiview deconvolution algorithm and the associated Fiji plugin was published at [Nature Methods](http://www.nature.com/nmeth/journal/vaop/ncurrent/full/nmeth.2929.html). The approach is relevant especially as a fusion strategy for SPIM data,

{% include citation doi="10.1038/nmeth.2929" %}
[PDF](/media/nmeth.2929.pdf), [Supplement](/media/news/nmeth.2929-s1.pdf)

Check out the extensive supplement that provides the derivation of the algorithm (for the mathematically inclined) and extensive evaluation and benchmarking against other approaches. The GPU code was developed by **Fernando Amat** from Philipp Keller's lab at the Janelia Farm.

The paper comes with an extensive collection of **Supplementary Videos** available at [Nature Methods website](http://www.nature.com/nmeth/journal/vaop/ncurrent/fig_tab/nmeth.2929_SV1.html).

If you are interested in the paper's genesis under intense but constructive scrutiny of reviewers, you may want to have a look at the various submitted pre-prints on arxiv [arxiv v1](http://arxiv.org/abs/1308.0730v1) [arxiv v2](http://arxiv.org/abs/1308.0730v2) [arxiv v3](http://arxiv.org/abs/1308.0730v3)

The [documentation](/plugins/multi-view-deconvolution) for the Fiji plugin contains description of parameters and a 'how to' for hacks that didn't yet make it into the plugins menu's. It complements other SPIM related Fiji plugins such as [bead based registration](/plugins/spim-bead-registration) & [Multiview fusion](/plugins/multi-view-fusion).

Finally, a Figure from the paper showing that multi-view deconvolution matters!

{% include img src="/media/news/mv-deconv-examples.jpg" width="700px" %}

This is probably not the last answer to SPIM data deconvolution. We are looking forward to the input from the computer vision community to this hard problem.


