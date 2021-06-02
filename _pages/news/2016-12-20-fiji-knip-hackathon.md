---
mediawiki: 2016-12-20_-_Fiji_+_KNIP_hackathon
title: 2016-12-20 - Fiji + KNIP hackathon
---

From Tuesday, December 6, 2016 through Friday, December 16, 2016, the [Max Planck Institute of Molecular Cell Biology and Genetics](https://mpi-cbg.de/) hosted \~20 developers at their facility in Dresden, Germany for a [hackathon](/events/hackathons) to develop [ImageJ2](/software/imagej2) and [Fiji](/software/fiji) core infrastructure and [plugins](/plugins).

## Timeline

The following chart illustrates when everyone was present:

<timeline> Preset = TimeHorizontal\_AutoPlaceBars\_UnitYear

ImageSize = width:600

Colors =

` id:c01 value:blue`  
` id:c02 value:red`  
` id:c03 value:green`  
` id:c04 value:black`  
` id:c05 value:magenta`  
` id:c06 value:teal`  
` id:c07 value:yelloworange`  
` id:c08 value:skyblue`  
` id:c09 value:claret`  
` id:c10 value:oceanblue`  
` id:c11 value:purple`  
` id:c12 value:powderblue`  
` id:c13 value:coral`  
` id:c14 value:redorange`  
` id:c15 value:kelleygreen`  
` id:c16 value:orange`  
` id:c17 value:lightpurple`  
` id:c18 value:tan2`  
` id:c19 value:gray(0.3)`  
` id:c20 value:blue`  
` id:c21 value:red`  
` id:c22 value:green`  
` id:c23 value:black`  
` id:c24 value:magenta`  
` id:c25 value:teal`  
` id:gridLine value:gray(0.5)`  
` id:gridCanvas value:gray(0.8)`

BackgroundColors = canvas:gridCanvas

Period = from:6 till:17

ScaleMajor = unit:year increment:1 start:6 grid:white

LineData =

` at:6 color:gridLine layer:back width:0.5`  
` at:7 color:gridLine layer:back width:0.5`  
` at:8 color:gridLine layer:back width:0.5`  
` at:9 color:gridLine layer:back width:0.5`  
` at:10 color:gridLine layer:back width:0.5`  
` at:11 color:gridLine layer:back width:0.5`  
` at:12 color:gridLine layer:back width:0.5`  
` at:13 color:gridLine layer:back width:0.5`  
` at:14 color:gridLine layer:back width:0.5`  
` at:15 color:gridLine layer:back width:0.5`  
` at:16 color:gridLine layer:back width:0.5`  
` at:17 color:gridLine layer:back width:0.5`

BarData=

` barset:Hackers`

PlotData=

` width:15 `  
` fontsize:M`  
` textcolor:white`  
` align:left `  
` anchor:from `  
` shift:(4,-4) `  
` color:black`

` barSet:Hackers`  
` color:c01 from:12 till:17 text:"Curtis Rueden (LOCI)"`  
` color:c02 from:11 till:17 text:"Christian Dietz (KNIME/UniKN)"`  
` color:c03 from:11 till:16 text:"Patrick Winter (KNIME/UniKN)"`  
` color:c04 from:9 till:17 text:"Marcel Wiedenmann (KNIME/UniKN)"`  
` color:c05 from:9 till:16 text:"Tim-Oliver Buchholz (KNIME/UniKN)"`  
` color:c06 from:6 till:16 text:"Matthias Arzt (MPI-CBG)"`  
` color:c07 from:6 till:16 text:"Richard Domander (BoneJ/RVC)"`  
` color:c08 from:6 till:16 text:"Ulrik Günther (MPI-CBG)"`  
` color:c09 from:6 till:16 text:"Robert Haase (MPI-CBG)"`  
` color:c10 from:6 till:16 text:"Philipp Hanslovsky (Janelia)"`  
` color:c11 from:6 till:16 text:"Kyle Harrington (Uni-Idaho)"`  
` color:c12 from:6 till:16 text:"Florian Jug (MPI-CBG)"`  
` color:c13 from:6 till:16 text:"Klim Kolyvanov (MDC/BIMSB)"`  
` color:c14 from:6 till:16 text:"HongKee Moon (MPI-CBG)"`  
` color:c15 from:6 till:16 text:"Tobias Pietzsch (MPI-CBG)"`  
` color:c16 from:6 till:16 text:"Loic Royer (MPI-CBG)"`  
` color:c17 from:6 till:16 text:"Stephan Saalfeld (Janelia)"`  
` color:c18 from:6 till:16 text:"Pavel Tomancak (MPI-CBG)"`  
` color:c19 from:6 till:16 text:"Vladimir Ulman (MPI-CBG)"`  
` color:c20 from:6 till:13 text:"Jean-Yves Tinevez (Pasteur)"`  
` color:c21 from:6 till:10 text:"David Hörl (LMU, MDC)"`  
` color:c22 from:6 till:9 text:"Carsten Haubold (HCI)"`  
` color:c23 from:6 till:9 text:"Jonas Massa (HCI)"`

</timeline>

## Gallery


{% capture content%}
/media/news/hackdd16-beautiful-dresden.jpg \| Beautiful Dresden
/media/news/hackdd16-beer-and-code.jpg \| Beer and code
/media/news/hackdd16-better-software.jpg \| Better software, better research!
/media/news/hackdd16-day1.jpg \| First day
/media/news/hackdd16-hackers.jpg \| Hackers at work
/media/news/hackdd16-hacking.jpg \| Hacking
/media/news/hackdd16-mpicbg-xmas-party.jpg \| MPI-CBG Christmas party
/media/news/hackdd16-waldschlosschen.jpg \| Waldschloßchen
/media/news/hackdd16-xmas.jpg \| Merry Christmas!
{% endcapture %}
{% include gallery content=content%}


## Hackathon progress

### Tim-Oliver Buchholz

-   Participated in technical discussions about ThreeDViewer, BigDataViewer and the next generation of viewers used in [KNIME Image Processing](/software/knime).
-   Participated in discussions about [ImageJ Ops](/libs/imagej-ops) based feature extraction.
-   Worked on the integration of the BigDataViewer as new standard viewer in [KNIME Image Processing](/software/knime).

### Ulrik Günther

-   continued work on the [Scenery](Scenery) 3D rendering backend for [ThreeDViewer](/plugins/sciview) and [ClearVolume](/plugins/clearvolume) 2.0:
    -   introduced the library and its features to the community
    -   fixed native code dependencies, included CI builds
    -   worked on the Vulkan ([1](https://www.khronos.org/vulkan)) backend for higher rendering performance, which finally got merged (see {% include github org='ClearVolume' repo='scenery' pr='31' label='ClearVolume/scenery\#31' %})
    -   helped various people getting scenery running on their machine
-   fixed some bugs in [ClearVolume](/plugins/clearvolume), together with {% include person id='royerloic' %}
-   discussed future directions for [ThreeDViewer](/plugins/sciview)/[ClearVolume](/plugins/clearvolume)/[BigDataViewer](/plugins/bdv) with {% include person id='kephale' %}, {% include person id='royerloic' %}, {% include person id='tpietzsch' %} and {% include person id='axtimwalde' %}

### Robert Haase

-   Participated in discussions about [Fiji](/software/fiji) release cycle and [ImageJ Ops](/libs/imagej-ops) based feature extraction
-   Bugfixed a tool for visualising Meshes in the good old [3D Viewer](/plugins/3d-viewer) which were derived from ArrayList&lt;RandomAccessibleInterval<BoolType>&gt;s as an intermediate solution until the [ThreeDViewer](/plugins/sciview) is ready.
-   Built an ImageJ-Ops based particle analyser, which will in the future allow processing 3D images in a way like 2D images were processed using the good old [Particle Analysis](/imaging/particle-analysis) tool
-   With {% include person id='maarzt' %}, {% include person id='fjug' %}, and {% include person id='ctrueden' %} we launched the work on a `PlotService` for ImageJ2.

### Kyle Harrington

-   Participated in technical discussions, especially those focused on the next generation ThreeDViewer
-   Finished integrating imagej-ops usage into Funimage (see [Funimage\#26](https://github.com/funimage/funimage/pull/26))
-   Unifying Mesh data structure from ops with [imagej-mesh](https://github.com/imagej/imagej-mesh) file loading with {% include person id='rimadoma' %}
-   More [ThreeDViewer](/plugins/sciview) enhancements

### Florian Jug

-   With {% include person id='ctrueden' %}, overhauled the [SciJava Common](/libs/scijava#scijava-common) [logging](/develop/logging) mechanism ({% include github org='scijava' repo='scijava-common' pr='253' label='scijava/scijava-common\#253' %}).
-   With {% include person id='ctrueden' %},{% include person id='haesleinhuepf' %},{% include person id='tpietzsch' %}, and {% include person id='axtimwalde' %} split up the necessary work in order to cut stable releases of Fiji (biannually). This 'earned' me the status of 'Grand Poobah'. ;)
-   Worked on an 'indago' parent POM for DAIS related projects and started using it for the new tracker 'Tr2d'.
-   Worked on the new tracker 'Tr2d'. New features: improved leveraged editing; tracklet export; improved BDV overlays.
-   With {% include person id='royerloic' %} and {% include person id='maweigert' %} we have fixed some reported [ClearVolume](/plugins/clearvolume) bugs and released a new version after testing on Win/Linux/MaxOS.
-   With {% include person id='maarzt' %}, {% include person id='haesleinhuepf' %}, and {% include person id='ctrueden' %} we launched the work on a `PlotService` for ImageJ2.

### Curtis Rueden

-   With {% include person id='aneevel' %} and {% include person id='axtimwalde' %}, completed update of ImageJ web resources to support HTTPS (see [separate news post](/news/2016-12-29-imagej-web-resources-now-support-https)).
-   With {% include person id='fjug' %}, overhauled the [SciJava Common](/libs/scijava#scijava-common) [logging](/develop/logging) mechanism ({% include github org='scijava' repo='scijava-common' pr='253' label='scijava/scijava-common\#253' %}).
-   With {% include person id='rimadoma' %}, improved [SciJava Common](/libs/scijava#scijava-common) context injection to be recursive, to fix bugs with service population of commands ({% include github org='scijava' repo='scijava-common' commit='b0c981b24fc8ec845656574d95f9eddbc285728e' label='scijava/scijava-common@b0c981b2' %}, {% include github org='imagej' repo='imagej-ops' commit='4f78eca5b061881865c2a2c1702a98e634248aa5' label='imagej/imagej-ops@4f78eca5' %}).
-   With {% include person id='rimadoma' %}, add a validater callback for parameter validation ({% include github org='scijava' repo='scijava-common' commit='66ed844ee76a264ca83629f0fef50c9b726c8897' label='scijava/scijava-common@66ed844e' %}, {% include github org='scijava' repo='scijava-common' commit='70c50f48cc20cec0a747a000778f013c7380155d' label='scijava/scijava-common@70c50f48' %}).
-   With {% include person id='maarzt' %}, began work on a `PlotService` for ImageJ2 ([maarzt/imagej-ui-swing@plot-service](https://github.com/imagej/imagej-ui-swing/compare/plot-service...maarzt:plot-service)).
-   Participated in technical discussions with various people, including a "big-picture" status update for ImageJ2 covering my [primary priorities](User_Rueden#primary-projects); see [Technical discussions](#technical-discussions) section below.

### Tobias Pietzsch

-   With {% include person id='tinevez' %}, worked on Mastodon/plugins/trackmate3, in particular the unified handling of adapter views onto the main tracking model.
-   With {% include person id='axtimwalde' %}, worked towards integration of caching mechanisms into unified scijava/imglib2 cache; generalization of BigDataViewer cache.
-   Added support in [ui-behaviour](https://github.com/scijava/ui-behaviour) for triggering multiple behaviours in parallel.
-   Documented [ui-behaviour](https://github.com/scijava/ui-behaviour) configuration [syntax](https://github.com/scijava/ui-behaviour/wiki/InputTrigger-syntax)
-   Assisted with various BigDataViewer-related projects.

### Patrick Winter

-   Improvements to KNIME SLURM integration:
    -   Many bugfixes (specifically for the use of image processing workflows)
    -   Implemented status view for more detailed information about the state of running jobs
-   Got KNIME SLURM integration to run with the MPI-CBG Dresden cluster
-   Achieved significant speed ups by running parts of an image processing workflow on the cluster

### JeanYvesTinevez

-   With {% include person id='tpietzsch' %}, worked on Mastodon/plugins/trackmate3, in particular view colouring by numerical features calculated on a model.
-   With {% include person id='tpietzsch' %},extended the [MaMuT](/plugins/mamut) so that it can be used for 2D over time properly.

### Christian Dietz

-   With Marcel Wiedenmann, worked on processing of very large images in ops
-   With Tim-Oliver Buchholz, worked on BDV integration in KNIP

### Klim Kolyvanov

-   Implemented the non-rigid [coherent point drift](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.250.5954&rep=rep1&type=pdf) algorithm using la4j.
-   Pushed forward the implementation of the [radial symmetry](https://github.com/milkyklim/RadialSymmetryLocalization) plugin for ImageJ.
-   Worked on tracking of C.elegans cells.

### Carsten Haubold

-   With {% include person id='tpietzsch' %}, added a loader for 5D ilastik HDF5 volumes for BigDataViewer
-   Worked on a prototype for a tracking export plugin system within ilastik to talk to MaMuT

### Jonas Massa

-   implemented an ilastik HDF5 import/export plugin for Imagej ({% include github org='Beinabih' repo='ilastik-Fiji-Plugin' label='Beinabih/ilastik-Fiji-Plugin' %})

### HongKee Moon

-   Separated BigDataServer into two versions. One is SimpleBigDataServer which can be launched by adding xml datasets in the command line. The other is (Advanced) BigDataServer which is running with H2 DBMS backend.
-   ER design is completed with {% include person id='tpietzsch' %}.

<!-- -->

-   (Advanced) BigDataServer
    -   H2 DBMS integration is completed.
    -   User/Dataset/Tag/Annotation entity relationships are decided and made in the hackathon.
    -   DataSets are managed as either private or public according to users.
    -   Manager context is still supported as well as user management is possible there.
    -   Each user can share private datasets with other users.

<!-- -->

-   SimpleBigDataServer
    -   This is almost same as the previous command line based BigDataServer.

<!-- -->

-   Technical notes
    -   Upgraded the stringtemplate with v4(org.stringtemplate.v4.ST) which is getting powerful for templating strings for HTML tables.
    -   By using AJAX, database CRUD operations are carried in a responsive way.
    -   Realized how important JDBC database connection pool is.

## Technical discussions

### Programmers Anonymous

-   Robert is addicted to ImageJ.
-   Ulrik can only do snapshot releases.
-   Florian is doing too much at once... at least he has a car! (Yes Klim, you can join...)

### Stable releases of Fiji

-   We agreed to cut a stable release of Fiji once every six months.
    -   {% include person id='fjug' %} will manage the releases, both socially and technically.
    -   {% include person id='haesleinhuepf' %} will update the [Updater](/plugins/updater) to more clearly communicate the ramifications of updating.
    -   {% include person id='ctrueden' %} will create Jenkins jobs for automating cutting of stable release candidates and releases.
-   We agreed to continue pursuing the "melting pot" builds of Fiji and/or the SciJava universe, to better detect cross-component regressions and incompatibilities.
    -   {% include person id='ctrueden' %} will research effective approaches for running the melting pot via CI.
    -   Core maintainers (esp. {% include person id='tpietzsch' %} and {% include person id='axtimwalde' %}) will run the melting pot manually to vet its usefulness and correctness.

### 3D viewers in ImageJ and Fiji

-   We discussed how best to proceed with the [ThreeDViewer](/plugins/sciview), [BigDataViewer](/plugins/bdv) et. al.
    -   All agree to be very grumpy if the discussion ever degrades back to a laundry list of desired features (before we actually finish the first iteration of the code)
    -   {% include person id='kephale' %} will continue efforts to consolidate [ThreeDViewer](/plugins/sciview) and [BigDataViewer](/plugins/bdv) into a unified viewer
    -   {% include person id='tibuch' %} and {% include person id='dietzc' %} will continue to develop UI components for BDV and KNIME using SciJava for use in the unified viewer
    -   {% include person id='kephale' %}, {% include person id='tibuch' %}, and {% include person id='dietzc' %} will reconvene in the Spring for component integration
    -   {% include person id='tpietzsch' %} will continue to work his BDV magic
-   Roughly the idea is (we previously discussed this at the 2016 summer Konsanz hackathon):
    -   4 viewer panels (number of panels is convenience not hard coded): X-Y, Y-Z, X-Z, and 3D. Viewer panels have sliders for time and other dimensions
    -   Control panel with selection of attributes that can be synced between viewer panels, but can also be used for independent control of viewer panels
    -   BDV provides orthogonal views
    -   Viewer panels have overlays: minimaps, intensity, etc.
    -   ROI overlays can also be provided
    -   Panels are just JPanels
    -   {% include person id='tpietzsch' %} says most of the backend has already been developed in BDV
    -   [ThreeDViewer](/plugins/sciview) should reuse more of [BigDataViewer](/plugins/bdv)'s UI components
    -   GUI tools/widgets will go into scijava-ui-swing
    -   {% include person id='skalarproduktraum' %} will continue to develop Scenery for the core 3D rendering functionality

 
