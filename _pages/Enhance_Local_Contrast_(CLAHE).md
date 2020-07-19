[[Image:Tem.jpg|thumb|left|361px|TEM original image]]
[[Image:Tem-clahe-50-256-2.5.jpg|thumb|right|361px|TEM CLAHE processed, (block: 50; bins: 256; max slope: 2.5)]]
{{-}}
{{Infobox
| name                   = Enhance Local Contrast (CLAHE)
| software               = Fiji
| author                  = {{Person|Saalfeld}} ([mailto:saalfeld@mpi-cbg.de])
| maintainer             = {{Person|Saalfeld}}
| source                 = [https://github.com/axtimwalde/mpicbg/tree/master/mpicbg/src/main/java/mpicbg/ij/clahe]
| released               = November 13<sup>th</sup>, 2009
| latest version         = September 1<sup>st</sup>, 2010
| status                 = stable, active
| category               = [[:Category:Plugins|Plugins]], [[:Category:Filtering|Filtering]]
}}
The plugin '''Enhance Local Contrast (CLAHE)''' implements the method ''[[wikipedia:CLAHE|Contrast Limited Adaptive Histogram Equalization]]''<ref>{{citation
 | last = Zuiderveld
 | first = Karel
 | contribution = Contrast limited adaptive histogram equalization
 | title = Graphics gems IV
 | pages = 474–485
 | publisher = Academic Press Professional, Inc.
 | address = San Diego, CA, USA
 | year = 1994
 | url = http://portal.acm.org/citation.cfm?id=180940 }} </ref>
for enhancing the local contrast of an image.  In Fiji, it is called through the menu entry '''Process / Enhance Local Contrast (CLAHE)'''.  The filter respects the selected regions of interest and triggers an Undo-step.

The method has three parameters:
;block size
:the size of the local region around a pixel for which the histogram is equalized.  This size should be larger than the size of features to be preserved.
;histogram bins
:the number of histogram bins used for histogram equalization.  The implementation internally works with byte resolution, so values larger than 256 are not meaningful.  This value also limits the quantification of the output when processing 8bit gray or 24bit RGB images.  The number of histogram bins should be smaller than the number of pixels in a block.
;max slope
:limits the contrast stretch in the intensity transfer function.  Very large values will let the histogram equalization do whatever it wants to do, that is result in maximal local contrast.  The value 1 will result in the original image.

In addition, the PlugIn asks for:
;mask
:choose, from the currently opened images, one that should be used as a mask for the filter application.  Selections and masks can be used exclusively or in combination.
;fast
:use the fast but less accurate version of the filter.  The fast version does not evaluate the intensity transfer function for each pixel independently but for a grid of adjacent boxes of the given '''block size''' only and interpolates for locations in between.
;process as composite
:images with multiple color channels can be processed in two modes
:;checked
::use the displayed image to estimate the intensity transfer that is then applied to all channels individually.  This is the desired mode for getting local contrast compression for color photographs with a higher bit-depth and higher dynamic range than appropriate for a digital display.
:;unchecked
::the selected channel is processed individually.

[[Image:Photo1.jpg|thumb|left|361px|Photo1 original image]]
[[Image:Photo1-clahe-150-256-3.jpg|thumb|right|361px|Photo1 CLAHE processed, (block: 150; bins: 256; max slope: 3)]]
{{-}}
[[Image:Photo3.jpg|thumb|left|361px|Photo2 original image]]
[[Image:Photo3-clahe-50-256-3.jpg|thumb|right|361px|Photo2 CLAHE processed, (block: 50; bins: 256; max slope: 3)]]
{{-}}

==Tips==

;How can I process a series/stack of images?
:Execute the following macro from [https://imagej.net/developer/macro/macros.html ImageJ's macro editor] or [[Using the Script Editor|Fiji's scripting editor]]:
<source lang="java">
blocksize = 127;
histogram_bins = 256;
maximum_slope = 3;
mask = "*None*";
fast = true;
process_as_composite = true;

getDimensions( width, height, channels, slices, frames );
isComposite = channels > 1;
parameters =
  "blocksize=" + blocksize +
  " histogram=" + histogram_bins +
  " maximum=" + maximum_slope +
  " mask=" + mask;
if ( fast )
  parameters += " fast_(less_accurate)";
if ( isComposite && process_as_composite ) {
  parameters += " process_as_composite";
  channels = 1;
}
  
for ( f=1; f<=frames; f++ ) {
  Stack.setFrame( f );
  for ( s=1; s<=slices; s++ ) {
    Stack.setSlice( s );
    for ( c=1; c<=channels; c++ ) {
      Stack.setChannel( c );
      run( "Enhance Local Contrast (CLAHE)", parameters );
    }
  }
}
</source>

==References==

<references />

[[Category:Plugins]]
[[Category:Filtering]]
