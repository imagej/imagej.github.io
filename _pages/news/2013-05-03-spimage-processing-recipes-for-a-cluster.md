---
title: 2013-05-03 - SPIMage processing recipes for a cluster
---

Time-lapse SPIM imaging produces ridiculous amounts of data and the way to deal with the data deluge is to process the timepoints in parallel on a cluster.

Pavel Tomancak wrote [recipes](/plugins/spim-registration/on-cluster) for launching Fiji's SPIM registration, fusion, deconvolution and rendering plugins on the MPI-CBG cluster. They should be easily adaptable to other cluster environments.

The pipeline was developed for processing of data from the commercial SPIM solution - [Lightsheet Z.1](http://microscopy.zeiss.com/microscopy/en_de/products/imaging-systems/lightsheet-z-1.html) from Zeiss.

It would be nice if other's contribute their scripts and experience...


