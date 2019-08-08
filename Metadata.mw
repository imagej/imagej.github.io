= What is metadata? =

When acquiring images in microscopy, the image files that are stored contain two main things:
# ''image data'': which is essentially 'pixel values'
# ''metadata'': information on the image data including pixel size, bit depth, dimension and objective information, etc.

Metadata is essential to correctly read image data; for example, to have accurate measurements, the image needs to be calibrated according to the correct/associated pixel size.  Saving and preserving metadata is key in quantitative image analysis.

= How do I open/read my metadata? =

To start, try a high level API approach via a GUI...
=== Using a GUI ===

If importing your images via [https://imagej.net/Bio-Formats#Bio-Formats_Importer Bio-Formats Importer] (which we suggest you do), you can either:
* In '''Stack Viewing''', View stack with: "Metadata only" 
OR
* In '''Metadata viewing''': check "Display Metadata" or "Display OME-XML metadata"

[[OMEVisual]] is another tool that can visualize OME metadata; it is a [[Fiji]] plugin.

These tools allow you to quickly check if your metadata 'looks' correct... are there the correct number of image blocks (i.e. one per tile if multi-scan image)?  Are the dimensions correct?  etc.

= What if I cannot read my metadata via a GUI?! =

Did you observe a problem with your metadata via a GUI?  Was there no data at all?  Or was metadata missing?  If this is the case, then perhaps there are structural issues with your metadata that require a bit more in-depth inspection via command line tools.

=== Using the Command Line ===
Bio-Formats has a whole host of information regarding extracting, processing, and validating OME-XML.  So check out [https://docs.openmicroscopy.org/ome-model/5.6.3/ome-tiff/tools.html their resources] for more detailed information.

In brief, there are [https://docs.openmicroscopy.org/bio-formats/6.2.0/users/comlinetools/ command line tools available via Bio-Formats] to properly inspect and validate the XML in an OME-TIFF file.

Both the <code>tiffcomment</code> and <code>xmlvalid</code> commands are used; <code>tiffcomment</code> extracts the XML from the file and <code>xmlvalid</code> validates the XML and prints any errors to the console.  See [https://docs.openmicroscopy.org/bio-formats/6.2.0/users/comlinetools/xml-validation.html this page] for more details.
