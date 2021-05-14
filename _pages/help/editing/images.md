---
title: Editing the Wiki - Images
section: Help:Editing the Wiki
---

This page explains how to add images to your page.

# Images

## Uploading an Image

If the image that you are seeking to add to your page has not yet been utilized on the site, it will need to be uploaded to a repository within the site. You can do so by uploading your image file within the [media folder](https://github.com/imagej/imagej.github.io/tree/main/media) of the [repository](https://github.com/imagej/imagej.github.io).

Once your image has been uploaded, you can follow the usage instructions below to add it to your page.

## Referencing an Image

Images can be added to your page by including `img` and the path to your image. Optionally a name can be specified as well. For example :

{% raw %}
```
{% include img name="spirals" src="/media/help/spirals.png" %}
```
{% endraw %}

{% include img name="spirals" src="/media/help/spirals.png" %}

**N.B.** for any file in `/media`, the prefix is optional:

{% raw %}
```
{% include img name="spirals" src="/help/spirals.png" %}
```
{% endraw %}

{% include img name="spirals" src="/help/spirals.png" %}

## Options

### Classes

Css classes can be expliticly specified with the `classes` parameter:

{% raw %}
```
{% include img name="spirals" src="/media/help/spirals.png" classes="thumbnail" %}
```
{% endraw %}

{% include img name="spirals" src="/media/help/spirals.png" classes="thumbnail" %}

Lorem ipsum dolor sit amet, qui possit aeterno denique ea, te usu affert consequuntur, vix in utinam mentitum reformidans. Sed ea vidisse eripuit aliquid, no usu ullum dictas, an epicurei maluisset vix. Ne posse virtute impedit duo. Eos homero euripidis honestatis no.

Sed ex magna honestatis, ea illud honestatis pri. Vix libris nemore suscipiantur cu. Offendit posidonium has ad, nec ad vocent maiorum consetetur. Vis ei iisque phaedrum atomorum, vis ea esse cetero. In est qualisque adipiscing reformidans, ut sint habeo libris quo.

Mel tempor consetetur posidonium in, mei admodum mentitum ullamcorper cu. Ius no prima dolorum. Mea electram imperdiet adversarium in, vide reque ei sed. Ut duo putant dictas theophrastus. Ne vim etiam theophrastus, cu vel minimum detracto, modus possit phaedrum ius an. Noster nominavi persequeris has ex, brute mnesarchum intellegebat eu eum.

Aliquam gravida maximus quam. Cras eu ornare sapien, ac tempor orci.

### Width

Image width can be manually controlled with the `width` parameter:

{% raw %}
```
{% include img name="spirals" src="/media/help/spirals.png" width="50px" %}
```
{% endraw %}

{% include img name="spirals" src="/media/help/spirals.png" width="50px" %}

### Alignment 

Optionally, an alignment specification can be added (_i.e._ `align="left"`, `align="right"`, `align="center"` or `align="fit"`) 

{% raw %}
```
{% include img align="left" name="spirals" src="/media/help/spirals.png" %}
```
{% endraw %}

{% include img align="left" name="spirals" src="/media/help/spirals.png" %}

Lorem ipsum dolor sit amet, qui possit aeterno denique ea, te usu affert consequuntur, vix in utinam mentitum reformidans. Sed ea vidisse eripuit aliquid, no usu ullum dictas, an epicurei maluisset vix. Ne posse virtute impedit duo. Eos homero euripidis honestatis no.

Sed ex magna honestatis, ea illud honestatis pri. Vix libris nemore suscipiantur cu. Offendit posidonium has ad, nec ad vocent maiorum consetetur. Vis ei iisque phaedrum atomorum, vis ea esse cetero. In est qualisque adipiscing reformidans, ut sint habeo libris quo.

Mel tempor consetetur posidonium in, mei admodum mentitum ullamcorper cu. Ius no prima dolorum. Mea electram imperdiet adversarium in, vide reque ei sed. Ut duo putant dictas theophrastus. Ne vim etiam theophrastus, cu vel minimum detracto, modus possit phaedrum ius an. Noster nominavi persequeris has ex, brute mnesarchum intellegebat eu eum.

Aliquam gravida maximus quam. Cras eu ornare sapien, ac tempor orci.

{% raw %}
```
{% include img align="right" name="spirals" src="/media/help/spirals.png" %}
```
{% endraw %}

{% include img align="right" name="spirals" src="/media/help/spirals.png" %}

Lorem ipsum dolor sit amet, qui possit aeterno denique ea, te usu affert consequuntur, vix in utinam mentitum reformidans. Sed ea vidisse eripuit aliquid, no usu ullum dictas, an epicurei maluisset vix. Ne posse virtute impedit duo. Eos homero euripidis honestatis no.

Sed ex magna honestatis, ea illud honestatis pri. Vix libris nemore suscipiantur cu. Offendit posidonium has ad, nec ad vocent maiorum consetetur. Vis ei iisque phaedrum atomorum, vis ea esse cetero. In est qualisque adipiscing reformidans, ut sint habeo libris quo.

Mel tempor consetetur posidonium in, mei admodum mentitum ullamcorper cu. Ius no prima dolorum. Mea electram imperdiet adversarium in, vide reque ei sed. Ut duo putant dictas theophrastus. Ne vim etiam theophrastus, cu vel minimum detracto, modus possit phaedrum ius an. Noster nominavi persequeris has ex, brute mnesarchum intellegebat eu eum.

Aliquam gravida maximus quam. Cras eu ornare sapien, ac tempor orci.

{% raw %}
```
{% include img align="center" name="spirals" src="/media/help/spirals.png" %}
```
{% endraw %}

{% include img align="center" name="spirals" src="/media/help/spirals.png" %}

Albucius eligendi est ei. Graeco alterum prodesset pro ad. Eum movet populo mediocrem ad, ut vix scaevola legendos tractatos. Omnes adolescens voluptatibus qui eu. Ut sea quando soluta qualisque, qui in simul reprehendunt, pro ei dico abhorreant. Ius amet munere erroribus te.

{% raw %}
```
{% include img align="fit" name="spirals" src="/media/help/spirals.png" %}
```
{% endraw %}

{% include img align="fit" name="spirals" src="/media/help/spirals.png" %}

Eum ei melius salutandi urbanitas, id duo modo discere dolorum. Tota nonumes ei vis, mea ne reque efficiantur, forensibus reprimique id duo. Ocurreret voluptaria in est, an sed nemore similique, affert aeterno recteque an nam. Porro integre detracto et sea, eum ne nulla ancillae intellegat. Ex dolorum referrentur cum, nec ei officiis convenire, ad vis cibo timeam.

# Figures

A *figure* is an image with legend text.

## Usage

Images can be added with an accompanying legend text by including `figure-` followed by a location (_e.g._ `left`, `right` and `center`) as well as a `content` variable for the legend text. For example, an image with a legened (or a "figure") can be added to the left of the text:

## Example 1

{% raw %}
```
{% include figure-left name="spiral left" src="/media/help/spirals.png" content="**Figure 1**: This is a left figure." %}

```
{% endraw %}

{% include figure-left name="place holder image" src="/media/help/spirals.png" content="**Figure 1**: This is a left figure." %}

Lorem ipsum dolor sit amet, qui possit aeterno denique ea, te usu affert consequuntur, vix in utinam mentitum reformidans. Sed ea vidisse eripuit aliquid, no usu ullum dictas, an epicurei maluisset vix. Ne posse virtute impedit duo. Eos homero euripidis honestatis no.

Sed ex magna honestatis, ea illud honestatis pri. Vix libris nemore suscipiantur cu. Offendit posidonium has ad, nec ad vocent maiorum consetetur. Vis ei iisque phaedrum atomorum, vis ea esse cetero. In est qualisque adipiscing reformidans, ut sint habeo libris quo.

Mel tempor consetetur posidonium in, mei admodum mentitum ullamcorper cu. Ius no prima dolorum. Mea electram imperdiet adversarium in, vide reque ei sed. Ut duo putant dictas theophrastus. Ne vim etiam theophrastus, cu vel minimum detracto, modus possit phaedrum ius an. Noster nominavi persequeris has ex, brute mnesarchum intellegebat eu eum.

Albucius eligendi est ei. Graeco alterum prodesset pro ad. Eum movet populo mediocrem ad, ut vix scaevola legendos tractatos. Omnes adolescens voluptatibus qui eu. Ut sea quando soluta qualisque, qui in simul reprehendunt, pro ei dico abhorreant. Ius amet munere erroribus te.

Eum ei melius salutandi urbanitas, id duo modo discere dolorum. Tota nonumes ei vis, mea ne reque efficiantur, forensibus reprimique id duo. Ocurreret voluptaria in est, an sed nemore similique, affert aeterno recteque an nam. Porro integre detracto et sea, eum ne nulla ancillae intellegat. Ex dolorum referrentur cum, nec ei officiis convenire, ad vis cibo timeam.

## Example 2

Or to the right of the text.

{% raw %}
```
{% include figure-right name="place holder image" src="/media/help/spirals.png" content="**Figure 2** : This is a right figure." %}
```
{% endraw %}

{% include figure-right name="place holder image" src="/media/help/spirals.png" content="**Figure 2** : This is a right figure." %}

Lorem ipsum dolor sit amet, qui possit aeterno denique ea, te usu affert consequuntur, vix in utinam mentitum reformidans. Sed ea vidisse eripuit aliquid, no usu ullum dictas, an epicurei maluisset vix. Ne posse virtute impedit duo. Eos homero euripidis honestatis no.

Sed ex magna honestatis, ea illud honestatis pri. Vix libris nemore suscipiantur cu. Offendit posidonium has ad, nec ad vocent maiorum consetetur. Vis ei iisque phaedrum atomorum, vis ea esse cetero. In est qualisque adipiscing reformidans, ut sint habeo libris quo.

Mel tempor consetetur posidonium in, mei admodum mentitum ullamcorper cu. Ius no prima dolorum. Mea electram imperdiet adversarium in, vide reque ei sed. Ut duo putant dictas theophrastus. Ne vim etiam theophrastus, cu vel minimum detracto, modus possit phaedrum ius an. Noster nominavi persequeris has ex, brute mnesarchum intellegebat eu eum.

Albucius eligendi est ei. Graeco alterum prodesset pro ad. Eum movet populo mediocrem ad, ut vix scaevola legendos tractatos. Omnes adolescens voluptatibus qui eu. Ut sea quando soluta qualisque, qui in simul reprehendunt, pro ei dico abhorreant. Ius amet munere erroribus te.

Eum ei melius salutandi urbanitas, id duo modo discere dolorum. Tota nonumes ei vis, mea ne reque efficiantur, forensibus reprimique id duo. Ocurreret voluptaria in est, an sed nemore similique, affert aeterno recteque an nam. Porro integre detracto et sea, eum ne nulla ancillae intellegat. Ex dolorum referrentur cum, nec ei officiis convenire, ad vis cibo timeam.

# Image Galleries

## Usage

{% raw %}
```
{% include gallery content=
"
/media/site/pic01.jpg | Example 1
/media/site/pic02.jpg | Example 2
/media/site/pic03.jpg | Example 3
/media/site/pic04.jpg | Example 4
/media/imagej2-icon.png | ImageJ!
"
%}
```
{% endraw %}

{% include gallery content=
"
/media/site/pic01.jpg | Example 1
/media/site/pic02.jpg | Example 2
/media/site/pic03.jpg | Example 3
/media/site/pic04.jpg | Example 4
/media/imagej2-icon.png | ImageJ!
"
%}
