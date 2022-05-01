---
mediawiki: How_to_apply_a_common_operation_to_a_complete_directory
title: How to apply a common operation to a complete directory
---

## How to apply a common operation to a complete directory

Often you want to apply a common operation to all images in a given directory. This tutorial tries to help you doing this. In addition, the [Script Editor](/scripting/script-editor) provides a template via {% include bc path='Templates | IJ1 Macro | Process Folder'%} that helps getting started quickly.

## Step 1: record a macro

First, start the Macro Recorder:

![](/media/tutorials/how-to-apply-a-common-operation-to-a-complete-directory-1.jpg)

This will open the Macro Recorder window:

![](/media/tutorials/how-to-apply-a-common-operation-to-a-complete-directory-2.jpg)

Now perform the operation on a single image. Make sure that you save the image at the end.

Exmaple: cropping the image. First, select a rectangle:

![](/media/tutorials/how-to-apply-a-common-operation-to-a-complete-directory-3.jpg)

Then crop it.

![](/media/tutorials/how-to-apply-a-common-operation-to-a-complete-directory-4.jpg)

After saving, the recorder window will show this:

![](/media/tutorials/how-to-apply-a-common-operation-to-a-complete-directory-6.jpg)

Click on the **Create** button, and you will get this:

![](/media/tutorials/how-to-apply-a-common-operation-to-a-complete-directory-7.jpg)

## Step 2: Make the macro generic

The problem now is that this macro contains the verbatim name of the file you saved, but of course, you do not want to save *all* the files in the direcotry as *clown.jpg*!

The solution is to wrap the macro in a function which takes a *placeholder* for the file name. Let's call that function *action*:

```javascript
function action(output, filename) {
        makeRectangle(10, 10, 300, 180);
        run("Crop");
        saveAs("Jpeg", output + filename);
}
```

As you can see, the full path to the file we saved which was enclosed in quotes by the Recorder (*"/home/fiji/images/clown.jpg"*) was cut down to the full path to the output directory and the file name appended with a *plus* operator (*output + filename*), which are passed as so-called *parameters* to the function.

The reason is that you want ImageJ to save the processed image with a variable name. For a single image, the function would be called like this:

```javascript
action("home/fiji/output-images/", "bridge.gif");
```

Now, let's enhance the function so that it opens the image itself, and also closes the image after it saved the result:

```javascript
function action(input, output, filename) {
        open(input + filename);
        makeRectangle(10, 10, 300, 180);
        run("Crop");
        saveAs("Jpeg", output + filename);
        close();
}
```

The function takes three parameters now: the input and output directories and the file name. These need to be three parameters because the image should be saved into a different directory than the original came from (so that the output images will not be mistaken for input images in subsequent runs of the final macro).

## Step 3: Iterating over all images in a given directory

After defining the generic *action* function, you can call it on each image in an input directory:

```Fjavascript
input = "/home/fiji/input/";
output = "/home/fiji/images/";
```
  
```javascript
list = getFileList(input);
for (i = 0; i < list.length; i++){
        action(input, output, list[i]);
}
```

Now, this is a little more complicated: First, a variable *input* is defined. The reason is that the input directory is not only needed to get the list of images, but also to pass to the *action* function.

To make the macro easier to modify, also the output directory is stored in a variable (with the name *output*).

The next line defines a variable *list*, which takes the result of the builtin function *getFileList*. The result is a so-called *array*, a list that contains a number of *list.length* items, indexed by the numbers *0, ..., list.length-1*. These items are the names of the files in the given *input* directory.

The *for* loop does nothing else than assigning the integral numbers *0, ..., list.length-1* to the variable *i* and executing the lines between { and } with each setting.

The line executed in the *for* loop calls the *action* function with the *i*th file name in the directory list, obtained by *list[i]*.

Sometimes, ImageJ can get confused when it has to open or close windows and perform operations on them, in which case it can appear as if operations are called out of order. To prevent that, enable the *batch mode*:

```javascript
input = "/home/fiji/input/";
output = "/home/fiji/images/";
```
  
```javascript
setBatchMode(true); 
list = getFileList(input);
for (i = 0; i < list.length; i++){
        action(input, output, list[i]);
}
setBatchMode(false);
```

## Alternative: Multiple Image Processor

If your macro does not use the actual name of the image (as e.g. the Image Calculator does), you can use the *Multiple Image Processor* plugin.

To be able to use this plugin, you need to save the macro into a file; this macro needs to perform the actions directly, i.e. there can be a function in the file, but it must be called after being defined. However, it is usually easier to adjust the output of the Macro Recorder just a little.

In our case, the file would simply contain these lines:

```javascript
makeRectangle(10, 10, 300, 180);
run("Crop");
```

Find the *Multiple ImageProcessor* plugin in the *Process* menu:

![](/media/tutorials/how-to-apply-a-common-operation-to-a-complete-directory-8.jpg)

The dialog would need to be filled out like this:

![](/media/tutorials/how-to-apply-a-common-operation-to-a-complete-directory-9.jpg)
