---
mediawiki: Edit_LUT_As_Text
name: "Edit LUT As Text"
title: Edit LUT As Text
dev-status: "stable"
team-founder: '@dscho'
team-maintainer: '@dscho'
---


{% capture source%}
{% include github repo='fiji' branch='master' path='plugins/Examples/Edit_LUT_As_Text.py' %}
{% endcapture %}
{% include info-box source=source %}

# Purpose

Demonstrate how to call ImageJ's editor and extend the menu in a Jython script.

It also helps you to edit the current lookup table as a list of triplets denoting the red/green/blue values.

You can also use the script to import lookup tables you have in the form of 256 red/green/blue triplets.
