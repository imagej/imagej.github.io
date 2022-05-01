---
mediawiki: TrackMate_version_history
title: TrackMate version history
---

<b>This page is deprecated!</b> Starting v5.1.0, please look at the gihub page for TrackMate releases: https://github.com/fiji/plugins/trackmate/releases

This page contains the version history for the [TrackMate](/plugins/trackmate) plugin. Bug fixes are not mentioned here, and do not get their own release number.

<div class="nonumtoc">
</div>

## 10/05/2012 - v.1.0

Initial release

## 22/05/2012 - v1.1

-   [TrackScheme](/plugins/trackmate/trackscheme) can change of display style.
-   De-activated folding branches in TrackScheme, as it was non-functional.
-   Fix bugs when loading invisible tracks.

## 13/06/2012 - v1.2

-   Far better memory management and speed improvement in LAP trackers when dealing with gap-closing only.
-   Renamed the "Fast LAP tracker" and "Simple Fast LAP tracker" to "LAP tracker" and "Simple LAP tracker". Also removed the old "LAP tracker" and "Simple LAP tracker". They give the same results, but are just way slower.
-   Replaced the ISBI challenge exporter by a simple track exporter.
-   New action: capture the spot images along a track.

## 25/02/2013 - v2.0.0

[Major update](/news/2013-02-25-trackmate-v2-0-0-released):

