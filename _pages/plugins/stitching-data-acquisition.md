---
mediawiki: Stitching_data_acquisition
title: Stitching data acquisition
categories: [Uncategorized]
---

# WiscScan Data Acquisition

{% include img src="/media/ows-1.jpg" align="right" width="300" caption="Microscope setup" %}

1.  Make sure the image being used has been set up correctly:
    1.  On the computer, click and hold the shutter button until it turns yellow. The shutter is now activated
    2.  Ensure the the outer shutter lever is pointing towards "Lamp" and the inner shutter lever is pointing to the right
    3.  Turn on the xyz controller

    -   NOTE: Do not attempt to adjust the focus of the image with the manual knob while the controller is engaged. You will wear down the gears.
        </ol>
2.  Move the outer shutter lever toward "Image" and the inner shutter lever toward
3.  Turn on the Pockel Power Cell
4.  Turn on the Ti Sapph Shutter Controller
5.  Log in to WiscScan
6.  Turn on the detector

-   Note: DO NOT turn on the detector till the main lights are off. You WILL damage the detector.

<li>

Start Scan and ensure your image is in focus on the left side of your screen&lt;\\li&gt;

<li>

Use the computer xyz controller to choose your initial image frame

</li>
<li>

Adjust the pockle cell dials until you can see an image on the right side of your screen (the blue portion)

</li>
<li>

Adjust the detector so that only a small amount of red can be seen in the frame of your image. If too much of a contrast is present, it will burn out the microscope's laser

</li>

-   Note: The normal range for the detector is 300-500. You should not go above 620.

 

<li>

Stop scan

</li>

 

<li>

Define the start position in your metadata by selecting "manual update" then "set 0"

</li>

 

<li>

Generate the specifics of your image acquisition using generate grid

</li>
<li>

Set the size of each image taken (in microns)

</li>
<li>

Set the amount of overlap you wish to have in your image, then press "calculate number of positions"

</li>

-   NOTE- You can also set your own step size and overlap amount and calculate the size of each image

<li>

Once you have calculated all the necessary positions, you can save this data using the "save positions" button and load them back into WiscScan at a later date

</li>
<li>

Select Z motor

</li>
<li>

under 4d imaging, calculate Z bottom, Z top, and Z step

</li>
<li>

These numbers should be set as 0 unless you are imaging in more than one plane of your sample

</li>
<li>

Select "Use XY coordinates" and then start sequence

</li>
<li>

Once WiscScan has run, your output will be a series of images that can be stitched together.

</li>

-   NOTE- If an noticeable amount of overlay can be seen in your images, there is a pixel to micron error within the microscope's initial setup. To fix this, recalibrate the microscope's objectives. 

## Generate the grid

{% include img src="basicgrid" align="right" width="250" caption="BasicGrid.png" %}

### The basic grid

1.  Fill in the Dimensions of X and Y in \#X and \#Y respectively

{% include img src="overlappedgrid" align="right" width="250" caption="OverlappedGrid.png" %}

<li>

Enter the step size in microns

</li>
<li>

Select "Calculate total size from \# Pos" to find the total size of your stitched image (optional)

</li>
<li>

Select "OK"

</li>
</ol>

### Percent overlapped grid

1.  Use the "Compute overlap slider" to set the overlap percentage you would like within your stitched image
2.  Enter your dimensions for X and Y &lt;\\li&gt;
3.  Select "Calculate total size from \# Pos" to find the total size of your stitched image (optional)
4.  Select "OK"

### Calculating grid using total sample size

{% include img src="samplesize" align="right" width="250" caption="SampleSize.png" %}

1.  Enter the total size dimensions of your stitched image in microns into the "Total Size" boxes
2.  Enter the step size or the overlap for you stitched images and select "Calculate total size from \# Pos"
3.  Select "OK"

### Computing the grid between two stage positions

1.  Determine your step size using either a pre-calculated value or the overlap slider

{% include img src="stagegrid" align="right" width="250" caption="StageGrid.png" %}

<li>

During your scan, use the XY motor controller to position on corner of your tissue into the field of view

</li>
<li>

Select "Set current pos at START corner"

</li>
<li>

Select "OK"

</li>
</ol>

# Gallery

{% include gallery content=
"
/media/plugins/frame-mover.jpg | (xyz computer controller)
/media/plugins/lever-1.jpg     | (Internal microscope lever)
/media/plugins/x-y-z.jpg       | (XYZ controller)
/media/plugins/pockel-cell.jpg | (Pockel Cell machine)
/media/plugins/ti-saph.jpg     | (Ti Sapph Shutter control)
/media/plugins/photosensor.jpg | Detector 
"
%}
