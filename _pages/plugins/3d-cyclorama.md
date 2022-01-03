---
mediawiki:
- 3D_cyclorama
- 3Dcyclorama
title: 3D cyclorama
categories: [3D, Digital Volume Unrolling, Digital Volume Flattening]
description: Fiji plugin to digitally unroll deformed tubes.
author: Charalambos Rossides
---

Fiji plugin to digitally unroll deformed tubes. If you use this plugin for your research or industrial applications we kindly ask you to cite our work [1]. 

[1] Rossides, C., Pender, S.L.F. & Schneider, P. "3D cyclorama for digital unrolling and visualisation of deformed tubes." Sci Rep 11, 14672 (2021).

[https://doi.org/10.1038/s41598-021-93184-x](https://doi.org/10.1038/s41598-021-93184-x)

## Download

Step 1 - enable the *3Dcyclorama* site:

- Start Fiji
- Go to Help > Update > Manage update sites
- Click *Add update site*. Name: 3D cyclorama, URL: https://sites.imagej.net/3Dcyclorama
- Check the newly added *3Dcyclorama* site
- Click *close*
- Click *Apply changes*

Step 2 - download dependencies:
- Create a directory named *FastDTW* in the Fiji plugins directory (Fiji.app/plugins/FastDTW)
- Download the FastDTW algorithm from github [https://github.com/rmaestre/FastDTW](https://github.com/rmaestre/FastDTW) (Click code > download zip)
- Extract the contents of FastDTW-master (FastDTW.iml, README.md, src, target, etc.) in Fiji.app/plugins/FastDTW

Step 3 - Run:
- Restart Fiji
- The 3D cyclorama plugin should appear in the Plugins menu towards the bottom in a menu titled **3D cyclorama**

## Tutorial

Usage:

A. Preparation
1. Run imagej
2. Open your image stack:
	```
	File > Import > Image Sequence

	Navigate to the directory of your image stack, select one image and click "Open".
	* An example image stack is distributed with the plugin and it is located at ./plugins/3Dcyclorama/Phantom/

	Leave the detected values unchanged (Number of images, starting image, increment and scale), check the "Use virtual stack" box and click "Ok".
	```
3. Define the boundary contours:

	> If you have loaded the example phantom you can skip step 3. as a roiSet is already loaded from ./plugins/Scripts/Plugins/3D cyclorama/Phantom/RoiSet.zip

	3.1 Select the segmented line tool:
	```
	Right-click the fifth tool from the left hand side of the tool bar, and select "Segmented Line".
	```
	3.2 Draw one contour:
	```
	Select the desired stack slice (e.g. slice 1) using the image stack slide bar Image > Stacks > Set Slice.

	Left click along the boundary of the deformed tube to draw a closed contour. Finish the contour by clicking on the first point, which is marked with a square.
	> It is not necessary to draw smooth contours as they will be smoothened later-on. A rough outline is enough (e.g. 10 to 50 points).

	Add the contour to the ROI manager:
		Method 1:
			Press "t"
		Method 2:
			Analyze > Tools > ROI manager to open the ROI manager window.
			Click "Add" on the ROI manager window.

	Rename the contour:
		On the ROI manager window click "Rename".
		Change the number between the two dashes to 0 or 1 for the inner or outer contours respectively: <unchanged>-<Inner/Outer>-<unchanged>
		Click "Ok"  
	```
	3.3 Repeat step 3.2 every several slices depending on how "quickly" the shape of the contours changes from slice to slice.
	```
	A minimum of 3 slices is required (i.e. for a dataset of 150 slices, draw the contours on every 50 slices).
	You can always add more contours to improve the result in the future.
	```
	3.4 Save the contours as a RoiSet
	```
	On the ROI manager press Ctrl + a to select all contours.

	Right-click and "Save"

	Navigate to the directory where the image stack is saved and click "Save" (Keep the file name "RoiSet.zip")
	```
4. Close the image stack and proceed to step "B. Unrolling".

B. Unrolling

0.  Open the cyclorama plugin:
    ```
	Click Plugins > 3D cyclorama > 3D cyclorama
    ```
1. Load the scanStack (Panel 1: Load scan stack):
    ```
	For the "Parameters" select among:
		"Previous" : Parameters saved during the last exit of the 3D cyclorama plugin.
		"Default" : A predefined set of parameters that is located at .plugins/3Dcyclorama/defaultCycloramaParameters.txt.
		"Custom" : A cyclorama parameters file assumed to be located in the directory of the image stack. This is helpful if a working set of parameters is saved using the "Save parameter file" button in Panel 3.

	If the deformed tube extends over the entire image stack, set the "First silce" to 1 and the "Number of slices" to 0.

	If a sub-stack is to be unrolled, set the "First slice" and the "Number of slices" accordingly.

	The interpolation interval corresponds to the vertical axis i.e. interpolation to create missing contours in-between slices. Depending on how "quickly" the deformed tube changes from slice to slice this number will vary. Begin by setting this equal to the number of slices in-between the defined contours (though it is not necessary that these two values are the same.)
	"Sample type" holds a user-given identifier of the sample and it is irrelevant to any computation. The "sample type" will be stored in the auto-generated log file for future reference.

	Uncheck the "Open as virtual stack" box.

	Select the "contour definition" as "Load ROIset"

	Select the inner and outer contour ID as 0 and 1 respectively. (These can be set by the user if more than two contours are defined on each slice in step A.3.2).

	Click "Load scanStack", navigate to the directory of your image stack, select one image and click "Open". This will open the image stack and it will load the ROIset file that is expected to be saved in the same directory. A message will be displayed in the script editor output panel informing of the selected RoiSet.
    ```
2. Compute the boundary contours (Panel 2: Compute boundary contours)
    ```
	Select the desired "contour length" (Start with 100 points. Increase if the contours do not properly capture the shape. Decrease as much as possible for improved performance).

	Select a "smoothing factor" if the contours need to be smoother (Number of moving average window).

	"Max number of threads" is the maximum number of concurrent threads spawned for parallel computing. Reduce this if the software freezes during computation.

	Set the rotation axis X and Y coordinates:
		Move the mouse over the image to a position within the two contours (roughly the centre). Observe the ImageJ window below the toolbar and note the coordinates in pixels. Set the "Rotation axis X" and "Rotation axis Y" values to define the axis perpendicular to the image plane that runs throughout the deformed tube. Note this axis must be in the inner side of the all of the (closed) contours on all image slices.

	Click "Compute boundary contours":
		When finished, the ROI manager will be populated with the computed boundary contours on all slices. Click on the first one and press the down arrow to go through all the contours. This will concurrently update the ROI on the image stack so that you can verify that the computed contours are valid.
		Note that this accesses all individual slices of the image stack. Therefore if the stack is loaded as virtual ("Open as virtual stack" in Panel 1), computing the boundary contours will be exceedingly slow.
		If the computed contours are not closed contours on the boundaries of the tube, the rotation axis needs to be tuned.
		If they are over-smoothed either the "contour length" needs to be increased or the "smoothing factor" needs to be reduced.
		If none of these works, the manually defined contours might need to be tuned.
		If the manually defined contours (on the relevant slices) are correct and the contours in the intermediate slices gradually shift from the tube's boundaries then more contours need to be manually defined.
		If the contours in the intermediate slices remain relatively unchanged, then the "Interpolation interval" on panel 1 needs to be reduced.
		If the contours oscillate exceedingly from slice to slice, the "Interpolation interval" on panel 1 needs to be increased.
    ```
3. Compute the intermediate contours and resampling surfaces (Panel 3: Compute resampling surfaces)
    ```
	Define the "number of contours" to be computed on each slice, which includes the boundary and intermediate contours:
		Begin with a small value (3 or 5) so that you can quickly derive the rest of the parameters on this panel.
		For an exact unrolling (explicit computation of all intermediate contours via the electric fields method) set the exact number of desired depth levels here.
		For an approximate unrolling, one can set a small "number of contours" here (e.g. 5) and set the desired number of depth levels as the "Number of interpolated depth levels" in panel 4. This method requires less computational time and the result is almost identical to the exact method.

	Define the "Contour length":
		This is the number of points used to represent each contour.
		Start with 100 points. Increase if the contours do not properly capture the shape. Decrease as much as possible for improved performance

	Define the "Span rigidity":
		This is a positive value (close to one) corresponding to how stiff (rigid) the electric field lines are.
		Increase the "span rigidity" if the electric field lines wander too much and do not make it to the outer contour.
		Decrease the "span rigidity" if the electric field lines are too straight to capture the tube's shape.

	Define the "Smoothing factor":
		This is equal to a moving average window that smoothens the contours.
		A value equal to one will keep the contours unchanged while a greater value (3 to 10 are plausible) will reduce the contour's ruggedness.

	Define the "Electric field search window":
		Defines the number of points on the inner and outer contour around the starting point of each electric field line that are accounted for during the computation of the electric field.
		This improves the algorithm's computational efficiency by reducing the number of points for the computation of the electric field lines (the computation does not take into account all contour points defined by the "contour length").
		It also imposes a locality factor in the computation. If the shape of the tube has very sharp bends, then reducing the electric field window allows the user to restrict the computation to a small neighborhood around the bend and disregard crosstalk from points further away.
		Begin by setting the "Electric field search window" equal to one tenth of the "contour length".

	Define the "Max number of steps" and the "Span step":
		The "max number of steps" is the maximum number of iterations that the software will execute to compute each electric field line, starting from the inner contour and attempting to reach the outer contour.
		On each iteration, the electric field line is extended by "span step".
		Therefore, the maximum electric field line length is equal to the "span step" multiplied by the "max number of steps".
		Set the "span step" equal to a small value greater than 1 (2 to 5). Small "span step" yields more continuous electric field lines in the expense of computational cost.
		To set the "max number of steps" measure the thickness of the tube in pixels at its thickest part and divide it by the "span step". Multiply this value by 1.5 (overestimate the thickest part) to avoid premature termination of the electric field line computation.
		If the contours (computed next) are not spaced equally, this means that the "max number of steps" is too small.
		If the software freezes failing to compute the intermediate contours, one of the reasons might be that the "max number of steps" is too large.

	Define the "Min span variance":
		This is the variance of the points that constitute an electric field line. Thus, too small variance signifies an electric field line that curls upon itself failing to reach the outer contour.
		Set the "min span variance" to a large enough value to ensure that the electric field lines spread adequately but a small enough value so that not too many electric field lines are rejected.
		A starting value of 10 is plausible.
		If the "min span variance" is too large, too many of the electric field lines will be rejected.
		If it is too small, invalid electric field lines (those that do not reach the opposite contours) will be included in the computation.

	Uncheck the "Save contours" checkbox:
		The "save contours" checkbox will save the contours to file when the "Compute contours" button is clicked.
		This can be checked later-on when all parameters have been derived.

	Check the "Show contours" checkbox:
		This will overlay a ROI for each contour on top of the image stack that enables visual validation of the result.

	Click "Test parameters":
		This will compute the electric field lines and intermediate contours for the active slice.
		The computation overwrites the boundary contours. Thus if the parameters are not appropriate to successfully compute the intermediate contours for the given slice, the invalid boundary contours will compromise a re-computation.
		Thus, make sure you activate a different slice every time you click "test parameters".
		Evaluate the result, adjust the parameters, select a different slice and repeat "test parameters" until you are satisfied with the outcome.
		Run the "test parameters" on several slices throughout the stack to make sure that the parameters are valid for all different morphologies throughout the sample.

	Define the mapping mode:
		In Panel 4 in "Mode" select "idx" for the linear mapping mode or "DTW" for the non-linear mapping mode (less wavy cycloramas but might include singularities).

	Define other miscellaneous parameters:
		Set the "Max number of threads" in Panels 3, 4, and 5 to define the maximum number of parallel computational threads used to compute the corresponding steps.
		If you would like to save the contours computed in step 3 to file, check the "Save contours" checkbox in Panel 3.
		If you would like to interpolate the computed contours in order to compute more depth levels in a computationally cheaper way (approximate unrolling), set the number of desired depth levels (number of cyclorama slices) in Panel 4.
		If you would like to save the mappping to file, check the "Save mapping" checkbox in Panel 4. Note that this is required for bi-directional examination of the result (see C. Analysis).
		If you would like to save the resulting 3D cyclorama to file as a tiff image, check the "Save cyclorama" in Panel 5.
    ```		
4. Proceed with the final unrolling:
    ```
	Close the image stack and run the 3D cyclorama plugin again.

	The previously selected parameters should be automatically loaded (If the "Previous" radio button is selected in Panel 1).

	Uncheck the "Open as virtual stack" checkbox in Panel 1.

	Uncheck the "Show contours" checkbox in Panel 3.

	Click "Load scanStack" in Panel 1 and load the image stack as earlier.

	Click "Compute all":
		The button will remain clicked until the computation is finished.
		Intermediate messages will be displayed on the script editor output area.
		A log file will be saved to file. This can be opened with a text editor and examine the used parameters and all associated files. It is also used to automatically open all files during the next step (C. Analysis).

	Side notes:
		Instead of clicking "Compute all" it is also possible to manually perform the process in a step-wise fashion by clicking "Compute boundary contours" > "Compute contours" > "Compute mapping" > "Compute cyclorama". This is generally useful for debugging when the process fails in order to identify the exact step that causes the issue.
		It is also possible to start from an intermediate step by clicking "Load contours" or "Load mapping" and proceeding from there.
    ```

C. Analysis

	Run the analysis module:
		Restart ImageJ and click Plugins > 3D cyclorama > Analyze

	Load the project:
		A "Load project" panel will pop up. Leave the default values and click "Load".
		In the file selector that pops up, navigate to the "Cyclorama" directory that was created in the directory of the image stack.
		Select the <datetime>_log.txt file and click "Open".
		This will open the image stack, the 3D cyclorama, the Imagej log window and a panel titled "Analyze cyclorama".

	Bidirectional mapping:
		When the checkbox "Link views" is checked clicking on either of the views (image stack or cyclorama) will create the corresponding (mapped) point on the other view.
		The mapped points are also presented in the "Console" window.
		This allows the user to interact with the image stack and the 3D cyclorama and identify matching features.

	Contours:
		Checking the "Show contours" checkbox reveals the contours on the image stack.
		This allows the user to evaluate the unrolling quality and better understand which contour each slice of the 3D cyclorama corresponds to.

	Feature tracking:
		Check the "Activate ROI manager" checkbox to reveal an empty ROI manager.
		Trace a feature on either of the two views by sequentially clicking along its shape. For each of the clicked points the corresponding (mapped) point on the dual view will be automatically added to the ROI manager.
		Example:
			Check both the "Activate ROI manager" and "Show contours" checkboxes.
			Click along a contour on the image stack to create several points.
			Select the cyclorama image.
			Click the "Show All" checkbox on the ROI manager.
			This should reveal a line of points on the cyclorama image corresponding to the points along the contour you have clicked on.

	Cyclorama inverting:
		It is possible to re-roll (apply the inverse mapping) any image that has the same dimensions of the 3D cyclorama.
		This is useful when features are segmented on the 3D cyclorama and the corresponding features need to be quantified on the image stack.
		Example:
			Uncheck all check boxes.
			Select the rectangle tool (leftmost tool on the Imagej toolbar).
			Draw a rectangle on top of the 3D cyclorama and press ctrl+f to fill it with a given colour.
			Repeat this over all slices of the cyclorama (Keep the rectangle unchanged, scroll to change image slice and press ctrl+f on each slice).
			Under the "Invert projected image (Cyclorama)" click "Select".
			In the "Invert image" window that pops up:
				Select the cyclorama image from the drop-down list and the maximum number of parallel threads (e.g. 10).
				When the 3D cyclorama is re-rolled only the pixels along the contours will be computed (this is where the mapping has been calculated). Instead, a denser approximation of the inverse mapping may be computed via interpolation. This is achieved via selecting the number of interpolation levels.
				Select "Interpolation levels" greater than zero for interpolation (e.g. 50) or 0 for exact inversion.
				Click ok.
				The 3D cyclorama will be re-rolled and the feature drawn using the rectangle tool should be apparent (slicing the deformed tube across its depth).

	ROI inverting:
		It is possible to re-roll (apply the inverse mapping) points defined on the 3D cyclorama.
		This is useful when seed-points (e.g. for region growth segmentation purposes) need to be identified on the 3D cyclorama and defined on the image stack.
		Example:
			Uncheck the "Activate ROI manager" to close any open ROI manager.
			Select the point tool (7th tool from the left on the Imagej toolbar).
			Click on a feature on the cyclorama image and press "t" to add the ROI to the ROI manager. Repeat this several times to create several ROIs.
			Under the "Invert ROIs" click the "Invert" button.
			This will create a black mask stack with the same dimensions as the image stack and white cubes of 5 x 5 x 5 pixels at the corresponding (mapped) points of all the points currently existing in the ROI manager.

<p style="text-align:center;"><img src="https://user-images.githubusercontent.com/20737950/131255975-c5f6bbd8-eafe-4d34-9770-65716e112b9e.png" width="800"></p>

## ChangeLog
v1.0.0:

- Added functionality to flatten sheets and scrolls.
  
v0.6.0:
  
- Implemented sanity checks in GUI.
  
v0.5.0:

- Restricted 3Dcyclorama GUI access to unnecessary backend functionality.
  
v0.4.0:
  
- First mature GUI.
  
