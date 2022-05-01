---
title: Frequently Asked Questions
section: Learn:ImageJ Basics
nav-links: true
nav-title: FAQ
extensions: ["mathjax"]
---

This page lists answers to the most frequently asked questions.

# Usage

## How do I apply an operation or macro to multiple images?

See the [Batch Processing](/scripting/batch) page.

## What is the largest size image that ImageJ can open?

There is a 2 gigapixel limit when opening and displaying image planes using the original [ImageJ](/software/imagej) user interface's default image viewer. However, one major goal of the [ImageJ2](/software/imagej2) project is to break this limit. ImageJ2 uses the [ImgLib2](/libs/imglib2) library as its data model, which has much larger limits on the number of pixels (theoretically: \~$$ 2^{63} $$ per dimension, up to \~ $$ 2^{31} $$ dimensions, totaling \~$$ 2^{63^{31}} $$ pixels). Hence, you can open larger images using the {% include github org='imagej' repo='tutorials' label='ImageJ2 API' %}. But you will not be able to display them in the user interface yet.

Furthermore, the [SCIFIO](/libs/scifio) library (what ImageJ2 uses for data I/O) supports opening such images on-demand as "cell images" such that blocks are read from disk as you iterate over the image. This is similar to (but more powerful than) ImageJ's virtual stacks feature. In this way, you can write code to process these large images without displaying them.

The [Fiji](/software/fiji) project also includes the [BigDataViewer](/plugins/bdv) (BDV) plugin, which currently functions as an alternative viewer, to display arbitrarily large images backed by ImgLib2. In the future we hope to integrate BDV-driven UI technology more completely into ImageJ2 core. But there are a couple of limitations right now:

1.  BDV was originally designed for large SPIM data; opening large image files more generally currently requires some coding. But we want to change this.
2.  Many ImageJ plugins assume the data is stored in an ImageJ 1.x data structure, which is not what BDV uses. So ["mixing and matching" ImageJ and ImageJ2 functionality](/libs/imagej-legacy) is tricky here. But we are working to lift these restrictions as time goes on.

# macOS

See the [MacOS](/platforms/macos) page.

# Running

## How do I launch ImageJ with a different version of Java?

### On Windows

