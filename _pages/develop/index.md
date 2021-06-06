---
mediawiki: Development
title: Development
section: Extend:Develop
---

{% include notice icon="info" content='If your goal is to automate the behavior of ImageJ, consider writing a [script](/scripting/script-editor) using ImageJ\'s [Script Editor](/scripting/script-editor)—it is often much simpler than a plugin in Java.' %} 
This page provides an overview of ImageJ from the perspective of software development: how to use it from your programs, as well as how to modify or extend its capabilities via [plugins](/plugins).

## Quick start

-   **Learn to write [ImageJ scripts](/scripting)** from the [ImageJ tutorial notebooks](/tutorials).
-   **Learn to use ImageJ from Java** with the [ImageJ tutorial Maven projects](https://github.com/imagej/tutorials/tree/master/maven-projects).

## What is ImageJ?

{::nomarkdown}
<table style="width: 60%; font-size: large; margin-left: 25px; margin-top: 5px;">
  <tbody>
    <tr>
      <td style="padding: 15px 15px;">
        An end-user {% include wikipedia title='Application software' text='software application'%}
      </td>
    </tr>
    <tr>
      <td style="border-top: 1px #aaa solid; padding: 15px 15px;">
        <a href="Getting%20started"><img src="/media/develop/imagej-app.png" width="500px"></a>
      </td>
    </tr>
    <tr>
      <td>
        Reusable {% include wikipedia title='Library (computing)' text='software libraries'%}
      </td>
    </tr>
    <tr>
      <td style="padding: 0 15px 15px 35px; font-size: small;">
      {%- highlight java -%}
public void loadAndDisplay(File file) {
  ImageJ ij = new ImageJ();
  Object data = ij.io().open(file);
  ij.ui().show(data);
}
      {%- endhighlight -%}
      </td>
    </tr>
    <tr>
      <td style="border-top: 1px #aaa solid; padding: 15px 15px 0 15px;">
        An extensible collection of <a href="plugins">plugins</a> and <a href="/libs/scijava#services">services</a>
      </td>
    </tr>
    <tr>
      <td style="padding: 15px 0 30px 45px;">
        <a href="/libs/scijava"><img src="/media/logos/scijava.png" height="72px"></a>
      </td>
    </tr>
    <tr>
      <td style="border-top: 1px #aaa solid; padding: 15px 15px 0 15px;">
        <em>"Write once, run anywhere"</em> <a href="/libs/imagej-ops">image processing routines</a>
      </td>
    </tr>
    <tr>
      <td style="padding: 15px 0 15px 25px;">
        <a href="/libs/imagej-ops"><img src="/media/develop/write-once-run-anywhere.png" width="500px"></a>
      </td>
    </tr>
  </tbody>
</table>
{:/}


## Project structure

ImageJ is divided into three parts---ImageJ, ImgLib2, and SciJava---with responsibilities as follows:

{::nomarkdown}
<table>
  <thead>
    <tr class="header">
      <th style="font-size: 56px; width: 350px">
        {% include icon name='ImageJ' size='72px' %}<a href="/software/imagej">ImageJ</a>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <span style="font-size: large">ImageJ provides <strong>image-specific components</strong></span>
        <ul>
          <li><a href="/libs/imagej-common">ImageJ Common</a></li>
          <li><a href="/libs/imagej-ops">ImageJ Ops</a></li>
          <li><a href="/plugins/updater">ImageJ Updater</a></li>
          <li><a href="/libs/imagej-legacy">ImageJ Legacy</a></li>
          <li><a href="/libs/scifio">SCIFIO</a></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td style="font-size: 56px">
        {% include icon name='ImgLib2' size='72px' %}<a href="/libs/imglib2">ImgLib2</a>
      </td>
    </tr>
    <tr>
      <td>
        <span style="font-size: large">ImgLib2 provides the <strong>core image data model</strong></span><br>
        <ul>
          <li>Extensible pixel types – not just uint8, uint16, float32</li>
          <li>Extensible data sources – not just files on disk</li>
          <li>Extensible sample organizations – not just arrays</li>
          <li>Extensible dimensionality – not just X, Y, Z and time</li>
          <li>Interface-driven design</li>
        </ul>
      </td>
    <tr>
      <td style="width: 350px;">
        <a href="/libs/scijava"><img src="/media/logos/scijava.png" height="72px"></a>
      </td>
    </tr>
      <td>
        <span style="font-size: large">SciJava provides <strong>scientific components more general than images</strong></span><br>
        <ul>
          <li>Application container</li>
          <li>Plugin framework</li>
          <li>Module framework</li>
          <li>Display and UI frameworks</li>
          <li>Scripting framework and plugins</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>
{:/}

For full details on the technical structure of ImageJ, see the [Architecture](architecture) page.

## Key developer tools

There are four indispensable software development tools on which ImageJ relies:

| {% include icon name='GitHub' %}  | [GitHub](github)   | A website which hosts all of ImageJ's [source code](source) and [issue trackers](project-management#issue-tracking). GitHub is ImageJ's nexus of online collaboration (i.e., "social coding"). |
| {% include icon name='Git' %}     | [Git](git)         | A first-class {% include wikipedia title='Distributed version control' text='distributed'%} {% include wikipedia title='Version control' text='version control'%} system. Git saves "snapshots" of the source code, keeping a history of changes. |
| {% include icon name='Maven' %}   | [Maven](maven)     | A {% include wikipedia title='Build automation' text='build automation'%} tool with great dependency management. Maven converts source code into program binaries, and much more. |
| {% include icon name='Eclipse' %} | [Eclipse](eclipse) | An [integrated development environment](ides) (IDE) used by many ImageJ developers. Eclipse makes it much easier to explore and edit the source code.<br>Although: ImageJ can be developed using [*any* IDE](ides) which supports [Maven](maven). |

See the [Project management](project-management) page for further details.

## Source code

[ImageJ](/software/imagej) and related [SciJava](/libs/scijava) software projects are [open source](/licensing/open-source). The code is organized into [well-separated](architecture#modularity) projects.

See the [source code](source) page for further details.

## Tutorials

Start with the [ImageJ tutorial notebooks](/tutorials)!

{::nomarkdown}
<table class="top striped-columns">
  <tbody>
    <tr>
      <th>Learning the ImageJ API</th>
      <th>ImageJ plugins</th>
      <th>The Fiji distribution of ImageJ</th>
    </tr>
    <tr>
      <td>
        <ul>
          <li><a href="https://github.com/imagej/tutorials">ImageJ tutorials</a></li>
          <li><a href="/libs/imglib2/examples">ImgLib2 Examples</a></li>
          <li><a href="ij1-ij2-cheat-sheet">ImageJ1-ImageJ2 cheat sheet</a></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><a href="plugins">Writing ImageJ2 plugins</a></li>
          <li><a href="improving-the-code">Contributing to an existing plugin</a></li>
          <li><a href="/contribute/distributing">Distributing your plugin</a></li>
          <li><a href="ij1-plugins">Writing ImageJ 1.x plugins</a></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><a href="/software/fiji/developing">Developing Fiji</a></li>
          <li><a href="eclipse">Fiji + Eclipse</a </li>
          <li><a href="/contribute/fiji">Fiji contribution requirements</a </li>
          <li><a href="supported-compilers">Supported Compilers</a </li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>
{:/}
