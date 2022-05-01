---
mediawiki: Registration
title: Registration
section: Learn:Scientific Imaging
nav-links: true
---

## What is Registration?

{% include wikipedia title='Image registration' text='Image registration'%} is the process of transforming different sets of image data into one coordinate system. Image data may be multiple photographs, data from different sensors, times, depths, or viewpoints. It is used in computer vision, medical imaging, biological imaging and brain mapping, military automatic target recognition, and compiling and analyzing images and data from satellites. Registration is necessary in order to be able to compare or integrate the data obtained from these different measurements.

Essentially, image registration is used to align two or more images of the same scene. The transformation function, the method for modifying the spatial relationship between pixels, needs to be estimated/modeled in order to register the two images. The input image is the image that will be transformed, and the reference image is the one against which the input is registered. Geometric distortions causing differences in angle, orientation, shifting, and distance need to be taken into account. One of the most common methods to do image registration uses *points* that correspond to locations known in both the input and reference images. Tools exist in ImageJ that can automatically detect such *correspondence points* to then estimate the transformation function.

## Recommended ImageJ Plugins for Registration

Here we summarize some of the Registration plugins in ImageJ.

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td>
        <p><strong>Plugin Name</strong></p>
      </td>
      <td>
        <p><strong>Short Description</strong></p>
      </td>
      <td>
        <p><strong>Highlights</strong></p>
      </td>
      <td>
        <p><strong>Plugin Snapshot</strong></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><a href="/plugins/feature-extraction">Feature Extraction</a></p>
      </td>
      <td>
        <p>A tool for identifying a set of corresponding points of interest in two images</p>
      </td>
      <td>
        <ul>
          <li>Interest points are detected using the Difference of Gaussian detector</li>
          <li>Uses the <a href="https://en.wikipedia.org/wiki/Scale-invariant_feature_transform">Scale Invariant Feature Transform (SIFT)</a> and <a href="http://matthewalunbrown.com/papers/cvpr05.pdf">Multi-Scale Oriented Patches (MOPS)</a> for local feature description
          </li>
          <li>Established matches are filtered using the <a href="https://en.wikipedia.org/wiki/Random_sample_consensus">Random Sample Consensus (RANSAC)</a>
          </li>
          <li>The extracted sets of corresponding landmarks and the calculated transformations are used in <a href="/plugins/trakem2">TrakEM2</a>, <a href="/plugins/register-virtual-stack-slices">Register Virtual Stack Slices</a> and <a href="/plugins/bunwarpj">BUnwarpJ</a> for image registration.
          </li>
        </ul>
      </td>
      <td>
        <p><img src="/media/tem-42-33-f.png" width="500"> MOPS feature correspondences (example 1)</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><a href="/plugins/linear-stack-alignment-with-sift">Linear Stack Alignment with SIFT</a></p>
      </td>
      <td>
        <p>A tool for aligning image stacks</p>
      </td>
      <td>
        <ul>
          <li>A lightweight SIFT-implementation for Java after the paper of David Lowe[^1].
          </li>
        </ul>
      </td>
      <td></td>
    </tr>
    <tr>
      <td>
        <p><a href="/plugins/bunwarpj">BUnwarpJ</a></p>
      </td>
      <td>
        <p>A tool for elastic and consistent image registration</p>
      </td>
      <td>
        <ul>
          <li>Performs 2D image registration based on elastic deformations represented by B-splines</li>
          <li>Invertibility of the deformations is enforced through a consistency restriction</li>
          <li>Get started with the detailed <a href="/plugins/bunwarpj#user-manual">BUnwarpJ user manual</a>
          </li>
        </ul>
      </td>
      <td>
        <p><img src="/media/plugins/bunwarpj-scheme.png" width="500"></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><a href="/plugins/trakem2">TrakEM2</a></p>
      </td>
      <td>
        <p>A tool for morphological data mining, three-dimensional modeling and image stitching, <strong>registration</strong>, editing and annotation</p>
      </td>
      <td>
        <ul>
          <li>Registers floating image tiles to each other using SIFT and global optimization algorithms.</li>
          <li>See the <a href="https://www.ini.uzh.ch/~acardona/trakem2_manual.html#registration">TrakEM2 sser manual section on registration</a>
          </li>
        </ul>
      </td>
      <td>
        <p><img src="/media/trakem2-snap.jpg" width="500"></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><a href="/plugins/register-virtual-stack-slices">Register Virtual Stack Slices</a></p>
      </td>
      <td>
        <p>A tool that takes a sequence of image slices stored in a folder and delivers a list of registered image slices</p>
      </td>
      <td>
        <ul>
          <li>The plugin can perform 6 types of image registration techniques: Translation, Rigid (translation + rotation), Similarity (translation + rotation + isotropic scaling), Affine, Elastic (via <a href="/plugins/bunwarpj">BUnwarpJ</a> with cubic B-splines), and Moving least squares
          </li>
          <li>All models are aided by automatically extracted <a href="/plugins/feature-extraction">SIFT features</a>
          </li>
        </ul>
      </td>
      <td>
        <p><img src="/media/rvs-scheme.png" width="500"></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><a href="/plugins/fijiyama">Fijiyama</a></p>
      </td>
      <td>
        <p>A registration tool for 3D multimodal time-lapse imaging</p>
      </td>
      <td>
        <ul>
          <li>User-friendly, generic and versatile</li>
          <li>Automatic 3D registration (two algorithms available)</li>
          <li>Manual registration (using the <a href="/plugins/3d-viewer">3D_Viewer</a>)
          </li>
          <li>Movie tutorials and example datasets</li>
          <li>Settings automatically adjust based on your data</li>
          <li>Transformations: linear or non-linear</li>
          <li>Tested on specimens: human, vine trunk,</li>
          <li>Tested on modalities: MRI, X-ray CT, Photograph</li>
          <li>Limitations: should be avoided for big datasets (more than 15 time points or 1GB+).</li>
        </ul>
      </td>
      <td>
        <p><img src="/media/reg-present-1.png" width="500"></p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

## Other pages and tools for Registration in ImageJ

Filter by the Registration category on the [list of extensions](/list-of-extensions) to see other ImageJ pages and tools about image registration.

# References

[^1] {% include citation id='plugins/linear-stack-alignment-with-sift' %}
