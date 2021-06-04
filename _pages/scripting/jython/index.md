---
mediawiki: Jython_Scripting
title: Jython Scripting
section: Extend:Scripting:Languages
---



## Introduction

Jython is an implementation of the Python programming language designed to run on the Java platform. [^1] In ImageJ Jython is one of several [supported languages](/scripting#supported-languages).

## When to use Jython

All scripting language supported by ImageJ can be used to access the [ImageJ API](http://javadoc.imagej.net/). There are only differences in how the imports are handled and in the syntax of the selected language. Jython has a syntax that differs from most other language as indentations instead of brackets are used to group code blocks.

The following list will help you to decide if Jython is the right choice to create scripts for ImageJ:

-   If you have experience with Python you can easily use Jython for ImageJ scripting. But you have to keep in mind that tools commonly used in many Python projects (e.g. Numpy) are not available in Jython. By building your [own modules](/scripting/jython#self-written-jython-modules-for-imagej) you can create complex scripts that otherwise are only possible by writing ImageJ plugins in Java.
-   If don't have any experience in programming, the Python language is a good choice to start with. If your only aim is to write scripts for ImageJ, there are other languages you should try first (e.g. [Groovy](/scripting/groovy)).
-   In Python many problems can be solved with less code than in other languages. Still the code is easy to read. Have a look at the examples on this page and decide if you want to start using Python for ImageJ scripting.

### Explanation

The Java implementation of Python is limited to the [standard library](https://docs.python.org/2/library/index.html) of Python 2.  
It is not possible to use external python modules (like Numpy...) however, [any Java class residing in the Fiji installation can be used](/scripting/jython#importing-java-module-and-classes).  
Even with the given limitations, Jython is a powerful language for ImageJ scripting. Hopefully the examples on this page can convince you of that.

## Jython basics for ImageJ

{% include notice icon="info" content='For an introduction in ImageJ scripting visit the page [Scripting basics](/scripting/basics).' %}

### Introduction

The aim of this page is not to teach how to program in Python. This purpose is much better fulfilled by the [documentation of Python2](https://docs.python.org/2/library/index.html). The focus of this page is to show how features of the Python language can be useful for ImageJ scripting.

That is why more complex examples are used that are fully functional. Just copy the code to the [Script Editor](/scripting/script-editor) and try them by yourself. Extensive in-line documentation is used to explain the implementation.

### Hello World

#### - With print

There are 2 ways to print some information back to the user.  
The first one is a classical python print statement, that will print some information to the console.  
`print "Hello world"`  
You can print any kind of variable and objects.  
`print "This is a string followed by an int", 10`

NB1 : If used in a plugin, and no console window is open then the printed information will not be visible to the user (contrary to the `log` function below)

NB2 : Using numerous print statements might slow down the execution time when used in a plugin (not observed when executing from the script interpreter).

#### - With IJ.log()

    from ij import IJ
    IJ.log("Hello world")
    IJ.log("This is a string followed by an int " + str(10))

Contrary to the print statement the log function display some output into a log window (newly open if not already open), and accept only a string as argument.

### Image selection using the GenericDialog class

This example script will create up to 10 new images and create a GenericDialog to select 3 of them. Finally the names of the selected images are printed to the Log window. It is recommended to copy the code to the [Script Editor](/scripting/script-editor) and run it by yourself.

The following list links to documentation of the used Python features:

-   [Future statement definitions](https://docs.python.org/2/library/__future__.html)
-   [Built-in Functions](https://docs.python.org/2/library/functions.html)
-   [str.join()-method](https://docs.python.org/2/library/stdtypes.html#str.join)
-   [List Comprehensions](https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions)
-   [Generator Expressions](https://www.python.org/dev/peps/pep-0289/)
-   [`**` (double star) and `*` (star) parameters](http://stackoverflow.com/questions/36901/what-does-double-star-and-star-do-for-python-parameters)
-   [Top-level script environment (`__main__`)](https://docs.python.org/2/library/%5F%5Fmain%5F%5F.html)
-   [Purpose of the single underscore `_` variable](http://stackoverflow.com/questions/5893163/what-is-the-purpose-of-the-single-underscore-variable-in-python)

{% include code org='imagej' repo='imagej-scripting' branch='master' path='src/main/resources/script_templates/Tutorials/Wiki_Jython_Tutorial_1.py' %}

### Using Scripting Parameters

The second example is inspired by atomic resolution images recorded with an Transmission Electron Microscope (TEM). Such images show a regular structure (a crystal), but the images are noisy because of the low signal. By using a Fourier filter the contrast can be enhanced.

The script will create a periodic structure and add some random noise. The user can control the parameters of the created image. This is realized using [Script parameters](/scripting/parameters). The Fourier filtering has been created by using the [Recorder](/scripting/macro#the-recorder). Finally a simple image calculator is used to show that functions can be passed as parameters.

This list links to the documentation of Python features that are introduced with this example:

-   [The zip() function](https://docs.python.org/2/library/functions.html#zip)
-   [Rotating a two-dimensional array](http://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python)
-   [Lambda expressions](https://docs.python.org/2/reference/expressions.html#lambda)

{% include code org='imagej' repo='imagej-scripting' branch='master' path='src/main/resources/script_templates/Tutorials/Wiki_Jython_Tutorial_2.py' %}

### A batch opener using `os.walk()`

We have yet introduced some powerful functions build into Python. Another one is `walk()` from the `os` module. It can be used to go through a directory structure and process the contained files. In this example `walk()` is used to batch open images with ImageJ's function `openImage()`.

To read more about the used features, the following list provides links to additional information:

-   [The walk() function](https://docs.python.org/2/library/os.html#os.walk)
-   [The documentation of os.path](https://docs.python.org/2/library/os.path.html)
-   [The listdir() function](https://docs.python.org/2/library/os.html#os.listdir)
-   [Javadoc on IJ.openImage()](http://javadoc.imagej.net/ImageJ1/)
-   [Testing the type of an object using isinstance()](https://docs.python.org/2/library/functions.html#isinstance)
-   [Identifying the type of an object using type()](https://docs.python.org/2/library/functions.html#type)
-   [Using continue to control a loop](https://docs.python.org/2/reference/simple_stmts.html#continue)
-   [Truth Value Testing](https://docs.python.org/2/library/stdtypes.html#truth-value-testing)

{% include code org='imagej' repo='imagej-scripting' branch='master' path='src/main/resources/script_templates/Tutorials/Wiki_Jython_Tutorial_3.py' %}

## Importing Java module and classes

Another great feature of Jython is the possibility to use functions from Java jar package that resides in the jar folder of imageJ.

### ImageJ and Fiji API

The following API documentation lists all available modules and functions :

-   [ImageJ](http://javadoc.scijava.org/ImageJ1/)
-   [Fiji](http://javadoc.scijava.org/Fiji/)

Those package are built-in with Fiji, but any package that resides in the jars folder can be imported provided you know the path to the class.

For example, one of the main built-in ImageJ packages is called `ij`, and often Jython scripts will write something like this at the top:

    from ij import IJ
    # do stuff below....

Doing this allows you to access the `IJ` *class* which resides in the `ij` *package*. You can find a description of the `ij` package [here](https://javadoc.scijava.org/ImageJ1/ij/package-summary.html). What can we do with the `IJ` class? Clicking on the `IJ` link brings you to the [class documentation](https://javadoc.scijava.org/ImageJ1/ij/IJ.html) page for `IJ`. This class contains "static utility methods" which means you can call them with without instantiating (calling the constructor) the `IJ` class. We will cover constructors later. Looking through the documentation for `IJ`, lets focus on the method `createImage` ([docs here](https://javadoc.scijava.org/ImageJ1/ij/IJ.html#createImage-java.lang.String-int-int-int-int-)). This method can be called just like you would call a method on a python class. The documentation shows you need to provide the following parameters (types in parenthesis):

1.  title (string)
2.  width (int)
3.  height (int)
4.  depth (int)
5.  bitdepth (int)

and it returns an `ImagePlus` object. `ImagePlus` objects are very important in ImageJ, and you will the documentation for them [here](/ij/developer/api/ij/ImagePlus.html). Below is an example of how to import and use the static methods on the `IJ` class to create an image.

    from ij import IJ # read this as: "from the ij package import the IJ class"
    test_img = IJ.createImage("Test image", 512, 512, 1, 8)
    # now check the type of test_img
    print(type(test_img))
    # <type 'ij.ImagePlus'>

This code shows that we have successfully created an `ImagePlus` object. Looking at the documentation for the [ImagePlus class](https://javadoc.scijava.org/ImageJ1/ij/ImagePlus.html), let's use a few of the methods to make sure the image was created correctly.

    from ij import IJ
    test_img = IJ.createImage("Test image", 512, 512, 1, 8)
    # check the type:
    print(type(test_img))
    # <type 'ij.ImagePlus'>
    title = test_img.getTitle()
    width = test_img.width
    height = test_img.height
    print("{} is {} wide and {} tall.".format(title, width, height))
    test_img.show()

We accessed the title using the `getTitle()` [method](https://javadoc.scijava.org/ImageJ1/ij/ImagePlus.html#getTitle--), which takes no arguments and returns the image name. We accessed the image width and height by accessing `test_img`'s **fields**. These are not methods, but contain information about the class. We could have also used the `getWidth()` and `getHeight()` methods as well. We then called the `show()` method on our test image and a (very boring) 512X512 8 bit image should have popped up.

Here is another example where we use the ImageJ package and the [RoiManager](http://javadoc.scijava.org/ImageJ1/ij/plugin/frame/RoiManager.html) class. According to the javadoc, the RoiManager class resides in `ij.plugin.frame`. Therefore the code will look like :

    from ij.plugin.frame import RoiManager
    RM = RoiManager()        # we create an instance of the RoiManager class
    rm = RM.getRoiManager()  # "activate" the RoiManager otherwise it can behave strangely

### Using openCV in Jython

It is even possible to use most of opencv functionalities within Jython/Fiji. There are several options (see the [wiki page about opencv](/software/opencv)), yet the most straight forward is probably IJ-OpenCV which is available via the update sites. It will automatically download the necessary packages and dependencies in your Fiji installation.

A manual installation is also possible by putting the jar packages in the jar folder of imageJ. They are avalaible on the [IJopenCV github](https://github.com/joheras/IJ-OpenCV), which even provides a maven option.

#### Matrices

The first thing to know about OpenCV is that most functions work with an OpenCV matrix object. Fortunately, the IJ-OpenCV project provides some converters :

    #@ ImagePlus ImP
    from ijopencv.ij      import ImagePlusMatConverter
    from ijopencv.opencv  import MatImagePlusConverter
    from ij               import ImagePlus

    # Convert ImagePlus (actually the contained ImageProcessor) to Matrix object
    imp2mat = ImagePlusMatConverter()
    ImMat = imp2mat.toMat(imp.getProcessor())
    print ImMat

    # Convert Matrix object to ImageProcessor
    mat2ip = MatImagePlusConverter()
    NewIP  = mat2ip.toImageProcessor(ImMat)
    NewImp = ImagePlus("Matrix converted back to ImagePlus", NewIP)
    print NewImP

Such kind of converter is also available for PointRoi to opencv keypoints...

Now to use opencv function, we use the [JavaCPP API](http://bytedeco.org/javacpp-presets/opencv/apidocs/) that contains almost all functions of opencv.

    from org.bytedeco.javacpp.opencv_core   import Mat, CvMat, vconcat

    ## Typical matrices ##

    # Identity Matrix of size (3x3) and type 8-bit
    Id = Mat().eye(3,3,0).asMat()
    print Id
    print CvMat(Id) # handy to visualise the matrix

    # Matrix of ones (3x3)
    One = Mat().ones(3,3,0).asMat()

    # Matrix of zeros (3x3)
    Zero = Mat().zeros(3,3,0).asMat()

    # Custom Matrices
    # 1D-Matrix can be initialize from a list
    # For 2D (or more) we have to concatenate 1D-Matrices

    Row1 = Mat([1,2,3,4,5]) # 1D matrix
    Row2 = Mat([6,7,8,9,10])

    TwoColumn = Mat()              # initialise output
    vconcat(Col1, Col2, TwoColumn) # output stored in TwoColumn
    print CvMat(TwoColumn)

{% include notice icon="warning" content='The `org.bytedeco.javacpp.opencv_core.Mat` object is different than the `org.opencv.core.Mat` !! They don"t have exactly the same attributes and functions. In Fiji you should always use the objects from `org.bytedeco.javacpp`.' %}

Similarly there is some apparent redudancy for the function in the javacpp API.

ex : Transform exists in 3 different places :

-   `org.opencv.core.Core.transform`

This one takes `org.opencv.core.Mat` as input. It is currently challenging to have such object in Fiji.

-   `org.bytedeco.javacpp.opencv_core.cvTransform`

using `CvArr` as input, but even if you manage to convert your input as a `CvArr` it crashes Fiji. Apparently it is a deprecated version.

-   `org.bytedeco.javacpp.opencv_core.transform`

That's the one to use ! It takes only `org.bytedeco.javacpp.opencv_core.Mat` as input, which is the most approriate in Fiji/Jython

#### Scalar

In addition to Matrices, opencv allows to use Scalar objects A scalar is a 4 item element (v0, v1, v2, v3). If v1=v2=v3=0 then the Scalar is real.

    from org.bytedeco.javacpp.opencv_core   import Scalar

    # Real scalar can be initiated with a float parameters
    Number = Scalar(5.0)
    Number = Scalar(float(5))
    print Number

    # Using an integer as parameter has a different meaning
    Empty = Scalar(5) # This initiate an empty Scalar object of size 5
    print Empty

    # Alternatively one can set the other values of the Scalar
    Complex = Scalar(1,2,3,4)
    print Complex

#### Operations

It is possible to perform some operations between matrices, or between Scalar and matrices.

    from org.bytedeco.javacpp.opencv_core   import Scalar, Mat, subtract

    A = Mat([1,2,3,4,5])
    B = Mat([1,2,-3,-4,0])

    Number = Scalar(10.0)

    ## Number - B ( B-Number is also possible)
    Expr = subtract(Number,B)
    print CvMat(Expr.asMat())

    ## A - B
    Out = Mat()
    subtract(A,B,Out)
    print CvMat(Out)

## Self written Jython modules for ImageJ

In Jython you can write all commands line by line in a single file and execute it. To create a neat program, [functions](https://docs.python.org/2/tutorial/controlflow.html#defining-functions) and [classes](https://docs.python.org/2/tutorial/classes.html) can be used to structure code. To prevent using copy&past for regularly used functions and classes, [modules](https://docs.python.org/2/tutorial/modules.html) are the way to choose. Modules are files that contain functions and classes to import into other files.

To load modules, one has to save them to a directory where Jython will find them. Two lines of code will reveal these directories to you:

    from sys import path
    print(path)

When running this code the result is an output like

    ['/home/michael/Software/ImageJ.app/jars/Lib', '/home/michael/Software/ImageJ.app/jars/jython-shaded-2.7.0.jar/Lib', '__classpath__', '__pyclasspath__/']

This tells us that the folder `jars/Lib/` inside our ImageJ/Fiji directory is the right place to save modules. As `Lib/` does not exist by default, we have to create it.

When a module is imported for the first time, Jython will compile it to Java code. If there is a module named `myModule.py`, Jython will create a file called `myModule$py.class`. The next time the module is imported, the jython interpreter uses the `.class` file instead of the `.py` file, even if this `.py` file was modified.

To force the interpreter to use the last version of the py script there are 2 possibilities :

-   Close Fiji, delete the `myModule$py.class` file and restart Fiji
-   Use the following lines of code (found at [stackoverflow](http://stackoverflow.com/questions/10531920/jython-import-or-reload-dynamically)) that will force Jython to recompile all modules

<!-- -->

    # Use this to recompile Jython modules to class files.
    from sys import modules
    modules.clear()
    # Imports of Jython modules are placed below:
    import myModule

### Adding a custom directory

If you don't want to use `jars/Lib/` to save your modules, you have to extend the array `sys.path`:

    from sys import path
    from java.lang.System import getProperty

    # extend the search path by $FIJI_ROOT/bin/
    # 'fiji.dir' works for plain ImageJ, too.
    path.append(getProperty('fiji.dir') + '/bin')
    # an alternative can be the users home directory
    # path.append(getProperty('user.home') + '/JythonModules')

    # Now you can import $FIJI_ROOT/bin/myModule.py
    import myModule

The function `getProperty()` accepts many more strings. A list can be found at [The Java Tutorials](https://docs.oracle.com/javase/tutorial/essential/environment/sysprop.html).

## Self written Jython packages for ImageJ

On the way to perfectly organize Jython code, [packages](https://docs.python.org/2/tutorial/modules.html#packages) are the next step. A Jython package is a folder that contain a set of modules scripts together with a `__init__.py` file. This file can be empty. Below is a typical structure for the `Imagej.app/jars/Lib` folder:

    Imagej.app/jars/Lib/
    -- myModule.py
    -- myPackage/
       -- __init__.py
       -- mathTools.py
       -- customFilters.py
       -- fftTools.py
    -- myPackage2/
       -- __init__.py
       -- mathTools.py
       -- stackProcessing.py

There are two packages and one module. The first package contains three modules and the second package contains two modules. We can import the modules on different ways:

    # Import the single module using the default name:
    import myModule

    # Import mathTools from the first package
    import myPackage.mathTools
    # Use a function from the imported module
    myPackage.mathTools.aFunction()

    # Import mathTools from the second package
    from myPackage2 import mathTools
    # Use a function from the imported module without prefixing the package
    mathTools.aFunction()

    # Import customFilters from the first package and rename it
    from myPackage import customFilters as filters
    # Use a function from customFilters.py
    filters.aFunction()

    # Importing all module from a package
    from myPackage2 import *
    # The next line will fail
    stackProcessing.aFunction()

The reason for the last import to fail is the empty `__init__.py`. We have to define which modules of the package are imported when using `import *`. This is done by setting the variable `__all__` in the `__init__.py`. For `myPackage2` this line of code is needed:

    __all__ = ["mathTools", "stackProcessing"]

Besides setting this variable, the `__init__.py` file can contain normal Jython code that is executed upon import of the package.

## Bundle packages in a JAR file

An interesting feature of Jython is to search for packages and modules inside of {% include wikipedia title="JAR (file format)" %}. The folder structure from the last section can be modified by packing everything into a single `myPackages.jar`. The name of the JAR file doesn't matter. All imports work the same as explained before.

    Imagej.app/jars/Lib/
    -- myPackages.jar
       -- myModule.py
       -- myPackage/
          -- __init__.py
          -- mathTools.py
          -- customFilters.py
          -- fftTools.py
       -- myPackage2/
          -- __init__.py
          -- mathTools.py
          -- stackProcessing.py

The advantage of this approach is that you can share your packages easily. For example you can upload the JAR file to an [update site](/update-sites). It is possible to upload .py scripts to update sites too, without packaging into a jar. The advantage of jar are that they allow to define dependencies more systematically.

**NB** : Script implementing "ImageJ menu macro" and "utilitary scripts" that are used as imported modules in other macros **should be packed in separate jar files** ! Indeed, if not explicitly mentioned, the jython interpreter only looks in the Jars/Lib folder to import module, so the .jar containing the "utilitary scripts" should be put there, while the jar containing the "ImageJ menu macro" can be put either in the Plugin or script/Plugin folder in order to appear in the ImageJ menu.

Contrary to the scripts in Jars/Lib, the menu macro scripts are not compiled, and as explained above they can not be imported in other scripts since the Plugin folder do not reside in the Jython search path by default.

This is the reason why a given project is rather distributed in 2 different jar files as explained [here](http://forum.imagej.net/t/using-self-written-jython-modules-in-imagej/2280).

### Using maven to build packages

Using maven you can automate the packaging of Jython code into JAR files. This approach is only recommended if you already use maven, as installing and learning how to use maven is not worth the time saving of automated packaging.

At GitHub you will find an [example project](https://github.com/m-entrup/imagej-jython-package) that you can use as a template. Just run `mvn package` and maven will generate a JAR file at the `target` directory.

## Links

-   [Jython Scripting Examples](/scripting/jython/examples)
-   [ImageJ2 Python Scripts](/tutorials/imagej2-python)
-   [A Fiji Scripting Tutorial by Albert Cardona](https://www.ini.uzh.ch/~acardona/fiji-tutorial/)
-   [Jython scripting cookbook](http://wiki.cmci.info/documents/120206pyip_cooking/python_imagej_cookbook)
-   [ImageJ tutorials repository](https://github.com/imagej/tutorials/tree/master/howtos/src/main/java/howto)

## References

[^1]: [Wikipedia entry on Jython](/ij/plugins/index.html). Accessed: 2016-08-30
