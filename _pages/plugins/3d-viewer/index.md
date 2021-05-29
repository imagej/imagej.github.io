---
mediawiki: 3D_Viewer
title: 3D Viewer
categories: [Visualization]
artifact: sc.fiji:3D_Viewer
doi: 10.1186/1471-2105-11-274
---

This plugin offers hardware-accelerated visualization possibilities for image stacks, using the [Java 3D](/libs/java-3d) library. Stacks can be displayed as texture-based volume renderings, surfaces or orthoslices.

![](/media/3d-viewer-overview.png)

## Screencasts

Here you are a demo screencast separated into two different videos (\~15 min in total) showing many of the features of the 3D viewer:

{% include video platform='youtube' id='cD3Hc3NYkaU'%} {% include video platform='youtube' id='GqG\_RcK3kYg'%}

Beyond this, a lot more screencasts can be found [here](/plugins/3d-viewer/screencasts), covering the following topics:

-   Display stacks
-   Rendering modes and attributes
-   Adjusting the transfer functions
-   Editing volumes
-   Point lists
-   Landmark-based registration
-   Transformations
-   3D Content in PDFs

## For users

Comprehensive usage guidelines in form of FAQs and tutorials can be found [here](/plugins/3d-viewer/user-faqs).

## For developers

A lot of functions of the 3D Viewer are macro-recordable. However, if that is not enough (or if the function is not recorded properly), it is better to [write a plugin](/develop/ij1-plugins). In the latter case no macros should be called from Java, as that would limit the code to work with the currently active 3D Viewer (even if the user clicked somewhere else).

This code snippet should get you started:

    Image3DUniverse univ = new Image3DUniverse();
    univ.show();
    univ.addMesh(yourImagePlus, null, "somename", 50, new boolean[] {true, true, true}, 2);
    ...

Full documentation for developers with tutorials and explained code snippets can be found [here](/plugins/3d-viewer/developer-documentation).

### Javadocs

The Fiji Javadocs provide detailed information about the {% include javadoc package='ij3d' class='package-summary' label='3D Viewer API' %}.

## FAQ

### The 3D Viewer opens a window saying *An unexpected exception occurred.*

If in the same window, it also says:

`java.lang.NullPointerException:Canvas3D: null GraphicsConfiguration`

the reason is most likely that your graphics setup does not have any hardware 3D acceleration. This can happen e.g. when you run ImageJ via a remote X11 connection (3D acceleration works only when the graphics are displayed on the same machine as the program runs).

Unfortunately, there is not workaround/fix for this situation yet, except to use ImageJ locally when you want to use the 3D Viewer.

### Problem with Intel graphics cards

There is a known problem with older Windows drivers for some Intel graphics cards. Usually, this is fixed by installing new drivers. If you would like to help make ImageJ nicer by detecting faulty driver versions, please [contact us](/discuss).

### The 3D Viewer simply crashes

Unfortunately, there are quite a large number of possible reasons. Please help us by [debugging the issues](/develop/debugging#debugging-java3d-issues) and [contacting us](/discuss) with the information. You can also [report a bug](/discuss/bugs), which will provide a lot of additional, potentially useful information.

### Only a gray rectangle is shown by the 3D Viewer

As with 3D Viewer crashes, there are quite a large number of possible reasons. Please help us by [debugging the issues](/develop/debugging#debugging-java3d-issues) and [contacting us](/discuss) with the information. You can also [report a bug](/discuss/bugs), which will provide a lot of addidtional, potentially useful information.

## Publication

{% include citation %}