Install Java 8, and delete or rename the `ImageJ.app\java` and/or `ImageJ.app\jre` folders, if they exist. If this does not result in ImageJ using the expected Java version, check the Environment Variables ({% include bc path='Control Panel | System and Security | System | Advanced Settings | Advanced | Environment Variables' %}) for the variable "JAVA\_HOME". Update or create this variable as needed; its value should be the desired JDK or JRE that you would like to use for ImageJ (for instance: "C:\\Program Files\\Java\\jdk1.8.0\_172"). See also [Java environment variable setup](http://stackoverflow.com/questions/1672281/environment-variables-for-java-installation).

### On macOS

Use the `--java-home` command line option:

    /Applications/ImageJ.app/Contents/MacOS/ImageJ-macosx --java-home \  
    '/Library/Java/JavaVirtualMachines/jdk1.7.0_45.jdk/Contents/Home'

Note: the `--java-home` flag does not support Apple Java installations. Specifying Apple Javas with this flag will give an error message about being unable to find `lib/server/libjvm.dylib`. However, ImageJ will fall back to Apple Java if no other Java installations are available.

In particular, this means that to run Java 6 on the latest macOS versions, you must do ***ONE*** of the following:

-   ***EITHER:*** Remove all installations of Java 7 and Java 8 ([remove the JRE](https://www.java.com/en/download/help/mac_uninstall_java.xml) and [remove all JDKs](http://docs.oracle.com/javase/7/docs/webnotes/install/mac/mac-jdk.html#uninstall)).
-   ***OR:*** Launch ImageJ explicitly using `java`. Here is a sample invocation for Fiji (copy and paste into Terminal):

    export J6="$(/usr/libexec/java_home -v 1.6)"
    export IJ_HOME=/Applications/Fiji.app
    $J6/bin/$($IJ_HOME/Contents/MacOS/ImageJ-macosx --dry-run | perl -pe 's/ -Djava.ext.dirs=.*? -D/ -D/')

See "How do I setup a launcher app" below for instructions on turning this invocation into a Dock icon.

### On Linux

Use the `--java-home` command line option:

    $HOME/ImageJ.app/ImageJ-linux64 --java-home \  
    /usr/lib/jvm/java-7-openjdk-amd64

One downside of doing this is that ImageJ will launch in a separate process, which has some unintuitive side effects. For example, Ubuntu's Unity user interface will not allow you to "Pin to Launcher" in this case...

## How do I setup a launcher app for macOS for running with a different JVM version?

Start Automator and select to create an *Application*. Double-click *Run Shell Script* in the Library/Utilities folder and replace the text content — cat — with the following:

    open -a "Fiji.app" --args --java-home \  
    /Library/Java/JavaVirtualMachines/jdk-11.0.1.jdk/Contents/Home/

Save anywhere you like.

To replace this application's icon, Get Info on your real Fiji, click on the icon on the top left, press {% include key keys="Cmd|C" %}, Get Info on your Fiji Automator app, click the icon, and press {% include key keys="Cmd|V" %}.

You will then see two icons in the dock, the one of the launcher app and the one of Fiji when it's running.

(based on [this](http://superuser.com/a/271697) guide)

## What is this *headless* mode and what do I need it for?

The term *headless* refers to running ImageJ without a graphical desktop, e.g. on a cluster. See the [Headless](/learn/headless) page for more information.

# Installing/Updating

## How can I verify that my ImageJ is really 100% up to date?

ImageJ will report itself as "up to date" as long as all files installed in your ImageJ match the latest versions from the remote update sites. However, there are cases where your ImageJ may report itself as "up to date" but still be missing critical files, or have mismatching versions (e.g., the dreaded [`NoSuchMethodError`](/learn/troubleshooting#nosuchmethoderror-or-noclassdeffounderror)).

To be certain, run {% include bc path='Help | Update...' %}, and click the "Advanced mode" button. Then verify the following View Options:

-   **View uninstalled files only:** Shows files that are available from remote ImageJ update sites, but *not* installed in your ImageJ. Consider changing the "Status/Action" to "/downloads" for these items, especially any `.jar` files that are flagged with "Not installed" status.
-   **View locally modified files only:** Shows files that have been edited locally (i.e., do not match any version from the remote update sites). Consider changing the "Status/Action" to "Update" for these items, especially any `.jar` files that you did not intentionally modify.
-   **View local-only files:** Shows files that are not known at all to the remote update sites. These files were likely added manually (e.g., if you installed additional plugins manually; see "How do I install additional plugins" below). Consider deleting these files if you do not need them, especially any `.jar` files of unknown origin or conflicting file names.

If you flag any changes to be made, press the "Apply changes" to update your ImageJ. And after restarting ImageJ, you might want to run {% include bc path='Help | Update...' %} again to make sure everything looks the way you expect!

## How do I install additional plugins?

If the plugin is published on an [ImageJ update site](/update-sites), you can run {% include bc path='Help | Update' %} then click {% include button label="Manage update sites" %} to enable it. Not only does this install the plugins for you automatically, but you will also be notified of any updates whenever they are released.

Otherwise, you can drag 'n drop the `.jar` files onto the ImageJ window, or use {% include bc path='Plugins | Install Plugin...' %} with .jar, .class and .java files, or copy the plugins to `ImageJ.app/plugins/` and restart ImageJ. See the [walk-through with screenshots](/plugins#installing-plugins).

## How do I downgrade ImageJ?

Downgrading is generally not recommended as a long-term solution, but can be handy to avoid new bugs that crop up.

*If you need to downgrade to avoid a critical bug, please [report that bug](/discuss/bugs) to the developers so that it can be fixed in a future version!*

-   You can change the version of [ImageJ](/software/imagej) used via the {% include bc path='Help | Update ImageJ...' %} menu item. Note that this *only* changes the version of ImageJ itself—not any installed extensions. This command also works in ImageJ2, but only changes the version of the embedded ImageJ 1.x, not all ImageJ2 components.
-   You can [switch to a different version of Java](#how-do-i-launch-imagej-with-a-different-version-of-java).
-   You can [download a Fiji Life-Line version](/software/fiji/downloads#life-line-fiji-versions).

Lastly, if you have not yet upgraded, and have a currently working configuration, you can make a backup copy of your ImageJ folder before upgrading. Then if the upgrade has undesirable consequences, switch back to the old copy.

## My plugin runs fine in the [Script Editor](/scripting/script-editor), but it does not show up in the menus when I install it. What's wrong?

To be picked up as a plugin, the `.jar`'s file name must contain an underscore, and it either needs to contain an appropriate `plugins.config` file or the class name needs to contain an underscore, too.

The safest way to ensure these conventions is to use the {% include bc path='File | Export as .jar file' %} menu item.

## I tried to update ImageJ via {% include bc path='Help | Update' %}, but it throws an exception instead?

Please download a fresh copy from [here](/downloads).

## I updated ImageJ via {% include bc path='Help | Update' %}, and now it does not start anymore!

See [If ImageJ does not start up](/learn/troubleshooting#if-imagej-does-not-start-up) on the Troubleshooting page.

## The Updater always says *Connection refused*. Maybe it does not use the proxy?

Indeed, an earlier version of the Updater does not use your system-wide network proxy settings. You can [download a new ImageJ](/downloads) to receive the fix. Or you can update the Updater manually like this:

-   open the [Script Editor](/scripting/script-editor) with {% include bc path='File | New | Script' %}
-   set the language to *BeanShell* in the {% include bc path="Language" %} menu of the editor
-   paste the following code (and adjust it to match your settings):

    import ij.IJ;

    System.setProperty("java.net.useSystemProxies", "true");
    IJ.run("Update...");

-   run the script via the {% include bc path="Run" %} menu

# Compatibility

## What is the difference between ImageJ and ImageJ2?

[ImageJ](/software/imagej) is an extensible platform for scientific image analysis. [ImageJ2](/software/imagej2) is redesigned from the ground up to meet the same needs, yet engineered with future-proof flexibility to adapt to researchers' growing requirements (new data types, higher dimensionality, huge images, etc...).

## Will ImageJ macros, plugins and scripts still work in ImageJ2?

Yes. We are completely committed to 100% backwards compatibility with the original ImageJ. ImageJ2 includes the latest version of ImageJ "under the hood" so that existing macros, plugins and scripts will still run the same as before.

ImageJ2 user interfaces are just plugins; ImageJ2 runs with the *ImageJ UI* by default. But we have also created a new ImageJ2 user interface modeled after the original ImageJ to a very large extent, with all the same shortcut keys and behaviors whenever possible. Either way, ImageJ2 looks and feels like the original ImageJ, but with a powerful new infrastructure allowing it to process a wider variety of image data more quickly and easily.

## Does ImageJ2 support the ImageJ macro language? Is it deprecated?

Thanks to the {% include github org='imagej' repo='imagej-legacy' label='ImageJ legacy layer' %}, [ImageJ](/software/imagej) [macros](/scripting/macro) will run unchanged in [ImageJ2](/software/imagej2), while also allowing to harness ImageJ2's new parameterized [scripting](/scripting) paradigm—something that was previously not possible with the macro language.

The ImageJ macro language has been extremely useful to many users. However, it has a substantial limitation: its functions are separate from those available from Java and the other scripting languages.

In ImageJ2, the goal is to provide one unified set of functions, which is fully accessible from Java and all scripting languages. Hence, ImageJ2 plugins and scripts are more flexible than [ImageJ](/software/imagej) [plugins](/plugins) and [macros](/scripting/macro). They can run [headless](/learn/headless) on a server, and are accessible from various applications such as CellProfiler, [KNIME](/software/knime), OMERO, and headless from the command line. We would encourage newly developed scripts and plugins to use the ImageJ2 API since it offers these advantages, but the ImageJ API will remain accessible, too.

## Can I call ImageJ API from an ImageJ2 command?

Yes, although it is not recommended. You will lose most of the advantages of ImageJ2 if you embed calls to ImageJ within your command. The original ImageJ is tightly coupled to AWT and hence does not work well headless. For details, see the [Headless](/learn/headless) page.

## Can I call ImageJ2 API from an ImageJ plugin?

Yes, see the [call-modern-from-legacy](https://github.com/imagej/tutorials/blob/d3ff8e818bb26cb4713371878b239b36cb7d4877/howtos/src/main/java/howto/adv/ModernFromLegacy.java) tutorial example.

## How do I find equivalent commands between the ImageJ and ImageJ2 APIs?

[ImageJ1-ImageJ2 cheat sheet](/develop/ij1-ij2-cheat-sheet) is available.

# [Fiji](/software/fiji)

## What is the difference between Fiji and ImageJ?

Fiji is a *distribution* of ImageJ + ImageJ2: it bundles the core application with a curated selection of plugins pre-installed.

## How do I install Fiji?

See [here](/software/fiji/downloads#installation) for instructions.

## How do I install a Fiji plugin into plain [ImageJ](/software/imagej)?

Doing this is not recommended:

-   Fiji plugin authors test their plugins in Fiji, not plain [ImageJ](/software/imagej).
-   An increasing number of plugins use features of [ImageJ2](/software/imagej2), which are not available in the original [ImageJ](/software/imagej).
-   If you install multiple plugins with complex dependency chains in this manner, you may have dependency [version](/develop/architecture#versioning) conflicts. For things to work, you will need to ensure that all the library versions are compatible. The [Fiji maintainers](/contribute/governance) have already solved this problem for the [Fiji](/software/fiji) distribution.

So you could save yourself a lot of pain by using Fiji instead.

That said, you can install a Fiji plugin in a plain ImageJ installation, as long as you copy all its dependencies with it. You can do this as follows:

    git clone git://github.com/fiji/Stitching
    cd Stitching
    mvn dependency:copy-dependencies

Then copy `target/dependency/*.jar` into your ImageJ installation.

You will need [Git](/develop/git) and [Maven](/develop/maven) installed for this to work.

# Interoperability

## How can I call ImageJ from MATLAB, or vice versa?

Use the ImageJ-MATLAB [update site](/update-sites). See the [MATLAB](/scripting/matlab) page for details.

# Development

## Why do I get a `NoSuchMethodError` or `NoSuchClassDefFoundError` when running a rebuilt plugin?

This is most likely caused by version skew, i.e. when an incompatible version of a build dependency is installed. Example: if you build against `mpicbg-1.0.0.jar` and run that plugin in a Fiji which has only installed `mpicbg-0.6.1.jar`, the latter might miss some methods or classes, or even contain incompatible class definitions.

To investigate, you can use `mvn dependency:copy-dependencies` on the command-line (to copy all build dependencies into `target/dependency/`) and then use your favorite Zip tool to look for the class name mentioned in the exception. In Eclipse, you can simply use {% include key keys="ctlcmd|shift|T" %} to look open the respective class; If a recent enough Eclipse is used, and the default settings have not been tampered with, this will start downloading and show the source attached to the dependency.

Once you know which dependency is supposed to contain the class/method, compare the version number of the file(s) in `ImageJ.app/plugins/` and `ImageJ.app/jars/`.

Sometimes, classes are contained in multiple `.jar` files. This is a frequent source of problems e.g. when some developers try to be helpful and include dependencies' classes into their plugin `.jar` files. This is a problem because those class files are naturally not updated when the dependency is installed as a proper, separate `.jar` file and updated. To investigate such issues, use the {% include bc path="Plugins | Utilities | Find Jar For Class" %} command in Fiji, to determine which `.jar` file serves the class you are looking for.

## What is Maven, and why did you pick it?

Maven is a system to build `.jar` files from source code, and to manage dependencies (i.e. it is easy to specify which minimal version of, say, ImageJ is required by the source code).

We picked it because we need a standard way to interact and collaborate with other projects and with each other. For starters, it allows developers to stay with their favorite development environment (Eclipse, Netbeans, IntelliJ, etc).

For details, please refer to our page on [Maven](/develop/maven).

## What is MiniMaven and why did you create it?

Please refer to the [MiniMaven](/develop/minimaven) and [Supported Compilers](/develop/supported-compilers) pages for an explanation.

## How do I create a new ImageJ plugin using Maven?

Please refer to our page on [Maven](/develop/maven).

## How do I upload a new release of an ImageJ plugin?

Please refer to the [Uploading plugins](/develop/uploading-plugins) tutorial.

## How do I upload a new release of a core ImageJ library such as ImgLib?

The same way you do a plugin. But it will upload to the ImageJ update site (you can only upload to one update site at a time, though, see also [this ticket](http://trac.imagej.net/ticket/1468)).

## What is the recommended way to develop in ImageJ?

Over the years we evolved a development style as follows:

-   create a topic branch
-   test as much as you need to be comfortable to merge
-   merge
-   deal with any fall-out

This development style has been adopted by the [ImageJ2 team](/people), with two additions (making the fall-out step much smaller):

-   tests are added as automated regression tests (to be run by the [continuous integration](/develop/travis) whenever new changes were pushed) whenever possible.
-   merges are usually done with `--no-ff`, so that even fast-forwarding branches (i.e. rebased on top of *master*) will get a merge commit in which the branch is described more broadly.

See also [coding style](/develop/coding-style).

## Class loading issue in 3-rd party libraries (e.g. JPPF)

Libraries trying to load resources or classes with the current thread's class loader rather than with IJ's class loader may fail. The solution is to first set the current thread's class loader to the IJ-classloader. This must be done from <u>the same thread</u> that will later call the problematic code:

    Thread.currentThread().setContextClassLoader(IJ.getClassLoader());

## How do I see the source code for a command?

ImageJ is open source; as such, it is possible to inspect the source code for any command, in the interest of transparency and reproducibility.

Here are several ways to do so:

1.  **Using [search.imagej.net](http://search.imagej.net):**
    -   Go to http://search.imagej.net/
    -   Type in your search
    -   Click the GitHub button!
2.  **Using the search bar:**
    -   Press {% include key key='L' %} to focus the search bar.
    -   Type the name of the command.
    -   Press {% include key key='Down' %} to select it.
    -   Click the Source button.
    -   This will open the source in a browser window.
3.  **Using GitHub:**
    -   Using the search bar, locate your command, taking note of the Class column's value.
        -   E.g., if we type "make binary" we see that the class is `ij.plugin.Thresholder`.
    -   Open the relevant project in GitHub:
        -   E.g., for "ij." classes, go to: https://github.com/imagej/ImageJ
    -   Press the {% include key key='T' %} key, and type the name of the file you are looking for.
        -   In the example above, this is Thresholder.java.
    -   You should end up with a hit like: https://github.com/imagej/ImageJ/blob/master/ij/plugin/Thresholder.java.
    -   This method requires that you know in which repository the code lives. However, you can combine it with **search.imagej.net** method above to figure out which repository, then load the code on GitHub, if desired.
4.  **Using the "Open Source for Menu Item" command:**
    -   Run {% include bc path='Plugins | Scripting | Open Source for Menu Item' %}.
        -   Unfortunately, you must select this from the menu, not using the search bar.
    -   Run the command whose source you want to see.
        -   E.g., {% include bc path='Process | Binary | Make Binary' %}.
        -   Again, select it from the menu directly, not using the search bar.
    -   This will open the source in your web browser.

In the future, we plan to make this easier by having one single easy command for viewing the source code.

## What are "external" plugins?

As far as users are concerned, external Fiji plugins are exactly the same as internal Fiji plugins. For developers, ["external plugin"](/develop/git/extract-a-subproject) simply implies that the plugin's source code is maintained in its own source code repository. For example, [TrakEM2](/plugins/trakem2) has been an external Fiji plugin since Fiji's inception.

## Where should I put the jars of my plugin?

If you develop a Fiji plugin, the result will be in the form of one or more jars containing your plugin and possibly third-party libraries that you rely on. To deploy your plugin you put the jars in the plugins/ or jars/ Fiji subdirectories. The general idea is that only the jars directly containing plugin classes go into plugins/. Auxiliary and third-party jars go into jars/. (see [this mail](https://groups.google.com/g/fiji-devel/c/pMe86pY_Kmc/m/vI-hUJyyrUwJ) for more background on this.)

## How can I call ImageJ from my software?

If your software is written in Java, we recommend using [Maven](/develop/maven) to structure your project. You can then add dependencies to portions of ImageJ that are of interest to you. See the {% include github org='imagej' repo='tutorials' label='ImageJ tutorials' %} for examples.

If your software is written in another language such as C or Python, there are [many ways to integrate Java functionality](http://loci.wisc.edu/bio-formats/interfacing-non-java-code). You must choose which one is best for your particular requirements.

To facilitate some use cases, we provide a script for generating a combined bundle of all ImageJ-related JARs in a single [uber-JAR](/develop/uber-jars) library. To use, check out the ImageJ [source code](/develop/source) and execute:

> `mvn -Pdeps package`

For convenience, we provide a build of this combined JAR file (with suffix `-all`) from the latest DEVELOPMENT, UNSTABLE version of ImageJ. This build includes the latest changes on the {% include github repo='imagej' label='master branch of the source repository' %}. It has not been thoroughly tested and may contain new bugs.

In some cases, use of this JAR file is appropriate and convenient; for example, [CellProfiler](http://cellprofiler.org/) uses it to integrate with ImageJ. However, you should consider carefully what would be best for your project; see the [Uber-JAR](/develop/uber-jars) page for further information.

## Does ImageJ work on mobile devices such as Android?

Not yet as an end-user application. But since Android is a Java-based platform, there is hope. One of the [ImageJ2](/software/imagej2) project's central design goals was a better {% include wikipedia title='Separation of concerns' text='separation of concerns' %}, which could make things like an Android version of ImageJ possible. In particular, the [core components of ImageJ2](/software/imagej2#imagej2-is-more-than-just-an-application) are militant in their avoidance of certain Java SE packages not present in the Android version of Java (which is based on Java ME), such as {% include wikipedia title='Abstract Window Toolkit' text='Java AWT' %}.

That said, ImageJ2 has not even been compile-tested yet using an Android SDK, so there are surely many problems which would need to be resolved. In the future, the ImageJ development team hopes to set up some continuous integration surrounding Android. If you are interested in helping drive this effort forward, please see the [`android` tag on the Image.sc Forum](http://forum.imagej.sc/tag/android)!

Another possibility for the future is a client/server version of ImageJ that runs in a web browser using HTML5 and JavaScript, which could include cross-platform support for mobile devices (Android, iPhone, tablets, etc.). Again, much groundwork has been done to make the [ImageJ2](/software/imagej2) core design compatible with such an application, but no one has written the server- or client-side yet. If you are seriously interested in helping to pursue such an application, you might also want to check out the [OMERO](/software/omero) project, which is a client/server application which has some [integration with ImageJ](https://github.com/imagej/imagej-omero).

# Community

## Why is there Fiji when there is already ImageJ? And what is this ImageJ2 about?

The [ImageJ](/software/imagej), [Fiji](/software/fiji) and [ImageJ2](/software/imagej2) projects are very closely related. See [ImageJ Flavors](/learn/flavors) for a thorough breakdown of the differences.

See also:

-   [an ImageJ2 blog post clarifying specifically the relationship between ImageJ and the version used in Fiji](/news/2011-10-05-the-relation-between-imageja-and-imagej)
-   [an ImageJ2 blog post illustrating that we move code from Fiji to ImageJ2 as appropriate](/news/2012-02-01-the-fiji-updater-has-been-integrated-into-the-imagej2-code-base)

In short: we all collaborate, but have slightly different focus, hence the different projects and names.

## How can we be sure that ImageJ, ImageJ2 and Fiji aren't going to diverge or fork over time?

We are working to create an architecture where the programs work together and preserve compatibility. Fiji is just ImageJ with batteries included, and ImageJ2 includes ImageJ as-is for maximum compatibility. Fiji now uses ImageJ2 at its core. Most importantly, all involved developers are strongly dedicated to avoiding divergence—we are working closely together to ensure that ImageJ2 represents a continuation of ImageJ and Fiji, rather than a project fork.

## Would it make sense to merge the ImageJ2 and Fiji projects?

[Fiji](/software/fiji) and [ImageJ2](/software/imagej2) are fundamentally the same software, using the same [launcher](/learn/launcher). So from the standpoint of development effort, the ImageJ2 and Fiji projects have indeed merged. ImageJ2 is the core software, and several pieces of infrastructure originally developed for Fiji have now migrated to ImageJ2 (e.g., the [Updater](/plugins/updater), [Launcher](/learn/launcher) and [Script Editor](/scripting/script-editor) components). At heart, Fiji is just a big collection of life sciences plugins (though "Fijabcolsp" doesn't have quite the same ring to it). In other words, Fiji is just an ImageJ update site ("Fijaius")—and as such, you can obtain a working Fiji installation by downloading ImageJ2, running the updater, and enabling the Fiji update site.

All of that said, we do not want to get rid of the two distinct project names, since people are familiar with both. But we are integrating resources when feasible: e.g., the [ImageJ wiki](/) serves all ImageJ content including Fiji-specific content (which is marked with the Fiji logo). But we want to ensure it is clear that ImageJ is not a life-sciences-specific project, whereas Fiji is. Historically, because Fiji has a life sciences focus, there have been some users who refused to switch from the original [ImageJ](/software/imagej) to Fiji even though Fiji makes users' lives easier in lots of ways. With ImageJ2, we want to avoid such misconceptions.

More effort is still needed to clarify web resources, to explain concisely and clearly where people should go in different circumstances. We also have plans to make bug reporting simpler and easier across the projects.

## This is a Wiki but I cannot edit it! Why?

To make changes, you need [a GitHub account](https://github.com/join). Then you can click the "Edit this page" link at the top right corner of any page.

## The Wiki is lacking documentation about X, Y and Z

Please feel free to enhance the Wiki! We are thankful for all contributions!

## How do I find more information about Command X?

Try searching for the command in [ImageJ's search bar](/learn#the-search-bar), and clicking the {% include button label="Help" %} button. Alternately, check this wiki: you can use its search bar above, or visit the [list of extensions](/list-of-extensions) page, which includes links to many documentation pages of ImageJ's various extensions.

If documentation is missing for the command you're interested in, you can always view the source directly:

1.  Jump to the [search bar](/learn#the-search-bar) (Shortcut: {% include key key='L' %})
2.  Filter to the command you're interested in.
3.  The \`File\` column will tell you the plugin where the desired command is contained.
4.  You can then use this information to find the source code on GitHub - for core [ImageJ](https://github.com/imagej) or [Fiji](https://github.com/fiji) plugins.
5.  From the appropriate project on GitHub, you can find the repository corresponding to the desired plugin.
6.  Finally, you can search for the actual file for the command of interest (Shortcut: {% include key key='T' %}).

As a complete example, if you were interested in the [2D Histogram](/plugins/2d-histogram) command:

-   The [search bar](/learn#the-search-bar) indicates it's located in VIB.jar
-   VIB is a Fiji plugin, so we go to [the VIB repository](https://github.com/fiji/VIB).
-   On GitHub, press {% include key key='T' %}, search for "Histogram", and find [the Histogram 2D](https://github.com/fiji/VIB/blob/master/src/main/java/util/Histogram_2D.java) source.

## I have a problem that is not covered on this page!

If you have an issue that is not mentioned here, you might want to [ask on one of the mailing lists, or via IRC](/discuss), or [enter a bug report](/discuss/bugs).

## How to report issues?

Please see [Report a Bug](/discuss/bugs)' %}. While private mail might seem more desirable sometimes, but it is almost always inferior to the open process we established in ImageJ. For starters, bug reporters are unlikely to know who would be the best person to address the issue.

## I reported an issue, but it is still not fixed! Why not?

[ImageJ](/software/imagej) and its [variants](/learn/flavors) are [open source](/licensing/open-source) community projects. The list of [contributors](/people) is large but many of the people involved are not paid to work on it. We greatly value community contributions and assistance.

There are not many professional developers whose formal jobs include responding to and addressing bug reports. These developers are not paid *solely* to fix bugs—rather, they are working to solve scientific problems and to advance the software's capabilities. And their attention is spread thin across many projects: [ImageJ](https://github.com/imagej), [Fiji](https://github.com/fiji), [SCIFIO](https://github.com/scifio), [SciJava](https://github.com/scijava), [LOCI](https://github.com/uw-loci), [OME](https://github.com/openmicroscopy), [ImgLib2](https://github.com/imglib), [OpenSPIM](https://github.com/openspim), and others.

The organizations above total over 300 source code repositories, many of which have dozens of open issues in their issue trackers. There are also several hundred tickets in the [old ImageJ2 issue tracker](https://imagej.net/tickets/) that were never migrated to GitHub Issues, as well as over a hundred [open issues archived in the Fiji Bugzilla](https://fiji.sc/bug/).

So please understand that just because we have not responded to a bug report, does not mean we are uninterested in fixing it. It's just that we are very busy, and can use all the help we can get!

If you want to increase the chances of your issue being worked on, you can:

-   [Report the issue](/discuss/bugs).
-   Provide a [minimal, complete, verifiable example](http://stackoverflow.com/help/mcve).
-   [Describe what you already tried](http://whathaveyoutried.com/).
-   [Put as much effort into your question](http://stackoverflow.com/help/how-to-ask) as you expect to be put into its response.
-   Consider [debugging](/develop/debugging) the issue yourself and [submitting a fix](/contribute) as a [pull request](https://help.github.com/articles/using-pull-requests).

See the [bug reporting best practices](/discuss/bugs#bug-reporting-best-practices) article for details.

## How do I contribute a bug fix or patch, or propose an idea for a change?

See the [Contributing](/contribute) page!

# Miscellaneous

## Why do you program in Java? Is C++ not much faster?

See the [Philosophy](/develop/philosophy#why-java) page!

## With Oracle buying Sun and Apple deprecating Java, does Java have a future?

Yes. Java is one of the [most popular programming languages](http://langpop.com/) and still one of the top choices for high-performance, cross-platform applications. Oracle is unlikely to attempt to "kill" Java, but even if they tried they probably couldn't—OpenJDK is open source and there is a massive community of Java developers behind it. Now that [Apple is partnering with Oracle and the OpenJDK community](http://www.apple.com/pr/library/2010/11/12openjdk.html), we are likely to see Java on macOS get better, not worse. Java's popularity will eventually wane, but not because of any company's actions now. Rather, as with any programming language, new technologies will emerge and gain popularity, over a course of many years.

## Why does ImageJ still target Java 6?

As of June 2014, around 19% of macOS systems still run version 10.6 Snow Leopard or older [http://www.netmarketshare.com/ 1](http://www.netmarketshare.com/_1). (In December 2013, it was around 25%.) Unfortunately, Apple and the OpenJDK developer community decided to target OS X 10.7 Lion and above for Java 7 and 8. For the time being, to avoid abandoning older machines which cannot be upgraded from Snow Leopard, ImageJ continues to target Java 6.

Furthermore, updating the required version to a newer version of Java would necessitate improvements to the ImageJ [Updater](/plugins/updater) such that it could also update the bundled version of Java, which would be a substantial undertaking. Otherwise, most existing installations of ImageJ would stop working, and those users would need to download ImageJ from scratch again.

See [this mailing list thread](https://list.nih.gov/cgi-bin/wa.exe?A2=IMAGEJ;29652c34.1412) for further details.

## How are you addressing the fact that with increased modularity comes increased complexity?

See the [Philosophy](/develop/philosophy#convention-over-configuration) page!

## How about a version of ImageJ for the web browser, mobile devices, etc.?

While a pure web version of ImageJ would be desirable for a number of reasons, there are several substantial challenges with current technology. In particular, it would be difficult for a Javascript-based ImageJ to maintain compatibility with existing plugins, macros and scripts. For now, our goal is to continue improving the Java version of ImageJ, while remaining cognizant of developments in the web applications domain, to reduce the difficulties of a web version at some future date.

We are developing ImageJ with a careful eye toward modularity, avoiding gratuitous dependencies—particularly on AWT, which is not available on most mobile devices. We hope this approach makes it easier to port ImageJ to additional platforms in the future.

A shorter term pragmatic solution would be an ImageJ web client that connects to a remote server running ImageJ in headless mode, which does the heavy lifting. See also the [OMERO project](http://openmicroscopy.org/info/omero).

## Why is open software vital to science?

See the [Open Source](/licensing/open-source) page!

## Is Java still free and open source? I heard Oracle is charging for Java now!

Java is still free and open source. The only reason to pay Oracle for a Java license is to continue receiving commercial support from Oracle after January 2019 for the *Oracle version of Java 8*. If you use OpenJDK, you are fine. If you use an older version of Oracle Java 8 (such as the one currently shipping with [Fiji](/software/fiji)), you are fine. See [this article](https://medium.com/@javachampions/java-is-still-free-c02aef8c9e04) for details.
