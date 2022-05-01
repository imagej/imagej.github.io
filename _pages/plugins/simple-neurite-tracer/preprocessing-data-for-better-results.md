---
mediawiki: Simple_Neurite_Tracer:_Preprocessing_Data_for_Better_Results
title: Simple Neurite Tracer › Preprocessing Data for Better Results
nav-links: true
nav-title: Preprocessing Data
---

{% include warning/deprecated new="[SNT](/plugins/snt)"
  old="[Simple Neurite Tracer](/plugins/simple-neurite-tracer)" %}

Simple Neurite Tracer's "Hessian-based analysis" option for filtering for tube-like structures is an quick way of improving the efficiency and accuracy of path-finding. However, for best results, I would recommend using a slower but more accurate method to preprocess the data.

## Using Pre-Processed Data

If the file you are tracing was originally called "example.tif" or "example.lsm", then the plugin will check for the existence of a file in the same directory called "example.tubes.tif". If such a file exists, the plugin will offer to load it for you:

![](/media/plugins/simple-neurite-tracer/snt-confirm-tubes-tif.png)

The "\*.tubes.tif" file must be a 32-bit float image. Then, if you select the "Use preprocessed image" option:

![](/media/plugins/simple-neurite-tracer/snt-use-preprocessed-image.png)

... then tracing will take place on the preprocessed image rather than the raw image data or the "Hessian-based analysis" filtered values.

## An Example Using Frangi et al.'s method

### A single image

To process a single image, load your image ("test.lsm", say) into Fiji and select {% include bc path='Plugins | Process | Frangi Vesselness'%}. (There is more information about this plugin [on its page](/plugins/frangi).) By way of example, let's say that you select 4 scales from half the x voxel separation to twice that value.

Then save that file in the same directory as "test.tubes.tif".

When you start up Simple Neurite Tracer with "test.lsm" as the current image, it will offer to load the preprocessed image you have just generated.

### Preprocess Multiple Images

The easiest way to preprocess multiple images is to record a macro for processing a single images, and then wrap it it in a loop to iterate over all the files in a directory. For example:

```javascript
d = getDirectory("Select a directory");
files = getFileList(d);

extension = ".tif";

for( i = 0; i < files.length; ++i ) {
    filename = files[i];
    if( endsWith(filename,extension) ) {
        l = lengthOf(filename);
        el = lengthOf(extension);
        basename = substring(filename,0,l-el);
        expected_window_name = "vesselness of "+filename;
        output_filename = d + File.separator + basename + ".tubes.tif";
        open(filename);
        run("Frangi Vesselness (imglib, experimental)", "number=1 minimum=0.288387 maximum=0.288387");
        selectWindow(expected_window_name);
        saveAs("Tiff", output_filename);
    }
}
```
