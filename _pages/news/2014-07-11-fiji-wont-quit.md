---
title: 2014-07-11 - Fiji won't quit!
---

## Introduction

Since [releasing ImageJ2 into the wild](/news/2014-06-04-imagej-2-0-0-release-candidate), there has been a tremendous amount of user feedback. For those who have [reported bugs](/discuss/bugs): thank you!

Of all the issues reported, one has stood out as the most tenacious and difficult to solve: [Fiji bug \#805, "Fiji not closing"](https://fiji.sc/bugzilla/show_bug.cgi?id=805), colloquially known as the "Fiji won't quit!" problem. (Actually, versions of this bug existed before bug \#805 was reported, but that bug is where we have been tracking the issue most recently.)

As of this writing, we have just released ImageJ 2.0.0-rc-9 which we believe finally solves this issue after [six](https://github.com/imagej/imagej-legacy/commit/f2ba2b2645fe6aa5f0a0b5591defd37881dba31f) [different](https://github.com/imagej/imagej-legacy/commit/c441b81ac5b830ee8752038b3d9d86858b552634) [attempts](https://github.com/imagej/imagej-legacy/commit/8af9bfc4a0010374fa2390041c3735a7bbcc7e6f) [to](https://github.com/imagej/imagej-legacy/commit/62259dab7bbe70064ccaed621ac3940ffc6aaf61) [fix](https://github.com/imagej/imagej-legacy/commit/fe237a23fbde86171b8d574bdeb9c34a397dcfff) [it](https://github.com/imagej/imagej-legacy/commit/1f9b76f270e08a9c50abaf09c5938c4e08733892).

There were actually two different classes of misbehavior:

1.  **Being unable to quit.** The main window refuses to disappear, and the program becomes largely nonfunctional from that point forward and must be force closed.
2.  **Process not terminating.** ImageJ completes its shutdown routine and all windows disappear, but the Java process continues running in the background because `System.exit(0)` is never called.

## Being unable to quit

This class of bug was introduced because [we tried to improve upon ImageJ 1.x's behavior relating to the closing of windows and dialogs](https://github.com/imagej/imagej-legacy/commit/11fa5cb86112ae381448bf15a40fa29aeb32d553). It was previously the case that if you quit ImageJ while the [Script Editor](/scripting/script-editor) had tabs with unsaved changes, those changes would be discarded with no chance to save first. The behavior of ImageJ 1.x with other types of "non-sanctioned" windows (i.e., {% include github org='imagej' repo='ImageJA' tag='v1.49d' source='ij/WindowManager.java\#L393-L400' label='all `Window` instances other than `ImageWindow`, `TextWindow` or non-`Editor` `PlugInFrame`' %}) is to dispose them immediately without warning just prior to shutdown.

To address the problem, we [added a callback hook to ImageJ 1.x](https://github.com/imagej/ij1-patcher/commit/7b202c6c826e870c23a1fb0b91ebb86c217c133c) on the `WindowManager.closeAllWindows()` method, so that we could inject additional behavior. We then [dispatched a windowClosing event to each remaining window](https://github.com/imagej/imagej-legacy/commit/11fa5cb86112ae381448bf15a40fa29aeb32d553#diff-fb9b7c8be0fd7333a89ddb85e48390e5R508) to give them a chance to opt out of being closed. But it turns out that Java's standard paradigm of allowing windows to cancel their own closing conflates the ideas of confirming the close (e.g., with the user) with the process of actually doing the close/dispose on the window afterward. The approach proved too fragile and prone to deadlocks, so we ended up opting for a [different approach](https://github.com/imagej/imagej-legacy/commit/a1b3987e0302c270f80b0847ce86ca1ce1dd6861) instead. With a [minor update to the Script Editor](https://github.com/imagej/imagej-ui-swing/commit/b830cf749115065407564e3c5a65dae3ec74ab09), its windows now still prompt to save changes when quitting (whoo hoo!), but without the fragility of the original approach.

## Process not terminating

The second class of problem was introduced because ImageJ2 does not launch ImageJ via the {% include github org='imagej' repo='ImageJA' tag='v1.49d' source='ij/ImageJ.java\#L624' label='`ij.ImageJ.main`' %} method. There are several reasons for this from an architectural and technical standpoint, which are outside the scope of this blog post. But suffice to say that `ij.ImageJ.main` performs many actions which the ImageJ2 startup routine also needs to perform (but not in exactly the same way), such as handling command line arguments, most of which we covered—except for {% include github org='imagej' repo='ImageJA' tag='v1.49d' source='ij/ImageJ.java\#L666' label='a call setting the `exitWhenQuitting` flag to true' %}. By default, ImageJ 1.x does *not* call `System.exit(0)` when quitting, but whenever it is launched via its main method, it does. So even after [we updated ImageJ2's quitting routine to lean on ImageJ 1.x as much as possible](https://github.com/imagej/imagej-legacy/commit/428b93d7420649f843128fb9a992f53579105d39) (which seemed to fix the problem in many of our tests), it was still not always enough since `System.exit(0)` was never ultimately called. We fixed this discrepancy in the ImageJ legacy layer by [always setting exitWhenQuitting to true](https://github.com/imagej/imagej-legacy/commit/fe237a23fbde86171b8d574bdeb9c34a397dcfff) as well.

## Other complications

There were other considerations too, of course. It needs to be possible to:

1.  Shut down ImageJ through the UI via the ImageJ 1.x-based code path of {% include github org='imagej' repo='ImageJA' tag='v1.49d' source='ij/ImageJ.java\#L603' label='ij.ImageJ\#quit()' %}.
2.  Dispose of ImageJ programmatically via the ImageJ2-based code path of {% include github org='scijava' repo='scijava-common' tag='scijava-common-2.27.0' source='org/scijava/Context.java\#L367' label='org.scijava.Context\#dispose()' %} which in turn {% include github org='imagej' repo='imagej-legacy' tag='imagej-legacy-0.5.20' source='net/imagej/legacy/DefaultLegacyService.java\#L402' label='disposes the `LegacyService` and hence ImageJ 1.x' %}.

These two code paths need to behave very differently. In the case of (1), ImageJ 1.x's quitting routine happens, but some extra logic is injected to handle window closing better (see "Being unable to quit" above) as well as shut down the ImageJ2 application context in addition to ImageJ 1.x itself. In the case of (2), ImageJ2 disposes its entire context including the `LegacyService` which is responsible for managing ImageJ 1.x, meaning that ImageJ 1.x gets disposed as *part of* ImageJ2's disposal—all of which must {% include github org='imagej' repo='imagej-legacy' tag='imagej-legacy-0.6.0' source='net/imagej/legacy/IJ1Helper.java\#L199-L219' label='happen *without* calling `System.exit(0)` and *without* prompting the user to save any changes' %}.

## Conclusion

We believe we have finally ironed out all these problems, but as the above explanation hopefully conveys, ImageJ 1.x is fraught with multiple code paths, and quitting the program is no exception. Searching the ImageJ 1.x codebase for `System.exit(0)` yields five separate places where it gets called, one of which, astonishingly, is a {% include github org='imagej' repo='ImageJA' tag='v1.49d' source='ij/IJ.java\#L1464' label='potential code path of the `ij.IJ#getImage()` method' %}! Adding on the ImageJ legacy layer on top is a very complex endeavor, but we are proud to say that instances of ImageJ2 can be cleanly disposed of *without* shutting down the entire JVM, which provides a substantial boost to ImageJ's usability as a software library.

P.S. We [added regression tests](https://github.com/imagej/imagej-legacy/commit/8ead1c0a5eeb1a040d2eb473d8420c695a487709) for all the major scenarios, even including [an integration test for verifying that `System.exit(0)` is called](https://github.com/imagej/imagej-legacy/commit/3dedc32cb4609f2840db65947d6adedbcba29400) under the correct circumstances.

P.P.S. The "Fiji won't quit" T-shirt is coming soon! :-)