-   TrackMate now uses [ImgLib2](/libs/imglib2) internally, and is therefore ready to be moved to [ImageJ2](/software/imagej2).
-   TrackMate now computes edge features (on top of spot and track features). These features enable the immediate measure of velocity, displacement, etc...
-   Tracks can be colored in the Hyperstack displayer, in the 3D viewer and in TrackScheme using indifferently track or edge features.
-   All spot, edge and track features are computed automatically and kept in sync even versus manual modifications.
-   All spot, edge and track features are saved in the XML file.
-   All spot, edge and track features can be exported as ImageJ results tables. Then they can be exported to text files, readable by let's say Excel. (Please note that the authors of the plugin do not deem Excel as a proper solution for scientific analysis and recommend more professional solutions.)
-   All spot, edge and track features can be plotted as specialized graphs, thanks to a dedicated GUI panel.
-   Tracks can be named in TrackScheme. These names are used to sort alphanumerically the tracks as they are laid out. To change the name of a track, just double-click its current name in the TrackScheme view.
-   We use [semantic versioning](http://semver.org/) for release numbers from now on. The rules about backward incompatible changes - described below - required a major version change. However, we reserve the right to make a major number change only when there is backward incompatible changes to the user only. API changes might not trigger a major version change.
-   The XML file format changed and is therefore not compatible anymore between major versions. However, XML files generated with the previous version (v1.2) can be imported in v2.0.0. and are converted on the fly.
-   In linear-assignment-problem trackers (LAP tracker and simple LAP tracker), the time interval to bridge gaps is specified in frame interval instead of time interval.
-   In LAP trackers, detection of split and merge events are constrained to two consecutive frames.
-   The spot morphology analyzer is disabled.
-   Removed the spot intensity kurtosis, skewness and variance features.
-   Much better memory management in LAP tracker: Tracking on large number of spots will consume much less memory if tracks are not branching.
-   Speed up considerably the loading of large xml files.
-   Better GUI refreshing when performing heavy calculations.
-   All major operations are now multi-threaded, notably computing spot, edge and track features.
-   Track layout in TrackScheme is now deterministic: when branching, branches are sorted left to right using the name of the first spot in the branches.
-   Spots added manually are added in TrackScheme live in a dedicated column, to facilitate manual tracking.
-   In TrackScheme, added menu items to select tracks downward or upward in time from current selection.
-   In TrackScheme, the selection table can be exported as an ImageJ results table.
-   Better track layout in TrackScheme for tree-like structures.
-   Improved the performance of several track analyzers.
-   Full keyboard navigation.
-   The filter panels that appear in the GUI can have their threshold entered by keyboard: Set the focus to the histogram panel (press tab until the threshold value is displayed in dark red instead of orange, or click the panel), and type a number - possibly decimal, wait 1 s. You can also use the arrow keys to change it by 10% (left/right) or set it to a max or min value (up/down).
-   Fix a nasty and dangerous bug in LoG detector: We were not converting the filter sigma to pixel coordinates, yielding different filter strengths depending on the spatial calibration entered, even if the user-specified radius was the same. This generated a weirdness in spot coordinates that Alison Twelvetrees noted.
-   Fix the bug that caused the GUI to often hang after the initial filtering step.
-   Fix a bug when rendering tracks in the 3D viewer: the filtered-out tracks were displayed anyway. Noticed by David Mason.
-   Fix a bug causing TrackScheme and XML files to sometimes receive empty tracks.
-   Numerous minor bugfixes.

## 15/03/2013 - v2.0.1

-   Fix a bug noticed by Jan Brocher that prevented track splitting and merging events to be correctly detected in some cases.

## 22/03/2013 - v2.0.2

-   Fix a bug that prevented selecting edges when the 3D displayer is used.
-   Fix a bug that prevented some spots to be displayed in the side table of TrackScheme.
-   Fix a bug that prevented v2.0.0 xml files to be read.
-   Fix a bug that crashed the 3D viewer when there is no spot in frame.
-   Slight optimization of the 3D viewer startup.

## 5/6/2013 - v2.0.4

-   Fix a GUI bug, noticed by Tobias Pietzsch.

## 5/8/2013 - v2.1.0

-   Major rewrite of the core track model to achieve a far better performance when manually editing a very large datasets. You can now interactively edit large datasets without the GUI becoming too sluggish.
-   You can now preview the detection parameters on the current frame before applying it to the whole data.
-   The detection step is now interruptible in the GUI. A click on the cancel button will gracefully interrupt the detection process, and yields the spots found so far. They can be used later on normally.
-   The HyperStack viewer and editor has now a configuration panel that has a log window and some tools for manual annotation.
-   Semi-automatic tracking: Select one (or more) spot, TrackMate will find its most likely successors.
-   Re-design of TrackScheme. TrackScheme is now about 40 times faster to launch, even on large dataset. By default it uses the 'simple' style, and the update of the small thumbnails can be switched on/off.
-   The 'Load' button was removed from the GUI. TrackMate files can be loaded from the {% include bc path='Plugins | Tracking | Load a TrackMate file'%} menu item.
-   T/here is a new {% include bc path='Plugins | Tracking | Manual tracking with TrackMate'%} menu item, that launched another GUI stripped down for manual editing.
-   The XML file format has changed, to include more data, and for better separability and reuse in other softwares. However, backward compatible loaders are present to ensure the loading and on-the-fly conversion with files generated by TrackMate versions above 1.2.
-   Better coloring scheme. There is a unique coloring scheme shared in all views.
-   The GUI is now resizable.
-   A 'Locale' problem prevented the entering of numerical features correctly on system relying on other decimal separators that the dot. TrackMate now enforces the dot to be used as a decimal separator on all Locales. <b>However</b> there are still reports that this fails on Windows machine with exotic (*i.e.* non dot as decimal separator) locales.
-   Numerous other bugfixes.

## 30/10/2013 - v2.1.1

-   Fixes a bug generated by a conflict with a new component of imglib2. The fix involves work on imglib2 and TrackMate sides, and beneficiated from the attention and sweat of Curtis Rueden and Johannes Schindelin.

## 19/03/2014 - v2.2.0

-   Major **improvement for tracking performance**: The LAP trackers are now based on the [Jonker-Volgenant](http://link.springer.com/article/10.1007%2FBF02278710) solver, which performs better than the Munkres-Kuhn we were using until then. Our initial tests report that this new version runs 2x to 4x faster.
-   A **major problem was found in the LoG detector**: Because of a severe rounding error, the LoG detector was not behaving as a true LoG detector, which strongly hindered its accuracy and potence. The problem is now fixed and **the accuracy of the detector has vastly improved**. You should now observe much better results when using this detector: less spurious spots, better spot size sensitivity, better sensitivity to faint spots. On its side, the DoG detector now handles spots that lie on the border of the images better. Of course, the results will be different when comparing to v2.1.1.
-   We also took the chance to rewrite all the detectors from scratch, using the latest development in [ImgLib2](/libs/imglib2). This prompted **major performance improvement for the detection process**.
-   Complete rewrite of the way we handle modules in TrackMate. TrackMate now uses [SciJava](http://www.scijava.org/) and exploit its automatic discovery mechanism for modules. Practically, **it is now very easy to extend TrackMate**, and you do not depend on us anymore at all for anything. We could completely disappear and you would still be able to extend TrackMate so that it suits your need, without requiring any of our help. Several [tutorials](/plugins/trackmate#for-developers-1) describe how to do this. This is made possible thanks to the enormous efforts of the SciJava team. Thanks to them!
-   In [TrackScheme](/plugins/trackmate/trackscheme), the tracks can be navigated through using the keyboard:
    -   UP: previous spot in time.
    -   DOWN: next spot in time.
    -   LEFT: next sibling within the same track
    -   RIGHT: previous sibling within the same track
    -   PAGE-DOWN: jump to next track, same frame
    -   PAGE-UP: jump to previous track, same frame
-   Major performance improvement when launching [TrackScheme](/plugins/trackmate/trackscheme) on a large models.
-   Major performance improvement when selecting/deselecting in [TrackScheme](/plugins/trackmate/trackscheme)
-   The 3D viewer is now in sync with manual modification. Any edit made to the model is immediately echoed on the 3D viewer. This comes at a price: the 3D viewer cannot be used for very large model in an efficient manner.
-   The user can now define a *depth of drawing* display setting, that limits the number of Z-slices on which we draw the model. This is useful on very thick samples where the drawing of all the data across all Zs can become confusing.
-   Minor improvement for the track display on the main view, for large models.
-   Ship a [MATLAB](/scripting/matlab) function to import in [MATLAB](/scripting/matlab) the tracks exported by TrackMate. Check [this](/plugins/trackmate/analyzing-results-with-matlab).
-   Warn the user if they feed TrackMate with a stack that has no time-points by plenty of Z-slices. This is one of the main reason we get irrelevant bug reports: By default, ImageJ considers that a multi-image file is always made of 1 time-points and many Z-slices. Whereas users mean to feed TrackMate with a movie made of several 2D planes filmed over time. We now warn the user that the dimensionality stored in the image might not be the one they expect.
-   **Fine tune multithreading**. Before this version, TrackMate was doing multithreading during detection in the following way: We run the detection process on as many frames as we have threads, and each frame is processed using 1 thread. This is suboptimal if we have a large number of threads, but a few number of frames (e.g. 1 frame, 24 threads). This release fixes this: If we have 10 threads and 15 frames to process, we process 10 frames at once, and allocate 1 thread per frame. But if we have 10 threads and 2 frames, we process the 2 frames at once, and allocate 5 threads per frame if we can. For this to work of course, the detector must be multithreaded, which is the case with the ones we ship now.
-   TrackMate can now load partial TrackMate files, and still display all the information it could retrieve, instead of generating an error and quitting. This is useful if you have file that contains the model section, but not the settings section.
-   Improved user messaging when loading a file.
-   Spots can be colored by the features of the track they belong to.
-   Slightly better memory management for spot, edge and track coloring for large models.
-   The GUI does not freeze when computing histograms.
-   Fix a major bug with the DoG detector preventing to use it with a ROI.
-   Fixed a minor warning triggered when using the 3D viewer as the main view for TrackMate.
-   When navigating backward in the GUI, the model is cleared when it is sensible. This is made to avoid having "ghost" results floating over unprocessed images.
-   Fix several issues with zooming and decorations in TrackScheme. Fix a bug that caused the sliders to disappear for the simple style and with some zoom levels. Zooming should be now more efficient, and offers more zoom levels.

## 02-06-2014 - v2.3.0

-   It is possible to manually color spots and edges. The colors attributed are saved and retrieved from XML. To use it, select a few cells in TrackScheme and right-click to make the contextual menu appear:
-   There is now an action to export to [Icy](http://icy.bioimageanalysis.org/) track manager. It generates a XML file that can be opened in the [Icy track manager](http://icy.bioimageanalysis.org/plugin/Track_Manager).
-   Icy XML track files can be opened in TrackMate. Just point the TrackMate loader plugin to such a file, and its type will be detected and it will be opened in TrackMate. We would like to express our thanks to {% include person id='Fab14' %} for his help in developing these two features.
-   A new action allows merging two TrackMate files into one.
-   The color scale used to display colored tracks, links and spots can now be manually adjusted. In the display panel of the GUI, double click on the label "color by" and a settings window will open allowing the user to select between manual or automatic scaling. This is great to generate views that are comparable between datasets. This feature is commissioned and offered by Fumio Hayashi, Kobe University.
-   The table in the InfoPane of TrackScheme displays the full spot name.
-   Auto-linking mode allows the creation of links backward in time.
-   Two new track feature analyzers allow filtering tracks by their spots quality or by their longest gap.
-   Fix a potential (and potentially long standing) bug with numerical input on machine using locales different from the US locale.
-   Put back the forgotten Manual Tracker.
-   Save and retrieve the tracker used in the XML file.
-   Fix crash triggered when the specified ROI had points out of the source image bounds.
-   Fix crash when saving with a source image not loaded from disk.
-   Do not crash when saving unconfigured detector or tracker.
-   Many other bugfixes.

## 07-07-2014 - v2.4.0

-   TrackScheme now has an outline panel, useful to navigate in large models.
-   TrackScheme has a better layout for tracks that have merge and split events.
-   The 'Refresh' button on detector config panels is not present anymore. It's confusing and useless now that the quality value does not match pixel intensity at all.
-   TrackMate has new logos and icons, made by Agnieszka Kawska @ IlluScientia. http://www.illuscientia.com/
-   Fixed several problems with the 'Copy Overlay' action.
-   Fixed a severe TrackScheme bug, happening when creating links with invisible tracks.
-   Fixed a detector crash when running a preview detection with 0 spots found.

## 27-08-2014 - v2.5.0

-   A full rewrite of the LAP (simple and not simple) tracker, that takes advantage of the sparse structure of tracking problems. This has major consequences on the memory usage and on speed performance. Because the results are not strictly identical, the old version of the LAP tracker is still present.
-   TrackScheme has now a search box that will center the view on the spots with names that match.
-   TrackScheme main panel has proper row and column headers that stay visible even when scrolling away from the border.
-   A new action that exemplify a branch-based analysis.

## 25-09-2014 - v2.5.1

-   Fix several issues with the manual tracking plugin. Files were saved with missing information, generating warnings upon reloading.
-   Fix a bug with the semi-automatic tracker, not putting the correct time feature to found spot.
-   The GUI is resizable, so as to avoid bad surprise when using TrackMate on several different OSes.
-   Format the display of floating point numbers in a better way.
-   Tweak the toolbar of TrackScheme.

## 23-10-2014 - v2.5.2

-   Fix a bug in the sparse LAP trackers.
-   Fix the track spot quality feature analyzer.

## 23-10-2014 - v2.5.3

-   Fix another bug in the sparse LAP trackers.
-   Fix a bug when loading at the tracker config state.

## 05-11-2014 - v2.5.4

-   When graphing spot features, only include spots from visible tracks.
-   Fix a bug that prevented the XML file to be saved.

## 22-12-2014 - v2.6.3

TrackMate version bumped by several increments, prompted by the [big update](/news/2014-12-10-imglib2-released) that happened to Fiji between this and the previous release. Some minor bugfixes and improvements are shipped nonetheless.

-   In the table exports, spots and links are sorted by track then by frame.
-   TrackMate now works with 1D images: image sequences made of single line or single column frames.
-   Fix a bug that caused off behavior when the manual tracking plugin was launched twice in the same Fiji session.
-   The semi auto tracker has a new parameter that limits the number of frames it processes.
-   TrackScheme: A tooltip displays the track name and the frame when lingering over the row or column headers. This is made to improve orientation when unzoomed.
-   TrackScheme: Change the order of components in the side toolbar.

## 07-01-2015 - v2.6.4

-   Fix a bug in TrackScheme when deselecting spots.

## 09-01-2015 - v2.6.5

-   Put some sensible defaults when presented an image with no metadata.

## 26-01-2015 - v2.7.1

-   Add a new tracking algorithm: [the linear motion LAP tracker](/plugins/trackmate/algorithms#linear-motion-tracker).

## 26-01-2015 - v2.7.2

-   Fix a bug in the Linear motion LAP tracker, noticed by Ronny Sczech. The bug caused the linear tracker to crash on some cases.

## 19-03-2015 - v2.7.3

-   Fix a bug introduced by recent changes in the imglib2-algorithm, noticed by several people, and that prevented any spot feature to be computed.

## 23-06-2015 - v2.7.4

-   Fix a bug, incorrectly fixed in imglib, that caused dead threads to accumulate upon running the detection step. Noticed and fixed by @hadim, @dietzc and @tpietzsch.

## 27-10-2015 - [v2.8.0](/news/2015-10-27-trackmate-v2-8-0-released)

-   Contributed modules.
    -   Ronny Sczech linear tracker and batch modules.
    -   Thorsten Wagner Find maxima detector.
    -   Benoit Lombardo analyzers.
-   Improvements.
    -   Faster track rendering.
    -   The ROI edit tool.
    -   The Block LoG detector.
    -   TrackMate honors ImageJ thread configuration.
    -   TrackScheme acknowledges the spot radius setting when capturing thumbnails.
    -   The Extract track stack action improved.
    -   A new action to prune filtered out data.
    -   The Quality value reported by the LoG detector is now sensible.
-   Bugfixes.
    -   Fix the accuracy problem in sub-pixel localization.
    -   Fix the huge delay when manually adding a spot to large models.
    -   The median filter was crashing TrackMate for 3D images.

## 07/11/2015 - v2.8.1

-   Fix a big causing tracks not to be displayed on Windows platforms.

## 24/03/2016 - v3.0.1

This major version change only reflects recent changes in TrackMate API, partly prompted by the overhaul in progress in the Fiji ecosystem. There is very little new features and bug fixes and this release will be mainly of use for project depending on TrackMate.

Improvements.

-   The semi-auto tracker now detects spots in the currently selected channel, in case of a multi-C image.
-   The thumbnail images in TrackScheme are taken from the currently selected channel as well.
-   There is now a step-wise time browsing ('à la MaMuT'): press 'F' and 'G' to move in time by jumping to frames, spaced by a number set in the Spot edit tool of TrackMate (double-click on the icon in the ImageJ toolbar).
-   TrackMate is now more verbose when doing manual editing.

Fixes.

-   Minor usability fixes.

Changes.

-   The 3D Viewer is working again, at least (as of today) on Windows platforms. On Macs, the time slider does not work and trying to interact with it will crash Fiji.
-   Also, to keep the 3D Viewer tidy, it is not kept in sync with the manual edits made on the model. It just shows a snapshot of the model at the time when it was launched. It was not working properly before anyway, so we officially disable this feature.

## 31/03/2016 - v3.1.0

Improvements:

-   Add an action that export all visible spots statistics, regardless of whether they belong in a track or not.

<!-- -->

-   New display mode: show only selection.

This track display mode only shows the content of the current selection, for spots and edges. It can be accessed in the GUI panel 'Configure views' with a special track display mode called 'Selection only'.

Careful: the content of the selection model can still be edited in this mode. Of course, the track display mode is ignored by TrackScheme, which then can be used to modify the selection in this mode.

Changes:

-   We really do not relaunch TrackScheme automatically when loading a TrackMate file.

## 12/04/2016 - v3.2.0

-   TrackMate can now be called from an IJ macro.

Only a subset of TrackMate features can be used, though. Right now, only the LoG detector and the Simple LAP tracker are used. But for instance, you can call TrackMate with the following syntax:

    run('TrackMate', "use_gui=false "
                            + "save_to=[/Users/tinevez/Desktop/plugins/trackmateSaveTest.xml] "
                            + "export_to=[/Users/tinevez/Desktop/plugins/trackmateExportTest.xml] "
                            + "display_results=true "
                            + "radius=2.5 "
                            + "threshold=50.1 "
                            + "subpixel=false "
                            + "median=false "
                            + "channel=1 "
                            + "max_frame_gap=0" )

If you need other detectors and trackers, you have to rely on Python for now. [Scripting\_TrackMate](/plugins/trackmate/scripting)

-   Several TrackScheme improvements:
    -   The row and column headers are now properly displayed and resized when zooming.
    -   TrackScheme can be navigated with the keyboard:
        -   The numeric keypad is used to pan around.
        -   +/- zoom in/out.
    -   Better navigation with mouse:
        -   Hold space and drag to pan, as in ImageJ.
        -   Hold space + mousewheel to zoom in/ out.

## 23/03/2017 - v3.5.0

-   The **Recalculate features** action now recomputes all features.

And if a Controller instance is provided, the analyzers declared in the GUI are used to recompute the features. This is useful if a file was saved before new feature analyzers were added.

-   GUI tweaks.

<!-- -->

-   Allow spot detection on images with a discontinuous ShapeRoi.

If the current ROI is an ij.gui.ShapeRoi, we use this to filter the spot detections in each frame. For other cases, we keep the settings.polygon for backward compatibility. Contributed by Jan Eglinger.

-   Switch from Jenkins to Travis CI.

By Curtis Rueden.

-   The Extract track stack action can capture 3D stacks.

<!-- -->

-   Fix Kalman tracker bug for empty first frames.

The Kalman tracker was unable to process if the first two frames contained zero spots. Noted by Hadrien Mary.

-   Fix improper image factory for very large images.

Noted by Christian Tischer.

## 25/06/2018 - v3.8.0

-   As advised by @ctrueden: do not use java.awt.Robot for capture, but instead directly paint into a BufferedImage. The capture is now much quicker (as fast as painting, no need to wait), more robust, and the code as fewer lines as well. It is so perfect that I wonder why I could not think of this before.

<!-- -->

-   Set the calibration properly, even if this is a capture.

<!-- -->

-   And give a better title to the imp.

## 06/09/2019 - v4.0.1

-   Properly use the ManualDetectorFactory in scripts: does not crash nor remove existing spots.

<!-- -->

-   Display the true plugin version on the GUI. It was displaying 3.8.0 but we were on 4.0.0 for quite some time.
