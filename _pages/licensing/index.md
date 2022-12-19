---
title: Licensing
description: This page describes the legal structure of ImageJ and SciJava projects.
section: Contribute:Licensing
---

{% include notice icon="info" content="This page describes the *legal* structure of [SciJava](/libs/scijava) projects.

-   For information on their *technical* structure, see [Architecture](/develop/architecture).
-   For information on their *social* structure, see [Governance](/contribute/governance)." %}

The [ImageJ2](/software/imagej2) project, and related projects in the
[SciJava](/libs/scijava) component collection, are licensed as
[open source](/licensing/open-source) software (OSS) projects.

For an introduction to OSS licensing, see
[http://choosealicense.com/](http://choosealicense.com/).

## Project summary

The following table summarizes the dominant license of each project's components.

{::nomarkdown}
<style>
  table.licensing td, table.licensing th {
    text-align: center;
  }
  table.licensing td {
    vertical-align: middle;
  }
  table.licensing th {
    vertical-align: bottom;
  }
  .vertical {
    min-height: 10em;
    max-height: 10em;
    height: 10em;
    min-width: 1em;
    width: 1em;
    max-width: 1em;
    vertical-align: middle !important;
    text-align: left; !important;
    padding: 0;
    margin: 0;
  }
  .vertical p {
    white-space: nowrap;
    transform: rotate(-90deg);
    text-align: left !important;
    vertical-align: middle !important;
    min-width: 10em;
    max-width: 10em;
    line-height: 1em;
    margin-left: -4em;
    padding-left: 0.5em;
  }
</style>
<table class="licensing">
  <tbody>
    <tr>
      <th colspan=4 style="text-align: center">Basics</th>
      <th colspan=3>Required*</th>
      <th colspan=7>Permitted*</th>
    </tr>
    <tr>
      <th>Logo</th>
      <th>Project</th>
      <th>License</th>
      <th>Type</th>
      <th class="vertical"><p>Disclose source</p></th>
      <th class="vertical"><p>License and<br>copyright notice</p></th>
      <th class="vertical"><p>State changes</p></th>
      <th class="vertical"><p>Commercial use</p></th>
      <th class="vertical"><p>Distribution</p></th>
      <th class="vertical"><p>Modification</p></th>
      <th class="vertical"><p>Patent grant</p></th>
      <th class="vertical"><p>Private use</p></th>
      <th class="vertical"><p>Hold liable</p></th>
      <th class="vertical"><p>Sublicensing</p></th>
    </tr>
    <tr>
      <th colspan=14 style="text-align: center"><a href="/software/imagej">ImageJ</a></th>
    </tr>
    <tr>
      <td><img src="/media/icons/imagej.png" width="48"></td>
      <th><a href="/software/imagej">ImageJ</a></th>
      <td><a href="https://imagej.net/ij/disclaimer.html">Disclaimer</a></td>
      <td>
        <a href="/licensing/public-domain">Public</a><br>
        <a href="/licensing/public-domain">Domain</a><sup>†</sup>
      </td>
      <td style="text-align: center">❌</td>
      <td>❌</td>
      <td>❌</td>
      <td>✅</td>
      <td>✅</td>
      <td>✅</td>
      <td>-</td>
      <td>✅</td>
      <td>❌</td>
      <td>✅</td>
    </tr>
    <tr>
      <th colspan=14 style="text-align: center"><a href="/develop/architecture">ImageJ2 software stack</a></th>
    </tr>
    <tr>
      <td><img src="/media/icons/scijava.png" width="48"></td>
      <th><a href="/libs/scijava">SciJava</a></th>
      <td><a href="https://github.com/scijava/scijava-common/blob/master/LICENSE.txt">License</a></td>
      <td rowspan="4"><a href="/licensing/bsd">BSD-2</a></td>
      <td rowspan="4">❌</td>
      <td rowspan="4">✅</td>
      <td rowspan="4">❌</td>
      <td rowspan="4">✅</td>
      <td rowspan="4">✅</td>
      <td rowspan="4">✅</td>
      <td rowspan="4">-</td>
      <td rowspan="4">✅</td>
      <td rowspan="4">❌</td>
      <td rowspan="4">-</td>
    </tr>
    <tr>
      <td><img src="/media/icons/imglib2.png" width="48"></td>
      <th><a href="/libs/imglib2">ImgLib2</a></th>
      <td><a href="https://github.com/imglib/imglib2/blob/master/LICENSE.txt">License</a></td>
    </tr>
    <tr>
      <td><img src="/media/icons/imagej2.png" width="48"></td>
      <th><a href="/software/imagej2">ImageJ2</a></th>
      <td><a href="https://github.com/imagej/imagej/blob/master/LICENSE.txt">License</a></td>
    </tr>
    <tr>
      <td><img src="/media/icons/scifio.png" width="48"></td>
      <th><a href="/libs/scifio">SCIFIO</a></th>
      <td><a href="https://github.com/scifio/scifio/blob/master/LICENSE.txt">License</a></td>
    </tr>
    <tr></tr>
    <tr>
      <th colspan="14" style="text-align: center"><a href="/software/fiji">Fiji projects</a></th>
    </tr>
    <tr>
      <td rowspan="3"><img src="/media/icons/fiji.png" width="48"></td>
      <th><a href="/software/fiji">Fiji</a></th>
      <td><a href="https://github.com/fiji/fiji/blob/master/LICENSES">Licenses</a></td>
      <td rowspan="2"><a href="/licensing/gpl">GPL</a></td>
      <td rowspan="2">✅</td>
      <td rowspan="2">✅</td>
      <td rowspan="2">✅</td>
      <td rowspan="2">✅</td>
      <td rowspan="2">✅</td>
      <td rowspan="2">✅</td>
      <td rowspan="2">✅</td>
      <td rowspan="2">✅</td>
      <td rowspan="2">❌</td>
      <td rowspan="2">❌</td>
    </tr>
    <tr>
      <th><a href="/plugins/trakem2">TrakEM2</a></th>
      <td><a href="https://github.com/trakem2/trakem2/blob/master/README">Readme</a></td>
    </tr>
    <tr>
      <th><a href="/plugins/bdv">BigDataViewer</a></th>
      <td><a href="https://github.com/bigdataviewer/bigdataviewer-core/blob/master/LICENSE.txt">License</a></td>
      <td><a href="/licensing/bsd">BSD-2</a><sup>‡</sup></td>
      <td>❌</td>
      <td>✅</td>
      <td>❌</td>
      <td>✅</td>
      <td>✅</td>
      <td>✅</td>
      <td>-</td>
      <td>✅</td>
      <td>❌</td>
      <td>-</td>
    </tr>
    <tr>
      <th colspan="14" style="text-align: center"><a href="/libs/scijava">SciJava consortium</a></th>
    </tr>
    <tr>
      <td><img src="/media/icons/cellprofiler.png" width="48"></td>
      <th><a href="/software/cellprofiler">CellProfiler</a></th>
      <td><a href="https://github.com/CellProfiler/CellProfiler/blob/master/LICENSE">License</a></td>
      <td><a href="/licensing/bsd">BSD-3</a></td>
      <td rowspan="1">❌</td>
      <td rowspan="1">✅</td>
      <td rowspan="1">❌</td>
      <td rowspan="1">✅</td>
      <td rowspan="1">✅</td>
      <td rowspan="1">✅</td>
      <td>-</td>
      <td rowspan="1">✅</td>
      <td rowspan="1">❌</td>
      <td>-</td>
    </tr>
    <tr>
      <td><img src="/media/icons/bio-formats.png" width="48"></td>
      <th><a href="/formats/bio-formats">Bio-Formats</a></th>
      <td>
        <a href="https://github.com/openmicroscopy/bioformats/blob/develop/LICENSE.txt">License</a><br>
        <a href="http://openmicroscopy.org/site/about/licensing-attribution">Info</a>
      </td>
      <td rowspan="3"><a href="/licensing/gpl">GPL</a></td>
      <td rowspan="3">✅</td>
      <td rowspan="3">✅</td>
      <td rowspan="3">✅</td>
      <td rowspan="3">✅</td>
      <td rowspan="3">✅</td>
      <td rowspan="3">✅</td>
      <td rowspan="3">✅</td>
      <td rowspan="3">✅</td>
      <td rowspan="3">❌</td>
      <td rowspan="3">❌</td>
    </tr>
    <tr>
      <td><img src="/media/icons/omero.png" width="48"></td>
      <th><a href="/software/omero">OMERO</a></th>
      <td>
        <a href="https://github.com/openmicroscopy/openmicroscopy/blob/develop/LICENSE.txt">License</a><br>
        <a href="http://openmicroscopy.org/site/about/licensing-attribution">Info</a>
      </td>
    </tr>
    <tr>
      <td><img src="/media/icons/knime.svg" width="48"></td>
      <th><a href="/software/knime">KNIME</a></th>
      <td><a href="http://www.knime.org/downloads/full-license">License</a></td>
    </tr>
  </tbody>
</table>
{:/}

<span>\*</span> See [choosealicense.com](http://choosealicense.com/) for details.\\
<sup>†</sup> See note below for details.\\
<sup>‡</sup> BigDataViewer libraries are licensed BSD-2; the BigDataViewer plugin for Fiji
  <a href="https://github.com/bigdataviewer/bigdataviewer_fiji/blob/master/LICENSE.txt">is GPLv3</a>.

## Exceptions

Since each project consists of many components, some may be licensed differently. You can always find the license of each project in a `LICENSE.txt` or similar file of the relevant repository on [GitHub](/develop/github). That said, in general, the table below is accurate with very few exceptions. When there *is* an exception, it is often licensed more permissively than the rest of the project—for example, the core of [Bio-Formats](/formats/bio-formats) is licensed under [BSD-2](/licensing/bsd) ([1](https://github.com/openmicroscopy/bioformats/blob/develop/components/formats-bsd/LICENSE.txt)), and the [ImageJ2](/software/imagej2) and [SCIFIO](/libs/scifio) tutorials are licensed under [CC0](/licensing/public-domain) ([1](https://github.com/imagej/tutorials/blob/master/README.md), [2](https://github.com/scifio/scifio-tutorials/blob/master/README.md)), waiving all copyright interest as allowed by law.

## A note about ImageJ

The original [ImageJ](/software/imagej) project is developed at the National Institutes of Health, a United States government organization. Hence, pursuant to [U.S. copyright law Title 17, Section 105](http://www.copyright.gov/title17/92chap1.html#105), no copyright applies. However, that waiver of copyright applies only to U.S. law, and does not apply to other countries. Furthermore, the ImageJ project includes substantial effort and code from individuals who are not U.S. government employees, making the legal status of ImageJ as a whole unclear. For further reading, see the {% include wikipedia title='Copyright status of work by the U.S. government' text='Wikipedia article "Copyright status of work by the U.S. government"'%}.

## Developers: How to use this page

If you will be creating and/or consuming open source code, you should familiarize yourself with the options for [managing copyright information](http://softwarefreedom.org/resources/2012/ManagingCopyrightInformation.html). There are numerous tools for assisting in license management; in SciJava projects, for example, the [license-maven-plugin](https://www.mojohaus.org/license-maven-plugin/) is used to maintain file-scope copyright notices.

### Linking to these libraries

If you are writing code (open source or not) that will use one or more of these libraries, you should first familiarize yourself with the type of license(s) used by your library(ies) of interest to determine the compatibility with the licensing of your own project. Then follow the corresponding *License text* column entry links to the actual document (if any) that needs to be distributed with your code.

### Applying these licenses

If you are writing open source code and aren't sure how to license it, you can use this page to get a feel for how other software layers are licensed, and thus what might be appropriate for your project. You can follow [general tutorials](http://opensource.org/faq#apply-license) on applying open source licenses, or use the fantastic [choosealicense.com](http://choosealicense.com/licenses/) to guide your choice (which also includes *How to apply this license* instructions for each license).
