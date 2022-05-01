---
mediawiki: BigDataViewer_Example_Datasets
title: BigDataViewer Example Datasets
---

This page links to example datasets for the [BigDataViewer](/plugins/bdv) Fiji plugin. See the [BigDataViewer](/plugins/bdv) user guide.

### Minimal SPIM example

This is an excerpt from a large multi-view time-lapse of *Drosophila* embryogenesis acquired on Zeiss Lightsheet Z.1. Download the XML and HDF5 files [drosophila.xml](http://fly.mpi-cbg.de/~pietzsch/bdv-examples/drosophila.xml) and [drosophila.h5](http://fly.mpi-cbg.de/~pietzsch/bdv-examples/drosophila.h5). Open the XML file with {% include bc path='Plugins | BigDataViewer | Open XML/HDF5'%} from the Fiji menu.

### His-YFP SPIM example

Based on Stephan Preibisch's example dataset ([available here](http://fly.mpi-cbg.de/preibisch/nm/HisYFP-SPIM.zip)) of *Drosophila* embryo expressing His-YFP in all cells, acquired using the Zeiss Demonstrator B. The data comprises one timepoint of this seven-view dataset. The data was exported to HDF5, registered, fused, and deconvolved the dataset using Stephan Preibsich's [Multiview-Reconstruction](/plugins/multiview-reconstruction) plugins. The dataset has 9 views: the 7 original angles from the microscope, a content-based fusion of the registered angles, and a multi-view deconvolution of the registered angles. Download the XML and HDF5 files [HisYFP-SPIM.xml](http://fly.mpi-cbg.de/~pietzsch/bdv-examples/HisYFP-SPIM.xml) and [HisYFP-SPIM.h5](http://fly.mpi-cbg.de/~pietzsch/bdv-examples/HisYFP-SPIM.h5). Open the XML file with {% include bc path='Plugins | BigDataViewer | Open XML/HDF5'%} from the Fiji menu. (Additionally you may download this settings file [HisYFP-SPIM.settings.xml](http://fly.mpi-cbg.de/~pietzsch/bdv-examples/HisYFP-SPIM.settings.xml) which adjusts the brightness of the fused and deconvolved data. Just place it next to the HisYFP-SPIM.xml file.)

### Remote HDF5

This dataset is served by our [BigDataServer](/plugins/bdv/server) (still in beta). It comprises 250 timepoints of a large 6-angle time-lapse *Drosophila* embryogenesis acquired on Zeiss Lightsheet Z.1. The dataset is stored as a 500GB XML/HDF5 file on the server. For remote viewing, only an XML file is required. Download [remote.xml](http://fly.mpi-cbg.de/~pietzsch/bdv-examples/remote.xml) and open it with {% include bc path='Plugins | BigDataViewer | Open XML/HDF5'%} from the Fiji menu.

Alternatively, choose {% include bc path='Plugins | BigDataViewer | Browse BigDataServer'%} from the Fiji menu, browse the server http://tomancak-srv1.mpi-cbg.de:8081 and open the *Drosophila* dataset.

### CATMAID

Electron microscopy dataset of 1.5 segments of the ventral nerve cord of a first-instar Drosophila larva (458 sections, each section consisting of ~ 70 overlapping image tiles, imaged at 4nm/px with 50nm section thickness) is available online through the web-browser based [CATMAID viewer](http://fly.mpi-cbg.de/).

This dataset was collected by **Albert Cardona** at Janelia Farm. The imaging was done by Albert Cardona and Wayne Pereanu. Rick Fetter prepared the sample and Julie Simpson funded the data collection through the HHMI Janelia farm visiting scientist program. The dataset was first introduced in this publication dealing with ssTEM elastic reconstruction:

Saalfeld S., Fetter R., Cardona A., Tomancak P. (2012) **Elastic Volume Reconstruction from Series of Ultra-thin Microscopy Sections** *Nature Methods* 9(7), 717-720

The data are provided here for the sole purpose of demonstrating the visualisation capabilities of BDV and are to be considered strictly "viewing only".

To view it in BigDataViewer, download [catmaid-abd1.5.xml](http://fly.mpi-cbg.de/~pietzsch/bdv-examples/catmaid-abd1.5.xml) and open with {% include bc path='Plugins | BigDataViewer | Open XML/HDF5'%} from the Fiji menu.


