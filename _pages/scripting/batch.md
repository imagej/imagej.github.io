---
mediawiki: Batch_Processing
title: Batch Processing
section: Extend:Scripting:Languages
---

# Overview

A fundamental benefit to creating [scripts and macros](/scripting) in [ImageJ](/software/imagej) is the ability to *reuse* their functionality *on more than one image*. Although this can be done manually, there are multiple ways to easily automate this batch processing.

# General workflow

1.  Create a basic macro/script which operates on the active image or on a single file.
    -   The [macro recorder](/scripting/macro#the-recorder) is an excellent way to generate macro code.
    -   The [Introduction into Macro Programming](/scripting/macro) explains the principles of macro writing.
2.  Apply your macro to a group of images.
    -   These images do not need to be open in ImageJ already—they will be read in as part of the batch process.
    -   See below for details.

# Option 1 - {% include bc path='Process | Batch | Macro...'%}

The fastest way to start batch conversion is via the [{% include bc path='Process | Batch | Macro...'%}](https://imagej.net/ij/docs/guide/146-29.html#toc-Subsubsection-29.12.3) command. This will open a dialog (below) that will allow you to specify an input and output directory. You can select an output file format, and then use the `Add Macro Code` drop-down to generate a macro with the desired functionality.

![](/media/scripting/batchprocess.png)

# Option 2 - Script Template

{% include notice icon="imagej2" content="This section requires ImageJ2." %}

Open the [script editor](/scripting/script-editor), select {% include bc path='Templates | ImageJ 1.x | Batch | Process Folder (ImageJ Macro)'%}. This will generate the following boilerplate:

<img src="/media/scripting/process-folder-ij1.png" width="762"/>

Lines 26 and 27 can now be edited, replaced with the functional macro code you would like to apply to all images of a given type in a folder. Furthermore you can now modify the batch processing logic itself, for example if you need to customize what (if any) output information is saved.

# Option 3 - Batch Processing with Script Parameters

{% include notice icon="info" content='This section is currently being expanded to document the current state of the [SciJava Batch Processor](https://github.com/scijava/batch-processor/). The Batch Processor is a new addition to the SciJava/ImageJ2 framework. If you encounter any issues, please report/ask on the [forum](/discuss).' %}

# See also

-   [{% include bc path='Process | Batch'%}](https://imagej.net/ij/docs/guide/146-29.html#toc-Subsection-29.12) submenu.
-   [Scripting](/scripting) documentation and tutorials.
-   [How to apply a common operation to a complete directory](/tutorials/apply-operation-to-a-complete-directory)
-   [Assign your own keyboard shortcuts](/learn/keyboard-shortcuts#creating-your-own-keyboard-shortcuts)
