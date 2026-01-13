---
title: BigVolumeBrowser
project: /software/fiji
categories: [3D Visualization,Meshes,SMLM]
icon: /media/icons/bigvolumebrowser.png
name: BigVolumeBrowser
source-url: https://github.com/UU-cellbiology/bigvolumebrowser
pom-url: https://raw.githubusercontent.com/UU-cellbiology/bigvolumebrowser/refs/heads/main/pom.xml
team-developers:
- Eugene Katrukha
---

FIJI plugin for interactive 3D exploration of multiple large (and small) volumetric datasets and geometric shapes, built on BigVolumeViewer ([fork](https://github.com/UU-cellbiology/bvv-playground)).  

It can display volumetric (microscopy) data, SMLM datasets, and geometric objects (point clouds and meshes) in various rendering modes.  
Objects can be clipped and transformed freely in 3D, and it works with timelapse data.   
  
BVB performs lazy loading and supports a multi-scale pyramidal data formats.  
This speeds up render and allows exploration of datasets larger than GPU memory.  

For full **documentation** please refer to [project's wiki](https://github.com/UU-cellbiology/bigvolumebrowser/wiki).
