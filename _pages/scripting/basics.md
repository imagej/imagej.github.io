---
title: Scripting basics
section: Extend:Scripting
---

## Introduction

[ImageJ2](/software/imagej2) and [Fiji](/software/fiji) utilize the **SciJava scripting framework**, which supports [scripts](/scripting) in [many languages](/scripting#supported-languages). The mechanics — `#@` parameters, script directives, services, the Script Editor — are language-agnostic; only the syntax of the host language changes. This article introduces those mechanics.

Most examples on this page are written in Groovy. They are straightforward to adapt to most other SciJava-supported languages. SciJava scripting is not part of the original [ImageJ](/software/imagej); for ImageJ 1.x macros see the [macro language](/scripting/macro) page and [original ImageJ developer documentation](https://imagej.net/ij/developer/).

{% include notice content="This page is about *writing* scripts. For *running* them from the command line, see [Scripting Headless](/scripting/headless)." %}

## Importing classes, services and functions

A SciJava script can access any class on the application classpath: the [ImageJ](https://javadoc.scijava.org/ImageJ/) and [ImageJ2](https://javadoc.scijava.org/ImageJ2/) APIs, [SciJava](/libs/scijava-common) services, and anything else bundled with [Fiji](/software/fiji) or installed via [update sites](/update-sites). Regular language `import` statements work as usual.

Services (long-lived helper objects provided by [SciJava](/libs/scijava-common) and ImageJ2) are injected into a script using the `#@` notation — the same notation used for user input. For instance, `PrefService` is responsible for storing previously entered values in memory.

```groovy
// Import the PrefService under the variable name pref
#@ PrefService pref

// Assign the currently opened image to variable imp
#@ ImagePlus imp

// Import a class from the original ImageJ
import ij.IJ
```

## Declaring the script language

A script file is normally identified by its extension (`.groovy`, `.py`, `.bsh`, …). Two SciJava directives let a script declare its language explicitly, overriding (or replacing) the extension hint.

### The language shebang

A `#!` line at the top of the script names the language directly:

```python
#!Python
print("Hello from a script declared as Python via shebang")
```

The shebang takes only a language name (or extension). It must appear as the very first line.

### The script directive

The more general `#@script` directive lets a script declare additional module metadata, including its language. The syntax is `#@script(key1=value1, key2=value2, …)`. Supported keys include:

| Key           | Meaning |
|---------------|---------|
| `name`        | Internal name of the script. |
| `label`       | Human-readable label (used in menus). |
| `description` | Longer description (tool-tip text). |
| `language`    | Script language by name or extension (e.g. `"Python"`, `"groovy"`). |
| `menuPath`    | Where the script appears in the menu structure; use `>` as separator. |
| `menuRoot`    | Identifier of the menu the script belongs to. |
| `iconPath`    | Path to an icon shown alongside the menu entry. |
| `priority`    | Module priority: `first`, `extremely-high`, `very-high`, `high`, `normal`, `low`, `very-low`, `extremely-low`, `last`. |
| `headless`    | Hint that the script is safe to run headlessly. Set only if the script makes no explicit AWT/Swing calls. |
| (other)       | Any other key/value pair is stored as a module property. |

Example:

```java
#@script(language="Python", headless=true, menuPath="Image > Import > My Text Importer...")
```

## Operating on images

First we want to learn different ways to select an image and perform an action on it. In the original [ImageJ](/software/imagej), the image is represented by an [`ImagePlus`](https://imagej.net/ij/developer/api/ij/ij/ImagePlus.html) object. The recommended way to select an `ImagePlus` object is to use [Script Parameters](/scripting/parameters):

```groovy
#@ ImagePlus imp
#@ Integer(label='Filter radius',description='The sigma of the gaussian filter.',value=2) sig

print(imp)

import ij.IJ

IJ.run(imp, "Gaussian Blur...", "sigma=" + sig)
```

Script Parameters are placed at the beginning of the script file. If only one `ImagePlus` is used, the front most image is selected. A second Script Parameter is used to get the radius of the gaussion filter. By using `print(imp)` we verify, that an `ImagePlus` object is assigned to the variable.

To perform an operation on the selected image, we use `IJ.run()`. Therefore we have to import the [`IJ`](https://imagej.net/ij/developer/api/ij/ij/IJ.html) class. There are three different versions of the [`run()` method](https://imagej.net/ij/developer/api/ij/ij/IJ.html#run(java.lang.String)) of these we need the one with three parameters. The first parameter is the image to perform the action on, the second parameters defines the action (called **command**) and the last parameter is used to configure the action (here we set the filter radius). The easiest way to find a command is to use the [Recorder](/scripting/macro#the-recorder).

The second approach is similar to how to perform this operation using the [macro language](/scripting/macro):

```groovy
import ij.IJ

imp = IJ.getImage()
sig = IJ.getNumber('Filter radius:', 2)
IJ.run(imp, "Gaussian Blur...", "sigma=" + sig)
```

The first step is to select the front most image by using `IJ`'s method `getImage()`. The second step is to use the method `getNumber()` to show up a dialog to enter the filter radius. Running the filter is the same as in the previous example.

Finally we want to use the [`WindowManager`](https://imagej.net/ij/developer/api/ij/ij/WindowManager.html) to select the front most image:

```groovy
import ij.IJ
import ij.WindowManager

imp = WindowManager.getCurrentImage()
sig = IJ.getNumber('Filter radius:', 2)
IJ.run(imp, "Gaussian Blur...", "sigma=" + sig)
```

This is nearly identical to the use of `IJ.getImage()` and therefore not recommended. The `WindowManager` class contains some useful methods that can be used to select more than one image (e.g. `getImageTitles()` and `getIDList()`.

## Opening images

In ImageJ and ImageJ2, there are several different ways to open images (or more general datasets). We want to introduce some of them.

The first example uses the [`DatasetIOService`](https://javadoc.scijava.org/SCIFIO/io/scif/services/DatasetIOService.html). It is part of [SCIFIO](/libs/scifio), a flexible framework for **SC**ientific **I**mage **F**ormat **I**nput and **O**utput. Two types of image files are opened. The first one is an example image, downloaded from the Internet. The second image can be chosen by the user. Both datasets are displayed using the [`UIService`](https://javadoc.scijava.org/SciJava/org/scijava/ui/UIService.html) that is part of the [SciJava](/libs/scijava) project.

```groovy
#@ DatasetIOService ds
#@ UIService ui
#@ String(label='Image URL', value='https://imagej.net/images/clown.jpg') fileUrl
#@ File(label='local image') file

// Load a sample file from the internet and a local file of your choice.
dataset1 = ds.open(fileUrl)
dataset2 = ds.open(file.getAbsolutePath())
// Display the datasets.
ui.show(dataset1)
ui.show(dataset2)
```

If a script only depends on ImageJ 1.x functionality, one can use the function `IJ.openImage()`. It will return an `ImagePlus` object.

```groovy
#@ String(label='Image URL', value='https://imagej.net/images/clown.jpg') fileUrl
#@ File(label='local image') file

import ij.IJ

// Load a sample file from the internet and a local file of your choice.
imagePlus1 = IJ.openImage(fileUrl)
imagePlus2 = IJ.openImage(file.getAbsolutePath())
// Display the datasets.
imagePlus1.show()
imagePlus2.show()
```

`IJ.openImage()` is based on the class [`ij.io.Opener`](https://imagej.net/ij/developer/api/ij/ij/io/Opener.html). You can use it directly to open images and other files (e.g. text files). The example uses the class [`ij.io.OpenDialog`](https://imagej.net/ij/developer/api/ij/ij/io/OpenDialog.html) to select a file. This is an alternative to the usage of the Scripting Parameter `File`.

```groovy
import ij.io.Opener
import ij.io.OpenDialog

// Use the OpenDialog to select a file.
filePath = new OpenDialog('Select an image file').getPath()
// Open the selected file.
imagePlus = new Opener().openImage(filePath)
// Display the ImagePlus.
imagePlus.show()
```

## ImagePlus, ImageStack and ImageProcessor Conversion

When working with the ImageJ API you will run into the problem that you have e.g. an `ImageProcessor`, but what you need right now is an `ImagePlus`.

To convert one to another use these commands:

```groovy
// ImagePlus to ImageProcessor:
ip = imp.getProcessor()

// ImageProcessor to ImagePlus:
imp = new ImagePlus('title', ip)

// ImagePlus to ImageStack:
stack = imp.getImageStack()

// ImageStack to ImagePlus:
imp = ImagePlus('title', stack)

// ImageStack to ImageProcessor:
ip = stack.getProcessor(nframe)

// ImageProcessor to ImageStack:
stack.addSlice(ip)
```

The following scheme depicts the relations between the different classes. <img src="/media/image-class-hierarchy.png" title="fig:Image_Class_Hierarchy.png" width="600" alt="Image_Class_Hierarchy.png" />

## Loop over ROI in ROI Manager

This small ImageJ macro scriptlet loops over the ROI in the ROI Manager, selecting one at a time.

```ijm
for (i = 0; i < roiManager("count"); i++){
  roiManager("Select", i);
  // do some operation
}
```

In Jython and other scripting languages, you can iterate over the `RoiManager` directly:

```python
from ij.plugin.frame import RoiManager

# Assume a RoiManager is opened
for roi in RoiManager.getInstance():
  print roi
```

## Calling a script from another script

There are different ways to call a script from another script. Generally, the called script is executed in the same thread than the calling script, which means that the calling script will wait that the called script terminates before going on with the rest of the execution.

### Using ImageJ 1.x commands

ImageJ offers the possibility to call a plugin, macro or script within another one.

If the plugin is already part of the Menu, the simple command `run(PluginName, string Arguments)` (or `IJ.run` for other scripting languages) as returned by the macro-recorder will work.

However when one wants to call a home-made local macro that is not part of the ImageJ menu, one uses a different command (see below).

Here the example of a mainMacro calling a subMacro.

- mainMacro
    ```ijm
    IJ.log("Hello world, I'm mainMacro");
    runMacro("C:/structure/temp/subMacro.ijm");
    ```
- subMacro
    ```ijm
    IJ.log("Hello world, I'm subMacro");
    ```
It is also possible to pass arguments to the subMacro, it works similar to the command line execution.

The subMacro needs to use `getArgument()` (or `IJ.imageJ.getArgs` of the ImageJ API) to recover the string of argument passed to it.

- mainMacro
    ```ijm
    IJ.log("Hello world, I'm mainMacro");
    runMacro("C:/structure/temp/subMacro.ijm", "Arg1,Arg2");
    ```

- subMacro
    ```ijm
    Arguments = getArgument()
    IJ.log(Arguments);
    ```

The command `runMacro` works only for ijm macro. To call a script written in another scripting languages, one should use the `runMacroFile(PathToScript, Arguments)` (respectively `IJ.runMacroFile` of the ImageJ API). Still using the `getArgument` to pass the variables from mainScript to subScript.

This first option is however limited to ImageJ 1.x code style, meaning that one cannot use script parameters, or call any service in subScript. Luckily, ImageJ2 also have is own way to call a script within a script.

### Using ImageJ2 commands

One can use the `ScriptService` from SciJava to run a script within a script.

Here the example of a mainScript calling a subScript both in Jython.

- mainScript.py
    ```python
    #@ ScriptService scriptService
    from ij import IJ

    IJ.log("Hello world, I'm mainScript");
    Arguments = ["some_string", "val1", "some_int", 5]
    scriptService.run(r"SomePath/subScript.py", True, Arguments);
    ```

- subScript.py
    ```python
    #@ String (label="some_string") some_string
    #@ Integer (label="some_int") some_int
    IJ.log(some_string)
    IJ.log(str(some_int))
    ```

subScript must use `#@` Script Parameters for the inputs, and mainScript pass the arguments to subScript as a list of `field, value`

## Calling external programs

Similar to the macro language, one can use the `exec` method available via [`java.lang.Runtime`](https://javadoc.scijava.org/Java8/java/lang/Runtime.html) class.

In Jython this looks like:

```python
from java.lang import Runtime

run = Runtime.getRuntime()

# Option 1: provide a single string command
proc = run.exec("someCommand")

# Option 2: Provide a string array of command and argument
proc = run.exec(["someExe", "Arg1", "Arg2"])

# Optionally: wait for the external command to finish before proceeding
proc.waitFor()

# ... do more things ...

print("Done")
```

## Links

-   [ImageJ API examples](/develop/ij1-plugins#imagejs-api)
-   [ImageJ2 tutorials repository](https://github.com/imagej/tutorials/tree/-/howtos/src/main/java/howto)
