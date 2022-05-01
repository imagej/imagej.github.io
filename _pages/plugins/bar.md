---
mediawiki: BAR
title: BAR
categories: [Analysis,Filtering,Image Annotation,Scripting,Segmentation]
doi: 10.5281/zenodo.28838
tags: data analysis,annotation,segmentation,scripts
artifact: com.github.tferr:BAR_
---

**BAR**: A collection of **B**roadly **A**pplicable **R**outines.

The collection contains [Macros](/scripting/macro), [Scripts](/scripting) and Plugins focused on Data Analysis, Image Annotation and Image Segmentation. It is curated using {% include github org='tferr' repo='Scripts#ij-bar' label='GitHub' %} and distributed as an optional [update site](/list-of-update-sites).

## Installation

Run {% include bc path='Help|Update...'%} and choose {% include button label="Manage update sites" %}. Activate the *BAR* checkbox in the alphabetically-sorted list of update sites. Press {% include button label="OK" %}, then {% include button label="Apply changes" %}. Restart ImageJ. That's it. Enjoy BAR!

## Description

BAR files are accessible through a dedicated top-level menu subdivided in task-oriented categories. All routines should be documented on {% include github org='tferr' repo='Scripts' branch='master' path='README.md#ij-bar' label='GitHub' %}.

