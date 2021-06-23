---
title: Script Parameters
project: /software/imagej2
---

All scripting languages have access to a universal `#@parameter` notation for declaring inputs and outputs. This approach is preferred over the original [ImageJ](/software/imagej)'s [GenericDialog](/scripting/generic-dialog) because it is totally agnostic of the user interface, allowing such scripts to run in a variety of contexts. As with [ImageJ2 plugins](/develop/plugins), script parameterization is based on the [SciJava](/libs/scijava) [parameter annotation](https://github.com/scijava/scijava-common/blob/scijava-common-2.40.0/src/main/java/org/scijava/plugin/Parameter.java)—so experience with plugin writing directly translates to scripting, and vice versa.

{% include notice icon="info" content='Script parameters are a feature of [ImageJ2](/software/imagej2); they will not work in the original [ImageJ](/software/imagej). The [Fiji](/software/fiji) distribution of ImageJ is built on ImageJ2, so they also work in Fiji.' %}

## Basic syntax

{% include testimonial person="kephale" description="Clojure developer"
  quote="zomg UIs are so easy now\\
done by lunchtime"
  source="https://gitter.im/fiji/fiji?at=5717afbc98c544f1396cef2f" %}

The rules for `#@` parameter use are as follows:

1.  Parameter declarations begin with `#@`. Each such line contains a single parameter declaration or script directive and nothing else.
2.  `#@ Type variableName` will declare an input of the indicated type, assigned to the specified name. (The use of a space between `#@` and `Type` is encouraged, but not required.)
3.  `#@output Type outputName` will declare the variable of the specified name as an output parameter with the given type. The `Type` parameter is optional, as the output will be treated as `Object` be default. (For the `output` directive and other script directives, no space is allowed between `#@` and the directive.)

