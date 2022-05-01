---
title: Citing
section: Contribute
nav-links: true
---

{% include notice icon="info" content='This page describes how to *cite* [ImageJ](/software/imagej) and related projects.

-   For information on who *contributes* to these projects, see [Contributors](/people).
-   For information on who *maintains* these projects, see [Governance](/contribute/governance).
-   For information on how these projects are *funded*, see [Funding](/contribute/funding).' %}

## Guidelines

We ask users to cite:

1.  Any [specific publications](#citable-software) of [plugins](/plugins) used.

2.  The general paper of [ImageJ flavor(s)](/learn/flavors) used; e.g.:
    - If you used [Fiji](/software/fiji), cite the [Fiji paper](/software/fiji#publication).
    - If you used [ImageJ2](/software/imagej2), cite the [ImageJ2 paper](/software/imagej2#publication).
    - If you used the original [ImageJ](/software/imagej), cite the [ImageJ paper](/software/imagej#publication).

If journal reference limits interfere, the plugin-specific publications should take precedence.

In general, please cite these projects—their long-term future depends on it!

Thank you for your support.

<style>
.publication-box {
  display: grid;
  grid-template-columns: auto auto;
}
.publication-box > div:first-child {
  text-align: center;
  width: 4em;
  line-height: 1em;
  padding-bottom: 1em;
}
.publication-box ul {
  list-style: none;
}
</style>

## ImageJ and variants

<div class="publication-box">
<div>{% include icon name='ImageJ' %}
<br><a href="/software/imagej">ImageJ</a></div>
{% include citation id='software/imagej' %}</div>

<div class="publication-box">
<div>{% include icon name='ImageJ2' %}
<br><a href="/software/imagej2">ImageJ2</a></div>
{% include citation id='software/imagej2' %}</div>

<div class="publication-box">
<div>{% include icon name='Fiji' %}
<br><a href="/software/fiji">Fiji</a></div>
{% include citation id='software/fiji' %}</div>

## Supporting libraries

<div class="publication-box">
<div>{% include icon name='ImgLib2' %}
<br><a href="/libs/imglib2">ImgLib2</a></div>
{% include citation id='libs/imglib2' %}</div>

<div class="publication-box">
<div>{% include icon name='SciJava' %}
  <br><a href="/libs/scijava#scijava-common">SciJava Common</a></div>
  {% include citation id='libs/scijava' %}</div>

<div class="publication-box">
<div>{% include icon name='SCIFIO' %}
  <br><a href="/libs/scifio">SCIFIO</a></div>
  {% include citation id='libs/scifio' %}</div>

<div class="publication-box">
<div>{% include icon name='ImageJ2' %}
  <br><a href="/libs/imagej-ops">ImageJ Ops</a></div>
  {% include citation id='libs/imagej-ops' %}</div>

## Citable software

The following table lists all citable software packages, plugins, etc.,
documented on the site. To add a tool to this list, add the `doi:` for
its publication to the tool's wiki page.

<table>
  <tr>
    <th>Project</th>
    <th>Publication(s) to cite</th>
  </tr>
{%- for p in site.pages -%}
  {%- if p.doi -%}
  <tr>
    <td><a href="{{p.url}}">{{p.title}}</a></td>
    <td>{% include citation doi=p.doi %}</td>
  </tr>
  {%- elsif p.ref -%}
  <tr>
    <td><a href="{{p.url}}">{{p.title}}</a></td>
    <td>{{p.ref}}</td>
  </tr>
  {%- endif -%}
{%- endfor -%}
</table>

## See also

* [Publications using Fiji](/software/fiji/publications)
