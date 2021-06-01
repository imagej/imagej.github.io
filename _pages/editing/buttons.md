---
title: Buttons
section: Contribute:Editing the Wiki
nav-links: true
---

This page demonstrates how to use the `button` include tag.

## Usage

This tag simply creates a non-functional [button](https://www.w3schools.com/tags/tag_button.asp) with the given text.

{% capture button-code %}
{% raw %}{% include button label="My Button"%}{% endraw %}
{% endcapture %}
{% capture button-result %}
{% include button label="My Button"%}
{% endcapture %}
{% include editing/example code=button-code result=button-result %}
