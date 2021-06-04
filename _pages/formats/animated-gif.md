---
title: Save as animated gif
section: Learn:File Formats
categories: [Tutorials]
---


{% capture source%}
{% include github org='fiji' repo='IO' branch='master' source='io/Gif\_Stack\_Writer.java' %}
{% endcapture %}
{% include info-box software='ImageJ' name='Save as animated gif' author='Ryan Raz' maintainer='Johannes Schindelin' filename='IO\_.jar' source=source latest-version='March 2002' status='stable' category='[Import/Export](/plugin-index#import-export)' %}

1.  Go to menu {% include bc path='Images | Stacks | Tools | Animation options...'%}
2.  In the dialog, set the desired frames per second, or "Speed".
3.  Select the stack to save, and go to menu {% include bc path='File | Save As | Animated Gif ...'%}

Done!

**PS.** in order to include overlays in the animated gif, such as ROI or scale bar overlays, these must first be converted to pixel data by flattening the image.

1.  Go to menu {% include bc path='Image | Overlay | Flatten'%}

or use `Ctrl+Shift+F`.

 
