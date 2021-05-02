---
title: Demo info-box
description: This page demonstrates how to insert an info-box.
---

## Usage

Information boxes allow you to notify the reader of something important details to keep in mind. To use the information box, include them in your markdown document, and utilize the `content` variable to contain your text.

Note that you can still use markdown inside the `""` where your text is placed. In this example I'm using markdown to create a list inside the information box.

## Example

{% raw %}
```
{% include info-box content="Hey this is the info box!

- item 1
- item 2

If you want to learn more about how to create an info box, view the source of this page! Such wow!" %}
```
{% endraw %}

{% include info-box content="Hey this is the info box!

- item 1
- item 2

If you want to learn more about how to create an info box, view the source of this page! Such wow!" %}
