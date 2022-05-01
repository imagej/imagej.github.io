---
mediawiki: IJ_Robot
title: IJ Robot
project: /software/fiji
categories: [Uncategorized]
artifact: sc.fiji:IJ_Robot
---

This plugin calls the Robot Java class. The purpose of the plugin is to allow the macro language to control other programs via clicking and key presses.

See also:

{% include link-banner url="https://blog.bham.ac.uk/intellimic/g-landini-software/" %}

## Use

When running the plugin one must specify an 'order' to the robot and some parameters (not all orders require all the parameters):

**Move**: moves the mouse to a particular position (x, y) on the screen.

**\[Left\|Middle\|Right\]\_Click**: Clicks the mouse at a given (x, y) postion with the chosen button.

**Delay**: this is the time in milliseconds that the button is down during a click.

**\[Left\|Middle\|Right\]\_Down**: presses the chosen button at the current position (this order does not read the x, y coordinates).

**\[Left\|Middle\|Right\]\_Up**: releases the chosen button at the current position (this order does not read the x, y coordinates).

**KeyPress**: this order will emulate typing the entered string, but will first Click (at the current position), so the cursor is guaranteed to focus in an entry box (maybe this click is not required, please send feedback or suggestions). KeyPress currently supports the following key presses: 0-9 a-z A-Z space /.,-

To emulate the \[enter\] key, type the exclamation mark '!'. Other characters are converted to '.' Note that in macOS with an AZERTY keyboard, the typed string does not get interpreted correctly. Be also aware that some OS do not support some key presses.

**GetPixel**: reports to the Log window the r,g,b values of the pixel at the specified postion (requires x, y coordinates). It will also return the Width and Height of the screen, as well as the coordinates of the pixel.

**CaptureScreen**: this is similar to the IJ function {% include bc path='Plugins | Utilities | Capture Screen'%}.

A handy way to find the target coordinates is to first grab the screen (which opens as an image in IJ) and check the coordinates with the mouse in IJ (reported in the status bar).

## Important

Be careful with this plugin. It is really easy to end up clicking in unintended places with undesired results. You have been warned!

It may be necessary to increase the delay time for clicking orders depending on what is needed to be done and the response time of the target program.

It may be also necessary to slow down the macro calls to this plugin between orders by using the macro command: wait(time\_in\_milliseconds). For instance if you are grabbing an image with an external programme, the grab function may not be available while the snapshot is being taken.

The included demo, seems to work fine in various platforms. Make sure that there are no open images in IJ and that please do not move the mouse while running the macro.

## Menu Path

{% include bc path='Plugins | Utilities (2nd on the list!) | IJ Robot'%}


