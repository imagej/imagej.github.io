---
title: Generic Dialog
project: /software/imagej
---

## Introduction

The [GenericDialog](https://imagej.nih.gov/ij/developer/api/ij/ij/gui/GenericDialog.html) class is part of [ImageJ](/software/imagej) and can be used to make simple graphical user interfaces for scripts and plugins. It requires a bit more work than with the [script parameters](/scripting/parameters) feature of [SciJava](/libs/scijava), but offers more possibilities.

Fiji offers an additional {% include javadoc project='Fiji' package='fiji/util/gui' class='GenericDialogPlus' %} subclass which include additional GUI items like a file input with a browse button.  

As with script parameters, plugins using the `GenericDialog` (or one of its subclasses) are macro recordable.

### In Jython (or similar scripting language)

Here is an example in Jython.

```python
from ij.gui import GenericDialog

# Create an instance of GenericDialog
gui = GenericDialog("My first GUI")

# Add some gui elements (Ok and Cancel button are present by default)
# Elements are stacked on top of each others by default (unless specified)
gui.addMessage("Some information to display at the top of the gui")
gui.addStringField("Type some input text :", "initial text")
gui.addCheckbox("This is a tickbox->Activate some option", True)

# We can add elements next to each other using the addToSameRow method
gui.addToSameRow() # The next item is appended next to the tick box
gui.addChoice("Choose one option among a list", ["Choice1", "Choice2"], "Choice1") # Choice1 is default here

gui.addNumericField("Some integer", 10, 0) # 0 for no decimal part

# Add a Help button in addition to the default OK/Cancel
gui.addHelp(r"https://imagej.net/scripting/generic-dialog") # clicking the help button will open the provided URL in the default browser

# Show dialog, the rest of the code is not executed before OK or Cancel is clicked
gui.showDialog() # dont forget to actually display the dialog at some point


# If the GUI is closed by clicking OK, then recover the inputs in order of "appearance"
if gui.wasOKed():
    inString = gui.getNextString()
    inBool   = gui.getNextBoolean()
    inChoice = gui.getNextChoice() # one could alternatively call the getNextChoiceIndex too
    inNum    = gui.getNextNumber() # This always return a double (ie might need to cast to int)
```

### In the macro language

There are 2 options to generate a GUI in the ImageJ macro language.  
The first option is convenient if only a single or few parameters are requested.  
It will open a dedicated input window for every parameter requested ie if there are multiple parameters, several windows will successively show up.
```javascript
someNumber = getNumber("Some number", 0); // 0 is the default here
someString = getString("Some string", "DefaultValue");
```

The list of possible inputs is the same than for the second option with the Dialog.  
Using Dialog (the 2nd option), a single input window will show up with all parameters. This requires a little bit more coding than the 1st option, but is more elegant.

```javascript
Dialog.create("My inputs");
Dialog.addMessage("Some message to display");

var min = 0;
var max = 10;
var default = 5;
Dialog.addSlider("Some slider", min, max, default);
Dialog.addNumber("Some number", 0);
Dialog.addString("Some string", "DefaultString");

Dialog.addChoice("Type:", newArray("8-bit", "16-bit", "32-bit", "RGB"));
Dialog.addCheckbox("Ramp", true);

// One can add a Help button that opens a webpage
Dialog.addHelp("https://imagej.nih.gov/ij/macros/DialogDemo.txt");

// Finally show the GUI, once all parameters have been added
Dialog.show();

// Once the Dialog is OKed the rest of the code is executed
// ie one can recover the values in order of appearance 
inNumber1 = Dialog.getNumber(); // Sliders are number too
inNumber2 = Dialog.getNumber();
inString  = Dialog.getString();
inChoice  = Dialog.getChoice();
inBoolean = Dialog.getCheckbox();

print("Number1:", inNumber1);
print("Number2:", inNumber2);
print(inString);
print("Choice:", inChoice);
print("Do something (1=True, 0=False):", inBoolean);
```

See the section "/scripting/generic-dialog" of the [Macro functions reference](https://imagej.nih.gov/ij/developer/macro/functions.html) for more details.

## Image and file inputs

By default, script and plugins process the last selected image.  
However sometime one needs to specify different images or files as input.  
The subclass {% include javadoc project='Fiji' package='fiji/util/gui' class='GenericDialogPlus' %} provides a couple of handful methods for such cases, while all methods shown above are inherited from the GenericDialog class.

```python
from fiji.util.gui import GenericDialogPlus

# Create an instance of GenericDialogPlus
gui = GenericDialogPlus("an enhanced GenericDialog")

# Add possibility to choose some images already opened in Fiji
gui.addImageChoice("Image1","Some description for image1")
gui.addImageChoice("Image2","Some description for image2")


# The GenericDialogPlus also allows to select files, folder or both using a browse button
gui.addFileField("Some_file path", "DefaultFilePath")
gui.addDirectoryField("Some_folder path", "DefaultFolderPath")
gui.addDirectoryOrFileField("Some_Path", "DefaultPath")

gui.showDialog()

# Recover the inputs in order of "appearance"
if gui.wasOKed():
    image1 = gui.getNextImage() # This method directly returns the ImagePlus object
    image2 = gui.getNextImage()

    # Path are recovered as string
    filePath   = gui.getNextString()
    folderPath = gui.getNextString()
    somePath   = gui.getNextString()
```

## Macro-recording

Just like script parameters, plugins using the GenericDialog class are macro-recordable.  
One important thing to note is the name of the variable in the recorded command. This name is actually the first word of the string used as label for each item, with lowercase letters only.  
A single word is not very intuitive to understand a parameter in most cases. To include the next words of the label in the recorded command replace the space with underscores, as in `some_file` above.

For instance the previous code saved as `GUI_.py` in `Fiji.app/scripts/Plugins/Test` yields the following recorded command:  
`run("GUI ", "image1=MyImage1.tif image2=MyImage2.tif some_file=DefaultFilePath some_folder=DefaultFolderPath some_path=DefaultPath");`

## Recalling previous entries using the PrefService

It is convenient to have the previously entered parameters recalled at the next run of a given plugin. This is happening automatically for Script parameters (unless specified differently) but not for the GenericDialog class.  
Fortunately, it is still possible to make it work using the PrefService.

Services are some ImageJ2/SciJava features that can be thought of as some kind of package import at runtime. They are not available in the original ImageJ, thus an alternative to recall parameters in ImageJ is to use a temp file to store the previously entered parameters.  
Here's the link to the {% include javadoc project='SciJava' package='org/scijava/prefs' class='PrefService' %}.  
And below is a Jython example of how to use it.
```python
#@ PrefService prefs 
from fiji.util.gui import GenericDialogPlus 

# Create GUI 
gui = GenericDialogPlus("Some GUI")

gui.addImageChoice("Image", prefs.get(None, "Image", "DefaultImage") ) 
gui.addCheckbox("Activate some option", prefs.getInt(None, "doOption", False) ) # in theory we should use the getBoolean method but it does not work for Jython, the wrong method signature is matched
gui.addStringField("Some_string", prefs.get(None, "someString", "initial")) 
gui.addChoice("Some_choice", ["Choice1","Choice2"], prefs.get(None, "someChoice", "DefaultChoice")) 
gui.addNumericField("Some_integer", prefs.getInt(None, "n", 1), 0)  
gui.addNumericField("Some_float", prefs.getFloat(None, "number", 0.5), 2) 

gui.showDialog() 

if gui.wasOKed(): 
    image      = gui.getNextImage() 
    doOption   = gui.getNextBoolean()
    someString = gui.getNextString() 
    someChoice = gui.getNextChoice() 
    n          = int(gui.getNextNumber()) # cast to int : getNextNumber always return a double
    number     = gui.getNextNumber()

    # Save in memory using PrefService 
    prefs.put(None, "image", image.getTitle()) 
    prefs.put(None, "doOption", doOption) 
    prefs.put(None, "someString", someString) 
    prefs.put(None, "someChoice", someChoice ) 
    prefs.put(None, "n", n) 
    prefs.put(None, "number", number) 
```
The first step is to "import" the PrefService and to assign it a name, here prefs.

Then there are 2 methods to respectively recover and store some parameter values from the PrefService, namely `get` and `put`.

Let's start with `get`. This method is define for the different datatype `getInt`, `getFloat`, `getBoolean`. An exception for String there is no `getString` just `get`.  
Also in Jython the `getBoolean` method is not mapping the right Java signature, so use `getInt` instead as illustrated above.

There are 3 arguments for the `get` methods:

1.  The Plugin class for which to associate the parameter persistence. Leave it None (or Null in other languages) to use the default.
2.  The name of the variable to recall from memory/the preferences, it should be the same name used by the `put` method for that parameter.
3.  The default value to use if no variable with such name exist in memory ie the first time you run your script or if you reset the preferences.

The method `put` is even simpler as there is only a single method that takes also 3 arguments:

1.  Like for `get` an optional Plugin class
2.  The name used to store the parameter value in memory/in the preferences, it is the same name used by `get` to recover the previously entered value.
3.  The value to store in memory with the name in argument 2. If the parameter was already existing in memory the value is updated to this newly provided value.

Therefore in the script above, the default values for the GenericDialog fields are initialized to the values available in memory, or some default values if there are missing in memory.  
Once the GUI is oked, the values in memory are updated with the newly typed values, using the `put` method.

## Custom buttons

Using the [GenericDialogPlus](https://javadoc.scijava.org/Fiji/fiji/util/gui/GenericDialogPlus.html) provided with Fiji, it is possible to add custom buttons and associated actions to a GUI.  
To do so, we have to import the [ActionListener](https://docs.oracle.com/javase/7/docs/api/java/awt/event/ActionListener.html) interface from `java.awt.event`.  
We then create a class that implements this interface, and that contains a single method named `actionPerformed`, which will be called anytime the user interacts with an item that is linked to this event-listening class, like a button.  
In the folloguig jython example, we define 2 buttons A and B, both associated to the same event-handling class named `ButtonClic`.  
If any of the button is clicked, the `actionPerformed` method of `ButtonClic` is called. However the source of the event is different (button A or B), and thus we can define different commands to execute for each case.  
For more complicated cases, one could also create different event-handling classes to assign to different set of GUI items.

```python
from fiji.util.gui    import GenericDialogPlus
from java.awt.event   import ActionListener


class ButtonClic(ActionListener):
    """Class which unique function is to handle the button clics"""

    def actionPerformed(self, event): # self (or this in Java) to state that the method will be associated to the class instances

        # Check from where comes the event 
        source = event.getSource() # returns the Button object
        print source 

        # Do an action depending on the button clicked
        if source.label == "A":
            print "You clicked A\n"

        elif source.label == "B":
            print "You clicked B\n"


gui = GenericDialogPlus("GUI with custom buttons")
clicRecorder = ButtonClic()      # Create an instance of the ButtonClic class
gui.addButton("A", clicRecorder) # Associate the buttons to an instance of the ButtonClic class
gui.addButton("B", clicRecorder)
gui.showDialog()
```
