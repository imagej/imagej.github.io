---
title: 2014-10-01 - ImageJ Ops Hackathon
---

{% include img align="right" src="/media/news/2014-ops-hackathon.png" caption="A graph of progress during the hackathon." width="304px" %}

From Sunday, September 14, 2014 through Friday, September 19, 2014, LOCI in Madison hosted Christian Dietz and Brian Northan, two developers of [ImageJ Ops](/libs/imagej-ops), for an exciting hackathon. [Christian Dietz](http://www.informatik.uni-konstanz.de/en/berthold/members/christian-dietz/) is a PhD student in computer science at the University of Konstanz and the lead developer of the [KNIME Image Processing](http://knime.imagej.net/) project; [Brian Northan](https://www.linkedin.com/pub/brian-northan/6/860/3a7) is a freelance contract research and development engineer specializing in scientific image and signal processing.

## Overview

ImageJ Ops is an extensible Java framework for algorithms, particularly image processing algorithms. Ops seeks to be a unifying library for scientific image processing. See the [Motivation](https://github.com/imagej/imagej-ops/wiki/Motivation) page on the Ops wiki for details.

[KNIME](/software/knime) is an open source data analytics, reporting and integration platform, which integrates various components for machine learning and data mining through its modular data pipelining concept. The [<u>KN</u>IME <u>I</u>mage <u>P</u>rocessing](http://knime.imagej.net/) extension, KNIP, provides nodes for working with images, and is built on the ImageJ Ops library. Ops makes it possible to execute the image processing algorithm in many contexts, including from within [ImageJ](/software/imagej) itself, from [OMERO](/software/omero), [KNIME](/software/knime), [CellProfiler](/software/cellprofiler) and beyond.

## Accomplishments

This hackathon focused on the [ImageJ Ops](/libs/imagej-ops) library, adding support for key image processing operations, as well as improving the framework itself. Achievements from the hackathon include:

-   Vastly improved thresholding code ([\#52](https://github.com/imagej/imagej-ops/pull/52))
-   Improvements to the code generation mechanism ([\#42](https://github.com/imagej/imagej-ops/pull/42))
-   Autogeneration of base op interfaces ([e1e2d18f](https://github.com/imagej/imagej-ops/commit/e1e2d18fd1e96968c4a8aa29d1f67c46222167b6))
-   Several miscellaneous design improvements ([\#36](https://github.com/imagej/imagej-ops/pull/36), [6cb8b083](https://github.com/imagej/imagej-ops/commit/6cb8b0831f9f3fb6d27bfcf2ee509ca20688b5c4))
-   See the [SCM history](https://github.com/imagej/imagej-ops/compare/master@%7B13-Sep-2014%7D...master@%7B20-Sep-2014%7D) for full details.

All thresholding algorithms from [ImageJ 1.x](/software/imagej1) have been ported to Ops. Available thresholding methods now include:

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td style="vertical-align: top">
        <ul>
          <li>huang</li>
          <li>ij1</li>
          <li>intermodes</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>isodata</li>
          <li>li</li>
          <li>maxEntropy</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>maxlikelihood</li>
          <li>mean</li>
          <li>minerror</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>minimum</li>
          <li>moments</li>
          <li>otsu</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>percentile</li>
          <li>renyientropy</li>
          <li>shanbhag</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>triangle</li>
          <li>yen</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>
{:/}

## Progress and future directions

We also made great progress on several new lines of development:

-   Type conversion ([\#47](https://github.com/imagej/imagej-ops/pull/47))
-   Kernels ([\#48](https://github.com/imagej/imagej-ops/pull/48))
-   Projection ([\#51](https://github.com/imagej/imagej-ops/pull/51))
-   Conditions ([\#73](https://github.com/imagej/imagej-ops/pull/73))
-   Features and descriptors ([feature-service branch](https://github.com/imagej/imagej-ops/compare/feature-service))

## Future directions

The Ops development plan and timeline is now [codified on GitHub](https://github.com/imagej/imagej-ops/milestones). Major milestones include:

1.  A [near-term release](https://github.com/imagej/imagej-ops/milestones/0.10.0) later this fall: high-priority design issues, features and ops.
2.  An [intermediate release](https://github.com/imagej/imagej-ops/milestones/0.20.0) before next spring: work to complete before coming out of incubation with 1.0.0, but less urgent than near-term items.
3.  A [stable 1.0.0 release](https://github.com/imagej/imagej-ops/milestones/1.0.0) before the end of 2015: first release with a goal of future backwards compatibility according to [SemVer](http://semver.org/).

Please direct questions about Ops to the [ImageJ forum](http://forum.imagej.net/).

Thanks to everyone involved for all the hard work, patience and enthusiasm!

   
