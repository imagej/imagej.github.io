---
title: QuickTime
section: Learn:ImageJ Basics:File Formats
categories: [Import-Export, Development]
---


The {% include wikipedia title='QuickTime File Format' text='QuickTime movie format'%} is a multimedia container format with extension `.mov`.

QuickTime MOV files come in many flavors, which are known as codecs. Whether you can open an MOV file in ImageJ will depend on several factors, including the codec used to store the movie, which version of which operating system you have, and which ImageJ [plugin](/plugins) is used.

There are several ways to import MOV files into ImageJ, each discussed below.

## Bio-Formats

The [Bio-Formats](/formats/bio-formats) library supports several, but not all, QuickTime codecs. It is written in pure Java, so those codecs will be readable within ImageJ on all platforms (Windows, macOS, Linux, etc.).

The Bio-Formats plugins are bundled with the [Fiji](/software/fiji) distribution of ImageJ.

See the [Bio-Formats QuickTime supported codecs](https://www.openmicroscopy.org/site/support/bio-formats/formats/quicktime-movie.html) page for a list of supported codecs.

## QuickTime for Java

ImageJ has built-in support for MOV files, but only via the {% include wikipedia title='QuickTime for Java' text='QuickTime for Java'%} (QTJ) library, which is Apple's library for reading and writing QuickTime files from Java. QTJ is only available on Windows and macOS platforms, and only when running a 32-bit version of Java. On macOS, this means [using Apple Java 6](/learn/faq#how-do-i-set-up-java-6-on-os-x).

{% include notice icon="warning" content='QuickTime for Java has been deprecated for many years, and Apple is steadily phasing it out. It is likely that it will no longer be possible to use QTJ at all in future operating system versions.

Apple has also deprecated several old codecs (e.g., `mjpb`), with its QuickTime Player application no longer able to read them in current versions of macOS. In general, we strongly encourage scientists *not* to use MOV format for storing scientific image data, since Apple is not committed to maintaining backwards compatibility.' %}

### Enabling QuickTime for Java on macOS

OS X 10.10 (Yosemite) and 10.11 (El Capitan) do not include key files required for running commands like {% include bc path='File | Import | Using QuickTime'%} and {% include bc path='File | Save As | QuickTime Movie'%} that use QuickTime for Java. You can work around this problem by copying the files `QTJava.zip` and `libQTJNative.jnilib`, [available here](https://imagej.nih.gov/ij/download/qt/), into `~/Library/Java/Extensions`, where `~` is your home directory. Yosemite hides the `Library` folder by default, so you will need to open your home folder and check "Show Library Folder" in the {% include bc path='View | Show View Options'%} dialog. Before copying the files, you will need to create the `~/Library/Java` and `~/Library/Java/Extensions` folders.

You can accomplish all of the above by pasting the following command into a running Terminal:

```shell
mkdir -p $HOME/Library/Java/Extensions && for f in QTJava.zip libQTJNative.jnilib; do curl -fsSL https://imagej.nih.gov/ij/download/qt/$f -o $HOME/Library/Java/Extensions/$f; done
```

## FFMPEG

There is an [update site](/update-sites) called FFMPEG which enables support for opening movie files via the {% include wikipedia title='FFMPEG' text='FFMPEG library'%}. This update site ships native libraries, which should work on Windows, macOS and Linux platforms, but not other platforms (AIX, Solaris, etc.).

See the [FFMPEG supported codecs](https://www.ffmpeg.org/general.html#Video-Codecs) page for a list of supported codecs.

## External conversion

You can use a video conversion tool such as [HandBrake](https://handbrake.fr/), [VLC](http://www.videolan.org/), [libav](https://libav.org/), [ffmpeg](https://ffmpeg.org/) or [VirtualDub](http://www.virtualdub.org/) to convert your MOV files into a different format which ImageJ is able to read more easily.
