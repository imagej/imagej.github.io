---
title: Labkit guidelines

---

# Guidelines

(In progress)

These guidelines are meant to help users improve their automatic segmentation pipeline.

## Labeling the image

### Label important features of each class

<!---  Examples of labeling (eg objects too dim are labeled to background, background between two objects) -->

### Do not over label

<!--- Explain impact of over labeling on the segmentation -->

## Pixel Classification Settings

Labkit's pixel classification algorithm applies a list of filters on the image to gather informations about the individual pixels.
The pixel classification settings dialog allows to select which filters Labkit uses.
The default settings should normally work well.
But selecting the filters manually might in some cases help to improve the runtime or the quality of the resulting segmentations.

Most of the filters first apply a gaussion blur on the image before they perform their individual operations.
Select sigma values that are in the range of your object sizes. For example if you want to segment blob-like structures. Where the blobs diameter is roughly 10, then this value divided by 2 is a good sigma value to use respective sigma = 5. But also add values that are smaller, and bigger sigmas = 1.25; 2.5; 5; 10 would be a good way to go. The pixel classification is slower for high sigma values, sigma shouldn’t be bigger than 16.

| Feature name          | Runtime / Complexity | Remarks |
| --------------------- | -------------------- | ------- |
| original image        | very low             | Always useful |
| gaussian blur         | low                  | Always useful, they work well on images that are easy to segment. |
| difference of gaussians | low | ^ |
| gaussian gradient magnitude | low | ^ |
| laplacian of gaussian | moderate | Useful for images that are harder to segment, might help to segment close gaps. |
| hessian eigenvalues | moderate | ^ |
| structure tensor eigenvalues | high | Similar to hessian eigenvalues but slow. Use only if it really helps on your images. |
| min, max, mean | low | Use special cases. |
| variance | moderate | Useful to segment objects with a rough texture. |

