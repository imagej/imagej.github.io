---
mediawiki: NONE
title: Citations
description: This page demonstrates how to cite sources.
section: Contribute:Editing the Wiki
nav-links: true
---

There are two kinds of sources which can be cited:

| `include citation`         | cite a publication                               |
| `include testimonial`      | insert a personal quote from a [person](/people) |

# Citing publications

The `citation` include is used to cite a publication.

## Citing by DOI

{% capture top-100-papers-code %}
{% raw %}{% include citation doi='10.1038/514550a' %}{% endraw %}
{% endcapture %}
{% capture top-100-papers-result %}
{% include citation doi='10.1038/514550a' %}
{% endcapture %}
{% include editing/example code=top-100-papers-code result=top-100-papers-result %}

### Citation styles

The default citation style is APA, but Harvard and Vancouver styles are also supported:

{% capture harvard-style-code %}
{% raw %}{% include citation doi='10.1038/514550a' style='harvard1' %}{% endraw %}
{% endcapture %}
{% capture harvard-style-result %}
{% include citation doi='10.1038/514550a' style='harvard1' %}
{% endcapture %}
{% include editing/example code=harvard-style-code result=harvard-style-result %}

{% capture vancouver-style-code %}
{% raw %}{% include citation doi='10.1038/514550a' style='vancouver' %}{% endraw %}
{% endcapture %}
{% capture vancouver-style-result %}
{% include citation doi='10.1038/514550a' style='vancouver' %}
{% endcapture %}
{% include editing/example code=vancouver-style-code result=vancouver-style-result %}

{% include notice icon="tech" content="All of these features are driven by the
  [citation-js](https://citation.js.org/) library,
  which is very powerful, even supporting
  [your own custom CSL template](https://github.com/citation-js/citation-js/blob/3f3eee0813c7d578a454c34e402fa342d0693cfa/packages/plugin-csl/README.md#templates),
  if you having extra time burning a hole in your continuum." %}

## Citing by wiki page URL 

{% capture citation-by-id-code %}
{% raw %}{% include citation id="plugins/3d-viewer" %}{% endraw %}
{% endcapture %}
{% capture citation-by-id-result %}
{% include citation id="plugins/3d-viewer" %}
{% endcapture %}
{% include editing/example code=citation-by-id-code result=citation-by-id-result %}

The DOI used is pulled from the front matter of the given wiki page URL.

{% capture citation-short-syntax %}
If you want to cite the publication(s) associated with the current page, you
can simply write `{% raw %}{% include citation %}{% endraw %}` with no
arguments, and the DOI will be pulled from the front matter at the top.
{% endcapture %}
{% include notice icon="tip" content=citation-short-syntax %}

### Multiple citations

Some wiki pages have multiple publications associated with them.
In that case, all citations will be shown in the list:

{% capture cellprofiler-citations-code %}
{% raw %}{% include citation id="software/cellprofiler" %}{% endraw %}
{% endcapture %}
{% capture cellprofiler-citations-result %}
{% include citation id="software/cellprofiler" %}
{% endcapture %}
{% include editing/example code=cellprofiler-citations-code result=cellprofiler-citations-result %}

# Testimonials

The `testimonial` include is used to quote an individual. Available fields:

| **person** | any user from [this list](/people#list-of-contributors) |
| **quote**  | the text that will be displayed                         |
| **source** | a link to the original quotation                        |

{% include testimonial person='ctrueden'
  quote='ON VACATION UNTIL OCTOBER 5. For real this time!'
  source='https://forum.image.sc/t/42450' %}

*The following liquid code:*
```
{% raw %}{% include testimonial person='ctrueden'
  quote='ON VACATION UNTIL OCTOBER 5. For real this time!'
  source='https://forum.image.sc/t/42450' %}{% endraw %}
```
produces the testimonial shown here.

# Creating footnotes

## In your document

Use the
[kramdown syntax](https://kramdown.gettalong.org/quickref.html#footnotes)
in your document to refer to footnotes by number.

{% include notice icon="note" content="Regardless of where the liquid reference
  appears in your document, footnote text will always be at the bottom." %}

## In your citation

Specify the footnote number in the `include`.

*The following markdown and liquid code:*

```
This is a reference[^1].

{% raw %}{% include citation fn=1 doi='10.1371/journal.pone.0038011' %}{% endraw %}
```

*produces:*

This is a reference[^1].

{% include citation fn=1 doi='10.1371/journal.pone.0038011' %}
