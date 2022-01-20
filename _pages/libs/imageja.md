---
title: ImageJA
icon: /media/icons/imagej.png
project: /software/imagej
source-url: https://github.com/imagej/ImageJA
---

{% include warning/deprecated old="ImageJA" new="[ImageJ](/software/imagej)" %}

ImageJA was a project providing a clean [Git](/develop/git) history of the
[ImageJ](/software/imagej) project, with a proper `pom.xml` file so that it
could be used with [Maven](/develop/maven) without hassles.

Releases of ImageJ up to 1.53j were published to [Maven](/develop/maven)
repositories via ImageJA, but starting with ImageJ 1.53k, releases are now
built and deployed directly from the
[primary ImageJ repository on GitHub](https://github.com/imagej/ImageJ).

## Historical note

ImageJA was originally
[launched in 2005](https://list.nih.gov/cgi-bin/wa.exe?A2=IMAGEJ;cd841de0.0510)
as a *fork* of [ImageJ](/software/imagej); i.e., it was synchronized closely
with ImageJ with a few changes on top:

-   When run as an applet, ImageJA is embedded.
-   The internal structure of ImageJA's recorder allows command listeners to
    get much more fine-grained information.
-   When launching a text editor, in many cases ImageJA will now choose Fiji's
    Script Editor, if available, instead of the old AWT based ImageJ editor.
-   ImageJA has an easy Plugin installer via {% include bc path='Plugins |
    Install PlugIn...'%} (ImageJ only has that drag-n-drop thingie).
-   The instance listener is RMI-based with ImageJA, so there is no security
    issue with it.
-   ImageJA's Command Launcher has fuzzy matching, too.
-   A couple of bug fixes:
    -   JavaScript in ImageJA can find plugin classes, too.
    -   ImageJA also put back some not-yet-deprecated methods as deprecated.
    -   A simple bug fix in PolygonRoi drawing (it moves to the first point,
        but then draws a line to the same first point rather than the second).
    -   A little bug fix in StackWindow: if you have a 2D time lapse, ImageJ
        will still use the zSelector (rather than the tSelector).
    -   ImageJA can handle https:// URLs, too.

However, nowadays, the [ImageJ2](/software/imagej2) project applies needed
changes to ImageJ via runtime patching; see the
[ImageJ Legacy](/libs/imagej-legacy) page for details.
