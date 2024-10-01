---
title: Script Interpreter
project: /libs/scijava
artifact: org.scijava:script-editor
---

The **Script Interpreter** is a {% include wikipedia title="Read–eval–print loop" %} allowing scripting from the command line.

## Getting Started

Start it via {% include bc path='Plugins|Scripting|Script Interpreter'%} or by typing {% include key key='Shift|[' %}.

![Script_Interpreter.png](/media/scripting/script-interpreter.png)

## Usage Examples

The examples below are written in "C-like" syntax. They should work as-is e.g. in [Groovy](groovy), [Jython](jython), and [JavaScript](javascript), but will need adjustment for languages like [Clojure](clojure) whose syntax diverges more from C.

| Operation                       | Code                                                  |
|---------------------------------|-------------------------------------------------------|
| Get the active dataset          | `image = imageDisplay.getActiveDataset()`             |
| Run an op                       | `blurred = op.run("filter.gauss", image, 5)`          |
| Quick display (no metadata!)    | `ui.show("Blurred", blurred)`                         |
| Wrap image to dataset           | `ds = dataset.create(blurred)`                        |
| Get dataset dimensionality      | `ds.numDimensions()`                                  |
| Get length of dim #d            | `ds.dimension(d)`                                     |
| Get dim #d axis type            | `ds.axis(d).type()`                                   |
| Override dim #d axis type       | `ds.axis(d).setType(Axes.CHANNEL)`                    |
| Blend channels when displaying  | `ds.setCompositeChannelCount(3)`                      |
| Wrap dataset to data view       | `dv = imageDisplay.createDataView(ds); dv.rebuild()`  |
| Set color table for channel #0  | `dv.setColorTable(ColorTables.MAGENTA, 0)`            |
| Set color table for channel #1  | `dv.setColorTable(ColorTables.GREEN, 1)`              |
| Set color table for channel #2  | `dv.setColorTable(ColorTables.BLUE, 2)`               |
| Wrap data view to display       | `disp = display.createDisplay("Blurred", dv)`         |
| Get a display by title          | `disp = display.getDisplay("Blurred")`                |
| Get `DataView` from display     | `dv = disp[0]`                                        |
| Get dataset from `DataView`     | `ds = dv.getData()`                                   |

You can import `Axes` from `net.imagej.axis`, and `ColorTables` from `net.imagej.display`.

See the [ImageJ2 Tutorials](https://github.com/imagej/tutorials) for more recipes.

## Inspecting API of an Object

The script interpreter does not yet have tab completion. :-( But you can using the following (Python) function to list the methods of an object:
```python
def methods(obj, prefix=""):
    return "\n".join(row["name"] + "(" + row["arguments"] + ") -> " + row["returns"] for row in notebook.methods(obj, prefix))
```
E.g.:
```
>>> methods(imageDisplay, "getActive")
getActiveDataset(<none>) -> net.imagej.Dataset
getActiveDataset(net.imagej.display.ImageDisplay) -> net.imagej.Dataset
getActiveDatasetView(<none>) -> net.imagej.display.DatasetView
getActiveDatasetView(net.imagej.display.ImageDisplay) -> net.imagej.display.DatasetView
getActiveImageDisplay(<none>) -> net.imagej.display.ImageDisplay
getActivePosition(<none>) -> net.imagej.Position
getActivePosition(net.imagej.display.ImageDisplay) -> net.imagej.Position
```

## Issues

The Script Interpreter is still somewhat immature. Currently, [Groovy](/scripting/groovy) works fine, but there some issues with other scripting languages.
