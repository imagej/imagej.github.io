---
mediawiki: 2017-05-30_-_Comprehensive_updates
title: 2017-05-30 - Comprehensive updates
categories: [News,Fiji]
---

Today, a lot of work on [ImageJ](/software/imagej), [Fiji](/software/fiji) and [SciJava](/libs/scijava) came to fruition all at once.

## ImageJ in Jupyter notebooks

The most exciting news is that, as [announced on the ImageJ forum](http://forum.imagej.net/t/jupyter-notebook-for-imagej/5421), there is now a {% include github org='hadim' repo='scijava-jupyter-kernel' label='SciJava Jupyter Kernel' %} enabling ImageJ to be used with [Jupyter Notebook](https://jupyter.org/) in all of the [supported scripting languages](/scripting#supported-languages).

Please peruse the [ImageJ Tutorial notebooks](/tutorials) for examples of this kernel in action!

## Sweeping component updates

Nearly all components of the [ImageJ software stack](/develop/architecture#definitions), as well nearly all [Fiji](/software/fiji) plugins, saw new releases [unifying and updating metadata](http://forum.imagej.net/t/split-boms-from-parent-configuration/2563) to better document [who is responsible for maintaining each component of the software](/contribute/governance#scijava-team-roles). This metadata update has been in the works for more than 18 months; the next step will be to [autogenerate the sidebars of component wiki pages](https://github.com/scijava/mediawiki-maven-info) so that plugin authors no longer need to manually keep wiki pages in sync. For technical details, see {% include github org='fiji' repo='fiji' issue='121' label='fiji/fiji\#121' %}.

This update also brings Fiji much closer to complete synchronization with the {% include github org='fiji' repo='fiji' label='fiji/fiji' %} source repository. Historically, there have been differences between the exact versions of components specified in the Fiji sources, versus those actually present on the Fiji update site at any given time. But we have been working very hard to reconcile those differences, such that the Fiji update site can ultimately be driven directly by what the source code specifies. For technical details, see {% include github org='fiji' repo='fiji' issue='37' label='fiji/fiji\#37' %}, {% include github org='fiji' repo='fiji' issue='38' label='fiji/fiji\#38' %} and {% include github org='fiji' repo='fiji' issue='39' label='fiji/fiji\#39' %}.

Finally, this update upgrades nearly all of Fiji's third party dependencies to their latest available release versions.

## New Fiji Life-Line versions

To guard against regressions which might result from such a big update, we updated the [Life-Line downloads of Fiji](/software/fiji/downloads#life-line-fiji-versions) with two new versions dated today: one for Java 8, and another for Java 6.

The Java 6 version in particular is notable because it provides a version of Fiji with the latest Java-6-compatible versions of all components. If you need to stick with Java 6 for some reason—e.g., you want to use Fiji with [BoneJ](/plugins/bonej), and/or with the [3D Viewer](/plugins/3d-viewer) + [Java 3D](/libs/java-3d) 1.5—then you can use this download as a starting point for your needs.

## Legacy Fiji components moved to their own update site

Several [legacy Fiji plugins](https://sites.imagej.net/Fiji-Legacy/plugins/) as well as [no-longer-needed dependent libraries](https://sites.imagej.net/Fiji-Legacy/jars/) have been retired from the ImageJ and Fiji update sites, migrating to a dedicated [Fiji-Legacy update site](https://sites.imagej.net/Fiji-Legacy/). None of these plugins completed the transition to reproducible builds in late 2014. Many of them are dedicated script interpreters, which have now been replaced by a unified SciJava Script Interpreter which allows dynamic language switching.

Note that the primary intent of the Fiji-Legacy update site is to be used in combination with a Java-6 installation of Fiji—see "New Fiji Life-Line versions" above. Enabling both the Java-8 and Fiji-Legacy sites will result in some components with overlapping classes—e.g., the batik uber-JAR plus all individual batik components.

 
