---
mediawiki: Moving_Least_Squares
title: Moving Least Squares
project: /software/fiji
categories: [Tutorials]
doi: 10.1145/1179352.1141920
artifact: sc.fiji:VIB_
---

This plugin implements the algorithms described in (Schaefer 2006)[^1] to deform an image given a set of landmarks.

## Tutorial

Load the original and choose the landmarks:

![](/media/plugins/mls-orig.jpg)

By clicking on the menu entry {% include bc path='Edit | Selection | Add to Manager'%} add this landmark set to the ROI Manager:

![](/media/plugins/mls-roi-manager.jpg)

Duplicate the image ({% include bc path='Image | Duplicate...'%}), click on the selection in the ROI manager and move the landmarks to their target location:

![](/media/plugins/mls-new1.jpg)

Now, run the plugin:

![](/media/plugins/mls-dialog.jpg)

And you get the result:

![](/media/plugins/mls-new2.jpg)

## References

{% include citation fn=1 %}
