---
title: Uploading plugins
---

{% include warning/outdated %}

{% include notice icon="note" content="Please make sure that you have a clean build of the plugin you try to upload. You can ensure a clean build by calling the [Fiji Build System](/develop) with the `-clean` suffix before building the actual target. Example:

```
./Build.sh plugins/Fiji_Plugins.jar-clean
./Build.sh plugins/Fiji_Plugins.jar
```
" %}

## The graphical way (recommended)

You can use the [Fiji Updater](/plugins/updater) to upload new plugins (or new versions thereof). First start {% include bc path='Help | Update Fiji'%}. It will tell you that there are *locally modified files*:

<figure><img src="/media/develop/updater-locally-modified.png" title="Updater-locally-modified.png" width="600" alt="Updater-locally-modified.png" /></figure>

Please make sure that there are <u>no</u> updateable files, lest you overwrite new versions with old ones. If that is the case, the *Updater* will automatically switch to the *Advanced Mode* and show you the *locally modified files*. By clicking on the *Locally modified*, you can choose to upload one or more files:

<figure><img src="/media/develop/updater-select-upload.png" title="Updater-select-upload.png" width="750" alt="Updater-select-upload.png" /></figure>

{% include notice icon="note" content="If you want to upload a new file, i.e. a file Fiji does not know anything about yet, you have to switch to *Advanced Mode* yourself and select the view option *View non-Fiji plugins only*." %}

Please make sure that the information in the *Details* is correct; you can edit it by clicking into the text and modifying it in-place.

Please make sure also that the files you are about to upload are clean. You should also use the *Show changes* button for an extra check -- in the top part, you will see information about changed and local-only/remote-only contents of the *.jar* file.

Once everything is ready for upload, just click the button *Upload to Server*.

{% include notice icon="note" content="You will need to have an account on [fiji.sc](/contribute/funding) which is in the group *updaters*, and you will only be offered the upload option by the Updater if you work from a working directory with source files." %}

## Internals

The original [Fiji Updater](/plugins/updater) was very limited; it only allowed to download new versions of files, and it did not have an option to determine whether a local version was previously installed via the Updater or not.

However, it already set the scene for the current Updater, as many people happily used the old one.

These are the building blocks of the Fiji Updater:

### Checksumming

File versions are identified by a cryptographic hash of the file contents, and possibly the file name.

Two different methods are applied: one for *.jar* files and one for all the other files. For regular files, the file name (without trailing NUL nor line feed character) and the exact file contents are piped into the SHA-1 algorithm. For *.jar* files, the file names of the <u>entries</u> and the exact contents of those files are pushed through the SHA-1 algorithm, one after another.

The reason why *.jar* files are different is that they are really nothing more than glorified *.zip* files, and as such contain timestamps. If those timestamps differ, the *.zip* files differ. So if developer Anne Berlin compiles some plugin in Chicago and developer Dario Espana compiles the same plugin on Fiji, chances are that the timestamps are different, and therefore the `.jar` files, even if they contain the same `*.class` files!

### The database

Originally, the database was stored in the file `current.txt`, which is stored in the `update/` directory of [fiji.sc](/contribute/funding)'s web server. Its format was simply lines in the form

```
<filename> <timestamp> <checksum>
```

and a file was considered updateable when its checksum disagreed with the local checksum and the timestamp of the local file was older than the timestamp in `current.txt`.

The old updater was never meant for anything else than the Fiji launchers, `ij.jar` and *.jar* files in the directories `plugins/`, `misc/`, `retro/` and `jars/`, so it would not even pick up on the fact that it installed a, say, *.py* file, and happily offer it for update <u>again</u>. Therefore, `current.txt` <u>must not</u> contain anything else than files matching said expectations.

The new database is stored in the file `db.xml.gz`, which again is a static file. But -- as the name suggests -- it obeys an extensible XML schema.

This database not only stores the same information as `current.txt`, it can contain arbitrary file names (even including spaces, which is not possible with the former database), store descriptions of the files, have information about the platform, categories and most importantly, it has the checksums of all known previous versions so that we can finally decide whether it is safe to update files or whether they are locally modified and the user should state **explicitly** that it is safe to update.

## File organization

Different file types are stored at different locations in an ImageJ/Fiji installation, where they are picked up by the updater (see the [source code](https://github.com/imagej/imagej-updater/blob/imagej-updater-0.8.1/src/main/java/net/imagej/updater/Checksummer.java#L439-L451) for technical details):

```
 jars/
 retro/
 misc/
   .jar
   .class

 plugins/ (and subfolders)
   .jar
   .class
   .txt
   .ijm
   .py
   .rb
   .clj
   .js
   .bsh
   .groovy
   .gvy

 scripts/
   .py
   .rb
   .clj
   .js
   .bsh
   .m
   .groovy
   .gvy

 macros/
   .txt
   .ijm

 luts/
   .lut

 images/
   .png
   .tif
   .txt

 Contents/
   .icns
   .plist

 lib/
 mm/
 mmautofocus/
 mmplugins/
   (all files)
```

The updater will only pick up files stored at the appropriate location according to their function. In addition, the `./lib/` folder contains platform-specific sub-directories to allow loading of native libraries dependent on the platform:

```
 lib/
   linux32/
   linux64/
   macosx/
   win32/
   win64/
```

Further information is in this [thread on fiji-devel](https://groups.google.com/g/fiji-devel/c/QbY4XnLC-wE)

## The actual files

The files corresponding to the database entries are also stored as flat files of the form

```
<relative path>-<timestamp>
```

in the same directory as the databases. The *relative path* refers to the path inside the Fiji directory, e.g. `plugins/Fiji_Updater.jar`.


