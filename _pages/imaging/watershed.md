---
mediawiki: Nuclei_Watershed_Separation
title: Watershed Separation
section: Imaging
nav-links: true
---

Watershed separation is a technique for cutting apart connected components into
separate ones. It is often useful on blob-like structures such as cell nuclei.

## Watershed Separation of touching DAPI stained nuclei images -Tutorial

### Introduction to the problem

-   A very common biological sample for microscopy is DAPI stained DNA in cell nuclei. The staining delineates the nuclei pretty well, since in a metaphase cell there is DNA all over the nucleus. however, the staining is not homogenous, as there are areas of more or less condensation of the chromosomes. This makes the nuclei appear granular. Worse still, in many tissues that are interesting for developmental biology, the cells are tightly packed, and are composed mostly of nucleus with very little cytoplasm separating them. The nuclei often seem to touch each other, which in reality, of course, they can not. There is a membrane or two at least between them, but an optical microscope cannot resolve that. The {% include wikipedia title='Point spread function' text='PSF'%} is much bigger than the width of a membrane! Just to make matters even worse the image is quite noisy, because it was made with a fast scan on a confocal laser scanning microscope, which inherently has a low signal/noise ratio. That gives objects fuzzy edges and adds uncertainty to the intensity values of each pixel, making it harder to segment properly.

<!-- -->

-   So, we are faced with the problem of being able to separate apparently touching, noisy, objects :-(

<!-- -->

-   Luckily, there is a method for doing exactly that. The Watershed method.

<!-- -->

-   Okay, so how can we denoise, segment, watershed (separate touching objects) and then count / measure the objects in Fiji? Read on...

### Open the sample image

-   open the [sample image of touching DAPI stained cell nuclei from a confocal laser scanning microscope.](/media/nucleidapiconfocal.png)

    {% include img src="nucleidapiconfocal" width=250 %}

-   Run a [Gaussian Blur filter](http://imagejdocu.list.lu/doku.php?id=gui:process:filters) on the image to blur out the "speckle", actually Poisson distributed, statistical "photon {% include wikipedia title='Shot noise' text='shot noise'%}", and also to smooth out the inhomogeneity of the nuclear staining. We will use a large sigma value of 3 for this task. A value of sigma too small will mean that the segmentation will be disturbed by the noise and staining pattern. Too high a sigma value, and the objects will be too blurred, making it harder to find their edges precisely and separate them later. Run menu command: Process - Filters - Gaussian Blur, with a sigma value of 3 pixels. You can preview other values to see how they look also. You should get an image that looks like this:

    {% include img src="nucleidapiconfocalgauss3pxsigma" width=250 %}

### Pixel Intensity Threshold - find the foreground areas

-   Next we need to separate the objects from the background using pixel intensity thresholding. Fiji has a number of built in [Automatic Thresholding](/plugins/auto-threshold) methods that try to distinguish the background from the foreground. In this case the default method works pretty well, but you can see there is a long list of methods, which give slightly different threshold results for this image. You can play with different methods if you like. You might get a different answer in the end!

<!-- -->

-   Do menu command Image - Adjust - Threshold. Turn on the check box for "Dark background" . Indeed, in this case the background is dark! The default method will be previewed automatically when you launch the menu command, and a threshold will be set, something close to 100 intensity. If you are happy with the automatically calculate threshold, then click "Apply", which will give you a binary image. Black is background, and white is foreground. It should look like this:

    {% include img src="nucleidapiconfocalautodefaultthresh" width=250 %}

-   So far so good... But we still don't have objects... only background and foreground pixels. Also it is clear that some nuclei are connected to adjacent ones... and we want them to be separated. We will use the watershed method built into Fiji for that:

### Watershed algorithm - separate touching objects

-   To run the built in [ImageJ watershed method](https://imagej.nih.gov/ij/docs/menus/process.html#watershed) choose menu item: Process - Binary - Watershed. This method finds the centre of each object (using a morphological erode operation), then calculates a distance map from the object centre points to the edges of the objects, then fills that "topological map" with imaginary water. Where 2 "Watersheds" meet, it builds a dam to separate them! One could do all these steps manually, but the watershed function automates that for you, which is nice. Your watershed image should look like this:

    {% include img src="nucleidapiconfocalwatershed" width=250 %}

-   Notice how the nuclei have been split away from each other. This method only works robustly for roughly circular objects. Why?

### Analyze the segmented objects

-   Now you have a set of white foreground patches of white pixels, surrounded by black background pixel areas, and we have separated touching objects with a watershed, which put "dams" one pixel wide between the objects.

-   Next we must run the Analyze Particles tool in Fiji to locate patches of white pixels and count them. But... that tool needs black objects on a white background or a threshold to be set on the image which contains the desired objects. To invert the image do Edit - Invert, or to threshold the binary image, again do Image - Adjust - Threshold (Since the image now contains only two intensities (0 and 255), the threshold default is of course correct, and the objects appear in thresholded red, for black background again of course).

-   Now choose menu item [{% include bc path="Analyze | Analyze Particles" %}](https://imagejdocu.list.lu/doku.php?id=gui:analyze:analyze_particles), using the settings in the screen shot below.

    {% include img src="nulceidapiconfocalanalyzeparticles" width=500 %}

-   You can filter out different sizes of particles. For example, you might only be interested in large objects, like nuclei. So you can exclude small objects that you know are junk. Change the area number range in the Size field and see what happens.

-   You can choose to count only those objects which are very circular by changing the Circularity range numbers to say 0.8-1. You could make it look for non circular objects too! How? Play with it, see what it does.

-   Use show outlines, or test the other options there if you like. Exclude on edges is very smart. It means you don't get nonsense results from objects that are chopped off at the edges of the image, and as such are of course smaller than they really are.

-   You can add all the objects to the ROI manager, by turning on Add to Manager. Then you could use those ROIs to measure the intensities of the signal in the objects of the original image. Can you figure out how to do that?

-   It also spits out lots of useful statistics:

    {% include img src="nulceidapiconfocalsegmentationresults" width=700 %}
