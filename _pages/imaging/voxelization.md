---
title: Voxelization
section: Imaging
nav-links: true
---

Voxelization is the process of converting a data structures that store geometric information in a continuous domain (such as a 3D triangular mesh) into a rasterized image (a discrete grid).

## How to voxel a 3D mesh with Fiji

### Requirements

A [Fiji](/software/fiji) installation with the [sciview](/plugins/sciview) update site enabled.

### Steps

#### Launch sciview

![](/media/imaging/launch-sciview.png)

#### Import a 3D mesh

![](/media/imaging/import-obj.png)

At the time of this writing OBJ, STL, and Isosurfaces taken from a 3D image opened in ImageJ, all work.

#### Convert mesh to image

![](/media/imaging/mesh-to-image.png)

#### Select output dimensions

![](/media/imaging/mesh-to-image-dimensions.png)

#### Inspect the result

![](/media/imaging/voxelization-output.png)

### Optional additional steps

This voxelization procedures creates an image that represents the *surface* of the mesh. Firstly, it may be possible that the geometry of the surface does not voxelize well at particular resolutions, resulting in gaps in the output image (i.e. the result is not "watertight"). In these cases either try another resolution, or try filling in the gaps with either manual touchup, or image processing routines, such as dilation.

If a filled volume is desired, then take a watertight image (see above) and use the Flood Fill (3D) utility available within Fiji under the {% include bc path='Plugins|Process|Flood Fill (3D)'%}.
