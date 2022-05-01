---
mediawiki: Make_Fiji_Package
title: Make Fiji Package
project: /software/fiji
categories: [Tutorials]
artifact: sc.fiji:Fiji_Package_Maker
---

The Fiji Packager allows you to bundle an existing Fiji installation so you can share all the plugins and update sites with colleagues. It makes a single archive (.zip, .tar.gz, .tar.bz2 are supported at the moment) from the files in *Fiji.app/*.

After clicking on {% include bc path='Plugins | Utilities | Make Fiji Package'%} (note: there are two {% include bc path='Plugins | Utilities'%} menus because ImageJ 1.x enforces separate submenus for non-core plugins which makes things a little bit confusing), you will be asked for the format and the file name.

After both are specified, the plugin does all the rest, reporting its progress in the status bar.

## Files included in the archive

The packager includes files from the following subdirectories of *Fiji.app/*:

-   images/
-   jars/
-   luts/
-   macros/
-   misc/
-   plugins/
-   retro/
-   scripts/

It also includes the ImageJ launcher and the updater database including the current list of update sites.

 
