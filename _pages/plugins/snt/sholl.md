---
title: SNT › Sholl Analysis
nav-links: true
nav-title: Sholl
name: Sholl plugins
categories: [Analysis,Neuroanatomy]
tags: [sholl,sholl analysis,snt,arbor,neuron,morphometry,dendrite,neuroanatomy]
forum-tag: sholl-analysis
artifact: org.morphonets:SNT
icon: /media/icons/snt.png
doi: 10.1038/nmeth.3125
update-site: Neuroanatomy
---

{% capture text%}
***SNT and Sholl Analysis* are based on [publications](/plugins/snt/faq#how-do-i-cite-snt). Please [cite](/plugins/snt/faq#how-do-i-cite-snt) them in your own research!**
{% endcapture %}
{% include notice icon="info" content=text %}
{% capture version%}
**This page was last revised for [version 5.0.0](https://github.com/morphonets/SNT/releases)**.<br>
Please help us to keep up-to-date documentation by [editing](https://github.com/imagej/imagej.github.io/edit/main/_pages/plugins/snt/reconstruction-viewer.md) this page directly to fill in any documentation gap. Do [reach out](https://forum.image.sc/tag/snt) if you need assistance!
{% endcapture %}
{% include notice content=version %}

Automated Sholl for direct analysis of segmented images and traced morphologies. Features powerful quantifications based on curve fitting. Analysis of profiles obtained by other software is also possible.


# Introduction
<img align="right" width="40%" src="/media/plugins/snt/snt-shortcuts-window.png" title="The Neuroanatomy Shortcuts panel can be toggled using the SNT icon in the ImageJ toolbar" />
The Sholl technique[^2] is used to describe neuronal arbors. SNT features a collection of tools that perform Sholl on reconstructed morphologies, or directly on 2D/3D images of isolated neurons (bypassing the need for reconstruction). The procedure is based upon how Sholl analysis is done by hand: Algorithms define a series of concentric *shells* (circles or spheroids) around a focal point of a neuronal arbor and count how many times the arbor intersects sampling shells. The major advantages of these tools over other implementations are:

- Both images and reconstructions can be analyzed
- When analyzing images directly, previous tracing of the arbor is not required
- [Curve fitting](#methods-table) is combined with several [methods](#sholl-plots) to automatically retrieve [quantitative descriptors](#metrics) from sampled data, which allows direct statistical comparisons between arbors
- [Continuous and repeated sampling](#multiple-samples-and-noise-reduction) around user-defined foci are allowed
- [Angular](#angular-sholl) and [Length-based](#length-based-profiles) profiles
- Extensive options for quantitative analysis
- [Batch processing](#batch-processing) is possible

After [installing SNT](/plugins/snt/#installation), Sholl commands can be accessed through the {% include bc path='Plugins|Neuroanatomy|Neuroanatomy Shortcut Window'%} (SNT icon in the ImageJ toolbar), or from SNT's [tracing interface](analysis#sholl-analysis).

<span id="ca1-cell-mask"></span><span id="ca1-cell-plot"></span>
{% include gallery align="center" content=
"
/media/plugins/snt/sholl-analysis-outputs.png | Overview of outputs: Linear and log-log profile (Sholl decay calculation), detailed and summary tables. ‘Traditional’ plots are obtained by disabling curve-fitting altogether
/media/plugins/snt/bitmapsholl-ca1mask.png | [Skeletonized](/plugins/skeletonize3d) hippocampal CA1 cell[^8] in which apical and basal dendrites have been analyzed [separately](#ca1-cell-plot) and [color coded](#output-options) according to their Sholl profile. Warmer hues indicate higher number of Intersections (*N*). [Critical radius](#critical-radius) (*r<sub>c</sub>*) and [Mean value](#mean-value-of-function) (*N<sub>av</sub>*) are indicated.
/media/plugins/snt/bitmapsholl-ca1compartment.png | Linear plot for the same CA1 cell[^8]. Using the soma as center, image was sampled twice using [hemishells](#hemishells) in order to segregate apical from basal dendrites. For clarity, distances for basal branches were assigned negative values and arbor overlaid (in green) over the profile.
/media/plugins/snt/combineshollprofiles.png | *Combine Sholl Profiles...* aggregates individual profiles into a single plot, obtaining the average profile for groups of cells [[use case](https://forum.image.sc/t/sholl-merging-profiles-with-different-radii/54144/13)]
/media/plugins/snt/sholl-group-statistics.png | Statistics for [groups of cells](/plugins/snt/analysis#comparing-reconstructions) [[use case](https://forum.image.sc/t/sholl-analysis-with-snt-one-graph-for-two-groups/82471/2)]
/media/plugins/snt/animatedpolyfit.gif | Sampled data can be fitted to polynomials of varying degree (animation created using [BAR](/plugins/bar))
/media/plugins/snt/sholl-convex-hull.png | Scripting allows for arbitrary focal points, in this case the centroid of the neuron's convex hull (*Convex Hull as Center* template script)
/media/plugins/snt/snt-angular-sholl-ddac.png | [Angular Sholl](#angular-sholl) and [Angle-based metrics](##metrics-based-on-angular-sholl)
/media/plugins/snt/shollresultasrois.png | Intersection points and sampling shells can be retrieved as ROIs. Intersection points are placed at edges of detected clusters of foreground pixels, not their center.
/media/plugins/snt/sholl-rasterized-shells.png | Using Sholl to measure the distribution of image objects (_Sholl Rasterize Shells_ template script) [[use case](https://forum.image.sc/t/measuring-distribution-of-object-diameters-in-different-stripes-using-sholl-plugin/51087)]
/media/plugins/snt/snt-sholl-integrate-density-profiles.png | Not only neurons: Integrated-density profiles can be used to obtain radial maps of fluorescent markers.
"
%}


# Length-based Profiles

Since SNTv5 it is possible to obtain **length profiles** in addition to the traditional **No. of intersections** counts. The two strategies are usually (highly) correlated but not identical: _Intersection counts_ summarize how often the arbor crosses each sampling shell (frequency of crossings). _Length_ summarizes ow much cable lies within each shell.

<i class="fas fa-image"></i> For direct parsing of images, groups of foreground pixels are first identified along each sampling shell:
- Groups are defined as 8‑connected components in 2D and 26‑connected in 3D
- The _No. of Intersections_ at a shell is the number of identified groups
- The _Intersected length_ at a shell is the sum of path lengths of all groups within that shell. Note that lengths can be affected by the apparent thickness of processes. Consider skeletonizing before analysis to reduce thickness bias

<i class="fas fa-pen"></i> For traced morphologies, each segment (straight line between consecutive nodes) is tested against each sampling shell:
 - If a segment intersects a shell, the segment is clipped to the shell and its arc length inside the shell is accumulated
 - Intersections at a shell correspond to the number of connected arbor components that cross the shell (based on the tracing graph topology, not pixel connectivity)
 - Length at a shell corresponds to the sum of Euclidean lengths of all clipped segment pieces inside that shell. Note that node radii are not considered for length calculations

**NB:**
- Conceptually, length requires a non‑zero [radius step size](#step-size). If you select continuous sampling (step size = 0), the program will internally fallback to a _minimum_ separation: Either the geometric mean of voxel dimension when parsing images, or the median inter-node distance of the structure when parsing reconstructions
- Reported lengths are in calibrated units (e.g., µm)


# Direct Analysis of Images
<img align="right" width="320px" src="/media/plugins/snt/sholl-bitmap-promptv4.png" title="Main prompt (v4.2.1) when input is a segmented image" >

In this mode (bitmap analysis), the plugin requires a [binary image or a segmented](#faq:threshold) [grayscale image](#faq:image-types) (2D or 3D) containing a single neuron.

1.  Segment the neuronal arbor using {% include bc path='Image|Adjust|Threshold...'%} (shortcut: {% include key keys='Shift|T' %}). When using multichannel images, you will have to set the display mode to *Grayscale* using {% include bc path='Image|Color|Channels Tool...'%} ({% include key keys='Shift|Z' %}), because images displayed as *Composites* cannot be thresholded.
2. [Visually inspect](#cf-segmentation) the two thresholded phases in the image to ensure the *arbor* is being parsed and not *background*.
3. Define the center of analysis using a valid [startup ROI](#startup-roi).
4. Run {% include bc path='Analysis|Sholl|Sholl Analysis...'%}, adjusting the default [Parameters](#parameters) in the dialog prompt.
5. Problems? Read the [FAQs](#faq).


## Startup ROI

The center of analysis can be specified using one of three possibilities:

1. Straight line: A Straight line from the focus of the arbor to its most distal point using the Straight Line Tool. The advantages of using line selections are twofold: 1) Center of analysis and [Ending radius](#end-radius) are automatically set, and 2) Horizontal/vertical lines (created by holding {% include key key='Shift' %} while using the Straight Line Selection Tool) can be used to [restrict analysis to sub-regions](#restrict) of the image.

2. Single point: A single point marking the focus of the arbor using the Point Selection Tool. With single point selections, only the center of analysis is defined. Thus, this option is suitable for [batch processing](#batch-processing) of images with different dimensions with undefined [Ending radius](#end-radius).

3. Multipoint selection:A Multi-point selection (multipoint counter) in which the first point marks the center of analysis while the remaining points mark (count) the number of primary branches required for the calculation of [ramification indices](#schoenen-sampled)). Suitable for cases in which [inference from starting radius](#primary-branches) is not effective.

{% include img align="center" name="sholl plots" src="/media/plugins/snt/shollanalysisstartuprois.png" %}

Three types of ROIs expected by the plugin when analyzing images directly. <b>Left</b>: Line defining center of analysis (focal point), hemisphere restriction and ending radius. <b>Middle</b>: Single point defining center of analysis. <b>Right</b>: Multi-point selection in which the first point defines the focal point while the remaining points (2 to 5) serve as counters for primary neurites.

## Cf. Segmentation

It is important to visually confirm which phase of the segmented image will be sampled, specially when using black and white (binary) lookup tables. To so, you can select the _Red_ lookup table in the Threshold widget ({% include bc path="Image | Adjust | Threshold..." %} {% include key keys='Shift|T' %}) to highlight foreground from background pixels to verify that you are measuring neuronal processes and not the interstitial spaces between them. Here is an example using an axonal arbor from the Drosophila olfactory neuron [demo dataset](./manual#load-demo-dataset):

<table>
  <tbody>
    <tr style="background-color:white">
      <td>
        <center>
          <p><span style="display:inline-block;text-align:center;width:230px">Segmented image<br><em>(Black/White LUT)</em></span> <span style="display:inline-block;text-align:center;width:230px">Segmented image<br><em>(Yellow/Blue LUT)</em></span> <span style="display:inline-block;text-align:center;width:230px">Intersections mask<br><em>(Jet LUT)</em></span></p>
        </center>
      </td>
    </tr>
    <tr style="background-color:white">
      <td>
        <center>
          <figure>
            <img src="/media/plugins/cfsegmentation.png" width="700">
          </figure>
        </center>
      </td>
    </tr>
    <tr style="background-color:white">
      <td>
        <center>
          <strong>Top row:</strong> Image properly segmented: Arbor is sampled. <strong>Bottom row:</strong> Aberrant segmentation (inverted image): Background is sampled.<br>
        Note the reversal of output and how the <em><a href="#output-options">intersections mask</a></em> no longer decorates the axonal processes but the interstitial spaces between them. The consequences of the phase inversion are twofold: 1) the program oversamples (cf. hue ramps on upper left of <em>Intersections mask</em>) and 2) the program detects artifacts induced by the edges of the image (cf. top-right and bottom-right corners of mask where intersections are sampled in the absence of real axons at those locations). Also, note that the initial black and white image would <em>look the same</em> under an inverted lookup table ({% include bc path='Image|Lookup Tables|Invert LUT'%}).
        </center>
      </td>
    </tr>
  </tbody>
</table>


{%- capture binary-tip -%}
With binary images, *Sholl Analysis* treats zero intensities as the background, independently of the image lookup table or the state of the *Black background option* in {% include bc path="Process | Binary | Options..." %}. As with any other [ImageJ routine](https://imagej.net/ij/docs/guide/146-29.html#infobox:blackBackground) , confusing background with foreground pixels will lead to aberrant results, including: 1) overestimation of branches and 2) artifacts at distances intersecting the boundaries of the image canvas.
{%- endcapture -%}
{% include notice icon="tip" content=binary-tip %}

<span id="traces"></span>


# Analysis of Traced Cells

<img align="right" width="320px" src="/media/plugins/snt/sholl-tracings-promptv4.png" title="Main prompt (v4.2.1) when input is a traced data" >

In this mode the plugin analyzes reconstructed arbors (traced in SNT or [elsewhere](/update-sites/neuroanatomy/external-resources)), which is particularly relevant for stainings that do not allow single-cell resolution or proper segmentation. There are several entry points to this analysis, namely:

- [SNT](/plugins/snt/analysis#sholl-analysis)'s main interface: Offers more options for defining the center of analysis, restrictions to tagged branches, etc., but is not amenable to batch processing.
  
- *Sholl Analysis (Tracings)* commands accessed through the {% include bc path='Plugins|Neuroanatomy|Neuroanatomy Shortcut Window'%} (SNT icon in the ImageJ toolbar): for cases in which viewing traces is not necessary, or when [batch processing](#batch-processing) is needed

To analyze cells without having to initialize SNT's tracing interface, run {% include bc path='Sholl Analysis (Tracings)...'%} and specify:
  
- **File** The [tracing file](/plugins/snt/faq#file-format) (swc, .ndf, .json, or .traces extension) to be parsed

- **Path filtering** Whether the analysis should be restricted to particular paths, e.g., those tagged as  (*axon*, *dendrite*, *soma*, etc.). Note that if your tracings are not tagged you can do so in [SNT](/plugins/snt/analysis#sholl-analysis)

- **Center** The center of analysis, defined by:
    - **Root nodes** These correspond to the starting nodes of primary (root) paths. If multiple primary paths exist, center becomes the centroid (mid-point) of their starting nodes
    - **Soma node(s)** These correspond to nodes tagged as "soma". If _Ignore connectivity_ is chosen, the centroid of all soma-tagged nodes is used, even if such nodes are not at the root of the structure. If _Primary paths only_ is chosen only root nodes tagged as "soma" are considered

- **Metrics & Output** These are described in [Curve fitting](#descriptors-and-curve-fitting), [Choice of Methods](#choice-of-methods), and [Output options](#output-options).

- **Advanced Options** These are included in the _Options, Preferences and Resources_ dialog, and include:

  - **Skip somatic segments** If primary paths start 'far-away' from the soma, this options allows segments between the soma and neurite be ignored. Note that this option is only considered when the arbor being analyzed is rooted on a single-node tagged as 'Soma'
  
  - **Include zero counts** Whether entries associated with 0 intersections should be included in detailed tables, plots, etc.


# Analysis of Existing Profiles
<span id="importing"></span>
This option allows curve fitting to be applied to previously sampled profiles and is achieved via [scripting](/plugins/snt/scripting). It requires only a tab or comma delimited text file (.csv, .txt) listing a sampled Sholl profile. Have a look at the *Sholl Extensive Stats Demo* [template script](/plugins/snt/scripting#bundled-templates) for more details.

# Parameters

Some parameters are specific to the type of data used as input whether a segmented image or a reconstruction (tracing). When analyzing images, input values take into account the scale information of the image (which can be set using the {% include bc path='Analyze|Set Scale...'%} or {% include bc path='Image|Properties...'%} ({% include key keys='Shift|P' %}), the type of image (2D or 3D), and its [active ROI](#startup-roi).

For clarity, settings pertaining to direct parsing of images are tagged with <i class="fas fa-image"></i>, those pertaining to reconstructions (tracings) with <i class="fas fa-pen"></i>.

## Shells
<span id="definition-of-shells"></span>

#### Profile type
<i class="fas fa-image"></i> <i class="fas fa-pen"></i> Whether the profile should report traditional **No. of intersections** counts or [intersected lengths](#length-based-profiles)

#### Start radius
<i class="fas fa-image"></i> The radius of the smallest sampling circle/sphere, i.e., the first distance to be sampled.

#### Step size
<i class="fas fa-image"></i> <i class="fas fa-pen"></i> The sampling interval between radii of consecutive sampling circles/spheres. This value may be set to zero for continuous (1-voxel increment) measurements. For stacks with anisotropic voxel size, setting *Radius step size* to zero, sets the step length to the dimension of the matching isotropic voxel, i.e., the geometric mean of voxel dimensions: For 3D images, the cube root of the product of the voxel dimensions; For 2D images: the square root of the product of the pixel dimensions.

#### End radius
<i class="fas fa-image"></i> The radius of the largest (last) sampling circle/sphere. It is automatically calculated if a [line ROI is used](#usage). Note that the specified distance may not be actually sampled, if *Radius step size* is not a divisor of *Ending radius*-*Starting radius*. In this case, the program will choose the largest possible distance smaller than the specified value. You can clear *Ending radius* or set it to *NaN* ("Not a Number") to sample the entire image. This is particularly useful when [batch processing](#batch-processing) images with different dimensions.

#### Hemishells
<span id="restrict"></span>
<i class="fas fa-image"></i> This option can be used to limit the analysis to sub-compartments of the arbor. This option instructs the algorithm to measure intersections at sites equidistant from the center that have y-coordinates above/below the drawn line or x-coordinates to the left/right of the center.

#### Preview
<i class="fas fa-image"></i> <i class="fas fa-pen"></i> Previews sampling shells on the image being analyzed. Note that with 3D images, the previewed 2D circumferences do not reflect the actual 3D spheres used by the algorithm.

#### Set center from Active ROI
<i class="fas fa-image"></i> Updates the center position by reading the centroid of the active ROI.


### Segmentation

#### Samples per radius *(2D images only)*
<span id="multiple-samplesnoise-reduction"></span>
<i class="fas fa-image"></i> Defines the number of measurements to be performed at each sampling circumference. These measurements are then combined into a single value according to the chosen [integration method](#samples-integration). This strategy, a break from previous approaches, increases the accuracy of non-continuos profiles by diluting out the effect of processes extending tangent to the sampling circumference.

Visually, this option can be imagined as the "thickness" of the sampling circumference: e.g., for a radius of 100 pixels and a value of 3 *Samples per radius*, the final number of intersections would integrate the measurements sampled at distances 99, 100 and 101. Note that it would not make sense to increase the number of samples beyond the length (in pixels) of *Radius step size*. For this reason, this option is limited to a draconian (and arbitrary) maximum of 10 samples.

#### Samples integration *(2D images only)*
<span id="samples-integration"></span>
<i class="fas fa-image"></i> The measure of central tendency used to combine intersection counts when multiple *Samples per radius* are used. Options are *Mean* (the default), *Median* or *Mode*.

#### Ignore isolated voxels *(3D images only)*
<i class="fas fa-image"></i> Accessed thorough the _Options & Preferences_ dialog. If checked, single (6-connected) isolated voxels intersecting the surface of sampling spheres are not taken into account, which may allow for smoother profiles on noisy image stacks. However, it should be noted that connectivity in the stack volume may not reflect connectivity on the surface of a digitized sphere. Indeed, in certain contexts, it is possible (though unlikely) to obtain higher intersection counts when this filtering option is active.

Keep in mind that this is just a refinement feature, and you should not expect it to mitigate major artifacts derived from poor segmentation.

#### No. of parallel threads  *(3D images only)*
<i class="fas fa-image"></i> Accessed thorough the _Options & Preferences_ dialog. Sets the max. no. of parallel threads to be used when parsing 3D stacks. Note that this options also sets the no. of threads used by ImageJ and SNT for other multithreaded tasks. Set it to 0 to use all of the available processors on your computer.

#### Number of primary branches
<i class="fas fa-image"></i> The number of primary branches (i.e., those originating directly from cell soma when the center of analysis is the perikaryon) to be used in the calculation of [Schoenen ramification indices](#schoenen-sampled). This option is only relevant when computing branching indices. Set it to zero to disable calculations of ramification indices. Choices include:

- **Infer from starting radius** If checked, the *Number of Primary branches* is inferred from the count of intersections at [Starting radius](#start-radius).
- **Infer from multipoint ROI** Uses multipoint counts if a multipoint ROI is [detected at startup](#startup-roi).


### Polynomial fit
<span id="descriptors-and-curve-fitting"></span>
<i class="fas fa-image"></i> <i class="fas fa-pen"></i> Specifies the degree of the [polynomial](#methods-table) to be fitted to the *Linear* profile[^4]. While the polynomial of best approximation, or "best fit", should be empirically determined for each analyzed cell type, it is possible to ask the plugin to predict the order of the fitting polynomial (or at least try) using the choice *Best fitting degree*. In this case, the plugin will loop through all the available choices of polynomials, perform each fit in the background and choose the one with the highest coefficient of determination.

Detailed control over polynomial fitting is controlled by the options in the *Options & Preferences* prompt, namely:

- **Min. Degree** The lowest order to be considered when calculating the 'best-fit' polynomial
- **Max. Degree** The highest order to be considered when calculating the 'best-fit' polynomial (degrees above 40 may not be supported)
- **R-squared cutoff** The coefficient of determination (R<sup>2</sup>) cutoff used to discard 'inappropriate fits'. Only fits associated with a R^2 greater than this value will be considered
- **K-S validation** Whether a fit should be discarded if two-sample Kolmogorov-Smirnov testing rejects the null hypothesis that fitted and profiled values are samples drawn from the same probability distribution (p&lt;0.05)

### Normalization
<span id="sholl-methods"></span><span id="choice-of-methods"></span>
<i class="fas fa-image"></i> <i class="fas fa-pen"></i> Options for computing metrics based on normalized ([Semi-log or Log-log](#methods-table) profiles), including [Sholl decay](#sholl-decay).

- **Method** Specifies the type of method. Select *Automatically choose* when you cannot predict which type of normalized profile best describes the dataset. If chosen, the plugin will use the [Determination ratio](#dratio) to determine which of *Semi-log* or *Log-log* methods is more appropriate.

- <span id="normalizer"></span>**Normalizer** The property of the sampling shell to be used in the normalization of *Linear-norm*, *Semi-log*, and *Log-log* profiles. Default is area (2D images)/volume (3D images). It is [described below](#methods-table).

### Output Options
<i class="fas fa-image"></i> <i class="fas fa-pen"></i> Defines which kind of annotations should be output, including:

- **Plots** The type of plot(s) to be output. In addition to the [Linear and Normalized profiles](#methods-table) and their cumulative variants, it is also possible to obtain integrated density plots when parsing images. In this case rather than reporting on intersections, these plots report on normalized integrated density (sum of all voxel intensities) along the sampling shell normalized to the perimeter/surface of the shell.

- **Tables** Defines which kind of tables should be output, including _Detailed_ and _Summary_ tables.

- **Annotations** Defines which kind of annotations should be output, including:

  - **LUT** The Lookup Table (LUT) used for annotations.

  - **ROIs** Allows for two sets of ROIS to be added to the image overlay: 1) concentric shells matching sampled distances (circular ROIs or composite ROIs when using hemicircles); and 2) Multipoint ROIs at intersection sites between shells and clusters of foreground pixels. Note that WYSIWYG versions (RGB images) of these masks can be obtained using by pressing {% include key keys='Shift|F' %} ({% include bc path='Image|Overlay|Flatten'%}) or by running {% include bc path='Analyze|Tools|Calibration Bar...'%}. Note that ROIs are not created when outputting integrated density plots.

  - **Mask** A 16/32–bit maximum intensity projection of the analyzed image is generated in which the measured arbor is painted according to its Sholl profile. The type of data (*Raw*, i.e., sampled or *Fitted*) is displayed in the image subtitle

- **Save files** If checked, outputs are saved to the specified directory. Files are named after the image filename .

-   **Show fitting details** - Choose this option to have all the parameters of the simplex fitting printed to the Log window. The {% include wikipedia title='Coefficient of determination' text='coefficient of determination'%} (*R<sup>2</sup>*, a measure of goodness of fit) is always stored in the *Sholl Results* table even when this option is not selected


# Sholl Plots

{% include img align="center" name="sholl plots" src="/media/plugins/snt/shollplots.png" %}

***Linear*, *Linear-norm*, *Semi-log* and *Log-log* profiles** for the ddaC [demo dataset](./manual#load-demo-dataset). Most of the retrieved [metrics](#metrics-based-on-fitted-data) are automatically highlighted by the plugin. *Linear profile*: [Mean value](#mean-value-of-function) (horizontal grid line) and [Centroid](#centroid) (colored mark). Logarithmic profiles: The [Sholl regression coefficient](#sholl-decay) (also known as Sholl decay) can be retrieved by linear regression using either the full range of data (blue line) or data within percentiles 10–90 (red line). For this particular cell type, the Semi-log method is more [informative](#dratio) when compared to the Log-log method. **See [Angular Sholl](#angular-sholl) for other type of plots**.

<span id="methods-table"></span>
<table>
  <thead>
    <tr class="header">
      <th></th>
      <th>
        <p>Method</p>
      </th>
      <th>
        <p>Fit</p>
      </th>
      <th>
        <p>Description</p>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <p><span id="eq1">(1)</span></p>
      </td>
      <td>
        <p>Linear</p>
      </td>
      <td>
        <p><i>N</i> = a + br + cr<sup>2</sup> + dr<sup>3</sup> + er<sup>4</sup> + fr<sup>5</sup> + ... + xr<sup>n</sup></p>
      </td>
      <td>
        <p><br>
        Outputs a <em>N vs Distance</em> profile. Data is fitted to a polynomial function<a href="#fn:4" class="footnote-ref" id="fnref4" role="doc-noteref"><sup>4</sup></a>. <a href="#critical-radius">Critical radius</a>, <a href="#critical-value">Critical value</a> and <a href="#mean-value-of-function">Mean value of function</a> are calculated<br></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><span id="eq2">(2)</span></p>
      </td>
      <td>
        <p>Linear-norm</p>
      </td>
      <td>
        <p><em>N/S</em> = a r<sup>b</sup></p>
      </td>
      <td>
        <p><br>
        Outputs a <i>N/S vs Distance</i> profile. Points are fitted to a power function. It is an intermediate representation of the data that can be used to gauge the choice of <a href="#normalizer">normalizer</a>. Once plotted under a logarithmic scale the Linear-norm curve is similar to the Semi-log profile<br></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><span id="eq3">(3)</span></p>
      </td>
      <td>
        <p>Semi-log</p>
      </td>
      <td>
        <p>log(<em>N/S</em>) = -k r + m</p>
      </td>
      <td>
        <p><br>
        Outputs a <i>log(N/S) vs Distance</i> profile. A linear regression is fitted to the sampled data. The <a href="#sholl-decay">Sholl regression coefficient</a> (<em>k</em>) is calculated<br></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><span id="eq4">(4)</span></p>
      </td>
      <td>
        <p>Log-log</p>
      </td>
      <td>
        <p>log(<em>N/S</em>) = -k × log(r) + m</p>
      </td>
      <td>
        <p><br>
        Outputs a <i>log(N/S) vs log(Distance)</i> profile. Data is also fitted to a straight line. This is an alternative approach<a href="#fn:5" class="footnote-ref" id="fnref5" role="doc-noteref"><sup>5</sup></a> of obtaining a relevant <a href="#sholl-decay">regression coefficient</a>, when the Semi-log method returns a poor fit<br></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><span id="eq5">(5)</span></p>
      </td>
      <td>
        <p>Angular (Polar)</p>
      </td>
      <td>
        <p>von Mises (unimodal distributions only)</p>
      </td>
      <td>
        <p><br>Distributes profiled data over [angular sections](#angular-sholl] to detect directional biases in the data. Preferred directions are identified by detecting maxima in the angular distribution of the data.
        <br></p>
      </td>
    </tr>
  </tbody>
</table>

<span style="display: inline-block; width: 25px">***N***</span> For 2D images, the <u>N</u>umber of clusters of pixels (8–connected) intersecting the circumference of radius *r*
<span style="display: inline-block; width: 25px"> </span> For 3D images, the <u>N</u>umber of clusters of voxels (26-connected) intersecting the surface of the sphere of radius *r*

<span style="display: inline-block; width: 25px">***r***</span> Distance from center of analysis (<u>r</u>adius of Sholl circle/sphere)

<span style="display: inline-block; width: 25px">***log***</span> Natural logarithm, the logarithm to the base *e*

<span style="display: inline-block; width: 25px">***S***</span>The [property](#normalization) of the sampling shell to be used in the normalization of *Linear-norm*, *Semi-log*, and *Log-log* profiles.
<span style="display: inline-block; width: 25px"> </span>For 2D images, the *Perimeter* of the sampling circumference (2πr) or the *Area* of the corresponding circle (πr<sup>2</sup>)
<span style="display: inline-block; width: 25px"> </span>For 3D images, the *Surface* of the sampling sphere (4πr<sup>2</sup>) or its respective *Volume* (4/3πr<sup>3</sup>)
<span style="display: inline-block; width: 25px"> </span>*Annulus*/*Spherical shell* normalization is also available when performing [non-continuous sampling](#step-size). In this case, the normalization is performed against the area/volume between circumferences/spheres at *r* ± *Radius step size*/2


# Angular Sholl

Angular Sholl (radius × angle, also called *Polar Sholl*) produces polar heatmaps to reveal directional biases in Sholl Profiles and how such biases change with distance. Angular Sholl distributes the location of Sholl intersection (i.e., "Sholl Points") over angular sectors. Summing the _No. of intersections_ (or _intersected length_) across each radius produces an *angular distribution* used to compute [angle-based metrics](#metrics-based-on-angular-sholl).

In simplistic terms, the algorithms in Angular Sholl that detected preferred orientations work as follows:

1. “compass histogram": Imagine the space around the neuron divided into equal slices like a pizza (e.g., every 10°). For each slice the program adds up how much arbor points each way—either the number of crossings (“intersections”) or the amount of intersected cable (“length”)

2. Smoothing: Each slice is averaged with its two neighbors to reduce jitter from noise
 
3. Standout slices (“peaks”) are identified: The program measures how much "taller" a slice is relative to its immediate neighbors using a local prominence (difference from the average of the two neighbors). Only taller slices with a strong prominence are considered real peaks

4. Curve fitting: If only one peak is identified, the distribution angles is fitted to a [von Mises distribution](https://en.wikipedia.org/wiki/Von_Mises_distribution). As detailed in [Root Angle Analysis](./analysis#root-angle-analysis), this a a circular analogue of the normal distribution that models angles/directions

5. After this process is concluded, a list of directional "peaks" are obtained: each has an angle (in degrees) and a strength (the height of that slice)


{% include img align="center" width="850px" src="/media/plugins/snt/snt-angular-sholl.png" %}
**Examples of angular (polar) profiles**. Left: Space filling dendrites of the ddaC demo dataset featuring an homogenous [angle distribution](#adc). Right: Pyramidal neuron (MouseLight dendrites demo dataset). Basal dendrites are associated with an homogenous angle distribution, but apical dendrites feature a strong [directional bias](#preferred-direction). In both causes, a bin width of 10° was used. This type of data can be obtained for [length-based profiles](#length-based-profiles) and [fitted data](#polynomial-fit).



# Metrics

Morphometric descriptors and other properties of the arbor are printed to the measurements table. Output is customizable using the _detailed metrics_ checkbox in the "Further Options" dialog in the analysis prompt.


## Metrics based on sampled data

- <span id="bi">**Branching Index (*BI*)** An index that summarizes neurite arborization as defined by Garcia-Segura & Perez-Marquez[^7]. Note that this index is broadly affected by radius step size. Comparison of this metric across cells sampled differently will be nonsensical, as [demonstrated here](https://forum.image.sc/t/access-sholl-profiles-with-python-script-from-tracings/78837/6). Step size should always be included (e.g., BI<sub>10μm</sub>=20) when reporting this metric.

- <span id="centroid">**Centroid radius**  The abscissa of the {% include wikipedia title='Centroid' text='centroid'%} (i.e., the geometric center or barycenter) of the linear profile. It is [highlighted](#sholl-plots) on the *N* vs *Distance* plot.

- **Centroid value** The ordinate of the {% include wikipedia title='Centroid' text='centroid'%} (i.e., the geometric center or barycenter) of the linear profile. It is [highlighted](#sholl-plots) on the *N* vs *Distance* plot.

- <span id="enclosing-radius"></span> **Enclosing radius**  The last (thus, the widest) of *Intersecting radii* to be associated with the number of intersections specified by [Enclosing radius cutoff](#enclosing-radius-cutoff). For a cutoff of 1 (the default) *Enclosing radius* is the widest of *Intersecting radii*. It reflects the {% include wikipedia title='Feret diameter' text='Feret length'%} of the arbor.

- <span id="kurtosis"></span> **Kurtosis** The {% include wikipedia title='Kurtosis' text='kurtosis'%} of the sampled data, which quantifies whether the shape of the distribution matches that of a Gaussian distribution, assuming that a Gaussian distribution has a kurtosis of 0. A distribution more peaked than a Gaussian has a positive kurtosis while a negative value indicates a flatter distribution. See also [Kurtosis (fitted data)](#kurtosis-fitted)

- <span id="max-inters"></span> **Highest count of intersections (*Max inters.*)**  The maximum value of sampled intersections, i.e., the maximum in a linear \[*N* vs *Distance*\] profile, reflecting the highest number of processes/branches in the arbor. See also [Critical value](#critical-value).

- **Intersecting radii** The number of sampling radii intersecting the arbor at least once.

- <span id="mean-inters"></span> **Mean of intersections (*Mean inters.*)** *Sum inters.* divided by *Intersecting radii*. See also [Mean value](#mean-value-of-function), [FAQ](#faq:AUC)

- **Median of intersections (*Median Inters.*)**  The median value of sampled intersections.

- <span id="max-inters-radius"></span> **Radius of highest count of intersections (*Max inters. radius*)** The distance at which the *Highest count of intersections* occurred, reflecting sites of highest branch density. Note that if the same maximum occurs multiple times, only the first distance is considered. See also [Critical radius](#critical-radius)

- <span id="schoenen-sampled"></span> **Schoenen Ramification index (*Ramification index (sampled)*)** A measure of ramification[^6]: the ratio between *Max inters.* and the number of [primary branches](#primary-branches). It is only calculated when [primary branches](#primary-branches) is valid and not zero. See also [Ramification index (fit)](#schoenen-fitted)

- <span id="skewness"></span> **Skewness** The {% include wikipedia title='Skewness' text='skewness'%} of the sampled data, an indication of how symmetrical the distribution is around its mean. Positive values indicate an asymmetrical distribution with a longer tail to the right. Negative values indicate data with a longer tail to the left. A popular rule of thumb considers that if the skewness is greater than 1.0 (or less than -1.0), the distribution may be considered far from symmetrical. See also [Skewness (fitted data)](#skewness-fitted)

- <span id="sum"></span> **Sum of intersections (*Sum inters.*)** The sum of all intersections.

<br><br>
{% include img align="center" width="750px" src="/media/plugins/snt/sholl-metrics-overview.jpg" %}
Overview of Sholl metrics) based on curve fitting including the Sholl regression coefficient (k), Critical value (Nm), Critical radius (rc) and Mean value (Nav). Differences between sampled and fitted maxima are shaded in gray. The centroid of the sampled profile is marked (×). Schoenen ramification index (RI) is the ratio between number of branches at the maximum and the number of primary branches, using either sampled data or the fitted Nm. (Ferreira T, et al., 2014, [supplementary booklet](https://www.nature.com/articles/nmeth.3125#Sec2))
<br><br>

## Metrics based on fitted data

- <span id="bi-fitted">**Branching Index (*BI fitted*)** the [branching index](#bi) obtained from the fitted profile.

- <span id="critical-radius"></span> **Critical radius**  The distance at which *Critical value* occurs. By default, it is calculated with a precision of 1/1000 of *Radius step size*. Abbreviation: *r<sub>c</sub>*. See also [Max inters. radius](#max-inters-radius)

- <span id="critical-value"></span> **Critical value**  The local maximum of the polynomial fit, i.e, *N* at *Critical radius* in [(1)](#eq1). Abbreviation: *N<sub>m</sub>*. See also [Max inters.](#max-inters)

{% include notice icon="tip" content='**Nomenclature**: [Previous authors](#references) have used different terms to describe the largest value taken by the Sholl profile, including *Dendrite maximum*. Since the Sholl technique is not restricted to dendritic arbors and can be applied to any tree-like structure such as axonal arbors, mammary ducts or blood vessels (cf. [List of citations](#publication)), Here we adopt the term [Critical radius](#critical-radius), renaming *Dendrite maximum* (*N<sub>m</sub>*) to [Critical value](#critical-value).' %}

- <span id="dratio"></span> **Determination ratio**  The ratio of the [coefficient of determination](#reg-r2) for the semi-log method and that for the log–log method[^5]. If the semi-log method is better relatively to the log–log method, the *Determination ratio* becomes larger than 1. It is the parameter used by the plugin to silently predict the normalization method that is the [most informative](#choice-of-methods). The prediction can be monitored by selecting *Debug mode* in *Options and Preferences*.

- <span id="kurtosis-fitted"></span> **Kurtosis (*Kurtosis (fit)*)**  The [kurtosis](#kurtosis) of the fitted polynomial distribution between [Starting radius](#start-radius) and [Ending radius](#end-radius).

- <span id="mean-value-of-function"></span> **Mean value**  The mean value[^4] of the fitted polynomial function [(1)](#eq1), representing the average of intersections over the whole area occupied by the arbor. Abbreviation *N<sub>av</sub>*. On the Sholl plot, it is [highlighted](#sholl-plots) as the height of the rectangle that has the width of *Enclosing radius* − *First intersecting radius* and the same area of the area under the fitted curve on that discrete interval. It is analogous to [Mean inters.](#mean-inters), the arithmetic mean of sampled intersections throughout the arbor (cf. [Metrics based on sampled data](#metrics-based-on-sampled-data)). By default, (see [Advanced Usage](#advanced-usage)), it is calculated with a precision of 1/1000 of *Radius step size*.

- **Polynomial R<sup>2</sup> (*Polyn. R^2*)** The coefficient of determination of the polynomial fit described in [(1)](#eq1).

- **Regression intercept**  The y-coordinate *m* described in [(3)](#eq3) and [(4)](#eq4).

- <span id="reg-r2"></span> **Regression R<sup>2</sup> (*Regression R^2*)**  The coefficient of determination of the linear regression described in [(3)](#eq3) and [(4)](#eq4).

- <span id="schoenen-fitted"></span> **Schoenen Ramification index (*Ramification index (fit)*)** Schoenen Ramification index retrieved from fitted profile: The ration between [Critical value](#critical-value) and [Number of primary branches](#primary-branches). See also [Ramification index (sampled)](#schoenen-sampled)

- <span id="sholl-decay"></span> **Sholl regression coefficient (*Regression coefficient*)** The slope (multiplied by -1) of the linear regression described in [(3)](#eq3) and [(4)](#eq4), i.e., *k*, a measure of the rate of decay of the number of branches with distance from the center of analysis. Higher *k* values reflect larger changes in the function log(N/S). To optimize the fit, the plugin retrieves a [second linear regression](#sholl-plots) centered around the median distance, excluding distances at the edges of the profile. Details of this second fit are also registered on the [*Sholl table*](#metrics) under dedicated columns, e.g., *Sholl regression coefficient \[P10-P90\]*, when data within the 10<sup>th</sup>–90<sup>th</sup> percentile is used.

- <span id="skewness-fitted"></span> **Skewness (*Skewness (fit)*)**  The [skewness](#skewness) of the fitted polynomial distribution between [Starting radius](#start-radius) and [Ending radius](#end-radius).


## Metrics based on [Angular Sholl](#angular-sholl)

- <span id="adc">**Angle distribution coherence (*ADC*)** The evenness of the angular distribution of [Sholl data](#angular-sholl). Unitless, ranging from [0, 1], with higher values indicating Sholl data is concentrated around a [preferred direction](#preferred-direction); 0 indicates a uniform distribution across all directions.

- <span id="preferred-direction">**Preferred directions (*PD*)** The direction around which [Sholl data](#angular-sholl) is the most concentrated when [Angle distribution coherence](#adc) is high. Range: [0°,360°[. Examples: A space filling neuron is not expected to be associated with a prominent direction (low ADC value). On the other hand, a cell may have more than one preferred direction (e.g., data from dendrites of a pyramidal neuron), as exemplified [above](#angular-sholl).

- <span id="odc">**Orientation distribution coherence (*ODC*)** This is a variant of [Angle distribution coherence](#adc) that considers *orientation* as opposed to *direction*. ODC can be useful to discriminate morphologies that are symmetric across 180° (e.g., a neuronal arbor with two opposite tufts) for which ADC can be near 0

- <span id="preferred-orientation">**Preferred orientatiosn** The orientation around which [Sholl data](#angular-sholl) is the most concentrated when [Orientation distribution coherence](#odc) is high. Range: [0°,180°[

Similarly to all other Sholl-related profiles, both intersection counts and [intersecting lengths](#length-based-profiles) can be used, as well as data from polynomial fits. By default, polar heatmaps use an angular bin width of 10°. This sensitivity can be adjusted in the "Further Options" dialog in the analysis prompt.


# Complementary Tools

SNT provides several scripts and commands that facilitate all type of Sholl-related analyses. You'll find them through the {% include bc path='Plugins|Neuroanatomy|Neuroanatomy Shortcut Window'%} (SNT icon in the ImageJ toolbar), as well as in Script Editor's {% include bc path='Templates|Neuroanatomy|'%} menu.

{% capture tip%}
For more information on image processing routines have a look at [tutorials](/tutorials), [segmentation](/imaging/segmentation) and the [ImageJ User Guide](https://imagej.net/ij/docs/guide/) .
{% endcapture %}
{% include notice icon="tip" content=tip %}


# Pre-processing

This section discusses some aspects that should be taken into account when segmenting neuronal arbors to be processed by *Sholl Analysis*. Since *image segmentation* (i.e., the partitioning of images into analyzable parts) is vulnerable to noise and background fluorescence, it is not possible to generalize universal routines that efficiently binarize grayscale images. This means that any procedure that tries to appropriately describe the original fluorescence image with a binary mask must be tailored to the characteristics of individual datasets.


## Noise

Noise can be mitigated through the usage of processing filters. Specially useful are edge-preserving filters:
- [Tubeness](/plugins/tubeness) and [Frangi](/plugins/frangi), see SNT's [Secondary Layer Wizard](/plugins/snt/manual#tracing-on-secondary-image)
- [Rolling Ball](/plugins/rolling-ball-background-subtraction) or "Top hat" filters, e.g., {% include bc path="Process | Subtract Background..." %}
- Median Filtering (2D/3D), e.g., {% include bc path="Process | Filters |" %}, {% include bc path="Plugins | 3D |" %}
- [Anisotropic Diffusion](/plugins/anisotropic-diffusion-2d), {% include bc path="Plugins | Process | Anisotropic Diffusion 2D" %}
- Sobel Edge Detection, e.g., {% include bc path="Process | Find Edges" %}
- Shen-Castan Edge Detector ([BAR](/plugins/bar) plugin), {% include bc path="BAR | Segmentation |" %}
- Frequency filters, e.g., {% include bc path="Process | FFT | Bandpass Filter..." %}

## Uneven Illumination

Uneven illumination problems, typically associated with [wide field microscopy](http://imagejdocu.list.lu/doku.php?id=howto:working:how_to_correct_background_illumination_in_brightfield_microscopy), do occur in confocal microscopy when signal from deep layers of the tissue is not captured as bright as with superficial layers. This signal attenuation along the Z-axis will generate a shaded gradient across the stack that [histogram-based segmentation](#automated-segmentation) will need to take into account. While these problems are better tackled during acquisition (e.g., using laser ramping), it is possible to mitigate this effect using histogram-normalization techniques. E.g.:

- [Tubeness](/plugins/tubeness) and [Frangi](/plugins/frangi), see SNT's [Secondary Layer Wizard](/plugins/snt/manual#tracing-on-secondary-image)
- [Bleach Correction](/plugins/bleach-correction), {% include bc path="Image | Adjust |" %}
- [Attenuation correction](http://imagejdocu.list.lu/doku.php?id=plugin:stacks:attenuation_correction:start)

## Segmentation

It is possible to adopt more sophisticated [segmentation algorithms](/imaging/segmentation) when [global thresholding methods](/plugins/auto-threshold) do not yield satisfactory results. Examples:
- [Machine learning algorithms](machine-learning) (semantic segmentation)
- [Local Threshold](/plugins/auto-local-threshold), {% include bc path="Image | Adjust |" %}
- [Robust Automatic Threshold Selection](/plugins/rats), {% include bc path="Plugins | Segmentation |" %}
- [Level Sets](/plugins/level-sets), {% include bc path="Plugins | Segmentation |" %}
- [Morphological Segmentation](/plugins/morphological-segmentation), {% include bc path="Plugins | Segmentation |" %}
- [Squassh](/plugins/squassh), split-Bregman Image Segmentation (Segmentation and Quantification of Sub-cellular Shapes, [MOSAIC ToolSuite](/plugins/mosaicsuite), {% include bc path="Plugins|Mosaic|Segmentation|" %}
- [MorphoLibJ](/plugins/morpholibj)
- [BAR](/plugins/bar) scripts for manual curation of thresholded images, {% include bc path="BAR | [Segmentation](/plugins/bar#segmentation) |" %}


# Batch Processing

SNTv5 reinstated macro-recordable commands. So the easiest/quickest way to automate analysis requires only 3 steps:
1. Open ImageJ's macro recorder: {% include bc path="Plugins|Macro|Record..." %}
2. From the Neuroanatomy Shortcuts Window, choose the relevant prompt from the _Macro Recordable_ section of {% include bc path="Sholl Analysis | " %}
3. Set the options as usual
4. Copy the recorded string into your macro/script. Beware that the recorded expression is quite large. Make sure to avoid copy/paste errors. It should look something like:

{% highlight javascript %}
// NB: have a look at the example scripts in Templates>Neuroanatomy> for more robust ways to automate Sholl. E.g., Sholl_Extract_Profile_From_Image_Demo.py exemplifies how to parse an image programmatically using API calls
run("Sholl Analysis (From Image)...", "datamodechoice=Intersections startradius=0.0 stepsize=10.0 endradius=400.0 hemishellchoice=[None. Use full shells] previewshells=false nspans=1 nspansintchoice=N/A primarybrancheschoice=[Infer from starting radius] primarybranches=0 polynomialchoice=['Best fitting' degree] polynomialdegree=0 normalizationmethoddescription=[Automatically choose] normalizerdescription=Default plotoutputdescription=[Linear, normalized, and polar plots] tableoutputdescription=[Detailed & Summary tables] annotationsdescription=[ROIs (points and 2D shells)] lutchoice=Ice.lut save=true savedir=/Users/ferreirat analysisaction=[Analyze image]");
{% endhighlight %}


For more comprehensive functionality, the Script Editor's {% include bc path='Templates|Neuroanatomy|'%} menu lists demo scripts that perform batch operations. For sake of completeness, here is a small tutorial on how to write a macro from the ground up:

## Tutorial: Batch Analysis of Images using IJM Languages

Any macro must set a center, or allow the Sholl Analysis plugin to access a ROI marking it. One could instruct ImageJ to read the coordinates of pre-existing ROIs from a text file, store a list of line selections in the ROI Manager, or write a morphology-based routine that detects the center of the arbor. However, marking the center of analysis is probably something that you will want to do manually. Here is a workflow:

1.  Place all the .tif images to be processed in a single folder.
2.  Select the <span style="border-bottom:1px dotted #ccc;">Point Selection Tool</span> in the main ImageJ window. With 3D images, make sure *Set stack positions* is active in the {% include bc path="Image | Overlay | Overlay Options..." %} prompt.
3.  Open the first image and press {% include key keys='Shift|T' %} to activate the Threshold widget ({% include bc path="Image | Adjust | Threshold..." %}).
4.  Adjust threshold levels. Press the *Apply* button of the Threshold widget to create a binary image.
5.  Select the z-slice containing the center of analysis. Click over the center with the <span style="border-bottom:1px dotted #ccc;">Point Selection Tool</span> and press {% include key key='B' %} (shortcut for {% include bc path="Image | Overlay | Add Selection..." %}). This will add the point ROI to the image overlay. Save the image as .TIFF by pressing {% include key key='S' %} ({% include bc path="File | Save As... | Tiff..." %}).
6.  Repeat the last 2 steps until all images are marked, using {% include key keys='Shift|O' %} (shortcut for {% include bc path="File | Open Next" %}) to iterate through all the images.

{% capture roi-tiff-tip %}
When working with ROIs, it is critical that you work with .tif files because only this format keeps track of image overlays. IJ's {% include bc path="Process | Batch | Convert..." %} command allows bulk conversion between image formats.
{%- endcapture -%}
{% include notice icon="tip" content=roi-tiff-tip %}

Now that all the images are marked, we could use the Macro Recorder ({% include bc path="Plugins | Macros | Record..." %}) and run *Sholl Analysis* on one of the images to find out how to call the plugin with suitable parameters. In this tutorial, we will use the ImageJ macro language. The single line of code that appears in the recorder window will look something like this:

{% highlight javascript %}
// Recording Sholl Analysis version 3.4.3
run("Sholl Analysis...", "starting=10 ending=400 radius_step=0 infer fit linear polynomial=[8th degree] semi-log normalizer=Volume create save do");
{% endhighlight %}

As you may have noticed, ImageJ plugins are controlled by a single lowercase sentence in which arguments are separated by a space. Input fields and choice lists appear as *keyword=value* pairs, active checkboxes by a single keyword. Options that are not needed can be omitted. This makes it easier to edit code blocks:

{% highlight javascript %}
start = 10;  // variable that controls starting radius
end   = 200; // variable that controls ending radius
step  = 2;   // variable that controls step size

// Run the plugin
run("Sholl Analysis...", "starting="+ start +" ending="+ end +" radius_step="+ step +" infer linear save do");
{% endhighlight %}

Now we just need to assemble a working macro to be pasted in the {% include bc path="Process | Batch | Macro..." %} prompt:

{% highlight javascript %}
// Get the number of ROIs of the image overlay
nROIs = Overlay.size;
// We cannot proceed if no ROI is available (safety check)
if (nROIs==0)
    exit("No ROI was found. Cannot proceed.");
// Select the last ROI of the overlay. Because we have activated the "Set stack positions" option,
// this will automatically activate the Z-slice in which the ROI was created (3D images)
Overlay.activateSelection(nROIs-1);
// We now call the plugin as detailed by the Macro Recorder. We'll set 'Ending radius' to a non-numeric
// value (NaN, "Not a Value") to make sure the maximum length for each individual image is used
run("Sholl Analysis...", "starting=10 ending=NaN radius_step=0 infer fit linear polynomial=[8th degree] semi-log normalizer=Volume create save do");
{% endhighlight %}

Of course you can also automate any preceding steps. However, do not forget to ensure that the center of analysis will be available when the plugin is called:

{% highlight javascript %}
// Impose spatial calibration
run("Properties...", "unit=um pixel_width=1.5 pixel_height=1.5 voxel_depth=3.0");
// Subtract background
run("Subtract Background...", "rolling=50 sliding stack");
// Apply a favorite threshold
setAutoThreshold("Huang dark stack");
// >>>> Make sure the initial point selection remains available <<<<
Overlay.activateSelection( Overlay.size - 1 );
// Run the plugin
run("Sholl Analysis...", "starting=10 ending=NaN radius_step=0 infer fit linear polynomial=[8th degree] semi-log normalizer=Volume create save do");
{% endhighlight %}

That's it. Use the Macro Recorder to generate the customizations you will need before parsing the entire folder of images with {% include bc path="Process | Batch | Macro..." %}


## Examples:

More complex scripts will take advantage of [SNT's API](/plugins/snt/scripting). Here are some examples:

{% include code org='morphonets' repo='SNT' branch='master' path='src/main/resources/script_templates/Neuroanatomy/Analysis/Sholl_Extensive_Stats_Demo.groovy' label='Extensive Stats Demo (Groovy)' %}

{% include code org='morphonets' repo='SNT' branch='master' path='src/main/resources/script_templates/Neuroanatomy/Analysis/Sholl_Extract_Profile_From_Image_Demo.py' label='Extract Profile from Image (Python)' %}

# FAQ

**General**

<ol>
<li markdown="1">

<span id="faq:citing"></span>**How do I cite *Sholl Analysis***?

</li>
<dl>
<dd markdown="1">

The authoritative references for *Sholl Analysis* are twofold:

- {% include citation id='plugins/sholl-analysis' %}

- {% include citation id='plugins/snt' %}

</dd>
</dl>

<li markdown="1">

<span id="faq:threshold"></span>**Why do I need to threshold the cell?**

</li>
<dl>
<dd markdown="1">

Counting intersections is really a binary procedure: a shell either intercepts a branch or it doesn't. For this reason the image must be split in two phases: *arbor* and *background*.

</dd>
</dl>
<li markdown="1">

<span id="faq:threshold2"></span>**In older versions it was not mandatory to adjust threshold values prior to analysis. Why is it now?**

</li>
<dl>
<dd markdown="1">

Image segmentation has always been [required](#faq:threshold). In its early implementations, the program dealt solely with binary images and used the intensity at the center of the analysis to decide how to segregate objects from background. This approach was very stringent: It assumed that the pixels representing the neuron would have the same (constant!) intensity that was not to be found in the remaining background. As the program became aware of grayscale images, this "feature" had to be removed because a single intensity can no longer be used to infer which parts of the image should be analyzed.

</dd>
</dl>
<li markdown="1">

<span id="faq:pre-processing"></span>**My images do not look that *great*. How can I treat them prior to analysis?**

</li>
<dl>
<dd markdown="1">

Have a look at [ Pre-processing](#pre-processing).

</dd>
</dl>
<li markdown="1">

<span id="faq:accuracy"></span>**My bitmap profiles are different from the ones obtained from tracings of the same cells. Why?**

</li>
<dl>
<dd markdown="1">

The quality of the analysis relies on how the arbor was segmented. If you are working with grayscale images you probably need to optimize your [segmentation routines](#pre-processing). On the other hand, if you already obtained binary images make sure you are [interpreting them properly](#cf-segmentation). You should also confirm that [Ending radius](#end-radius) does not intersect objects in the image canvas that extend beyond the analyzed arbor. As a rule of thumb, always refer to the [Sholl mask](#faq:sholl-mask) to visually inspect which regions of the image have been measured.

</dd>
</dl>
<li markdown="1">

<span id="faq:updates"></span>**My version is not the latest after running {% include bc path="Help | Update Fiji..." %} Why?**

</li>
<dl>
<dd markdown="1">
This may happen if you have manually installed/modified core files.. Run the [Updater](/plugins/updater), choose *Advanced Mode* then *View locally modified files* under *View Options*. Locate files from the *Neuroanatomy* update site. If the *Details pane* indicates an available update, click on *Locally modified* under *Status/Action* and choose *Install/Update*. The latest release version will be available once you press *Apply changes*. See [Installation FAQs](/learn/faq#installingupdating) for more details.
</dd>
</dl>
<li markdown="1">

<span id="faq:documentation"></span>**This documentation is not that useful. How long do I have to wait until it gets improved?**

</li>
<dl>
<dd markdown="1">

Use the Edit this page option on the [top](#top) of the page and edit its contents at will. Don’t be shy. All changes are undoable!

</dd>
</dl>
</ol>

**Analysis**

<ol>
<li markdown="1">

<span id="faq:image-types"></span>**The plugin complains about a wrong image type. Why?**

</li>
<dl>
<dd markdown="1">

The plugin does not parse RGB images, but will process any grayscale image (8/16-bit), including multichannel (composite) images. This is intentional: RGB images are inflexible and images of fluorescence-labeled cells are typically non-RGB images. As explained in the [ImageJ User Guide](https://imagej.net/ij/docs/guide/), RGB images can be converted using {% include bc path='Image|Color|Channels Tool...'%} or {% include bc path='Image|Type|'%} commands.

</dd>
</dl>
<li markdown="1">

<span id="faq:z-position"></span>**With 3D and 4D images, how do I set the Z-position and of the center?**

</li>
<dl>
<dd markdown="1">

The Z-position (depth) of the center of analysis is the active Z-slice of the stack. With multichannel (composite) images, the active channel also defines the C-position. Both are reported in the *Sholl Results* table.

</dd>
</dl>
<li markdown="1">

<span id="faq:parameters"></span>**Why so many parameters?**

</li>
<dl>
<dd markdown="1">

The plugin is designed for the analysis of a wide diversity of arbors and it is not biased to any particular cell type. The only way to ensure this broad applicability is to give users full control over the mathematical techniques used by the plugin to analyze sampled data.

</dd>
</dl>
</ol>

**Results**

<ol>
<li markdown="1">

<span id="faq:Sholl-table"></span>**How can I save/edit the *Sholl Results* table?**

</li>
<dl>
<dd markdown="1">
Use Fiji's {% include bc path="File | Export | Table..." %} command or SNT's {% include bc path="File | Save Tables and Analysis Plots.." %} ([details](/plugins/snt/manual#save-tables--analysis-plots)). Single cells cannot be modified from within ImageJ, but custom extensions (e.g., .csv, .xls or .ods) will allow the table to be imported by other spreadsheet applications.

</dd>
</dl>
<li markdown="1">

<span id="faq:sholl-mask"></span>**What is the *Sholl mask*?**

</li>
<dl>
<dd markdown="1">

The Sholl mask ([see example of CA1 cell](#ca1-cell-mask)) is simply an illustration: a maximum intensity projection of the analyzed cell in which [intersection counts](#output-options) are used as pixel intensities. As explained in [Output Options](#output-options), its LUT can be modified, and intensities calibrated using ImageJ default commands. As mentioned, it can also be used to visually inspect for [segmentation artifacts](#cf-segmentation).

</dd>
</dl>
<li markdown="1">

<span id="faq:3Dvs2D"></span>**The 3D profile looks *worse* than the 2D profile of the Maximum Intensity Projection of the same cell. Why?**

</li>
<dl>
<dd markdown="1">

An anisotropic voxel size will have a strong impact on [step size](#step-size). On the other hand, 2D and 3D images can be sampled differently depending on the [options chosen](#parameters). If {% include bc path="Image | Properties..." %} ({% include key keys='Shift|P' %}) reports the appropriate spatial calibration, make sure to read [Multiple Samples and Noise Reduction](#multiple-samples-and-noise-reduction) before deciding which type of images to use.

</dd>
</dl>
<li markdown="1">

<span id="faq:no-output"></span>**The program terminates without warnings. What am I doing wrong?**

</li>
<dl>
<dd markdown="1">

The program should not terminate without throwing an error message. However, do note that some exiting messages are displayed in the often overlooked status bar of the main ImageJ window. This is intentional, as it minimizes the frequency of modal windows popping up for each failed operation.

</dd>
</dl>
</ol>

**Metrics and Curve Fitting**
<ol>
<li markdown="1">

<span id="faq:AUC"></span>**Would it be possible to retrieve the Area Under the Curve (linear Sholl plot)?**

</li>
<dl>
<dd markdown="1">

Sure. But it would hardly be relevant for data sampled at fixed intervals. The area under the curve (AUC, the area between the sampled curve and the horizontal axis, i.e., its definite integral) could be estimated using, e.g., the {% include wikipedia title='Trapezoidal rule' text='trapezoidal rule'%}. However, because data is always sampled at equally spaced intervals, doing so would be the same as multiplying [Mean inters.](#mean-inters) by the distance between [Ending radius](#end-radius) and [Starting radius](#start-radius). Thus, effectively, AUC is redundant with [Mean inters.](#mean-inters), that is already an integrated measurement of the sampled data. On the other hand, one could retrieve the AUC of the polynomial fit, but such property is already covered by [Mean value](#mean-value-of-function).

</dd>
</dl>
<li markdown="1">

<span id="faq:inflection-points"></span>**The shape of the polynomial changes at the edges of the profile. Why?**

</li>
<dl>
<dd markdown="1">

Inflection points at [starting/ending radius](#start-radius) are usually associated with a poor fit and/or the fact that all the radii in which no intersections were counted are ignored. The latter is required to calculate the [Sholl regression coefficient](#sholl-decay), as *log(0)* is undefined.

</dd>
</dl>
<li markdown="1">

<span id="faq:poor-fitting"></span>**None of the fitting options is suitable for my datasets. What should I do?**

</li>
<dl>
<dd markdown="1">

Have a look at [Complementary Tools](#complementary-tools).

</dd>
</dl>
</ol>

**Batch Processing**
<ol>
<li markdown="1">

<span id="faq:recorder"></span>**The code that the Macro Recorder produced does not seem to work. What am I doing wrong?**

</li>
<dl>
<dd markdown="1">

It is likely that frequent interactions with the dialog prompt(s) (from which the Recorder retrieves user-specified parameters) have "confused" ImageJ. The solution is to repeat the recording, while minimizing such interactions.

</dd>
</dl>
</ol>

**Development**
<ol>
<li markdown="1">

<span id="faq:bug-report"></span>**I found a bug. How do I report it?**

</li>
<dl>
<dd markdown="1">
Report it in the [ImageJ Forum](http://forum.imagej.net).
</dd>
</dl>
</ol>

<span id="release-notes"></span>
# Version History

Release notes are available on the {% include github org='morphonets' repo='SNT' label='SNT repository' %}. Releases notes up to version 3.7.3 are available on an {% include github org='tferr' repo='ASA' branch='master' path='Notes.md#release-notes-for-sholl-analysis' label='older repository' %}. In turn, the latter inherited (with permission) the 2D algorithm of an even earlier [ImageJ 1.35 plugin](http://web.archive.org/web/20140216075253/http://labs.biology.ucsd.edu/ghosh/software/) by Tom Maddock. Note that throughout 2012 the project was temporarily called *Advanced Sholl Analysis*.


# Publication

{% include citation %}

Citing manuscripts can be retrieved using [Scholar](https://scholar.google.com/scholar?cites=15441574333602897335&as_sdt=2005&sciodt=1,5&hl=en) or [PubMed](http://www.ncbi.nlm.nih.gov/pmc/articles/pmid/25264773/citedby/?tool=pubmed), although many [more publications seem to be using it](https://scholar.google.com/scholar?hl=en&as_sdt=1%2C5&as_vis=1&q=fiji+AND+%22Sholl+Analysis%22&btnG=). See [Global FAQs](/plugins/snt/faq#how-do-i-cite-snt) for details on how to cite SNT.


# References

[^2]: Sholl DA. Dendritic organization in the neurons of the visual and motor cortices of the cat. J Anat. 1953 Oct;87(4):387-406. [PMID: 13117757](http://www.ncbi.nlm.nih.gov/pubmed?term=13117757)

{% include citation fn=3 doi='10.1016/j.jneumeth.2006.05.030' %}

{% include citation fn=4 doi='10.1016/0306-4522(82)90120-8' %}

{% include citation fn=5 doi='10.1016/j.jtbi.2006.09.022' %}

{% include citation fn=6 doi='10.1007/s12021-010-9095-5' %}

{% include citation fn=7 doi='10.1016/j.jneumeth.2014.01.016' %}

{% include citation fn=8 doi='10.1111/j.1460-9568.2010.07283.x' %}
