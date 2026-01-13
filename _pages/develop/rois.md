---
title: ROIs
project: /libs/imglib2
---

{% include warning/wip %}
 In {% include wikipedia title='Image processing' text='image processing'%}, two of the most often needed yet complex operations are {% include wikipedia title='Segmentation (image processing)' text='segmentation'%} and {% include wikipedia title='Image registration' text='registration'%}. Regions of interest (ROIs) are an effective way of expressing and visualizing the results of a segmentation. For the current implementation of ROIs in ImageJ, see the [imglib2-roi](https://github.com/imglib/imglib2-roi) repository.

# Introduction

The base interface for all ROIs is **MaskPredicate**. **MaskPredicate** extends Java's **Predicate** whose `test(...)` method is used to determine if a given point is inside or outside a ROI.

ROIs are further separated into discrete and continuous space ROIs, which can be bounded or unbounded. **Mask** is the base interface for all discrete space ROIs, and **MaskInterval** is the base interface for all bounded discrete space ROIs. Similarly, **RealMask** is the base interface for all continuous space ROIs, and **RealMaskRealInterval** is the base interface for all bounded continuous space ROIs.

Concrete implementations of geometric ROIs (i.e. ellipsoids, polylines, etc.) can be retrieve from **GeomMasks**. The below example creates a 3D sphere centered at (12.5, 6, 93.25) with a radius of 0.5.

```java
final double[] center = new double[] { 12.5, 6, 93.25 };
final double radius = 0.5;
final Sphere sphere = GeomMasks.closedWritableSphere( center, radius );
```

## Naming

All n-dimensional geometric ROIs should be named with the name of their 3D counterpart. For example, an n-dimensional hyper-ellipsoid would just be named 'ellipsoid'. If a ROI implementation is not n-dimensional, its dimensionality should be stated in the name. For example, **Polygon2D** which is a 2D polygon.

Additionally, ROIs prefixed with "Writable" are mutable. ROIs without this prefix are assumed to be immutable.

## BoundaryType

The boundary behavior of a ROI is given by its **BoundaryType** enum which has three values.

-   **CLOSED** - all points on the boundary are considered inside
-   **OPEN** - all points on the boundary are considered outside
-   **UNSPECIFIED** - some points on the boundary may be inside while others are outside

## KnownConstant

The **KnownConstant** enum is used for determining if a ROI returns `false` for all locations, or `true` for all locations. This is useful for determining if the result of an operation between ROIs results in "empty" space or "all" space.

-   **`ALL_FALSE`** - ROI is known to return `false` for all locations
-   **`ALL_TRUE`** - ROI is known to return `true` for all locations
-   **`UNKNOWN`** - it is undetermined what the ROI returns for all locations, most ROIs have this

# Combining ROIs

ROIs can be combined via a number of operations, namely: `and`, `or`, `negate`, `minus`, and `xor`. **RealMask**s also have a `transform` operation. Combined ROIs are **CompositeMaskPredicate**s, which preserves the provenance of the composite ROI. For each **CompositeMaskPredicate** it is possible to retrieve the operator and operands. This results in a "tree" of ROIs.

The below example creates a composite ROI: 

```java
final Sphere s1 = new ClosedWritableSphere( new double[] { 0, 0, 0 }, 3.5 );
final Sphere s2 = new ClosedWritableSphere( new double[] { 1, 2, 0 }, 1.5 );
final Sphere s3 = new ClosedWritableSphere( new double[] { 2, 2, 0 }, 1.5 );
final RealMaskRealInterval composite = s1.and( s2.minus( s3 ) ).and( s3 ).or( s1.minus( s3.negate() ) );
```

The resulting composite ROI has the resulting "tree":

```
leaf  (net.imglib2.roi.geom.real.ClosedWritableSphere@a4)
OR  (net.imglib2.roi.composite.DefaultBinaryCompositeRealMaskRealInterval@5a050f05)
 +--AND  (net.imglib2.roi.composite.DefaultBinaryCompositeRealMaskRealInterval@d5189b46)
 |   +--AND  (net.imglib2.roi.composite.DefaultBinaryCompositeRealMaskRealInterval@f1bb9aa6)
 |   |   +--leaf  (net.imglib2.roi.geom.real.ClosedWritableSphere@a4)
 |   |   +--MINUS  (net.imglib2.roi.composite.DefaultBinaryCompositeRealMaskRealInterval@516e3be)
 |   |       +--leaf  (net.imglib2.roi.geom.real.ClosedWritableSphere@7d)
 |   |       +--leaf  (net.imglib2.roi.geom.real.ClosedWritableSphere@8a)
 |   +--leaf  (net.imglib2.roi.geom.real.ClosedWritableSphere@8a)
 +--MINUS  (net.imglib2.roi.composite.DefaultBinaryCompositeRealMaskRealInterval@fcc5e4e3)
     +--leaf  (net.imglib2.roi.geom.real.ClosedWritableSphere@a4)
     +--NEGATE  (net.imglib2.roi.composite.DefaultUnaryCompositeRealMask@c2ea3a1e)
         +--leaf  (net.imglib2.roi.geom.real.ClosedWritableSphere@8a)

```
Note that the same ROI can be used in multiple operations within the same composite.

## BoundaryType of Composites

The boundary behavior of a ROI may change as a result of the operation. The below outlines the composite BoundaryType logic, used when composite ROIs are formed.

### Unary Operators

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <caption style="caption-side:bottom; text-align: left; font-size: 0.9em; font-weight: normal;">
      <sup>1</sup> Transform is {% include wikipedia title='Continuous function' text='continuous'%} (preserves boundary behavior) and will preserve the interval bounds<br>
      <sup>2</sup> Transform is discontinuous or doesn't preserve bounds
      </caption>
      <td>
        <p><b>Operation</b></p>
      </td>
      <td></td>
      <td>
        <p><b>BoundaryType</b></p>
      </td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>
        <p><b>open</b></p>
      </td>
      <td>
        <p><b>closed</b></p>
      </td>
      <td>
        <p><b>unspecified</b></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><b>negate</b></p>
      </td>
      <td>
        <p>closed</p>
      </td>
      <td>
        <p>open</p>
      </td>
      <td>
        <p>unspecified</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><b>transform<sup>1</sup></b></p>
      </td>
      <td>
        <p>open</p>
      </td>
      <td>
        <p>closed</p>
      </td>
      <td>
        <p>unspecified</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><b>transform<sup>2</sup></b></p>
      </td>
      <td>
        <p>unspecified</p>
      </td>
      <td>
        <p>unspecified</p>
      </td>
      <td>
        <p>unspecified</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

### Binary Operators


<table>
<tbody>
<tr><td>
<table>
  <tbody>
    <tr>
      <td colspan=4><p><b>And</b></p></td>
    </tr>
    <tr>
      <td colspan=4><p><b>OperandBoundaryType</b></p></td>
    </tr>
    <tr>
      <td><p><b>Left</b></p></td>
      <td colspan=3><p><b>Right</b></p></td>
    </tr>
    <tr>
      <td></td>
      <td><p><b>open</b></p></td>
      <td><p><b>closed</b></p></td>
      <td><p><b>unspecified</b></p></td>
    </tr>
    <tr>
      <td><p><b>open</b></p></td>
      <td><p>open</p></td>
      <td><p>unspecified</p></td>
      <td><p>unspecified</p></td>
    </tr>
    <tr>
      <td><p><b>closed</b></p></td>
      <td><p>unspecified</p></td>
      <td><p>closed</p></td>
      <td><p>unspecified</p></td>
    </tr>
    <tr>
      <td><p><b>unspecified</b></p></td>
      <td><p>unspecified</p></td>
      <td><p>unspecified</p></td>
      <td><p>unspecified</p></td>
    </tr>
  </tbody>
</table>
</td>
<td>
<table>
  <tbody>
    <tr>
      <td colspan=4><p><b>Minus</b></p></td>
    </tr>
    <tr>
      <td colspan=4><p><b>OperandBoundaryType</b></p></td>
    </tr>
    <tr>
      <td><p><b>Left</b></p></td>
      <td colspan=3><p><b>Right</b></p></td>
    </tr>
    <tr>
      <td></td>
      <td><p><b>open</b></p></td>
      <td><p><b>closed</b></p></td>
      <td><p><b>unspecified</b></p></td>
    </tr>
    <tr>
      <td><p><b>open</b></p></td>
      <td><p>unspecified</p></td>
      <td><p>open</p></td>
      <td><p>unspecified</p></td>
    </tr>
    <tr>
      <td><p><b>closed</b></p></td>
      <td><p>closed</p></td>
      <td><p>unspecified</p></td>
      <td><p>unspecified</p></td>
    </tr>
    <tr>
      <td><p><b>unspecified</b></p></td>
      <td><p>unspecified</p></td>
      <td><p>unspecified</p></td>
      <td><p>unspecified</p></td>
    </tr>
  </tbody>
</table>
</td></tr>
<tr><td>
<table>
  <tbody>
    <tr>
      <td colspan=4><p><b>Or</b></p></td>
    </tr>
    <tr>
      <td colspan=4><p><b>OperandBoundaryType</b></p></td>
    </tr>
    <tr>
      <td><p><b>Left</b></p></td>
      <td colspan=3><p><b>Right</b></p></td>
    </tr>
    <tr>
      <td></td>
      <td><p><b>open</b></p></td>
      <td><p><b>closed</b></p></td>
      <td><p><b>unspecified</b></p></td>
    </tr>
    <tr>
      <td><p><b>open</b></p></td>
      <td><p>open</p></td>
      <td><p>unspecified</p></td>
      <td><p>unspecified</p></td>
    </tr>
    <tr>
      <td><p><b>closed</b></p></td>
      <td><p>unspecified</p></td>
      <td><p>closed</p></td>
      <td><p>unspecified</p></td>
    </tr>
    <tr>
      <td><p><b>unspecified</b></p></td>
      <td><p>unspecified</p></td>
      <td><p>unspecified</p></td>
      <td><p>unspecified</p></td>
    </tr>
  </tbody>
</table>
</td>
<td>
<table>
  <tbody>
    <tr>
      <td colspan=4><p><b>Xor</b></p></td>
    </tr>
    <tr>
      <td colspan=4><p><b>OperandBoundaryType</b></p></td>
    </tr>
    <tr>
      <td><p><b>Left</b></p></td>
      <td colspan=3><p><b>Right</b></p></td>
    </tr>
    <tr>
      <td></td>
      <td><p><b>open</b></p></td>
      <td><p><b>closed</b></p></td>
      <td><p><b>unspecified</b></p></td>
    </tr>
    <tr>
      <td><p><b>open</b></p></td>
      <td><p>unspecified</p></td>
      <td><p>unspecified</p></td>
      <td><p>unspecified</p></td>
    </tr>
    <tr>
      <td><p><b>closed</b></p></td>
      <td><p>unspecified</p></td>
      <td><p>unspecified</p></td>
      <td><p>unspecified</p></td>
    </tr>
    <tr>
      <td><p><b>unspecified</b></p></td>
      <td><p>unspecified</p></td>
      <td><p>unspecified</p></td>
      <td><p>unspecified</p></td>
    </tr>
  </tbody>
</table>
</td></tr>
</tbody>
</table>

## Bounds of Composites

The composite logic tries very hard to preserve the bounds of ROIs whenever possible. Additionally, the bounds will update when the composite's leaves are updated.

In the below example, a **CompositeMaskPredicate** is generated by and-ing a **Sphere** and a **Box**. The below example shows that the bounds are sensitive to changes in the operands' bounds. It also demonstrates ROIs ability to detect if a composite is empty.

```java
final WritableSphere s = GeomMasks.closedWritableSphere( new double[] { 7.5, 8 }, 5 );
final WritableBox b = GeomMasks.closedWritableBox( new double[] { 3, 2 }, new double[] { 20, 9 } );
final RealMaskRealInterval and = s.and( b );

System.out.println( "Min Bounds: " + and.realMin( 0 ) + ", " + and.realMin( 1 ) );
System.out.println( "Max Bounds: " + and.realMax( 0 ) + ", " + and.realMax( 1 ) );
// Min Bounds: 3.0, 3.0
// Max Bounds: 12.5, 9.0

// Move the sphere's center to (11.5, 5.5)
s.center().setPosition( new double[] { 11.5, 5.5 } );
System.out.println( "Min Bounds: " + and.realMin( 0 ) + ", " + and.realMin( 1 ) );
System.out.println( "Max Bounds: " + and.realMax( 0 ) + ", " + and.realMax( 1 ) );
		// Composite ROIs new bounds
// Min Bounds: 6.5, 2.0
// Max Bounds: 16.5, 9.0

// Move the box's center to (100, 100), such that it no longer
// intersects with the sphere
b.center().setPosition( new double[] { 100, 100 } );
System.out.println( "Is empty? " + and.isEmpty() );
// Is empty? true
// The two ROIs no longer intersect, so the composite is empty now
```

### Unary Operators

<table>
  <tbody>
    <tr>
      <caption style="caption-side:bottom; text-align: left; font-size: 0.9em; font-weight: normal;">
      <sup>1</sup> Transformation is affine<br>
      <sup>2</sup> Transformation is not affine
      </caption>
      <td><p><b>Operation</b></p></td>
      <td colspan=2><p><b>Operand has bounds?</b></p></td>
    </tr>
    <tr>
      <td></td>
      <td><p><b>yes</b></p></td>
      <td><p><b>no</b></p></td>
    </tr>
    <tr>
      <td><p><b>negate</b></p></td>
      <td>unbounded</td>
      <td>unbounded</td>
    </tr>
    <tr>
      <td><p><b>transform<sup>1</sup></b></p></td>
      <td>bounded</td>
      <td>unbounded</td>
    </tr>
    <tr>
      <td><p><b>transform<sup>2</sup></b></p></td>
      <td>unbounded</td>
      <td>unbounded</td>
    </tr>
  </tbody>
</table>

### Binary Operators

<table>
<tbody>
<tr>
<td>
<table>
  <tbody>
    <tr>
      <td colspan=3><p><b>And</b></p></td>
    </tr>
    <tr>
      <td colspan=3><p><b>Operand has bounds?</b></p></td>
    </tr>
    <tr>
      <td><p><b>Left</b></p></td>
      <td colspan=2><p><b>Right</b></p></td>
    </tr>
    <tr>
      <td></td>
      <td><p><b>yes</b></p></td>
      <td><p><b>no</b></p></td>
    </tr>
    <tr>
      <td><p><b>yes</b></p></td>
      <td>bounded</td>
      <td>bounded</td>
    </tr>
    <tr>
      <td><p><b>no</b></p></td>
      <td>bounded</td>
      <td>unbounded</td>
    </tr>
  </tbody>
</table>
</td>
<td>
<table>
  <tbody>
    <tr>
      <td colspan=3><p><b>Minus</b></p></td>
    </tr>
    <tr>
      <td colspan=3><p><b>Operand has bounds?</b></p></td>
    </tr>
    <tr>
      <td><p><b>Left</b></p></td>
      <td colspan=2><p><b>Right</b></p></td>
    </tr>
    <tr>
      <td></td>
      <td><p><b>yes</b></p></td>
      <td><p><b>no</b></p></td>
    </tr>
    <tr>
      <td><p><b>yes</b></p></td>
      <td>bounded</td>
      <td>bounded</td>
    </tr>
    <tr>
      <td><p><b>no</b></p></td>
      <td>unbounded</td>
      <td>unbounded</td>
    </tr>
  </tbody>
</table>
</td>
<td>
<table>
  <tbody>
    <tr>
      <td colspan=3><p><b>Or</b></p></td>
    </tr>
    <tr>
      <td colspan=3><p><b>Operand has bounds?</b></p></td>
    </tr>
    <tr>
      <td><p><b>Left</b></p></td>
      <td colspan=2><p><b>Right</b></p></td>
    </tr>
    <tr>
      <td></td>
      <td><p><b>yes</b></p></td>
      <td><p><b>no</b></p></td>
    </tr>
    <tr>
      <td><p><b>yes</b></p></td>
      <td>bounded</td>
      <td>unbounded</td>
    </tr>
    <tr>
      <td><p><b>no</b></p></td>
      <td>unbounded</td>
      <td>unbounded</td>
    </tr>
  </tbody>
</table>
</td>
<td>
<table>
  <tbody>
    <tr>
      <td colspan=3><p><b>Xor</b></p></td>
    </tr>
    <tr>
      <td colspan=3><p><b>Operand has bounds?</b></p></td>
    </tr>
    <tr>
      <td><p><b>Left</b></p></td>
      <td colspan=2><p><b>Right</b></p></td>
    </tr>
    <tr>
      <td></td>
      <td><p><b>yes</b></p></td>
      <td><p><b>no</b></p></td>
    </tr>
    <tr>
      <td><p><b>yes</b></p></td>
      <td>bounded</td>
      <td>unbounded</td>
    </tr>
    <tr>
      <td><p><b>no</b></p></td>
      <td>unbounded</td>
      <td>unbounded</td>
    </tr>
  </tbody>
</table>
</td>
</tr>
</tbody>
</table>

# Converting to RandomAccessible

It is also possible to convert **MaskPredicate**s to **(Real)RandomAccessible**s. The easiest way to do this is via the **Masks** class.

```java
final double[] center = new double[] { 10, 13, 22.25 };
final double[] semiAxisLengths = new double[] { 4, 5, 1 };
final double exponent = 6;
final SuperEllipsoid se = GeomMasks.closedWritableSuperEllipsoid( center, semiAxisLengths, exponent );

final RealRandomAccessibleRealInterval< BoolType > rrari = Masks.toRealRandomAccessibleRealInterval( se );
```

# Discussion

-   [G. Landini: Imglib or ImageJ2 and ROIs](https://groups.google.com/g/fiji-devel/c/AdeqZKffIUU/m/K8NRgKgk-WUJ) – ROIs should be drawn from the center of each pixel
-   [S. Preibisch: Imglib or ImageJ2 and ROIs - Where is a pixel?](https://groups.google.com/g/fiji-devel/c/AdeqZKffIUU/m/9SoisoaivWwJ) – Two kinds of ROIs: discrete and continuous
-   [D. White: Imglib or ImageJ2 and ROIs - A pixel is not a little square](https://groups.google.com/g/fiji-devel/c/AdeqZKffIUU/m/FU2Js4zNPG0J) – Alvy Ray's classic article
-   [J. Tinevez: ImageJ class hierarchy suggestions](https://groups.google.com/g/fiji-devel/c/E9SSt9z2zRQ/m/Slc1BLzuvtcJ) – a proposed interface-driven design for ROIs
-   [Implementation plan for Imglib2-rois 2D](https://forum.image.sc/t/implementation-plan-for-imglib2-rois-2d/2531) - forum discussion regarding ROI API
