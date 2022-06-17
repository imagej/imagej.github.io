---
title: Development
section: Extend:Develop
project: /software/imagej2
---

{% include notice icon="info" content="If your goal is to automate the behavior of ImageJ, consider writing a [script](/scripting/script-editor) using ImageJ2's [Script Editor](/scripting/script-editor)—it is often much simpler than a plugin in Java." %} 
This page provides an overview of ImageJ2 from the perspective of software development: how to use it from your programs, as well as how to modify or extend its capabilities via [plugins](/plugins).

## Quick start

-   **Learn to write [scripts](/scripting)** from the [tutorial notebooks](/tutorials/notebooks).
-   **Learn to use ImageJ2 from Java** with the [tutorial Maven projects](https://github.com/imagej/tutorials/tree/master/java).

## What is ImageJ2?

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

ImageJ2 is divided into three parts---ImageJ2, ImgLib2, and SciJava---with responsibilities as follows:

{::nomarkdown}
<style>
  .layer {
    display: flex;
    flex-wrap: wrap;
  }
  .project {
    flex-grow: 1;
    border: 1px solid lightgray;
    margin-bottom: 0.5em;
    min-width: 350px;
    text-align: center;
  }
  .project div:first-child {
    font-size: 3rem;
    white-space: nowrap;
    padding: 0.25em;
  }
  .project p {
    margin: 0;
    padding: 0;
  }
  .project p a, .project p img {
    vertical-align: middle;
  }
  .project p:nth-child(2) {
    font-size: 1rem;
    font-weight: bold;
    margin: 0;
  }
  .project ul.links {
    list-style-type: none;
    padding-top: 0.5em;
    padding-bottom: 1em;
  }
  .project ul.links li {
    display: inline;
    background-color: peachpuff;
    border-radius: 0.5em;
    margin: 0.5em 0.1em;
    padding: 0.3em 0.5em;
    line-height: 2.3em;
    white-space: nowrap;
  }
  .project ul.bullets {
    display: inline-block;
    text-align: left;
    padding: 0.5em 1em 1em 2em;
    list-style-type: square;
  }
</style>
<div class="layer">
  <div class="project">
    <div>
      <p>{% include icon name='ImageJ2' size='72px' %}<a href="/software/imagej2">ImageJ2</a></p>
      <p>image-specific components</p>
    </div>
    <div>
      <ul class="links">
        <li><a href="/libs/imagej-common">ImageJ Common</a></li>
        <li><a href="/libs/imagej-ops">ImageJ Ops</a></li>
        <li><a href="/plugins/updater">ImageJ Updater</a></li>
        <li><a href="/libs/imagej-legacy">ImageJ Legacy</a></li>
        <li><a href="/libs/scifio">SCIFIO</a></li>
      </ul>
    </div>
  </div>
</div>
<div class="layer">
  <div class="project">
    <div>
      <p><a href="/libs/scijava"><img src="/media/logos/scijava.png" height="72px"></a></p>
      <p>more general than images</p>
    </div>
    <div>
      <ul class="bullets">
        <li>Application container</li>
        <li>Plugin framework</li>
        <li>Module framework</li>
        <li>Display and UI frameworks</li>
        <li>Scripting framework and plugins</li>
      </ul>
    </div>
  </div>
  <div class="project">
    <div>
      <p>{% include icon name='ImgLib2' size='72px' %}<a href="/libs/imglib2">ImgLib2</a></p>
      <p>core image data model</p>
    </div>
    <div>
      <ul class="bullets">
        <li>Extensible pixel types – not just uint8, uint16, float32</li>
        <li>Extensible data sources – not just files on disk</li>
        <li>Extensible sample organizations – not just arrays</li>
        <li>Extensible dimensionality – not just X, Y, Z and time</li>
        <li>Interface-driven design</li>
      </ul>
    </div>
  </div>
</div>
{:/}

For full details on the technical structure of ImageJ2, see the [Architecture](architecture) page.

## Key developer tools

There are four indispensable software development tools on which ImageJ2 relies:

| {% include icon name='GitHub' %}  | [GitHub](github)   | A website which hosts all the [source code](source) and [issue trackers](project-management#issue-tracking). GitHub is the ImageJ community's nexus of online collaboration (i.e., "social coding"). |
| {% include icon name='Git' %}     | [Git](git)         | A first-class {% include wikipedia title='Distributed version control' text='distributed'%} {% include wikipedia title='Version control' text='version control'%} system. Git saves "snapshots" of the source code, keeping a history of changes. |
| {% include icon name='Maven' %}   | [Maven](maven)     | A {% include wikipedia title='Build automation' text='build automation'%} tool with great dependency management. Maven converts source code into program binaries, and much more. |
| {% include icon name='Eclipse' %} | [Eclipse](eclipse) | An [integrated development environment](ides) (IDE) used by many developers in this community. Eclipse makes it much easier to explore and edit the source code.<br>Although: ImageJ and friends can be developed using [*any* IDE](ides) which supports [Maven](maven). |

See the [Project management](project-management) page for further details.

## Source code

[ImageJ2](/software/imagej2) and related [SciJava](/libs/scijava) software projects are [open source](/licensing/open-source). The code is organized into [well-separated](architecture#modularity) projects.

See the [source code](source) page for further details.

## Tutorials

Start with the [ImageJ2 tutorial notebooks](/tutorials/notebooks)!

{::nomarkdown}
<table class="top striped-columns">
  <tbody>
    <tr>
      <th>Learning the ImageJ2 API</th>
      <th>ImageJ2 plugins</th>
      <th>The Fiji distribution of ImageJ2</th>
    </tr>
    <tr>
      <td>
        <ul>
          <li><a href="https://github.com/imagej/tutorials">ImageJ2 tutorials</a></li>
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
