---
title: Editing the Wiki - Info Boxes
section: Help:Editing the Wiki
---

This page demonstrates how to add various stylized blurbs to your page.

## Info Box

Information boxes allow you to notify the reader of something important details to keep in mind. To use the information box, include them in your markdown document, and utilize the `content` variable to contain your text.

Note that you can still use markdown inside the `""` where your text is placed. In this example I'm using markdown to create a list inside the information box.

### Example

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

## Warning Box

Warning boxes allow you to notify the reader of something important details to keep in mind. To use the warning box, include them in your markdown document, and utilize the `content` variable to contain your text.

Note that you can still use markdown inside the `""` where your text is placed. In this example I'm using markdown to create a list inside the warning box.

### Example

{% raw %}
```
{% include warning-box content="Stop! This is an important message! Did you check out the plugins categories page? What do you think? Make sure you wash your hands! Okay please continue reading.
" %}
```
{% endraw %}

{% include warning-box content="Stop! This is an important message! Did you check out the plugins categories page? What do you think? Make sure you wash your hands! Okay please continue reading.
" %}

## Tech Box

Tech boxes allow you to notify the reader of something important details to keep in mind. To use the tech box, include them in your markdown document, and utilize the `content` variable to contain your text.

Note that you can still use markdown inside the `""` where your text is placed. In this example I'm using markdown to create a list inside the tech box.

### Example

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

## OS Logo boxes

Our site supports a predetermined list of frequently used logo-boxes. If you would like to use a stand alone logo, you can add one to your page as an image file with the [include image](/help/editing/image) feature.

This code: {% raw %} `{% include macos content="Your text here."%}`  produces: {% endraw %} {% include macos content="Your text here." %}

This code: {% raw %} `{% include windows content="Your text here."%}`  produces: {% endraw %} {% include windows content="Your text here."%}

This code: {% raw %} `{% include linux content="Your text here."%}`   produces: {% endraw %} {% include linux content="Your text here."%}
