---
title: Demo warning-box
author: 
description: This page demonstrates how to insert a warning box.
---

## Usage

Warning boxes allow you to notify the reader of something important details to keep in mind. To use the warning box, include them in your markdown document, and utilize the `content` variable to contain your text.

Note that you can still use markdown inside the `""` where your text is placed. In this example I'm using markdown to create a list inside the warning box.


## Example

{% raw %}
```
{% include warning-box content="Stop! This is an important message! Did you check out the plugins categories page? What do you think? Make sure you wash your hands! Okay please continue reading.
" %}
```
{% endraw %}

{% include warning-box content="Stop! This is an important message! Did you check out the plugins categories page? What do you think? Make sure you wash your hands! Okay please continue reading.
" %}
