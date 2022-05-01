---
mediawiki: Hough_Circle_Transform
title: Hough Circle Transform
categories: [Analysis]
extensions: ["mathjax"]
---


{% capture author%}
{% include person id='llamero' %}
{% endcapture %}

{% capture maintainer%}
{% include person id='llamero' %}
{% endcapture %}

{% capture source%}
{% include github org='llamero' repo='Local_Hough_Circle' %}
{% endcapture %}
{% include info-box name='Hough Circle Transform' software='plugin' update-site='UCB Vision Sciences' author=author maintainer=maintainer source=source released='February 4<sup>th</sup>, 2017' latest-version='September 21<sup>st</sup>, 2018 (v1.0.0)' status='stable, active' category='Analysis, Feature Extraction' %}

## Introduction

A {% include wikipedia title='Circle Hough Transform' text='Hough circle transform'%} is an image transform that allows for circular objects to be extracted from an image, even if the circle is incomplete. The transform is also selective for circles, and will generally ignore elongated ellipses. The transform effectively searches for objects with a high degree of radial symmetry, with each degree of symmetry receiving one "vote" in the search space. By searching a 3D Hough search space, the transform can measure the centroid and radius of each circular object in an image.

{%- include img src='hough-intro2' align='center' width='1000px' caption='**Hough circle transform is specific to circular objects.** *Left Panel:* This panel shown the input data for the Hough circle transform. The data includes (clockwise from top left) a circle (radius 37 pixels), a square (length 37 pixels), an ellipse (minor axis 37 pixels), and a sectored circle (radius 37 pixels).

*Right Panel:* This panel shows the output of a 24 step Hough circle transform. As you can see, the circle and the sectored circle converge to local maxima, while the square and ellipse do not, show the specificity of the transform for circular objects.' -%}

The method works by transforming an image around in a circle. Each time a transformed pixel with an intensity greater than zero lands on a Cartesian coordinate, that coordinate gets one vote. As the image continues to be transformed in a circle of a given radius, if a circle in the image has the same radius, then votes will accumulate at the centroid of this circle. Therefore, by finding the maxima in the transform (points with the highest number of votes) you can find the centroid of circles within the image. A Hough circle transform can also be used to find circles of an unknown radius by searching a 3D transform space, where the the third dimension is the range of radii to be tested.

## Image Processing Workflow

The Hough circle transform finds circles based on the rotational symmetry of the perimeter. Therefore, the data needs to be converted to this format for the transform to work.

{% include thumbnail src='/media/plugins/data-setup.png' title='**Data processing steps to perform a Hough circle transform on an XYZ stack.** *Panel 1:* Create an average intensity projection of the XYZ stack to generate a 2D projection. *Panel 2:* Use the "Find Edges" tool to preserve just the perimeter of each object. *Panel 3:* Threshold the image from panel 2 and create a binary mask. *Panel 4:* Run the Hough circle transform.'%}

### Step 0: Convert XYZ(T) data to XY(T) data

If the data is a 3D stack, then collapse the data to 2D space using a maximum, sum, or average intensity projection. The plugin can handle multiple frames (time-points) in a stack, but it can only search in 2D space.

### Step 1: Find Edges

If the circular objects are solid rather than hollow, take the derivative of the image by running: {% include bc path='Process | Find Edges'%}. This will preserve just the perimeter of each object.

### Step 2: Threshold

The algorithm does not weight the transform based on the intensity of the pixels, as this would result in bright, non-circular objects getting a very high score. Therefore, any pixel with an intensity &gt; 0 is given one vote per transform. This means that any pixel you do not want to be part of the transform needs to be set to zero, which is best done by thresholding the image and creating a mask by running: {% include bc path='Image | Adjust | Threshold'%}. After choosing the right threshold for the data press "Apply" to create a mask with an inverting LUT (0 is white, 255 is black). The LUT can be changed back to a normal gray-scale by going to {% include bc path='Image | Lookup Tables | Grays'%}.

### Step 3: Run the Hough Transform

Now you are ready to run the Hough transform (see below for detailed information on the various options). If the number of circles is unknown or varies from frame to frame, then the best option is to set the search to one circle and perform the transform with the output set to show the results table, and the centroids marked on the original image. This will give you the highest Hough score in the whole image, and will allow you to confirm that the circle found is correct and what its score was. If the circle is incorrect, adjust the search parameters to narrow the Hough search space.

If the circle found is correct, then gradually reduce the threshold until all the circles in the image are found. This will give you the upper threshold bound. Continue to decrease the threshold until an errant circle is detected, this will give you the lower threshold bound. Set the threshold between the upper and lower bounds, and then run the transform on the full data set.

## Running the Hough Circle Transform Plugin

The plugin runs on the current active image, and can also process stacks, but it cannot handle hyperstacks. The plugin is also recordable for macro implementation, and multi-threaded to fast searching on the 3D Hough space. The plugin can be cancelled at any time by either pressing the "Cancel" button in the GUI or pressing the "Escape" key.

The plugin has two separate algorithms available:

**Full Hough Transform: ** This algorithm performs a full Hough circle transform on every frame. The algorithm then searches for the highest scoring circle first, then the second highest, and so on. When a circle is found, the Hough transform space is cleared out around the found circle to prevent the same circle from being found repeatedly. This parameter can be adjusted to allow for increasing degrees of overlap between neighboring circles.

**Local Hough Transform: ** This algorithm is designed for high-speed tracking of circles in a time-lapse series. The algorithm performs the full Hough circle transform on the first frame to find the initial radius and position of each circle. In subsequent frames, the algorithm then only performs a Hough transform near the centroid of each circle in subsequent frames. If the number of found circles drops below the minimum number of specified circles, the algorithm performs a full Hough circle transform on the next frame to try and find any circles missed in the local search.

{% include thumbnail src='/media/plugins/hough-gui2.png' title='**Hough Circle Transform GUI configurations** *Panel 1:* Hough Circle transform - Easy Mode *Panel 2:* Hough Circle transform - Advanced Mode *Panel 3:* Local Hough Circle transform - Easy Mode *Panel 4:* Local Hough Circle transform - Advanced Mode'%}

### GUI Mode

The GUI has two available modes, "Easy" and "Advanced."

#### *Easy Mode*

This mode uses the minimal number of user input values necessary to run the transform. The remaining parameters are all defaulted to the most conservative values, such that all circles matching the criteria are found. To retrieve the default values, run the GUI in easy mode with the recorder turned on: {% include bc path='Plugins | Macros | Record...'%} This will return the value for every argument used in the search.

#### *Advanced Mode*

This mode is intended for a more fine tuned search, such as to better adapt the search space to your data, and/or increase the speed of the Hough transform. In this mode, all of the available search parameters are available, and the option to see the Raw Hough transform output also becomes available.

------------------------------------------------------------------------

### Search Parameters

The Hough circle plugin is designed to be adaptable to a variety of segmentation tasks, and as such, there are seven search parameters that can be adjusted to tune the search space.

#### *Minimum/maximum search radius*

The minimum and maximum search radii are the lower and upper cutoff for the radii you expect to find in the image. Ideally, you want to make the Hough search space as specific as possible, so be sure to set these values to specifically the range of radii you expect to find in your data.

#### *Radius search increment*

This determines the radius step size to use when creating the 3D Hough space from the minimum radius to the maximum radius. This allows a trade-off between speed and resolution, where larger steps will give a linear increase in speed, but also decrease the precision of the measured radii.

NOTE: This option is only available in advanced mode. In easy mode, this value defaults to 1.

#### *Maximum number of circles to be found*

This option sets the upper limit for the number of circles that can be found in the search. If there are fewer than the specified number of circles in the image with a score above the threshold (see below), then the algorithm will only return the number of circles that were above the threshold. Since the Hough space search starts with the highest scoring circle, and then the second highest, and so on, if there are a greater number of circles with a score above the threshold than the limit set in "Maximum number of circles to be found", only the highest scoring circles will be returned. This value is capped at 65535, since this is the largest number of circle IDs that can be generated at a 16-bit resolution.

NOTE: This option is only available in advanced mode. In easy mode, this value defaults to 65535.

#### *Hough score threshold*

This option sets the minimum cutoff for the Hough score (i.e. ratio of votes) that a circle can have to count as a valid object. This value is described as the following ratio:

  
$$\text{Hough score}=\left ( \frac{\text{number of votes}}{\text{transform resolution}} \right )$$

Since the maximum number of votes a circle can receive is the transform resolution (i.e. every transform resulted in a vote), the highest score a circle can receive is 1.0. Thus, the lower the score threshold, the more tolerant the search will be of incomplete and/or imperfect circles.

#### *Hough transform resolution*

This option sets the number of steps in each circle transform. To reduce unnecessary computation, if the resolution is set arbitrarily high (such as the default value of 1000), the algorithm will automatically find the nearest number of unique transforms possible (i.e. unique integer x,y coordinates) for the maximum radius, and will use this value as the actual resolution in the transform series (NOTE: This option can be turned off in Advanced Mode: see "Reduce transform resolution"). Reducing the resolution below the maximum value can greatly speed up the algorithm, but it will also decrease the transform's specificity and sensitivity.

NOTE: This option is only available in advanced mode. In easy mode, this value defaults to 1000.

{%- include img src='resolution-figure' align='center' width='1000px' caption='**Effect of transform resolution on distinguishing various n-gons.** *Panel 1* shows a circle and three regular polygons: a 4-gon, 8-gon, and 16-gon. *Panel 2* shows a Hough circle transform with four steps. Since all the shapes are radially symmetrical with 90° rotations, they all have an equal peak score at their centroids.

*Panel 3* shows a Hough circle transform with eight steps. Since the circle, 8-gon, and 16-gon radially symmetrical with 45° rotations, they all have an equal peak score at their centroids. These shapes have a higher score at their centroids than the 4-gon, because it lacks 45° radial symmetry.

*Panel 4* shows a Hough circle transform with sixteen steps. Only the circle and 16-gon are radially symmetrical at this resolution, so their centroids have equally high scores, while the 4-gon and 8-gon have significantly lower scores.

*Panel 5* shows a Hough circle transform with 400 steps. The centroid of the circle now has a higher score than all of the other shapes, allowing for the circle to be distinguished even from the 16-gon.' -%}

#### *Clear neighbors radius ratio*

The 3D Hough search space approaches a local maxima. Therefore, when a circle is found, the space around the local maxima needs to be removed to prevent the circle from being found a second time. The radius of the Hough search space that is cleared is defined as a ratio of the radius of the circle found, meaning that large circles clear out more Hough search space than small circles.

By default, this ratio is set to be one, meaning that a circle of the same size and location as the one found is cleared from the entire search space. This has the effect of eliminating all potential centroids within one radius of the found centroid. This effectively excludes overlapping circles of a similar radius from the search. To allow overlapping circles, this ratio can be reduced. A ratio of "0" will result in the same circle being found repeatedly. This means that perfectly concentric circles cannot be found in one run of the plugin, and rather need to be found iteratively by removing the found circles from the image and re-running the plugin.

NOTE: This option is only available in advanced mode. In easy mode, this value defaults to 1.0.

{%- include img src='clear-ratio2' width='1000px' align='center' caption='**Adjusting the clear radius ratio to find overlapping circles.**

The left panel shows the input data with a single circle on top and a pair of overlapping circles below. The next panel shows the resulting Hough circle transform (24 steps).

The top right pair of panels show the effect of a clear ratio of 1.0, where when the first overlapping circle is found, the centroid of the neighboring circle is removed, resulting in only two high scoring circles being found.

The bottom right pair of panels show the effect of a clear ratio of 0.2, where when the first overlapping circle is found, only its centroid is removed and the neighboring centroid is preserved for the neighboring circle to also be found, resulting in all three circles being found.' -%}

#### *Reduce transform resolution*

Since all images will be pixels in a Cartesian coordinate system, transforms can only be to discrete integer coordinates (i.e. x=5,y=10). Therefore, with an infinitely fine resolution, then when the next step of a transform is rounded to the nearest integer coordinate, it is possible that these are the same coordinates as the previous transform step. This means that when the transform is performed, it will perform identical transformations for both these steps.

To speed up a Hough transform, you can find and remove all of the redundant transform steps before performing the transform, keeping only the set of unique transform steps. The plugin performs this check by removing all redundant transform steps for the maximum search radius, and then setting this as the new resolution for the subsequent radii. This means the smaller radii will perform redundant transforms, but this is essential to ensure that each radius gets and equal number of voting rounds (or else large circles will always score higher than small circles).

While speeding up the algorithm, the trade-off is that the transform steps are distributed anisotropically for the maximum radius (all subsequent radii will be isotropic). Unchecking this box will result in the transform perform all of the specified transform steps, which can be be very computationally intensive for high resolution values.

NOTE: This option is only available in advanced mode. In easy mode, this option is selected by default.

------------------------------------------------------------------------

### Local Search Parameters

When using a Hough Transform to track circular objects over time, such as with pupil dilation or eye tracking, it is highly inefficient to calculate the full Hough Space and then search the full Hough space, since you know the object in the current frame is going to be roughly in the same position and have roughly the same radius as the corresponding object in the previous frame.

The local search algorithm takes advantage of this *a priori* information to greatly reduce the volume of the transform and search space in subsequent frames, allowing for many orders of magnitude increase in processing speed.

The local search algorithm is comprised of three sub-algorithms, depending on the state of the prior frame:

**Full - **For the first frame, a "full" Hough circle transform (the standard algorithm) is performed to find the initial radius and position of each circular object in the frame (up to the maximum number of circles set). The full Hough transform will also be used if the number of circular objects found in a given frame is 0.

**Local - **If the number of circular objects in the previous frame is greater than or equal to the minimum number of objects set, then the algorithm will use an exclusively local search to find the same circular objects in the next frame. The local algorithm performs a transform of only the nearby Hough space of the object found in the last frame, and then searches only this local space for the same object in the current frame.

**Partial Local - ** If the number of circular objects in the previous frame is less than the minimum number of objects set but greater than 0, then the algorithm will use a a hybrid search. A full Hough transform will be performed such that any missing circles will now be found. However, so speed up the search, the algorithm will first search locally within the Hough space for the same circular objects found in the previous frame, and then will search the entire Hough space for any remaining circular objects.

{%- include img src='local-search' width='1000px' align='center' caption='**Local versus full Hough transform.**

The left panel shows the input data with a single circle in the center of the image with a radius of 50 pixels. The center panel shows orthogonal projections of the full 3D Hough space. The radius search range was 10-110 pixels. The left panel shows a local Hough transform of the same circle, with a search area of 20x20 pixels, and a radius search range of +/- 10 pixels of the original circle radius. NOTE: In Hough space, the Z-dimension is the radius of the transform.' -%}

#### *Minimum number of circles to be found*

This value represents the minimum number of circles the Hough circle transform will search for before switching to using the partial or full search algorithms to find missing circles. For example, if the transform found 20 circles in the first frame, and the minimum is set to 10, then the algorithm will tolerate loosing track of 10 of the original circles before searching the full Hough space for the missing circles.

#### *Local radius search bandwidth (+/- previous radius)*

This value allows you to set the Z-axis of the local Hough search space. For example, if in your data you do not expect the radius of any circular object to change by more than 10 pixels in a single frame, then you would narrow the local search by entering 10. The local search will then search for a circular object of the same radius as in the previous frame +/- 10 pixels.

NOTE: This option is only available in advanced mode. In easy mode, this value defaults to the total radius search range (maximum search radius - minimum search radius).

#### *Local search radius for position of next centroid*

This value allows you to set the x,y axis search radius. For example, if in your data you do not expect the position of any circular object to change by more than 10 pixels in a single frame, then you would narrow the local search by entering 10. The local search will then search for a circular object of the same position as in the previous frame +/- 10 pixels.

NOTE: This option is only available in advanced mode. In easy mode, this value defaults to the minimum search radius.

------------------------------------------------------------------------

### Output Options:

The plugin contains several output options to both visualize the transform, as well as export the results of the analysis.

#### *Raw Hough transform series*

{% include thumbnail src='/media/plugins/raw-output.png' title=''%} This option will output a stack where each slice is the transform for specified radius. Each slice is also labelled with the radius (in pixels) and resolution in the header. If the inputted data was a multi-frame stack, then the transform will return a hyperstack, where the Z-dimension is each radius tested, and the T-dimension is each frame in the movie.

To save memory, the Hough scores are set to an 8-bit scale, with the highest score in the transform search space getting a value of 255 (i.e. no saturation). If the inputted data was a movie, each frame will be rescaled independently. However, while the scores are down-sampled to an 8-bit scale, a Hough transform adds an extra dimension to your dataset, so be sure you will have sufficient RAM if your movie and search space are large.

NOTE: This option is only available in advanced mode. this value defaults to 1.0.

#### *Circle centroid(s) marked on the original image*

{% include thumbnail src='/media/plugins/mask-output.png' title=''%} This option will draw a cross-hair pattern on each centroid found within the image, overlaid on a mask of the original image. This output is especially useful for optimizing the Hough seach parameters. The header of the image contains the number of circles that were found within the image. If the inputted data was not a mask, it will calculate a mask with a threshold of 1.

If the inputted data was a multi-frame stack, then the transform will return a stack, where the Z-dimension is each frame in the movie, and the header will show the number of circles found in each frame.

#### *Map of circle radius at centroids (pixel intensity = circle radius)*

{% include thumbnail src='/media/plugins/radius-output2.png' title=''%} This option returns an image where the centroid of each circle is marked by a single pixel whose intensity is equal to the radius of the circle, with the header of the image showing the number of circles that was found. To save memory, the image is formatted to 16-bit, meaning that the largest radius it can show is 65535 pixels. If you need to export larger radii, export the results to a results table (see below).

If the inputted data was a multi-frame stack, then the transform will return a stack, where the Z-dimension is each frame in the movie, and the header will show the number of circles found in each frame.

#### *Map of circle score at centroids (pixel intensity = circle score)*

This output is identical to the radius output (see above), however the pixel intensity is the Hough Score. To save memory, the image is formatted to 16-bit, meaning that the highest score it can show is 65535.

#### *Export measurements to the results table*

{% include thumbnail src='/media/plugins/results-output.png' title=''%} This will output the results of the transform to the results table. The measurements exported are: 1) the X and Y coordinates of each centroid, 2) the radius (in pixels) of each circle, 3) the Hough score for each circle, 4) the number of circles found within that frame, 5) the actual resolution that the transform used (this is also effectively the highest Hough score possible), and 6) the frame in which the circle was found.

