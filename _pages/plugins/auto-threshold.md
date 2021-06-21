---
mediawiki: Auto_Threshold
title: Auto Threshold
categories: [Segmentation]
artifact: sc.fiji:Auto_Threshold
---

This plugin binarises 8 and 16-bit images using various **global** (histogram-derived) thresholding methods. The segmented phase is always shown as white (255).

For **local** thresholding rather than global, see the [Auto Local Threshold](/plugins/auto-local-threshold) plugin.

## Installation

**ImageJ**: requires v1.42m or newer. Download [Auto_Threshold-X.Y.Z.jar](https://maven.scijava.org/service/local/artifact/maven/redirect?r=releases&g=sc.fiji&a=Auto_Threshold&v=RELEASE&e=jar) and copy it into the ImageJ/plugins folder and either restart ImageJ or run the '{% include bc path='Help | Update Menus'%}' command. After this a new command should appear in '{% include bc path='Image | Adjust | Auto Threshold'%}'.

**Fiji**: this plugin is part of the Fiji distribution, there is no need to download it.

## Use

**Method** selects the algorithm to be applied (detailed below).

The **Ignore black** and **Ignore white** options set the image histogram bins for [0] and [255] greylevels to 0 respectively. This may be useful if the digitised image has under- or over- exposed pixels.

**White object on black background** sets to white the pixels with values above the threshold value (otherwise, it sets to white the values less or equal to the threshold).

**Set Threshold instead of Threshold (single images)** sets the thresholding LUT, without changing the pixel data. This works only for single images.

It you are processing a stack, two additional options are available: **Stack** can be used to process all the slices (the threshold of each slice will be computed separately). If this option is left unchecked, only the current slice will be processed. **Use stack histogram** first computes the histogram of the whole stack, then computes the threshold based on that histogram and finally binarises all the slices with that single value. Selecting this option also selects the **Stack** option above automatically.

**Important notes:**

**1.** This plugin is accessed through the {% include bc path='Image | Auto Threshold'%} menu entry, however the thresholding methods were also partially implemented in ImageJ's thresholder applet accessible through the {% include bc path='Image | Adjust | Threshold...'%} menu entry. While the Auto Threshold plugin can use or ignore the extremes of the image histogram (Ignore black, Ignore white) the applet cannot: the 'default' method ignores the histogram extremes but the others methods do not. This means that applying the two commands to the same image can produce apparently different results. In essence, the Auto Threshold plugin, with the correct settings, can reproduce the results of the applet, but not the way round.

**2.** From version 1.12 the plugin supports thresholding of 16-bit images. Since the Auto Threshold plugin processes the full greyscale space, it can be slow when dealing with 16-bit images. Note that the ImageJ thresholder applet also processes 16-bit images, but in reality ImageJ first computes a histogram with 256 bins. Therefore, there might be differences in the results obtained on 16-bit images when using the applet and the true 16-bit results obtained with this plugin. Note that for speeding up, the histogram is bracketed to include only the range of bins that contain data (and avoid processing empty histogram bins at both extremes).

**3.** The result of 16 bit images and stacks (when processing all slices) is an 8 bit container showing the result in white [255] to comply with the concept of "binary image" (i.e. 8 bits with 0 and 255 values). However, for stacks where only 1 slice is thresholded, the result is still a 16 bit container with the thresholded phase shown as white [65535]. This is to keep the data untouched in the remaining slices. The "Try all" option retains the 16 bit format to still show the images with methods that might fail to obtain a threshold. Images and stacks that are impossible to threshold remain unchanged.

**4.** The same image in 8 and 16 bits (without *scaling*) returns the same threshold value, however Li's method originally would return different values when the image data was *offset* (e.g. when adding a fixed value to all pixels). The current implementation avoids this offset-dependent problem.

**5.** The same image *scaled* by a fixed value (e.g. when multiplying all pixels by a fixed value) returns a similar threshold result (within 2 greyscale levels of the original unscaled image) for all methods except Huang, Li and Triangle due to the way these algorithms work. E.g. the Triangle method applied to an 8 bit image and to the same image converted to 16 bits *with scaling* can result in different threshold values. This is because the scaling from 8 to 16 bits creates empty bins in between the scaled grey values. The Triangle method (based on a geometric approach) finds those artefactual gaps in the new 16 bit histogram which satisfy the method constraints, but which would not exist in the original 8 bit image. This cannot be prevented (for example by detecting empty histogram bins) as it would interfere with the analysis when real empty bins (as oppose to artefactual ones) exist in the image.

## Available methods

### Try all

Which method segments your data best? One can attempt to answer this question using the **Try all** option. This produces a montage with results from all the methods, allowing to explore how the different algorithms perform on a particular image or stack. When using stacks, in some cases it might not be a good idea to segment each slice individually rather than with a single threshold for all slices (try the mri-stack.tif from the sample images to better understand this issue).

![](/media/lymp.png)

Original image

![](/media/plugins/lympm2.png)

Try all methods.

When processing stacks with many slices, the montages can become very large (~16 times the original stack size) and one risks running out of RAM. A popup window will appear (when stacks have more than 25 slices) to confirm whether the procedure should display the montaged results. Select **No** to compute the threshold values and display them in the log window.

### Default

This is the original method of auto thresholding available in ImageJ, which is a variation of the IsoData algorithm (described below). The **Default** option should return the same values as the '{% include bc path='Image | Adjust | Threshold | Auto'%}', when selecting **Ignore black** and **Ignore white**. To indicate segmentation of the desired phase, use the **White objects on black background** option. The IsoData method is also known as *iterative intermeans*.

### Huang

Implements Huang's fuzzy thresholding method. This uses Shannon's entropy function (one can also use Yager's entropy function).

{% include citation doi='10.1016/0031-3203(94)E0043-K' %} ([PDF](http://www.ktl.elf.stuba.sk/study/vacso/Zadania-Cvicenia/Cvicenie_3/TimA2/Huang_E016529624.pdf))

Ported from ME Celebi's fourier_0.8 routines [1](http://sourceforge.net/projects/fourier-ipal) and [2](http://www.lsus.edu/faculty/~ecelebi/fourier.htm).

### Huang2

This is an alternative implementation of Huang's method by J. Schindelin with an impressive speed advantage on 16 bit images. On some images, however the method gives returns different values than the original Huang method above.

### Intermodes

This assumes a bimodal histogram. The histogram is iteratively smoothed using a running average of size 3, until there are only two local maxima: j and k. The threshold t is then computed as (j+k)/2. Images with histograms having extremely unequal peaks or a broad and flat valley are unsuitable for this method. method

{% include citation doi='10.1111/j.1749-6632.1965.tb11715.x' %}

Ported from Antti Niemistö's [MATLAB](/scripting/matlab) code. See [here](https://github.com/carandraug/histthresh) for an excellent slide presentation and his original [MATLAB](/scripting/matlab) code.

### IsoData

Iterative procedure based on the isodata algorithm of:

{% include citation doi='10.1109/TSMC.1978.4310039' %}

The procedure divides the image into object and background by taking an initial threshold, then the averages of the pixels at or below the threshold and pixels above are computed. The averages of those two values are computed, the threshold is incremented and the process is repeated until the threshold is larger than the composite average. That is,

```java
threshold = (average background + average objects)/2.
```

Several implementations of this method exist. See the source code for further comments.

### Li

Implements Li's Minimum Cross Entropy thresholding method based on the iterative version (2nd reference below) of the algorithm.

{% include citation doi='10.1016/0031-3203(93)90115-D' %}

{% include citation doi='10.1016/S0167-8655(98)00057-9' %} ([PDF](http://corkfits.net.temporary-domain.com/Articles/files/Li1998.pdf))

{% include citation doi='10.1117/1.1631315' %}

Ported from ME Celebi's fourier_0.8 routines [3](http://sourceforge.net/projects/fourier-ipal) and [4](http://www.lsus.edu/faculty/~ecelebi/fourier.htm).

### MaxEntropy

Implements Kapur-Sahoo-Wong (Maximum Entropy) thresholding method:

{% include citation doi='10.1016/0734-189X(85)90125-2' %}

Ported from ME Celebi's fourier_0.8 routines [5](http://sourceforge.net/projects/fourier-ipal) and [6](http://www.lsus.edu/faculty/~ecelebi/fourier.htm).

### Mean

Uses the mean of grey levels as the threshold. It is used by some other methods as a first guess threshold.

{% include citation doi='10.1006/cgip.1993.1040' %}

### MinError(I)

An iterative implementation of Kittler and Illingworth's Minimum Error thresholding.

This implementation seems to converge more often than the original. Nevertheless, sometimes the algorithm does not converge to a solution. In that case a warning is reported to the log window and the result defaults to the initial estimate of the threshold which is computed using the Mean method. The **Ignore black** or **Ignore white** options might help to avoid this problem.

{% include citation doi='10.1016/0031-3203(86)90030-0' %}

Ported from Antti Niemistö's [MATLAB](/scripting/matlab) code. See [here](http://www.cs.tut.fi/~ant/histthresh/) for an excellent slide presentation and the original [MATLAB](/scripting/matlab) code.

### Minimum

Similarly to the Intermodes method, this assumes a bimodal histogram. The histogram is iteratively smoothed using a running average of size 3, until there are only two local maxima. The threshold t is such that yt−1 &gt; yt &lt;= yt+1.

Images with histograms having extremely unequal peaks or a broad and flat valley are unsuitable for this method.

{% include citation doi='10.1111/j.1749-6632.1965.tb11715.x' %}

Ported from Antti Niemistö's [MATLAB](/scripting/matlab) code. See [here](http://www.cs.tut.fi/~ant/histthresh/) for an excellent slide presentation and the original [MATLAB](/scripting/matlab) code.

### Moments

Tsai's method attempts to preserve the moments of the original image in the thresholded result.

{% include citation doi='10.1016/0734-189X(85)90133-1' %}

Ported from ME Celebi's fourier_0.8 routines [7](http://sourceforge.net/projects/fourier-ipal) and [8](http://www.lsus.edu/faculty/~ecelebi/fourier.htm).

### Otsu

Otsu's threshold clustering algorithm searches for the threshold that minimizes the intra-class variance, defined as a weighted sum of variances of the two classes.

{% include citation doi='10.1109/TSMC.1979.4310076' %}

See also the {% include wikipedia title="Otsu's_method" text="Wikipedia article on Otsu's method" %}.

Ported from C++ code by Jordan Bevik.

### Percentile

Assumes the fraction of foreground pixels to be 0.5.

{% include citation doi='10.1145/321119.321123' %}

Ported from Antti Niemistö's [MATLAB](/scripting/matlab) code. See [here](http://www.cs.tut.fi/~ant/histthresh/) for an excellent slide presentation and the original [MATLAB](/scripting/matlab) code.

### RenyiEntropy

Similar to the **MaxEntropy** method, but using Renyi's entropy instead.

{% include citation doi='10.1016/0734-189X(85)90125-2' %}

Ported from ME Celebi's fourier_0.8 routines [9](http://sourceforge.net/projects/fourier-ipal) and [10](http://www.lsus.edu/faculty/~ecelebi/fourier.htm).

### Shanbhag

{% include citation doi='10.1006/cgip.1994.1037' %}

Ported from ME Celebi's fourier_0.8 routines [11](http://sourceforge.net/projects/fourier-ipal) and [12](http://www.lsus.edu/faculty/~ecelebi/fourier.htm).

### Triangle

This is an implementation of the Triangle method:

{% include citation doi='10.1177/25.7.70454' %}

Modified from Johannes Schindelin's plugin [Triangle_Algorithm](http://wbgn013.biozentrum.uni-wuerzburg.de/ImageJ/triangle-algorithm.html).

See also: http://www.ph.tn.tudelft.nl/Courses/FIP/noframes/fip-Segmenta.html#Heading118

The Triangle algorithm, a geometric method, cannot tell whether the data is skewed to one side or another, but assumes a maximum peak (mode) near one end of the histogram and searches towards the other end. This causes a problem in the absence of information of the type of image to be processed, or when the maximum is not near one of the histogram extremes (resulting in two possible threshold regions between that max and the extremes). Here the algorithm was extended to find on which side of the max peak the data goes the furthest and searches for the threshold within that largest range.

### Yen

Implements Yen's thresholding method from:

{% include citation doi='10.1109/83.366472' %}

{% include citation doi='10.1117/1.1631315' %}

Ported from ME Celebi's fourier_0.8 routines [13](http://sourceforge.net/projects/fourier-ipal) and [14](http://www.lsus.edu/faculty/~ecelebi/fourier.htm).
