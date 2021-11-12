---
title: Labkit - Frequently Asked Questions
---

**Is it possible to manually segment a 3D image slice by slice?**

Yes, this can be achieved by a workaround: Simple convert your image to 2D+time before opening it with Labkit. In Fiji use "Image > Hyperstacks > Re-order Hyperstack ..." to convert your image from 3D to 2D+time.

**After starting Labkit the window that should show my image is black?**

This often happens if Labkit can't find proper brightness & contrast settings. Please click the button that says "auto contrast".

**How I manually select the colors and brightness settings that are used to show the image?**

Click {% include key key='S' %} on your keyboard. This should show the BigDataViewer brightness & color dialog. Use it to manually adjust those settings.

**Can Labkit distinguish more than two classes "foreground" and "background"**

Yes, simple click the "Add label" button this will add a new class. You are free to name labels / classes as you would like, simple double click on the label.

**How can I change the color of the labels?**

Just click on the colored rectangle left of the labels name. This will show a color selection dialog.
