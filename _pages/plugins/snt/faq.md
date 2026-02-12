---
title: SNT › FAQ
nav-links: true
nav-title: FAQ
artifact: org.morphonets:SNT
icon: /media/icons/snt.png
forum-tag: snt
update-site: Neuroanatomy
---

## General

### How do I install SNT?

See [Installation details](/plugins/snt/index#installation).

### How do I cite SNT?

**Note that neither the main [Fiji article](/software/fiji#publication), nor the first [Simple Neurite Tracer](#what-is-the-difference-between-snt-and-simple-neurite-tracer) publication are appropriate citations for SNT. The proper citation for SNT is**:

- {% include citation id='plugins/snt' %}

In addition, you should also cite any additional modules that you may use:

- **[Sholl Analysis](/plugins/snt/sholl)**
  {% include citation id="plugins/sholl-analysis" %}
- **[Cx3D](/plugins/snt/modeling)**
  {% include citation doi="10.3389/neuro.10.025.2009" %}
- **[Tubular Geodesics](/plugins/snt/extending#tubular-geodesics)**
  {% include citation doi='10.1109/cvpr.2012.6247722' %}


### What is the difference between SNT and Simple Neurite Tracer?

Simple Neurite Tracer was the first Fiji plugin dedicated to visualization and reconstruction of neurons, developed by [Mark Longair](/people/mhl) and [published in 2011](https://doi.org/10.1093/bioinformatics/btr390), to become the single most cited open-source software for semi-automated 3D reconstructions. In the wake of ImageJ2 development, a new team of developers led by [Tiago Ferreira](/people/tferr) took on the effort of modernizing its code base. The project quickly snowballed beyond the re-write of the software, and focused on establishing a complete framework for reconstruction, visualization, quantification and modeling of neuronal morphology. Several name changes were proposed for this "next-gen" Simple Neurite Tracer (*Not so Simple Neurite Tracer*, *Smart Neurite Tracer*, *Super Neurite Tracer* to name a few), but in the end it was decided to adopt the acronym of the original software, as an homage to Mark's outstanding work. You can follow the entire history of the plugin on GitHub: Simple Neurite Tracer's {% include github org='fiji' repo='Simple_Neurite_Tracer' label='historic' %} and SNT's {% include github org='morphonets' repo='SNT' label='current' %} repositories.

### How accurate is SNT?

When SNT is compiled, a [suite of tests](https://github.com/morphonets/SNT/tree/-/src/test/java/sc/fiji/snt) is run to detect deficiencies in the code base. Morphometry results are benchmarked against values obtained in [L-Measure](http://cng.gmu.edu:8080/Lm/) and [NeuroM](https://github.com/BlueBrain/NeuroM). However, no test suite is ever perfect. If you detect inaccuracies, please {% include github org='morphonets' repo='SNT' label='report' %} them\!

### What is a SWC file?
<span id="swc"></span>
It is the most widely adopted format for encoding neuronal reconstructions, in which information is stored in plain text. It was first described by (Cannon et al., 1998) and since then became a somewhat loose *lingua franca* of a neuron's three-dimensional structure. The latest [SWC specification](https://swc-specification.readthedocs.io/en/latest/index.html) provides more details about the format. SNT supports all known variants of the format including [ESWC](https://www.nature.com/articles/sdata2017207), [SWC+](https://neuroinformatics.nl/swcPlus/), and latest [specification](https://swc-specification.readthedocs.io/en/latest/index.html) (v1.0.3, as of this writing). The extension stems from the last names of Stockley, Wheal, and Cole, who developed a neat computer system for reconstructing neuronal cells ( Stockley et al., 1993). Confusingly, an unrelated {% include wikipedia title="Adobe SWC file" %} format also used to exist.

### In which format should I save my tracings: TRACES or SWC?
<span id="file-format"></span>
When tracing 4D or 5D images, TRACES is preferable because the channel and/or time frame associated with the data are stored. With simpler 2/3D images TRACES is also preferable to preserve [Path Manager tags](/plugins/snt/manual#tag) across restarts. Note that the {% include bc path='[Scripts](/plugins/snt/manual#scripts)| '%} menu provides a [batch converter](#convert) for TRACES → SWC conversion. The following table summarizes the differences between the two formats:

|                                              | **SWC**                                                                                                                              | **TRACES**                                                                                  |
|----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| No. reconstructions per file                 | Formally only one. When multiple reconstructions exist, SNT splits them across multiple files appending unique suffixes to filenames | Multiple reconstructions per file allowed                                                   |
| Image metadata                               | Formally none. SNT stores the spatial calibration of the image in the header                                                         | Rich. Including channel and frame of the traced structure.                                  |
| [Path Manager tags](/plugins/snt/manual#tag) | Not stored                                                                                                                           | Stored                                                                                      |
| [Fits](/plugins/snt/manual#refinefit)        | Not stored, unless fitting replaces existing nodes                                                                                   | Stored                                                                                      |
| [Fills](/plugins/snt/manual#fill)            | Not stored                                                                                                                           | Filling parameters stored                                                                   |
| Format                                       | Plain text                                                                                                                           | XML or compressed XML (as per [preferences](/plugins/snt/manual#misc))                      |
| Presence                                     | Ubiquitous among reconstruction software. The *de facto* standard in data sharing                                                    | Exclusive to SNT. But [open and easily parsable](/plugins/snt/extending#traces-file-format) |

### Which file formats for neuronal reconstruction are supported by SNT?
SNT can read TRACES, SWC, NDF (NeuronJ data format), and JSON files (as used by the [MouseLight](https://ml-neuronbrowser.janelia.org/) project). Other file formats can be converted to [SWC](#swc) using [xyz2swc](https://neuromorpho.org/xyz2swc/ui/).

### My neuronal reconstructions are saved under a format that is not supported. How can I open them?
Unsupported and proprietary file formats can be converted to [SWC](#swc) using [xyz2swc](https://neuromorpho.org/xyz2swc/ui/).

### Which image file formats are supported by SNT?
Any file format supported by ImageJ/Bio-Formats with up to 5 dimensions. RGB images are strongly discouraged and are converted to multichannel before loading.

### How do I (batch) convert TRACES to SWC?
Use the {% include bc path='Batch|Convert Traces to SWC'%} script either from the Scripts menu in the main dialog, or the {% include bc path='Templates|Neuroanatomy|'%} menu in the Script Editor.

### How can I improve SNT documentation?
Use the *Edit this page* option on the <a href="#top">top</a> of the documentation page and edit its contents at will. Don't be shy. All changes are undoable\!


## Tracing

### Can I trace in 3D?
Yes. You can trace using the the XY,ZY,XZ [views](/plugins/snt/walkthroughs#accurate-point-placement) or more interactively: using the [3D Viewer](/plugins/snt/manual#legacy-3d-viewer) (legacy), or [sciview](/plugins/snt/manual#sciview) (experimental). There is also growing support for [Big Volume Viewer](/plugins/snt/manual#big-volume-viewer).

### Having to confirm individual segments is too cumbersome. Is it possible to trace without interruption, by clicking in succession?
Yes. Uncheck the *Confirm temporary segments* in the *Options* tab (*Temporary Paths* section).

### How can I browse voxel intensities around processes?
Right-click on the image canvas and select *Pause SNT* from the contextual menu. Voxel intensities will be reported in the ImageJ status bar.
Alternatively, you can also obtain [Path profiles](/plugins/snt/manual#path-profiler), in which voxel intensities are plotted along selected path(s).

### I traced an image in pixel coordinates but need to scale the reconstruction to physical units. How do I do it?
Have a look at [these instructions](https://forum.image.sc/t/how-to-set-the-correct-scale-micrometer-um-of-traced-cell-in-sholl-analysis/84764/4)

### Is there a way to process one image after another in a fast way?
Yes. Have a look at these [instructions](https://forum.image.sc/t/simple-neurite-tracer-for-multiple-2d-images/22564/6?u=tferr).

### How can I import an image sequence into SNT?
Loading of images that require input options is handled by ImageJ directly. To load a directory of images (e.g., one file per Z-slice), run {% include bc path='File| Import|Image Sequence' color='white'%} and select the first file in the sequence, adjusting any needed parameters in the subsequent dialog prompt. Once the sequence is imported adjust voxel dimensions using {% include bc path='Image|Properties...' color='white'%}. To save yourself from having to go through these steps again, you should save the imported stack as a single TIFF file using {% include bc path='File|Save As|Tiff...' color='white'%}

## Sholl Analysis
See [Sholl Analysis › FAQ](./sholl#faq).


## Spine Analysis

### Does SNT support spine analysis?
Currently only [Spine densities](./walkthroughs#spinevaricosity-analysis) are supported. In-depth quantification of spine morphology can be done using [Spot Spine](/plugins/spot-spine), after tracing dendrites in SNT.


## Soma Analysis

### Can SNT reconstruct somata?
Currently SNT favors the [single-point soma representation](https://neuromorpho.org/SomaFormat.html). The task of soma segmentation is better tackled using ImageJ built-in tools for analysis of contours, or by means of dedicated machine-learning tools, including:

| **Tools**                                       | **Fiji Integration**                                                                                    | **Resources**                                                                               |
|-------------------------------------------------|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| [Labkit](../labkit) and [TWS](../tws)           | Bundled with Fiji                                                                                       | [SNT › Machine Learning](./machine-learning), [Forum](https://forum.image.sc/tag/labkit)    |
| [Cellpose](https://www.cellpose.org/)           | Via [PTBIOP](https://wiki-biop.epfl.ch/en/ipa/fiji/update-site) update site                             | [Documentation](https://github.com/BIOP/ijl-utilities-wrappers?tab=readme-ov-file#cellpose), [Forum](https://forum.image.sc/tag/cellpose)|
| [StarDist](https://github.com/stardist/stardist)| Via [PTBIOP](https://wiki-biop.epfl.ch/en/ipa/fiji/update-site)/[CSBDeep](/plugins/csbdeep) update sites| [Documentation](https://github.com/BIOP/ijl-utilities-wrappers?tab=readme-ov-file#stardist), [Forum](https://forum.image.sc/tag/stardist)|
