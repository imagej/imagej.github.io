---
mediawiki: Updater
title: Updater
categories: [ImageJ2]
artifact: net.imagej:imagej-updater
project: /software/imagej2
---

The purpose of the ImageJ Updater is to keep you up-to-date with all components of ImageJ (or Fiji), i.e. the macros, scripts, plugins and the core components (libraries) needed by the plugins.

As of 2011, the ImageJ Updater can handle [3rd-party update sites](#adding-update-sites), i.e. anybody can set up their own update site which users can follow.

## Automatic Update

The Updater is a mechanism to update individual packages. It is automatically run when all the following conditions are met:

-   ImageJ was just started
-   ImageJ was started without parameters (i.e. no Drag 'n Drop onto the ImageJ icon)
-   ImageJ's files can be updated by the current user
-   There is a network connection

If there were updates since the Updater was run the last time, the user will be asked whether you want to run the Updater now or later:

![](/media/plugins/up-to-date-check.png)

In case you do not want to run the Updater upon startup, you can choose *Never*.

## Starting the Updater explicitly

The Updater can be run via {% include bc path='Help | Update...'%}.

## Easy mode

The Updater has two modes, the *Easy Mode* and the *Advanced Mode*. In the easy mode, you will only see the files that can be updated. The easy mode looks like this:

![](/media/plugins/updater-easy-mode.png)

For technical reasons, a restart of ImageJ is required before the changes take effect. You can read about technical details [here](/develop/uploading-plugins).

### Resolve dependencies

Some plugins require other components to be updated. For example, the [Simple Neurite Tracer](/plugins/snt) needs the [3D Viewer](/plugins/3d-viewer). If you have a locally modified version of the dependency (i.e. the Updater does not know that particular version), the Updater will ask you what to do:

![](/media/plugins/updater-resolve-dependencies.png)

A typical scenario when you can have a locally modified version of a component is when you asked the respective plugin author for a change in a certain component and got a test version that you [installed manually](/plugins#installing-plugins).

You can keep the local version if you are certain that the version you have is new enough to work with the plugin noted under the text *A newer version might be required by*, otherwise you should consider to choose *Update <component>* instead.

## Advanced mode

In the advanced mode, you can see details about the files, choose to skip updating selected components, and search by filename.

Note: in the advanced mode you can also upload plugins to your [update site](/update-sites). The details for each component can be edited by writing below the respective entry. To save the changes, you have to upload the plugin to the server.

<figure><img src="/media/plugins/snapshot-of-the-advanced-mode-of-the-updater.png" title="Snapshot_of_the_Advanced_Mode_of_the_Updater.png" width="750" alt="Snapshot_of_the_Advanced_Mode_of_the_Updater.png" /><figcaption aria-hidden="true">Snapshot_of_the_Advanced_Mode_of_the_Updater.png</figcaption></figure>

## Starting the Updater manually

Just click on the {% include bc path='Help | Update...'%} menu item:

![](/media/plugins/fiji-updater-screenshot.png)

## Adding update sites

If you want to update plugins from other update sites than the principal one, follow [these instructions](/update-sites/following).

You can also [set up and populate your own update site](/update-sites/setup).

## Command-line usage

It is possible to drive the Updater through the command-line option *--update*. If you call that without arguments, it will show you what subcommands are available:

    ./ImageJ-<platform> --update

The simplest usage is to update either single files:

    ./ImageJ-<platform> --update update jars/ij.jar plugins/Simple_Neurite_Tracer.jar

or all files that would be marked for update in the interactive Updater by default:

    ./ImageJ-<platform> --update update

If you configured upload sites, you can also use the command-line version of the Updater to upload files:

    ./ImageJ-<platform> --update upload plugins/My_New_Cool_Plugin.jar

The full list of options available when running ImageJ from command line looks like this:

    Commands:
        diff [ --list-files | --javap | --class-file-diff | --hex-diff ] [<files>]
        list [<files>]
        list-uptodate [<files>]
        list-not-uptodate [<files>]
        list-updateable [<files>]
        list-modified [<files>]
        list-current [<files>]
        list-local-only [<files>]
        list-from-site <name>
        show [<files>]
        update [<files>]
        update-force [<files>]
        update-force-pristine [<files>]
        upload [--simulate] [--[update-]site <name>] [--force-shadow] [--forget-missing-dependencies] [<files>]
        upload-complete-site [--simulate] [--force] [--force-shadow] [--platforms <platform>[,<platform>...]] <name>
        list-update-sites [<nick>...]
        add-update-site <nick> <url> [<host> <upload-directory>]
        edit-update-site <nick> <url> [<host> <upload-directory>]

In order to update from command line using a specific update site (for example the BigDataViewer) use the following command:

    ./ImageJ-<platform> --update add-update-site BigDataViewer http://sites.imagej.net/Pietzsch/

## Bootstrapping the updater

If you do not have ImageJ yet, you can download [bootstrap.js](http://update.imagej.net/bootstrap.js) and run it like this:

    jrunscript bootstrap.js help

This uses the **jrunscript** executable of your Java installation to run the Javascript file tracked in ImageJ's {% include github org='imagej' repo='imagej-updater' branch='master' path='bin/bootstrap.js' label='source code repository' %}.

The `bootstrap.js` script was originally intended to fix broken [Fiji](/software/fiji) installations, and was subsequently enhanced to initialize the updater in an ImageJ 1.x-only directory -- or even from a complete fresh state.

## History

The original updater was written in a frantic week in October 2008 in preparation for the first public [Fiji](/software/fiji) release, to be able to keep Fiji up-to-date.

In the course of one of two successful Google Summer of Code projects, the updater was rewritten from scratch (but in a [backwards-compatible manner](/libs/imagej-legacy)) by Yap Chin Kiet under the mentorship of Mark Longair and Johannes Schindelin in 2009.

Johannes Schindelin got stuck with the maintainership and introduced third-party update sites (a feature that many claimed to desire, though no pinky was harmed by contributing any code) in the course of a very successful [hackathon](/events/hackathons#imagej-hackathons) at the Lawrence Berkeley National Laboratory in October 2010 and another one in February 2011 hosted by [LOCI](/orgs/loci).

As of September 2012, the Fiji Updater has moved to [ImageJ2](/software/imagej2). Details can be found in the announcement: [2012-09-14 - The Updater moved](/news/2012-09-14-the-updater-moved).
