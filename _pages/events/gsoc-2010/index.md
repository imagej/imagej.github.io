---
title: SoC 2010 Ideas
---

# Welcome!

Fiji applied to the Google Summer of Code 2010 program, but was not accepted.

This page contains project ideas culled from the Fiji user and developer community. You can get started by reading some project descriptions, and the mailing list thread(s) that spawned them. Also consider joining the developer mailing list, or finding us on IRC. Details can be found in [Help](/discuss).

If none of the listed projects suit you, but you have your own project idea instead, just throw your ideas at us, on the developer mailing list! (Of course, it should be related to Fiji...)

# General Requirements

All projects have the following basic requirements:

-   Unless otherwise stated, projects will require programming in Java.
-   All materials must be released under the [GNU General Public License (GPL)](http://www.gnu.org/copyleft/gpl.html), version 2.
-   Individual students shall retain copyright on their works.
-   Projects must be tracked and managed in Git (we will help you with setting up a repository).
-   Weekly project status reports should be sent to the project's mentors. Each status report should outline what was accomplished that week, any issues that prevented that week's goals from being completed, and your goals for the next week. This will help you to break your project down into manageable chunks, and will also help the project's mentors to better support your efforts.

Interested students are encouraged to read the [Advice for GSoC Students Page](http://code.google.com/p/google-summer-of-code/wiki/AdviceforStudents), as it has excellent suggestions that might help you to pick a project and shape your proposal.

If your proposal is accepted by the Fiji Development Community you will be expected to work on it full time during the summer. It is cool if you want to take a week off for vacation, but remember that Google is hiring you for the summer to help us improve Fiji. That should be your focus. Don't expect that you will be able to work on your project for just 10 hours a week and then collect at the end.

If your original proposal doesn't pan out or becomes too much of a challenge, you should work with your mentor to help redefine it. We really want to see every project succeed this summer, as there is a great deal of interest in these projects from within the user community.

Students can apply for the program at the [Google Summer of Code website](http://code.google.com/soc/). Please consider reviewing our [SoC 2010 Template](template) and answering its questions as part of your application.

# Project ideas

## Applying machine learning to the image segmentation problem

The term *image segmentation* describes the task where objects in an image are to be outlined, so that every pixel is connected to either a named object, or background.

Segmentation is traditionally a very difficult problem, especially in the presence of variable lighting, noise, or low contrast.

Many segmentation algorithms have been implemented in Fiji to perform image segmentation, such as [Auto Threshold](/plugins/auto-threshold) and [Auto Local Threshold](/plugins/auto-local-threshold), but in practice, none of them might work, as they were designed with specific images in mind, and these expectations might not be met by your images.

Recently, a new class of segmentation algorithms has been emerging: segmentation by example. These algorithms require a set of examples from which a model is calculated which can be applied to other -- similar-looking -- images.

We will consider applications for implementations that are either as generic as possible (i.e. they apply to any images), or that try to solve a very specific problem (such as segmenting neurons in serial sections imaged with electron microscopy, or with confocal imaging.)

We have several data sets of images and their corresponding manual segmentations (for training the algorithm). See for example:

-   <i>Drosophila</i> larva brain imaged with ssTEM: [http://t2.ini.uzh.ch/data.html](http://t2.ini.uzh.ch/data.html)
-   <i>Drosophila</i> embryonic nuclei imaged with confocal microscopy.

You are welcome to use any scientifically-relevant dataset of your choice, but we will give priority to biologically-oriented data sets.

**Goal:** Implement a number of segmentation algorithms based on machine learning.  
**Language:** Java.  
**Mentor:** Johannes Schindelin (johannes.schindelin AT gmx.de) or Albert Cardona (acardona AT ini phys ethz ch)  

## Add JMathLib (MATLAB clone) support

Quite a few algorithms are available as proof-of-concept [MATLAB](/scripting/matlab) scripts. While it is [wrong to think of pixels as little squares](http://alvyray.com/Memos/CG/Microsoft/6_pixel.pdf), and literally all [MATLAB](/scripting/matlab) scripts to perform image processing are suffering from that shortcoming, it would be very nice nevertheless to be able to run the scripts without having to buy [MATLAB](/scripting/matlab) licenses just for that purpose.

Happily, there is a [MATLAB](/scripting/matlab) clone written in Java: [JMathLib](http://www.jmathlib.de/). While it is apparently not a speed demon, it should be useful to add JMathLib as a new scripting language to ImageJ, and integrate it into Fiji so that [MATLAB](/scripting/matlab) scripts can be executed just like all other ImageJ scripts, too.

The project would consist of

-   getting as many .m scripts for image processing as possible,

-   integrating JMathLib as a script language into Fiji (using the infrastructure shared by Jython, JRuby, Clojure, Javascript and BeanShell) -- I suggest having a look at {% include github repo='fiji' branch='master' path='src-plugins/JRuby_Interpreter/src/main/java/JRuby/JRuby_Interpreter.java' label='the JRuby Interpreter' %} for an example,

-   adapting (or overriding) JMathLib's image toolbox so that it integrates seamlessly with ImageJ,

-   test (and fix what does not work) as many .m scripts as possible.

**Goal:** Integrate JMathLib as a new scripting language.  
**Language:** Java.  
**Mentor:** Johannes Schindelin (johannes.schindelin AT gmx.de)  

## Teach the Fiji Updater about multiple update sites and offer to upgrade the Java Runtime

The Fiji Updater always looks for a static file containing an XML database of Fiji plugins (both current and past versions) on our website. To put new versions or new plugins there (to *upload into the updater*), you have to be a Fiji developer with write permission for that particular directory on our server.

In some cases, there are plugins that are either too sensitive, or too specific for a certain application, or not ready for public consumption yet, but still somebody might want to install Fiji in such a way that it automatically updates those plugins, too. Of course, there must be a different location for those plugins than the official Fiji update site, lest the general audience receive those plugins automatically.

The project is not without complications, though:

-   The XML database is saved as a file in the local Fiji directory, and it is always checked at startup whether the timestamp is newer than the timestamp of the XML database on the server. If you have multiple update sites, it should be handled in a way, where the local XML database reflects the sources of the metadata, and for uploading, a temporary XML database must be constructed for one particular upload site.

-   There may be conflicts between plugins that are official Fiji plugins, but also available from a secondary site. This has to be coped with (it is not clear what the best strategy should be: take the official Fiji version over the secondary site? let the user choose?)

-   With a new site, you need to be able to [upload plugins](/develop/uploading-plugins) to that site, too. There needs to be a very good way to prevent confusion, lest the plugin is uploaded to the <u>wrong</u> site.

-   To determine whether a developer can upload new plugins (because there are new versions), the Fiji Updater scans the complete plugins directory, along with a few other places where macros, 3rd party libraries, or the Fiji launcher might hide. The Fiji Updater needs to learn <u>not</u> to offer these plugins for upload to a secondary site, but only the non-Fiji ones.

-   It is unlikely that our current Fiji Updater can start a database from scratch. This has to be verified, and if there is no code for that yet, it has to be implemented.

-   Cross-site dependencies should be handled by having hints in the XML database as to what other site is supposed to have the newest dependency.

Also, the Updater cannot upgrade the Java Runtime as of now. There is little reason why it should not offer to download the installer directly from the [Sun Developer Network](http://java.sun.com/javase/downloads/index.jsp), run the installer, and install Java 3D on top.

**Goal:** Improve the Fiji Updater.  
**Language:** Java.  
**Mentor:** Johannes Schindelin (johannes.schindelin AT gmx.de)  

## Add a "real" installer

For now, Fiji is a portable application, which means you can unpack it anywhere and run it from there.

However, it would be nice to have an installer (similar to [IzPack](http://izpack.org/) or other Java-based installers), which just copies Fiji from where it happens to be at the moment to a user specified location, and then adds menu entries, file type associations, desktop icons, QuickLaunch shortcuts, maybe adjusts the PATH environment variable.

In short, basically provide all the niceties one expects from an installer.

**Goal:** Provide a proper installer for Fiji.  
**Language:** Java.  
**Mentor:** Johannes Schindelin (johannes.schindelin AT gmx.de)  

## Implementing algorithms for imglib

The new imglib supports dimension-, storage- and data type independent image processing. This library has some algorithms built-in already but there is a strong need to generically implement more general image processing algorithms, storage strategies and data types such as:

-   Interpolation (Cubic, Sinc, Spline, ...)
-   Histograms
-   Entropy Filter, Average Filter, Percentile(Min, Median, Max) Filter, ...
-   Memory Management for partial image loading
-   Color Spaces and Color Space Conversions
-   Generic Import/Export

**Goal:** Implement as many image processing algorithms using the imglib as possible  
**Language:** Java.  
**Mentor:** Stephan Preibisch (preibisch AT mpi-cbg.de) or Johannes Schindelin (johannes.schindelin AT gmx.de)  

## Composing a feature extraction library for supervised training of segmentations

On natural images machine learning approaches like boosted edge learning \[1\] or global probability of boundary \[2\] have demonstrated significant improvement in image segmentation by training on manually labeled ground truth.

In order to apply similar approaches to biological images a feature extraction library is necessary to capture the large variability of biological structures. The library should cover a range of features adaptable to different image modalities.

Possible features include: local binary patterns, wavelets, textons, gabor filter, ...

While significant features for a specific classification task can be selected based on manual labels, it would be beneficial for the usability of segmentation plugins to have an intuitive wizard that allows the user to define potential parameters by visual inspection of the data, e.g. providing the corresponding blurred image to select reasonable frequencies.

\[1\] Piotr Dollar, Zhuowen Tu, and Serge Belongie, [*Supervised Learning of Edges and Object Boundaries*](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.91.4383&rep=rep1&type=pdf), CVPR, 2006.  
\[2\] Michael Maire, Pablo Arbelaez, Charless Fowlkes and Jitendra Malik, [*Using Contours to Detect and Localize Junctions in Natural Images.*](http://www.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/papers/mafm-cvpr08.pdf),CVPR 2008

## Translate ITK methods into Fiji

The new **imglib** library facilitates the task of translating [ITK routines](http://www.itk.org/itkindex.html) into Fiji. The main idea of this project is to import interesting algorithms from [ITK](http://www.itk.org/itkindex.html) into native imglib code, mainly methods for:

-   2D/3D registration.
-   2D/3D segmentation.
-   Interpolation (for n-dimensional images).
-   Optimization.

**Goal:** Port ITK methods into Fiji.  
**Language:** Java, C++, ITK  
**Mentor:** Ignacio Arganda-Carreras (iarganda@mit.edu), Stephan Preibisch (preibisch@mpi-cbg.edu) or Johannes Schindelin (johannes.schindelin@gmx.de)

## Integrate µManager into Fiji

[µManager](http://www.micro-manager.org/) is a partly platform-dependent ImageJ project that adds support for controlling microscopes (focus, stages, filter banks, objective wheels, etc).

This project requires a bit of knowledge in compiling C++ code on Linux, MacOSX and Windows. The idea is to make a recipe that other people can use to (cross-)compile new releases of µManager, as well as integrate it into the Fiji project for a smooth user experience. To ensure that support for Micro-Manager is not broken inadvertently, you shall add regression tests, too.

**Goal:** Provide an easy way to compile and ship Micro-Manager with Fiji.  
**Language:** Java, C++, shell  
**Mentor:** Johannes Schindelin (johannes.schindelin@gmx.de)

## Morphological classification via hierarchical clustering

The idea behind this project is to implement interactive object classification on an image or stack containing various binary objects, based on morphological data residing on the Results Table. This data will be submitted to one of various hierarchical cluster analysis methods and produce a dendrogram graph. The distance between clusters in the dendrogram is represented by a "distance" axis and the user should be able to select the number of clusters via a slider on the "distance" axis. The objects in the original image are then labelled according to the cluster they belong defined by the distance slider.

**Goal:** Provide a means of data mining information from images using an interactive form of labelling based on cluster analysis.  
**Language:** Java, Weka library  
**Mentor:** G. Landini (G.Landini at bham.ac.uk) and Johannes Schindelin (johannes.schindelin@gmx.de)

## Applying machine learning to the image classification problem

This project is motivated by a specific biological questions associated with large-scale image set describing patterns of gene expression in [<i>Drosophila</i> embryogenesis](http://www.fruitfly.org/cgi-bin/ex/insitu.pl). It is inspired by the software developed under the [Cell Profiler project](http://www.pnas.org/content/106/6/1826.long).

General formulation of the problem: given a large set of related images, use (and extend) Fiji feature detection capabilities to extract numerical descriptors from the images and use them for iterative generation of a classifier based on user feedback.

Practically, develop an interface where a user (experienced biology expert) can select from a large set of <i>Drosophila</i> embryo images a subset of pictures showing similar anatomical features (highlighted by staining) while interactively assessing the performance of machine learning derived classifier on the whole set of images. The user should be able to influence the machine learning in two ways, by selecting or de-selecting training set images and by influencing the selection of the pre-computed features used in training.

This approach has been successfully used to classify embryo images yet a usable interactive implementation [is missing](http://bioinformatics.oxfordjournals.org/cgi/content/full/24/17/1881). Interestingly, the images are described by a control vocabulary annotation which presents an unique way to independently validate the results of the machine learning and could also be incorporated in the image selection process (i.e. starting from a more homogenous group).

<b>Pre-requisites:</b>

-   Large scale database of annotated RNA in situ images of gene expression patterns consisting of about 90,000 image representing 6000 genes.
-   Feature extraction approaches implemented [in Fiji](/plugins/feature-extraction)
-   Machine learning implemented in Fiji ([Weka](http://www.cs.waikato.ac.nz/ml/weka/))
-   [Paper](http://bioinformatics.oxfordjournals.org/cgi/content/full/24/17/1881) describing the principles of unsupervised machine learning approach on this dataset using combination of number of invariant features
-   Biologically motivated candidate with significant programming skills

<b>Goal</b> Implement a user interface for supervised machine learning  
<b>Language</b> Java  
<b>Mentors</b> Pavel Tomancak (tomancak at mpi-cbg.de) and Erwin Frise  

## Provide cluster support for Fiji

Fiji runs fine on desktop machines, but for some tasks, it is better to use a cluster.

To that end, Fiji already supports "headless" mode, i.e. operation without the need to have a graphical user interface running. But that is not enough:

-   There must be an easy way to define what operation should be performed on what set of images, or on what set of subimages.
-   Clusters come in all kinds of flavors with a lot of different schedulers. A general backend with adapters for the most common schedulers will be needed.
-   The user should have a nice user interface to see the progress, and the end result.
-   For convenience, Fiji should offer the option to make sure that the current Fiji is installed.

**Goal:** Add a component to schedule processes.  
**Language:** Java.  
**Mentor:** Pavel Tomancak (tomancak at mpi-cbg.de) and Johannes Schindelin (johannes.schindelin at gmx.de)  

## Hierarchical n-dimensional compressable cell-base storage backend

Develop storage backend that enables fast random access through limited bandwidth channels to large scale image datasets, e.g. a Java client that can arbitrarily slice into very large volumes hosted by a server without making the server render the slices and without the client loading the full volume.

In 3d, the scale pyramid would be an octree with each box differentially compressed by e.g. DCT or Wavelets. The project would require extending wavelets and DCT to arbitrary dimensions. As there is currently no file format for this kind of data such format has to be defined.

The project should make use of the imglib library

<b>Goal</b> Implementation and detailed specification of hierarchical compressable cell-based storage format  
<b>Language</b> Java  
<b>Mentors</b> Stephan Saalfeld (saalfeld at mpi-cbg.de)  

## Motion Deblurring from a Single Image

The aim of the project is to implement a state-of-the-art motion deblurring algorithm as described in the paper of Qi Shan et al., "High-quality Motion Deblurring from a Single Image" published at the Siggraph 2008. The algorithm is capable of approximating the undisturbed image without any prior knowledge like the Point Spread Function. Convergence is achieved by using improved noise modeling and actively suppressing ringing artifacts.

(Motion) Deblurring is a major problem in photography, thus interesting to a large audience and can be easily adopted to microscopic images to perform deconvolution.

-   [Webpage of Siggraph Paper](http://www.cse.cuhk.edu.hk/~leojia/projects/motion_deblurring/index.html)

<b>Goal</b> Implementation of motion deblurring using algorithms avaible in imglib  
<b>Language</b> Java  
<b>Mentors</b> Stephan Preibisch (preibisch at mpi-cbg.de)  

## Robust blob segmentation

In life sciences, you often cope with round structures of interest. Such round structures can be cells, vesicles, nuclei or similarly shaped objects. While an ellipse might be a good initial fit, the final outline most certainly is not.

It is important to keep in mind that the objects are clearly convex, as they sometimes overlap, and we still want to find the objects correctly. Example:

<figure><img src="/media/nucleidapiconfocal.png" title="NucleiDAPIconfocal.png" width="400" alt="NucleiDAPIconfocal.png" /><figcaption aria-hidden="true">NucleiDAPIconfocal.png</figcaption></figure>

The purpose of this project is to segment in a fully automatic way round, convex structures in biological images. This could be done by using a simple template matching approach for the initial stage, or a Gaussian fit, followed by a fit of the whole outline under the desired constraints.

**Goal:** Provide a robust blob segmentation algorithm that can work in 2D, 3D and 4D.  
**Language:** Java  
**Mentor:** Johannes Schindelin (johannes.schindelin@gmx.de)

## Fiber segmentation

Biological images sometimes contain fiber-like structures, such as cell membranes (in 2D, they are fiber-like), the mitotic spindle, or microtubuli. Example (the green signal):

![](/media/mitosis.jpg)

A combination of edge detection, hough transform and fitting should provide a robust segmentation of such structures.

**Goal:** Implement a segmentation method for linear structures.  
**Language:** Java  
**Mentor:** Johannes Schindelin (johannes.schindelin@gmx.de)

## Texture segmentation

Not all images which Fiji users are interested in contain bright objects on dark background, or vice versa. Sometimes, the structures cannot be discerned using the intensity, but only using statistic measures where the inside pixels have a different geometric distribution than the outside pixels. Example:

<figure><img src="/media/tem-clahe-50-256-2.5.jpg" title="Tem-clahe-50-256-2.5.jpg" width="500" alt="Tem-clahe-50-256-2.5.jpg" /><figcaption aria-hidden="true">Tem-clahe-50-256-2.5.jpg</figcaption></figure>

There are [a number](http://ai.stanford.edu/~ruzon/tex_seg/) [of](http://people.csail.mit.edu/sarasu/pub/texture05/) [texture](http://www-sop.inria.fr/ariana/DEMOS/wold/node2.html) [segmentation](http://www.cs.iupui.edu/~tuceryan/research/ComputerVision/moment-paper.pdf) [algorithms](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.49.6534) that appear to solve the problem to various extents.

This proposal is about adding at least one such segmentation algorithm to Fiji.

**Goal:** Add a segmentation algorithm to Fiji which uses texture features to discern different objects from background (and from each other).  
**Language:** Java  
**Mentor:** Johannes Schindelin (johannes.schindelin@gmx.de)

## Add trainable region merging

We have implemented the Statistical Region Merging algorithm in Fiji. It segments the image into different regions.

This is done by iterating over all pixel neighbor pairs sorted by pixel difference in ascending order, testing by a simple statistical test whether the two regions the two pixels belong to (if they are not already in the same region) are not really different, and therefore can be merged.

The same strategy can be performed using different statistical tests, or parameterized tests.

This project is about implementing a trainer for such tests, whose result is a model that would perform the same segmentation as it was trained with, but can be applied to high-throughput segmentation as well.

**Goal:** Implement a plugin that trains a region merging model on user-specified images.  
**Language:** Java  
**Mentor:** Johannes Schindelin (johannes.schindelin@gmx.de)

# Other Resources

-   [SoC 2010 Application](application)

# Other links

-   [Fiji's developer mailing list](https://groups.google.com/g/fiji-devel)
-   [Weka project](http://www.cs.waikato.ac.nz/ml/weka/)
-   [#fiji-devel channel](/discuss/chat#irc) on irc.freenode.net
-   Other [Project ideas](/contribute/project-ideas)
-   [more links](/software/fiji/links)
