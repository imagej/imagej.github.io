---
mediawiki:
- Spirals_(Macro)
- Spirals
title: Spirals
categories: Tutorials
---

The {% include github repo='fiji' branch='master' path='plugins/Scripts/File/Open_Samples/Spirals_.ijm' label='Spirals macro' %} shows an optical illusion demonstrating that our vision is optimized for non-quantitative measurements. It is designed to dispel the all-too-common idea that human beings are able to quantify color. The perception of colors depends highly on the context (i.e. the surrounding colors). If you ever hear a scientist say: <span style='font-size: 20px;'>"But I can see it!"</span> show them this image. It is an example of [Munker's illusion](http://engineering.utep.edu/novick/colors/).

![](/media/spiralsrgy.png)

In the generated image, the human eye perceives some yellow and some green-yellow bands, but they have exactly the same color.

## The macro

Any self-respecting scientist will doubt your statement. This is where the source code comes in. In Fiji, press the {% include key key='Shift' %} key and then open {% include bc path='File | Open Samples | Spirals (macro)'%} which will open the macro in the [Script Editor](/scripting/script-editor) instead of running it directly. Alternatively, you can drag & drop [this link](https://raw.github.com/fiji/fiji/master/plugins/Scripts/File/Open_Samples/Spirals_.ijm) to your main window.

You can inspect the source code, run it, change it, run it again. This is the proper scientific way to convince yourself that the spiral arms have indeed the exact same color.

The macro originally illustrated this idea with blue versus green, rather than green versus yellow:

![](/media/spirals.png)

But it was changed to address the objection: "Yeah, but I want to quantify red versus green."

## Take home message

You cannot quantify color by eye. Nobody can. The only thing you can quantify by eye are written-out numbers.

See also [this wired article](http://www.wired.com/2015/02/science-one-agrees-color-dress/).
