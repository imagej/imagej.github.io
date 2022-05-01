---
title: Script Templates
section: Extend:Scripting
project: /libs/scijava
---

Templates are pre-written scripts in a particular scripting language. They can be distributed as any other plugin, and automatically discovered by the [Script Editor](/scripting/script-editor). Templates thus present an excellent way to demonstrate a particular operation to a wide audience of users.

Available templates are sorted by language under the `Templates` menu of the [Script Editor](/scripting/script-editor). The contents of a template will be loaded into the editor window when selected. The script can then be inspected, executed and modified as normal.

# Adding a new template

The [Script Editor](/scripting/script-editor) will automatically search the `script_templates` directory and register any discovered scripts as templates. For example, a [Mavenized](/develop/maven) project could add a sample script in `src/main/resources/script_templates` and it would be packaged into the appropriate location of the resultant `.jar`.

For examples of how the existing templates are structured and distributed, take a look at the [`imagej-legacy` project](https://github.com/imagej/imagej-legacy/tree/master/src/main/resources/script_templates) (which maintains the script templates that were previously shipped with Fiji's script editor) as well as the [`imagej-scripting` project](https://github.com/imagej/imagej-scripting).

# Template best practices

Above all else, templates should be **well documented**. Templates are intended to explain specific functionality in a given language, to users who may have limited experience with the language or programming/scripting in general.

Ideally, a template will be focused on an a single objective (e.g. opening an image, calculating a threshold, operating on a directory, etc...).

It is especially helpful to document how the template can be adapted to meet the user's needs.
