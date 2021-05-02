---
title: Demo citations

description: This page demonstrates how to add a citation to your page.
---

## Citation Options

There are currently two options to include citations on your page:
`include citation`: allows you to create a single-use citation
`include publication`: pulls a pre-formatted citation from a [list of frequently cited publications](/about/citing).

## Include Citations

### Usage
This include creates a citation given the following inputs:
author (all authors of the publication, this input will be presented as entered): <br><br>
**title** title of the publication <br>
**url** url link to location the publication is hosted<br>
**year** year of publication<br>
**journal** name of the publishing journal<br>
**volume** volume of the publishing journal<br>
**number** issuing number of the publishing journal<br>
**pages** page numbers that the publication appears in publishing journal<br>
**doi** digital object identifier<br>

### Example
*The following liquid code:*
```
{% raw %}
{% include cite content='journal' author='Albert Cardona, Stephan Saalfeld, Johannes Schindelin, Ignacio Arganda-Carreras, Stephan Preibisch, Mark Longair, Pavel Tomancak, Volker Hartenstein and Rodney J. Douglas'
year='2012'
title='TrakEM2 software for neural circuit reconstruction' journal='PLoS ONE'
url='http://www.plosone.org/article/info%3Adoi%2F10.1371%2Fjournal.pone.0038011'
doi='10.1371/journal.pone.0038011' %}
{% endraw %}
```
*produces:*

{% include cite content='journal' author='Albert Cardona, Stephan Saalfeld, Johannes Schindelin, Ignacio Arganda-Carreras, Stephan Preibisch, Mark Longair, Pavel Tomancak, Volker Hartenstein and Rodney J. Douglas' year='2012' title='TrakEM2 software for neural circuit reconstruction' journal='PLoS ONE' url='http://www.plosone.org/article/info%3Adoi%2F10.1371%2Fjournal.pone.0038011' doi='10.1371/journal.pone.0038011' %}

## Include Publication

### Usage
This include is primarily used to reference ImageJ/Fiji related plugins, and pulls from a list of already created citations. The list can be found [here](/about/citing).
This include uses the following field:<br><br>
**content** the input for this field must match the plugin/tool/package name listed on the [Citations page](/about/citing).

### Example
*The following liquid code:*
```
{% raw %}
{% include publication content='3D Viewer' %}
{% endraw %}
```
*produces:*

{% include publication content='3D Viewer' %}
