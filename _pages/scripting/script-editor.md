---
title: Using the Script Editor
section: Extend:Scripting
project: /libs/scijava
artifact: org.scijava:script-editor
---

The script editor is an invaluable help when writing scripts in any of the [SciJava](/_pages/libs/scijava.md) framework's supported [languages](comparisons.md).

## Features

Text Editing  

-   Full undo support
-   Auto-indent
-   Configurable white-space options

Programming  

-   Syntax highlighting
-   Output console
-   Git integration (file being edited must be part of a [Git](../develop/git/index.md) repository)
-   Language specific [templates](templates.md)
-   Find and replace using regex patterns
-   Automatic brace highlighting
-   Line numbers

Language specific tools  

-   Organization of `import` declarations
-   Access to online documentation ([Javadocs](https://javadoc.scijava.org/), [ImageJ Macro Functions](https://imagej.nih.gov/ij/developer/macro/functions.html))
-   Access to source code in `.jar` files

Interface  

-   Bookmarks
-   Tabs for easy switching between open files
-   Navigation shortcuts

## Usage

### Starting the editor

To get started, start up the script editor:

<img src="/media/scripting/script-editor-new.jpg" width="500"/>

There is also the keyboard shortcut {% include key key='[' %} (open square bracket) to open the editor.

### Choosing a language

Then choose a language from the language menu:

![Script-Editor-choose-language.jpg](/media/scripting/script-editor-choose-language.jpg)

Now you can write your script. In this tutorial, Jython was chosen as scripting language, but the process is really the same for all scripting languages.

![](/media/script-editor-first-script.jpg)

### Running the script

Once you are satisfied with the script, run it. This does not require saving, but of course you should save your script later when it works.

![](/media/scripting/script-editor-run.jpg)

Note that while the script is running, the window title shows the tell-tale *(Running)*.

{% include warning/importing-classes %}

You can use all of ImageJ's classes right away. Here is an example that shows a dialog where the user can input a number. For details how to write dialogs in the different scripting languages, see [Scripting comparisons](comparisons.md).

![](/media/scripting/script-editor-dialog.jpg)

## Further reading

See the [Scripting overview](index.md) page for an introduction to scripting, and list of available languages, with links to more documentation.
