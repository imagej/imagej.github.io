---
mediawiki: Edit_LUT_As_Text
title: Edit LUT As Text
---


{% capture source%}
{% include github repo='fiji' branch='master' path='plugins/Examples/Edit\_LUT\_As\_Text.py' %}
{% endcapture %}
{% include info-box software='ImageJ' name='Edit LUT As Text' author='Johannes Schindelin' maintainer='Johannes Schindelin' source=source status='stable' %}

# Purpose

Demonstrate how to call ImageJ's editor and extend the menu in a Jython script.

It also helps you to edit the current lookup table as a list of triplets denoting the red/green/blue values.

You can also use the script to import lookup tables you have in the form of 256 red/green/blue triplets.
