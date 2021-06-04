---
mediawiki: Development
title: Development
section: Extend:Develop
---

{% include notice icon="info" content='If your goal is to automate the behavior of ImageJ, consider writing a [script](/scripting/script-editor) using ImageJ"s [Script Editor](/scripting/script-editor)—it is often much simpler than a plugin in Java.' %} 
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
        <p>An end-user {% include wikipedia title='Application software' text='software application'%}</p>
      </td>
    </tr>
    <tr>
      <td style="border-top: 1px #aaa solid; padding: 15px 15px;">
        <p><a href="Getting%20started"><img src="/media/develop/imagej-app.png" width="500px"></a></p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Reusable {% include wikipedia title='Library (computing)' text='software libraries'%}</p>
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
        <p>An extensible collection of <a href="plugins">plugins</a> and <a href="services">services</a></p>
      </td>
    </tr>
    <tr>
      <td style="padding: 15px 0 30px 45px;">
        <p><a href="/libs/scijava"><img src="/media/logos/scijava.png" height="72px"></a></p>
      </td>
    </tr>
    <tr>
      <td style="border-top: 1px #aaa solid; padding: 15px 15px 0 15px;">
        <p><em>"Write once, run anywhere"</em> <a href="/libs/imagej-ops">image processing routines</a></p>
      </td>
    </tr>
    <tr>
      <td style="padding: 15px 0 15px 25px;">
        <p><a href="/libs/imagej-ops"><img src="/media/develop/write-once-run-anywhere.png" width="500px"></a></p>
      </td>
    </tr>
  </tbody>
</table>
{:/}


## Project structure

ImageJ is divided into three parts:

{::nomarkdown}
<table>
  <thead>
    <tr class="header">
      <th style="font-size: 56px; width: 350px">
        <p>{% include icon name='ImageJ' size='72px' %}<a href="/software/imagej">ImageJ</a></p>
      </th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <p><span style="font-size: large"><strong>Image-specific components</strong></span></p>
      </td>
      <td>
        <ul>
          <li>
            <a href="/libs/imagej-common">ImageJ Common</a>
          </li>
          <li>
            <a href="/libs/imagej-ops">ImageJ Ops</a>
          </li>
          <li>
            <a href="/plugins/updater">ImageJ Updater</a>
          </li>
          <li>
            <a href="/libs/imagej-legacy">ImageJ Legacy</a>
          </li>
          <li>
            <a href="/libs/scifio">SCIFIO</a>
          </li>
        </ul>
      </td>
    </tr>
    <tr>
      <td style="font-size: 56px; bold">
        <p>{% include icon name='ImgLib2' size='72px' %}<a href="/libs/imglib2">ImgLib2</a></p>
      </td>
      <td style="width: 350px;">
        <p><a href="/libs/scijava"><img src="/media/logos/scijava.png" height="72px"></a></p>
      </td>
    </tr>
    <tr>
      <td style="text-align: center; vertical-align: top">
        <p><span style="font-size: large"><strong>Core image data model</strong></span><br></p>
        <ul>
          <li>Extensible pixel types – not just uint8, uint16, float32</li>
          <li>Extensible data sources – not just files on disk</li>
          <li>Extensible sample organizations – not just arrays</li>
          <li>Extensible dimensionality – not just X, Y, Z and time</li>
          <li>Interface-driven design</li>
        </ul>
      </td>
      <td style="text-align: center; vertical-align: top">
        <p><span style="font-size: large"><strong>More general than images</strong></span><br></p>
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

For full details on the technical structure of ImageJ, see the [Architecture](/develop/architecture) page.

## Key developer tools

There are four indispensable software development tools on which ImageJ relies:

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td style="vertical-align: middle">
        <p>{% include icon name='GitHub' %}</p>
      </td>
      <td>
        <p><a href="/develop/github">GitHub</a></p>
      </td>
      <td>
        <p>A website which hosts all of ImageJ's <a href="source_code">source code</a> and <a href="issues">issue trackers</a>. GitHub is ImageJ's nexus of online collaboration (i.e., "social coding").</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include icon name='Git' %}</p>
      </td>
      <td>
        <p><a href="/develop/git">Git</a></p>
      </td>
      <td>
        <p>A first-class {% include wikipedia title='Distributed version control' text='distributed'%} {% include wikipedia title='Version control' text='version control'%} system. Git saves "snapshots" of the source code, keeping a history of changes.</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include icon name='Maven' %}</p>
      </td>
      <td>
        <p><a href="/develop/maven">Maven</a></p>
      </td>
      <td>
        <p>A {% include wikipedia title='Build automation' text='build automation'%} tool with great dependency management. Maven converts source code into program binaries, and much more.</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include icon name='Eclipse' %}</p>
      </td>
      <td>
        <p><a href="/develop/eclipse">Eclipse</a></p>
      </td>
      <td>
        <p>An <a href="/develop/ides">integrated development environment</a> (IDE) used by many ImageJ developers. Eclipse makes it much easier to explore and edit the source code.<br>
        Although: ImageJ can be developed using <a href="/develop/ides"><em>any</em> IDE</a> which supports <a href="/develop/maven">Maven</a>.</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

See the [Project management](/develop/project-management) page for further details.

## Source code

[ImageJ](/software/imagej) and related [SciJava](/libs/scijava) software projects are [open source](/licensing/open-source). The code is organized into [well-separated](/develop/architecture#modularity) projects.

See the [source code](/develop/source) page for further details.

## Tutorials

Start with the [ImageJ tutorial notebooks](/tutorials)!

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td style="vertical-align: top">
        <p><strong>Learning the ImageJ API</strong></p>
      </td>
      <td>
        <p><strong>ImageJ plugins</strong></p>
      </td>
      <td>
        <p><strong>The Fiji distribution of ImageJ</strong></p>
      </td>
    </tr>
    <tr>
      <td>
        <ul>
          <li>
            <a href="https://github.com/imagej/tutorials">ImageJ tutorials</a>
          </li>
          <li>
            <a href="/libs/imglib2/examples">ImgLib2 Examples</a>
          </li>
          <li>
            <a href="/develop/ij1-ij2-cheat-sheet">ImageJ1-ImageJ2 cheat sheet</a>
          </li>
        </ul>
      </td>
      <td style="vertical-align: top">
        <ul>
          <li>
            <a href="/develop/plugins">Writing ImageJ2 plugins</a>
          </li>
          <li>
            <a href="/develop/improving-the-code">Contributing to an existing plugin</a>
          </li>
          <li>
            <a href="/contribute/distributing">Distributing your plugin</a>
          </li>
          <li>
            <a href="/develop/ij1-plugins">Writing ImageJ 1.x plugins</a>
          </li>
        </ul>
      </td>
      <td>
        <ul>
          <li>
            <a href="/software/fiji/developing">Developing Fiji</a>
          </li>
          <li>
            <a href="/develop/eclipse">Fiji + Eclipse</a>
          </li>
          <li>
            <a href="/contribute/fiji">Fiji contribution requirements</a>
          </li>
          <li>
            <a href="/develop/supported-compilers">Supported Compilers</a>
          </li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>
{:/}
