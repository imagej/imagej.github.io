---
mediawiki: The_Hue_Game
title: The Hue Game
---

{% include info-box software='ImageJ' name='The Hue Game' maintainer='Johannes Schindelin' author='Johannes Schindelin' source=' [in GitWeb](https://fiji.sc/cgi-bin/gitweb.cgi?p=fiji.git;a=blob;f=plugins/Examples/The_Hue_Game.bsh;hb=refs/heads/master)' released='16/04/2012' latest-version='16/04/2012' status='stable' website='http://www.xrite.com/custom\_page.aspx?PageID=77&Lang=en' %}

## The Hue Game

This game is based on an online demonstration of [xrite.com](http://www.xrite.com/custom_page.aspx?PageID=77&Lang=en) and is included in Fiji to demonstrate a couple of things:

-   Humans' color perception is a tricky thing (take home lesson: use color maps to analyze images visually)
-   how to override ImageJ 1.x's mouse listeners from a script
-   that you can have fun in Fiji

It is also educating to play with the hues that are displayed. The script represents colors in the {% include wikipedia title='CIELAB' text='CIELab space'%}. The *L* axis represents the luminance. The *a* and *b* axes represent the hue (*a* is often referred to as the green/red axis and *b* as yellow/blue one, but this is not quite an accurate notion).

The four grid lines of the game display evenly spaced color samples along the sides of a quadrilateral in the plane defined by *L = 72*.

To play with the script, hold down the {% include key key='Shift' %} key and then open the {% include bc path='Plugins | Examples'%} menu and click on *The Hue Game* (hold the {% include key key='Shift' %} key pressed down all while doing that). This will open the script in the [Script Editor](/scripting/script-editor). Just change the numbers in the second-to-last line of the script (the *72* is the luminance, the next parameter is a list of the *a* coordinates of the quadrilateral, followed by the *b* coordinates). Then call the script with *Run&gt;Run*.


