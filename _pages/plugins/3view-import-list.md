---
mediawiki: 3View_import_list
title: 3View import list
categories: [TrakEM2]
---

{% include info-box name='3View import list' software='ImageJ' author='Nuno Dias' maintainer='Nuno Dias' source=' [link](https://dl.dropboxusercontent.com/u/5200940/3view_import_list.zip)' released='March 2013' latest-version='March 2013' %}

## Import 3View montages into TrakEM2: overview

The purpose of this plugin is to create a text file with a list of files from [Gatan's 3View](http://www.gatan.com/products/sem_products/products/3View_landing.php) montage image stacks. This text file can then be used to automatically import all the images into TrakEM2, as they are, stored in the original directories.

In montage mode, [Gatan's DigitalMicrograph](http://www.gatan.com/software/) software saves the files for each tile in their own directory. Taking the example of a 2x3 montage with 10 z slices, at the end of the job there will be 6 folders created, with 10 files each. The folders are named following the pattern `Montage_xxx`, where xxx is a number (starting at 000).

This plugin will read all Gatan's files (.dm3) inside the folders and create a file list in a text document (.txt), in a format suitable for importing into TrakEM2, directly from their original directories. You can move the parent directory from the acquisition computer to any other suitable location, of course. The plugin will also attempt to read metadata from the files to automatically calculate the montage configuration (how many tiles in x and y) and to provide rough coordinates for the image positioning, according to image size and overlap. This information will leave the images roughly in place in the TrakEM2 workspace and makes the next step - stitching the images - much quicker.

## Installation instructions

The [Jython plugin installation rules](https://fiji.sc/Jython_Scripting#using-a-jython-script-as-a-plugin) apply. You must [download](https://dl.dropboxusercontent.com/u/5200940/3view_import_list.zip) and copy `3view_import_list.py` and MakeImportList4TrakEM2.py together in the same directory. The third file, `TrakEM2_import_list.py` is optional (see point 3 below). If you want to call the script from your own code, only the second file is necessary. As a suggestion only, you can follow these steps:

1.  Copy `3view_import_list.py` and `MakeImportList4TrakEM2.py` into Fiji directory `...\Fiji.app\plugins\Scripts\Plugins\Utilities`.
2.  To make the plugin appear in the menu, you have the option of selecting {% include bc path='Plugins | Scripting | Refresh Jython Scripts'%}, {% include bc path='Help | Refresh Menus'%} or restarting Fiji. Then the menu entry '3View import list' will appear under {% include bc path='Plugins | Utilities'%} (the first Utilities folder...)
3.  Extra: if you need to use different settings other than file type .dm3, other directory names or change the name of the final text file, you can copy `TrakEM2_import_list.py` to the same folder and select the plugin with this name from the same menu location.

## How to use

1.  After selecting the plugin from the Fiji menu:
2.  Select the parent directory where all the `Montage_xxx` folders are located;
3.  The plugin *would* try to produce the final text file without any further input from the user if possible, calculating tile configuration and overlap using metadata from the image files, but this feature is not working at the moment. See bold text below.
4.  The Fiji log and the status messages in Fiji window will show step-by-step information of what is happening. The whole operation should only take a few seconds. You can use this plugin over a network connection, but the actual importing job (step 6 below) should be done with the files placed in a local hard drive or through an extremely fast data connection, for an optimal performance.
5.  The text file will be saved in the same directory initially selected by the user.
6.  To actually use the text file, right-click anywhere in the TrakEM2 workspace (the black area) and select {% include bc path='Import | Import from text file...'%} After selecting the file, you should get a window asking for some options. These should be left at default, making sure 'Column separator' indicates 'tab'. TrakEM2 will then ask for the location of the files to be imported and you should provide the parent folder where all the `Montage_xxx` directories are located - the very same one you selected when running this plugin. TrakEM2 will then import every file in the list and create the minimaps for fast loading/zooming. This may take a while.

## Small print: what is allowed and the known limitations

1.  **Reading stage coordinates from the metadata is currently not possible. This means the user will always be asked for the tile configuration and overlap.**
2.  You can have other directories at the same level of the montage directories (for example, the TrakEM2 data directory). Also, any sub-directories of those montage directories you may create and their contents will be completely ignored. However, you shouldn't have directories in the parent directory following the same `Montage_xxx` pattern that are actually not part of the dataset.
3.  You can have other file formats together with the .dm3 files, those will be ignored.
4.  All .dm3 files within the montage directories will be added to the list.
5.  The plugin doesn't check/care if the number of files is not the same in every directory; what is mandatory is to have at least one file in the first, the second and the last directories.
6.  If for some reason you need to change the numbering of the directories, just make sure they stay in the same order. Non-consecutive numbering is not a problem; directories will simply be read in ascending order.
7.  If stage position values cannot be read or the calculated tile configuration doesn't match the number of detected folders, the plugin will ask the user for the x and y tile number and overlap percentage.
8.  If you plan to add or modify files inside the acquisition directories, because you need to merge interrupted acquisition jobs for example, you have to modify the numbering so that the final 4 digits of the file name match the z position of the image in the stack. Z positions are not being read from the metadata exactly to accommodate for situations like this.  
    Tip: doing this by hand is tedious and error prone; there are however free software applications that can automate this file renaming job easily.
9.  If you run the slightly modified version, 'TrakEM2 import list', you can choose another file format other than .dm3, choose another folder pattern (these are {% include wikipedia title='Regular expression' text='Regular Expression'%} patterns) or a different file name for the final text file. However, the image files still need to have metadata for stage coordinates and pixel dimension (size), in the same units, for the automatic calculations to work. Currently I don't have any 'non-automatic' version that will take all required information for the user.  
    Note 1: The numbering in the files must have 4 digits. I *may* fix this in the future.  
    Note 2: The file format input is case sensitive: '.tif' is not the same as '.TIF'
10. To automate or call the plugin from another script, you need to provide the details mentioned in the previous point. See the file `TrakEM2_import_list.py` for an example.
11. The plugin assumes all files have the same pixel dimension (size).
12. The plugin assumes pixels to be square and overlap to be the same in x and y.
13. The plugin *should* work independently of operative system (Linux, Windows, Mac). Feedback is appreciated.
14. Because of the 45° angle between the FoV and the X/Y axis in the 3View stage, this plugin will probably fail if provided with a dataset acquired with an angle close to zero (ie, from another system/stage). Because of the behavior indicated in point 7, stripping the files from any stage position metadata would be a way to circumvent this limitation.
15. As a bonus, you can also use this plugin to create an import file for a single position z stack; in that case it doesn't matter where the images came from, as no montage calculations are necessary.  
    Note 1: selecting the 'main' plugin for a situation like this using .dm3 files, you still must have the folder name match the pattern `Montage_xxx`.  
    Note 2: to create a single-position file list of images in another file format (.tif files for example) using the 'alternate' 'TrakEM2 import list' plugin, you don't need to modify the directory name where you keep the files in the options dialog. You can just submit this name in the 'Directory RegExp' field (no Regular Expression special patterns are necessary). However, you must choose its parent directory in the 'Choose directory' dialog, as you would in every case. As an example, if you have your image files in `C:\data\images\stack1`, you should select the directory `C:\data\images\` and submit 'stack1' as the 'Directory RegExp' value in the 'Import parameters' dialog.

## Code

```
3view_import_list.py
```

```python
import sys
from ij import IJ
from ij.io import DirectoryChooser
from java.lang.System import getProperty
sys.path.append(getProperty("fiji.dir") + "/plugins/Scripts/plugins/Utilities")
from MakeImportList4TrakEM2 import make_list

dc = DirectoryChooser('Select 3View dataset base directory')
folder = dc.getDirectory()

if folder is None:
	IJ.log('User canceled the folder selection!')
else:
	dir_RegExp = 'Montage_\d{3}'
	list_filename = 'TrakEM2_import.txt'
	filetype = '.dm3'
	how_many = make_list(filetype, folder, dir_RegExp, list_filename)
	IJ.showProgress(1,1) #in case there is an error, the progress bar still disappears
	IJ.showStatus('Completed. Files added to import list: ' + str(how_many))
```

```
TrakEM2_import_list.py
```

```python
import sys
from ij import IJ
from ij.io import DirectoryChooser
from ij.gui import GenericDialog
from java.lang.System import getProperty
sys.path.append(getProperty("fiji.dir") + "/plugins/Scripts/plugins/Utilities")
from MakeImportList4TrakEM2 import make_list

def getParameters():  
  gd = GenericDialog("Import parameters")
  gd.addStringField("Import list name", "TrakEM2_import.txt")
  gd.addStringField("Directory RegExp", "Montage_\d{3}")
  gd.addStringField("Filetype filter", ".tif")
  gd.showDialog()  
  #  
  if gd.wasCanceled():  
	print "User canceled dialog!"  
	return  
  # Read out the options  
  list_name = gd.getNextString()  
  reg_exp = gd.getNextString()
  ftype = gd.getNextString()
  return list_name, reg_exp, ftype

dc = DirectoryChooser('Select 3View dataset base directory')
folder2 = dc.getDirectory()

if folder2 is None:
	IJ.log('User canceled the folder selection!')
else:
	param = getParameters()  
	if param is not None:  
		list_name, reg_exp, ftype = param
		how_many = make_list(ftype, folder2, reg_exp, list_name)
		IJ.showProgress(1,1) #in case there is an error, the progress bar still disappears
		IJ.showStatus('Completed. Files added to import list: ' + str(how_many))
```

```
MakeImportList4TrakEM2.py
```

```python
import os, re, math, sys
from ij import IJ
from ij.gui import GenericDialog
from loci.formats import ImageReader, MetadataTools

def read_meta(filen2):
	rf = ImageReader()
	meta = MetadataTools.createOMEXMLMetadata()
	rf.setMetadataStore(meta)
	rf.setId(filen2)
	# get stage position:
	planeCount = meta.getPlaneCount(0)
	for p in range(planeCount):
		posX = float(str(meta.getPlanePositionX(0, p)))
		posY = float(str(meta.getPlanePositionY(0, p)))
	try:
		posX, posY
	except NameError:
		posX = posY = 0
	return rf, meta, posX, posY

def getOptions(X, Y, Ol, mnts):
	IJ.showStatus('Asking user for input...')
	gd = GenericDialog("Montage configuration")
	gd.addNumericField("Number of tiles in X", X, 0)  # show 0 decimals
	gd.addNumericField("Number of tiles in Y", Y, 0)  # show 0 decimals
	gd.addNumericField("Overlap (%)", Ol, 1)  # show 1 decimal
	gd.showDialog()  
	if gd.wasCanceled():
		IJ.log('User canceled dialog. Text file not created')
		return
	# Read the input into variables
	pos_x = int(gd.getNextNumber())
	pos_y = int(gd.getNextNumber())
	if (pos_x * pos_y) != mnts:
		IJ.log('The configuration you provided (' + str(pos_x) + 'X by ' + str(pos_y) + 'Y) and number of detected directories (' + str(mnts) + ') do not match.\nText file not created.')
		IJ.showMessage('The configuration you provided and number of detected directories do not match.\nText file not created.')
		return
	overlp = gd.getNextNumber()
	return pos_x, pos_y, overlp
  
def make_list(filetype, folder, dir_RegExp, list_filename): 
	IJ.log('--- Begin creating 3View file list for TrakEM2 import ---')
	IJ.showStatus('Starting...')
	x_now = y_now = counter1 = 0
	import_list = ''

	try:
		f = open(folder + list_filename, 'w') # Save the text file for importing in same root folder, auto overwrite
	except IOError:
		IJ.log('Error: can\'t create file in selected directory')
		return
	else:
		IJ.showStatus('Reading directories...')
		subdirs = sorted(os.walk(folder).next()[1]) # create list with the contents of the directory, selecting only 1st level directories and sorting them ascending. Sorting is fundamental for correctly reading of stage position values and for correct positioning os the tiles in each montage
		subdirs[:] = [sd for sd in subdirs if re.match(dir_RegExp, sd, flags=0)] # filter the dirs that match the RegExp. For 3View the name is 'Montage_xxx'. This allows for some flexibility: users can have other folders together with the stack folders such as TrakEM2 minimaps folder
		montage_size = len(subdirs) # count how many dirs were selected - to calculate configuration of montage and progress reporting
		if montage_size == 0:
			IJ.log('Error: No directories found matching RegExp pattern \'' + dir_RegExp + '\' in ' + folder)
			return
		try:
			scnd_dir = subdirs[1] # check if there is more than one folder, setting at the same time the variable for the second (folder in the list) index position - [1]
		except IndexError:
			# since there is only one folder, move on with settings to create a file list for just one position. The whole else: part below will be skipped
			IJ.log('Only one directory detected. Creating file list for single position z-stack')
			x_coord = y_coord = 1
			x_now = y_now = x_img_size = y_img_size = overlap = 0
		else:
			IJ.log(str(montage_size) + ' matching directories found in ' + folder)
			# get values for calc of montage configuration and overlap
			files_2nd_dir = os.listdir(os.path.join(folder,scnd_dir))
			files_2nd_dir[:] = [fn1 for fn1 in files_2nd_dir if os.path.isfile(os.path.join(folder,scnd_dir,fn1))and fn1.endswith(filetype)] 
			IJ.showStatus('Reading stage coordinates 1/3...')
			try: # stop if no files are found in the 2nd folder:
				r1, meta1, pos2_Xstage, pos2_Ystage = read_meta(os.path.join(folder, scnd_dir, files_2nd_dir[0])) # pick a file from the second folder to read metadata
				r1.close()
			except IndexError:
				IJ.log('Error: the 2nd directory in the list does not contain any files of type ' + filetype)
				return
			last_dir = subdirs[-1] # pick one file from the last folder to read metadata
			files_lastdir = os.listdir(os.path.join(folder,last_dir))
			files_lastdir[:] = [fn2 for fn2 in files_lastdir if os.path.isfile(os.path.join(folder,last_dir,fn2))and fn2.endswith(filetype)]
			IJ.showStatus('Reading stage coordinates 2/3...')
			try:
				r2, meta2, posLast_Xstage, posLast_Ystage = read_meta(os.path.join(folder, last_dir, files_lastdir[0]))
				r2.close()
			except IndexError:
				IJ.log('Error: the last directory in the list does not contain any files of type ' + filetype)
				return
		for d, dirs in enumerate(subdirs):
			filenames = sorted(os.listdir(os.path.join(folder,dirs))) # the sorting is just to try and hide the darker, overlap areas of the image to be in front when displaying the montage in TrakEM2. This is probably not necessary if some contrast homogenization is performed after importing
			filenames[:] = [fn3 for fn3 in filenames if os.path.isfile(os.path.join(folder,dirs,fn3))and fn3.endswith(filetype)] # make sure there are no dirs ending in desired filetype (one never knows~) and filter for the filetype
			filenames_size = len(filenames) # for progress bar only
			for p, filen in enumerate(filenames):
				try: # check if metadata was read already and extract metadata info from the 1st file on the list - if it was not, get this info by executing the except clause. This makes the metadata routine run only once in the beginning. Being nested inside the else: stm above, metadata is only read if it's not a single position acquisition - in this case it wouldn't be necessary. Also, complete calc of overlap and montage configuration
					overlap
				except NameError:
					IJ.showStatus('Reading stage coordinates 3/3...')
					try:
						r3, meta3, pos1_Xstage, pos1_Ystage = read_meta(os.path.join(folder, dirs, filen))
					except IndexError:
						IJ.log('Error: the first directory in the list does not contain any files of type ' + filetype)
						r3.close()
						return
					IJ.showStatus('Reading more metadata...')
					x_img_size = r3.getSizeX()
					y_img_size = r3.getSizeY()
					r3.close()
					pSizeX = float(str(meta3.getPixelsPhysicalSizeX(0))) # getPixelsPhysicalSizeX(0) it's an object, and needs both str and float before it can be used in calculations
					pSizeY = float(str(meta3.getPixelsPhysicalSizeY(0)))
					IJ.log('Read image size ' + str(x_img_size) + ' X ' + str(y_img_size))
					IJ.log('Read pixel dimensions ' + str(round(pSizeX * 1000, 1)) + ' X ' + str(round(pSizeY * 1000, 1)) + ' nm')
					# next 2 are needed to calculate overlap:
					deltaX1 = pos2_Xstage - pos1_Xstage
					deltaY1 = pos2_Ystage - pos1_Ystage #only for single column montage
					# if deltaX1=0 then something went wrong with the metadata reading and the user has to manually input the coordinate values. note that for the case of a single folder deltaX1 would theoretically also be =0 (but this code doesn't even allow for that, since it requires at least 2 folders for the calculation)
					#(or close to zero - most likely in a case of 'multiple ROI' acquisition (there would be stage movement) instead of 'montage') but that situation was already covered above and at that step the overlap var was initiated; in that situation this whole except NameError: is skipped and no deltaX1 calc is ever performed
					if deltaX1 == 0:
						IJ.log('Warning: Could not read stage position from files. Asking for user input')
						options1 = getOptions(0, 0, 0, montage_size)
						if options1 is None:
							overlap = 0 # to prevent "UnboundLocalError: local variable 'overlap' referenced before assignment". Rrom http://docs.python.org/2/reference/simple_stmts.html : "When return passes control out of a try statement with a finally clause, that finally clause is executed before really leaving the function."
							return
						x_coord, y_coord, ovlap1 = options1
						overlap = 1 - (ovlap1 / 100)
						IJ.log('User provided montage configuration ' + str(x_coord) + 'X by ' + str(y_coord) + 'Y and ' + str(ovlap1) + '% overlap')
					# if deltaX1 > 0 means the second position(dir) is in the X axis(to the right instead of down); otherwise the next folder is in the Y axis and therefore a single column montage# this is because the stage is at an angle (45  without scan rotation) with the montage axis This check is not robust enough to accomodate a 0 deg stage (it may not work with images acquired without a significant axis angle in relation to the images, ie, not with 3View)# also: assumes the coordinate system is always the same in relation to the images; if there are invertions, then this check needs to be reworked
					elif deltaX1 > 0:
						IJ.showStatus('Calculating parameters...')
						overlap = round(math.hypot(deltaX1, deltaY1) / float(x_img_size) * pSizeX, 1) # assumes overlap and pixel size to be the same in x and y
						IJ.log('Calculated overlap: ' + str((1 - round(overlap, 1)) * 100) + '%')
						# calc max stage movement distance measured between 1st and last montage 'positions'
						deltaX2 = posLast_Xstage-pos1_Xstage
						deltaY2 = posLast_Ystage-pos1_Ystage
						# then to 'convert' the stage distance into 'real' montage span distances some more trig needs to be applied because the 45 deg rotation of the axis relative to the image acquisition (FoV)
						bigger_angle = math.atan(deltaY2 / deltaX2) # arc tangent in radians
						smaller_angle = bigger_angle - math.radians(45)
						# hypotenuse of the rectangle formed between the 1st and the last stage position
						montage_hyp = math.hypot(deltaX2, deltaY2)
						# it's a rectangle, the hypotenuse angle will vary. Calcs for x length is 'adjacent side', so cos(x) and calcs for y is 'opposite side', so sin(x)
						montage_Xlenght = round(math.cos(smaller_angle) * montage_hyp, 3)
						montage_Yheight = round(math.sin(smaller_angle) * montage_hyp, 3)
						# and finally calculate the number of tiles in the x and y axis, assuming stage movement is reasonably accurate
						x_coord = int(round(montage_Xlenght / (x_img_size * overlap), 0)) + 1
						y_coord = int(round(montage_Yheight / (y_img_size * overlap), 0)) + 1
						IJ.log('Montage configuration calculated to be ' + str(x_coord) + 'X by ' + str(y_coord) + 'Y')
						if (x_coord * y_coord) != montage_size:
							# create dialog to get user input because the calculated configuration doesn't match the number of folders
							IJ.log('Warning: Calculated montage configuration and total number of folders found do not match')
							options2 = getOptions(x_coord, y_coord, overlap, montage_size)
							if options2 is None:
								overlap = 0 # to prevent UnboundLocalError: local variable 'overlap' referenced before assignment
								return
							x_coord, y_coord, ovlap2 = options2
							overlap = 1 - (ovlap2 / 100)
							IJ.log('User provided montage configuration ' + str(x_coord) + 'X by ' + str(y_coord) + 'Y and ' + str(ovlap2) + '% overlap')
					else:
						# The alternative is a single column montage and for that case the calculations are more simple
						IJ.showStatus('Calculating parameters...')
						overlap = round(math.hypot(deltaX1, deltaY1) / (y_img_size * pSizeY), 1)
						IJ.log('Calculated overlap: ' + str((1 - overlap) * 100) + '%')
						x_coord = 1
						y_coord = montage_size
						IJ.log('Montage configuration should be ' + str(x_coord) + 'X by ' + str(y_coord) + 'Y')
				finally:
					IJ.showStatus('Adding files to import list...')
					reg_expr4_zval = '.+(\\d{4})\\' + filetype + '$' # RegExp to get the z position (number) from the filename
					find_zval = re.match(reg_expr4_zval, filen, flags=0) # get the last 4 digits from the filename
					z_now = int(find_zval.group(1)) # should be the z order/position of the file in the stack. int() removes leading zeros
					# append the file info to the list ASCII 13=Enter ; 92=\ ; 9=TAB
					import_list = os.path.join(dirs, filen) + chr(9) + str(int(x_now*x_img_size*overlap)) + chr(9) + str(int(y_now*y_img_size*overlap)) + chr(9) + str(z_now) + chr(13) + import_list
					counter1 += 1
					progress = int(((((p + 1)/ float(filenames_size)) + d) * 100))
					IJ.showProgress(progress, montage_size * 100)
			x_now += 1 # gone through the contents of one folder; before moving to the next, move the montage position counters
			if (x_now == x_coord): # if all x positions in a row are recorded, reset x and move to next row (y position)
				y_now += 1
				x_now = 0
		f.write(import_list.strip())
		f.close()
		IJ.log(str(counter1) + ' entries were written to the file ' + f.name)
		return counter1
```

## Contact

All comments, questions or suggestions are very welcome. Please send an email to nuno.dias at emez.ethz.ch or ngdias at ibmc.up.pt.

## Acknowledgements

-   [Curtis Rueden](http://loci.wisc.edu/people/curtis-rueden)
-   [This page](http://www.ini.uzh.ch/~acardona/fiji-tutorial/) prepared by Albert Cardona
-   [This other page](https://fiji.sc/Jython_Scripting) prepared by Albert Cardona
-   Many, many people who ask and reply to questions about Python all over the Internet

## See Also

-   [Importing list](http://www.ini.uzh.ch/~acardona/trakem2_manual.html#importing_list) How the text file should look like.
