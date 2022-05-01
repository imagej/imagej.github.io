---
title: 2010-06-14 - Fiji "Heidelberg" is out
---

I proudly announce a new version of Fiji (Fiji Is Just ImageJ -- batteries included).

In our cherished tradition, the current version is named after the location of a big hackathon: Heidelberg. We were honored to have some Fiji developers invited by the [EMBL](http://www.embl.de) in Heidelberg from March 15 -- 26, 2010, thanks to the generous support of [Francesca Peri](http://www.embl.de/research/units/dev_biology/peri/index.html) and Kota Miura.

There have been 524190 lines added and 245463 removed since the previous release, with the help of (in alphabetical order): Albert Cardona, Andreas Wiese, Benjamin Schmid, Ben Tupper, Chris Elliott, Curtis Rueden, Daniel Hornung, Daniel James White, Davi Bock, Gabriel Landini, Gregory Jefferis, Ignacio Arganda-Carreras, Jacques Pecreaux, Jan Eglinger, Jean-Yves Tinevez, Johannes Schindelin, Larry Lindsey, Mark Longair, Nick Weiler, pixelhead, pogo, Ricardo Henriques, Stephan Preibisch, Stephan Saalfeld, Tom Kazimiers and Verena Kaynig, and many other helpers.

## Changes since Fiji Plzeň

-   There is a new plugin called [Trainable Segmentation](/plugins/tws). This plugin offers advanced machine learning techniques to train a model that segments your images into different classes.  
While it is developed actively, it is already quite powerful and easily usable by non-programmers.

-   Fixed a critical bug in the [Fiji Updater](/plugins/updater) that affected MacOSX. Symptom:  
Fiji no longer starts after an update). If you have not updated between April 8, 2010 and June 3rd, 2010, this bug affects you and you have to follow [these instructions](/learn/troubleshooting).