If no circles were found in a frame, than that frame is excluded from the results table.

## Installing the Plugin

The Hough Circle Transform plugin is part of the [UCB Vision Sciences](UCB_Vision_Sciences) library. To install it, you just need to [ add](/update-sites/following#add-update-sites) the UCB Vision Sciences update site:

1\) Select {% include bc path='Help | Update...'%} from the Fiji menu to start the updater.

2\) Click on *Manage update sites*. This brings up a dialog where you can activate additional update sites.

3\) Activate the [UCB Vision Sciences](UCB_Vision_Sciences) update site and close the dialog. Now you should see additional jar files for download.

4\) Click *Apply changes* and restart Fiji.

You should now find the plugin under the sub-menu {% include bc path='Plugins | UCB Vision Sciences | Hough Circle Transform'%}.

NOTE: Hough Circle Transform is only one of the plugins included in the [UCB Vision Sciences](UCB_Vision_Sciences) suite. By following these installation steps, you will be installing as well the rest of plugins in the suite.

## Acknowledgements

This plugin is a modified version of the Hough circle transform implemented by [Hemerson Pistori and Eduardo Rocha Costa](https://imagej.nih.gov/ij/plugins/hough-circles.html). The transform algorithm was based off of an original implementation by [Mark Schulze](http://www.markschulze.net/).

This plugin was developed as part of the University of California, Berkeley Vision Sciences core grant NIH P30EY003176.

## Bug Report

April 5, 2018 - Fixed bug where the clear radius ratio was ignored.

September 21, 2018 - Fixed bug where repeated calls to the plugin would result in a memory leak.

## License

This program is **free software**; you can redistribute it and/or modify it under the terms of the **GNU General Public License** as published by the Free Software Foundation ([http://www.gnu.org/licenses/gpl.txt](http://www.gnu.org/licenses/gpl.txt)).

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

,

 
