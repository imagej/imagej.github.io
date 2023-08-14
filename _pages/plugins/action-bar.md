---
title: ActionBar
categories: [Development]
dev-status: Stable
support-status: Active
team-founders: "@mutterer"
doi: 10.6084/m9.figshare.3397603
---

## Overview

This plugin extends ImageJ's graphical user interface. Its purpose is to provide one or many easy to use button bar(s). This type of bars is called 'ActionBar'. It will be a good place to install frequently used items like macros, built-in commands, or user plugins.

{% include notice icon="info" content='Find the latest ActionBar plus documentation <a href="https://doi.org/10.6084/m9.figshare.3397603">here</a>' %}

## Authors

{% include person-list ids="mutterer | dscho | axtimwalde | Michael Schmid | Serge Mazères | lacan | Simon Roussel | landinig" %}.

## Citing

Please cite ActionBar like this:

{% include citation %}

## Description

This plugin extends ImageJ's graphical user interface. Its purpose is
to provide one or many easy to use button bar(s). This type of bars is
called 'ActionBar'. It will be a good place to install frequently used
items like macros, built-in commands, or user plugins. It can turn a
series of plugins into a good looking user interface (see examples).

{% include img src="actionbar.jpeg" title="ABDemo" align="center" %}

Each button can have a name, an icon, and can do **one of three actions
type**:

-   *run a macro string*
-   *hide or show the ImageJ window*
-   *close the current bar*

Of course with the macro language you can run other macros, user or
builtin plugins, javascripts, etc.

### How to add a line of buttons

Each line of buttons should be included between line tags like this:

```
<line>
// add buttons here

</line>
```

### How to add buttons

All buttons are simply described in a basic configuration file. You can
edit this file manually with ImageJ's built-in text editor. Simply add
new buttons there with 5 descriptors for each button :

|            |                                                                                     |
|------------|-------------------------------------------------------------------------------------|
| `<button>` | Declares a new button in your ActionBar.                                            |
| label      | The button's name, display in a tooltip.                                            |
| icon       | The button's icon file which should be in the 'icons' folder.                       |
| bgcolor    | The button's background color 1-8 preset colors or RGB value in the form of #RRGGBB |
| arg        | Is the argument to the button's action                                              |

### Creating an empty config file canvas with icons

Choose "Action Bar" alone from the plugins menu, and you'll be
invited to create your first Action Bar. After that, you can edit the
config file to do real things.

## Customizing your ActionBar(s)

You can customize the default `ActionBarConf.txt` as you like, but you can
also have more than one Action Bar (an idea by {% include person id="landinig" %}). To
achieve that, simply call Action Bar with the reference to the
configuration file of your choice. Here are two ways of doing this:

-   from a macro:
    ```javascript
    run("Action Bar", "/plugins/Morphology/ActionBarMorphoset.txt");
    ```
    see also the example macro provided that starts 3 ActionBars.

-   by installing the Action Bar plugin with different arguments. This
    will make your custom action bar available through a standard menu
    command. You can do this from Plugins/Shortcuts/Install Plugin...,
    or from a macro :
    ```javascript
    run("Install Plugin...", "plugin=Action_Bar menu=Plugins
    command=sampleActionBar shortcut=F1
    argument=/plugins/ActionBar/sampleActionBar.txt");
    ```

-   PATH to the configuration files must be relative to ImageJ startup
    directory (see example)

-   icons should be in the plugins/ActionBar/icons/ folder.

### How to have one or more Action Bars showing at Startup time?

#### Recommended way (since ImageJ v1.49e 2 August 2014)

Go to {% include bc path="Edit|Options|Startup" %}

here, enter the command that starts your ActionBar, eg:

```javascript
run("Action Bar","/plugins/ActionBar/lambda_bar.txt");
```

If your ActionBar file has an underscore in it and is located
in your plugins folder, you should also be able to start it using its
own command, e.g.:

```javascript
run("lambda bar");
```

#### If the StartupMacros file is available

There is an invocation via AutoRun inside the "StartupMacros" file,
which executes all macros residing in `../macros/AutoRun/`. To use this
facility, simply put a macro into this folder ending with `*.ijm` and use
e.g. this one line of code, to start your ActionBar.
```javascript
run("Action Bar", "/plugins/ActionBar/MyNewActionBar.txt");
```

#### For older versions, mainly deprecated

Include an AutoRun macro in StartupMacros.txt:

```javascript
macro "AutoRun" {
    run("Action Bar", "/plugins/Morphology/ActionBarMorphoset.txt");
}
```

{% include notice icon="tip" content="One Action Bar can start others..." %}

