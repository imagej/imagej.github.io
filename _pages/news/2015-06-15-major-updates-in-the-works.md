---
title: 2015-06-15 - Major updates in the works
---

In recent months, ImageJ has seen an increasing number of issues relating to application distribution, packaging and deployment.

This summer, the ImageJ team at [LOCI](/orgs/loci) is taking several major steps to bring [ImageJ2](/software/imagej2) and [Fiji](/software/fiji) up to the latest Java packaging and deployment standards.

## The obsolescence of Java 6

Fiji still ships with Java 6. However, Oracle ceased support for Java 6 in February 2013. Java 7 was released on July 28, 2011—almost four years ago. Java 8 was released on March 11, 2014—more than one year ago. An increasing number of people are using Java 8, and many ImageJ plugin developers want to start taking advantage of powerful new Java 8 language features.

The main reason that ImageJ has not already switched over to Java 8 is the OS X platform: Java 7 requires OS X 10.7 "Lion" or later. Users running OS X 10.6 "Snow Leopard" cannot upgrade to Java 7 or 8, and users with sufficiently old Macs cannot upgrade past Snow Leopard because they do not meet the hardware requirements. Hence, an update of ImageJ to require Java 8 would discontinue support for ImageJ on those old Mac machines.

However, at this point in time, there are an increasing number problems relating to Java 6 (especially on OS X—see next section):

-   Users experience hard crashes with Fiji's bundled version of Java 6 (1.6.0\_24), which are avoided by using Java 7 or Java 8.
-   More and more libraries used by ImageJ are updating their version requirement to Java 7 in newer releases. E.g., Jython 1.7.0 now requires Java 7—as such, ImageJ is stuck with Jython 1.5.3 as long as it continues to run using Java 6.

It seems inevitable that ImageJ will need to switch to Java 8 very soon. At minimum, the ImageJ2 and Fiji downloads offered on the [Downloads](/downloads) page will be updated to ship with Java 8 instead of Java 6. And we are strongly considering updating the core ImageJ2 components to simply require Java 8. The ImageJ [Updater](/plugins/updater) will need to be updated to support these changes.

## Java on OS X

