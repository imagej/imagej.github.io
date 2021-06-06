---
title: Save as animated gif
section: Learn:File Formats
categories: [Import-Export]
artifact: sc.fiji:IO_
name: Save as animated gif
---

1.  Go to menu {% include bc path='Images | Stacks | Tools | Animation options...'%}
2.  In the dialog, set the desired frames per second, or "Speed".
3.  Select the stack to save, and go to menu {% include bc path='File | Save As | Animated Gif ...'%}

Done!

**PS.** in order to include overlays in the animated gif, such as ROI or scale bar overlays, these must first be converted to pixel data by flattening the image.

1.  Go to menu {% include bc path='Image | Overlay | Flatten' %}

or use {% include key keys='Ctlcmd|Shift|F' %}.
