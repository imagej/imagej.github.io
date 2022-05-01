---
mediawiki: SNT:_FAQ
title: SNT › FAQ
nav-links: true
nav-title: FAQ
---

## General

### How do I install SNT?

See [Installation details](/plugins/snt/index#installation).

### How do I cite SNT?

- {% include citation id='plugins/snt' %}

To reference specific modules/plugins that enhance SNT:

- **[Sholl Analysis](/plugins/sholl-analysis)**
  {% include citation id="plugins/sholl-analysis" %}
- **[Tubular Geodesics](/plugins/snt/tubular-geodesics)**
  {% include citation id="plugins/snt/tubular-geodesics" %}
- **[Cx3D](/plugins/snt/modeling)**
  {% include citation id="plugins/snt/modeling" %}

The original [Simple Neurite Tracer](#snt) publication is:

- {% include citation id='plugins/simple-neurite-tracer' %}

### What is the difference between SNT and Simple Neurite Tracer?

Simple Neurite Tracer was the first Fiji plugin dedicated to visualization and reconstruction of neurons, developed by [Mark Longair](/people/mhl) and [published in 2011](#citing), to become the single most cited open-source software for semi-automated 3D reconstructions. In the wake of ImageJ2 development, a new team of developers lead by [Tiago Ferreira](/people/tferr) took on the effort of modernizing its code base. The project quickly snowballed beyond the re-write of the software, and focused on establishing a complete framework for reconstruction, visualization, quantification and modelling of neuronal morphology. Several name changes were proposed for this "next-gen" Simple Neurite Tracer (*Not so Simple Neurite Tracer*, *Smart Neurite Tracer*, *Super Neurite Tracer* to name a few), but in the end it was decided to adopt the acronym of the original software, as an homage to Mark's outstanding work. You can follow the entire history of the plugin on GitHub: Simple Neurite Tracer's {% include github org='fiji ' repo='Simple_Neurite_Tracer' label='historic ' %} and SNT's {% include github org='morphonets ' repo='SNT ' label='current ' %} repositories.

### How accurate is SNT?

When SNT is compiled, a [suite of tests](https://github.com/morphonets/SNT/tree/master/src/test/java/sc/fiji/snt) is run to detect deficiencies in the code base. Morphometry results are benchmarked against values obtained in [L-Measure](http://cng.gmu.edu:8080/Lm/) and [NeuroM](https://github.com/BlueBrain/NeuroM). However, no test suite is ever perfect. If you detect inaccuracies, please {% include github org='morphonets ' repo='SNT ' label='report ' %} them\!

### What is a SWC file?

It is the most widely adopted format for encoding neuronal reconstructions, in which information is stored in plain text. It was first described by (Cannon et al., 1998) and since then became a somewhat loose *lingua franca* of a neuron's three dimensional structure. It is described in more detail [here](http://www.neuronland.org/NLMorphologyConverter/MorphologyFormats/SWC/Spec.html) and [here](https://neuroinformatics.nl/swcPlus/). SNT supports all known variants of the format including [ESWC](https://www.nature.com/articles/sdata2017207) and [SWC+](https://neuroinformatics.nl/swcPlus/). The extension stems from the last names of Stockley, Wheal, and Cole, who developed a neat computer system for reconstructing neuronal cells ( Stockley et al., 1993). Confusingly, it is also a {% include wikipedia title="Adobe SWC file" %} used by Adobe.

### In which format should I save my tracings: TRACES or SWC?

When tracing 4D or 5D images, `TRACES` is preferable because the channel and/or time frame associated with the data are stored. With simpler 2/3D images `TRACES` is also preferable to preserve [Path Manager tags](/plugins/snt/manual#tag) across restarts. Note that the {% include bc path='[Scripts](/plugins/snt/manual#scripts)| '%} menu provides a [batch converter](#convert) for `TRACES` → `SWC` conversion. The following table summarizes the differences between the two formats:

|                                                   | SWC                                                                                                                                  | TRACES                                                                               |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| No. reconstructions / file                        | Formally only one. When multiple reconstructions exits, SNT splits them across multiple files appending unique suffixes to filenames | Multiple reconstructions per file allowed                                            |
| Image metadata                                    | Formally none. SNT stores the spatial calibration of the image in the header                                                         | Rich. Including channel and frame of the traced structure.                           |
| [Path Manager tags](/plugins/snt/manual#tag) | Not stored                                                                                                                           | Stored                                                                               |
| Format                                            | Plain text                                                                                                                           | XML or compressed XML (as per [preferences](/plugins/snt/manual#misc))          |
| Presence                                          | Ubiquitous among reconstruction software. The *de facto* standard in data sharing                                                    | Exlusive to SNT. But [open and easily parsable](/plugins/snt/traces-file-format) |

### How do I (batch) convert TRACES to SWC?

In the [Script Editor](/scripting/script-editor) ({% include bc path='File|New|Script...'%}) look for {% include bc path='Templates|Neuroanatomy|Batch|Convert Traces to SWC'%} and run it. Note that all of SNT scripts are also listed in the main as regular GUI commands in the main [interface](/plugins/snt/scripting#script-templates). Don't see the scripts? Please ensure SNT is properly [installed](/plugins/snt#installation).

### How can I improve SNT documentation?

[Create an account](/editing#new-accounts) on this wiki. Once you have created one, you can edit contents at will. Don't be shy. All changes are undoable\!

## Tracing

### Having to confirm indivual segments is too cumbersome for me. Is it possible to trace without interruption, by clicking in succession?

Yes. Uncheck the *Confirm temporary segments* in the *Options* tab (*Temporay Paths* section).

### How can I browse voxel intensities around processes?

Righ-click on the image canvas and select *Pause SNT* from the contextual menu. Voxel intensities will be reported in the ImageJ status bar.

### Is there a way to process one image after another in a fast way?

Yes. Have a look at these [detailed instructions](https://forum.image.sc/t/simple-neurite-tracer-for-multiple-2d-images/22564/6?u=tferr).

### How can I import an image sequence into SNT?

Loading of images that require input options is handled by ImageJ directly. To load a directory of images (e.g., one file per Z-slice), run {% include bc path='File| Import|Image Sequence' color='white'%} and select the first file in the sequence, adjusting any needed parameters in the subsequent dialog prompt. Once the sequence is imported adjust voxel dimensions using {% include bc path='Image|Properties...' color='white'%}. To save yourself from having to go through these steps again, you should save the imported stack as a single TIFF file using {% include bc path='File|Save As|Tiff...' color='white'%}
