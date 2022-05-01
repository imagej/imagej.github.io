---
mediawiki: Replace_Red_with_Magenta
title: Replace Red with Magenta
categories: [Tutorials]
---


{% capture maintainer%}
{% include person id='dscho' %}
{% endcapture %}

{% capture source%}
{% include github org='fiji' repo='Fiji_Plugins' branch='master' source='fiji/color/Convert_Red_To_Magenta.java' %}
{% endcapture %}
{% include info-box software='ImageJ' name='Replace Red with Magenta' maintainer=maintainer author='Johannes Schindelin' source=source released='27/06/2011' latest-version='27/06/2011' status='' category='Plugins' %}

This plugin converts all occurrences of red in a red/green image with magenta, effectively replacing it with a magenta/green merge.

Note: the plugin completely ignores the blue channel, and replaces it with a copy of the red channel.

Example:

|                            |                                            |
|----------------------------|--------------------------------------------|
| ![](/media/clown.jpg) | ![](/media/plugins/clown-magenta.jpg) |

## Replace Red with Magenta (system clipboard)

Frequently all you [want](#Why.3F) to do is to replace red by magenta in some images in a text document or a presentation. With this function, you only need to copy the image into the system clipboard in the other program, call this plugin in Fiji, and then you can paste the corrected image in the other program.

## Why?

8% of the male population is red-green blind. If given the task to find two colors maximizing the number of people who cannot see the difference, red and green are a wise choice. Yet, still way too many figures in scientific publications show red/green merges.

At least magenta/green images help this situation. However, [the only thing human eyes can quantify are numbers](/plugins/spirals).

As a demonstration, call Fiji's {% include bc path='File | Open Samples | Spirals'%} and if you see a bright green and a bright yellow in the dominant spirals, you should look closer.

However, in the 21st century, one should always use proper [Colocalization](/imaging/colocalization-analysis) with scatter plots and statistics. It is [too easy not to](/plugins/coloc-2).

 
