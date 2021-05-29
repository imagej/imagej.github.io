---
mediawiki: NONE
title: Citations
section: Contribute:Editing the Wiki
nav-links: true
---

This page demonstrates how to add a citation to your page.

There are currently three options to include citations on your page:

| `include citation`         | create a single-use citation, or footnote |
| `include testimonial`      | insert a personal quote from a [person](/people) |
| `include citation id="plugins/<id>`" | pulls a pre-formatted citation from the [list of registered publications](#registered-publications) |

## `citation`

This include creates a citation given the following inputs:
author (all authors of the publication, this input will be presented as entered):

| **title**   | title of the publication                                        |
| **url**     | url link to location the publication is hosted                  |
| **year**    | year of publication                                             |
| **journal** | name of the publishing journal                                  |
| **volume**  | volume of the publishing journal                                |
| **number**  | issuing number of the publishing journal                        |
| **pages**   | page numbers that the publication appears in publishing journal |
| **doi**     | digital object identifier                                       |
| **fn**      | foot note number                                                |

{% capture lowry-1951-code %}
{% raw %}
{% include citation
  title="Protein measurement with the Folin phenol reagent"
  last="Lowry" first="O. H."
  last2="Rosebrough" first="N. J."
  last3="Farr" first="A. L."
  last4="Randall" first="R. J."
  journal="Journal of biological chemistry"
  volume=193
  pages="265-275"
  year=1951
  scholar=14244920428100608083
%}
{% endraw %}
{% endcapture %}
{% capture lowry-1951-result %}
{% include citation
  title="Protein measurement with the Folin phenol reagent"
  last="Lowry" first="O. H."
  last2="Rosebrough" first="N. J."
  last3="Farr" first="A. L."
  last4="Randall" first="R. J."
  journal="Journal of biological chemistry"
  volume=193
  pages="265-275"
  year=1951
  scholar=14244920428100608083
%}
{% endcapture %}
{% include code-example code=lowry-1951-code result=lowry-1951-result %}

## `publication`

This include is primarily used to reference ImageJ/Fiji related plugins, and pulls from a list of already created citations. The list can be found [here](/contribute/citing).
This include uses the following field:<br><br>
**content** the input for this field must match the plugin/tool/package name listed on the [Citations page](/contribute/citing).

*The following liquid code:*
```
{% raw %}
{% include citation id="plugins/3d-viewer" %}
{% endraw %}
```
*produces:*

{% include citation id="plugins/3d-viewer" %}

## `testimonial`

This include is used to quote a particular individual. Available fields:

* **person** can be any user from [this list](/people)
* **quote** is the text that will be displayed
* **source** is a link to the original quotation

*The following liquid code:*
```
{% raw %}
{% include testimonial person='ctrueden' quote='ON VACATION UNTIL OCTOBER 5. For real this time!' source='https://forum.image.sc/t/coba-imagej-fiji-2020-summer-progress-report-and-fall-roadmap/42450' %}
{% endraw %}
```
*produces:*

{% include testimonial person='ctrueden' quote='ON VACATION UNTIL OCTOBER 5. For real this time!' source='https://forum.image.sc/t/coba-imagej-fiji-2020-summer-progress-report-and-fall-roadmap/42450' %}

{% include clear %}

## Creating footnotes

### In your document
Use the [kramdown syntax](https://kramdown.gettalong.org/quickref.html#footnotes) in your document to refer to footnotes by number.

**NB:** regardless of where the liquid reference appears in your document, footnote text will always be at the bottom.

### In your citation

Specify the footnote number in the `include`.

*The following markdown and liquid code:*

```
This is a reference[^1].

{% raw %}
{% include citation author='Albert Cardona, Stephan Saalfeld, Johannes Schindelin, Ignacio Arganda-Carreras, Stephan Preibisch, Mark Longair, Pavel Tomancak, Volker Hartenstein and Rodney J. Douglas'
year='2012'
fn=1
title='TrakEM2 software for neural circuit reconstruction' journal='PLoS ONE'
url='http://www.plosone.org/article/info%3Adoi%2F10.1371%2Fjournal.pone.0038011'
doi='10.1371/journal.pone.0038011' %}
{% endraw %}
```
*produces:*

This is a reference[^1].

{% include citation fn=1 author='Albert Cardona, Stephan Saalfeld, Johannes Schindelin, Ignacio Arganda-Carreras, Stephan Preibisch, Mark Longair, Pavel Tomancak, Volker Hartenstein and Rodney J. Douglas' year='2012' title='TrakEM2 software for neural circuit reconstruction' journal='PLoS ONE' url='http://www.plosone.org/article/info%3Adoi%2F10.1371%2Fjournal.pone.0038011' doi='10.1371/journal.pone.0038011' %}

## Registered publications