For example, if we look at the [Greeting.py](https://github.com/scijava/scripting-jython/blob/scripting-jython-0.2.0/src/main/resources/script_templates/Python/Greeting.py) [template](/scripting/templates) supplied with Fiji:

{% include code org='scijava' repo='scripting-jython' branch='master' path='src/main/resources/script_templates/Intro/Greeting.py' %}

We see that an input parameter `name` of type `String` is declared. `@Parameters` are handled automatically by the framework; if we run this script when the User Interface is available (e.g. from the script editor), the `name` parameter will automatically be harvested via a pop-up dialog:

<img src="/media/scripting/scriptparams.png" width="450"/>

We could also run this script [headlessly](/scripting/headless), thanks to the general nature of `@parameters`.

When the script is completed, any `#@output` variables are handled by the framework, based on their type. In this case we expect the `greeting` variable to be printed, since it is a `string`.

## Parameter types

A list of possible data types and the corresponding widgets is provided below.  
The optional style argument defines how the widget are rendered in the input window.  
See the respective widget sections for a preview of the styles.

| **Data type**                   | **Widget type**                          | **Available styles**                           |
|---------------------------------|------------------------------------------|------------------------------------------------|
| `boolean` `Boolean`             | checkbox                                 |                                                |
| `byte` `short` `int` `long`     | numeric field                            | `slider` `spinner` `scroll bar`                |
| `Byte` `Short` `Integer` `Long` | numeric field                            | `slider` `spinner` `scroll bar`                |
| `Float`                         | numeric field                            | `slider` `spinner` `scroll bar`                |
| `BigInteger` `BigDecimal`       | numeric field                            | `slider` `spinner` `scroll bar`                |
| `char` `Character` `String`     | text field                               | `text field` `text area` `password`            |
| `Dataset` `ImagePlus`           | (&gt;=2 images) triggers a dropdown list |                                                |
| `ColorRGB`                      | color chooser                            |                                                |
| `Date`                          | date chooser                             |                                                |
| `File`                          | file chooser                             | `open` `save` `file` `directory` `extensions:` |

Notes and gotchas:
* `float` is also an accepted field but the decimal t is not displayed in the form compared to `Float` (mind the capital F).
* A related [issue](https://github.com/scijava/scijava-common/issues/302) occurs with `int` and `double` when a default value is set in the code and entered in the form, the value is not properly recalled at the next run. Use `Integer` and `Double` instead.
* A single `#@ ImagePlus` or `#@ Dataset` field will not show up in the input form, instead the current image will automatically be processed. However, if two `#@ ImagePlus` (or respectively `#@ Dataset`) are present then they will be rendered as drop-down buttons.

By implementing {% include javadoc project='SciJava' package='org/scijava/widget' class='InputWidget' %} it is possible to extend this list.

## Examples

### Integer and Decimal input

Integer and float can have the optional argument *min*, *max* and *stepSize* value (default 1) as well as a default value indicated by *value*.  
Different styles are also possible.

```javascript
#@ Integer (label="Default integer style", min=0, max=10, value=5) myint1
#@ Integer (label="Slider integer style", style="slider", min=0, max=10, stepSize=2) myint2
#@ Float   (label="Slider with float", style="slider", min=0, max=1, stepSize=0.1) myfloat
```

<img src="/media/scripting/scriptparameters-integerstyles.jpg" width="450"/>

## Parameter properties

If you look at the [@Parameter annotation](https://github.com/scijava/scijava-common/blob/scijava-common-2.40.0/src/main/java/org/scijava/plugin/Parameter.java), you will notice it has many properties—for example, `name` and `description`.

Script parameters can set these properties, following these guidelines:

1.  All properties are defined in a **single parenthetical expression** immediately following the `#@type` declaration.
2.  Properties are set by a [comma-separated list of **key=value** pairs](https://docs.oracle.com/javase/tutorial/java/annotations/basics.html)

Properties are your way to customize how an `#@parameter` should be handled by the framework.

### Widget labels

Widgets are the User Interface elements shown to users to collect input information. For example, instead of just displaying "Name" to the user, we can add a custom label to the field of our `Greeting.py` script as follows:
```python
#@ String (label="Please enter your name") name
#@ output String greeting

greeting = "Hello, " + name + "!"
```
### Widget mouseover

We can add a `description` property to provide mouse-over text for our field:
```python
#@ String (label="Please enter your name", description="Your name") name
#@ output String greeting

greeting = "Hello, " + name + "!"
```
### Default values

Default values are also supported as parameter properties:
```javascript
#@ Integer (label="An integer!",value=15) someInt`
```
### Persistence

Per default, variable values are persisted between runs of a script. This means that parameter values from a previous run are used as starting value. Please note that a persisted value will overwrite a defined [default value](#default-value).
```javascript
#@ Integer (label="An integer!", value=15, persist=false) someInt`
```
{% include notice icon="warning" content='Currently, "two scripts which declare the same parameter name, even with different types, will stomp each other." See [1](https://github.com/scijava/scijava-common/issues/193).' %}

### Visibility

This property set if the parameter should be displayed, editable and/or recorded.

\- NORMAL: parameter is included in the history for purposes of data provenance, and included as a parameter when recording scripts.

\- TRANSIENT: parameter is excluded from the history for the purposes of data provenance, but still included as a parameter when recording scripts.

\- INVISIBLE: parameter is excluded from the history for the purposes of data provenance, and also excluded as a parameter when recording scripts. This option should only be used for parameters with no effect on the final output, such as a "verbose" flag.

\- MESSAGE: parameter value is intended as a message only, not editable by the user nor included as an input or output parameter. The option `required` should be set to false.


<img src="/media/scripting/scriptparam-messagestring.jpg" width="450"/>

```javascript
#@ String (visibility=MESSAGE, value="This is a documentation line", required=false) msg
#@ Integer (label="Some integer parameter") my_int
```

You can [use HTML](https://forum.image.sc/t/multiline-messages-in-dialog-widgets/183) to format the message string, for example:

```javascript
#@ String (visibility=MESSAGE, value="<html>Message line 1<br/>Message line 2<p>Let's make a list<ul><li>item a</li><li>item b</li></ul></html>") docmsg
#@ Integer anIntParam
```
 ![](/media/scripting/scijavamultilinemessage.png)

{% include notice icon="warning" content='Currently if a script containing a MESSAGE string is recorded with the macro recorder and the resulting recorded code executed, a window will show up containing only the MESSAGE string This is unexpected and will be corrected in the future.' %}

### Multiple Choice

Any parameter can be turned into a multiple-choice selector by adding a `choices={...}` property.  
The choice widget can have different styles like dropdown list or radio buttons.
```javascript
#@ String (choices={"Option 1", "Option 2"}, style="listBox") myChoice123
#@ String (choices={"Option A", "Option B"}, style="radioButtonHorizontal") myChoiceABC

print(myChoice123)
print(myChoiceABC)
```
![](/media/scripting/input-styles.png)

### Files and Folders

By default, a `#@ File` parameter will create a chooser for a single file. Here is an example in python:
```javascript
#@ File (label="Select a file") myFile

print(myFile)
```
You can request for multiple files or folders as well. However multiple files/folders input are not yet macro-recordable.

Example in ImageJ Macro Language:
```javascript
#@ File[] listOfPaths (label="select files or folders", style="both")

print("There are "+listOfPaths.length+" paths selected.");

for (i=0;i<listOfPaths.length;i++) {
        myFile=listOfPaths[i];
        if (File.exists(myFile)) {
                print(myFile + " exists.");
                if (File.isDirectory(myFile)) {
                        print("Is a directory");
                } else {
                        print("Is a file");
                }
        }
}
```

If you want to select files or folders exclusively, use a `style` property:
```javascript
#@ File (label="Select a file", style="file") myFile
#@ File (label="Select a directory", style="directory") myDir

print(myFile)
print(myDir)
```
The single `File` parameter support the styles "*file*", "*directory*", "*open*", "*save*".

For multiple file or directories, the styles are plural
```javascript
#@ File[] (label="Select some files", style="files") listfiles
#@ File[] (label="Select some directories", style="directories") listdirs

print(listfiles)
print(listdirs)
```
The `File[]` parameter supports the styles "*files*", "*directories*", "*both*".

### Styles
You can influence the visual style of some of the input widgets. See previous paragraph for widget-specific style examples.