The way Java works on OS X has undergone a radical shift. Apple no longer ships their own version of Java, but rather relies on users to install Java themselves, the same as on Windows and Linux. The last version of Apple Java is Java 6, which has been unsupported for over two years now (see above). OS X 10.9 "Mavericks" and OS X 10.10 "Yosemite" do not come with Apple Java 6 preinstalled, and in fact *uninstall* it when upgrading, if it is present. OS X 10.11 "El Capitan" will be the [last OS X release to support Java 6](https://developer.apple.com/library/prerelease/mac/releasenotes/General/rn-osx-10.11/).

Furthermore, there are substantial technical challenges with packaging a Java application that works properly on both Apple Java and OpenJDK (see next section).

## The ImageJ launcher

The ImageJ project currently maintains the ImageJ [Launcher](/learn/launcher) component, which is a complex piece of C code with many layers of case logic intended to support many different OS and Java versions. At the dawn of Fiji in early 2008, there was no suitable cross-platform alternative for launching Java applications. But these days, the story is different: Oracle provides a standard tool called `javapackager` along with a [complete guide for Java application deployment](https://docs.oracle.com/javase/8/docs/technotes/guides/deploy/toc.html). It would greatly simplify continued ImageJ development to use the standard packaging tool, rather than continuing to maintain ImageJ's custom cross-platform launcher.

## Standalone stable downloads of ImageJ2

There are currently no stable downloads for the ImageJ2 project itself—only for the Fiji distribution. We want to change that: the flagship download on the [Downloads](/downloads) page should be vanilla ImageJ2, with the Fiji downloads offered on their own page. The following downloads need to be offered:

-   Application installers and bundles *including* Java runtime—for Windows, OS X and Linux.
-   Application installers and bundles *without* the Java runtime—for Windows, OS X and Linux.
-   Platform-agnostic "portable application" bundle (without the Java runtime), for use on thumb drives, and with other platforms such as Raspberry Pi.

## Deploying ImageJ with industry standard tools

We are having good success packaging ImageJ via [Oracle's Java packaging mechanism](https://docs.oracle.com/javase/8/docs/technotes/guides/deploy/toc.html) as a self-contained application. This relatively new packaging mechanism (part of the JavaFX software suite) lets you deploy Java applications in four different ways:

-   As a self-contained application—i.e., platform native launcher (.exe on Windows, .app on OS X, etc.)
-   As a standalone application—i.e., double-clickable JAR file.
-   As a {% include wikipedia title='Java Web Start' text='Java Web Start'%} application
-   As an embedded web page—i.e., a Java applet.

The **self-contained application** bundles are the most relevant to ImageJ specifically (although all of the above may be useful to various niches of software development). With Java's built-in bundling tools, we will be able to provide:

-   Native .msi installer for Windows, and native .dmg and .pkg installers for OS X
-   A .exe launcher for Windows, and .app bundle for OS X
-   Continued support for Linux
-   Double-clickable JAR file entry point for developers and debugging

With this new deployment scheme, the current ImageJ [Launcher](/learn/launcher) will be retired. ImageJ will lose some features of that launcher, but the change will be worth it to avoid the high maintenance burden we currently incur from thousands of lines of native C code rife with platform-specific case logic. We will provide shell scripts to cover some of the most useful features, such as launching ImageJ in remote debugging mode.

## Java 3D

The [Java 3D](https://java3d.java.net/) library is a great add-on to Java which provides support for 3D visualization and rendering. It is required for the [3D Viewer](/plugins/3d-viewer) plugin in particular. Unfortunately, historically, Java 3D has been distributed separately with its own installer that must modify the Java runtime itself. This scheme meant we could not distribute Java 3D as a simple JAR dependency, unlike other libraries used by ImageJ plugins. And as such, the 3D Viewer developed its own custom installer for Java 3D, to help users get up and running more easily. But the 3D Viewer downloads Java 3D from an external website which has seen an increasing amount of downtime recently, which has prevented users from successfully using the 3D Viewer on new installations, resulting in repeated volleys of bug reports.

Fortunately, in recent years, the [JogAmp](http://jogamp.org/) team has updated Java 3D to use the [JOGL](http://jogamp.org/jogl/www/) library under the hood, and in so doing, solved the deployment issues regarding native libraries needed for JOGL and Java 3D. We have a working prototype of a Java 3D 1.6 prerelease bundled with Fiji, which enables the 3D Viewer to work without the user needing to explicitly install Java 3D into their Java runtime. [https://github.com/imagej/imagej/issues/120 imagej/imagej\#120](https://github.com/imagej/imagej/issues/120_imagej/imagej#120)

## Issue reporting

Fiji ships with a [Report a Bug](/discuss/bugs) plugin that sends a bug report to the Fiji BugZilla. Soon, we will be retiring that system in favor of GitHub Issues for all ImageJ and Fiji components. The "Report a Bug" plugin will be overhauled to send the report to the appropriate component on GitHub Issues, rather than BugZilla. (And as such, instead of the user needing to create a Fiji BugZilla account, they will need to have a GitHub account.) This will help integrate all our issue tracking, as well as seamlessly link to external issue trackers such as the Bio-Formats GH issues tracker. [https://github.com/imagej/imagej/issues/122 imagej/imagej\#122](https://github.com/imagej/imagej/issues/122_imagej/imagej#122)

## Further reading

For a complete list of deployment-related issues we are tackling over the summer, see [the list on GitHub issues](https://github.com/issues?q=label%3Adeployment+is%3Aopen+user%3Abigdataviewer+user%3Afiji+user%3Aimagej+user%3Aimglib+user%3Ascifio+user%3Ascijava+user%3ATrakEM2+).

As you can see, it's going to be a busy summer. We will push hard to have a newer, stronger ImageJ ready to go for [this fall's ImageJ conference](/events/conference-2015)!

 
