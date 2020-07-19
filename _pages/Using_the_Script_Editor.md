{{Infobox
| name                   = Script Editor
| software               = ImageJ
| author                 = Johannes Schindelin, Sumit Dubey (Google Summer of Code 2009)
| maintainer             = {{Person|Rueden}}
| source                 = {{GitHub|org=scijava|repo=script-editor|source=org/scijava/ui/swing/script/ScriptEditor.java}}
| released               = 11 Sep 2008
| status                 = active
}}The script editor is an invaluable help when writing scripts in any of ImageJ's supported [[Scripting comparisons|languages]].{{Learn | scripting}}
== Features ==
;Text Editing
* Full undo support
* Auto-indent
* Configurable white-space options

;Programming
* Syntax highlighting
* Output console
* Git integration (file being edited must be part of a [[Git]] repository)
* Language specific [[Script Templates|templates]]
* Find and replace using regex patterns
* Automatic brace highlighting
* Line numbers

;Language specific tools
* Organization of <tt>import</tt> declarations
* Access to online documentation ([http://javadoc.imagej.net Javadocs], [http://imagej.nih.gov/ij/developer/macro/functions.html Built-in Macro Functions])
* Access to source code in <tt>.jar</tt> files

;Interface
* Bookmarks
* Tabs for easy switching between open files
* Navigation shortcuts

== Usage ==
=== Starting the editor ===

To get started, start up the script editor:

[[Image:Script-Editor-new.jpg|500px]]

There is also the keyboard shortcut {{key|[}} (open square bracket) to open the editor.

=== Choosing a language ===

Then choose a language from the language menu:

[[Image:Script-Editor-choose-language.jpg]]

Now you can write your script. In this tutorial, Jython was chosen as scripting language, but the process is really the same for all scripting languages.

[[Image:Script-Editor-first-script.jpg]]

=== Running the script ===

Once you are satisfied with the script, run it.  This does not require saving, but of course you should save your script later when it works.

[[Image:Script-Editor-run.jpg]]

Note that while the script is running, the window title shows the tell-tale ''(Running)''.

You can use all of ImageJ's classes right away.  Here is an example that shows a dialog where the user can input a number.
For details how to  write dialogs in the different scripting languages, see [[Scripting comparisons]]

[[Image:Script-Editor-dialog.jpg]]

== Further reading ==
See the [[Scripting Help]] page for an introduction to scripting. For more information about each specific language, see the Languages section of top right sidebar.

[[Category:Plugins]]
[[Category:Tutorials]]
[[Category:Scripting]]
