---
title: Editing the Wiki - Logos
section: Help:Editing the Wiki
---

This page demonstrates how to use the `logo` include tag.

## Usage

Specify a logo icon by name.

{% raw %}
```
{% include icon name='ImageJ' %}
```
{% endraw %}

{% include icon name='ImageJ' %}

Optionally, override the icon size (default is `48px`):

{% raw %}
```
{% include icon name='SciJava' size='96px' %}
```
{% endraw %}

{% include icon name='SciJava' size='96px' %}

Use `size=x96px` to set the height instead of the width:

{% raw %}
```
{% include icon name='Bio-Formats' size='x96px' %}
```
{% endraw %}

{% include icon name='Bio-Formats' size='x96px' %}

You can also override the horizontal alignment:

{% raw %}
```
{% include icon name='Linux' size='96px' align='left' %}
```
{% endraw %}

{% include icon name='Linux' size='96px' align='left' %}
Alpha  
Beta  
Gamma

See also [:Category:Logos](:Category:Logos).