### Sticky ActionBars

Defining your Action Bar 'sticky' with the `<sticky>` property, will
allow you to always have your favorite functions next to the active
image window. The following screenshot shows you what it looks like :

Follow [this link for a screencast](https://blip.tv/file/1943257).
Available soon.

## Installation

First download latest version from Download section it in an ActionBar
folder inside the plugins folder. Restart ImageJ.

```
ImageJ/plugins/action_bar201d.jar     Action Bar plugin
ImageJ/plugins/ActionBar/             ActionBar folder for your bars
ImageJ/plugins/ActionBar/icons/       ..icons folder
...
ImageJ/plugins/test_bar.jar           a standalone actionbar file
```

## Advanced usage tips

-   Rainer M. Engel wrote a
    [macro](/howto/working/easily_update_your_actionbar) that can be
    used to update an ActionBar in a comfortable way. Another
    [macro](/howto/working/easily_modify_your_actionbar) makes it easy
    to add/remove rows/columns or for example switch button positions.
-   The "Close AB" command is meant to be called from a macro, to
    programmatically close an action bar. A 'name' should be passed as
    an argument.

## Licence

No licence associated. Citing Action Bar will be apreciated.

## Contact

Contact [Jerome](mailto:jerome.mutterer@ibmp-ulp.u-strasbg.fr) if you
find any bugs or if you'd like to see a feature appear in a new
release.

## Version history

**Starting 2017, I will upload new versions on figshare.**
{% include link-banner url='https://dx.doi.org/10.6084/m9.figshare.3397603' %}

### August 2014

-   Worked around a Fiji change that prevented button icons to be shown.

### January 2014

-   Michael Schmid added code to keep IJ menus alive on Macintosh when
    the Action Bar is activated, and fixed several bugs.
-   use the new `<hideMenus>` feature to block IJ menus from being
    restored.

### March 2013 version
-   Thanks to {% include person id="lacan" %}, ActionBars can be distributed as single jar
    files, so that they can be served through Fiji update sites.

    The jar file should contain: * the action bar config file * a
    plugins.config file referencing the config file like this:
    ```
    Plugins>Test, "Test AB with icons in jar", Action_Bar("jar:file:test_bar.jar!/test.txt")
    ```
    an `icons/` folder with the icons.

-   Suggested by {% include person id="axtimwalde" %} and {% include person id="dscho" %}, action bars
    can carry [BeanShell](/scripting/beanshell) code that will be executed in a single BeanShell
    interpreter, so that you can share variables across buttons.
    ```
    <beanshell> <line>
    <button> label=A arg=<bsh> i=34; </bsh>
    <button> label=B arg=<bsh> i=i*2; print (i); </bsh>
    </line>
    ```

### May 2012 version

-   thanks to Simon Roussel, works with the new toolbar new tool
    positioning to the last free or last slot for IJ version &gt;= 1.46d
    November 2011 version
-   icon attribute is now optional (defaults to *noicon*)
-   Thanks to Serge Mazères (IBPS, FR), added the optional button
    background color attribute.
    <br>&rarr; either use one of 8 preset colors
    ```
    <button> label=test1 bgcolor=1 ...
    ```
    <br>&rarr; or specify RGB color code
    ```
    <button> label=test2 bgcolor=#ff4480 ...
    ```

### March 2011 version

-   Included bug fixes by {% include person id="dscho" %} (package everything in a
    jar file, load example bars from jar file, include editor paster and
    function finder in the same class)

-   Included improved Magic Montage, Code Bar, and several examples.

-   Works in Fiji : save your custom bars in `Fiji/plugins/ActionBar/` as
    a `*.ijm` file with an underscore, and refresh menus. Example: the
    `Fiji/plugins/ActionBar/1_pixel.ijm` should start like this:
    ```javascript
    run("Action Bar","/plugins/ActionBar/1_pixel.ijm"); exit();
    <line> <button> label=1-pixel ...
    ```

-   Some new features :
    * drag and drop actions processes files dropped on the bars
    ```
    ... <DnDAction> file=getArgument(); open(file); run("8-bit"); </DnDAction> ...
    ```

-   Sticky bars buttons can be contextually disabled
    ```
    ... <sticky> <line> <button> <enabled>if (bitDepth==8) return '1'; label=info icon=no arg=run("Show Info..."); </line> ...
    ```

### previous version

* Contains `<sticky>` feature, and Alt-click actionbar removal.

ImageJ Luxembourg 2008 Workshop support material : [mutterer_workshop.pdf](/media/plugins/action-bar/mutterer_workshop.pdf)
