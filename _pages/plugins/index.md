---
mediawiki: Plugins
title: Plugins
section: Extend
categories: [Uncategorized]
---

ImageJ has been extended with thousands of {% include wikipedia title='Plug-in (computing)' text='plugins'%}: special-purpose software components that extend ImageJ's functionality—e.g., by offering additional commands via menu entries.

## Available plugins

{% include notice icon='info' size='large' content='You can browse the [list of available ImageJ extensions](/list-of-extensions).' %}

## Tiers of plugins

There are four tiers of plugins:

1.  Core ImageJ plugins, bundled with the base ImageJ distribution. (more than 1000 as of this writing)
2.  Core Fiji plugins, bundled with the [Fiji](/software/fiji) distribution of ImageJ. (nearly 1000 additional plugins as of this writing)
3.  Plugins installable from an ImageJ [update site](/update-sites).
4.  Additional plugins available from various online sources, which must be manually installed.

## Installing plugins

The ImageJ [Updater](/plugins/updater) is the best way to install and update plugins. Simply [add the update site](/update-sites) containing your plugins of interest, and they will be installed automatically for you. If the plugin is not available via update site, but packaged as *.jar* file, or as unpackaged directory with *.class* files, see [Installing plugins manually](#installing-plugins-manually) below.

## Advanced topics

### Installing plugins manually

If the plugin you want is not distributed via an ImageJ update site, please encourage the plugin's maintainer to do so! Anyone can create a [hosted update site](/update-sites/setup#creating-a-hosted-update-site) on [sites.imagej.net](http://sites.imagej.net/), to easily share and maintain updated plugins.

In the meantime, to install a plugin manually, follow the plugin's installation instructions, if any. The plugin will consist of one or more files which must be downloaded and (typically) placed in ImageJ's `plugins` folder:

-   If the file suffix is `.jar` or `.class` then it is usually enough to simply restart ImageJ after dropping the file into `plugins`.
-   If the file suffix is `.java` then you typically must execute the [Compile and Run](https://imagej.nih.gov/ij/docs/guide/146-31.html#toc-Subsection-31.5) command on the file to first compile it to a `.class`. After running this command once and restarting ImageJ, the plugin will become available in ImageJ's `Plugins` menu.

### User-specific plugins

In addition to looking in the `plugins` folder of ImageJ itself, ImageJ also looks in the `.plugins` folder in the current user's home folder. This is useful if you want to install some of your own plugins without affecting the system-wide ImageJ installation.

### Configuring where ImageJ looks for plugins

Power users may wish to configure exactly which folder(s) ImageJ scans for plugins. The default folder is the `plugins` folder of the ImageJ installation. However, this can be overridden using the `plugins.dir` system property. See the ImageJ website's article [Changing Location of Plugins Directory](https://imagej.nih.gov/ij/docs/menus/plugins.html#dir).

### Multiple plugin directories

For ultimate control, ImageJ also provides support for manually configuring the list of plugin paths, similar to Java's classpath, using the `ij1.plugin.dirs` system property.

E.g.,

-   on 64-bit Linux:
	```shell
	$IJ_DIR/ImageJ-linux64 -Dij1.plugin.dirs=$IJ_DIR/jars:$IJ_DIR/plugins:$HOME/.plugins
	```
-   On macOS:

$IJ_DIR/Contents/MacOS/ImageJ-macosx -Dij1.plugin.dirs=$IJ_DIR/jars:$IJ_DIR/plugins:$HOME/.plugins

-   On 64-bit Windows:
	```shell
	%IJ_DIR%\ImageJ-win64 -Dij1.plugin.dirs=%IJ_DIR%\jars;%IJ_DIR%\plugins;%HOMEDRIVE%%HOMEPATH%\.plugins
	```

Where `$IJ_DIR` (or `%IJ_DIR%` on Windows) is the path to your ImageJ installation.
