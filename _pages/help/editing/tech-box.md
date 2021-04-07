---
title: Demo tech-box
author: 
description: This page demonstrates how to insert a tech box.
---

## Usage

Tech boxes allow you to notify the reader of something important details to keep in mind. To use the tech box, include them in your markdown document, and utilize the `content` variable to contain your text.

Note that you can still use markdown inside the `""` where your text is placed. In this example I'm using markdown to create a list inside the tech box.


## Example

{% raw %}
```
{% include tech-box content="Wait stop! There's some tech going on here!

- Tech item 1
- Tech item 2
- Tech item 3

" %}
```
{% endraw %}

{% include tech-box content="Wait stop! There's some tech going on here!

- Tech item 1
- Tech item 2
- Tech item 3

" %}
