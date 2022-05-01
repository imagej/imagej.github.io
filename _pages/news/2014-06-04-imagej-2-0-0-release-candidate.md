---
title: 2014-06-04 - ImageJ 2.0.0 release candidate
---

Today, the [ImageJ team](/people) is pleased to announce a public release candidate for [ImageJ2](/software/imagej2): version 2.0.0-rc-2. We tested the first release candidate internally, but now is the time to engage the community: please test the second release candidate with your favorite workflows.

Unlike the beta releases during the past two years, this version of ImageJ2 integrates fully with the legacy [ImageJ 1.x](/software/imagej) user interface. Consequently, this version of ImageJ2 really is the same ImageJ you know and love, achieving 100% backwards compatibility with existing ImageJ 1.x plugins, scripts and macros, while still providing access to the redesigned capabilities of ImageJ2. This allows you to keep using ImageJ in familiar ways, while also enabling migration toward more powerful new features as needed.

The [Fiji](/software/fiji) distribution of ImageJ has bundled ImageJ2 for quite some time, so you may already be familiar with some of ImageJ2's features, some of which—such as the [Updater](/plugins/updater) and [Launcher](/learn/launcher)—were originally developed as part of Fiji, now they are part of ImageJ proper. But this release candidate represents the first time Fiji has really been built fully on top of ImageJ2.

## Features of ImageJ2

ImageJ2 provides a wealth of new features and capabilities:

-   The ImageJ Updater makes it simple to keep your ImageJ up to date, and to add new plugins by enabling additional [Update Sites](/update-sites).
-   The ImageJ Updater also makes it simple to publish your own tools based on ImageJ, via [Personal Update Sites](/update-sites/setup#creating-a-hosted-update-site).
-   New and enhanced file format support via the SCIFIO library. There is no need to call a special SCIFIO plugin; it works with commands like {% include bc path="File | Open" %} automatically. Additional import options are available via the {% include bc path="File | Import | Image..." %} command. See the [SCIFIO](/libs/scifio) page of the ImageJ wiki for further details. {% include img align="right" src="/media/news/imagej2-options.png" width="270px" %}
-   New commands:
    -   {% include bc path="Plugins | Debug | Dump Stack" %} for debugging when things {% include wikipedia title='Hang (computing)' text='hang'%}.
    -   {% include bc path="Plugins | Debug | System Information" %} for reporting on versions of installed plugins and libraries.
-   More powerful [Script Editor](/scripting/script-editor) with support for several scripting languages through a generic, consistent scripting framework (see screenshot below).
-   Write parameterized commands and scripts:
    -   Declare typed inputs and outputs with the `@Parameter` annotation and let ImageJ handle the user interaction, avoiding any dependence on the AWT user interface (see example below).
    -   Parameter support for scripts and macros (see section below)
    -   Reusable in many contexts: [KNIME](/software/knime), [CellProfiler](http://www.cellprofiler.org/), [OMERO](http://www.openmicroscopy.org/site/products/omero), headless...
    -   Plugins appear in the menu automatically without `plugins.config` files, and without having to set the `plugins.dir` property to a single directory containing all the .jar files with special naming requirements.
    -   Mix and match ImageJ 1.x and ImageJ2 data structures!

    Example:

```java
import ij.ImagePlus;
import org.scijava.command.Command;
import org.scijava.plugin.Parameter;
import org.scijava.plugin.Plugin;

@Plugin(type = Command.class, menu = "Plugins > Set Image Title")
public class SetImageTitle implements Command {
    @Parameter
    private ImagePlus imp;

    @Parameter
    private String title;

    @Override
    public void run() {
        imp.setTitle(title);
    }
}
```

-   Easy yet powerful plugin concept—stay tuned for a dedicated blog post soon!
-   Use ImageJ2's N-dimensional [ImgLib2](/libs/imglib2)-based data structures (still in beta).

{% include img align="right" src="/media/news/parameterized-macro.png" width="439px" %}

## Enhanced scripting

ImageJ2 comes with a versatile and elegant scripting framework: all languages can be accessed in the same, consistent way. New languages can be supported by implementing script language plugins; the script editor will automatically support such languages. By default, ImageJ supports Beanshell, Javascript, Jython, JRuby, Clojure, ImageJ 1.x macro and Java "as a script language". Experimental alpha versions are available for Scala and native Python.

Similar to commands supporting `@Parameter` annotations asking ImageJ to auto-generate dialogs, scripts support a related concept: By declaring typed variables in commented lines on top of the script, ImageJ (or [KNIME](/software/knime), CellProfiler, OMERO, etc) will be asked to auto-generate the appropriate dialogs when executing the scripts.

Identical to thusly parameterized scripts, it is now also possible to declare in ImageJ 1.x macros what input parameters are required (see the ImageJ2 script editor screenshot on the right with a parameterized macro in action).

## More than just an application

ImageJ2 breaks the "one developer, one machine, one task" paradigm: it is also a modular collection of highly reusable software libraries built on [SciJava](/libs/scijava), using a powerful plugin framework to facilitate rapid development and painless user customization.

The following software component libraries form the core of ImageJ2:

-   {% include github org='imagej' repo='imagej-common' label='ImageJ Common' %} - The core image data model, using ImgLib2.
-   {% include github org='imagej' repo='imagej-ops' label='ImageJ Ops' %} - An extensible framework for reusable image processing algorithms.
-   {% include github org='imagej' repo='imagej-updater' label='ImageJ Updater' %} - A mechanism to update individual plugins and libraries within ImageJ.
-   {% include github org='imagej' repo='imagej-legacy' label='ImageJ Legacy' %} - Provides complete backwards compatibility with ImageJ 1.x.
-   {% include github org='scijava' repo='scijava-common' label='SciJava Common' %} - The core frameworks for plugins, modules, scripting and the application itself.

## How to test the release candidate?

You can either [download the .zip file](https://maven.scijava.org/service/local/repositories/releases/content/net/imagej/imagej/2.0.0-rc-2/imagej-2.0.0-rc-2-application.zip) or just update your Fiji installation: ImageJ 2.0.0-rc-2 is already part of Fiji.

Please send all bug reports to the [ImageJ mailing list](/discuss/mailing-lists). And thank you very much for trying ImageJ2!

 
