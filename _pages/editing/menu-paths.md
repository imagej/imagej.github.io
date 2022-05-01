---
title: Menu Paths
section: Contribute:Editing the Wiki
nav-links: true
---

This page demonstrates how to use the `bc` include tag.

## Usage

Breadcrumbs can be used to illustrate procedural layers, as in menus.

{% capture bc-code %}
{% raw %}{% include bc path="File|Save As|New Microscope"%}{% endraw %}
{% endcapture %}
{% capture bc-result %}
{% include bc path="File|Save As|New Microscope"%}
{% endcapture %}
{% include editing/example code=bc-code result=bc-result %}

### Styles

You can optionally change the style of the path separators:

{% capture bc-filled-code %}
{% raw %}{% include bc path="File|Save As|New Microscope" style='filled' %}{% endraw %}
{% endcapture %}
{% capture bc-filled-result %}
{% include bc path="File|Save As|New Microscope" style='filled' %}
{% endcapture %}
{% include editing/example code=bc-filled-code result=bc-filled-result %}

{% capture bc-hollow-code %}
{% raw %}{% include bc path="File|Save As|New Microscope" style='hollow' %}{% endraw %}
{% endcapture %}
{% capture bc-hollow-result %}
{% include bc path="File|Save As|New Microscope" style='hollow' %}
{% endcapture %}
{% include editing/example code=bc-hollow-code result=bc-hollow-result %}

