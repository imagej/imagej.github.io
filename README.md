ImageJ.net (Experimental)
===

Welcome to ImageJ.net.

## **Images (without legends):**

Images can be added and placed on the _left_, _right_, _center_ and _fit_ positions. For example:

```
{% include image-left name="spirals" image_path="/images/readme/spirals_2.png" %}
```
<p align="center">
	<img src="/images/readme/image-left.png">
</p>

Replace `image-left` with:

- `image-right`
- `image-center`
- `image-fit`

To render the image on the right and center respectively. Fit renders the image in the center and stretches the image to the webpage. This is useful if you want a centered image that is very large and may render outside of the webpage on mobile devices.

## **Images (with legends):**

You may wish to add an image with legend text. To do so use the following syntax:

```
{% include figure-right name="place holder image" image_path="/images/readme/spirals_2.png" content="**Figure 2** : This is a right figure." %}
```

<p align="center">
	<img src="/images/readme/figure-right.png">
</p>

_Note_: You can use markdown **bolding** and _italics_ in the figure legend text to add emphsis to your legend.

## YouTube videos

To include an embedded YouTube video on your page, copy the `embed` url of the video and use the following syntax:

```
{% include youtube url="https://www.youtube.com/embed/4NOM-kLfDR8" %}
```

<p align="center">
	<img src="/images/readme/youtube.png">
</p>


## Equations

1. Set the `use_math` variable to `true` in the front matter.

```
---
title: Page Title
layout: page
use_math: true
```

2. Type your math forumula using TeX (you can check out how here: [LaTeX/Mathematics](https://en.wikibooks.org/wiki/LaTeX/Mathematics)). _Note: Because MathJax 3 broke support for MathJax 2 style equations parsed by the Kramdown, equations are only recognized by the `$$` tag._

Example:

```
When $$a \ne 0$$ , there are two solutions to $$(ax^2 + bx + c = 0)$$ and they are

$$x = {-b \pm \sqrt{b^2-4ac} \over 2a}.$$

Wow such pretty math!

```

<p align="center">
	<img src="/images/readme/math.png">
</p>

## Info-box

To add an info-box to your page, specifiy the icon you wish to use and include the info-box content:

```
{% include info-box icon_path="/images/icons/40px-Information-sign.png" content="Hey this is the info box! If you want to learn more about how to create an info box, view the source of this page!" %}
```

<p align="center">
	<img src="/images/readme/info-box.png">
</p>

## Setting up the side bar with anchors

Adding a sidebar with anchor

Place this at the top of the page (before content)

```
<div class="sidebar" markdown="1">

Learn
<hr>
[Introduction](#Introduction)
<hr>
[Section 1](#Section 1)
[Section 2](#Section 2)
[Section 3](#Section 3)

</div>

```
Add anchors where apporpriate:

Title anchors:

```
## <a name="Introduction"></a> **Introduction**

<!-- content -->

## <a name="Section 1"></a> **Section 1**

<!-- content -->

## <a name="Section 2"></a> **Section 2**

<!-- content -->

## <a name="Section 3"></a> **Section 3**

<!-- content -->

```

![sidebar example](/images/readme/sidebar.jpg)

**The following options are available:**

| Option | Result |
| :---: | :---: |
| {: .image.left} | left alignment |
| {: .image.right} | right alignment |
| {: .image.center} | center alignment |
| {: .image.fit} | centers and fits image (recommended over .image.center)

_Note:_ We recommend using `{: .image.fit}` instead of `{: .image.center}` to avoid images that escape the container (_i.e._ images may span off screen on mobile devices).


## TODO (pre-live):

- [X] Math support via Mathjax.
- [X] UX bread crumbs (top of page)
- [X] Code syntax highlighting
- [X] Add infobox elements
- [X] Add brief description to front matter.
- [X] Add Lazy loading to images
- [ ] Add ABC lists to CSS style
- [ ] Table of contents heirachy
- [ ] Remove "category indexes" from search
- [ ] Create wide table style
- [X] Add link support for the info-box
- [X] Fix footer -- does not stick to bottom
- [ ] Fix h2 header --> normal/bold should be #585858
- [X] Fix tables (too wide) -- set to `width: 50%;`
- [ ] Change table style -- needs lines
- [ ] Fix Figure center - width issues
- [X] Convert all links to use relative_url (safely prepend links to the domain root and allows for moving to different `baseurl` if necessary)
- [X] Add Sidebox element
- [X] Add Edit and view source links to page template
- [X] Add page/post type to categories
- [ ] Add supporting pages
	- [x] Getting started (/learn.md)
	- [ ] Architecture (/learn/architecture.md)

## TODO (post-live):

- [ ] Change base url for "View source" page info from jekyll-protoype branch

Credit:
------------------

Photon by HTML5 UP
html5up.net | @ajlkn
Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)


A simple (gradient-heavy) single pager that revisits a style I messed with on two
previous designs (Tessellate and Telephasic). Fully responsive, built on Sass,
and, as usual, loaded with an assortment of pre-styled elements. Have fun! :)

Demo images* courtesy of Unsplash, a radtastic collection of CC0 (public domain) images
you can use for pretty much whatever.

(* = Not included)

Feedback, bug reports, and comments are not only welcome, but strongly encouraged :)

AJ
aj@lkn.io | @ajlkn


Credits:

	Demo Images:
		Unsplash (unsplash.com)

	Icons:
		Font Awesome (fontawesome.io)

	Other:
		jQuery (jquery.com)
		Responsive Tools (github.com/ajlkn/responsive-tools)