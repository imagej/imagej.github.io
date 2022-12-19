---
title: Downloads
description: This page provides download links for ImageJ.
---

{% include aside icon="icons/imagej2" title="Where is [ImageJ2](/software/imagej2)?" content="A standalone download of ImageJ2 is not yet available, due to how the core [ImageJ update sites](/update-sites) are currently structured. The ImageJ2 team is working hard to change this, but in the meantime, please use the [Fiji distribution of ImageJ](/software/fiji), which is built on ImageJ2 and bundles many additional useful plugins." %}

Which distribution of ImageJ would you like to download?

| [![](/media/icons/fiji.svg){:width="96px"}<br>Fiji](/software/fiji/downloads) | [![](/media/icons/imagej.png){:width="96px"}<br>ImageJ](https://imagej.net/ij/download.html) |
{:.plain.center.center-text}

{% capture help-me-decide %}
Here are a few highlights of the two flavors of ImageJ. It's not an exhaustive comparison, just a summary to give you an idea of their respective strengths.

<style>
table.help-me-decide th:first-child, table.help-me-decide td:first-child {
  border-right: 1px solid lightgray;
}
table.help-me-decide tr:first-child {
 border-bottom: 1px solid lightgray;
}
table.help-me-decide td {
  font-size: 0.8em;
  line-height: 1.3em;
}
table.help-me-decide ul {
  margin-bottom: 0;
}
table.help-me-decide li {
  padding-bottom: 0.3em;
}
</style>
<table class="plain top help-me-decide">
<tr>
  <th class="center-text middle"><a href="/software/imagej">{% include img src="icons/imagej" width=24 %} ImageJ</a></th>
  <th class="center-text middle"><a href="/software/imagej2">{% include img src="icons/imagej2"  width=24 %} ImageJ2</a></th>
</tr>
<tr>
  <td><ul>
    <li>Lightweight (ImageJ is a single JAR file)</li>
    <li>Small download (81 MB)</li>
    <li>Simple software architecture is <a href="https://imagej.net/ij/developer/">approachable for non-programmers</a></li>
    <li>Often faster than Fiji, for the scenarios ImageJ supports</li>
    <li><a href="/licensing/#a-note-about-imagej">No copyright whatsoever</a></li>
    <li>Very stable and mature</li>
    <li><a href="/people/rasband">Responsive and experienced maintainer</a> fixes bugs quickly</li>
    <li>Runs natively on M1 (arm64) Macs</li>
  </ul></td>
  <td><ul>
    <li><a href="https://imagej.net/presentations/2017-02-16-imagej2-neubias/#/24">More powerful</a></li>
    <li>Robust <a href="/develop/architecture">software architecture</a></li>
    <li>Advanced <a href="/scripting">scripting</a> features</li>
    <li><a href="/licensing">Licensed as permissive open source</a></li>
    <li><a href="/libs/imagej-legacy">Backwards compatible with the original ImageJ</a></li>
    <li><a href="/plugins/updater">ImageJ Updater</a> lets you install plugins from <a href="/update-sites">ImageJ update sites</a></li>
    <li>Support for <a href="/learn/headless">headless execution</a></li>
    <li><a href="/scripting/python">Works from Python</a>, including from Jupyter Notebooks</li>
    <li>ImageJ2 scripts are usable from <a href="/libs/scijava">various software tools</a></li>
    <li>Integrated <a href="/learn#the-search-bar">search bar</a></li>
  </ul></td>
</tr>
</table>

For a thorough discussion of the two projects and their differences, please read these papers:

* {% include citation id='software/imagej2' %}
* {% include citation id='learn/flavors' %}
* {% include citation id='software/imagej' %}

Still have questions? Ask on the [Image.sc Forum](https://forum.image.sc/tag/imagej)!
{% endcapture %}
<details class="shadowed-box"><summary><strong>Need help deciding? Click here.</strong></summary>
{{help-me-decide | markdownify}}
</details>

# System requirements

ImageJ will run on any system that has a Java 8 (or later) runtime installed. This includes, but is not limited to:

1.  Windows XP, Vista, 7 or 8 with Java installed from [java.com](https://java.com/)
2.  Mac OS X 10.8 "Mountain Lion" or later with Java installed from [java.com](https://java.com/)
3.  Ubuntu Linux 12.04 LTS or later with OpenJDK 8 installed

# ImageJ as a web application

In lieu of downloading and installing a desktop application, you can run
ImageJ in your web browser (on desktops or mobile devices).

You can try it here: [https://ij.imjoy.io](https://ij.imjoy.io).

And see [ImageJ.JS](/software/imagej-js) for details.

# Troubleshooting

  - Many common questions are answered on the [FAQ](/learn/faq) and [Troubleshooting](/learn/troubleshooting) pages.
  - If you encounter bugs, please see the [Getting Help](/discuss) page.

# Source code

See the [source code](/develop/source) page for details on obtaining the ImageJ source code.

## See also

  - [ImageJ2 development releases](/software/imagej2/development-releases) for early versions of [ImageJ2](/software/imagej2).
