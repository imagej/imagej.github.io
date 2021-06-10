---
mediawiki: 3D_Viewer:_Isosurface
title: 3D Viewer › Isosurface
nav-links: true
nav-title: Isosurface
---

## How to work with isosurfaces

You can download example source code for this HowTo [here](/plugins/3d-viewer/example-code).

Before reading this HowTo, it may be helpful to read [The relation between Content and Universe](/plugins/3d-viewer/content-structure).

When a `Content` is displayed as an isosurface, its `ContentNode` is of type `MeshGroup`. Since `MeshGroup` offers no additional functionality, than what can done with any `Content`, there is actually no reason under normal circumstances to retrieve a `MeshGroup` (although, it can be done of course).
