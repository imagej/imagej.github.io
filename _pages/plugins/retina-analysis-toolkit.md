---
mediawiki: RETINA_Analysis_Toolkit
title: RETINA Analysis Toolkit
doi: 10.1167/iovs.15-17599
categories: [Uncategorized]
---

{% include info-box software='ImageJ' name='RETINA Analysis Toolkit' author=' [**Daniel E. Maidana**](https://www.researchgate.net/profile/Daniel_Maidana2)  
[**Demetrios G. Vavvas**](https://www.masseyeandear.org/research/investigators/v/vavvas-demetrios-g)' maintainer='**Daniel E. Maidana**  
Angiogenesis Laboratory  
Massachusetts Eye and Ear Infirmary  
Harvard Medical School  
Email: [Daniel Maidana](mailto:dmaida3@uic.edu)' filename=' [TUNEL Cell Counter Macro](https://github.com/DanielMaidana/TUNEL_Cell_Counter/archive/master.zip)' source=' [TUNEL Cell Counter Repository](https://osf.io/9rveh/)  
' released='August 18<sup>th</sup>, 2015' latest-version='July 21<sup>th</sup>, 2016' status='Active and validated with Fiji (ImageJ 1.51d)' website=' [RETINA Analysis Toolkit at YouTube](https://www.youtube.com/channel/UCqGMCPY9ViyAPWhYciRNuKQ)' %}  
**RETINA Analysis Toolkit** is a free macro toolkit designed and developed for Fiji (ImageJ). The purpose of the RETINA Analysis Toolkit is to perform fast quantitation of digital RGB images from retina cryosections, acquired by fluorescent microscopes. The current components of these toolkit are: TUNEL Cell Counter and RETINA Cell Heatmap.


----

# TUNEL Cell Counter


TUNEL Cell Counter is a customizable tool that processes digital images from retinal cryosections. It segments retinal outer nuclear (ONL) and inner nuclear layers (INL) and quantitates fluorescent-labelled cells in these layers. {% include thumbnail src='/media/plugins/retina-cell-counter-montage.png' title='**TUNEL Cell Counter**: Input a fluorescent-labeled retinal image for ONL & INL layer segmentation and cell quantitation.'%}

## Required Components

The following are required to execute this tool:

1.  <b>TUNEL Cell Counter</b>: Macro should be installed in Fiji (ImageJ).
2.  <b>Digital Image</b>: Files should be in TIFF format.
3.  <b>Microscope Spatial Scale</b>: Pixels/microns.
4.  <b>Minimum Cell Size & Maximum Cell Area (µm<sup>2</sup>)</b>: These values should be determined upfront, according to your image dataset. These measurements can be performed in Fiji with the freehand selection tool, after setting the spatial scale factor.

## How to Use: 2 Minute Tutorial

{% include video platform='youtube' id='NyCXqNA-NTc'%}

## Processing Settings

{% include thumbnail src='/media/plugins/retina-cell-counter-dialog.png' title='**Settings Dialog**: Input the spatial scale obtained from the image metadata or microscope.'%} After importing a TIFF image and executing the counter, the following settings should be selected:

1.  <b>Microscope Magnification</b>: Displays the working 20x objective magnification.
2.  <b>Image Native Resolution</b>: Displays the imported image resolution.
3.  <b>Native Spatial Scale</b>: Input the current image scale in pixels/microns.
4.  <b>Image Rescaling Options</b>: If the image is larger that 1300 pixels width, it will be rescaled to speed up the processing. The rescaled image will be saved as a copy.
5.  <b>Minimum and Maximum Cell Area</b>: Input the previously measured and selected cutoff values.
6.  <b>Cell Roundness</b>: If "All" is selected, all thresholded cells will be counted (Circularity 0-1). If "Mostly rounded" is selected, mostly circular cells will be counted (Circularity 0.5-1.0). If "Mostly not rounded" is selected, mostly not circular cells will be counted (Circularity 0.0-0.5).
7.  <b>Retina Area Selection</b>: Choose between automated ONL & INL segmentation or manual freehand selection.
8.  <b>Threshold Sensitivity</b>: Choose between a standard and high sensitivity threshold, in case you need to detect cells with low intensity values.
9.  <b>Channels</b>: Choose the cells of interest in either the green, red, or combined channels.
10. <b>Help</b>: Links directly to this site.

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td>
        <p>style="vertical-align:top"|{% include thumbnail src='/media/plugins/retina-cell-counter-roundness.png' title='**Cell Roundness**: Select the desired morphology for cells.'%}</p>
      </td>
      <td>
        <p>style="vertical-align:top"|{% include thumbnail src='/media/plugins/retina-cell-counter-area.png' title='**Retina Area Selection**: Choose between automated or manual segmentation.'%}</p>
      </td>
      <td>
        <p>style="vertical-align:top"|{% include thumbnail src='/media/plugins/retina-cell-counter-threshold.png' title='**Threshold Sensitivity**: Select the threshold protocol for cell counting.'%}</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

## Results

A processed image is generated and saved in a new directory. Results are saved as an Excel (.xls) file.

## Limitations

1.  Acquisition: The macro was designed for images acquired with a 20x/0.8 air objective. We considered this magnification the most suitable to assess a reasonably large area without missing out cell morphology details.
2.  Staining quality: Images need to have an intense cell staining and low background noise.
3.  Image Focus: Uneven image focus will render incomplete layer segmentation.
4.  Indistinguishable Retinal Layers: The macro cannot distinguish between the ONL and INL if you can't either!
5.  Uncentered Image: For best results, acquire images centered in frame.
6.  Significant Shadowing: Shadowing will render incomplete layer segmentation.


To have an idea of suitable images for this macro, we recommend to review the image dataset used for validation:

:\*[TUNEL Cell Counter Repository](https://osf.io/9rveh/)

## FAQs

1.  Q: Can I modify the source code?
    -   A: *Yes, you can modify the code to develop new macros or plugins. Please acknowledge previous work that helped or inspired you, and share your contribution with the scientific community!*  
2.  Q: I used this tool for my research. How should I acknowledge it?
    -   A: *Please cite or reference this work as follows: Maidana DE, Tsoka P, Tian B, Dib B, Matsumoto H, Kataoka K, Lin H, Miller JW, Vavvas DG. A Novel ImageJ Macro for Automated Cell Death Quantitation in the Retina. Invest Ophthalmol Vis Sci. 2015;56:6701–6708. <DOI:10.1167/> iovs.15-17599.*  
3.  Q: I cannot get accurate segmentation or counting. Any advice?
    -   A: *Check your acquisition and post-processing parameters for the channel of interest. First, reduce background as much as possible to remove any fragments. Next, adjust saturation until cells are easily identifiable. Apply the same settings to the entire dataset if comparison is intended.*  

## Future Developments

Yes, we know there is a lot to improve!  
<b>In case you have any comments, suggestions, or any difficulties with your images, just send us a message!</b>

## References

1.  Maidana DE, Tsoka P, Tian B, Dib B, Matsumoto H, Kataoka K, Lin H, Miller JW, Vavvas DG. A Novel ImageJ Macro for Automated Cell Death Quantitation in the Retina.<i> Invest Ophthalmol Vis Sci</i>. 2015;56:6701–6708. <DOI:10.1167/> iovs.15-17599.

------------------------------------------------------------------------

# Macro Setup Instructions

## How to Download and Install ImageJ Macros

{% include video platform='youtube' id='CvhPjZ62cik'%}
