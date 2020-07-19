ImageJ has a simple and effective tool for Straightening images of curved structures, which can be found in the menus as "{{bc | Edit | Selection | Straighten...}}".  A silly example (straightening an MPI canteen banana) is shown here.

First, select the "Segmented Line" selection tool by right-clicking on the "Straight Line Selections" tool icon in the toolbar and choosing the "Segemented Lines" option.  Then click along a selection of points along the structure, completing the line with a right click.  You should have something like this:

[[Image:Tutorial-banana-selection.png|The original banana with a segmented line selection]]

Then select the {{bc | Edit | Selection | Straighten...}} menu option and you should be prompted for a line width - this determines the width around the line you've drawn that will be used in the final image.  In this case, the default was far too small, so I set it to 500 pixels.  The result after doing this looks like the following:

[[Image:Tutorial-banana-straightened.jpg|The result of running the Straighten plugin]]

Note that you will not be prompted for the line width when running the plugin a second time - you can change the line width with {{bc | Image | Adjust | Line Width...}}

The two images composed are shown below:

[[Image:Tutorial-bananas-result.jpg|The original banana and the straightened version]]

[[Category:Plugins]]
