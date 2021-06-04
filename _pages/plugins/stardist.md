---
mediawiki: StarDist
title: StarDist
categories: [Uncategorized]
---


{% capture source%}
{% include github org='stardist' repo='stardist-imagej' %}
{% endcapture %}
{% include info-box name='StarDist' software='ImageJ' update-site='StarDist' author='Uwe Schmidt, Martin Weigert' maintainer='Uwe Schmidt, Martin Weigert' source=source website='https://github.com/stardist/stardist' %} <img src="/media/icons/stardist.jpg" width="128"/>

## Overview

This is the ImageJ/Fiji plugin for [StarDist](https://github.com/stardist/stardist), a cell/nuclei detection method for microscopy images with star-convex shape priors. The plugin can be used to apply already trained models to new images. See the [main repository](https://github.com/stardist/stardist) for links to our publications and the full-featured Python package that can also be used to train new models.

If you need any help, please first take a look at the StarDist [documentation](https://github.com/stardist/stardist/blob/master/README.md) and [frequently asked questions (FAQ)](https://stardist.net/docs/faq.html). 
If that doesn't solve your issue, you can browse the existing [`stardist`-tagged forum posts](https://forum.image.sc/tag/stardist) or search the [image.sc forum](https://forum.image.sc/). If you can't find what you're looking for, please create a new topic at [the forum](https://forum.image.sc/) (and use the tag `stardist`).
If you open a new topic, please provide a clear and concise description to understand and ideally reproduce the issue you're having.
Please only file an issue [here](https://github.com/stardist/stardist-imagej) for bug reports or if you have technical questions regarding the plugin.

*The plugin currently only supports 2D image and time lapse data. If you have 3D data, please use our [python library](https://github.com/stardist/stardist).*

<img src="/media/plugins/stardist-screenshot-small.jpg" width="640"/>

## Installation

1.  Start Fiji (or download and install it from [here](https://fiji.sc) first).
2.  Select `Help > Update...` from the menu bar.
3.  Click on the button `Manage update sites`.
4.  Scroll down the list and tick the checkboxes for update sites `CSBDeep` and `StarDist`, then click the `Close` button.  
    (If `StarDist` is missing, click `Update URLs` to refresh the list of update sites.)  
    <img src="/media/plugins/stardist-update-site2.png" width="320"/><img src="/media/plugins/stardist-update-site.png" width="320"/>
5.  Click on `Apply changes` to install the plugin.
6.  Restart Fiji.

## Usage

### Plugin

Open the image that should be segmented. Note, that currently only 2D and 2D+time images are supported. Suitable test images can for instance be found at the [Broad Bioimage Benchmark Collection](https://data.broadinstitute.org/bbbc/BBBC008/BBBC008_v1_images.zip)[1]:

<img src="/media/plugins/stardist-usage-input.png" height="240"/>

Start the plugin from `Plugins > StarDist > StarDist 2D`. The following parameters can be set:

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td>
        <p><img src="/media/plugins/stardist-usage-param-pred.jpg" width="400"></p>
      </td>
      <td>
        <p>Select a neural network model from the dropdown list, which can be one of the following:</p>
        <ul>
          <li>
            <em>A built-in model</em>. We currently provide:
            <ul>
              <li>
                <code>Versatile (fluorescent nuclei)</code> and <code>DSB 2018 (from StarDist 2D paper)</code> that were both trained on a subset of the <a href="https://data.broadinstitute.org/bbbc/BBBC038/">DSB 2018 nuclei segmentation challenge dataset</a>.
              </li>
              <li>
                <code>Versatile (H&amp;E nuclei)</code> that was trained on images from the <a href="https://monuseg.grand-challenge.org/Data/">MoNuSeg 2018 training data</a> and the <a href="http://cancergenome.nih.gov/">TCGA archive</a>.
              </li>
            </ul>
          </li>
          <li>
            <em>A custom user-trained model</em> (<a href="https://github.com/stardist/stardist">via the training code</a>) that has been <a href="https://github.com/stardist/stardist/search?q=export_TF&amp;type=Code">exported as a zip file</a> and can be loaded from a file or URL (see <em>Advanced options</em> below).
          </li>
        </ul>
        <p>If necessary, one can change/disable the percentile-based input image normalization.</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><img src="/media/plugins/stardist-usage-param-nms.jpg" width="400"></p>
      </td>
      <td>
        <p>Adjust the NMS (non-maximum suppression) postprocessing parameters:</p>
        <ul>
          <li><em>Probability/Score Threshold</em> - higher values lead to fewer segmented objects, but will likely avoid false positives.</li>
          <li><em>Overlap Threshold</em> - higher values allow segmented objects to overlap substantially.</li>
        </ul>
        <p>If in doubt, load the default NMS parameters of the selected built-in model (see below).</p>
        <p>The segmented objects can be returned as a <em>Label Image</em> or in the <em>ROI Manager</em> (or both).</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><img src="/media/plugins/stardist-usage-param-advanced.jpg" width="400"></p>
      </td>
      <td>
        <p>Advanced options:</p>
        <ul>
          <li>Specify a user-trained model file or URL</li>
          <li>Increase the number of tiles (in case of GPU memory limitations/errors, i.e. for larger images)</li>
          <li>Load default NMS parameters for the selected built-in model.</li>
          <li>Restore all default parameters.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>
{:/}

Example of running the plugin, showing the returned label image and ROIs overlaid on the input image (check `Show All` in the ROI Manager):

<img src="/media/plugins/stardist-usage-output.png" height="240"/>

### Scripting/Batch-Processing

Please have a look at the [Fiji/Jython script batch-processing example](https://gist.github.com/maweigert/8dd6ef139e1cd37b2307b35fb50dee4a) that runs stardist on all files of a folder.

## Citation

Please cite the paper if you are using the plugin in your research:

-   Uwe Schmidt, Martin Weigert, Coleman Broaddus, and Gene Myers. [Cell Detection with Star-convex Polygons](https://arxiv.org/abs/1806.03535). International Conference on Medical Image Computing and Computer-Assisted Intervention (MICCAI), Granada, Spain, September 2018.

## References

  

[1] Carpenter et al., Genome Biology, 2006
