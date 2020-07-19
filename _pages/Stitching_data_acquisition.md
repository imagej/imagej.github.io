= Wiscan Data Acquisition =
[[Image:OWS 1.jpg|300px|thumb|Microscope setup]]
<ol>
<li>Make sure the image being used has been set up correctly:
<ol>
<li>On the computer, click and hold the shutter button until it turns yellow. The shutter is now activated</li>
<li>Ensure the the outer shutter lever is pointing towards "Lamp" and the inner shutter lever is pointing to the right</li>

<li>Turn on the xyz controller</li>

*NOTE: Do not attempt to adjust the focus of the image with the manual knob while the controller is engaged. You will wear down the gears. </ol>

<li>Move the outer shutter lever toward "Image" and the inner shutter lever toward</li>

<li> Turn on the Pockel Power Cell </li>

<li> Turn on the Ti Sapph Shutter Controller</li>

<li>Log in to Wiscan</li>

<li>Turn on the detector</li>
*Note: DO NOT turn on the detector till the main lights are off. You WILL damage the detector.

<li>Start Scan and ensure your image is in focus on the left side of your screen<\li>

<li>Use the computer xyz controller to choose your initial image frame</li>

<li>Adjust the pockle cell dials until you can see an image on the right side of your screen (the blue portion)</li>

<li>Adjust the detector so that only a small amount of red can be seen in the frame of your image. If too much of a contrast is present, it will burn out the microscope's laser </li>
*Note: The normal range for the detector is 300-500. You should not go above 620.

 <li>Stop scan</li>

 <li>Define the start position in your metadata by selecting "manual update" then "set 0"</li>

 <li>Generate the specifics of your image acquisition using generate grid</li>

<li>Set the size of each image taken (in microns)</li>

<li>Set the amount of overlap you wish to have in your image, then press "calculate number of positions"</li>

*NOTE- You can also set your own step size and overlap amount and calculate the size of each image

<li>Once you have calculated all the necessary positions, you can save this data using the "save positions" button and load them back into Wiscan at a later date</li>

<li>Select Z motor</li>

<li>under 4d imaging, calculate Z bottom, Z top, and Z step</li>

<li>These numbers should be set as 0 unless you are imaging in more than one plane of your sample</li>

<li>Select "Use XY coordinates" and then start sequence</li>

<li>Once Wiscan has run, your output will be a series of images that can be stitched together.</li>

*NOTE- If an noticeable amount of overlay can be seen in your images, there is a pixel to micron error within the microscope's initial setup. To fix this, recalibrate the microscope's objectives. 

==Generate the grid ==
[[Image:BasicGrid.png|250px|right]]
=== The basic grid ===
<ol>
<li>Fill in the Dimensions of X and Y in #X and #Y respectively</li>
[[Image:OverlappedGrid.png|250px|right]]
<li>Enter the step size in microns</li>
<li>Select "Calculate total size from # Pos" to find the total size of your stitched image (optional) </li>
<li>Select "OK" </li>
</ol>

=== Percent overlapped grid ===
<ol>
<li> Use the "Compute overlap slider" to set the overlap percentage you would like within your stitched image </li>
<li> Enter your dimensions for X and Y <\li>
<li>Select "Calculate total size from # Pos" to find the total size of your stitched image (optional) </li>
<li>Select "OK" </li>
</ol>

=== Calculating grid using total sample size ===
[[Image:SampleSize.png|250px|right]]
<ol>
<li>Enter the total size dimensions of your stitched image in microns into the "Total Size" boxes </li>
<li>Enter the step size or the overlap for you stitched images and select  "Calculate total size from # Pos" </li>
<li> Select "OK"</li>
</ol>

===Computing the grid between two stage positions ===
<ol>
<li>Determine your step size using either a pre-calculated value or the overlap slider </li>
[[Image:StageGrid.png|250px|right]]
<li>During your scan, use the XY motor controller to position on corner of your tissue into the field of view </li>
<li>Select "Set current pos at START corner"</li> 
<li>Select "OK" </li>
</ol>

= Gallery =
<gallery>
File:Frame mover.jpg | (xyz computer controller)
File:Lever 1.jpg| (Internal microscope lever)
File:X y z.jpg| (XYZ controller)
File:Pockel cell.jpg| (Pockel Cell machine)
File:Ti saph.jpg | (Ti Sapph Shutter control)
File:Photosensor.jpg | Detector
</gallery>
