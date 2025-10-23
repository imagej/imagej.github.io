---
title: Scripting
section: Extend:Scripting
project: /software/imagej2
---

[ImageJ](/software/imagej) and [ImageJ2](/software/imagej2) allow you to write scripts in several different languages.

# Getting started

-   Read the [ImageJ2 tutorial notebooks](/tutorials/notebooks) to learn how to write scripts.
-   Press the {% include key key='[' %} key to open the [Script Editor](/scripting/script-editor) (or {% include key key='Shift' %}-{% include key key='[' %} to open the [Script Interpreter](/scripting/interpreter)).
-   Optionally, choose a template from the {% include bc path="Templates" %} menu to get you started.
-   Otherwise, choose your language from the {% include bc path="Language" %} menu.
-   Grab code snippets for common tasks from the [Scripting toolbox](/scripting/toolbox).
-   See [Scripting comparisons](/scripting/comparisons) for a side-by-side comparison of scripting languages.

# Supported languages

ImageJ2's [Script Editor](/scripting/script-editor) supports many different languages. The following table summarizes the possibilities.

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td colspan=2>Recommended options</td>
    </tr>
    <tr>
      <td><a href="/scripting/groovy">Groovy</a></td>
      <td>
        {% include wikipedia title='Groovy (programming language)' text='Groovy'%} is a flexible and powerful scripting language, Java-like but less verbose and dynamically typed. Learn this, and using Java later (if needed) will become easier.
      </td>
    </tr>
    <tr>
      <td style="white-space: nowrap"><a href="/scripting/macro">ImageJ Macro</a></td>
      <td>
        The <a href="/software/imagej">ImageJ</a> macro language is less powerful than the other scripting languages, but is designed to be easy to learn and use.
      </td>
    </tr>
    <tr>
      <td><a href="/scripting/python">Python</a></td>
      <td>
        {% include wikipedia title='Python (programming language)' text='Python'%} is a popular choice among scientists. You can write [Jython scripts](/scripting/jython) (a Java-based Python 2 dialect) from inside ImageJ using its [script editor](/scripting/script-editor), or use [PyImageJ](/scripting/pyimagej) to invoke ImageJ functions from Python scripts.
      </td>
    </tr>
    <tr>
      <td><a href="/scripting/javascript">JavaScript</a></td>
      <td>
        {% include wikipedia title='JavaScript' text='JavaScript'%} is a popular choice among web developers.
      </td>
    </tr>
    <tr>
      <td style="white-space: nowrap"><a href="/scripting/jruby">Ruby (JRuby)</a></td>
      <td>
        {% include wikipedia title='Ruby (programming language)' text='Ruby'%} is another popular choice among web developers.
      </td>
    </tr>
    <tr>
      <td style="white-space: nowrap"><a href="/scripting/clojure">Lisp (Clojure)</a></td>
      <td>
        {% include wikipedia title='Lisp (programming language)' text='Lisp'%} is a popular choice among computer scientists.
      </td>
    </tr>
    <tr>
      <td style="white-space: nowrap"><a href="/scripting/renjin">R (Renjin)</a></td>
      <td>
        {% include wikipedia title='R (programming language)' text='R'%} is a popular choice among scientists and statisticians.
      </td>
    </tr>
    <tr>
      <td colspan=2>Other options</td>
    </tr>
    <tr>
      <td><a href="/develop/plugins">Java</a></td>
      <td>
        You can code Java plugins in the Script Editor. This is the most difficult path, but also the most powerful.
      </td>
    </tr>
    <tr>
      <td><a href="/scripting/matlab">MATLAB</a></td>
      <td>
        ImageJ2 can interface bidirectionally with MATLAB. See the <a href="/scripting/matlab">MATLAB Scripting</a> page for details.
      </td>
    </tr>
    <tr>
      <td><a href="/scripting/beanshell">BeanShell</a></td>
      <td>
        {% include wikipedia title='BeanShell' text='BeanShell'%} is an old script language, maintained mostly for backwards compatibility. It is nearly 100% compatible with Java syntax, but so is <a href="/scripting/groovy">Groovy</a>.
      </td>
    </tr>
    <tr>
      <td><a href="/scripting/scala">Scala</a></td>
      <td>
        {% include wikipedia title='Scala (programming language)' text='Scala'%} support is currently experimental, and has bugs.
      </td>
    </tr>
  </tbody>
