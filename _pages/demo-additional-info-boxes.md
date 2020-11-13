---
title: Demo additonal info boxes
layout: page
author:
categories: help
description: This page demonstrates how to add various stylized blurbs to your page.
---
## Big Info Box

The big info box include creates a large, centered box on your page.

The following code:
{% raw %}
```
{% include biginfo-box content='See [:Category:Tracking](Category_Tracking) for pages about particle tracking.' %}
```
{% endraw %}

Produces:
{% include biginfo-box content='See [:Category:Tracking](Category_Tracking) for pages about particle tracking.' %}

<br>
<br>
<br>
<br>

## Mini Info Box

The minibox include creates a small text box with room for a short blurb.

The following code:
{% raw %}
```
{% include minibox logo='Pi.svg' blurb='Learn programming through fun, practical projects!' %}
```
{% endraw %}
Produces:
{% include minibox logo='Pi.svg' blurb='Learn programming through fun, practical projects!' %}

<br>
<br>
<br>
<br>
<br>
## Tip Box
The following code:
{% raw %}
```
{% include tip tip='Your text here.' %}
```
{% endraw %}
Produces:
{% include tip tip='Your text here.' %}

## Ambox

This code: {% raw %} `{% include ambox text="Your text here."%}`  produces: {% endraw %} {% include ambox text="Your text here." %}

<br>
<br>
<br>
<br>
<br>
## OS Logo boxes

Our site supports a predetermined list of frequently used logo-boxes. If you would like to use a stand alone logo, you can add one to your page as an image file with the [include image](/demo-image) feature.

This code: {% raw %} `{% include macos content="Your text here."%}`  produces: {% endraw %} {% include macos content="Your text here." %}
<br>
<br>
<br>
This code: {% raw %} `{% include windows content="Your text here."%}`  produces: {% endraw %} {% include windows content="Your text here."%}
<br>
<br>
<br>
This code: {% raw %} `{% include linux content="Your text here."%}`   produces: {% endraw %} {% include linux content="Your text here."%}
<br>
<br>
<br>
