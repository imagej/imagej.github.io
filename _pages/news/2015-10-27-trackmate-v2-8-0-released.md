---
title: 2015-10-27 - TrackMate v2.8.0 released
---

It is our please to announce the release of the version 2.8.0 of [TrackMate](/plugins/trackmate), after a quieter pace of development.

This version ships mainly small utilities, improvement and bugfixes. But more importantly, I would like to highlight several contributed [TrackMate modules](/plugins/trackmate/custom-edge-feature-analyzer-algorithms) since the last release.

## Contributed modules.

Pardon the informal tone this developer announcement will take but Ah! the joy this part causes me! All of us that wrote documentation for an academic open-source project know this pain and doubt very well: Is spending an excruciating time redacting tutorials for others to use an API worth anything? Is there any good that will come of it? Will this ever reach anyone? I am doing this for naught?

Picture yourself at work, leaned over the keyboard, this Wiki edit page opened, pondering the best way to make your message on [SciJava](/libs/scijava) extension mechanism through. When your boss knock at the door and says "I hope you are not writing tutorials for TrackMate. There is still papers X and Y to write, project Z has a report coming, and N users waiting for you to train them."

Picture yourself at home. It's night. It's cold. The kids approach the desk, full of expectations.

" - Daddy, come and play with us!

\- Daddy can't, boys, he's redacting tutorials for TrackMate extension mechanisms."

So of course we were thrilled when we saw the first 3rd party contributed TrackMate modules. We list the ones we are aware of. If you know others we missed, contact us directly to have this list updated.

### Ronny Sczech linear tracker and batch modules.

Ronny Sczech contributed:

-   A linear tracker module that deals specifically with spots that travel at a roughly constant velocity.
-   A track analyzer that reports track length, mean quality and angle.
-   A batch processor for TrackMate.
-   A new estimator for spot radius.

The source code is found on [his github page](https://github.com/chicoronny/RonnyTrackMate).

### Thorsten Wagner Find maxima detector.

Thorsten Wagner is working on a detector that emulates the Find maxima tool of ImageJ. The module is not totally ready, but you can find a working fork of TrackMate [here](https://github.com/thorstenwagner/plugins/trackmate) that ships the functionality.

### Benoit Lombardo analyzers.

Benoit Lombardo wrote a spot analyzer that compute mean intensities in all the channels of an image, when you have a multi-channel image. You can find it on the [TrackMate extras](https://github.com/tinevez/plugins/trackmate-extras) page.

## Improvements.

### Faster track rendering.

Since rather recently, the display of tracks on MacOSX and Linux platforms has become incredibly slow for a large number of tracks. I could not track the origin of the problem, that probably lies in the code of the JDK.

To temper it, the track rendering has changed and is now finer. This is has a strong and positive impact on track rendering on the aforementioned platforms.

### The ROI edit tool.

TrackMate permits semi-automated and curation of automated results. In some cases, there might be many spurious spots to remove manually. To make it less cumbersome, you can draw a ROI to select many spots at once. This is best explained in the following short video:

{% include video platform='youtube' id='IZenKcv6R4Y'%}

### The Block LoG detector.

TrackMate initial design always favored speed over memory consumption. This can be a problem for applications with large images, particularly for the detection of spots. For instance, when the LoG detector processes a single frame, it first copies it to a `float` image, then takes its complex FFT. This has a major impact when working with large images and using multithreading to process several frames at once.

To deal with this TrackMate now ships a **Block LoG detector**. It is identical to the LoG detector, except that it splits the image in smaller XY blocks and processes them independently. If you process each of this block sequentially, you can drastically reduce memory usage.

{% include img src="/media/news/trackmate-blocklogdetector.png" width="600px" alt="TrackMate Block LoG Detector" %}

Of course there is a price to pay: Spots that are present exactly on the block borders might be detected twice on two different blocks. This will have a very detrimental effect on the subsequent tracking step. To temper this problem, this detector prunes spots that are found inside other spots.

Also, you will save memory only if you process blocks sequentially. If you fire several threads at once, several blocks will be processed simultaneously, and each will consume some memory. So you need to tell TrackMate to use only 1 thread for processing, which is now possible.

### TrackMate honors ImageJ thread configuration.

To configure how many threads TrackMate can use, Go the the {% include bc path="Edit | Options | Memory & Threads..." %} menu item.

### TrackScheme acknowledges the spot radius setting when capturing thumbnails.

If you need to capture spot images with a larger radius than what the spots have, set the display radius ratio. This is very useful when you need to inspect a larger spatial context around spots.

{% include img src="/media/news/trackschemehonorsradiusratio.png" width="600px" %}

### The *Extract track stack* action improved.

It also acknowledges the display radius factor, and can generate multi-channel output when the source image has several channels. Also, if you just select one spot, it will generate the track stack for the whole track this spot belongs to.

### A new action to prune filtered out data.

TrackMate keeps the tracks and spots that have been marked as invisible by filtering. This can generate large XML files and memory usage, even when the useful data is small.

There is now an action called *Trim non-visible data* that actually discards the filtered-out data from memory.

### The *Quality* value reported by the LoG detector is now sensible.

By contract, all detectors must generate a quality value for each spot they found, that reflects how confident we are that this spot is not a spurious one. Quality is expected to be a positive number, large for 'good' spots, small for probably spurious spots.

Though the absolute value does not matter, the one reported by the LoG detector had several drawbacks. It could arbitrarily very large or very small depending on the physical spot size, and depended on the physical calibration of the source image.

Now, the quality value returned by the LoG detector is such that:

-   It has a maximal value for spots that have the size this kernel is tuned to (for equal spot intensity).

-   The quality will be of the same order of magnitude than the raw spot (if it
has the right size).

-   If the image has its calibration changed by a constant factor, one will retrieve the same quality value value than before scaling. However, I (JYT) could not derive the exact formula if the image is scaled differently across X, Y and Z.

## Bugfixes.

### Fix the accuracy problem in sub-pixel localization.

There was a bug that caused the sub-pixel localization to display a strong bias on the Y and Z coordinates for 3D data. It affected 2D data, though in a less marked manner.

This bug is now fixed in `imglib2-algorithm-0.3.3`. The bias is now gone, and you should see a marked improvement on the localization accuracy.

This bug was discovered by both Leanna Owen and Jan Eglinger, and was discussed in part [here](http://forum.imagej.net/t/accuracy-of-subpixel-localization-in-log-detector/).

### Fix the huge delay when manually adding a spot to large models.

When manually editing large models with many spots, just adding a single spot could take ages. This was due to a bug that triggered spot feature recalculation for the whole model. The bug is now fixed and editing even a large model is now considerably more responsive.

This bug was first reported by Anna Gilles though many may have feel the pain.

### The median filter was crashing TrackMate for 3D images.

Now fixed. Bug reported by Jan Eglinger.

{% include person id='tinevez' %} 10:53, 27 October 2015 (CDT)


