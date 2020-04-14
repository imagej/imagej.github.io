---
title: 3D Viewer
author: Curtis Rueden
category: Analysis
layout: page
---

![3D Viewer Overview](../images/posts/3D_Viewer_overview.png){: .image.fit}

This plugin offers hardware-accelerated visualization possibilities for image stacks, using the [Java 3D](https://imagej.net/Java_3D) library. Stacks can be displayed as texture-based volume renderings, surfaces or orthoslices.

## **Screencasts**
<hr>

Here you are a demo screencast separated into two different videos (~15 min in total) showing many of the features of the 3D viewer:

<div class="video-wrapper">
    <iframe width="100%" height="100%" src="https://www.youtube.com/embed/cD3Hc3NYkaU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

<br>

<div class="video-wrapper">
    <iframe width="100%" height="100%" src="https://www.youtube.com/embed/GqG_RcK3kYg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

<br>

Beyond this, a lot more screencasts can be found [here](https://imagej.net/3D_Viewer:_Screencasts), covering the following topics:

- Display stacks
- Rendering modes and attributes
- Adjusting the transfer functions
- Editing volumes
- Point lists
- Landmark-based registration
- Transformations
- 3D Content in PDFs

## **For users**
<hr>

Comprehensive usage guidelines in form of FAQs and tutorials can be found [here](https://imagej.net/3D_Viewer:_User_FAQs).

## **For developers**
<hr>

A lot of functions of the 3D Viewer are macro-recordable. However, if that is not enough (or if the function is not recorded properly), it is better to [write a plugin](https://imagej.net/Introduction_into_Developing_Plugins). In the latter case no macros should be called from Java, as that would limit the code to work with the currently active 3D Viewer (even if the user clicked somewhere else).

This code snippet should get you started:

```
Image3DUniverse univ = new Image3DUniverse();
univ.show();
univ.addMesh(yourImagePlus, null, "somename", 50, new boolean[] {true, true, true}, 2);
...
```

Full documentation for developers with tutorials and explained code snippets can be found [here](https://imagej.net/3D_Viewer:_Developer_Documentation).

## **Javadocs**
<hr>

The Fiji Javadocs provide detailed information about the [3D Viewer API](https://javadoc.scijava.org/ImageJ/ij3d/package-summary.html).

## **FAQ**
<hr>

### **_The 3D Viewer opens a window saying An unexpected exception occurred._**

If in the same window, it also says:

```
java.lang.NullPointerException:Canvas3D: null GraphicsConfiguration
the reason is most likely that your graphics setup does not have any hardware 3D acceleration. This can happen e.g. when you run ImageJ via a remote X11 connection (3D acceleration works only when the graphics are displayed on the same machine as the program runs).
```

Unfortunately, there is not workaround/fix for this situation yet, except to use ImageJ locally when you want to use the 3D Viewer.

### **_Problem with Intel graphics cards_**

There is a known problem with older Windows drivers for some Intel graphics cards. Usually, this is fixed by installing new drivers. If you would like to help make ImageJ nicer by detecting faulty driver versions, please [contact us](https://imagej.net/Contact).

### **_The 3D Viewer simply crashes_**

Unfortunately, there are quite a large number of possible reasons. Please help us by [debugging the issues](https://imagej.net/Debugging_intro#Debugging_Java3D_issues) and [contacting us](https://imagej.net/Contact) with the information. You can also [report a bug](https://imagej.net/Report_a_Bug), which will provide a lot of additional, potentially useful information.

### **_Only a gray rectangle is shown by the 3D Viewer_**

As with 3D Viewer crashes, there are quite a large number of possible reasons. Please help us by [debugging the issues](https://imagej.net/Debugging_intro#Debugging_Java3D_issues) and [contacting us](https://imagej.net/Contact) with the information. You can also [report a bug](https://imagej.net/Report_a_Bug), which will provide a lot of addidtional, potentially useful information.

## **Publication**
<hr>

- Schmid, B.; Schindelin, J. & Cardona, A. et al. (2010), "[A high-level 3D visualization API for Java and ImageJ](http://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-11-274)", _BMC Bioinformatics_ **11(1)**: 1, PMID 20492697, doi:[10.1038/nmeth.3392](http://dx.doi.org/10.1038%2Fnmeth.3392) ([on Google Scholar](http://scholar.google.com/scholar?cluster=5464881898236181205)).