---
mediawiki: 2011-03-16_-_Elastic_aligment_and_montaging
title: 2011-03-16 - Elastic aligment and montaging
---

We have implemented a long-standing simple idea for elastic alignment of large section series and montaging mosaics from unpredictably deformed tiles inspired by work from Elisabeth Guest and Takeo Igarashi. The idea is best explained at an old [poster from 2008](http://fly.mpi-cbg.de/dev/?pid=13&zp=0&yp=915416000.3604&xp=497332000.1958&sid0=17&s0=2) that you can browse through [CATMAID](https://catmaid.readthedocs.io/en/stable/).

Basically, each image is represented as an elastic mesh of spring-connected vertices that are dragged towards corresponding locations in overlapping images. Corresponding locations are found by block matching.

Find the (still experimental) plugins for series alignment and montaging in an updated Fiji's Registration menu. [Documentation](/plugins/elastic-alignment-and-montage) is available at the [Fiji Wiki](/plugins/elastic-alignment-and-montage).

[Elastic Alignment and Montage](/plugins/elastic-alignment-and-montage) was developed by {% include person id='axtimwalde' %}.

Many thanks to {% include person id='acardona' %} and {% include person id='iarganda' %} for pushing and helping.

  
