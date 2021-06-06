---
title: 2016-01-05 - ImageScience is moving to an update site
---

Resulting from [a discussion](https://github.com/imagescience/ImageScience/pull/1) with {% include person id='emeijering' %}, the [ImageScience](/libs/imagescience) plugins have moved to their own dedicated [update site](/update-sites), and will no longer be distributed as part of core [Fiji](/software/fiji).

## What moved?

The ImageScience plugins include:

-   [FeatureJ](/plugins/featurej)
-   [MTrackJ](/plugins/mtrackj)
-   [RandomJ](/plugins/randomj)
-   [TransformJ](/plugins/transformj)

There is also a fifth plugin, [NeuronJ](/plugins/neuronj), which is now part of the ImageScience update site, not part of Fiji previously.

## Why?

The main reasons for the switch are:

-   To give Erik more control over the [development lifecycle](/develop/releasing) ([versioning](/develop/versioning), [releases](/develop/releasing), etc.).
-   To avoid a licensing conflict between Fiji's [GPL](/licensing/gpl) license and [ImageScience's proprietary one](http://www.imagescience.org/meijering/software/imagescience/).

## How does this affect users?

If you are using these plugins in your own workflows ([scripts](/scripting), [macros](/scripting/macro), [plugins](/plugins), etc.), then you will need to [enable the ImageScience update site](/update-sites/following) for those workflows to remain functional.

We will leave the current versions of the ImageScience plugins on the Fiji update site for a few more weeks, to give people time to transition to the update site. We anticipate a "spring cleaning" announcement in a couple of months, announcing the removal of several plugins, including the ImageScience ones.

As always, thanks for your support, and [let us know](/discuss) if you have any questions or concerns with this change.

  
