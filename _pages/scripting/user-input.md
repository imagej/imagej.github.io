---
title: User Input
section: Extend:Scripting
---

Even though one could use any Java library to present a graphical user interface (GUI) for a script or plugin, there are mostly two recommended ways to collect input from the user in [ImageJ](/software/imagej) and [ImageJ2](/software/imagej2). Both methods can be used with all [available scripting languages](/scripting#supported-languages), including the [ImageJ macro language](/scripting/macro).

## Script Parameters

{% include notice icon='imagej2' content="Script parameters are a feature of ImageJ2. They will not work with the original ImageJ." %}

<img src="/media/scripting/script-parameters.png" title="fig:Script-parameters.png" width="400" alt="Script-parameters.png" /> 

[Script parameters](/scripting/parameters) are a fast, succinct option to make a GUI in [ImageJ2](/software/imagej2) and beyond. Scripts written using the `#@` parameter syntax can also be consumed by other tools in the [SciJava](/libs/scijava) ecosystem, including [KNIME](/software/knime), [OMERO](/software/omero) and others. They are independent of user interface, meaning alternative GUIs coded in other frameworks—such as [ImageJFX](/software/imagejfx) coded using JavaFX—can also present a GUI for your plugin/script that matches the application.

Each parameter (integer, string input, etc.) corresponds to a user interface element, and is created by using a generic notation in the form `#@ ParameterType variableName` that is put at the top of the script.

There are as many notations/lines as there are items to put in the GUI, and the items are rendered vertically in the resulting interface, in the order of appearance in the code.

See the [script parameters](/scripting/parameters) page for further details.

## GenericDialog

<img src="/media/scripting/multi-column-dialog.png" title="fig:Multi-column-dialog.png" width="300" alt="Multi-column-dialog.png" /> 

The [GenericDialog](/scripting/generic-dialog) class—part of the original [ImageJ](/software/imagej)—offers more flexibility than the [script parameters](/scripting/parameters), including custom layout and buttons, but requires more coding—e.g., successive calls to the plugin do not automatically remember previously entered values. Plugins coded using `GenericDialog` are also not automatically usable in other [SciJava](/libs/scijava) tools such as [KNIME](/software/knime) or [ImageJFX](/software/imagejfx).

See the [generic dialog](/scripting/generic-dialog) page for further details.
