---
mediawiki: 3Dscript
title: 3Dscript
categories: [Visualization]
doi: 10.1038/s41592-019-0359-1
---


{% capture maintainer%}
{% include person id='bene51' %}
{% endcapture %}

{% capture author%}
{% include person id='bene51' %}
{% endcapture %}

{% capture source%}
{% include github org='bene51' repo='3Dscript' %}
{% endcapture %}
{% include info-box software='Create high-quality 3D/4D animations using a natural-language based syntax' logo='<img src="/media/logos/3dscript.png" width="160">' name='3Dscript' maintainer=maintainer author=author source=source status='active' released='January 2019' category='Visualization, Plugins' %}

In state-of-the-art 3D rendering and animation software the user typically creates an animation by specifying a number of keyframes. While intuitive, this approach becomes tedious for complex motions like simultaneous rotations around multiple axes, and even worse for accelerated and decelerated motions: The number of required keyframes increases, and creating them becomes hardly reproducible.

In 3Dscript, animations are defined by a syntax based on natural English language, in sentences such as "From frame 0 to frame 100 rotate by 360 degrees horizontally ease-in".

![](/media/plugins/3dscript-wiki-01.jpg)

## Publication

{% include citation %}

## Installation

-   Click on {% include bc path="Help|Update..." %}
-   Click on Manage update sites
-   Check the box in front of '3Dscript'
-   Click on Close
-   Click on Apply changes
-   Restart Fiji

## Quick start

-   Click on {% include bc path="File|Open Samples|T1 Head" %}
-   Click on {% include bc path="Plugins|3D script|Interactive Animation" %}
-   In the "Interactive Raycaster" window, click on "show" next to "Animation"
-   Click on "Start text-based animation editor"
-   In the editor window, type the following text: From frame 0 to frame 200 rotate by 360 degrees horizontally
-   Click on "Run" This will render 200 frames of a movie sequence, within which the MRI data set rotates by 360 degrees.

Rendering of 200 frames of this data set will typically take less than a minute on an OpenCL-enabled Graphics Card. The resulting stack can be saved as a video file using Fiji's {% include bc path="File|Save As|AVI..." %} command.

To run the software on another data set, open a different image stack (instead of the T1 Head sample data) before running 3Dscript.

More information is available at [https://bene51.github.io/3Dscript](https://bene51.github.io/3Dscript).

## User documentation

See 3Dscript in action below:

{% include video platform='youtube' id='eRrSoAubv6w'%}

More examples can be found on [https://bene51.github.io/3Dscript/gallery.html](https://bene51.github.io/3Dscript/gallery.html).

A full manual as [PDF](https://bene51.github.io/3Dscript/Manual.pdf).

  
