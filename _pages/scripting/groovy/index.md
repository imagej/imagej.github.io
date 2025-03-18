---
title: Groovy Scripting
section: Extend:Scripting:Languages
project: /software/imagej2
nav-links: true
---

## Introduction

[Groovy](http://groovy-lang.org/) is an agile and dynamic language for the Java Virtual Machine. It builds upon the strengths of [Java](/develop/plugins) but has additional power features inspired by languages like [Python](/scripting/python), [Ruby](/scripting/jruby) and Smalltalk.

## Quickstart

-   Press {% include key key='[' %} to bring up the [Script Editor](/scripting/script-editor).
-   Select an example Groovy script from the {% include bc path='Templates | [by language] | Groovy'%} menu.
-   Press {% include key keys='Ctrl|R' %} to run the script!

## Tips for groovy scripting in ImageJ

{% include notice icon="info" content='For an introduction in ImageJ scripting visit the page [Scripting basics](/scripting/basics).' %}

### Introduction

The aim of this page is not to teach how to program in Groovy. This purpose is much better fullfiled by the [Groovy Quick Start](http://groovy-lang.org/documentation.html#gettingstarted). The focus of this page is to show how to best use Groovy for scripting in ImageJ

### Use an IDE for Groovy scripting

As Groovy builds upon [Java](/develop/plugins), it can be use in a full fledged IDE with Fiji. If interested, follow this [tutorial](/scripting/groovy/ides).

## When to use Groovy

The following list will help you to decide if Groovy is the right choice for you to create scripts for ImageJ:

* If you have experience with Java, you can easily use Groovy for ImageJ scripting.

* If you want to be able to rapidly prototype something and make calls to external libraries, Groovy is a good choice.

* If you don't have experience with Java, but would like to get some, then scripting with Groovy can be a good way to learn.

* If you have very little or no experience in programming, you may like to explore [Jython](/scripting/jython) as it is an easy-to-read but feature-rich language.


## Explanation
At a basic level, Groovy is very similar to Java. As your familiarity with it grows, you will find it can do some things that Java can't.
Like Java, Groovy can access any class libraries that are present in the classpath. This allows you to to include 3rd party libraries which may not immediately be present in Fiji/ImageJ, but which you can download. Examples would include database connections, libraries for communication purposes, The list is long!

## Groovy basics for ImageJ

{% include notice icon="info" content='For an introduction in ImageJ scripting visit the page [Scripting basics](/scripting/basics).' %}

### Hello, World!

#### - With print / println

The print and println commands send output to the console, with the difference being that println always appends a newline character at the end

```groovy
println "Hello, World!"
// Let's show it handling numbers too
println "Result of 2 + 2: " + (2+2)

// what happens if we don't use the parentheses?
print "Result of 2 + 2: " + 2+2
```

Note - `print` and `println` will send their output to the standalone console if it's open. If not, it will go to the console of the Fiji Script Editor. Use cases would be where you want some sort of text output (to show values, progress etc), but you don't want it popping up for the user.

#### - With IJ.log()

`IJ.log()` is an example of an ImageJ java function (also called a method.
It creates a window in ImageJ (if one isn't already open) and writes text to it. 
Newline characters are always appended with each call.

```groovy
import ij.IJ

IJ.log("Hello, World!")
// Let's show it handling numbers too
IJ.log("Result of 2 + 2: " + (2+2))

// what happens if we don't use the parentheses?
IJ.log("Result of 2 + 2: " + 2+2)
```

If you tried out both sets of examples, the lines containing (2+2) will have evaluated as `4`, whereas the lines that don't have the brackets are treated as strings, giving `22`

Image selection using the GenericDialog class

This example script will create up to 10 new images and create a GenericDialog to select 3 of them. Finally the names of the selected images are printed to the Log window. It is recommended to copy the code to the [Script Editor](/scripting/script-editor) and run it by yourself.

```groovy
// Import the classes that are needed. 

import ij.IJ							          
import ij.WindowManager					    
import ij.gui.GenericDialog				  
import ij.plugin.frame.RoiManager		

// The IJ class contains a number of utilities. For this script, it provides the "log" functionality
// A class which gives access to the window objects
// A class which allows for creation of custom dialogs with relative ease.
// The ROI Manager - useful for accessing ROIs.

// next we'll define some functions. 

// Function to create a test image
def createTestImage() {
    int imageWidth = 512			// here, we're using explicit types - int holds an integer.
    int imageHeight = 512
    int boxWidth = 128
    int boxHeight = 128
    int offsetX = (int) 192 * 2 * Math.random()  // (int) causes the rest of the statement to be forced to an integer - no decimal places!
    int offsetY = (int) 192 * 2 * Math.random()
    int counts = 64
    int stdv = 16

    // The following are nested definitions. They are not available outside the "createTestImage" function.
    // the following line is called a closure. It's a short-hand way of creating a function.
    // This one returns a string:  makeTitle("Testing", 1, 2) will give 'Testing: 1, 2' as the output.
    def makeTitle = { prefix, x, y -> "${prefix}: ${x}, ${y}" }
      
    // we'll now call the makeTitle function and store the result in a variable called "title"
    // note that it's not a pre-defined type, instead the interpreter will decide what to use.
    def title = makeTitle('TestImage', offsetX, offsetY)
	
    // This closure looks a bit more like a java function. It's going to return either true or false.
    def checkExistence = { titleToCheck ->
        def idList = WindowManager.getIDList()    // get the list of open images
        if (idList == null) return false          // if the list is empty, return false.
        
        // 'collect', in the next line, is a Groovy method that iterates through whatever it is attached to 
        // and executes the code inside the curly brackets on each item it encounters.
        // In this case, it retrieves the title of each image into a list.
        def imageTitles = idList.collect { WindowManager.getImage(it).getTitle() }
        return imageTitles.contains(titleToCheck)
    }

    // That's it for the nested definitions, now lets use them.

    // Check if the image *doesn't* exist..
    if (!checkExistence(title)) {
        // if not, create an ImagePlus with the title, and image dimensions given
        def imp = IJ.createImage(title, "8-bit black", imageWidth, imageHeight, 1)	
        imp.show()

        // The following lines use calls to functionality that's already available - no need to reinvent the wheel.
        // Use the ImageJ mathematical function to add the value of "counts" to the current pixel values.
        IJ.run(imp, "Add...", "value=${counts}")
        // Create a simple rectangular ROI
        imp.setRoi(offsetX, offsetY, boxWidth, boxHeight)
        // and use the Add function again. This will only apply to the ROI
        IJ.run(imp, "Add...", "value=${counts}")
        // Select None removes the ROI - the whole image is now "active"                                    
        IJ.run("Select None")
        // Add noise to the image
        IJ.run(imp, "Add Specified Noise...", "standard=${stdv}")
        // That was a groovy-styled way of building the required parameter string
        // In Java, you would use "standard=" + stdv)

        // Tell ImageJ we're not interested in changes
        imp.changes = false
        // Display the image.
        imp.show()                                                                  
        
    }
}

// Another function to help us to build a dialog to show to the user. 
// It uses the GenericDialog class and takes 3 arguments: titles, defaults and a string for the dialog title.
def createSelectionDialog(imageTitles, defaults, dialogTitle) {                           
    // create a new instance of GenericDialog
    def gd = new GenericDialog(dialogTitle)

    // A quick way to loop through an object, adding choices as we go.
    defaults.eachWithIndex { defVal, index ->
        gd.addChoice("Image_${index + 1}", imageTitles as String[], imageTitles[defVal]) 
    }

    // show the dialog to the user
    gd.showDialog()                                                                       
    if (gd.wasCanceled()) return null   // if the user clicks cancel, return Null. 

    // the next line won't execute if the previous one evaluated as true, because the return statement causes the function to terminate.    
    return defaults.collect { gd.getNextChoiceIndex() }    
}

// Main script execution
def runScript() {
    while (WindowManager.getImageCount() < 10) {            // create a test image as long as the count is less than 10
        createTestImage()
    }

    // retrieve a list of the image titles using the WindowManager class.
    def imageTitles = WindowManager.getIDList().collect { WindowManager.getImage(it).getTitle() }
    
    // now we'll pass this to the createSelectionDialog function that was defined earlier.
    def selectedIndices = createSelectionDialog(imageTitles, [0, 1, 2], 'Select images for processing')
    if (selectedIndices == null) {                          // check if the user clicked cancel - see above!!
        println "Script was canceled."                      // print this to the console (Not the log window)
        return                                              // return without a value
    }
	
    // if selectedIndices wasn't null, the following code will execute
    // get a list of the avilable images (as ImagePlus objects)
    def selectedImages = selectedIndices.collect { WindowManager.getImage(WindowManager.getIDList()[it]) }

    // Display info on the ImageJ log.
    selectedImages.each { imp -> IJ.log("The image '${imp.getTitle()}' has been selected.") }	
}

// This is the only line of code that can actually be run - all the others have to be called.
// So the "runScript" function is called, which subsequently calls other functions.
runScript()

```

{% include notice icon="info" content='This page is under construction. Check back for updates.' %}
