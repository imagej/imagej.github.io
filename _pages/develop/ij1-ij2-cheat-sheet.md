---
title: ImageJ-ImageJ2 cheat sheet
project: /software/imagej2
---

This page summarizes translation of basic operations of [ImageJ 1.x](/software/imagej) and [ImageJ2](/software/imagej2) API. Based on the work of {% include person id='haesleinhuepf' %}, Scientific Computing Facility, MPI-CBG Dresden.

{::nomarkdown}
<table>
  <thead>
    <tr class="header">
      <th style="text-align:left; min-width: 10em;">
        <p><strong>Task</strong></p>
      </th>
      <th>
        <p><strong>ImageJ</strong></p>
      </th>
      <th>
        <p><strong>ImageJ2</strong></p>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <p>Starting ImageJ</p>
      </td>
      <td>
{%- highlight java -%}
new ij.ImageJ();
{%- endhighlight -%}
      </td>
      <td>
{%- highlight java -%}
ImageJ ij = new net.imagej.ImageJ();
ij.ui().showUI();
{%- endhighlight -%}
      </td>
    </tr>
    <tr>
      <td>
        <p>Show images</p>
      </td>
      <td>
        <p><code>imp</code> is an <code>ImagePlus</code> object</p>
{%- highlight java -%}
imp.show();
{%- endhighlight -%}
      </td>
      <td>
{%- highlight java -%}
ij.ui().show(imp);
ImageJFunctions.show(imp);
ImageJFunctions.wrap(imp,"Image").show();
{%- endhighlight -%}
      </td>
    </tr>
    <tr>
      <td>
        <p>Retrieve an active image object</p>
      </td>
      <td>
{%- highlight java -%}
ImagePlus imp = IJ.getImage();
{%- endhighlight -%}
      </td>
      <td>
        <p>Script parameter (the same for <code>Dataset</code>, <code>ImagePlus</code>, etc.):</p>
{%- highlight plain -%}
#@ Img image
{%- endhighlight -%}
        <p>In Java code:</p>
{%- highlight java -%}
@Parameter
private Img image;
{%- endhighlight -%}
        <p>Using <code>ImageDisplayService</code>:</p>
{%- highlight java -%}
Dataset image = ij.imageDisplay().getActiveDataset();
{%- endhighlight -%}
      </td>
    </tr>
    <tr>
      <td>
        <p>Open an image file</p>
      </td>
      <td>
        <p><code>IJ.openImage()</code> returns an <code>ImagePlus</code> object without showing.</p>
{%- highlight java -%}
ImagePlus imp = IJ.openImage(urlOrFilePath);
imp.show();
{%- endhighlight -%}
        <p><code>IJ.open()</code> automatically shows the image without returning <code>ImagePlus</code>.</p>
{%- highlight java -%}
IJ.open(urlOrFilePath);
ImagePlus imp = IJ.getImage();
{%- endhighlight -%}
      </td>
      <td>
        <p>Using <code>IOService</code>:</p>
{%- highlight java -%}
Object image = ij.io().open(urlOrFilePath);
{%- endhighlight -%}
        <p>Using <code>DatasetIOService</code> (for type safety):</p>
{%- highlight java -%}
Dataset image = ij.scifio().datasetIO().open(urlOrFilePath);
{%- endhighlight -%}
      </td>
    </tr>
    <tr>
      <td>
        <p>Save an image file</p>
      </td>
      <td>
{%- highlight java -%}
IJ.saveasTiff(imp, "/path/to/image.tif")
{%- endhighlight -%}
      </td>
      <td>
        <p>Using <code>IOService</code>:</p>
{%- highlight java -%}
ij.io().save(dataset, "/path/to/image.tif");
{%- endhighlight -%}
        <p>Using <code>DatasetIOService</code>:</p>
{%- highlight java -%}
ij.scifio().datasetIO().save(dataset, "/path/to/image.tif");
{%- endhighlight -%}
      </td>
    </tr>
    <tr>
      <td>
        <p>Convert image types</p>
      </td>
      <td>
        <p>Convert from ImgLib2 <code>Img</code> object to ImageJ <code>ImagePlus</code> object:</p>
{%- highlight java -%}
ImagePlus imp = ImageJFunctions.wrap(img,"Title");
{%- endhighlight -%}
      </td>
      <td>
        <p>Convert from ImageJ <code>ImagePlus</code> object to ImgLib2 <code>Img</code> object:</p>
{%- highlight java -%}
Img img = ij.convert().convert(imp, Img.class);
Img<T> realImg = ImageJFunctions.wrapReal(imp);
Img<FloatType> floatImg = ImageJFunctions.convertFloat(imp);
Img<FloatType> realImg2 = ImageJFunctions.wrap(imp);
{%- endhighlight -%}
      </td>
    </tr>
    <tr>
      <td>
        <p>Show regions</p>
      </td>
      <td>
{%- highlight java -%}
imagePlus.setRoi(roi);
{%- endhighlight -%}
      </td>
      <td>
{% highlight java %}
Img<BitType> mask; // = ...
Roi roi = ij.convert().convert(mask, Roi.class);
imagePlus.setRoi(roi);
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td>
        <p>Run plugins</p>
      </td>
      <td>
{%- highlight java -%}
IJ.run(imagePlus,"Normalisation","");
{%- endhighlight -%}
      </td>
      <td>
{%- highlight java -%}
ij.command().run(ImageNormalizerIJ2Plugin.class, true,
                 "input", img, "ij", ij);
{%- endhighlight -%}
      </td>
    </tr>
    <tr>
      <td>
        <p>Define plugins</p>
      </td>
      <td>
{%- highlight java -%}
public class ImageNormalizerPlugin implements PluginFilter {
  ...
}
{%- endhighlight -%}
        <p>In <code>resources/plugins.config</code>:</p>
{%- highlight plain -%}
Plugins>Filtering, "Normalisation", NormalizerPlugin
{%- endhighlight -%}
      </td>
      <td>
{%- highlight java -%}
@Plugin(type = Command.class, menuPath = "Plugins>Normalization")
public class ImageNormalizerIJ2Plugin implements Command {
  ...
}
{%- endhighlight -%}
      </td>
    </tr>
  </tbody>
</table>
{:/}

## See also

{% include github org="mpicbg-scicomp" repo="ij2course-images" branch='master' path="slides/ij_legacy_cheetsheet.pdf" %}
