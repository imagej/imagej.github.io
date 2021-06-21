---
title: Images
section: Contribute:Editing the Wiki
nav-links: true
---

This page explains how to use the `img` include tag.

We encourage the uploading of images used in your pages to assure the future integrity of the wiki. For external images (e.g. if the file is too large for GitHub) we recommend using [markdown](/editing/#markdown).

## Uploading an Image

If the image that you are seeking to add to your page has not yet been utilized on the site, it will need to be uploaded to a repository within the site. You can do so by uploading your image file within the [media folder](https://github.com/imagej/imagej.github.io/tree/main/media) of the [repository](https://github.com/imagej/imagej.github.io).

Once your image has been uploaded, you can follow the usage instructions below to add it to your page.

## Referencing an Image

Images can be added to your page by including `img` and the path to your image. Optionally a name can be specified as well. For example :

{% highlight liquid %}{% raw %}
{% include img name="spirals" src="/media/spirals.png" %}
{% endraw %}{% endhighlight %}

{% include img name="spirals" src="/media/spirals.png" %}

**N.B.** for any file in `/media`, the prefix is optional:

{% highlight liquid %}{% raw %}
{% include img name="spirals" src="spirals" %}
{% endraw %}{% endhighlight %}

{% include img name="spirals" src="spirals" %}

The file extension is also optional if the filename ends in .svg, .png, .gif, or .jpg.

## Options

### Classes

CSS classes can be explicitly specified with the `class` parameter:

{% highlight liquid %}{% raw %}
{% include img name="spirals" src="spirals" class="box" %}
{% endraw %}{% endhighlight %}

{% include img name="spirals" src="spirals" class="box" %}

### Width

Image width can be manually controlled with the `width` parameter:

{% highlight liquid %}{% raw %}
{% include img name="spirals" src="spirals" width="50px" %}
{% endraw %}{% endhighlight %}

{% include img name="spirals" src="spirals" width="50px" %}

### Alignment

Optionally, an alignment specification can be added with
`align="left"`, `align="right"`, `align="center"` or `align="fit"`.

{% highlight liquid %}{% raw %}
{% include img align="left" name="spirals" src="spirals" %}
{% endraw %}{% endhighlight %}

{% include img align="left" name="spirals" src="spirals" %}

Lorem ipsum dolor sit amet, qui possit aeterno denique ea, te usu affert consequuntur, vix in utinam mentitum reformidans. Sed ea vidisse eripuit aliquid, no usu ullum dictas, an epicurei maluisset vix. Ne posse virtute impedit duo. Eos homero euripidis honestatis no.

Sed ex magna honestatis, ea illud honestatis pri. Vix libris nemore suscipiantur cu. Offendit posidonium has ad, nec ad vocent maiorum consetetur. Vis ei iisque phaedrum atomorum, vis ea esse cetero. In est qualisque adipiscing reformidans, ut sint habeo libris quo.

Mel tempor consetetur posidonium in, mei admodum mentitum ullamcorper cu. Ius no prima dolorum. Mea electram imperdiet adversarium in, vide reque ei sed. Ut duo putant dictas theophrastus. Ne vim etiam theophrastus, cu vel minimum detracto, modus possit phaedrum ius an. Noster nominavi persequeris has ex, brute mnesarchum intellegebat eu eum.

Aliquam gravida maximus quam. Cras eu ornare sapien, ac tempor orci.

{% highlight liquid %}{% raw %}
{% include img align="right" name="spirals" src="spirals" %}
{% endraw %}{% endhighlight %}

{% include img align="right" name="spirals" src="spirals" %}

Lorem ipsum dolor sit amet, qui possit aeterno denique ea, te usu affert consequuntur, vix in utinam mentitum reformidans. Sed ea vidisse eripuit aliquid, no usu ullum dictas, an epicurei maluisset vix. Ne posse virtute impedit duo. Eos homero euripidis honestatis no.

Sed ex magna honestatis, ea illud honestatis pri. Vix libris nemore suscipiantur cu. Offendit posidonium has ad, nec ad vocent maiorum consetetur. Vis ei iisque phaedrum atomorum, vis ea esse cetero. In est qualisque adipiscing reformidans, ut sint habeo libris quo.

Mel tempor consetetur posidonium in, mei admodum mentitum ullamcorper cu. Ius no prima dolorum. Mea electram imperdiet adversarium in, vide reque ei sed. Ut duo putant dictas theophrastus. Ne vim etiam theophrastus, cu vel minimum detracto, modus possit phaedrum ius an. Noster nominavi persequeris has ex, brute mnesarchum intellegebat eu eum.

Aliquam gravida maximus quam. Cras eu ornare sapien, ac tempor orci.

{% highlight liquid %}{% raw %}
{% include img align="center" name="spirals" src="spirals" %}
{% endraw %}{% endhighlight %}

{% include img align="center" name="spirals" src="spirals" %}

Albucius eligendi est ei. Graeco alterum prodesset pro ad. Eum movet populo mediocrem ad, ut vix scaevola legendos tractatos. Omnes adolescens voluptatibus qui eu. Ut sea quando soluta qualisque, qui in simul reprehendunt, pro ei dico abhorreant. Ius amet munere erroribus te.

{% highlight liquid %}{% raw %}
{% include img align="fit" name="spirals" src="spirals" %}
{% endraw %}{% endhighlight %}

{% include img align="fit" name="spirals" src="spirals" %}

Eum ei melius salutandi urbanitas, id duo modo discere dolorum. Tota nonumes ei vis, mea ne reque efficiantur, forensibus reprimique id duo. Ocurreret voluptaria in est, an sed nemore similique, affert aeterno recteque an nam. Porro integre detracto et sea, eum ne nulla ancillae intellegat. Ex dolorum referrentur cum, nec ei officiis convenire, ad vis cibo timeam.

# Figures

A *figure* is an image with legend text.

## Usage

Images can be added with an accompanying legend text by including `figure` followed by a location (_e.g._ `align="left"`, `align="right"` and `align="center"`) as well as a `content` variable for the legend text.

## Example 1

{% highlight liquid %}{% raw %}
{% include img align="left" name="spiral left" src="spirals" caption="**Figure 1**: This is a left figure." %}
{% endraw %}{% endhighlight %}

{% include img align="left" name="spiral left" src="spirals" caption="**Figure 1**: This is a left figure." %}

Lorem ipsum dolor sit amet, qui possit aeterno denique ea, te usu affert consequuntur, vix in utinam mentitum reformidans. Sed ea vidisse eripuit aliquid, no usu ullum dictas, an epicurei maluisset vix. Ne posse virtute impedit duo. Eos homero euripidis honestatis no.

Sed ex magna honestatis, ea illud honestatis pri. Vix libris nemore suscipiantur cu. Offendit posidonium has ad, nec ad vocent maiorum consetetur. Vis ei iisque phaedrum atomorum, vis ea esse cetero. In est qualisque adipiscing reformidans, ut sint habeo libris quo.

Mel tempor consetetur posidonium in, mei admodum mentitum ullamcorper cu. Ius no prima dolorum. Mea electram imperdiet adversarium in, vide reque ei sed. Ut duo putant dictas theophrastus. Ne vim etiam theophrastus, cu vel minimum detracto, modus possit phaedrum ius an. Noster nominavi persequeris has ex, brute mnesarchum intellegebat eu eum.

Albucius eligendi est ei. Graeco alterum prodesset pro ad. Eum movet populo mediocrem ad, ut vix scaevola legendos tractatos. Omnes adolescens voluptatibus qui eu. Ut sea quando soluta qualisque, qui in simul reprehendunt, pro ei dico abhorreant. Ius amet munere erroribus te.

Eum ei melius salutandi urbanitas, id duo modo discere dolorum. Tota nonumes ei vis, mea ne reque efficiantur, forensibus reprimique id duo. Ocurreret voluptaria in est, an sed nemore similique, affert aeterno recteque an nam. Porro integre detracto et sea, eum ne nulla ancillae intellegat. Ex dolorum referrentur cum, nec ei officiis convenire, ad vis cibo timeam.

## Example 2

Or to the right of the text.

{% raw %}
```
{% include img align="right" name="spiral right" src="spirals" caption="**Figure 2** : This is a right figure." %}
```
{% endraw %}

{% include img align="right" name="spiral right" src="spirals" caption="**Figure 2** : This is a right figure." %}

Lorem ipsum dolor sit amet, qui possit aeterno denique ea, te usu affert consequuntur, vix in utinam mentitum reformidans. Sed ea vidisse eripuit aliquid, no usu ullum dictas, an epicurei maluisset vix. Ne posse virtute impedit duo. Eos homero euripidis honestatis no.

Sed ex magna honestatis, ea illud honestatis pri. Vix libris nemore suscipiantur cu. Offendit posidonium has ad, nec ad vocent maiorum consetetur. Vis ei iisque phaedrum atomorum, vis ea esse cetero. In est qualisque adipiscing reformidans, ut sint habeo libris quo.

Mel tempor consetetur posidonium in, mei admodum mentitum ullamcorper cu. Ius no prima dolorum. Mea electram imperdiet adversarium in, vide reque ei sed. Ut duo putant dictas theophrastus. Ne vim etiam theophrastus, cu vel minimum detracto, modus possit phaedrum ius an. Noster nominavi persequeris has ex, brute mnesarchum intellegebat eu eum.

Albucius eligendi est ei. Graeco alterum prodesset pro ad. Eum movet populo mediocrem ad, ut vix scaevola legendos tractatos. Omnes adolescens voluptatibus qui eu. Ut sea quando soluta qualisque, qui in simul reprehendunt, pro ei dico abhorreant. Ius amet munere erroribus te.

Eum ei melius salutandi urbanitas, id duo modo discere dolorum. Tota nonumes ei vis, mea ne reque efficiantur, forensibus reprimique id duo. Ocurreret voluptaria in est, an sed nemore similique, affert aeterno recteque an nam. Porro integre detracto et sea, eum ne nulla ancillae intellegat. Ex dolorum referrentur cum, nec ei officiis convenire, ad vis cibo timeam.

## Example 3

Or centered.

{% raw %}
```
{% include img align="center" name="spiral center" src="spirals" caption="**Figure 1**: This is a centered figure." %}

```
{% endraw %}

{% include img align="center" name="spiral center" src="spirals" caption="**Figure 1**: This is a centered figure." %}

# Image Galleries

## Usage

{% raw %}
```
{% include gallery content=
"
/media/editing/pic01.jpg | Example 1
/media/editing/pic02.jpg | Example 2
/media/editing/pic03.jpg | Example 3
/media/editing/pic04.jpg | Example 4
/media/icons/imagej2.png | ImageJ!
"
%}
```
{% endraw %}

{% include gallery content=
"
/media/editing/pic01.jpg | Example 1
/media/editing/pic02.jpg | Example 2
/media/editing/pic03.jpg | Example 3
/media/editing/pic04.jpg | Example 4
/media/icons/imagej2.png | ImageJ!
"
%}
