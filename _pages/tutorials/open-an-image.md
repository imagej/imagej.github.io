---
mediawiki: Open_an_image
title: Open an image
section: Learn:ImageJ Basics
---

**How to open an image in ImageJ2?**

The answer to this question depends on how you use ImageJ.

-   Do you want the open an image using the graphical user interface?
-   Are you writing a script?
-   Are you using Java, to develop an ImageJ2 plug-in or do write your one program using ImgLib2 and ImageJ libraries?

## From the GUI

In the menu select {% include bc path="File | Open..." %} or {% include bc path="File | Import | ..." %}.

## From a Script

What are then possible ways to open an image when you are writing an Python / Groovy / ... script in ImageJ?

### Use a parameter of type Dataset

When the following script is run in ImageJ. ImageJ will ask to user to select two Images, before it runs the script.

    #@ Dataset firstImage
    #@ Dataset secondImage
    #@ UIService ui
    ui.show(firstImage)
    ui.show(secondImage)

### Use the DatasetIOService

    #@ DatasetIOService io
    #@ UIService ui
    path = "/path/to/image.tif"
    image = io.open(path)
    ui.show(image)

## From Java

```java
import net.imagej.ImageJ;
...
ImageJ ij = new ImageJ();
Object image = ij.io().open("/path/to/image.tif");
// OR, if you need to know the object will be a Dataset:
Dataset dataset = ij.scifio().datasetIO().open("/path/to/image.tif");
```
