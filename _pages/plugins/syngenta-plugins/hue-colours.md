# [Syngenta Plugins](/plugins/syngenta-plugins) > Hue Colours Plugin

This plug-in provides the ability to segment images in colour-space.

The filter can be found under the ImageJ Plugins menu:

Plugins > Segmentation > Hue Colours

To invoke the filter from a macro use the following, e.g.

`run("Hue Colours", "<parameter values>");`

To invoke the filter programmatically use the `PlugInFilterRunner`, e.g.

```java
import ij.ImagePlus;
import ij.WindowManager;
import ij.io.Opener;
import ij.plugin.filter.PlugInFilter;
import ij.plugin.filter.PlugInFilterRunner;

import com.syngenta.imagej.plugins.imagecolours.HueColoursFilter;

// Open an image and make it current image.
final ImagePlus image=new Opener().openImage(inputImagePath);
        WindowManager.setTempCurrentImage(image);

// Create and apply the filter to the current image.
final PluginFilter filter=new HueColoursFilter();
        new PlugInFilterRunner(filter,"","");
```
