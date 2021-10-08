---
title: MacOS
section: Learn:ImageJ Basics:Supported Platforms
---

{% capture macos-caption %}
{% include wikipedia title='Think different' text='Think different' %}.
{% endcapture %}
{% include img src='icons/macos' align='right' width=150 caption=macos-caption %}

{% include wikipedia title='macOS' text='macOS' %} (formerly called Mac OS X, then OS X) is {% include wikipedia title='Apple Inc.' text='Apple' %}'s desktop operating system. It is [the second most common desktop computing platform](https://www.netmarketshare.com/operating-system-market-share.aspx) after [Windows](/platforms/windows). This page details issues specific to using ImageJ and friends on macOS systems.

# Installation

See also the [Java 8](/news/2016-05-10-imagej-howto-java-8-java-6-java-3d) page for OS-X-specific issues.

# Troubleshooting

See also the [Troubleshooting](/learn/troubleshooting) page.

## ImageJ becomes very slow after running for a while

There are several reasons ImageJ can run slowly on macOS.

### Java painting bug

On macOS, older versions of Java 8 (prior to 1.8.0_45)—as well as all versions of Java 7 (including 1.7.0_80)—are extremely slow at displaying images. You should either upgrade to the latest version of Java 8, or revert to Java 6 (see "Frequently Asked Questions" below).

### Window menu bar bug

There is a bug in Java 8 on macOS which causes the application to drastically slow down as many windows are opened and closed over time. Make sure you are using the latest version of Java 8, as well as the latest version of ImageJ.

### App Nap

With macOS version 10.9 "Mavericks" and later, there is an "App Nap" feature which dramatically slows down applications that are not in the foreground. Leave ImageJ in the foreground while it is processing to avoid this issue. (There are also [various](http://osxdaily.com/2014/05/13/disable-app-nap-mac-os-x/) [ways](http://www.cultofmac.com/274396/disable-app-nap-specific-apps-os-x-tips/) to disable App Nap on your machine, but we have not had much success with them. If you find a solution that works, allowing ImageJ to run fast in the background, please [tell us on the forum](http://forum.imagej.net/)!)

## No title bar in file chooser dialogs

On macOS 10.11 "El Capitan" and later, the operating system no longer includes a title bar for file chooser dialogs. See e.g. [this JDK bug](https://bugs.openjdk.java.net/browse/JDK-8136427) discussing the issue.

As a workaround, you can check "Use JFileChooser to open/save" in the {% include bc path='Edit | Options | Input/Output...'%} dialog.

# Frequently Asked Questions

See also the [Frequently Asked Questions](/learn/faq) page.

## How do I run ImageJ with Java 6?

It is unfortunately no longer feasible to install Apple Java 6 on current versions of macOS. However, ImageJ should work OK with Java 8. If you have difficulties, please post on the [Image.sc Forum](https://forum.image.sc/).

At any time, you can verify which Javas are installed on your system using {% include github org='ctrueden' repo='dotfiles' branch='master' path='bin/java-info' label='this script' %}.

## How do I run ImageJ with JavaFX support?

Whether JavaFX is supported on macOS depends on the version of Java that is used. You can check the version of Java packaged with ImageJ2 or Fiji by right-clicking the app and viewing the contents. Then go into the `java/macos` folder. Versions of java starting with jdk1.8.0 should support JavaFX. However, if you see the default upon installation, `adoptopenjdk-8.jdk`, you will not have JavaFX support. In this case, you can add JavaFX support by replacing this will the Azul JDK that comes with JavaFX included as described [here](https://forum.image.sc/t/44030/17). 

{% capture find-jar-for-class-fiji-tip %}
"You can check if you have JavaFX installed using the {% include bc path="Plugins | Utilities | Find Jar for Class" %} command and searching for `javafx.scene.Scene`. If you can't find this class then you don't have JavaFX installed.
{% endcapture %}
{% include notice icon="fiji" content=find-jar-for-class-fiji-tip %}

# Fiji tips

## Accessing Fiji's plugins and macros folders

To access the `plugins` or `macros` folders, set the Finder window to either icons or lists mode, **not** in column mode, and double-click them.

Alternatively, right-click (or {% include key keys='Ctrl|Left Click' %}) the `Fiji.app` and select "Show package contents", to open the folder where the actual `plugins` and `macros` folders are.

## Running Fiji on the command line

Often it is necessary to run Fiji on the command line, e.g. to pass some command-line options. To do so, start a Terminal (in the Finder, {% include bc path="Go | Utilities" %}), and switch to the correct directory using the `cd` command. Note that the application itself is actually a directory called `Fiji.app`. For example, if you installed Fiji into `/Applications` as recommended, do this:
```
cd /Applications/Fiji.app
```
If you unpacked Fiji onto your desktop, do this:
```
cd $HOME/Desktop/Fiji.app
```
Once you switched to the correct directory, start the ImageJ launcher:
```
Contents/MacOS/ImageJ-macosx
```
{% include notice icon="note" content="A backslash (`\`) is not the same as a slash (`/`). So: `Contents\MacOS\ImageJ-macosx` will **not** work." %}

Now you can pass, say, [Java Options](Java_Options):
```
Contents/MacOS/ImageJ-macosx -verbose:gc --
```
{% include notice icon="note" content="To distinguish between options intended for Java and options intended for ImageJ, you need to separate the former from the latter with a double-dash: `--`. Since the default is to accept ImageJ options, you have to pass a trailing double-dash if you want to pass only Java options." %}

## macOS keyboard shortcuts

It is often helpful to use keyboard shortcuts when using ImageJ. There are also operating system specific shortcuts which can be quite helpful. For example, pressing {% include key keys='Command|Tab' %} and releasing first only the {% include key key='Tab' %} key will allow you to cycle through the running applications, while {% include key keys='Command|\`' %} will do the same for the windows opened by the current application. [Dave Polaschek](http://davespicks.com/) has [a comprehensive list](http://davespicks.com/writing/programming/mackeys.html).
