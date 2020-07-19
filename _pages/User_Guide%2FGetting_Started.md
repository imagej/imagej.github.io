{{DISPLAYTITLE:Getting Started}}

This part provides basic information on ImageJ installation, troubleshooting and update strategies. It discusses [[#sub:Fiji-intro|Fiji↓]][[#nom-fiji|↓]] and [[#sub:ImageJ2intro|ImageJ2↓]] as well as third-party software related to ImageJ. Being impossible to document all the capabilities of ImageJ without exploring technical aspects of image processing, external resources allowing willing readers to know more about digital signal processing are also provided.

__TOC__
==Introduction==

ImageJ is a [http://rsb.info.nih.gov/ij/disclaimer.html public domain] Java image processing and analysis program inspired by [http://rsb.info.nih.gov/nih-image/ NIH Image] for the Macintosh. It runs, either as an online applet or as a downloadable application, on any computer with a Java 1.5 or later virtual machine. [http://imagej.nih.gov/ij/download.html Downloadable distributions] are available for Windows, Mac OS X and Linux. It can display, edit, analyze, process, save and print 8--bit, 16--bit and 32--bit images. It can read many image formats including TIFF, GIF, JPEG, BMP, DICOM, FITS and ‘raw’. It supports ‘stacks’ (and hyperstacks), a series of images that share a single window. It is multithreaded, so time-consuming operations such as image file reading can be performed in parallel with other operations<span class="FootOuter"><span class="SupFootMarker"> [A] </span><span class="HoverFoot"><span class="SupFootMarker"> [A] </span>A somehow outdated list of ImageJ’s features is available at http://imagej.nih.gov/ij/features.html</span></span>.

It can calculate area and pixel value statistics of user-defined selections. It can measure distances and angles. It can create density histograms and line profile plots. It supports standard image processing functions such as contrast manipulation, sharpening, smoothing, edge detection and median filtering.

It does geometric transformations such as scaling, rotation and flips. Image can be zoomed up to 32 : 1 and down to 1 : 32. All analysis and processing functions are available at any magnification factor. The program supports any number of windows (images) simultaneously, limited only by available memory.

Spatial calibration is available to provide real world dimensional measurements in units such as millimeters. Density or gray scale calibration is also available.

ImageJ was designed with an open architecture that provides extensibility via Java plugins. Custom acquisition, analysis and processing plugins can be developed using ImageJ’s built in editor and Java compiler. User-written plugins make it possible to solve almost any image processing or analysis problem.

Being public domain open source software, an ImageJ user has the [http://wikieducator.org/The_right_license/The_essential_freedoms four essential freedoms] defined by the Richard Stallman in 1986: 1) The freedom to run the program, for any purpose; 2) The freedom to study how the program works, and change it to make it do what you wish; 3) The freedom to redistribute copies so you can help your neighbor; 4) The freedom to improve the program, and release your improvements to the public, so that the whole community benefits.

ImageJ is being developed on Mac OS X using its built in editor and Java compiler, plus the ''BBEdit'' editor and the ''Ant'' build tool. The source code is freely [http://imagej.nih.gov/ij/developer/source/index.html available]. The author, Wayne Rasband ([mailto:wsr@nih.gov wsr@nih.gov]), is a Special Volunteer at the National Institute of Mental Health, Bethesda, Maryland, USA.

<div class="See">

[http://imagejdev.org/history History of ImageJ at imagejdev.org]

</div>

==Installing and Maintaining ImageJ==

ImageJ can be downloaded from http://imagej.nih.gov/ij/download.html. Details on how to install ImageJ on [[#index-Linux|↓]][http://imagej.nih.gov/ij/docs/install/linux.html Linux], [http://imagej.nih.gov/ij/docs/install/mac.html Mac OS 9], [[#index-Mac-OS-X|↓]][http://imagej.nih.gov/ij/docs/install/osx.html Mac OS X] and [[#index-Windows-(OS)|↓]][http://imagej.nih.gov/ij/docs/install/windows.html Windows] <span class="bibcites">[[[#biblio-1|1]]]</span> are available at http://imagej.nih.gov/ij/docs/install/ (<span class="sans"><span class="menuitem"><span class="sans">Help ▷ [[#sub:Installation...|Installation…↓]]</span></span></span> command). Specially useful are the platform-specific ''Troubleshooting'' and ''Known Problems'' sections. [[#index-Fiji|↓]][[#sub:Fiji-intro|Fiji↓]] installation is described at https://fiji.sc/wiki/index.php/Downloads.

The downloaded package may not contain the latest bug fixes so it is recommended to upgrade ImageJ right after a first installation. [[#index-Updates|↓]]Updating IJ[[#nom-ij|↓]] consists only of running <span class="sans"><span class="menuitem"><span class="sans">Help ▷ [[#sub:Update-ImageJ...|Update ImageJ…↓]]</span></span></span>, which will install the latest <span class="Filename">[http://imagej.nih.gov/ij/upgrade/ ij.jar]</span> in the ImageJ folder (on Linux and Windows) or inside the ImageJ.app (on Mac OS X).

<span class="sans"><span class="menuitem"><span class="sans">Help ▷ [[#sub:Update-ImageJ...|Update ImageJ…↓]]</span></span></span> can be used to upgrade (or downgrade) the <span class="Filename">ij.jar</span> file to ''release updates'' or ''daily builds''. Release updates are announced frequently on the [http://imagej.nih.gov/ij/notes.html IJ news website] and are labelled alphabetically (e.g., v. 1.43m). Typically, these releases contain several new features and bug fixes, described in detail on the [http://imagej.nih.gov/ij/notes.html ImageJ News page]. ''Daily builds,'' on the other hand, are labelled with numeric sub-indexes (e.g., v. 1.43n4) and are often released without documentation. Nevertheless, if available, release notes for daily builds can be found at http://imagej.nih.gov/ij/source/release-notes.html. When a release cycle ends (v. 1.42 ended with 1.42q, v. 1.43 with 1.43u, etc.) an ''installation package'' is created, downloadable from http://imagej.nih.gov/ij/download.html. Typically, this package is bundled with a small list of add-ons ([[#sub:Macros-ExtendingIJ|Macros↓]], [[#sub:Scripts|Scripts↓]] and [[#sub:Plugins|Plugins↓]]).

<div class="See">

[http://imagej.nih.gov/ij/macros/toolsets/Luts%20Macros%20and%20Tools%20Updater.txt Luts, Macros and Tools Updater], a macro toolset that performs live-updating of [http://imagej.nih.gov/ij/macros/ macros] listed on the ImageJ web site

</div>

===ImageJDistributions===

ImageJ alone is not that powerful: it’s real strength is the vast repertoire of [[#sub:Plugins|Plugins↓]] that extend ImageJ’s functionality beyond its basic core. The many hundreds, probably thousands, freely available plugins from contributors around the world play a pivotal role in ImageJ’s success <span class="bibcites">[[[#biblio-162|<span class="bib-index">112</span>]]]</span>. Running <span class="sans"><span class="menuitem"><span class="sans">Help ▷ [[#sub:Update-ImageJ...|Update ImageJ…↓]]</span></span></span>, however, will not update any of the plugins you may have installed<span class="FootOuter"><span class="SupFootMarker"> [B] </span><span class="HoverFoot"><span class="SupFootMarker"> [B] </span>Certain plugins, however, provide self-updating mechanisms (e.g., [http://simon.bio.uva.nl/objectj/ ObjectJ] and the [[#index-Bio-Formats|↓]][http://loci.wisc.edu/software/bio-formats OME Bio-Formats]).</span></span>.

ImageJ add-ons ([[#sub:Plugins|Plugins↓]], [[#sub:Scripts|Scripts↓]] and [[#sub:Macros-ExtendingIJ|Macros↓]]) are available from several sources ([http://imagej.nih.gov/ij/plugins/ ImageJ's plugins page] [<span class="sans"><span class="menuitem"><span class="sans">Help ▷ [[#sub:Plugins...|Plugins…↓]]</span></span></span>], [http://imagejdocu.tudor.lu/doku.php?id=plugin:start ImageJ Information and Documentation Portal] and [https://fiji.sc/wiki/index.php/Category:Plugins Fiji's webpage], among others) making manual updates of a daunting task. This reason alone, makes it extremely convenient the use of [[#sec:ImageJ-Distributions|ImageJDistributions↑]] bundled with a pre-organized collection of add-ons.

Below is a list of the most relevant projects that address the seeming difficult task of organizing and maintaining ImageJ beyond its basics. If you are a life scientist and have doubts about which distribution to choose you should opt for [[#sub:Fiji-intro|Fiji↓]]. It is heavily maintained, offers an automatic updater, improved scripting capabilities and ships with powerful plugins. More specialized adaptations of ImageJ are discussed in [[#sub:Other-Software-Packages|Software Packages Built on Top of ImageJ↓]].

====Fiji====

[https://fiji.sc/ Fiji][[#index-Fiji|↓]] (''Fiji Is Just ImageJ---Batteries included'') is a distribution of ImageJ together with Java, Java 3D and several plugins organized into a coherent menu structure. Citing its developers, “Fiji compares to ImageJ as Ubuntu compares to Linux”. The main focus of Fiji is to assist research in life sciences, targeting image registration, stitching, segmentation, feature extraction and 3D visualization, among others. It also supports many scripting languages (BeanScript, Clojure, Jython, Python, Ruby, ''see'' [[#sec:ScriptingOtherLang|Scripting in Other Languages↓]]). Importantly, Fiji ships with a [https://fiji.sc/wiki/index.php/Update_Fiji convenient updater] that knows whether your files are up-to-date, obsolete or locally modified. [https://fiji.sc/wiki/index.php/Documentation Comprehensive documentation] is available for most of its plugins. The Fiji project was presented publicly for the first time at the [http://imagejconf.tudor.lu/doku.php ImageJ User and Developer Conference] in November 2008.

====MBF ImageJ====

The [[#index-MBF-ImageJ|↓]][[#index-ImageJ-for-Microscopy|↓]][http://www.macbiophotonics.ca/imagej/ MBF ImageJ bundle] or ''ImageJ for Microscopy'' (formerly [http://www.uhnres.utoronto.ca/facilities/wcif/imagej/ WCIF-ImageJ]) features a collection of plugins and macros, collated and organized by Tony Collins at the MacBiophotonics facility, McMaster University. It is accompanied by a [http://www.macbiophotonics.ca/imagej/ comprehensive manual] describing how to use the bundle with light microscopy image data. It is a great resource for microscopists but is not maintained actively, lagging behind the development of core ImageJ.

Note that you can add plugins from MBF ImageJ to Fiji, combining the best of both programs. Actually, you can use multiple ImageJ distributions simultaneously, assemble your own ImageJ bundle by gathering the plugins that best serve your needs (probably, someone else at your institution already started one?) or create symbolic links to share plugins between different installations.

<div class="See">

Description of all ImageJ related projects at [http://imagejdev.org/faq#n141 ImageDev]

</div>
===Related Software===

====Software Packages Built on Top of ImageJ====

<div class="Description">

<span class="Description-entry">'''Bio7'''</span> [http://bio7.org/ Bio7] is an integrated development environment for [[#index-Bio7|↓]]ecological modeling with a main focus on individual based modeling and spatially explicit models. Bio7 features: Statistical analysis (using R); Spatial statistics; Fast communication between [[#index-R-(GNU-S)|↓]]R and Java; BeanShell and Groovy support; Sensitivity analysis with an embedded flowchart editor and creation of 3D OpenGL (Jogl) models (''see also'' RImageJ in [[#sec:ImageJ-Interoperability|ImageJ Interoperability↓]]).

</div>
<div class="Description">

<span class="Description-entry">BoneJ</span> [http://bonej.org/ BoneJ] [[#index-BoneJ|↓]]is a collection of tools for trabecular geometry and whole bone shape analysis.

</div>
<div class="Description">

<span class="Description-entry">'''<span class="formula"><span class="unknown">\micro</span></span>Manager'''</span> [http://www.micro-manager.org/ Micro-Manager] is a software package for control of automated microscopes. It lets you execute common microscope image acquisition strategies such as time-lapses, multi-channel imaging, z-stacks, and combinations thereof. [[#index-Micro_Manager|↓]]<span class="formula"><span class="unknown">\micro</span></span>Manager works with microscopes from all four major manufacturers, most scientific-grade cameras and many peripherals used in microscope imaging.

</div>
<div class="Description">

<span class="Description-entry">MRI--CIA''''''</span> ''''''[http://www.mri.cnrs.fr/index.php?m=38 MRI Cell Image Analyzer], developed by the Montpellier RIO Imaging facility (CNRS), is a rapid image analysis application development framework, adding visual scripting interface to ImageJ’s capabilities. It can create batch applications as well as interactive applications. The applications include the topics “DNA combing”, “quantification of stained proteins in cells”, “comparison of intensity ratios between nuclei and cytoplasm” and “counting nuclei stained in different channels”.

</div>
<div class="Description">

<span class="Description-entry">'''ObjectJ'''</span> [http://simon.bio.uva.nl/objectj/index.html ObjectJ], the successor of [http://simon.bio.uva.nl/Object-Image/object-image.html object-image], supports graphical vector objects that non-destructively mark images on a transparent layer. Vector objects can be placed manually or by macro commands. Composite objects can encapsulate different color-coded marker structures in order to bundle features that belong together. ObjectJ provides back-and-forth navigation between results and images. The results table supports statistics, sorting, color coding, qualifying and macro access.

</div>
<div class="Description">

<span class="Description-entry">'''SalsaJ'''</span> [http://www.euhou.net/index.php?option=com_content&task=view&id=7&Itemid=9 SalsaJ] is a student-friendly software developed specifically for the [http://www.euhou.net/ EU-HOU project]. It is dedicated to image handling and analysis of astronomical images in the classroom. [[#index-SalsaJ|↓]]SalsaJ has been translated into several languages.

</div>
<div class="Description">

<span class="Description-entry">'''[[|]]TrakEM2'''</span> [http://www.ini.uzh.ch/~acardona/trakem2.html TrakEM2] is a program for morphological [[#index-Data-mining|↓]]data mining, three-dimensional [[#index-Modeling|↓]]modeling and image stitching, registration, editing and annotation <span class="bibcites">[[[#biblio-57|<span class="bib-index">7</span>]]]</span>. [[#index-TrakEM2|↓]][[#index-Fiji|↓]]TrakEM2 is [https://fiji.sc/wiki/index.php/TrakEM2 distributed with Fiji] and [http://www.ini.uzh.ch/~acardona/trakem2_manual.html capable of]:
<div class="vspace" style="height: -8pt;">



</div>

</div>
<ul>
<li><div class="Description">

<span class="Description-entry">'''3D modeling'''</span> Objects in 3D, defined by sequences of contours, or profiles, from which a skin, or mesh, can be constructed, and visualized in 3D.

</div>
<div class="Description">

<span class="Description-entry">'''Relational modeling'''</span> The extraction of the map that describes links between objects. For example, which neuron contacts which other neurons through how many and which synapses.

</div></li></ul>

<div class="See">

[[#index-BioImageXD|↓]][http://www.bioimagexd.net/ BioImageXD], [[#index-Endrov|↓]][http://www.endrov.net/ Endrov], [[#index-Image-SXM|↓]][http://www.liv.ac.uk/%7Esdb/ImageSXM/ Image SXM]

</div>
====ImageJ Interoperability====

Several packages exist that allow ImageJ to [[#index-Interoperability|↓]]interact with other applications/environments:

<div class="Description">

<span class="Description-entry">Bitplane Imaris</span> [http://www.bitplane.com/go/products/imarisxt ImarisXT] can load and execute ImageJ plugins. [[#index-Imaris|↓]][http://www.bitplane.com/go/products/imarisxt/xtensions/imagej bpImarisAdapter] (Windows only and requiring valid licenses for Imaris and ImarisXT) allows the exchange of images between Imaris and ImageJ.

</div>
<div class="Description">

<span class="Description-entry">CellProfiler</span> [[#index-CellProfiler|↓]][http://www.cellprofiler.org/ CellProfiler] <span class="bibcites">[[[#biblio-61|<span class="bib-index">11</span>]]]</span> features [http://cellprofiler.org/CPmanual/RunImageJ.html RunImageJ], a module that allows ImageJ plugins to be run in a CellProfiler pipeline.

</div>
<div class="Description">

<span class="Description-entry">Icy</span> [http://www.bioimageanalysis.org/icy/ Icy], an open source community software for [[#index-Icy|↓]]bio-imaging, executes ImageJ plugins with almost 100% plugin compatibility.

</div>
<div class="Description">

<span class="Description-entry">Knime</span> [[#index-Knime|↓]] [http://knime.org/ Knime] ([[#nom-knime|↓]]Konstanz Information Miner) contains several image processing nodes ([[#nom-knip|↓]][http://tech.knime.org/community/image-processing KNIP][[#index-KNIP|↓]]) that are capable of executing ImageJ plugins and macros.

</div>
<div class="Description">

<span class="Description-entry">Open Microscopy Environment</span> [[#nom-ome|↓]]All [http://www.openmicroscopy.org/ Open Microscopy Environment] projects such as [[#index-Bio-Formats|↓]][http://www.openmicroscopy.org/site/products/bio-formats Bio-Formats], [http://www.openmicroscopy.org/site/products/visbio VisBio] and [http://www.openmicroscopy.org/site/products/omero OMERO] integrate well with ImageJ.

</div>
<div class="Description">

<span class="Description-entry">RImageJ --- R bindings for ImageJ</span> Bindings between ImageJ and [[#index-R-(GNU-S)|↓]][http://www.r-project.org/ R (GNU S)] — The free software environment for statistical computing and graphics. The documentation for RImageJ is available at http://cran.r-project.org/web/packages/RImageJ/RImageJ.pdf (''see also'' Bio7 in [[#sub:Other-Software-Packages|Software Packages Built on Top of ImageJ↑]]).

</div>
<div class="Description">

<span class="Description-entry">MIJ --- Matlab--ImageJ bi-directional communication</span> A Java package for bi-directional data exchange between [[#index-MATLAB|↓]]Matlab and ImageJ, allowing to exchange images between the two imaging software. [[#index-MIJ|↓]]MIJ also allows MATLAB to access all built-in functions of ImageJ as well as third-party ImageJ plugins. The developers provide more information on the [http://bigwww.epfl.ch/sage/soft/mij/ MIJ] and [http://www.mathworks.com/matlabcentral/fileexchange/32344-hardware-accelerated-3d-viewer-for-matlab Matlab File Exchange] websites. [[#sub:Fiji-intro|Fiji↑]] features <span class="code">[https://fiji.sc/wiki/index.php/Miji Miji.m]</span>, which makes even more convenient to use the libraries and functions provided by Fiji’s components from within Matlab.

</div>
<div class="See">

[http://imagej.nih.gov/ij/links.html ImageJ related links], list of [http://developer.imagej.net/category/web-links/related-imaging-software related imaging software] on the [[#sub:ImageJ2intro|ImageJ2↓]] website

</div>
===ImageJ2===

[http://imagejdev.org/ ImageJDev] is a [http://imagejdev.org/funding federally funded], [http://imagejdev.org/collaborators multi-institution] project dedicated to the development of the next-generation version of ImageJ: “[[#index-ImageJ2|↓]]ImageJ2”. [[#index-ImageJ2|↓]][[#index-ImageDev|↓]]ImageJ2 is a complete rewrite of ImageJ, that includes the current, stable version ImageJ (“ImageJ1”) with a compatibility layer so that old-style plugins and macros can run the same as they currently do in ImageJ1. Below is a [http://imagejdev.org/aims summary] of the [http://imagejdev.org/ ImageJDev] project aims:

* To create the next generation version of ImageJ and improve its core architecture based on the needs of the community.
* To ensure ImageJ remains useful and relevant to the broadest possible community, maintaining backwards compatibility with ImageJ1 as close to 100% as possible.
* Expand functionality by interfacing ImageJ with existing open-source programs.
* To lead ImageJ development with a clear vision, avoiding duplication of efforts
* To provide a central online resource for ImageJ: program downloads, a plugin repository, developer resources and more.

Be sure to follow the ImageJ2 [http://imagejdev.org/recent_changes project news] and the [http://imagejdev.org/blog ImageDev blog] for updates on this exciting project.

==Getting Help==

===Help on Image Analysis===

[[#index-Ethics|↓]][[#index-Acceptable-manipulation|↓]]Below is a list of online resources (in no particular order) related to image processing and scientific image analysis, complementing the list of [http://imagej.nih.gov/ij/links.html external resources on the IJ web site].

====Ethics in Scientific Image Processing====

<ul>
<li>[http://www.ori.dhhs.gov/education/products/RIandImages/default.html Online learning Tool for Research Integrity and Image Processing]<br />
This website, created by the [http://ori.dhhs.gov/ Office of Research Integrity], explains what is appropriate in image processing in science and what is not.</li>
<li>[http://swehsc.pharmacy.arizona.edu/exppath/micro/digimage_ethics.php Digital Imaging: Ethics (at the Cellular Imaging Facily Core, SEHSC)]<br />
This website, compiled by Douglas Cromey at the University of Alabama -- Birmingham, discusses thoroughly the topic of digital imaging ethics. It is recommended for all scientists. The website contains links to several external resources, including:
<div class="vspace" style="height: -8pt;">



</div>
<ol>
<li>[http://www.jcb.org/cgi/reprint/166/1/11 What's in a picture? The temptation of image manipulation] (2004) M Rossner and K M Yamada, J Cell Biology 166(1):11--15, doi:10.1083/jcb.200406019</li>
<li>[http://www.nature.com/nature/journal/v439/n7079/full/439891b.html Not picture-perfect] (2006), Nature 439, 891--892, doi:10.1038/439891b.</li></ol>
</li></ul>

====Scientific Image Processing====

* [https://fiji.sc/wiki/index.php/IP_Principles What you need to know about scientific image processing]<br />
Simple and clear, this [[#sub:Fiji-intro|Fiji↑]] webpage explains basic aspects of scientific image processing.
* [http://www.imagingbook.com imagingbook.com]<br />
Web site of ''Digital Image Processing: An Algorithmic Introduction using Java'' by Wilhelm Burger and Mark Burge <span class="bibcites">[[[#biblio-164|<span class="bib-index">114</span>]]]</span>. This technical book provides a modern, self-contained, introduction to digital image processing techniques. Numerous complete Java implementations are provided, all of which work within ImageJ.
* [http://homepages.inf.ed.ac.uk/rbf/HIPR2/ Hypermedia Image Processing Reference (HIPR2)]<br />
Developed at the Department of Artificial Intelligence in the University of Edinburgh, provides on-line reference and tutorial information on a wide range of image processing operations.
* [https://ifn.mpi-cbg.de/wiki/ifn/index.php/Imaging_Facility_Network IFN wikipage]<br />
The Imaging Facility Network (IFN) in Biopolis Dresden provides access to advanced microscopy systems and image processing. The website hosts high quality [https://ifn.mpi-cbg.de/wiki/ifn/index.php/Teaching_Material teaching material] and useful links to external resources.
* [http://www.stereology.info/ stereology.info]<br />
Stereology Information for the Biological Sciences, designed to introduce both basic and advanced concepts in the field of stereology.

<div class="See">

ImageJ Related Publications on page [[#sec:IJ-related-pub|1↓]]

</div>
===Help on ImageJ===

Below is a list of the ImageJ [[#index-Help-resources|↓]]help resources that complement this guide (''see'' [[#sec:Guide-Formats|$↓]]). Specific documentation on advanced uses of ImageJ (macro programming, plugin development, etc.) is discussed in [[#sec:Extending-ImageJ|Extending ImageJ↓]].

# The ImageJ [http://imagej.nih.gov/ij/docs/ online documentation pages]<br />Can be accessed via the <span class="sans"><span class="menuitem"><span class="sans">Help ▷ [[#sub:Documentation...|Documentation…↓]]</span></span></span> command.
# The [[#index-Fiji|↓]][[#sub:Fiji-intro|Fiji↑]] webpage:<br /> https://fiji.sc/
# The ImageJ Information and Documentation Portal (ImageJ wikipage):<br />http://imagejdocu.tudor.lu/doku.php
# Video [[#index-Tutorials|↓]]tutorials on the ImageJ Documentation Portal and the Fiji YouTube channel:<br />http://imagejdocu.tudor.lu/doku.php?id=video:start&s%5B%5D=video and http://www.youtube.com/user/fijichannel. New ImageJ users will probably profit from [http://imagejdocu.tudor.lu/doku.php?id=video:beginner_help:imagej_beginner_s_tutorial Christine Labno's video tutorial].
# The [[#index-MBF-ImageJ|↓]]ImageJ for Microscopy manual<br />http://www.macbiophotonics.ca/imagej/
# Several online documents, most of them listed at:<br />http://imagej.nih.gov/ij/links.html and http://imagej.nih.gov/ij/docs/examples/
# Mailing lists:[[#index-Mailing-lists|↓]]
## '''ImageJ''' — http://imagej.nih.gov/ij/list.html<br />General user and developer discussion about ImageJ. Can be accessed via the <span class="sans"><span class="menuitem"><span class="sans">Help ▷ [[#sub:List-Archives...|<span class="menuitem">Mailing List…</span>↓]]</span></span></span> command. This list is also mirrored at [http://imagej.1557.n6.nabble.com/ Nabble] and [http://dir.gmane.org/gmane.comp.java.imagej Gmane]. You may find it easier to search and browse the list archives on these mirrors. Specially useful are the [feed://rss.gmane.org/topics/excerpts/gmane.comp.java.imagej RSS feeds] and the ''[http://news.gmane.org/gmane.comp.java.imagej frames and threads]'' view provided by Gmane.
## '''Fiji users''' --- http://groups.google.com/group/fiji-users<br />For user discussion specific to [[#sub:Fiji-intro|Fiji↑]] (rather than core ImageJ).
## '''Fiji-devel''' — http://groups.google.com/group/fiji-devel<br />For developer discussion specific to Fiji.
## '''ImageJ-devel''' — http://imagejdev.org/mailman/listinfo/imagej-devel<br />For communication and coordination of the ImageJDev project.
## '''Dedicated mailing lists''' for ImageJ related projects<br />Described at http://imagejdev.org/mailing-lists .

====Using Mailing-lists====

If you are having problems with ImageJ, you should inquiry about them in the appropriated [[#index-Help-resources|↓]]list. The ImageJ mailing list is an unmoderated forum subscribed by a knowledgeable worldwide user community with <span class="formula"><span class="unknown">\thickapprox</span></span>2000 advanced users and developers. To have your questions promptly answered you should consider the following:

# Read the documentation files (described earlier in this section) before posting. Because there will always be a natural lag between the implementation of key features and their documentation it may be wise to check briefly the ImageJ news website (<span class="sans"><span class="menuitem"><span class="sans">Help ▷ [[#sub:ImageJ-News...|ImageJ News…↓]]</span></span></span>).
# Look up the mailing list archives (<span class="sans"><span class="menuitem"><span class="sans">Help ▷ [[#sub:List-Archives...|<span class="menuitem">Mailing List…</span>↓]]</span></span></span>). Most of your questions may have already been answered.
# If you think you are facing a [[#index-Bug-(reporting)|↓]]bug try to upgrade to the latest version of ImageJ (<span class="sans"><span class="menuitem"><span class="sans">Help ▷ [[#sub:Update-ImageJ...|Update ImageJ…↓]]</span></span></span>). You should also check if you are running the latest version of the Java Virtual Machine for your operating system. Detailed instructions on how to submit a bug report are found at http://imagej.nih.gov/ij/docs/faqs.html#bug.
# Remember that in most cases you can find answers within your own ImageJ installation without even connecting to the internet since the heuristics for finding commands or writing macros have been significantly improved in later versions (''see'' [[#sec:Finding-Commands|Finding Commands↓]] and [[#sec:Extending-ImageJ|Extending ImageJ↓]]).
# As with any other mailing list, you should always follow basic [http://en.wikipedia.org/wiki/Netiquette netiquette], namely:
## Use descriptive subject lines — ''Re: Problem with Image&gt;Set Scale command'' is much more effective than a general ''Re: Problem.''
## Stay on topic — Do not post off-topic messages, unrelated to the message thread.
## Be careful when sending attachments — Refrain from attaching large files. Use, e.g., a [http://en.wikipedia.org/wiki/File_hosting_service#Comparison_of_notable_file_hosting_services file hosting service] instead.
## Edit replies — You should include only the minimum content that is necessary to provide a logical flow from the question to the answer, i.e., quote only as much as absolutely necessary and relevant.
