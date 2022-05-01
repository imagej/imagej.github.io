---
mediawiki: Visualization
title: Visualization
section: Learn:Scientific Imaging
nav-links: true
---

{% include wikipedia title='Scientific visualization' text='Scientific visualization'%} is a set of techniques for graphically illustrating scientific data, enabling scientists to better understand, illustrate, and glean insight from their data.

## Getting Started with Simple Visualization Options in ImageJ

### Pseudocolor Image Look-Up Tables (LUTs)

A [pseudocolor image](/imaging/color-image-processing#pseudo-color) is a single channel gray image (8, 16 or 32-bit) that has color assigned to it via a lookup table, i.e. a {% include wikipedia title='Lookup table#Lookup_tables_in_image_processing' text='LUT' %}. A LUT is a predefined table of gray values with matching red, green, and blue values so that shadows of gray are displayed as colorized pixels. Thus, differences in color in the pseudo-colored image reflect differences in intensity of the object rather than differences in color of the specimen that has been imaged.

The [LUT Menu](https://imagej.nih.gov/ij/docs/guide/146-19.html#sub:LUTMenu) of ImageJ contains a large collection of lookup tables that can be applied to a pseudocolor image.

{% include notice icon='note' content="In the ImageJ user interface, LUTs are always 8-bit. When working with an image of higher bit depth, its intensity values are binned into 256 levels between minimum and maximum (see section Brightness/Contrast), and the LUT is applied onto these binned levels." %}

More information on this topic can be found on the [Color Image Processing](/imaging/color-image-processing) page.

Fluorescence images are usually acquired without color information (i.e. by monochrome cameras or with photomultipliers): each channel contains just intensity values. To display a multi-channel fluorescence image in composite mode (i.e. an overlay of all channels), each channel can be assigned a **monochrome false-color LUT**, e.g. 'Red', 'Green', 'Blue', 'Cyan', 'Magenta', 'Yellow', etc.

When analyzing quantitative data in an image, a false-color LUT (in this case also referred to as **color map**) can increase the visibility of low-contrasted features in the image and help the human eye to compare different images.

Here's a list of recommended options to choose a LUT:

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <th>LUT Name</th>
      <th>Properties</th>
      <th>Common Usage</th>
      <th>Histogram</th>
    </tr>
    <tr>
      <th>mpl-viridis</th>
      <td>
        <ul>
          <li>
            <em>Perceptually uniform</em><a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a>
          </li>
          <li>Dark-to-Bright mapping</li>
        </ul>
      </td>
      <td>Quantitative display of positive values on a continuous scale</td>
      <td>
        <figure>
          <img src="/media/imaging/m51-histogram-mplviridis.png" title="Histogram of the M51 Galaxy sample image with the mpl-viridis LUT applied" width="300" alt="Histogram of the M51 Galaxy sample image with the mpl-viridis LUT applied">
          <figcaption aria-hidden="true">
            Histogram of the M51 Galaxy sample image with the <em>mpl-viridis</em> LUT applied
          </figcaption>
        </figure>
      </td>
    </tr>
    <tr>
      <th>HiLo</th>
      <td>
        <ul>
          <li>Minimum of display range is blue</li>
          <li>Maximum of display range is red</li>
          <li>Normal gray-scale LUT for all other values</li>
        </ul>
      </td>
      <td>Assessment of over-/under-exposure in an image</td>
      <td>
        <figure>
          <img src="/media/imaging/m51-histogram-hilo.png" title="Histogram of the M51 Galaxy sample image with the displayed range adjusted and the HiLo LUT applied" width="300" alt="Histogram of the M51 Galaxy sample image with the displayed range adjusted and the HiLo LUT applied">
          <figcaption aria-hidden="true">
            Histogram of the M51 Galaxy sample image with the displayed range adjusted and the <em>HiLo</em> LUT applied
          </figcaption>
        </figure>
      </td>
    </tr>
    <tr>
      <th>phase</th>
      <td>
        <ul>
          <li><em>Diverging</em> color map</li>
          <li>Bright center, dark min and max</li>
        </ul>
      </td>
      <td></td>
      <td>
        <figure>
          <img src="/media/imaging/randomized-image-histogram-phase.png" title="Histogram of a randomized calibrated 8-bit image with the phase LUT applied" width="300" alt="Histogram of a randomized calibrated 8-bit image with the phase LUT applied">
          <figcaption aria-hidden="true">
            Histogram of a randomized calibrated 8-bit image with the <em>phase</em> LUT applied
          </figcaption>
        </figure>
      </td>
    </tr>
  </tbody>
</table>
{:/}
<section class="footnotes" role="doc-endnotes"><hr /><ol><li id="fn1" role="doc-endnote"><a href="https://bids.github.io/colormap/">https://bids.github.io/colormap/</a><a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></li></ol></section>

For further reading about color maps, see [1] and [2]

### Adjusting your Image in ImageJ

The [Adjust submenu](https://imagej.nih.gov/ij/docs/guide/146-28.html#toc-Subsection-28.2) contains commands that adjust [Brightness/Contrast](https://imagej.nih.gov/ij/docs/guide/146-28.html#sub:Brightness/Contrast...%5BC%5D), [Threshold](https://imagej.nih.gov/ij/docs/guide/146-28.html#sub:Threshold...%5BT%5D) levels, and image [Size](https://imagej.nih.gov/ij/docs/guide/146-28.html#sub:Size...).

### Visualization of Volumetric Image Data

Here we summarize some of the 3D visualization plugins in ImageJ.

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <th>Plugin Name</th>
      <th>Short Description</th>
      <th>Highlights</th>
      <th>Plugin Snapshot</th>
    </tr>
    <tr>
      <td>
        <a href="/plugins/3d-viewer">3D Viewer</a>
      </td>
      <td>
        A tool for hardware-accelerated visualization possibilities for image stacks, using the <a href="/libs/java-3d">Java 3D</a> library.
      </td>
      <td>
        <ul>
          <li>Stacks can be displayed as texture-based volume renderings, surfaces, or orthoslices</li>
          <li>Macro-recordable functions</li>
          <li>Adjust the transfer functions, edit volumes, point lists, landmark-based registration, transformations, 3D Content in PDFs</li>
        </ul>
      </td>
      <td>
        <figure>
          <img src="/media/3d-viewer-overview.png" title="3D_Viewer_overview.png" alt="3D_Viewer_overview.png">
          <figcaption aria-hidden="true">
            3D_Viewer_overview.png
          </figcaption>
        </figure>
      </td>
    </tr>
    <tr>
      <td>
        <a href="/plugins/clearvolume">ClearVolume</a>
      </td>
      <td>A tool for live rendering volumetric multi-channel data.</td>
      <td>
        <ul>
          <li>Create instant multiview and multicolor renderings</li>
          <li>Instant rewind and replay of time-lapse recordings</li>
          <li>Provides real-time GPU-based image processing capabilities, such as image sharpness estimation and sample drift tracking</li>
          <li>Enables live streaming of 3D data in real time over the internet</li>
        </ul>
      </td>
      <td><img src="/media/clearvolumeinfiji.png" width="500"></td>
    </tr>
    <tr>
      <td>
        <a href="/plugins/volume-viewer">Volume Viewer</a>
      </td>
      <td>A tool for 3D reslicing and threshold-enabled 3D visualization.</td>
      <td>
        <ul>
          <li>Non-hardware accelerated volume rendering in different modalities.</li>
          <li>
            <a href="/plugins/volume-viewer.html">Documentation</a>
          </li>
        </ul>
      </td>
      <td><img src="/media/imaging/volviewer.png" width="500"></td>
    </tr>
    <tr>
      <td>
        <a href="/plugins/sciview">SciView</a>
      </td>
      <td>A tool for 3D visualization capabilities for images and meshes.</td>
      <td>
        <ul>
          <li>Uses the <a href="https://github.com/ClearVolume/scenery">Scenery</a> and <a href="/plugins/clearvolume">ClearVolume</a> infrastructure
          </li>
          <li>Integrates <a href="/software/imagej2">ImageJ2</a> functionality, including <a href="/libs/imagej-ops">ImageJ Ops</a>
          </li>
          <li>Aims to serve as a modern replacement to <a href="/plugins/3d-viewer">3D Viewer</a>
          </li>
        </ul>
      </td>
      <td><img src="/media/imaging/sciview-gameoflife.gif" width="500"></td>
    </tr>
  </tbody>
</table>
{:/}

## Making Plots in ImageJ

### The Basics: ImageJ v1.x Plot Tools

1.  [Plot Profile](https://imagej.nih.gov/ij/docs/guide/146-30.html#sub:Plot-Profile-%5Bk%5D)
2.  [Plot Z-axis Profile](https://imagej.nih.gov/ij/docs/guide/146-28.html#sub:Plot-Z-axis-Profile...)
3.  [Surface Plot](https://imagej.nih.gov/ij/docs/guide/146-30.html#sub:Surface-Plot...)

### Available Plugins for Making Plots in ImageJ

1.  [Quiver Plot](/plugins/quiver-plot)

### Plotting tools available via scripting...

1.  JFreeChart (used by [Directionality](/plugins/directionality))
2.  [Matplotlib](http://matplotlib.org/)

## Making Figures in ImageJ

### Available Plugins for Making Figures in ImageJ

1.  [Magic Montage](http://imagejdocu.list.lu/doku.php?id=video:utilities:creating_montages_with_magic_montage)
2.  [FigureJ](http://imagejdocu.list.lu/doku.php?id=plugin:utilities:figurej:start)
3.  [ScientiFig](https://grr.gred-clermont.fr/labmirouse/software/)
4.  [Figure Maker](https://github.com/quantixed/imagej-macros#figure-maker)

## Recommended ImageJ Plugins for 'Big Data' Visualization

Here we summarize some of the 'big data' visualization plugins in ImageJ.

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <th>Plugin Name</th>
      <th>Short Description</th>
      <th>Highlights</th>
      <th>Plugin Snapshot</th>
    </tr>
    <tr>
      <td>
        <a href="/plugins/bdv">BigDataViewer</a>
      </td>
      <td>A tool for interactive browsing of arbitrarily large image datasets.</td>
      <td>
        <ul>
          <li>Arbitrary slicing, zooming, etc.</li>
          <li>For multi-angle, multi-channel, time-series, etc.</li>
          <li>Adding overlays, annotations, etc.</li>
          <li>Reusable software components</li>
          <li>Used as data backend and/or visualization frontend by <a href="/plugins/multiview-reconstruction">MultiView Reconstruction</a>, <a href="/plugins/mamut">MaMuT</a>, <a href="/plugins/bigwarp">BigWarp</a>, etc.
          </li>
        </ul>
      </td>
      <td><img src="/media/bdv.png" width="500"></td>
    </tr>
    <tr>
      <td>
        <a href="/plugins/multiview-reconstruction">MultiView Reconstruction</a>
      </td>
      <td>A tool for registration, fusion, deconvolution, and visualization of multiview microscopy images.</td>
      <td>
        <ul>
          <li>Designed for lightsheet fluorescence microscopy</li>
          <li>Applicable to any form of three or higher dimensional imaging modalities</li>
          <li>Interactive viewing and annotation of the data</li>
        </ul>
      </td>
      <td><img src="/media/imaging/spim-application.png" width="500"></td>
    </tr>
  </tbody>
</table>
{:/}

## Interactive Analysis Plugins based on 'Big Data' Visualization Tools

Here we summarize the more advanced analysis plugins in ImageJ using the above 'big data' visualization tools.

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <th>Plugin Name</th>
      <th>Short Description</th>
      <th>More Details...</th>
      <th>Plugin Snapshot</th>
    </tr>
    <tr>
      <td>
        <a href="/plugins/mamut">MaMuT</a> (<strong>Ma</strong>ssive <strong>Mu</strong>lti-view <strong>T</strong>racker)
      </td>
      <td>A tool for manual and semi-automatic tracking in multiple views.</td>
      <td>
        <ul>
          <li>Allows browsing, annotating, and curating annotations for large image data</li>
          <li>Combines <a href="/plugins/bdv">BigDataViewer</a> and <a href="/plugins/trackmate">TrackMate</a>
          </li>
          <li>Ships <a href="/plugins/trackmate/trackscheme">TrackScheme</a>, the lineage browser taken from <a href="/plugins/trackmate">TrackMate</a>
          </li>
        </ul>
      </td>
      <td><img src="/media/mamut.png" width="500"></td>
    </tr>
    <tr>
      <td>
        <a href="/plugins/bigwarp">BigWarp</a>
      </td>
      <td>A tool for manual, interactive, landmark-based deformable image alignment.</td>
      <td>
        <ul>
          <li>Uses <a href="/plugins/bdv">BigDataViewer</a> for visualization and navigation
          </li>
          <li>Uses a {% include wikipedia title='Thin plate spline' text='Thin Plate Spline'%} implemented {% include github org='saalfeldlab' repo='bigwarp' label='in Java' %} to build a deformation from point correspondences</li>
          <li>Enables landmark pair placement and displays the effects of the warp on-the-fly</li>
        </ul>
      </td>
      <td><img src="/media/bigwarp.png" width="400"></td>
    </tr>
  </tbody>
</table>
{:/}

[1] http://peterkovesi.com/projects/colourmaps/

[2] http://www.kennethmoreland.com/color-maps/
