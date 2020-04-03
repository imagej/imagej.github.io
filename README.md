ImageJ.net (Experimental)
===

This is a working prototype of a new ImageJ webpage built on GitHub pages! This is a work in progress and **will change**. This template is based on Photo by HTML5 UP and has been modified for our purposes.

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

## Adding images without legends

To include images without a legend (see below for images with a legend) simply use the markdown syntax followed by the `.image` tag with a position. **Left**, **right**, **center** and **fit** are available aligment positions.

_Example:_

```
![placeholder image]({{site.baseurl}})/images/placeholder.png){: .image.left}
```

![image left example](/images/readme/image-left.jpg)

**The following options are available:**

| Option | Result |
| :---: | :---: |
| {: .image.left} | left alignment |
| {: .image.right} | right alignment |
| {: .image.center} | center alignment |
| {: .image.fit} | centers and fits image (recommended over .image.center)

_Note:_ We recommend using `{: .image.fit}` instead of `{: .image.center}` to avoid images that escape the container (_i.e._ images may span off screen on mobile devices).

## Adding images with legends

To include images with a legend, insert your image with the `{: .image.fit}` tag and nest them inside `<div class="figure POSITION" markdown="1"></div>` tags. **Left**, **right** and **center** are avaiable position options.

_Example:_

```
<div class="figure right" markdown="1">

![placeholder image]({{site.baseurl}}/images/posts/placeholder.png){: .image.fit}

This is the legend text.

</div>
```

![figure right example](/images/readme/figure-right.jpg)

_Note:_ This is space sensitive. If you indent the nested markdown line it will render as a code block instead of your image with legend.

For multiple images on the same line with individual legends, compact this syntax and place it inside a markdown table using the `figure row` class.

_Example:_

```
<div class="figure row" markdown="1">

| ![placeholder image 1]({{site.baseurl}}/images/placeholder.png){: .image.fit} Legend 1 | ![placeholder image 2]({{site.baseurl}}/images/placeholder.png){: .image.fit} Legend 2 | ![placeholder image 3]({{site.baseurl}}/images/placeholder.png){: .image.fit} Legend 3 | 

</div>
```

![figure row example](/images/readme/figure-row.jpg)

## Adding YouTube videos

To include a link to a YouTube video use the following syntax, using the "video-wrapper" class to ensure your video does not escape the container. Copy the iframe video URL and past it inside `<div clas="video-wrapper"></div>` tags. Dont worry about setting the width and height of the video, the wrapper will fit the video to the window.

_Example:_

```
<div class="video-wrapper">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/4NOM-kLfDR8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
```
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