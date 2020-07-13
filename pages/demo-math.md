---
title: Demo math
layout: page
author: 
categories: 
description: This page demonstrates how to use math equations.
---

## Usage

Math equations are implemented via MathJax3. Use MathJax (LaTeX) syntax to add your math equations (inline or as a block).

Note, Because MathJax 3 broke support for MathJax 2 style equations parsed by Kramdown, equations are only recognized by the `$$` tag.

## Examples

Block equations:

{% raw %}
```
$$x = {-b \pm \sqrt{b^2-4ac} \over 2a}$$
```
{% endraw %}

$$x = {-b \pm \sqrt{b^2-4ac} \over 2a}$$

Inline equations:

{% raw %}
```
When $$a \ne 0$$ , there are two solutions to $$(ax^2 + bx + c = 0)$$.
```
{% endraw %}

When $$a \ne 0$$ , there are two solutions to $$(ax^2 + bx + c = 0)$$.