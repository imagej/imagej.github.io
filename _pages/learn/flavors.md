---
title: Flavors of ImageJ
section: Learn:ImageJ Basics
doi: 10.1002/mrd.22489

timeline-imagej:
- 1987 | NIH Image             | TODO
- 1997 | ImageJ                | TODO
- 2000 | ImageSXM              | TODO
- 2005 | WCIF ImageJ, ImageJA  | TODO
- 2007 | MBF ImageJ            | TODO
- 2008 | Fiji                  | TODO
- 2009 | ImageJ2               | TODO
- 2015 | ImageJFX              | TODO
---

There are a many different derivatives of ImageJ with very similar names, and some confusion is inevitable. Below is a table which should help to clarify the purpose of each. For the historical context of these projects, see [History](#history) below.

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td></td>
      <th>Name</th>
      <th>Author/Maintainer(s)</th>
      <th>Description</th>
      <th>Initiated</th>
      <th>Status</th>
    </tr>
    <tr>
      <td><img src="/media/icons/imagej.png" width="64"/></td>
      <td><a href="/software/imagej">ImageJ</a></td>
      <td>{% include person id='rasband' %}</td>
      <td>The original version of ImageJ which has been in development since 1997.
        It has a strong, established user base, with thousands of plugins and
        macros for performing a wide variety of tasks. Sometimes referred to as
        <strong>the original ImageJ</strong> or <strong>ImageJ 1.x</strong> for
        technical clarity, or informally with the shorthands
        <strong>ImageJ1</strong> or <strong>IJ1</strong>.</td>
      <td>1997</td>
      <td>Active</td>
    </tr>
    <tr>
      <td><img src="/media/icons/imagej2.png" width="64"/></td>
      <td><a href="/software/imagej2">ImageJ2</a></td>
      <td><a href="/people">ImageJ2 developers</a></td>
      <td>A new version of ImageJ targeting scientific multidimensional image
        data. It is a complete rewrite of the
        <a href="/software/imagej">original ImageJ</a>, but includes the
        original ImageJ with a compatibility layer, so that old-style plugins
        and macros can run the same as always. ImageJ2 provides several
        significant new features, such as an automatic
        <a href="updater">updater</a>, and improved
        <a href="scripting">scripting</a> capabilities.</td>
      <td>Dec. 2009</td>
      <td>Active</td>
    </tr>
    <tr>
      <td><img src="/media/icons/fiji.png" width="64"/></td>
      <td><a href="/software/fiji">Fiji</a></td>
      <td><a href="/people">Fiji contributors</a></td>
      <td><strong>F</strong>iji <strong>i</strong>s <strong>J</strong>ust
        <strong>I</strong>mageJ, with extras. It is a distribution of ImageJ
        and ImageJ2 with many plugins useful for scientific image analysis in
        fields such as life sciences. It is actively maintained, with updates
        released often.</td>
      <td><a href="/people/dscho#a-short-story-about-fiji">Dec. 2007</a></td>
      <td>Active</td>
    </tr>
    <tr>
      <td><img src="https://ij.imjoy.io/assets/icons/chrome/chrome-installprocess-128-128.png" width="64"/></td>
      <td><a href="/software/imagej-js">ImageJ.JS</a></td>
      <td>{% include person id='oeway' %}</td>
      <td>ImageJ.JS is a web version of ImageJ that runs in the browser without
        installation, compiled from Java to JavaScript using the
        <a href="https://leaningtech.com/cheerpj/">Cheerpj compiler</a> and
        integrated with the <a href="/software/imjoy">ImJoy</a> plugin system.
        It's accessible from
        <a href="https://ij.imjoy.io">https://ij.imjoy.io</a>
        and also supports mobile devices and tablets.
      </td>
      <td>2020</td>
      <td>Active</td>
    </tr>
    <tr>
      <td></td>
      <td><a href="/software/imagejfx">ImageJFX</a></td>
      <td>{% include person id='cmongis' %}</td>
      <td>ImageJFX is a new user interface for ImageJ, built using
        {% include wikipedia title='JavaFX' text='JavaFX' %}.</td>
      <td>2015</td>
      <td>Abandoned</td>
    </tr>
    <tr>
      <td><img src="/media/icons/imagesxm.png" width="64"/></td>
      <td><a href="/software/imagesxm">ImageSXM</a></td>
      <td>Steve Barrett</td>
      <td>Image SXM is a version of NIH Image that has been extended to handle
        the loading, display and analysis of scanning microscope images.</td>
      <td>May 1993</td>
      <td>Active</td>
    </tr>
    <tr>
      <td><img src="/media/software/astroimagej.png" width="64"/></td>
      <td><a href="http://www.astro.louisville.edu/software/astroimagej/">AstroImageJ</a></td>
      <td><a href="http://www.astro.louisville.edu/john_kielkopf/">John Kielkopf</a></td>
      <td>AstroImageJ is ImageJ with astronomy plugins and macros installed.</td>
      <td>Unknown</td>
      <td>Active</td>
    </tr>
    <tr>
      <td></td>
      <td><a href="http://www.rawak.de/ij2x/imagej2x.html">ImageJ2x</a></td>
      <td><a href="http://rawak.de/">Rawak Software</a></td>
      <td>ImageJ2x is a fork of the original ImageJ, modified to use a Swing interface.</td>
      <td>Unknown</td>
      <td>Last update:<br>May 2015</td>
    </tr>
    <tr>
      <th colspan=6>Closed-source variants</th>
    </tr>
    <tr>
      <td><img src="/media/logos/eu-hou.png" width="64"/></td>
      <td><a href="http://www.euhou.net/index.php?option=com_content&amp;task=view&amp;id=7&amp;Itemid=9">SalsaJ</a></td>
      <td><a href="http://www.euhou.net/">EU-HOU</a></td>
      <td>SalsaJ is a closed-source fork of the original ImageJ intended for
        use with professional astronomy images. It was designed to be used in
        classrooms, and has been localized into over 30 different
        languages.</td>
      <td>Unknown</td>
      <td>Last update:<br>Oct. 2012</td>
    </tr>
    <tr>
      <th colspan=6>Obsolete variants</th>
    </tr>
    <tr>
      <td></td>
      <td><a href="/software/mbf-imagej">MBF ImageJ</a></td>
      <td>Tony Collins</td>
      <td>The MBF "ImageJ for Microscopy" bundle (formerly
        <a href="http://www.uhnres.utoronto.ca/facilities/wcif/imagej/">WCIF
        ImageJ</a>) is a collection of plugins and macros, collated and
        organized by the MacBiophotonics facility.<br><br>It went hand in
        hand with a comprehensive manual describing how to use the bundle
        with light microscopy image data. It was a great resource by
        microscopists, for microscopists. Unfortunately, the manual went
        offline in late 2012. In response, the software team at
        <a href="/orgs/loci">LOCI</a> created the
        <a href="/imaging">Cookbook</a> user guide and
        <a href="update_site">update site</a>, which
        includes most of the same plugins.</td>
      <td>2005</td>
      <td>Defunct<br>(Last update:<br>Dec. 2009)</td>
    </tr>
    <tr>
      <td><img src="/media/icons/imagej.png" width="64"/></td>
      <td><a href="/libs/imageja">ImageJA</a></td>
      <td><a href="/people">{% include person id='rasband' %} (author); ImageJ2 team (maintainers)</a></td>
      <td>ImageJA was a project that provided a clean <a href="/develop/git">Git</a>
        history of the original ImageJ, with a proper <code>pom.xml</code> file
        so that it could be used with Maven without hassles. The ImageJ project
        has since been updated to deploy releases to Maven Central directly,
        without the need for the ImageJA project as an intermediate.</td>
      <td>Jul. 2005</td>
      <td>Superseded by ImageJ</td>
    </tr>
    <tr>
      <td></td>
      <td><a href="/software/imagejx">ImageJX</a></td>
      <td>{% include person id='tnargsirrah' %}</td>
      <td>ImageJX was created as a means to discuss and explore
        improvements to ImageJ. There was an
        <a href="https://groups.google.com/g/imagejx">ImageJX mailing
        list</a> as well as an ImageJX software prototype. The ImageJX
        software prototype was a proof of concept—an attempt to
        reorganize ImageJ's internals to make it more flexible. The
        prototype demonstrated this flexibility by recasting the program
        in Swing. The ImageJX project formed the basis of an application
        to NIH for funding, which is what launched the ImageJ2 project
        (see above).</td>
      <td>Mar. 2009</td>
      <td>Superseded by ImageJ2</td>
    </tr>
    <tr>
      <td><img src="/media/icons/nih-image.png"/></td>
      <td><a href="/software/nih-image">NIH Image</a></td>
      <td>{% include person id='rasband' %}</td>
      <td>NIH Image is a public domain image processing and analysis
        program for the Macintosh. It is the direct predecessor of ImageJ,
        and is no longer under active development (though see ImageSXM
        above).</td>
      <td>1993 or earlier</td>
      <td>Superseded by ImageJ</td>
    </tr>
  </tbody>
</table>
{:/}

## History

The first imaging program that {% include person id='rasband' %} developed, starting in the late 70s, was called simply "Image". It was written in Pascal, ran on PDP-11 minicomputers and ran in only 64KB of memory! Rasband started work on the second, [NIH Image](/software/nih-image), in 1987 when the Mac II became available. Rasband was a Mac enthusiast, and the Mac II had card slots just like the PDP-11. Rasband started work on ImageJ in 1997, when Java was becoming popular. Rasband was intrigued by the idea of creating a version of NIH Image that would "run anywhere", including as an applet in Web browsers.

## Timeline

Here is a timeline of software development related to ImageJ:

{% comment %}{% include timeline title="Flavors of ImageJ" timeline=page.timeline-imagej initial='1987' %}{% endcomment %}

![](/media/software/timeline-history-of-imagej.png)

## Publications

{% include citation %}

{% include citation id='software/imagej' %}

See also [Citing](/contribute/citing).
