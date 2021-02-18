---
title: Demo logos
layout: page
author:
categories: help
description: this page demonstrates how to use the logo include tag
---

## Usage

Specify a logo icon by name.

{% raw %}
```
{% include logo content='ImageJ' %}
```
{% endraw %}

{% include logo content='ImageJ' %}

Optionally, override the icon size (default is `48px`):

{% raw %}
```
{% include logo content='SciJava' size='96px' %}
```
{% endraw %}

{% include logo content='SciJava' size='96px' %}

Use `size=x96px` to set the height instead of the width:

{% raw %}
```
{% include logo content='Bio-Formats' size='x96px' %}
```
{% endraw %}

{% include logo content='Bio-Formats' size='x96px' %}

You can also override the horizontal alignment:

{% raw %}
```
{% include logo content='Linux' size='96px' align='left' %}
```
{% endraw %}

{% include logo content='Linux' size='96px' align='left' %}
Alpha  
Beta  
Gamma

See also [:Category:Logos](:Category:Logos).