Some of the scripts have a dedicated documentation page, others feature built-in help, while a handful were deemed too simple to require dedicated instructions. Nevertheless, all files contain useful commentary at the top of the source code file. **Remember:** You can open all the scripts using the [{% include key key='shift' %} key](#OpeningBAR).

### List of BARs

{% include img src="barsnapshot" align="right" caption="Overview of BAR (v1.0.0)" %}

#### {% include github org='tferr' repo='Scripts' branch='master' path='README.md#analysis' label='Analysis' %}

{% include github org='tferr' repo='Scripts' branch='master' path='BAR/src/main/resources/scripts/BAR/Analysis/README.md#log-dog-spot-counter' label='LoG-DoG Spot Counter' %},
{% include github org='tferr' repo='Scripts' branch='master' path='BAR/src/main/resources/scripts/BAR/Analysis/README.md#multi-roi-profiler' label='Multi ROI Profiler' %},
{% include github org='tferr' repo='Scripts' branch='master' path='BAR/src/main/resources/scripts/BAR/Analysis/README.md#multichannel-plot-profile' label='Multichannel Plot Profile' %},
{% include github org='tferr' repo='Scripts' branch='master' path='BAR/src/main/resources/scripts/BAR/Analysis/README.md#multichannel-zt-axis-profile' label='Multichannel ZT-axis Profile' %},
{% include github org='tferr' repo='Scripts' branch='master' path='BAR/src/main/resources/scripts/BAR/Analysis/README.md#smoothed-plot-profile' label='Smoothed Plot Profile' %}

#### {% include github org='tferr' repo='Scripts' branch='master' path='README.md#image-annotation' label='Annotation' %}
{% include github org='tferr' repo='Scripts' branch='master' path='BAR/src/main/resources/scripts/BAR/Annotation/README.md#combine-orthogonal-views' label='Combine Orthogonal Views' %},
{% include github org='tferr' repo='Scripts' branch='master' path='BAR/src/main/resources/scripts/BAR/Annotation/README.md#cumulative-z-project' label='Cumulative Z Project' %},
{% include github org='tferr' repo='Scripts' branch='master' path='BAR/src/main/resources/scripts/BAR/Annotation/README.md#roi-color-coder' label='ROI Color Coder' %}

#### {% include github org='tferr' repo='Scripts' branch='master' path='README.md#data-analysis' label='Data Analysis' %}

{% include github org='tferr' repo='Scripts' branch='master' path='BAR/src/main/resources/scripts/BAR/Data_Analysis/README.md#create-boxplot' label='Create Boxplot' %},
{% include github org='tferr' repo='Scripts' branch='master' path='BAR/src/main/resources/scripts/BAR/Data_Analysis/README.md#create-polar-plot' label='Create Polar Plot' %},
{% include github org='tferr' repo='Scripts' branch='master' path='BAR/src/main/resources/scripts/BAR/Data_Analysis/README.md#distribution-plotter' label='Distribution Plotter' %}, [Find Peaks](/plugins/find-peaks), [Fit Polynomial](/plugins/sholl-analysis#complementary-tools), {% include github org='tferr' repo='Scripts' branch='master' path='BAR/src/main/resources/scripts/BAR/Data_Analysis/README.md#interactive-plotting' label='Interactive Plotting' %}

#### {% include github org='tferr' repo='Scripts' branch='master' path='README.md#image-segmentation' label='Segmentation' %}

{% include github org='tferr' repo='Scripts' branch='master' path='BAR/src/main/resources/scripts/BAR/Segmentation/README.md#shen-castan-edge-detector' label='Shen-Castan Edge Detector' %},
{% include github org='tferr' repo='Scripts' branch='master' path='BAR/src/main/resources/scripts/BAR/Segmentation/README.md#apply-threshold-to-roi' label='Apply Threshold To ROI' %},
{% include github org='tferr' repo='Scripts' branch='master' path='BAR/src/main/resources/scripts/BAR/Segmentation/README.md#clear-thresholded-pixels' label='Clear Thresholded Pixels' %},
{% include github org='tferr' repo='Scripts' branch='master' path='BAR/src/main/resources/scripts/BAR/Segmentation/README.md#remove-isolated-pixels' label='Remove Isolated Pixels' %},
{% include github org='tferr' repo='Scripts' branch='master' path='BAR/src/main/resources/scripts/BAR/Segmentation/README.md#threshold-from-background' label='Threshold From Background' %},
{% include github org='tferr' repo='Scripts' branch='master' path='BAR/src/main/resources/scripts/BAR/Segmentation/README.md#wipe-background' label='Wipe Background' %}

<h4 id="snippets-list">{% include github org='tferr' repo='Scripts' branch='master' path='README.md#snippets' label='Snippets' %}, {% include github org='tferr' repo='Scripts' branch='master' path='/lib#lib' label='BAR lib' %} and {% include github org='tferr' repo='Scripts' branch='master' path='BAR/src/main/resources/tutorials/' label='Tutorials' %}</h4>

Described in [Scripting BARs](#scripting-bars).

#### {% include github org='tferr' repo='Scripts' branch='master' path='README.md#tools-and-toolsets' label='Tools and Toolsets' %}

{% include github org='tferr' repo='Scripts' branch='master' path='Tools/README.md#calibration-menu' label='Calibration Menu' %},
{% include github org='tferr' repo='Scripts' branch='master' path='Tools/README.md#list-folder-menu' label='List Folder Menu' %},
{% include github org='tferr' repo='Scripts' branch='master' path='Tools/README.md#segment-profile-tool' label='Segment Profile' %},
{% include github org='tferr' repo='Scripts' branch='master' path='Tools/README.md#shortcuts-menu' label='Shortcuts Menu' %},
{% include github org='tferr' repo='Scripts' branch='master' path='Tools/README.md#roi-manager-tools' label='ROI Manager Tools' %},
{% include github org='tferr' repo='Scripts' branch='master' path='Tools/README.md#toolset-creator' label='Toolset Creator' %}

<span id="Utilities"></span>
#### {% include github org='tferr' repo='Scripts' branch='master' path='README.md#utilities' label='Utilities' %}
[Commander](#commander)

## Accessing BARs

As with all ImageJ commands, BAR scripts can be accessed in multiple ways: 1) through the {% include bc path="BAR |" %} menu, 2) the [Context Menu](#context-menu), 3) [Keyboard Shortcuts](#keyboard-shortcuts), 3) the *Shortcuts Menu Tool* ({% include bc path="BAR | Tool Installers | Install Shortcuts Menu" %}), that registers frequently used commands in the ImageJ toolbar, 4) by [pressing](#ExpediteAccess) {% include key key='L' %}, or 5) from other [scripts, macros and plugins](#scripting-bars). 
{% capture tip%}
You can open any BAR script by holding {% include key key='Shift' %} while selecting its name from the {% include bc path="BAR |" %} menu. For pre-compiled java plugins, the source code is available through the {% include bc path="About BAR..." %} command.
{% endcapture %}
{% include notice icon="tip" content=tip %}

### Context Menu

{% include img src="transposablebarmenu" align="right" caption="BAR features a neat mechanism that allows BAR commands to shuttle between the main menu bar and the image&#39;s context menu." width=350 %}
{% include bc path="BAR |" %} submenus can be appended to the image's context menu (the menu that pops up when right-clicking on the image canvas) by running {% include bc path="BAR | &lt;Submenu&gt; | Move Menu (Context&lt;&gt;Main)" %}. The transfer is bidirectional: once in the context menu, running the same command will place the submenu back in the main menu bar.

The shuttling mechanism is not permanent, i.e., it will not be remembered across restarts. However, it is macro recordable which means it can be imposed at startup, using the ImageJ macro language. So, e.g., to install {% include bc path="BAR | Segmentation |" %} in the context menu, one would:

1.  Start the Macro Recorder ({% include bc path="Plugins | Macros | Record..." %})
2.  Run {% include bc path="BAR | Segmentation | Move Menu (Context&lt;&gt;Main)" %}
3.  Open the {% include bc path="Edit | Options | Startup..." %} window and paste the string generated by the Macro Recorder into its text area so that ImageJ can run the command at every startup.

It may be wise to allow ImageJ enough time to register all scripts before triggering transfers to the context menu. This can be achieved through the built-in macro function [`wait()`](https://imagej.nih.gov/ij/developer/macro/functions.html#wait). For a slow setup requiring at least 1 second (1000 milliseconds), the pasted code would look something like this:

<center>

<img src="/media/plugins/startupbar.png" width="380"/>

</center>

**Notes**

-   The several {% include bc path="Move Menu (Context&lt;&gt;Main)" %} commands across {% include bc path=" BAR |" %} submenus do not use the same label and are distinguishable by extra trailing spaces. This is intentional because all ImageJ commands must have unique names.
-   Any toolset loaded via the "&gt;&gt;" *More Tools* drop down menu can define its own contextual menu (as detailed in the [ImageJ User Guide](https://imagej.nih.gov/ij/docs/guide/146-21.html#sec:ContextualMenu), the contextual menu is controlled by a macro called *Popup Menu* that gets loaded at startup). To have BARs immediately available when such toolsets are loaded, just append the same `run("Move Menu (Context<>Main)");` call described above for StartupMacros.

### Commander

{% include img src="commanderoverview" align="right" caption="Commander overview (BAR 1.1.2)." width=400 %}
Since the majority of BARs are scripts stored in dedicated files, BAR features Commander ({% include bc path='BAR|BAR Commander...'%}), a keyboard-based file browser that produces filtered lists of directory contents.

It is a productivity tool that applies the principles of the [search bar](/learn#the-search-bar) to file browsing, providing instant access to files just by typing abbreviations of filenames. It serves two purposes: 1) to expedite the opening of files and 2) to produce filtered lists of directory contents. Features include: drag-and-drop support, interaction with native file manager, regex filtering, and a built-in console for common operations.

<i>Console mode</i> is triggered by typing {% include key key='!' %}, which evokes a list of searchable commands so that all file navigation can be done exclusively with the keyboard. Some of these (`cd`, `ls`, `pwd`, etc.) are reminiscent of commands found in most command-line interfaces. Here are some examples:

* To access ImageJ's LUT folder: type `!LUT` and press {% include key key='Enter' %}
* To access all JavaScript [lib files](#lib): type `!LIB` and press {% include key key='Enter' %}, then `.JS`
* To reveal the directory of active image: type `!IMP` and press {% include key key='Enter' %}, then choose {% include bc path='Reveal Path'%}.
* To access Commander's built-in help: type `!HELP` and press {% include key key='Enter' %}
* To extract the paths of all TIFF images in a directory:
    * Drag and drop the desired folder into the Commander list
    * Type `TIF` and press {% include key key='Enter' %}
    * Choose {% include bc path='Print Current List'%} in the Options Menu or press {% include key keys='Control|P' %} ({% include key keys='Command|P' %} in Mac OS).

### Keyboard Shortcuts

You can use {% include bc path="Plugins | Shortcuts | Create Shortcut..." %} to assign hotkeys (e.g., keyboard key that you do not use frequently such as {% include key key='0' %} or {% include key key='F7' %}) to any script registered in the {% include bc path="BAR |" %} menu. These shortcuts will be listed in {% include bc path="Plugins | Shortcuts |" %} and are remembered across restarts.

Alternatively, keyboard shortcuts can be defined in macros that call BAR commands by placing the [shortcut key within square brackets](/scripting/macro#keyboard-shortcuts) at the end of the macro name. Such macros can pass specific options to BAR commands, allowing scripts to run without prompt. Example:

```javascript
macro "Remove Round Structures [0]" {
    run("Wipe Background", "size=100 circ.=0.75-1.00"); // Runs Wipe_Background.ijm with the specified parameters
}
```

As [mentioned](#context-menu), such macros can then be pasted into the text area of {% include bc path="Edit | Options | Startup..." %} so that they can be executed when ImageJ starts up. 
{% capture tip%}
Two other expedite ways of retrieving commands include: 1) Pressing {% include key key='L' %}, the shortcut for the [search bar](/learn#the-search-bar) and 2) Pressing {% include key key='9' %}, the default shortcut for the *Recent Commands* list.
{% endcapture %}
{% include notice icon="tip" content=tip %}== Scripting BARs == Although BARs can be used as standalone commands, the scripts and plugins in BAR become more useful when incorporated into other routines.

You can use BARs as a starting point for your own workflows. Whether you are just looking to automate a simple task or you are an advanced developer, you can use BAR to achieve your analysis goals more easily, by means of Snippets - source code templates - and libs - scripting additions to be shared across routines.

### Snippets

{% capture snippetcreator-caption %}
{% include bc path='BAR|Snippets|NewSnippet...'%} (BAR 1.1.0)
{% endcapture %}
{% include img src="snippetcreator" align="right" caption=snippetcreator-caption width="350" %}
BAR contains a directory, `plugins/Scripts/BAR/Snippets/`, containing multi-language [examples](https://github.com/tferr/Scripts/tree/master/Snippets) that you can customize and recycle in your own scripts. You can, of course, also retrieve code and inspiration from the more complete BARs in the remaining `plugins/Scripts/BAR/` subdirectories. Any script or macro file stored in the *Snippets/*, folder with an underscore `_` in the filename will be listed in {% include bc path="BAR | Snippets |" %}. The {% include bc path="BAR | Snippets |" %} menu contains some utilities to help you manage your scripts:

List Snippets:Prints a table listing all scripts in `plugins/Scripts/BAR/Snippets/`. Files can then be opened in the [Script Editor](/scripting/script-editor) by double-clicking on their filename.\\
New Snippet: A java plugin that speeds up the creation of new scripts, pre-configured to use [BAR lib](#lib).\\
Reveal Snippets:Opens `plugins/Scripts/BAR/Snippets/` in the file browser of the operating system.\\
Search BAR: Searches the contents of BAR files.

{% capture tip%}
BAR provides several utility methods that simplify the creation of [snippets](#snippets) and [BAR lib](#bar-lib) usage. These are documented in the [BAR API](https://tferr.github.io/Scripts/apidocs/) , that can be accessed using {% include bc path='BAR|About BAR...'%}, which also provides links to several online resources including the [ImageJ Search Portal](https://search.imagej.net), [ImageJ Javadocs](https://javadoc.scijava.org) , and the [GitHub documentation](https://github.com/tferr/Scripts#ij-bar) of BAR.
{% endcapture %}
{% include notice icon="tip" content=tip %} <span id="lib"></span>

### BAR lib

{% include github org='tferr' repo='Scripts' branch='master' path='/lib/README.md#lib' label='BAR libs' %} (stored in the */BAR/lib/* directory) are centralized libraries ([BeanShell](/scripting/beanshell), [IJM](/scripting/macro) and [Python](/scripting/jython), etc.) that can be shared across files. These libraries serve as scripting additions to [Snippets](#Snippets) and other routines.

Do you find yourself copy and pasting functions from one file to the other? Do you keep on writing the same lines of code? Do you have some key code written across different languages? Would you like to make side-by-side comparisons of scripting languages? Then, BAR lib is for you.

The idea is quite simple: Reusable functions and methods are written to a lib file that gets loaded at execution time so that it can be called by the running script. {% include bc path="BAR | Snippets | New Snippet..." %} exemplifies how to use these scripting add-ons. Here is a BeanShell example:

```java
// Add BAR/lib to classpath
addClassPath(bar.Utils.getBARDir()); // See https://tferr.github.io/Scripts/apidocs/index.html?bar/Utils.html for details
importCommands("lib/");
// Load BARlib.bsh
BARlib();
// Confirm availability of BARlib
lib = new BARlib();
lib.confirmLoading();
```

Run it in the [Script Editor](/scripting/script-editor) ({% include bc path='File|New|Script...'%}), and you should be greeted by a *"BAR lib successfully loaded"* message. Further details are provided on the {% include github org='tferr' repo='Scripts' branch='master' path='/lib#lib' label='GitHub lib page' %} and on the documentation of the [bar.Utils](https://tferr.github.io/Scripts/apidocs/index.html?bar/Utils.html) class.

### Batch Processors

Some of the scripts included in */BAR/Snippets/* are scripts that apply a [common operation to a directory](/tutorials/apply-operation-to-a-complete-directory). These [batch processors](/scripting/batch) are implemented in different languages and perform the following operations:

1.  Take an input folder specified by the user
2.  Apply a series of operations to individual files of matched extension(s)
3.  Save processed files as TIFF to a dedicated directory, so that no files are overwritten

Typically each of these tasks is handled by separated functions so only the function processing single files needs to be edited. In the {% include github org='tferr' repo='Scripts' branch='master' path='Snippets/Process_Folder_PY.py' label='Python' %} and {% include github org='tferr' repo='Scripts' branch='master' path='Snippets/Process_Folder_IJM.ijm' label='IJM' %} implementation, this processing function is called `myRoutines()`. Note that when editing `myRoutines()` we do not need to worry about opening, closing or saving the image without overriding the original file, because those tasks are already performed by other functions. <span id="ProcessingFunction">

#### Processing Functions

The file-processing function can include your own code, code generated by the Macro Recorder ({% include bc path="Plugins | Macros | Record..." %}), pre-existing snippets or methods/functions defined in a common [BAR lib](#lib) file.

IJM example, running a macro and a python script in the *Snippets/* (another [example below](#IJMlib) exemplifies how to call a macro function from {% include github org='tferr' repo='Scripts' branch='master' path='lib/BARlib.ijm' label='BARlib.ijm' %}):

```javascript
function myRoutines() {
    snippetsPath = call("bar.Utils.getSnippetsDir");
    runMacro(snippetsPath + "MyCoolestMacro.ijm");
    eval("python", File.openAsString(snippetsPath + "Median_Filter.py"));
}
```

Jython example, demonstrating how to 1) load [BAR lib](#lib) (in this case {% include github org='tferr' repo='Scripts' branch='master' path='lib/BARlib.py' label='BARlib.py' %}, using code generated by {% include bc path="Bar | Snippets | New Snippet..." %}) and 2) how to run a Snippet (in this case {% include github org='tferr' repo='Scripts' branch='master' path='Snippets/Median_Filter.py' label='Median_Filter.py' %}):

```python
def myRoutines():
    import sys, ij, bar

    # 1) Call a lib function:
    # 1.1) Extend the search path to /BAR/lib/
    sys.path.append(bar.Utils.getLibDir())
    # 1.2) Import all functions in /BAR/lib/BARlib.py
    import BARlib as lib
    # 1.3) Call a function from the file
    lib.confirmLoading()

    # 2) Run a script directly:
    from org.python.util import PythonInterpreter
    script = bar.Utils.getSnippetsDir() + "Median_Filter.py"
    PythonInterpreter().execfile(script)
```

{% capture tip %}
Note also that there is an [easier](/scripting/batch#option-1---process--batch--macro) (but less flexible) way to [batch process](/scripting/batch) a folder: The built-in {% include bc path="Process | Batch | Macro..." %} [command](/scripting/batch#option-1---process--batch--macro).

In this case, you only need to paste the contents of your `myRoutines()` function into the text area of the command. However, by default, {% include bc path="Process | Batch | Macro..." %} assumes you want to process *all* the files in a directory. If that is not the case, i.e., you want to restrict the processing to certain file types, you will have to use {% include wikipedia title='Regular expression' text='regex'%} to instruct the built-in command on the file extensions to be considered (see [Commander](#commander)'s built-in help for several regex examples). E.g., typing the following in the *File name contains* field of {% include bc path="Process | Batch | Macro..." %}, would restrict processing to `.tif`, `.stk` and `.oib` files (the default extensions specified in the `validExtension()` function of {% include github org='tferr' repo='Scripts' branch='master' path='Snippets/Process_Folder_IJM.ijm' label='Process_Folder_IJM.ijm' %}):
```
(.*(\.(?i)(tif
```
{% endcapture %}
{% include notice icon="tip" content=tip %}

### Example: Batch Randomization of Filenames

The default task of both the Python and IJM implementation of {% include github org='tferr' repo='Scripts' branch='master' path='Snippets/README.md#batch-processors' label='BAR' %} *Process Folder* scripts is filename randomization: 1) They copy images from one folder to another, 2) Rename their filenames using a random string and 3) Log changes to a CSV table (so that id of randomized filename can be traced back to the original file). This approach allows for blind analyses of datasets that are sensitive to user interpretation. Below are the descriptions of {% include github org='tferr' repo='Scripts' branch='master' path='Snippets/Process_Folder_PY.py' label='Process_Folder_PY.py' %} and {% include github org='tferr' repo='Scripts' branch='master' path='Snippets/Process_Folder_IJM.ijm' label='Process_Folder_IJM.ijm' %}.

#### Python
In Python we can use the [https://docs.python.org/library/uuid.html uuid module] to generate a random filename (rational [https://stackoverflow.com/a/10501355 here]). The result is an impressively succinct function:

```python
def myRoutines(image):
    import uuid
    image.setTitle( str(uuid.uuid4()) )
```

In more detail: Pass the active image - an {% include javadoc project="ImageJ1" package="ij" class="ImagePlus" label="ImagePlus" %} object - to `myRoutines()`. Retrieve a random {% include wikipedia title='Universally unique identifier' text='UUID'%} (e.g., `f7dfd6a9-f745-42c2-8874-0af67380c3f5`), convert it to a string, then use that string to rename the image using the {% include javadoc project="ImageJ1" package="ij" class="ImagePlus" anchor="setTitle(java.lang.String)" label="`setTitle()`" %} method in `ij.ImagePlus`.

But because [BAR libs](#lib) already contain such a function, we can just call the `randomString()` function in {% include github org='tferr' repo='Scripts' branch='master' path='lib/BARlib.py' label='BARlib.py' %}, after loading the file:

```python
def myRoutines(image):
    import sys, bar
    sys.path.append(bar.Utils.getLibDir())
    import BARlib as lib
    image.setTitle( lib.randomString() )
```

To log filename changes, we could use the same strategy used for the [IJM implementation](#ij-macro-language). The simplest way to generate a CSV list would be to use ImageJ's Log window:

```python
def myRoutines(image):
    import uuid
    from ij import IJ

    # Remember original filename before changing it
    log_row = image.getTitle()
    # Rename image
    image.setTitle( str(uuid.uuid4()) )
    # Append modified filename to CSV row
    log_row += ", " + image.getTitle()
    # Print row
    IJ.log(log_row)
```

However, we can use the [csv module](http://docs.python.org/library/csv.html) to achieve a more robust implementation:

```python
import csv, os

# Create a CSV table documenting processed files
csvPath = out_dir + "_ProcessedFileList.csv"
csvExists = os.path.exists(csvPath)
csvFile = open(csvPath, 'a')
csvWriter = csv.writer(csvFile)

# Specify column headings
if not csvExists:
    headers = ['Original path','Processed path']
    csvWriter.writerow(headers)
```

As such, we only need to add the following, every time a file is processed:

```python
csvWriter.writerow([old_filename, new_filename])
```

Visit the {% include github org='tferr' repo='Scripts' label='BAR repository' %} to check how the assembled script ({% include github org='tferr' repo='Scripts' branch='master' path='Snippets/Process_Folder_PY.py?raw=true' label='Process_Folder_PY.py' %}) {% include github org='tferr' repo='Scripts' branch='master' path='Snippets/Process_Folder_PY.py' label='looks like' %}.

#### IJ Macro Language

In an ImageJ macro (IJM) we will need to define first a function that produces a random filename. The IJM language does not feature an equivalent to the UUID module used previously in the [Python implementation](#Python). So, we are left with two approaches: 1) call [java.util. randomUUID](http://javadoc.imagej.net/Java8/java/util/UUID.html#randomUUID--) directly, or 2) write an ad-hoc function.

For the former, we take advantage of the IJM language built-in [call()](https://imagej.nih.gov/ij/developer/macro/functions.html#call) function, that calls public static methods in any Java class that ImageJ is aware of:

```javascript
function myRoutines() {
    randomString = call("java.util.UUID.randomUUID");
    rename(randomString);
}
```

or even shorter:

```javascript
rename(call("java.util.UUID.randomUUID"));
```

But discovering which methods can be called by the IJM language may not be trivial. Typically, it will require access to an [IDE](/develop/ides) and some Java experience. So what about writing an ad-hoc function?

The approach used in {% include github org='tferr' repo='Scripts' branch='master' path='Snippets/Process_Folder_IJM.ijm' label='Process_Folder_IJM.ijm' %} is the following: 1) Take a template string containing the characters A-Z and digits 0-9; 2) Pick a random position between the first and last character of the string template. Extract the character at that position; 3) Repeat the last step several times, assembling extracted characters into a concatenated string:

```javascript
function randomString() {
    // We define the template and measure the number of positions
    template = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    nChars = lengthOf(template);
    // We define an empty string that will hold the result
    string = "";
    // We will want a final string to be 10-characters long
    for (i=0; i<10; i++) {
        // Define a random position between 0 and the penultime character in template
        idx = maxOf(0, round(random()*nChars-1));
        // Extract and concatenate characters
        string += substring(template, idx, idx+1);
    }
    // return result
    return string;
}
```

This would create e.g., `NHH6KG30C9`. However, a lengthier filename may be required. Larger filenames would be harder to read, so we can insert hyphens at fixed positions. We will improve the function by passing two arguments to it: the length of the desired filename and a boolean flag to instruct on the usage of hyphens:

```javascript
function randomString(length, spacers) {
    template = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    nChars = lengthOf(template);
    string = "";
    for (i=0; i<length; i++) {
        idx = maxOf(0, round(random()*nChars-1));
        string += substring(template, idx, idx+1);
        if (spacers && i%5==0) string += "_";
    }
    return string;
}
```

As such, calling `randomString(50, true)` would produce e.g., `E_ZXTQO_8E9XM_45WG7_8S39`. As with the [Python](#Python) implementation, we could also use [BAR lib](#lib) (in this case {% include github org='tferr' repo='Scripts' branch='master' path='lib/BARlib.ijm' label='BARlib.ijm' %}). First, we need to load the file [before running our macro](#faq:ijm-lib), using the code generated by {% include bc path="Bar | Snippets | New Snippet" %}:<span id="IJMlib"></span>

```javascript
libPath = call('bar.Utils.getLibDir') + 'BARlib.ijm';
libContents = File.openAsString(libPath);
call('ij.macro.Interpreter.setAdditionalFunctions', libContents);

// Press 'Run' twice to confirm availability of new additions
confirmLoading();
```

Once `lib/BARlib.ijm` is in memory, the function can be called directly:

```javascript
rename( randomString(50, true) );
```

Now that we are capable of generating a random filename, we just need to monitor filename changes. We could use the [print()](https://imagej.nih.gov/ij/developer/macro/functions.html#print) function (that outputs to the Log window), or create a two-column table describing the changes. Here is how the final {% include github org='tferr' repo='Scripts' branch='master' path='Snippets/Process_Folder_IJM.ijm' label='Process_Folder_IJM.ijm' %} looks like:

```javascript
function myRoutines() {

    // Note that functions can contain other functions
    function randomString(length, spacers) {...}

    // Since we'll be logging filename changes to the Results table, we
    // need to keep track of the table's measurement counter. We'll assume
    // that the Results table was closed when myroutines() was first called
    availableRow = maxOf(0, nResults);
    // Log original filename before changing it
    setResult("Original filename", availableRow, getTitle());
    // Rename image and log changes
    rename(randomString(20, true));
    setResult("Randomized filename", availableRow, getTitle());
}
```

## FAQ

**What is the rationale behind BAR?**\\
The motivation behind bar is quite simple: To collect snippets of code that can be incorporated into any workflow. So rather than performing fully fledged procedures, BARs tend to produce single tasks. The advantages are two-fold: 1) Scripts are easier to understand and maintain and 2) they can be used to complement any other ImageJ add-on, let it be the simplest macro or the most sophisticated plugin.

**Will I find BAR useful?**\\
{% include github org='tferr' repo='Scripts' branch='master' path='README.md#citations' label='Probably' %}. But it is likely that you will need to delve a bit into the [BAR philosophy](#scripting-bars).

**Can I contribute to BAR?**\\
Yes, please do! If you have some suggestions on how to improve it, do {% include github org='tferr' repo='Scripts' branch='master' path='README.md#help' label='let us know' %}.

**Nothing happens when I run a BAR. What's going on?**\\
In a case of premature termination BARs tend to exit rather silently. The best way to have insights on an unexpected error is to run it directly from the [Script Editor](/scripting/script-editor): Open the script by holding {% include key key='Shift' %} while selecting it from the {% include bc path="BAR |" %} menu, press *Run* and have a look at the editors' s console, where all sort of useful messages will be printed to. Do {% include github org='tferr' repo='Scripts' branch='master' path='README.md#help' label='let us know' %} if you have found a bug.

<span id="faq:ImageJ1"></span>**Does BAR work outside Fiji/ImageJ2?**\\
Yes, but with limitations. The original ImageJ will only register scripts saved in the `plugins/` folder or on one of its immediate subfolders. For this reason, some of the {% include bc path='BAR|'%} submenus will appear as empty, and it may not be possible to navigate the *BAR/* directory using menu commands ([Commander](#Commander) could still be used, nevertheless). Another important aspect is that, without access to the [built-in updater](/plugins/updater), you will have to manually update BAR (by monitoring its {% include github org='tferr' repo='Scripts/releases' label='rpository' %}), and to manually install (and update) the dependencies (i.e., third-party plugins and third-party libraries) used by BAR).

**How do I uninstall BAR?**\\
Run the [Updater](/plugins/updater) ({% include bc path='Help|Update...'%}). Choose *Advance Mode* then *Manage update sites*. Deactivate the *BAR* checkbox in the alphabetically-sorted list of update sites. Press *OK*, then *Apply changes*. All BAR files will be deleted. Note that you can install and uninstall BAR as you see fit. See [How to follow a 3rd party update site](/update-sites/following) for more details.

<span id="faq:ijm-lib"></span>**I get an error when I try to load BAR lib (IJM). Why?**\\
Macro functions from a IJ macro [lib](#lib) may only be available once a new instance of the macro interpreter is initiated (this is not the case for other scripting languages). This means you have to call `ij.macro.Interpreter.setAdditionalFunctions` <u>before</u> running your macro. You can test this by running the default macro generated by {% include bc path="BAR | Snippets | New Snippet..." %}:

```javascript
// Load BARlib.ijm
libPath = call('bar.Utils.getLibDir') + 'BARlib.ijm';
libContents = File.openAsString(libPath);
call('ij.macro.Interpreter.setAdditionalFunctions', libContents);
```

The first time you run `confirmLoading();` ImageJ will complain about `confirmLoading` being an undefined identifier, but it will successfully recognize the call the second time you run the code above.

## Citation

BAR scripts can be cited using the DOI associated with the repository:

{% include citation %}

## License

These scripts are free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the [Free Software Foundation](http://www.gnu.org/licenses/gpl.txt). This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