</table>
{:/}

# Script parameters

There is a universal script parameter notation available across all scripts for declaring inputs and outputs. This approach is preferred to using `GenericDialog` because it is totally agnostic to the user interface, allowing such scripts to run in a variety of contexts.

See the [script parameters](/scripting/parameters) page for details.

# Using an interpreter

All scripting languages use the same basic interpreter, with the following common features.

## General key bindings

-   {% include key key='up' %}: bring the previously typed command.
-   {% include key key='down' %}: bring the next typed command.
-   {% include key key='enter' %}: execute the contents of the prompt.

## Multiline editing and keybindings

You can enlarge the prompt by dragging the middle bar.

-   {% include key keys='Shift|Enter' %}: create a new line within the prompt.
-   {% include key keys='Shift|Up' %}: move to the line above within the prompt.
-   {% include key keys='Shift|Down' %}: move to the line below within the prompt.

## Selecting and executing text from the screen

On selecting text, a popup offers to:

-   copy
-   execute
-   save to a new file

# Using the script editor

You can create, edit and run scripts using the built-in [Script Editor](/scripting/script-editor). For details, please see [the Script Editor documentation](/scripting/script-editor).

# Adding scripts to the Plugins menu

For the script to appear in the menus, the following must apply:

{% include notice icon="warning" content="`.txt` is not a supported script extension" %}

1.  The script file is saved in the `ImageJ2.app/scripts` or the
    `ImageJ2.app/plugins/Scripts` directory (or a subdirectory thereof).
2.  The script name ends in a supported script extension. For example:
    - `.groovy` for groovy,
    - `.js` for javascript,
    - `.py` for jython,
    - `.rb` for jruby,
    - `.clj` for clojure,
    - `.bsh` for beanshell, and
    - `.ijm` for ImageJ 1.x macros.
3.  The script name contains a `_` (underscore) character,
    e.g. `MyScript_.ijm`.

{% include notice icon="fiji" content='Fiji users: replace `ImageJ2.app` with `Fiji.app`' %}

The extension will be stripped and any underscores will be turned into spaces before the script is added to the menus.

Scripts in the top-level `ImageJ2.app/plugins` directory will appear at the bottom of the *Plugins* menu. Scripts can be placed in other menus by nesting subdirectories, for example placing a script in the `ImageJ2.app/scripts/File` directory will add it to the {% include bc path="File" %} menu.

If you aren't able to find your script, you can always use the [search bar](/learn#the-search-bar) to verify its location (or absence).

Commands added to the menu in the described way can be called from other scripts. Use the [macro recorder](/scripting/macro#the-recorder) to get the required code for doing so.

## Adding JAR-packaged scripts to the menu

Scripts can be packaged in a JAR file for easier distribution to your colleagues and via [Update Sites](/update-sites). For this purpose, [example-script-collection](https://github.com/imagej/example-script-collection) can be used as the template Maven project.

Inside the example-script-collection jar, the scripts are in `./resources/scripts.` and therefore get added to the menu when the JAR is on the classpath (i.e. in `./plugins/` or `./jars/`).

ImageJ2 (and therefore Fiji) looks for scripts in subfolders of `./scripts/` as it is already described in the previous section, and for jars in `./jars/`. The original [ImageJ](/software/imagej) recognizes plugins and scripts in `./plugins/`.

# Running scripts in headless mode

See the [Scripting Headless](/scripting/headless) page for instructions on executing scripts headlessly.
