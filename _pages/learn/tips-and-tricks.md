---
title: Tips and Tricks
section: Learn:ImageJ Basics
nav-links: true
---

ImageJ is easy to use, but sometimes you wish for some function that is actually implemented, yet you do not know how to trigger. This page lists a few of those tricks.

## Show the memory consumption

Just click on the [status bar](/learn#the-main-window), and you will see how much memory is used, and how much memory is available.

## Execute external programs

The macro language allows executing programs, and capturing their output:

```javascript
output = exec("dir /w");
```

## Quickly see return values

You do not need to wrap macro calls into write() calls: if you just write something like

```javascript
getDirectory("plugins");
```

the return value will appear in your Log window when called.

## Find out in which menu (or .jar file) a certain command is

Hit {% include key keys='Ctrl|L' %} to use the [search bar](/learn#the-search-bar). Type (part of) the name of the entry, then click on *Show full information*.

If *{% include bc path='Edit | Options | Misc...'%}&gt;Require command key for shortcuts* is *un*checked, typing {% include key key='L' %} is sufficient.

## Put the main window to the foreground

Pressing the {% include key key='Enter' %} key on any image will bring the main window to the foreground.

## Close all images (without being asked whether to save them)

{% include bc path='Plugins | Utilities | Close All Without Saving'%}

## Set the foreground color

Double-click on the pipette, or press {% include key keys='CtlCmd|Shift|K' %}, or select the menu item {% include bc path='Image | Color | Color Picker...' %}.

## Set the line width

Line selections can have a width larger than one, which also has an effect on line profiles. You can set it by double clicking on the line selection tool, or by calling {% include bc path='Edit | Options | Line Width...'%}

## Quickly copy a ROI from one image to another

Simply activate the image with the desired ROI, then the image you want to put that ROI into, and press {% include key keys='Ctrl|Shift|E' %}. This triggers the {% include bc path='Edit | Selection | Restore Selection'%} which "restores" the selection.
