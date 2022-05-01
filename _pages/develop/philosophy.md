---
title: Philosophy
section: Extend:Development
project: /libs/scijava
---

[SciJava](/libs/scijava) projects are developed according to certain biases, which we describe here. This philosophy has evolved over a very long development history, reflecting many lessons learned over a course of decades.

## Open source

The SciJava ecosystem is strongly committed to [open source](/licensing/open-source) software development. But this software is not an [open source](/licensing/open-source) software *product*—it is an [open source](/licensing/open-source) software *project* following an [open source](/licensing/open-source) development *process*.

These projects are funded by taxpayer money, so the project strives to be as transparent as possible. There are public [source code repositories](/develop/source), public [communication](/discuss/#ways-to-get-help) channels, public [project management](/develop/project-management) resources, and of course, this [community editable website](/editing). As you can see, we love [doing it in public](http://blog.codinghorror.com/how-to-stop-sucking-and-be-awesome-instead/)!

## Independent learning

> Tell me and I forget. Teach me and I remember. Involve me and I learn. —{% include wikipedia title='Xun Kuang' text='Xunzi'%}

These projects are intended to foster not only scientific *independent thinking*, but just as importantly, *[independent learning](http://conference.imagej.net/2015/pariksheet-nanda/transcript.pdf)*. We want to not only [teach people how to fish](https://en.wiktionary.org/wiki/give_a_man_a_fish_and_you_feed_him_for_a_day;_teach_a_man_to_fish_and_you_feed_him_for_a_lifetime), but *teach them how to learn*.

As such, responses to questions on [public channels](/discuss/#ways-to-get-help) will often begin with "What have you tried?" or "Can you make a minimal, complete, verifiable example?"—see the [Bug reporting best practices](/discuss/bugs#bug-reporting-best-practices) for details. A good rule of thumb for questioners is to "put as much effort into your question as you expect to be put into its reply"—and for responders, to cordially encourage this behavior in questioners. Responses may give detailed macro or script solutions to image analysis questions, but they will also often include details of *how such solutions were produced*, as well as *how they might be improved or tailored to other similar scenarios*.

We are always looking for more ways to improve the software to meet this goal of encouraging independent learning. Write to the [Image.sc Forum](/discuss) with your ideas!

## Extensibility

[Extensibility](/develop/architecture#extensibility) is [ImageJ](/software/imagej)'s greatest strength. [ImageJ2](/software/imagej2) is not just a software application—it is an extensible *platform* for the development of image [visualization](/imaging/visualization), [segmentation](/imaging/segmentation), [registration](/imaging/registration), and analysis routines.

Isaac Newton attributed his success to {% include wikipedia title='Standing on the shoulders of giants' text='standing on the shoulders of giants'%}. The [SciJava component collection](/develop/architecture)'s powerful [plugin](/plugins) mechanism and [open source](/licensing/open-source) software process codify that metaphor into the software itself. Not only are there many different types of plugins, but it is also possible to extend the system with your own new types of plugins. See the [Extensibility](/develop/architecture#extensibility) page for details.

## Interoperability

One of the central goals of the [SciJava component collection](/develop/architecture) is to extend Java's mantra of "write once, run anywhere" in new directions: [ImageJ Ops](/libs/imagej-ops) for image processing algorithms, and [SCIFIO](/libs/scifio) for scientific image I/O.

[ImageJ2](/software/imagej2) commands work not only in the user interface, but also from many [other applications](/software) in the [SciJava ecosystem](SciJava), including [CellProfiler](/software/cellprofiler), [OMERO](/software/omero), [KNIME](/software/knime) and [Alida](/software/alida).

## Compatibility

Backward compatibility is one of ImageJ2's most important goals. It must remain possible to use existing [plugins](/plugins) and [macros](/scripting/macro) with new versions of ImageJ. See the [Compatibility](/libs/imagej-legacy) page for details.

## Release early, release often

{% include aside title="What's the alternative?" content="
Some projects opt to release their entire software stack in a ***big bang*** with a single monolithic version number. This has one extremely nice ramification: it clearly communicates which versions of which software components are intended to be compatible with one another.

For example, the [OME](/software/omero) project (which includes [OMERO](/software/omero) and [Bio-Formats](/formats/bio-formats)) employed this approach to versioning and release management for many years. Before each release, the OME team would perform careful and thorough integration testing of all components.

ImageJ and Fiji, in contrast, use the ***RERO*** style of releases, with compatible component versions declared in a [Bill of Materials](/develop/architecture#bill-of-materials) (BOM). Releases can happen more frequently, but consumers must take care to consult the BOM when combining various components together, or else there might be *version skew*.

| *Versioning*            | **BOM**                                                                                                    | **Monoversioned**                                  |
|-------------------------|------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| *Releases*              | **Release early, release often (RERO)**                                                                    | **Big bang**                                       |
| *Version compatibility* | Compatible components are declared in a [Bill of Materials](/develop/architecture#bill-of-materials) (BOM) | Compatible components have the same version number |
| *Frequency of releases* | Faster                                                                                                     | Slower                                             |
| *Stability*             | Less                                                                                                       | More                                               |
" -%}

ImageJ subscribes to the {% include wikipedia title='Release early, release often' text='release early, release often' %} (RERO) mantra often cited in software engineering circles. In particular—and especially because there is a small core development team—the project is driven by [Boyd's Law of Iteration](http://blog.codinghorror.com/boyds-law-of-iteration/): **speed of iteration beats quality of iteration**. That is not to say that we do not strive for quality—we do. But we have found through experience that more releases, together with guiding user feedback, push a project forward more efficiently than a slower release cycle does.

To ensure releases can happen quickly, each SciJava component is independently released and versioned, using [reproducible builds](/develop/architecture#reproducible-builds) with a "release ready" `master` branch. This allows individual SciJava components to be released with the [push of a button](/develop/travis), in a *timespan less than five minutes*. This puts bug-fixes into the hands of users as quickly as possible.

## Convention over configuration

With increased [modularity](/develop/architecture#modularity) often comes increased complexity. One key way of addressing this issue is to provide sensible defaults (e.g., the [big green Xerox button](http://athinkingperson.com/2010/06/02/where-the-big-green-copier-button-came-from/)) as a way of dealing with complex software programs. We embrace the philosophy of {% include wikipedia title='Convention over configuration' text='convention over configuration'%} utilized by many large software projects in recent years. For this reason, SciJava projects use the [Maven](/develop/maven) build tool for [project management](/develop/project-management).

## Why Java?

While it was once true that Java is always slower than the equivalent in C++, this is no longer the case. [There have been](http://paulbuchheit.blogspot.com/2007/06/java-is-faster-than-c.html) quite [a few benchmarks](http://vanillajava.blogspot.com/2011/08/java-can-be-significantly-faster-than-c.html) comparing Java vs C++ performance, [this one](http://keithlea.com/javabench/) probably being the grandfather of all.

Pragmatically, one should note that there is not really a big difference in performance when comparing Java to C++.

Java programs run without trouble and without recompiling on the major platforms: Windows, macOS and Linux. And plugins compiled on one platform also execute on all other platforms without recompiling. And profiling and debugging is easier with Java than with C++. And all programs/plugins double as libraries.

So the true reason why we use Java is probably: it makes [ImageJ](/software/imagej) accessible.

See also [LOCI's Why Java page](https://uw-loci.github.io/why-java).
