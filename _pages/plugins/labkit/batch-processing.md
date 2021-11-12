---
title: Labkit - How To Use Labkit In An ImageJ Macro?
---

# Labkit - How To Use Labkit In An ImageJ Macro?

Automatic image segmentation can be used to segment a large number of images. Beforehand, make sure of the following:

- Images must be similar in order to get reproducible results
- Brightness and contrast must be normalized across images
- (Optional) background removal can improve results
- Select a representative image

Open the representative image with Labkit and segment the image as described in the [quick automatic segmentation](). Save the trained classifier {% include bc path="Segmentation | Save Classifier ..." %} into a file. Finally, you can use the following ImageJ macro to automatically segment images with the trained classifier.

```java
// ImageJ macro for segmenting a list of images
folder = "C:/path/to/folder/"
for (i = 0; i < 10; i++) {
   open(folder + "image_" + i + ".tif");
   run("Segment Image With Labkit", "segmenter_file=" + folder + "my_pretrained_classifier.classifier use_gpu=false");
   saveAs("Tiff", folder + "segmentation_" + i + ".tif");
   close();
   close();
}
```

