---
title: Scripting
section: Extend:Scripting
project: /software/imagej2
---

The [ImageJ ecosystem](#terminology) supports scripting in many languages. *Which* scripting system you're using depends on which application you're running.

## Which scripting system?

There are two distinct scripting systems in the ImageJ ecosystem:

{% include icon name="ImageJ" align="left" size="24px" %} **The original [ImageJ](/software/imagej) (1.x)** ships its own scripting support: the [ImageJ macro language](/scripting/macro) plus a few other script languages. For this system, see the [ImageJ developer documentation](https://imagej.net/ij/developer/) on the original ImageJ website. SciJava `#@` [script parameters](/scripting/parameters) are **not** part of the original ImageJ.

{% include icon name="Fiji" align="left" size="24px" %} &nbsp;**[Fiji](/software/fiji)** ships the **SciJava scripting framework**: a cross-language system with [`#@` parameters](/scripting/parameters), the [`#@script` directive](/scripting/basics#the-script-directive), the [`#!Lang` shebang](/scripting/basics#the-language-shebang), a unified [Script Editor](/scripting/script-editor), and many [supported languages](#supported-languages). The rest of this section covers SciJava scripting.

## Terminology

These pages use the following terms consistently:

- **ImageJ** — the original ImageJ 1.x application.
- **ImageJ2** — the [ImageJ2](/software/imagej2) libraries upon which Fiji is built.
- **Fiji** — the Fiji distribution (ImageJ + ImageJ2 + curated plugin set + [Jaunch](https://github.com/apposed/jaunch)-based launcher).
- **SciJava scripting** — the cross-language scripting framework shared by ImageJ2 and Fiji.
- **ImageJ ecosystem** — all of the above, plus other ImageJ-flavored applications.

## Getting started

-   Read the [Scripting basics](/scripting/basics) page for an introduction to writing SciJava scripts.
-   Read the [ImageJ2 tutorial notebooks](/tutorials/notebooks) for runnable examples.
-   Press the {% include key key='[' %} key in Fiji to open the [Script Editor](/scripting/script-editor) (or {% include key key='Shift' %}-{% include key key='[' %} to open the [Script Interpreter](/scripting/interpreter)).
-   Optionally, choose a template from the {% include bc path="Templates" %} menu to get you started.
-   Otherwise, choose your language from the {% include bc path="Language" %} menu.
-   Grab code snippets for common tasks from the [Scripting toolbox](/scripting/toolbox).
-   See [Scripting comparisons](/scripting/comparisons) for a side-by-side comparison of scripting languages.

## Supported languages

Many different languages are supported. The following table summarizes the possibilities.

### Recommended options

| [Python](/scripting/python)          | {% include wikipedia title='Python (programming language)' text='Python' %} is a popular choice among scientists. There are [several ways to combine Python with Fiji](/scripting/python). |
| [Groovy](/scripting/groovy)          | {% include wikipedia title='Groovy (programming language)' text='Groovy' %} is a flexible and powerful scripting language, Java-like but less verbose and dynamically typed. Learn this, and using Java later (if needed) will become easier. |
| [ImageJ Macro](/scripting/macro)     | The [ImageJ](/software/imagej) macro language is less powerful than the other scripting languages, but is designed to be easy to learn and use. |
| [JavaScript](/scripting/javascript)  | {% include wikipedia title='JavaScript' text='JavaScript' %} is a popular choice among web developers. |
| [Ruby (JRuby)](/scripting/jruby)     | {% include wikipedia title='Ruby (programming language)' text='Ruby' %} is another popular choice among web developers. |
| [Lisp (Clojure)](/scripting/clojure) | {% include wikipedia title='Lisp (programming language)' text='Lisp' %} is a popular choice among computer scientists. |
| [R (Renjin)](/scripting/renjin)      | {% include wikipedia title='R (programming language)' text='R' %} is a popular choice among scientists and statisticians. |

### Other options

| [Java](/develop/plugins)          | You can code Java plugins in the Script Editor. This is the most difficult path, but also the most powerful. |
| [MATLAB](/scripting/matlab)       | Fiji can interface bidirectionally with MATLAB. See the [MATLAB Scripting](/scripting/matlab) page for details. |
| [BeanShell](/scripting/beanshell) | {% include wikipedia title='BeanShell' text='BeanShell' %} is an old script language, maintained mostly for backwards compatibility. It is nearly 100% compatible with Java syntax, but so is [Groovy](/scripting/groovy). |
| [Scala](/scripting/scala)         | {% include wikipedia title='Scala (programming language)' text='Scala' %} support is currently experimental, and has bugs. |

## Script parameters

There is a universal script parameter notation available across all SciJava scripts for declaring inputs and outputs. This approach is preferred to using `GenericDialog` because it is totally agnostic to the user interface, allowing such scripts to run in a variety of contexts.

See the [script parameters](/scripting/parameters) page for details.

## Using an interpreter

All scripting languages use the same basic interpreter, with the following common features.

### General key bindings

-   {% include key key='up' %}: bring the previously typed command.
-   {% include key key='down' %}: bring the next typed command.
-   {% include key key='enter' %}: execute the contents of the prompt.

### Multiline editing and keybindings

You can enlarge the prompt by dragging the middle bar.

-   {% include key keys='Shift|Enter' %}: create a new line within the prompt.
-   {% include key keys='Shift|Up' %}: move to the line above within the prompt.
-   {% include key keys='Shift|Down' %}: move to the line below within the prompt.

### Selecting and executing text from the screen

On selecting text, a popup offers to:

-   copy
-   execute
-   save to a new file

## Using the script editor

You can create, edit and run scripts using the built-in [Script Editor](/scripting/script-editor). For details, please see [the Script Editor documentation](/scripting/script-editor).

## Adding scripts to the Plugins menu

For the script to appear in the menus, the following must apply:

{% include notice icon="warning" content="`.txt` is not a supported script extension" %}

1.  The script file is saved in the `Fiji/scripts` or the `Fiji/plugins/Scripts` directory (or a subdirectory thereof).
2.  The script name ends in a supported script extension. For example:
    - `.groovy` for groovy,
    - `.js` for javascript,
    - `.py` for jython,
    - `.rb` for jruby,
    - `.clj` for clojure,
    - `.bsh` for beanshell, and
    - `.ijm` for ImageJ 1.x macros.
3.  The script name contains a `_` (underscore) character, e.g. `MyScript_.ijm`.

The extension will be stripped and any underscores will be turned into spaces before the script is added to the menus.

Scripts in the top-level `Fiji/plugins` directory will appear at the bottom of the *Plugins* menu. Scripts can be placed in other menus by nesting subdirectories, for example placing a script in the `Fiji/scripts/File` directory will add it to the {% include bc path="File" %} menu.

The menu path, label, icon, and other module metadata can also be set from within a script using the [`#@script` directive](/scripting/basics#the-script-directive).

If you aren't able to find your script, you can always use the [search bar](/learn#the-search-bar) to verify its location (or absence).

Commands added to the menu in the described way can be called from other scripts. Use the [macro recorder](/scripting/macro#the-recorder) to get the required code for doing so.

### Adding JAR-packaged scripts to the menu

Scripts can be packaged in a JAR file for easier distribution to your colleagues and via [Update Sites](/update-sites). For this purpose, [example-script-collection](https://github.com/imagej/example-script-collection) can be used as the template Maven project.

Inside the example-script-collection jar, the scripts are in `./resources/scripts.` and therefore get added to the menu when the JAR is on the classpath (i.e. in `./plugins/` or `./jars/`).

Fiji looks for scripts in subfolders of `./scripts/` as it is already described in the previous section, and for jars in `./jars/`. The original [ImageJ](/software/imagej) recognizes plugins and scripts in `./plugins/`.

## Running scripts in headless mode

See the [Scripting Headless](/scripting/headless) page for instructions on executing scripts headlessly.
