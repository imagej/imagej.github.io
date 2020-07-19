---
title: Demo figure
layout: page
author: 
categories: 
description: This page demonstrates how to use figures (_i.e._ images with legend text).
---

## Usage

Images can be added with an accompanying legend text by including `figure-` followed by a location (_e.g._ `left`, `right` and `center`) as well as a `content` variable for the legend text. For example, an image with a legened (or a "figure") can be added to the left of the text:

## Example 1

{% raw %}
```
{% include figure-left name="spiral left" image_path="/images/readme/spirals.png" content="**Figure 1**: This is a left figure." %}

```
{% endraw %}

{% include figure-left name="place holder image" image_path="/images/readme/spirals.png" content="**Figure 1**: This is a left figure." %}

Lorem ipsum dolor sit amet, qui possit aeterno denique ea, te usu affert consequuntur, vix in utinam mentitum reformidans. Sed ea vidisse eripuit aliquid, no usu ullum dictas, an epicurei maluisset vix. Ne posse virtute impedit duo. Eos homero euripidis honestatis no.

Sed ex magna honestatis, ea illud honestatis pri. Vix libris nemore suscipiantur cu. Offendit posidonium has ad, nec ad vocent maiorum consetetur. Vis ei iisque phaedrum atomorum, vis ea esse cetero. In est qualisque adipiscing reformidans, ut sint habeo libris quo.

Mel tempor consetetur posidonium in, mei admodum mentitum ullamcorper cu. Ius no prima dolorum. Mea electram imperdiet adversarium in, vide reque ei sed. Ut duo putant dictas theophrastus. Ne vim etiam theophrastus, cu vel minimum detracto, modus possit phaedrum ius an. Noster nominavi persequeris has ex, brute mnesarchum intellegebat eu eum.

Albucius eligendi est ei. Graeco alterum prodesset pro ad. Eum movet populo mediocrem ad, ut vix scaevola legendos tractatos. Omnes adolescens voluptatibus qui eu. Ut sea quando soluta qualisque, qui in simul reprehendunt, pro ei dico abhorreant. Ius amet munere erroribus te.

Eum ei melius salutandi urbanitas, id duo modo discere dolorum. Tota nonumes ei vis, mea ne reque efficiantur, forensibus reprimique id duo. Ocurreret voluptaria in est, an sed nemore similique, affert aeterno recteque an nam. Porro integre detracto et sea, eum ne nulla ancillae intellegat. Ex dolorum referrentur cum, nec ei officiis convenire, ad vis cibo timeam.

## Example 2

Or to the right of the text.

{% raw %}
```
{% include figure-right name="place holder image" image_path="/images/readme/spirals.png" content="**Figure 2** : This is a right figure." %}
```
{% endraw %}

{% include figure-right name="place holder image" image_path="/images/readme/spirals.png" content="**Figure 2** : This is a right figure." %}

Lorem ipsum dolor sit amet, qui possit aeterno denique ea, te usu affert consequuntur, vix in utinam mentitum reformidans. Sed ea vidisse eripuit aliquid, no usu ullum dictas, an epicurei maluisset vix. Ne posse virtute impedit duo. Eos homero euripidis honestatis no.

Sed ex magna honestatis, ea illud honestatis pri. Vix libris nemore suscipiantur cu. Offendit posidonium has ad, nec ad vocent maiorum consetetur. Vis ei iisque phaedrum atomorum, vis ea esse cetero. In est qualisque adipiscing reformidans, ut sint habeo libris quo.

Mel tempor consetetur posidonium in, mei admodum mentitum ullamcorper cu. Ius no prima dolorum. Mea electram imperdiet adversarium in, vide reque ei sed. Ut duo putant dictas theophrastus. Ne vim etiam theophrastus, cu vel minimum detracto, modus possit phaedrum ius an. Noster nominavi persequeris has ex, brute mnesarchum intellegebat eu eum.

Albucius eligendi est ei. Graeco alterum prodesset pro ad. Eum movet populo mediocrem ad, ut vix scaevola legendos tractatos. Omnes adolescens voluptatibus qui eu. Ut sea quando soluta qualisque, qui in simul reprehendunt, pro ei dico abhorreant. Ius amet munere erroribus te.

Eum ei melius salutandi urbanitas, id duo modo discere dolorum. Tota nonumes ei vis, mea ne reque efficiantur, forensibus reprimique id duo. Ocurreret voluptaria in est, an sed nemore similique, affert aeterno recteque an nam. Porro integre detracto et sea, eum ne nulla ancillae intellegat. Ex dolorum referrentur cum, nec ei officiis convenire, ad vis cibo timeam.
