---
title: Buttons
section: Contribute:Editing the Wiki
nav-links: true
---

This page demonstrates how to use the `button` include tag.

## Usage

This tag creates a visual button with the given text. It is intended for use documenting features and workflows of software applications; these "buttons" do not perform any action when clicked on the page.

{% capture button-code %}
{% raw %}Click {% include button label="OK" %} to continue,
or {% include button label="Cancel" %} to stop.{% endraw %}
{% endcapture %}
{% capture button-result %}
Click {% include button label="OK" %} to continue,
or {% include button label="Cancel" %} to stop.
{% endcapture %}
{% include editing/example code=button-code result=button-result %}
