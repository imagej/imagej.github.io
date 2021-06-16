---
title: 3D Viewer › Orthoslices
nav-links: true
nav-title: Orthoslices
---

## How to work with orthoslices

You can download example source code for this HowTo [here](/plugins/3d-viewer/example-code).

Before reading this HowTo, it may be helpful to read [The relation between Content and Universe](/plugins/3d-viewer/content-structure).

When displaying a `Content` as orthoslices, the corresponding `ContentNode` of the `Content` is of type `OrthoGroup`.

`OrthoGroup` extends `VoltexGroup`, and therefore also shares its functionality regarding volume editing. Additionally, `OrthoGroup` provides functions for adjusting the displayed slices (planes) and hiding them:

```java
// Add the image as a volume
Content c = univ.addOrthoslice(imp);

// Retrieve the OrthoGroup OrthoGroup ortho = (OrthoGroup)c.getContent();

for(int i = 0; i &lt; 10; i++) {
   ortho.increase(AxisConstants.Z_AXIS);
   sleep(1);
}

// Hide the x-axis ortho.setVisible(AxisConstants.X\_AXIS, false);

// Show it again and hide the z-axis ortho.setVisible(AxisConstants.X\_AXIS, true); ortho.setVisible(AxisConstants.Z\_AXIS, false);

// Show it again ortho.setVisible(AxisConstants.Z\_AXIS, true);
```


**Important methods of `OrthoGroup`**

    public void setSlice(int axis, int v);

    public int getSlice(int axis);

    public void decrease(int axis);

    public void increase(int axis);

    public boolean isVisible(int axis);

    public void setVisible(int axis, boolean b);
