---
mediawiki: SIOX:_Simple_Interactive_Object_Extraction
title: "SIOX: Simple Interactive Object Extraction"
project: /software/fiji
categories: [Uncategorized]
artifact: sc.fiji:Siox_Segmentation
---

 

<div style="float: left">

{% include thumbnail src='/media/plugins/embryos775x581.png' title='Embryos original sample'%}

</div>
<div style="float:
 left">

{% include thumbnail src='/media/plugins/siox-result-embryos775x581.png' title='SIOX segmentation result'%}

</div>

{% include clear content='left' %}

This is a Fiji plugin based on the [SIOX project](http://www.siox.org) **to segment color images**. [SIOX](/plugins/siox) stands for *Simple Interactive Object Extraction*, a method for **extracting foreground from still images** with very little user interaction. [SIOX](/plugins/siox) is fast, noise robust and can therefore also be used for the segmentation of videos. It avoids many of the drawbacks of graph-based segmentation methods but performs about equally well on different benchmarks. [SIOX](/plugins/siox) is open and free (Apache License) and the authors have intentionally not patented any part of the technology. As a result, it has been integrated into several open-source image manipulation programs over the past years. [SIOX](/plugins/siox) is the underlying algorithm of the foreground extraction tool in the GNU Image Manipulation Program ([GIMP](http://www.gimp.org/)) and is part of the tracer tool in [Inkscape](http://www.inkscape.org/). [SIOX](/plugins/siox) originates from [E-Chalk](http://www.echalk.de/) where an instructor standing in front of an electronic chalkboard is segmented. Variants of [SIOX](/plugins/siox) are being used for robotic vision and for improving 3D time-of-flight camera segmentation.

## Quick Start

**Premises:**  
In order to call the plugin, you need to have at least one **RGB color image** open.

After clicking on {% include bc path='Plugins | Segmentation | SIOX: Simple Interactive Object Extraction'%}, the image will be embedded into the plugin GUI.

**Step 1:** Initial Segmentation.  
Paint the regions of interest (ROIs) corresponding to the foreground and background. Select any of the ROI tools and mark the areas you consider foreground and background. To segment multiple objects, select "Allow multiple foreground components"

<!-- -->

**Step 2:** Detail Refinement Brush.  
Select new ROIs to be added or subtracted from the current segmentation. Press "Refine" to add/subtract those areas based on the previous result.

<!-- -->

**Step 3:** Reset or Create mask.  
Click the "Reset" button to restart the process or click on the "Create mask" button to create a binary image. Please, note that the binary image polarity will follow the option set in {% include bc path='Process | Binary | Options'%}.

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td>
        <p>style="vertical-align:top"|{% include thumbnail src='/media/plugins/screenshot-siox-segmentation.png' title='SIOX segmentation Graphical User Interface applied to Leaf sample'%}</p>
      </td>
      <td>
        <p>style="vertical-align:top"|{% include thumbnail src='/media/plugins/siox-mask.png' title='Resulting mask of Leaf sample after SIOX segmentation'%}</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

## User Manual

[SIOX](/plugins/siox) is a plugin designed to segment 2D color images. If the image is not RGB color, it can be converted to RGB using the command {% include bc path='Image | Type | RGB Color'%}. However, the [SIOX](/plugins/siox) algorithm makes uses color information, so it is expected to work better on real RGB images.

When calling the plugin, the image will be embedded into the [SIOX](/plugins/siox) graphical user interface (GUI). This GUI has 3 section (panels): Initial Segmentation, Detail Refinement Brush and the Mask/Reset buttons.

### Initial Segmentation

{% include thumbnail src='/media/plugins/siox-initial-segmentation.png' title='SIOX initial segmentation panel'%} This is the **first step** of the procedure where one defines the ROIs that correspond to typical areas of foreground or background.

**Defining foreground and background**  

<!-- -->

  
The radio buttons *Foreground* and *Background* switch between the two ROI types. When the foreground ROIs are being defined, the background ROIs are shown in translucent **red**. Similarly, when defining the background ROIs, the foreground ROIs are shown in translucent **green**.

<!-- -->

  
The ROIs can be defined with any of the Selection Tools:

<!-- -->

  
![](/media/plugins/fiji-selection-tools.png)

<!-- -->

  
**TIP**: Multiple ROIs can be selected with any of the selection tools by pressing the SHIFT key and clicking on different parts of the image.

<!-- -->

**Multiple objects**  

<!-- -->

  
For segmenting **multiple objects**, check *Allow multiple foreground components*. This option tells [SIOX](/plugins/siox) to look for several objects in the image. If you introduce multiple foreground ROIs, this option will be then assumed.

<!-- -->

**Smoothing**  

<!-- -->

  
The *Smoothing* slider defines the sharpness of the resulting contours. For example, when segmenting the default sample "Leaf (36K)", reducing the smoothing provides more accurate borders.

<!-- -->

**Segmentation**  

{% include thumbnail src='/media/plugins/siox-segmentation-gui-step1.png' title='Example of SIOX result after initial segmentation'%}

  
In order to proceed with the initial segmentation, click on *Segment*.

<!-- -->

  
Remember that [SIOX](/plugins/siox) needs at least one foreground component (ROI) to produce the segmentation, the background ROI is optional.

<!-- -->

  
After a few seconds (depending on the image size), the result will be shown (darkened background and foreground area(s) in the original colors).

<!-- -->

  
Following this, the initial segmentation panel is disabled. If the results are not satisfactory, press *Reset* to restart the process. Otherwise, continue to the next refinement step.

### Detail Refinement Brush

{% include thumbnail src='/media/plugins/siox-detail-refinement-brush.png' title='SIOX detail refinement brush panel'%} This is the **second step** in the [SIOX](/plugins/siox) segmentation process.

At this point, the method can be called again to refine the results obtained so far to subtract or add new areas to the background or foreground components **as many times needed**.

The *Add* mode only modifies pixels formerly classified as background, while the *Subtract* mode only modifies those formerly classified as foreground.

**Note**: this step is optional. If you are already satisfied with the result, proceed to create the binary mask.

Clicking on *subtract* or *add* selects the ROIs to be added or subtracted. The **sliders represent the threshold for the add and subtract refinement**, deciding at which confidence level to stop at. Increasing the subtraction slider relaxes the threshold value to set an area as background, while decreasing the addition slider relaxes the threshold value to set an area as foreground.

Finally, by clicking on *Refine*, the segmentation is recalculated for the selected areas and the result will be displayed as before (darkened background and full color foreground). Repeat this step until you are completely satisfied.

### Reset or Create mask

{% include thumbnail src='/media/plugins/siox-reset-create-mask.png' title='SIOX Reset/Create mask panel'%} This panel is enabled during any of the other segmentation steps.

**Reset**  

<!-- -->

  
Resets the image including the internal status of the confidence matrix (foreground, background and refinement areas). The **initial ROIs are reloaded** so they can be reused.

<!-- -->

**Create mask**  

<!-- -->

  
Creates a binary (0-255) image based on the current state of the segmentation process. The background color (black or white) is defined in {% include bc path='Process | Binary | Options...'%} This button can be pressed during any of the previous steps.

### Save segmentator

You can save the segmentation information into a file by clicking on the "Save segmentator" button. This can be used later to a different image or stack of images by clicking on {% include bc path='Plugins | Segmentation | Apply SIOX segmentator'%} (see next section).

### Apply SIOX segmentator

You can apply a previously saved SIOX segmentator to any open image or set of images (stack).

**Step 1**: Click on the image or stack to segment.

**Step 2**: Click on {% include bc path='Plugins | Segmentation | Apply SIOX segmentator'%}, and the following dialog will pop up:

![ left \| thumb \| 600 px \| Apply SIOX segmentator input dialog](/media/plugins/screenshot-load-siox-segmentator.png)

**Step 3**: Select the siox segmentator file (or just drag and drop it) and click "OK".

The segmentator will be applied to the selected image or stack and the result will pop up.

![ left \| thumb \| 1014px \| Results of applying the previously calculated SIOX segmentator to a stack of transformed versions of the Leaf sample](/media/plugins/combined-siox-stacks.gif)

**Note**: when applying a saved segmentator there is no information about the size of the expected foreground components so the largest component will be used as reference. The multiple component option will be consistent with what it was used during the segmentator calculation.

## API documentation

The latest documentation of the package can be found here:

-   For the SIOX plugin: [https://fiji.sc/javadoc/siox/package-summary.html](https://fiji.sc/javadoc/siox/package-summary.html)
-   For the SIOX library: [https://fiji.sc/javadoc/org/siox/package-summary.html](https://fiji.sc/javadoc/org/siox/package-summary.html)

## References

Most Comprehensive Work:

-   G. Friedland: Adaptive Audio and Video Processing for Electronic Chalkboard Lectures, [PhD thesis](http://www.diss.fu-berlin.de/2006/514/indexe.html), Department of Computer Science, Freie Universitaet Berlin, October 2006.

Still Image Approach:

-   G. Friedland, K. Jantz, T. Lenz, F. Wiesel, R. Rojas: Object Cut and Paste in Images and Videos, International Journal of Semantic Computing Vol 1, No 2, pp. 221-247, World Scientific, USA, June 2007.
-   G. Friedland, K. Jantz, L. Knipping, R. Rojas: Image Segmentation by Uniform Color Clustering -- Approach and Benchmark Results, [Technical Report B-05-07](http://www.siox.org/downloads/tr-b-05-07.pdf), Department of Computer Science, Freie Universitaet Berlin, June 2005 (PDF, 18MB).
-   G. Friedland, K. Jantz, R. Rojas: SIOX: Simple Interactive Object Extraction in Still Images, Proceedings of the IEEE International Symposium on Multimedia (ISM2005), pp. 253-259, Irvine (California), December, 2005. [Download PDF](http://csdl.computer.org/dl/proceedings/ism/2005/2489/00/24890253.pdf) from IEEE Computer Society Digital Library.
-   G. Friedland, K. Jantz, T. Lenz, R. Rojas: Extending the SIOX Algorithm: Alternative Clustering Methods, Sub-pixel Accurate Object Extraction from Still Images, and Generic Video Segmentation, [Technical Report B-06-06](http://www.siox.org/downloads/tr-b-06-06.pdf), Department of Computer Science, Freie Universitaet Berlin, January 2006 (PDF, 10MB).
-   G. Friedland, K. Jantz, T. Lenz, F. Wiesel, R. Rojas: A Practical Approach to Boundary-Accurate Multi-Object Extraction from Still Images and Videos, to appear in Proceedings of the IEEE International Symposium on Multimedia (ISM2006), San Diego (California), December, 2006.

## ImageJ version

Thanks to {% include person id='rasband' %}, there is an [ImageJ](https://imagej.nih.gov/ij/plugins/siox/index.html) version of this plugin without Fiji dependencies:

[https://imagej.nih.gov/ij/plugins/siox/index.html](https://imagej.nih.gov/ij/plugins/siox/index.html)

## Licenses

The [SIOX Java library](https://fiji.sc/cgi-bin/gitweb.cgi?p=fiji.git;a=tree;f=src-plugins/Siox_Segmentation/org;h=902e7e0379b36f7f03b512552fb899861d866fa9;hb=d451306e290fb55a31052cbfc5426eaa70df17d6) developed by [Gerald Friedland](http://www.gerald-friedland.org/), [Kristian Jantz](http://www.inf.fu-berlin.de/~jantz) and [Lars Knipping](http://www.inf.fu-berlin.de/~knipping) is licensed under the **Apache License**, Version 2.0 (the "/licensing"): [http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0). Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

The Fiji plugin GUI, developed by {% include person id='iarganda' %}, [Stephan Saalfeld](http://fly.mpi-cbg.de/~saalfeld/) and {% include person id='dscho' %} is free software; you can redistribute it and/or modify it under the terms of the **GNU General Public License** as published by the Free Software Foundation ([http://www.gnu.org/licenses/gpl.txt](http://www.gnu.org/licenses/gpl.txt)).

## See also

-   Original SIOX project: [http://www.siox.org/](http://www.siox.org/)
-   SIOX project FAQs: [http://www.siox.org/faq.html](http://www.siox.org/faq.html)

 
