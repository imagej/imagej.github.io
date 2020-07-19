{{Learn|scripting}}Even though one could use any Java library to present a graphical user interface (GUI) for a script or plugin, there are mostly 2 recommended ways to collect input from the user in ImageJ. Both methods can be used with all [[Scripting#Supported_languages|available scripting languages]], including the [[Macros|ImageJ macro language]].

== Script Parameters ==

[[File:Script-parameters.png|400px|left]] [[Script parameters]] are a fast, succinct option to make a GUI in ImageJ and beyond. Scripts written using the <code>#@</code> parameter syntax can also be consumed by other tools in the [[SciJava]] ecosystem, including [[KNIME]], [[OMERO]] and others. They are independent of user interface, meaning alternative GUIs coded in other frameworks—such as [[ImageJFX]] coded using JavaFX—can also present a GUI for your plugin/script that matches the application.

Each parameter (integer, string input, etc.) corresponds to a user interface element, and is created by using a generic notation in the form <code>#@ ParameterType variableName</code> that is put at the top of the script.

There are as many notations/lines as there are items to put in the GUI, and the items are rendered vertically in the resulting interface, in the order of appearance in the code.

See the [[script parameters]] page for further details.

== GenericDialog ==

[[File:Multi-column-dialog.png|300px|left]] The [[generic dialog|GenericDialog]] class—part of [[ImageJ1]]—offers more flexibility than the [[script parameters]], including custom layout and buttons, but requires more coding—e.g., successive calls to the plugin do not automatically remember previously entered values. Plugins coded using <code>GenericDialog</code> are also not automatically usable in other [[SciJava]] tools such as [[KNIME]] or [[ImageJFX]].

See the [[generic dialog]] page for further details.
