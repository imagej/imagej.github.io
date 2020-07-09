---
title: Demo logos
layout: page
author: 
categories: 
description: this page demonstrates how to use the logo include tag
---

Please click on <code>View source</code> to see how this page was written.

Specify a logo icon by name.

{% include logo content='ImageJ' %}

Optionally, override the icon size (default is `48px`):

{% include logo content='SciJava' size='96px' %}

Use `size=x96px` to set the height instead of the width:

{% include logo content='Bio-Formats' size='x96px' %}

You can also override the horizontal alignment:

{% include logo content='Linux' size='96px' align='left' %} 
Alpha  
Beta  
Gamma

See also [:Category:Logos](:Category:Logos).
