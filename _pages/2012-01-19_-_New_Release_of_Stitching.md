You can now reconstruct arbitrarily sized, tiled acquisitions (which can be multi-channel, time-lapse stacks) with just very little RAM (even <1GB) if you activate the options to write the result directly to disk and/or open the input stacks only virtually!!

Here is a list of all new highlights:

* supports composite images and hyperstacks now (arbitrary amount of channels and time-points)
* can optionally write the stitched image slice-by-slice directly to disk (significantly reduces the RAM requirements)
* can optionally open the input images as Virtual Stacks (significantly reduces the RAM requirements)
* supports timelapse alignment with different stitching options
* subpixel-resolution
* supports many different types of grids (row-by-row, column-by-column, snake, ...)
* can read the approximate tile positions from the image metadata
* finally based on ImgLib

There are only two plugins left, they replace the Stitching2D/3D and the Stitch Grid, ... Sequence, ... Collection and so on. They are called:

* '''Stitching -> Pairwise Stitching'''
* '''Stitching -> Grid/Collection Stitching'''

You will find a complete documentation on the Fiji wiki: 
[[Image_Stitching]]

The Stitching is deployed as a component of Fiji (simply update Fiji) or you can download it for ImageJ as a stand-alone package which includes all necessary libraries (11MB):
[http://fly.mpi-cbg.de/~preibisch/software.html#Stitching Download...]

I thank all the authors of the libraries and other people who helped me with the Stitching: [[Image_Stitching#Download_for_ImageJ_.26_Acknowledgements | Acknowledgements]]

Last but not least, it would be really nice if you could cite the publication that is associated with the plugin:

* S. Preibisch, S. Saalfeld, P. Tomancak (2009) "Globally optimal stitching of tiled 3D microscopic image acquisitions", ''Bioinformatics'', '''25'''(11):1463-1465. [http://bioinformatics.oxfordjournals.org/cgi/content/abstract/btp184 Webpage] [http://bioinformatics.oxfordjournals.org/cgi/reprint/25/11/1463.pdf PDF]

[[Category:News]]