-   Unfortunately, we had to drop support for MacOSX PPC. If you need Fiji on such a system, please contact [the Fiji developer mailing list](https://groups.google.com/g/fiji-devel), and we will try to provide a special edition.

-   For Debian/Ubuntu users, there will be [fine-grained packages](/develop/debian-notes) of Fiji Heidelberg available soon.

### Other changes

-   Fiji's core was frequently synchronized with ImageJ.

-   many, many improvements in [bUnwarpJ](/plugins/bunwarpj) (thanks Ignacio Arganda-Carreras).

-   Context Help: If you click on {% include bc path='Help | Help on Menu Item'%}, the next click on a menu item will open the corresponding page (if there is one) on the Fiji Wiki.

-   Statistical Region Merging can work in 3D now (this uses lots of memory).

-   The Stack Manipulation menu got another entry: Slice Keeper (thanks Jean-Yves Tinevez).

-   many, many improvements to the [Simple Neurite Tracer](/plugins/snt) and [3D Viewer](/plugins/3d-viewer), which were split off from the [VIB Protocol](/plugins/vib-protocol) plugin (thanks Mark Longair and Benjamin Schmid).

-   many updates for the [Register Virtual Stack Slices](/plugins/register-virtual-stack-slices) plugin (thanks Ignacio Arganda-Carreras).

-   [Auto Threshold](/plugins/auto-threshold) was improved, and made accessible to other plugins (thanks Gabriel Landini).

-   implemented [CLAHE](/plugins/clahe), a filter for adaptive local contrast enhancement (thanks to Stephan Saalfeld).

-   removed dependency on Jama of mpicbg plugins (thanks to Stephan Saalfeld).

-   separated libraries from plugins, e.g. mpicbg plugins from mpicbg library (thanks to Stephan Saalfeld).

-   added several mpicbg library tools, many bug-fixes and improvements (thanks to Stephan Saalfeld).

-   [TrakEM2](/plugins/trakem2) was updated several times, with tons of new goodies (thanks Albert Cardona and Stephan Saalfeld). For example:

    - extended multi-layer-mosaic alignment to handle

        - adjustable weights for cross-section vs intra section features

        - handle multiple disconnected graphs

        - non-linearly deform section graphs

    -  properly propagate non-linear manual deformations

    -  speed up rendering of deformed images

    -  calibrate exported snapshots

    -  several bug-fixes

-   A plugin was added that performs the [SIOX](/plugins/siox) algorithm (color segmentation by example, thanks Ignacio Arganda-Carreras).

-   Some bugs in [Stitching 2D/3D](/plugins/stitching-2d-3d) were fixed (thanks Stephan Preibisch and Ignacio Arganda-Carreras).

-   A plugin "IsoData Classifier" was added that extends the default automatic threshold of ImageJ to multiple classes (more than two).

-   Fiji's arrow tool offers interactive manipulation of the arrow (which is a ROI now), with different widths, head sizes, and head shapes (thanks to Jean-Yves Tinevez).

-   A bug was fixed in the [MTrack2](/plugins/mtrack2) plugin (thanks to Chris Elliott).

-   There is a GenericDialogPlus in fiji-lib.jar now that supports adding "file" and "directory" fields with a button to choose the value via a file dialog (thanks Stephan Preibisch and Ignacio Arganda-Carreras).

-   Many improvements to the [AnalyzeSkeleton](/plugins/analyze-skeleton)/[Skeletonize3D](/plugins/skeletonize3d) plugins (thanks Ignacio Arganda-Carreras and Daniel Hornung).

-   The [RATS](/plugins/rats) plugin was added, providing a very powerful automatic local thresholding technique (thanks Ben Tupper).

-   Jython was updated to version 2.5.

-   The code of the [VIB Protocol](/plugins/vib-protocol) was improved (thanks to Mark Longair, Benjamin Schmid and Nick Weiler).

-   {% include bc path='Plugins | Macros | About Startup Macros'%} works again (thanks Gabriel Landini).

-   The Fiji launcher was modified to work around a Java 1.5 bug on Linux.

-   The Java WebStart'able Fiji was fixed.

-   The [Script Editor](/scripting/script-editor) offers code templates now (thanks Tom Kazimiers).

-   The Find/Replace function in the [Script Editor](/scripting/script-editor) now defaults to the selected text (thanks Tom Kazimiers).

-   The [Tutorial Maker](/plugins/tutorial-maker) was renamed to {% include bc path='Plugins | Utilities | Fiji | New Fiji Tutorial'%}, and you can choose to upload to another Wiki than the Fiji Wiki (provided that it is powered by MediaWiki). It also uses the [Script Editor](/scripting/script-editor) for better usability now.

-   The [Image Expression Parser](/plugins/image-expression-parser) plugin was added, providing much more powerful operations on Images than the simple Image Calculator or Image Calculator Plus plugins (thanks to Jean-Yves Tinevez).

-   There is an {% include bc path='Image | Adjust | Auto Crop'%} plugin (cropping the maximal border that matches the background color), and an {% include bc path='Image | Adjust | Auto Crop (guess background color)'%} plugin (estimating the most likely background color from the border).

-   We have a Linear Gradient and Radial Gradient plugin now, to generate gradients in existing images.

-   There was a bug fix in .mrc reading (thanks Jean-Marc Verbavatz and Quentin de Robillard).

-   Fiji starts with Java settings optimized for heavy-duty usage now (thanks Albert Cardona).

-   when using a .java plugin transparently (by putting it into Fiji's plugins/ directory), the error output will be shown now.

-   The [Script Editor](/scripting/script-editor) offers tabs now.

-   When a file changed outside the [Script Editor](/scripting/script-editor), it offers to reload the file now.

-   The [Script Editor](/scripting/script-editor) offers the ImageJ Macro Language in the Languages menu, with syntax-highlighting. Consequently, it is now the default editor for macros.

-   The [Script Editor](/scripting/script-editor) got a function to run just the selected part of the script.

-   Many more improvements in the [Script Editor](/scripting/script-editor).

-   Many improvements to the Colocalization plugins (e.g. the output of Colocalization Threshold can be saved to a file now, etc). Thanks to Daniel James White and Tom Kazimiers.

-   The [Directionality](/plugins/directionality) plugin was added to analyze images containing oriented structures (thanks Jean-Yves Tinevez).

-   The [Time Stamper](/plugins/time-stamper) plugin was updated (thanks Jean-Yves Tinevez, Daniel James White and Tom Kazimiers).

-   Add a Recent Commands menu entry to list the most recent and the most frequent commands.

-   The FileDialogs on Linux have more sensible keyboard handling now, and are Drag 'n Drop targets, as on other platforms, too.

-   There is an Imglib Algorithm Launcher now, which makes it easy to use the full power of imglib for users, and which is easily extensible to future algorithms in imglib (thanks to Curtis Rueden).

-   In Fiji, the menu entry is called {% include bc path='Help | Refresh Menus'%} instead of {% include bc path='Help | Update Menus'%}, to clarify what the function is about.

-   When Fiji detects that the user attempted to launch a plugin that was compiled for Java 1.6, but run on Java 1.5, it tries very hard to convert the classes to be usable on Java 1.5 nevertheless.

-   There is another optical illusion in macros/grey-squares.ijm now: Adelson's checker illusion. It shows that we cannot trust our perception of absolute gray values. Thanks to Gabriel Landini for improvements of the script, and Daniel James White for the idea.

-   The Exact Euclidean Distance Transform (3D) plugin was added, providing a real exact EDT, still with linear complexity. A signed version is available, too (attaching negative distances to outside pixels).

-   The [Script Editor](/scripting/script-editor) supports bookmarks now.

-   The [3D Viewer](/plugins/3d-viewer) is now actually a 4D Viewer, handling hyperstacks correctly, and was improved in many other ways, too (thanks to Benjamin Schmid and Gabriel Landini).

-   The [3D Viewer](/plugins/3d-viewer) can export any kind of mesh now (thanks to Albert Cardona).

-   The [Anisotropic Diffusion 2D](/plugins/anisotropic-diffusion-2d) plugin was added.

-   The [LSM Toolbox](/formats/lsm) was updated to version 4.0g (thanks to Patrick Pirotte and Jean-Yves Tinevez).

-   The HandleExtraFileTypes class was synchronized with the upstream version, handling more file formats by default (thanks Albert Cardona for a fixup).

-   There is no need for a StartupMacros.txt anymore, so you can create/modify it without making the Fiji Updater report it as "Locally modified". Thanks Ilan Tal for the suggestion.

-   [View5D](/plugins/view5d) was updated to version 1.2.17, thanks to Rainer Heintzmann and Jean-Yves Tinevez.

-   The [Find Connected Regions](/plugins/find-connected-regions) plugin was updated, thanks to Mark Longair.

-   The Fiji launcher is no longer a C++ program, but a C program. This results in smaller executables, less requirements when building, and a larger range of supported Linux setups.

-   The [Fiji Updater](/plugins/updater) up-to-date check is no longer run when you call Fiji with an argument (e.g. by Drag 'n Drop of an image onto the Fiji icon). Thanks to Jean-Marc Verbavatz for the suggestion.

-   The [Fiji Updater](/plugins/updater) offers to update Java on Windows and Linux in the Advanced Mode, thanks to one of the rare less-exciting talks at the ELMI meeting.

-   The Java WebStart generator was fixed, and is now run every night.

-   The [SPIM Registration](/plugins/spim-registration) plugin was added, offering multi-angle registration and reconstruction typically needed in Selective Plane Illumination Microscopy (thanks to Stephan Preibisch, Stephan Saalfeld and Pavel Tomancak).

-   [Clojure](/scripting/clojure) was updated to a newer version (thanks to Albert Cardona).

-   clojure-contrib is no longer required, and was therefore removed (thanks to Albert Cardona).

-   The [QuickPALM](/plugins/quickpalm) plugin was added (thanks to Ricardo Henriques).

-   Loads of bugfixes

## Developer-visible changes

-   There are two nightly builds, one including all the submodules, and the other to make sure that Fiji builds using Java 5 (which we are stuck to, because there will not be any Java 6 for MacOSX 10.4, or for 32-bit MacOSX 10.5).

-   The [full javadocs](https://javadoc.scijava.org/Fiji/) are built after the nightly build.

-   Developers can upload new plugins or updates from the [Fiji Updater](/plugins/updater) GUI, if they have the write permissions on the server (includes bug fixes by Mark Longair).

-   Many improvements in the [build system](/develop) (less unnecessary rebuilds, separate output directory, excluding files from a .jar target, etc). Thanks to Jacques Pecreaux, Mark Longair and Curtis Rueden.

-   There is a generic way to define a tool in Java now, fiji.util.AbstractTool, rather than going the awkward way to define a macro that calls back into the Java code (thanks Jean-Yves Tinevez). An example is our [Arrow](/plugins/arrow) Tool.

-   The [Script Editor](/scripting/script-editor) can launch classes outside of plugins/ now.

-   The [Script Editor](/scripting/script-editor) can make .jar files from .java plugins now.

-   The [Script Editor](/scripting/script-editor) can build and launch [plugins](/plugins) from `$FIJI_ROOT/src-plugins/<name>/` now.

-   The [Script Editor](/scripting/script-editor) recognizes errors from the Java compiler and offers to jump to the location of the next/previous error.

-   The [Script Editor](/scripting/script-editor) recognizes exceptions thrown during the execution of a script and offers to jump to the next/previous location in the stacktrace.

-   You can ask the [Script Editor](/scripting/script-editor) to open the [JavaDoc](https://javadoc.scijava.org/) for a given class using {% include bc path='Tools | Open Help on Class...'%}

-   The [WEKA library](/develop/using-weka) is now part of Fiji; the {% include github org='fiji' repo='fiji-compat' branch='master' source='fiji/FijiClassLoader.java' label='FijiClassLoader' %} is now an instance of URLClassLoader just because of that (thanks for Verena Kaynig, Albert Cardona and Ignacio Arganda-Carreras for the prodding).

-   There is an easy way to add a screenshot to be shown on the front page of the Fiji Wiki: {% include bc path='Plugins | Utilities | Fiji | New Fiji Wiki Screenshot'%}.

-   The new [versatile and most generic image processing library](/libs/imglib1) -- fully Open Source! -- was added (thanks Stephan Saalfeld and Stephan Preibisch).

-   [imglib](/libs/imglib1) was improved dramatically (thanks to Stephan Saalfeld, Stephan Preibisch, Larry Lindsey and Curtis Rueden).

-   To use the [imglib](/libs/imglib1), just select the Imglib Plugin item of [Script Editor's](/scripting/script-editor) *Templates* menu.

-   The [Script Editor](/scripting/script-editor) learnt quite a number of functions that are useful when developing plugins written in Java (e.g. opening the sources for a menu item, or opening the directory of the current file upon {% include bc path='File | Open'%}/, or offering to search for the sources of a class).

-   If you have an account on the Fiji Wiki, you can easily add News entries using the {% include bc path='Plugins | Utilities | Fiji | New Fiji News'%} menu item.

-   There is a simple *Object Inspector* for Java objects now, accessible via `fiji.debugging.Object_Inspector.openFrame(label, object)`.

-   The **MediaWikiClient** class is now scriptable.

-   The [Fiji Updater](/plugins/updater) offers developers to see the plugin changes since the latest upload of said plugin.

-   The sources for [Jama](http://math.nist.gov/javanumerics/jama/) are bundled now.

-   Both *plugins/\*.jar* and *jars/\*.jar* are loaded via the {% include github org='fiji' repo='fiji-compat' branch='master' source='fiji/FijiClassLoader.java' label='FijiClassLoader' %} now, which allows *.jar* files from *jars/* to call functions in *.jar* files from *plugins/* (notable exception: *jars/ij.jar* and *jars/Fiji.jar*).

-   You can use the **analyze-dependencies.bsh** script to check dependencies of .jar files, reusing the functionality of the [Fiji Updater's](/plugins/updater) upload functionality.

-   You can make your own "View on Fiji Development" movie, as seen on our [YouTube channel](http://youtube.com/fijichannel), using the combined-gource-video.bsh script (requires {% include github org='dscho' repo='Gource' label='Gource' %}).

-   The [VIB](/plugins/vib-protocol) sources were moved from a submodule directly into `fiji.git`.

-   The sources for plugins and libraries are now expected to live either in submodules, or in `src-plugins/<name>/<package>/<class-name>.java`, where `<name>` is the base name of the resulting *.jar* file.

-   There is a command line interface to the [Fiji Updater](/plugins/updater) now (e.g. run `fiji --jar plugins/Fiji_Updater.jar --list jars/ij.jar` to find out the status of *jars/ij.jar*).

-   [Fiji Build](/develop) allows falling back to the [updater](/plugins/updater) if there is no *precompiled/* file for a not-checked-out submodule.

-   The [Fiji Build](/develop) is more easily called via a public API now.

-   Fiji now has a working implementation of a KD-Tree (thanks to Stephan Preibisch).

-   All submodules' main branches are called 'master' now, thanks to Curtis Rueden.

-   You can include *plugins.config* in `src-plugins/<name>/` directly, instead of using `staged-plugins/<name>.config`.

-   You may link VIB-lib.jar and APLv2-licensed code (such as commons-math) together now, due to a slight license change in VIB-lib.

-   "git diff" shows Java method names in the hunk headers now.

-   You can call '"fiji --compile-and-run /path/to/class.java"' now.

-   You can rebuild the Windows 64-bit launcher on said platform now, using the mingw-w64 compiler (e.g. by running /src/mingw-w64/release-easy.sh in [msysGit](http://msysgit.googlecode.com/) as installed by the net or the full installer).

-   There are functions in *fiji.Main* now to identify and recall AWT components by a "component path" a la "Some Dialog&gt;Panel\[2\]&gt;TextField{Name:}".

-   Fiji can be asked to use the G1 garbage collector available since Java 1.6 Update 20, via the `--gc-g1` option (thanks to Albert Cardona).

-   When developing a in the [Script Editor](/scripting/script-editor), one can see the diff and commit the changes from within the [Script Editor](/scripting/script-editor) now.

-   You can open the source for a class with `fiji --edit class:<class-name>`.

-   There is a maven helper in **bin/maven.sh** now, you can call it from Fakefiles to download maven if necessary, and then run it.

