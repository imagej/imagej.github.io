{{DISPLAYTITLE:Working with ImageJ}}

This part introduces some basic aspects of ImageJ so that you can use the software more efficiently. It also introduces some important terms and concepts used throughout this guide. You may skip it if you already use the program efficiently and are familiar with terms such as [[#sub:Virtual-Stacks|Virtual Stacks↓]], [[#sub:Hyperstacks-Intro|Hyperstacks↓]], [[#sub:Pseudocolor-Images|Pseudocolor Images↓]], [[#sub:Color-Composites|Color Composite Images↓]] or [[#sub:Composite-selections|Composite Selections↓]].

==Using Keyboard Shortcuts==

You’ll learn more and more [[#index-Keyboard|↓]][[#index-Shortcuts|↓]]shortcut keys as you use ImageJ, because (almost) all shortcuts are listed throughout ImageJ menus. Similarly, in this guide each command has its shortcut key listed on its name (flanked by square brackets). Please note that the notation for these key-bindings is case sensitive, i.e., Shift-modifiers are not explicitly mentioned (a capital <span class="sans">A</span> means <span class="sans">Shift--A</span>) and assumes that ''Require control key for shortcuts'' in <span class="sans"><span class="menuitem"><span class="sans">Edit ▷ Options ▷ [[#sub:Misc...|Misc…↓]]</span></span></span> is unchecked (i.e., except when using the IJ [[#sub:ImageJ-Macro-Editor|Editor↓]] or the [[#sec:Text-Tool|Text Tool↓]], you won’t have to hold down the Control key to use menu shortcuts). For example, the command <span class="sans"><span class="menuitem"><span class="sans">Edit ▷ [[#sub:Invert-%5BI%5D|Invert [I]↓]]</span></span></span> can be evoked by <span class="Keystroke">Shift</span> <span class="Keystroke">I</span> or <span class="Keystroke">Ctrl</span> <span class="Keystroke">Shift</span> <span class="Keystroke">I</span> if ''Require control key for shortcuts'' is checked. The full list of ImageJ shortcuts (''see'' [[#sec:Keyboard-Shortcuts|Keyboard Shortcuts↓]]) can be retrieved at any time using the <span class="sans"><span class="menuitem"><span class="sans">Plugins ▷ Utilities ▷ [[#sub:List-Shortcuts...|List Shortcuts…↓]]</span></span></span> command.

There are three [[#index-Modifier-keys|↓]]modifier keys in ImageJ:

<div class="Labeling">

'''Control''' ('''Command Key'''[[#index-Command-key|↓]] on Apple keyboards) Denoted by ‘Ctrl’[[#nom-ctrl|↓]] or <span class="Keystroke">Ctrl</span> in this document. Although a control key is typically present on Apple keyboards, on a Macintosh computer running ImageJ the Command key <span class="Keystroke"><span class="unknown">\cmd</span>  Cmd</span> replaces the functionality of the Control key of other operating systems. For sake of simplification, ‘Ctrl’ will always refer to both throughout this guide.

</div>
<div class="Labeling">

'''Shift''' Denoted by ‘Shift’[[#nom-shift|↓]] or <span class="Keystroke">Shift</span> in this document.

</div>
<div class="Labeling">

'''Alt''' Denoted by ‘Alt’[[#nom-alt|↓]] or <span class="Keystroke">Alt</span> in this document. This is also the ‘Option’ or ‘Meta’ key on many keyboards. In ImageJ, it is also used to type special unit symbols such as <span class="formula"><span class="unknown">\micro</span></span> (<span class="Keystroke">Alt</span><span class="Keystroke">M</span>) or <span class="formula"><span class="unknown">\angstrom</span></span> (<span class="Keystroke">Alt</span><span class="Keystroke">Shift</span><span class="Keystroke">A</span>).

</div>
<div class="See">

[[#sec:Keyboard-Shortcuts|Keyboard Shortcuts↓]], <span class="menuitem">Plugins ▷ [[#sub:Shortcuts|Shortcuts ▷ ↓]]</span>

</div>
<div class="float">

[[|]]
<div class="infobox">

<div class="caption">

float-infobox2 Frontmost Window and Window Activation

</div>
In ImageJ, all operations are performed on the active (frontmost) image (which has its title bar highlighted). If a window is already open it will activate when its opening command is re-run, e.g., if the B&amp;C window is already opened (<span class="menuitem">Image ▷ Adjust ▷ [[#sub:Brightness/Contrast...%5BC%5D|Brightness/Contrast… [C]↓]]</span>), pressing its keyboard shortcut ( <span class="Keystroke">Shift</span> <span class="Keystroke">C</span> ) will activate it.
<div class="medskip">



</div>
<div class="PlainVisible">

Pressing <span class="Keystroke">Enter</span> on any image will bring the [[#fig:The-ImageJ-window|]]
<div class="PlainVisible">

Main ImageJ window

</div>
↓ to the foreground. In addition, it is also possible to permanently place the main window above all other windows (''see'' [[#sub:FloatingMainWin|Floating Behavior of Main Window↓]]).

</div>

</div>

</div>

==Finding Commands==

Navigating through the extensive list of ImageJ commands, macros and plugins may be quite cumbersome. Through its built-in Command Finder / Launcher<span class="bibcites">[[[#biblio-48|48]]]</span>, ImageJ offers an expedite alternative that allows you to retrieve commands extremely fast: <span class="sans"><span class="menuitem"><span class="sans">Plugins ▷ Utilities ▷ [[#sub:Command-Finder|Find Commands… [l]↓]]</span></span></span>.

In addition, ImageJ features a find function that locates macros, scripts and plugins source (<span class="Filename">.java</span>) files on your computer: the <span class="sans"><span class="menuitem"><span class="sans">Plugins ▷ Utilities ▷ [[#sub:Search...|<span class="menuitem">Search…</span>↓]]</span></span></span> command. Because most of IJ source files contain circumstanced comments, you can use this utility to retrieve files related not only to a image processing routine (e.g., ''background'' or ''co-localization'') but also to a practical context such as ''radiogram'', ''cell'' or ''histology''. Indeed, ImageJ source files contain detailed annotations useful to both developers and regular users that want to know more about ImageJ routines and algorithms.

<span class="sans"><span class="menuitem"><span class="sans">[[#sub:Search...|<span class="menuitem">Search…</span>↓]]</span></span></span> and <span class="sans"><span class="menuitem"><span class="sans">[[#sub:Command-Finder|Find Commands… [l]↓]]</span></span></span> are described in detail in <span class="sans"><span class="menuitem"><span class="sans">Plugins ▷ [[#sub:Utilities|Utilities ▷ ↓]]</span></span></span>.
<div class="float">

<div class="figure">

<div class="center">

<span class="hspace" style="width: 11.1em;"></span><span class="sans"><span class="small">Plugins ▷ Utilities ▷ [[#sub:Command-Finder|Find Commands… [l]↓]]</span></span>
<div class="vspace" style="height: 3pt;">



</div>

</div>
<div class="PlainVisible">

<div class="center">

[[File:images/CommandFinderAndSearch.png|class=embedded|figure images/CommandFinderAndSearch.png]]

</div>

</div>
<div class="PlainVisible">

<div class="center">

<span class="sans"><span class="small">Plugins ▷ Utilities ▷ [[#sub:Search...|<span class="menuitem">Search…</span>↓]]</span></span>

</div>

</div>

</div>

</div>

<div class="See">

[[#sub:Control-Panel...|Control Panel… [U]↓]], [[#sec:Keyboard-Shortcuts|Keyboard Shortcuts↓]] and <span class="Filename">[http://imagej.nih.gov/ij/macros/SourceCodeRetriever.txt SourceCodeRetriever]</span>, a macro that searches for a menu entry and retrieves the source file of the respective command

</div>
==Undo and Redo==

Probably the first thing you will notice is that ImageJ does not have a large [[#index-Undo|↓]]undo/redo buffer. Undo (<span class="sans"><span class="menuitem"><span class="sans">Edit ▷ [[#sub:Undo-%5Bz%5D|Undo [z]↓]]</span></span></span>) is currently limited to the most recent image editing / filtering operation. With time you will appreciate that this is necessary to minimize memory overhead. Nevertheless, with IJ 1.45 and later, <span class="sans"><span class="menuitem"><span class="sans">[[#sub:Undo-%5Bz%5D|Undo [z]↓]]</span></span></span> is, in most cases, undoable and can be applied to multiple images if ''Keep multiple undo buffers'' is checked in <span class="sans"><span class="menuitem"><span class="sans">Edit ▷ Options ▷ [[#sub:Memory-&-Threads...|Memory &amp; Threads…↓]]</span></span></span>

If you cannot recover from a mistake, you can always use <span class="sans"><span class="menuitem"><span class="sans">File ▷ [[#sub:Revert%5Br%5D|Revert [r]↓]]</span></span></span> to reset the image lo its last saved state. For selections, <span class="sans"><span class="menuitem"><span class="sans">Edit ▷ Selection ▷ [[#sub:Restore-Selection-%5BE%5D|Restore Selection [E]↓]]</span></span></span> can be used to recover any misdealt selection.

In ImageJ the equivalent to [[#index-Redo|↓]]‘Redo’ is the <span class="sans"><span class="menuitem"><span class="sans">Process ▷ [[#sub:Repeat-Command-%5BR%5D|Repeat Command [R]↓]]</span></span></span>, that re-runs the previous used command (skipping <span class="sans"><span class="menuitem"><span class="sans">Edit ▷ [[#sub:Undo-%5Bz%5D|Undo [z]↓]]</span></span></span> and <span class="sans"><span class="menuitem"><span class="sans">File ▷ [[#sub:Open...|Open… [o]↓]]</span></span></span> commands).

<div class="See">

<span class="sans"><span class="menuitem"><span class="sans">Plugins ▷ Utilities ▷ [[#sub:Reset...|Reset…↓]]</span></span></span>, [http://imagejdocu.tudor.lu/doku.php?id=plugin:utilities:multi_undo:start Multi Undo] plugin

</div>
==Image Types and Formats==

[[#index-Image-types|↓]]Digital Images are two-dimensional grids of pixel[[#nom-pixel|↓]] intensities values with the width and height of the image being defined by the number of pixels in <span class="formula">''x''</span> (rows) and <span class="formula">''y''</span> (columns) direction. Thus, pixels (picture elements) are the smallest single components of images, holding numeric values — pixel intensities — that range between black and white. The characteristics of this range, i.e., the number of unique intensity (brightness) values that can exist in the image is defined as the bit[[#nom-bit|↓]]--depth of the image and specifies the level of precision in which intensities are coded, e.g.: A 2--bit image has <span class="formula">2<sup>2</sup> = 4</span> tones: 00 (black), 01 (gray), 10 (gray), and 11 (white). A 4--bit image has <span class="formula">2<sup>4</sup> = 16</span> tones ranging from 0000 (0) to 1111 (16), etc. In terms of bits per pixel (bpp[[#nom-bpp|↓]]), the most frequent types of images (<span class="menuitem">Image ▷ [[#sub:Type|Type ▷ ↓]]</span>) that ImageJ deals with are ([[#index-ImageJ2|↓]][[#sub:ImageJ2intro|ImageJ2↑]] supports [http://imagejdev.org/imagej2-pixel-types many more types of image data]):

<div class="Labeling">

'''8--bit''' Images that can display 256 (<span class="formula">2<sup>8</sup></span>) gray levels (integers only).

</div>
<div class="Labeling">

'''16--bit''' Images that can display 65, 536 (<span class="formula">2<sup>16</sup></span>) gray levels (integers only).

</div>
<div class="Labeling">

'''32--bit''' Images that can display 4, 294, 967, 296 (<span class="formula">2<sup>32</sup></span>) gray levels (real numbers). In 32--bit images, pixels are described by [http://en.wikipedia.org/wiki/Floating_point floating point] values and can have<span class="versalitas"> any</span> intensity value including ''NaN''[[#nom-nan|↓]] (Not a Number).

</div>
<div class="Labeling">

'''RGB Color''' [[#sec:Color-Images|Color Images↓]] that can display 256 values in the Red, Green and Blue channel. These are 24--bit (<span class="formula">2<sup>3 × 8</sup></span>) images. RGB[[#nom-rgb|↓]] color images can also be 32--bit color images (24--bit color images with additional eight bits coding alpha blending values, i.e., transparency).

</div>
===Native Formats===


Natively (i.e. without the need of third-party plugins) ImageJ opens the following formats: '''TIFF'''[[#nom-tiff|↓]], '''GIF'''[[#nom-gif|↓]], '''JPEG'''[[#nom-jpeg|↓]], '''PNG'''[[#nom-png|↓]], '''DICOM'''[[#nom-dicom|↓]], '''BMP'''[[#nom-bmp|↓]], '''PGM'''[[#nom-pgm|↓]] and '''FITS'''[[#nom-fits|↓]]. [[#index-Image-formats-Native|↓]]Many more formats are supported with the aid of plugins. These are discussed in [[#sub:Non-native-Supported-Formats|Non--native Formats ↓]].

<div class="Labeling">

'''TIFF''' (Tagged Image File Format) is the ‘default’ format of ImageJ (cf. <span class="sans"><span class="menuitem"><span class="sans">File ▷ [[#sub:Save%5Bs%5D|Save [s]↓]]</span></span></span>). Images can be 1--bit, 8--bit, 16--bit (unsigned<span class="FootOuter"><span class="SupFootMarker"> [C] </span><span class="HoverFoot"><span class="SupFootMarker"> [C] </span>A numeric variable is signed if it can represent both positive and negative numbers, and unsigned if it can only represent positive numbers.</span></span>), 32--bit (real) or RGB color. [[#index-TIFF|↓]]TIFF files with multiple images of the same type and size open as [[#sub:Stacks-Intro|Stacks↓]] or [[#sub:Hyperstacks-Intro|Hyperstacks↓]]. ImageJ opens [[#index-Lossless-compression|↓]]lossless compressed TIFF files (''see'' [[#infobox:Formats|3↓]] [[#infobox:Formats|Image Types: Lossy Compression and Metadata↓]]) by the LZW[[#nom-lzw|↓]][[#index-LZW-compression|↓]], [[#index-PackBits-compression|↓]]PackBits and [[#index-ZIP-Lossless-compression|↓]]ZIP ([[#index-Deflate|↓]]Deflate/Inflate) <span class="bibcites">[[[#biblio-2|2]]]</span> compression schemes. In addition, TIFF files can be opened and saved as [[#index-ZIP-Archived-TIFF-files|↓]]ZIP archives.<br />
Tiff tags and information needed to import the file (number of images, offset to first images, gap between images) are printed to the [[#sec:Log-Window|Log Window↓]] when ImageJ is running in ''Debug Mode'' (<span class="menuitem">Edit ▷ Options ▷ [[#sub:Misc...|Misc…↓]]</span>, ''see'' [[#sec:Settings-and-Preferences|Settings and Preferences↓]]).

</div>
<div class="Labeling">

'''DICOM''' (Digital Imaging and Communications in Medicine) is a standard popular in the medical imaging community. Support in ImageJ is limited to uncompressed [[#index-DICOM|↓]]DICOM files. DICOM files containing multiple images open as [[#sub:Stacks-Intro|Stacks↓]].<br />
Use <span class="sans"><span class="menuitem"><span class="sans">Image ▷ [[#sub:Show-Info...|]]</span></span></span>
<div class="PlainVisible">

<span class="menuitem"></span>
<div class="PlainVisible">

Show Info… [i]

</div>

</div>
↓ to display the DICOM header information. A DICOM sequence can be opened using <span class="sans"><span class="menuitem"><span class="sans">File ▷ Import ▷ [[#sub:Image-Sequence...|<span class="menuitem">Image Sequence…</span>↓]]</span></span></span> or by dragging and dropping the folder on the ‘ImageJ’ window. Imported sequences are sorted by image number instead of filename and the tags are preserved when DICOM images are saved in TIFF format. ImageJ supports custom DICOM dictionaries, such as the one at http://imagej.nih.gov/ij/download/docs/DICOM_Dictionary.txt. More information can be found at the [http://www.cabiatl.com/mricro/dicom/index.html Center for Advanced Brain Imaging].

</div>
<div class="Labeling">

'''FITS''' (Flexible Image Transport System) image is the format adopted by the astronomical community for data interchange and archival storage. Use <span class="sans"><span class="menuitem"><span class="sans">Image ▷ [[#sub:Show-Info...|]]</span></span></span>
<div class="PlainVisible">

<span class="menuitem"></span>
<div class="PlainVisible">

Show Info… [i]

</div>

</div>
↓ to display the [[#index-FITS|↓]]FITS header. More information [http://fits.gsfc.nasa.gov here].

</div>
<div class="Labeling">

'''PGM''' ([[#index-PGM|↓]]Portable GrayMap), '''PBM[[#nom-pbm|↓]]''' (Portable BitMap) and '''PPM[[#nom-ppm|↓]]''' (Portable PixMap) are simple image formats that use an ASCII[[#nom-ascii|↓]] header. More information [http://local.wasp.uwa.edu.au/~pbourke/dataformats/ppm/ here].

</div>
<div class="Labeling">

'''AVI''' (Audio Video Interleave) is a container format which can contain data encoded in many different ways. ImageJ only supports uncompressed [[#index-AVI|↓]]AVIs, various [[#index-YUV|↓]]YUV 4:2:2 compressed formats, and [[#index-PNG|↓]]PNG or [[#index-JPEG|↓]]JPEG-encoded individual frames. Note that most [[#index-MJPG|↓]]MJPG[[#nom-mjpg|↓]] (motion-JPEG) formats are not read correctly. Attempts to open AVIs in other formats will fail.

</div>
<div class="See">

[[#sub:Non-native-Supported-Formats|Non--native Formats ↓]], [[#infobox:Formats|3↓]] [[#infobox:Formats|Image Types: Lossy Compression and Metadata↓]], [[#infobox:JpegAlert|11↓]] [[#infobox:JpegAlert|Warning on JPEG Compression↓]]

</div>
===Non--native Formats===

When opening a file, ImageJ first checks whether it can natively handle the format. [[#index-Image-formats-Non-native|↓]]If ImageJ does not recognize the type of file it calls for the appropriate reader plugin using [http://imagej.nih.gov/ij/plugins/file-handler.html HandleExtraFileTypes], a plugin bundled with ImageJ. If that fails, it tries to open the file using the [[#index-OME-Bio-Formats|↓]][[#index-LOCI-Bio-Formats|↓]][[#index-Bio-formats|↓]][http://loci.wisc.edu/software/bio-formats OME Bio-Formats library] (if present), a remarkable plugin that supports more than [http://loci.wisc.edu/bio-formats/formats one hundred of the most common] file formats used in microscopy. If nevertheless the file cannot be opened, an error message is displayed.

Because both these plugins are under active development, it is important that you keep them updated. The OME Bio-Formats library can be updated using its self-updating plugin (<span class="menuitem">Plugins ▷ LOCI ▷ Update LOCI Plugin…</span>) or Fiji↑’s built-in updater (<span class="menuitem">Help ▷ Update Fiji…</span>). The following websites provide more information on the OME Bio-Formats:

* http://loci.wisc.edu/bio-formats/imagej
* https://fiji.sc/Bio-Formats
* http://loci.wisc.edu/bio-formats/using-bio-formats

In addition, the ImageJ web site lists [http://imagej.nih.gov/ij/plugins/#io more than sixty plugins] that recognize more ‘exotic’ file formats. The ImageJ Documentation Portal also maintains a (somewhat outdated) [http://imagejdocu.tudor.lu/doku.php?id=faq:general:which_file_formats_are_supported_by_imagej list of file formats] that are supported by ImageJ.

<div class="See">

[[#sub:Native-Formats|Native Formats↑]], <span class="sans"><span class="menuitem"><span class="sans">File ▷ [[#sub:Import|Import ▷ ↓]]</span></span></span>, [[#infobox:Formats|3↓]] [[#infobox:Formats|Image Types: Lossy Compression and Metadata↓]], [[#infobox:JpegAlert|11↓]] [[#infobox:JpegAlert|Warning on JPEG Compression↓]], [http://imagej.nih.gov/ij/plugins/#acq Acquisition plugins], [http://imagej.nih.gov/ij/plugins/#io Input/Output plugins]

</div>

<div class="float">

[[|]]
<div class="infobox">

<div class="caption">

float-infobox3 Image Types: Lossy Compression and Metadata

</div>
Two critical aspects to keep in mind when converting images:
<div class="Description">

<span class="Description-entry">[[|]]</span> [[|]]Lossy compression Transcoding an image into a format that uses [[#index-Lossy-compression|↓]]lossy compression will alter the original data, introducing artifacts (''see'' [[#infobox:JpegAlert|11↓]] [[#infobox:JpegAlert|Warning on JPEG Compression↓]]). This is the case, e.g., for JPEG formats (with the exception of some [[#index-JPEG2000|↓]]JPEG2000 images that use lossless compression). As such, these types of data are intended for human interpretation only and are not suitable for quantitative analyses

</div>
<div class="Description">

<span class="Description-entry">[[|]]</span> [[|]]Metadata In ImageJ, [[#index-Metadata|↓]]metadata associated with the image, such as scale, gray value calibration and user comments is only supported in tiff and zip (compressed tiff) images. In addition, selections and [[#sub:Overlay-Intro|Overlays↓]] are also saved in the TIFF header (cf. <span class="sans"><span class="menuitem">File ▷ [[#sub:Save%5Bs%5D|Save [s]↓]]</span></span>). None of the above is saved in other formats (cf. [[#sub:Native-Formats|Native Formats↑]]).

</div>

</div>

</div>

==Stacks, Virtual Stacks and Hyperstacks==

===Stacks===

ImageJ can display multiple spatially or temporally related images in a single window. These image sets are called stacks. The images that make up a stack are called slices. In [[#index-Stacks|↓]]stacks, a pixel (which represents 2D image data in a bitmap image) becomes a voxel[[#nom-voxel|↓]] (volumetric pixel), i.e., an intensity value on a regular grid in a three dimensional space.

All the slices in a stack must be the same size and bit depth. A scrollbar provides the ability to move through the slices and the slider is preceded by a play/pause icon that can be used to start/stop stack animation. Right-clicking on this icon runs the <span class="menuitem">[[#sub:Animation-Options...|Animation Options… [Alt /]↓]]</span> dialog box.

Most ImageJ filters will, as an option, process all the slices in a stack. ImageJ opens multi-image TIFF files as a stack, and saves stacks as multi-image TIFFs. The <span class="menuitem"><span class="sans">File ▷ Import ▷ </span>[[#sub:Import%3ERaw|Raw…↓]]</span> command opens other multi-image, uncompressed files. A folder of images can be opened as a stack either by dragging and dropping the folder onto the ‘ImageJ’ window or or by choosing <span class="menuitem"><span class="sans">File ▷ Import ▷ </span>[[#sub:Image-Sequence...|<span class="menuitem">Image Sequence…</span>↓]]</span> To create a new stack, simply choose <span class="menuitem">File ▷ New ▷ [[#sub:Image...%5Bn%5D|Image… [n]↓]]</span> and set the ''Slices'' field to a value greater than one. The <span class="menuitem">Image ▷ [[#sub:Stacks|Stacks ▷ ↓]]</span> submenu contains commands for common stack operations.
<div class="float">

[[|]]
<div class="figure">

[[File:images/StacksHyperstacks.png|class=embedded|figure images/StacksHyperstacks.png]]
<div class="caption">

Figure 2 '''Stacks and Hyperstacks in ImageJ:<span class="sans"></span>''' <span class="menuitem">File ▷ Open Samples ▷ Mitosis (26MB, 5D stack)</span>. Hyperstacks dimensionality can be reduced using <span class="menuitem">Image ▷ Hyperstacks ▷ [[#sub:Reduce-Dimensionality...|Reduce Dimensionality…↓]]</span>, <span class="menuitem">Image ▷ Stacks ▷ [[#sub:Z-Project...|<span class="menuitem">Z Project…</span>↓]]</span> or <span class="menuitem">Image ▷ Hyperstacks ▷ [[#sub:Channels...%5BZ%5D|Channels Tool… [Z]↓]]</span> The ‘(V)’ on the window title denotes a virtual image (''see'' [[#sub:Virtual-Stacks|Virtual Stacks↓]]).

</div>

</div>

</div>

<div class="See">

<span class="small">[[#sub:StacksMenu|Stacks Menu↓]], [https://fiji.sc/wiki/index.php/Stack_Manipulation Stack Manipulations] on Fiji website, [http://imagej.nih.gov/ij/plugins/image5d.html Image5D]</span>

</div>
===Virtual Stacks===

[[#index-Stacks-Virtual|↓]][[#index-Virtual-stacks|↓]]Virtual stacks are disk resident (as opposed to RAM[[#nom-ram|↓]] resident) and are the only way to load image sequences that do not fit in RAM. There are several things to keep in mind when working with virtual stacks:

<ul>
<li>Virtual stacks are read-only, so changes made to the pixel data are not saved when you switch to a different slice. You can work around this by using macros (e.g., <span class="small">[http://imagej.nih.gov/ij/macros/Process_Virtual_Stack.txt Process Virtual Stack]</span><span class="default">) or the <span class="sans"><span class="menuitem"><span class="sans">Process ▷ Batch ▷ [[#sub:Virtual-Stack...|<span class="menuitem">Virtual Stack…</span>↓]]</span></span></span> command</span></li>
<li>You can easily run out of memory using commands like <span class="sans"><span class="menuitem"><span class="sans">Image ▷ </span>[[#sub:Crop-%5BX%5D|]]</span></span>
<div class="PlainVisible">

<span class="menuitem"></span>
<div class="PlainVisible">

Crop [X]

</div>

</div>
↓ because any stack generated from commands that do not generate virtual stacks will be RAM resident.</li>
<li>TIFF virtual stacks can usually be accessed faster than [[#index-JPEG|↓]]JPEG virtual stacks. A JPEG sequence can be converted to TIFF by opening the JPEG images as a virtual stack and using <span class="sans"><span class="menuitem"><span class="sans">File ▷ Save As ▷ </span>[[#sub:SaveAs%3EImage-Seq...|<span class="menuitem">Image Sequence…</span>↓]]</span></span> to save in TIFF format</li></ul>

ImageJ appends a ‘(V)’ to the window title of virtual stacks and hyperstacks (''see'' [[#sub:Hyperstacks-Intro|Hyperstacks↓]]). Several built-in ImageJ commands in the <span class="sans"><span class="menuitem"><span class="sans">File ▷ </span>[[#sub:Import|Import ▷ ↓]]</span></span> submenu have the ability to open virtual stacks, namely: <span class="menuitem">[[#sub:Import%3ETIFF-Virtual-Stack|TIFF Virtual Stack…↓]]</span>, <span class="menuitem">[[#sub:Image-Sequence...|<span class="menuitem">Image Sequence…</span>↓]]</span>, <span class="menuitem">[[#sub:Import%3ERaw|Raw…↓]]</span>,<span class="sans"> </span><span class="menuitem">[[#sub:Stack-From-List...|<span class="menuitem">Stack From List…</span>↓]]</span>,<span class="sans"> </span><span class="menuitem">[[#sub:Import%3EAVI...|<span class="menuitem">AVI…</span>↓]]</span> (cf. [http://imagej.nih.gov/ij/plugins/virtual-opener.html Virtual Stack Opener]). In addition, TIFF stacks can be open as virtual stacks by drag and drop (cf. [[#infobox:VirtualTiff|4↓]] [[#infobox:VirtualTiff|Opening Virtual Stacks by Drag &amp; Drop↓]]).

<div class="See">

<span class="small">[http://www.loci.wisc.edu/ome/formats.html LOCI Bio-Formats] and [https://fiji.sc/wiki/index.php/Register_Virtual_Stack_Slices RegisterVirtualStackSlices] plugins, [http://imagej.nih.gov/ij/macros/Process_Virtual_Stack.txt Process Virtual Stack] and [http://imagej.nih.gov/ij/macros/VirtualStackFromList.txt VirtualStackFromList] macros </span>

</div>
<div class="float">

[[|]]
<div class="infobox">

<div class="caption">

float-infobox4 Opening Virtual Stacks by Drag &amp; Drop

</div>
TIFF stacks with a <span class="Filename">.tif</span> extension open as virtual stacks when dragged and dropped on the<span class="sans"> [[File:images/tools/Switcher-small.png|class=embedded|figure images/tools/Switcher-small.png]]  </span>toolbar icon.
<div class="medskip">



</div>
<div class="PlainVisible">

<div class="center">

[[File:images/DragAndDropVirtualTiff.png|class=embedded|figure images/DragAndDropVirtualTiff.png]]

</div>

</div>

</div>

</div>

===Hyperstacks===

[[#index-Stacks-Hyperstacks|↓]]Hyperstacks are multidimensional images, extending image stacks to four (4D) or five (5D) dimensions: <span class="formula">''x''</span> (width), <span class="formula">''y''</span> (height), <span class="formula">''z''</span> (slices), <span class="formula">''c''</span> (channels or wavelengths) and <span class="formula">''t''</span> (time frames). Hyperstacks are displayed in a window with three labelled scrollbars (''see'' [[#fig:Stacks-and-Hyperstacks|Stacks and Hyperstacks↑]]). Similarly to the scrollbar in [[#sub:Stacks-Intro|Stacks↑]], the frame slider (''t'') has a play/pause icon.

<div class="See">

<span class="menuitem"><span class="sans">Image</span> ▷ [[#sub:Hyperstacks|Hyperstacks ▷ ↓]]</span> submenu

</div>
==Color Images<span class="FootOuter"><span class="SupFootMarker"> [D] </span><span class="HoverFoot"><span class="SupFootMarker"> [D] </span>This section is partially extracted from the MBF ImageJ online manual at http://www.macbiophotonics.ca/imagej/colour_image_processi.htm.</span></span>==

[[#index-MBF-ImageJ|↓]]ImageJ deals with color mainly in three ways: pseudocolor images, RGB images, RGB/ HS<span class="small">B[[#nom-hsb|↓]]</span><span class="default"> stacks, and composite images.[[#index-Image-types|↓]]</span>

===Pseudocolor Images===

A pseudocolor (or indexed color) image is a single channel gray image (8, 16 or 32--bit) that has color assigned to it via a lookup table or LUT[[#nom-lut|↓]][[#index-LUT|↓]]. A LUT is literally a predefined table of gray values with matching red, green and blue values so that shadows of gray are displayed as colorized pixels. Thus, differences in color in the pseudo-colored image reflect differences in intensity of the object rather than differences in color of the specimen that has been imaged.

8-bit indexed color images (such as GIFs) are a special case of pseudocolor images as their lookup table is stored in the file with the image. These images are limited to 256 colors (24--bit RGB images allow 16.7 million of colors, ''see'' [[#sec:Image-Types|Image Types and Formats↑]]) and concomitantly smaller file sizes. Reduction of true color values to a 256 [[#index-Color-palette|↓]]color palette is performed by color quantization algorithms. ImageJ uses the [[#index-Color-Quantization|↓]][[#index-Heckbert-quantization|↓]][[#index-Algorithm-Heckbert-quantization|↓]]Heckbert’s median-cut color quantization algorithm (''see'' <span class="menuitem">Image ▷ [[#sub:Type|Type ▷ ↓]]</span> menu), which, in most cases, allows indexed color images to look nearly identical to their 24-bit originals.

<div class="See">

<span class="menuitem"><span class="sans">Image</span> ▷ [[#sub:Lookup-Tables|Lookup Tables ▷ ↓]]</span> and [[#sub:LUTMenu|LUT Menu↓]]

</div>
===True Color Images===

As described in [[#sec:Image-Types|Image Types and Formats↑]], true color images such as RGB images reflect genuine colors, i.e., the green in an RGB image reflects green color in the specimen. Color images are typically produced by color CCD[[#nom-ccd|↓]] cameras, in which [[#index-Color-filter-array|↓]]color filter arrays ([http://en.wikipedia.org/wiki/Bayer_filter Bayer masks]) are placed over the image sensor.[[#index-CCD|↓]]

====Color Spaces and Color Separation====

[http://en.wikipedia.org/wiki/Color_space Color spaces] [[#index-Color-Models|↓]]describe the gamut of colors that image-handling devices deal with. Because human vision is trichromatic, most color models represent colors by three values. Mathematically, these values (color components) form a three-dimensional space such as the RGB[[#index-RGB|↓]], [[#index-HSB|↓]]HSB, [[#index-CIE-Lab|↓]]CIE Lab or [[#index-YUV|↓]]YUV color space.
<div class="float">

[[|]]
<div class="figure" style="max-width: 100%;">

[[File:images/RGB-HSBcolorModels.png|class=figure|figure images/RGB-HSBcolorModels.png]]
<div class="caption">

Figure 3 '''Representation of an eight pixel color image in the RGB and HSB color spaces.''' The RGB color space maps the RGB color model to a cube with ''Red'' (R) values increasing along the x-axis, ''Green'' (G) along the y-axis and ''Blue'' (B) along the z-axis. In the HSB cylindrical coordinate system, the angle around the central vertical axis corresponds to ''Hue'' (H), the distance from the axis corresponds to ''Saturation'' (S), and the distance along the axis corresponds to ''Brightness'' (B). In both cases the origin holds the black color. The right panel shows the same image after brightness reduction, easily noted by the vertical displacement along the HSB cylinder. Images produced using Kai Uwe Barthel’s [http://www.f4.fhtw-berlin.de/~barthel/ImageJ/ColorInspector//help.htm 3D Color Inspector] plugin.

</div>

</div>

</div>

RGB (Red, Green, Blue) is the most commonly-used color space. However, other alternatives such as HSB (Hue, Saturation, Brightness) provide significant advantages when processing color information. In the HSB color space, ''Hue'' describes the attribute of pure color, and therefore distinguishes between colors. ''Saturation'' (sometimes called “purity” or “vibrancy”) characterizes the shade of color, i.e., how much white is added to the pure color. ''Brightness'' (also know as ''Value'' — HSV system) describes the overall brightness of the color (''see'' e.g., the color palette of [[#fig:CPtool|Color Picker window↓]]). In terms of digital imaging processing, using the HSB system over the traditional RGB is often advantageous: e.g., since the Brightness component of an HSB image corresponds to the grayscale version of that image, processing only the brightness channel in routines that require grayscale images is a significant computational gain<span class="FootOuter"><span class="SupFootMarker"> [E] </span><span class="HoverFoot"><span class="SupFootMarker"> [E] </span>''See'' Wootton R, Springall DR, Polak JM. Image Analysis in Histology: Conventional and Confocal Microscopy. ''Cambridge University Press'', 1995'','' ISBN 0521434823</span></span>. You can read more about the HSB color model [http://en.wikipedia.org/wiki/HSB_color_space here].

In ImageJ, conversions between image types are performed using the <span class="menuitem"><span class="sans"><span class="small">Image</span></span><span class="default"> ▷ [[#sub:Type|Type ▷ ↓]]</span></span> submenu. Segmentation on the HSB, RGB, CIE Lab and YUV color spaces can be performed by the <span class="menuitem"><span class="sans"><span class="small">Image</span></span><span class="default"> ▷ Adjust ▷ [[#sub:Color-Threshold...|Color Threshold…↓]]</span></span> command <span class="bibcites">[[[#biblio-20|20]]]</span>. Segregation of color components (specially useful for quantification of [[#index-Color-Deconvolution|↓]][[#index-Color-Separation|↓]][[#index-Immunohistochemistry|↓]]histochemical staining) is also possible using Gabriel Landini’s [http://www.dentistry.bham.ac.uk/landinig/software/cdeconv/cdeconv.html Colour Deconvolution] plugin. In addition, several other plugins related to color processing can be obtained from the [http://imagej.nih.gov/ij/plugins/index.html#color ImageJ website].

====Conveying Color Information<span class="FootOuter"><span class="SupFootMarker"> [F] </span><span class="HoverFoot"><span class="SupFootMarker"> [F] </span>This section is partially extracted from Masataka Okabe and Kei Ito, ''Color Universal Design (CUD) — How to make figures and presentations that are friendly to Colorblind people'', http://jfly.iam.u-tokyo.ac.jp/color/, accessed 2009.01.15</span></span>====

People see color with significant variations. Indeed, the popular phrase “One picture is worth ten thousand words” may not apply to certain color images, specially those that do not follow the basic principles of [http://jfly.iam.u-tokyo.ac.jp/color/ Color Universal Design]. Citing Masataka Okabe and Kei Ito:

<blockquote>[[#index-Color-Blindness|↓]]Colorblind people can recognize a wide ranges of colors. But certain ranges of colors are hard to distinguish. The frequency of colorblindness is fairly high. One in 12 Caucasian (8%), one in 20 Asian (5%), and one in 25 African (4%) males are so-called ‘red--green’ colorblind.</blockquote>
<blockquote>There are always colorblind people among the audience and readers. There should be more than <span class="versalitas">ten</span> colorblind in a room with 250 people (assuming 50% male and 50% <span class="small">female</span><span class="default">).</span></blockquote>
<blockquote>[ …] There is a good chance that the paper you submit may go to colorblind reviewers. Supposing that your paper will be reviewed by three white males (which is not unlikely considering the current population in science), the probability that at least one of them is colorblind is whopping 22%!</blockquote>

<div class="float">

[[|]]
<div class="figure" style="max-width: 100%;">

[[File:images/Dichromacy.png|class=figure|figure images/Dichromacy.png]]
<div class="caption">

Figure 4 '''Red--green images and partial color blindness.''' Deuteranopia (second panel), protanopia (third panel) are the most common types of partial color blindness (red / green confusion). Tritanopia (blue / orange confusion, fourth panel) is quite rare. [[#infobox:Replacing-Red-w-Magenta|Replacing Red with Magenta in RGB Images↓]] (bottom row) is a simple way to compensate for color vision deficiencies.

</div>

</div>

</div>
One practical point defined by the [http://jfly.iam.u-tokyo.ac.jp/color/ Color Universal Design] is the use of magenta in red--green overlays (''see also'' <span class="bibcites">[[[#biblio-97|<span class="bib-index">47</span>]]]</span>). Magenta is the equal mixture of red and blue. Colorblind people that have difficulties recognizing the red component can easily recognize the blue hue. The region of double positive becomes white, which is easily distinguishable for colorblind. In ImageJ this is easily accomplished using the <span class="menuitem">Image ▷ Color ▷ [[#sub:Merge-Channels...|<span class="menuitem">Merge Channels…</span>↓]]</span>, or using the ImageJ macro language (''see'' [[#infobox:Replacing-Red-w-Magenta|5↓]] [[#infobox:Replacing-Red-w-Magenta|Replacing Red with Magenta in RGB Images↓]]).
<div class="float">

[[|]]
<div class="infobox">

<div class="caption">

float-infobox5 Replacing Red with Magenta in RGB Images

</div>
When building RGB images, magenta can be obtained using the <span class="menuitem">Image ▷ Color ▷ [[#sub:Merge-Channels...|<span class="menuitem">Merge Channels…</span>↓]]</span> Previously created RGB images can be converted to [[#index-Magenta-Green-Blue-(MGB)|↓]]‘MGB’ using <span class="menuitem">Image ▷ Color ▷ [[#sub:Channels...%5BZ%5D|Channels Tool… [Z]↓]]</span>. Alternatively, the <span class="sans"><span class="menuitem"><span class="sans">Process ▷ [[#sub:Image-Calculator...|Image Calculator…↓]]</span></span></span> command can be used to add the red channel to the blue channel. Both these approaches can be automated using the ImageJ macro language as exemplified by Macros [[#lis:RGBtoMGB1|(11↓)]] and [[#lis:RGBtoMGB2|(7↓)]]. Once saved in the <span class="Directory">ImageJ/plugins/</span> folder these [[#sub:Macros-ExtendingIJ|Macros↓]] are treated as regular ImageJ commands.
<div class="medskip">



</div>
<div class="PlainVisible">

In [[#sub:Fiji-intro|Fiji↑]], as expected, the procedure of modifying RGB images is simpler: one just needs to run <span class="sans"><span class="menuitem"><span class="sans">Image ▷ Color ▷ Replace Red with Magenta</span></span></span>. For even more convenience, Fiji provides an analogous command that replaces the system clipboard’s image with a magenta-green one.

</div>

</div>

</div>

It is also possible to simulate color blindness using the [http://www.vischeck.com/downloads/ Vischeck] or [http://www.dentistry.bham.ac.uk/landinig/software/dichromacy/dichromacy.html Dichromacy] plugins<span class="FootOuter"><span class="SupFootMarker"> [G] </span><span class="HoverFoot"><span class="SupFootMarker"> [G] </span>One advantage of Dichromacy over the Vischeck plugin is that it can be recorded and called from scripts and macros, without user interaction.</span></span>, or in [[#index-Fiji|↓]][[#sub:Fiji-intro|Fiji↑]], using the <span class="menuitem">Image ▷ Color ▷ Simulate Color Blindness</span> command.
<div class="listing">

<div class="caption">

[[|]]Replace Red with Magenta.ijm (Using <span class="menuitem">Process ▷ Image Calculator…</span>)

</div>
<pre class="listing"> /* This macro replaces Red with Magenta in RGB images using Process&gt;Image Calculator...  command. */
   if (bitDepth!=24)
       exit(&quot;This macro requires an RGB image&quot;);
 setBatchMode(true);
   title= getTitle();
   r= title+&quot; (red)&quot;; g= title+&quot; (green)&quot;; b= title+&quot; (blue)&quot;;
   run(&quot;Split Channels&quot;);
   imageCalculator(&quot;Add&quot;, b, r);
   run(&quot;Merge Channels...&quot;, &quot;red=&amp;r green=&amp;g blue=&amp;b&quot;);
   rename(title + &quot; (MGB)&quot;);
 setBatchMode(false);</pre>

</div>

===Color Composite Images===

In a [[#index-Color-Composites|↓]]composite image colors are handled through channels. The advantages with this type of image over plain RGB images are:

# Each channel is kept separate from the others and can be turned on and off using the ‘Channels’ tool (<span class="sans"><span class="menuitem"><span class="sans">Image ▷ Color ▷ [[#sub:Channels...%5BZ%5D|Channels Tool… [Z]↓]]</span></span></span>). This feature allows, e.g., to perform measurements on a specific channel while visualizing multiple.
# Channels can be 8, 16 or 32--bit and can be displayed with any lookup table
# More than 3 channels can be merged or kept separate

<div class="listing">

<div class="caption">

[[|]]Replace Red with Magenta.ijm (Using <span class="menuitem">Image ▷ Color ▷ Channels…</span>)

</div>
<pre class="listing"> /* This macro replaces Red with Magenta in RGB images using the Image&gt;Color&gt;Channels... tool. */
   if (bitDepth!=24)         // Ignore non-RGB images
       exit(&quot;This macro requires an RGB image&quot;);
 setBatchMode(true);         // Enter ‘Batch’ mode
   title = getTitle();       // Retrieve the image title
   run(&quot;Make Composite&quot;);    // Run Image&gt;Color&gt;Make Composite
   run(&quot;Magenta&quot;);           // Run Image&gt;Lookup Tables&gt;Magenta on channel 1
   run(&quot;RGB Color&quot;);         // Run Image&gt;Type&gt;RGB Color
   rename(title + &quot; (MGB)&quot;); // Rename the image
 setBatchMode(false);        // Restore ‘GUI’ mode</pre>

</div>

==Selections==

Selections (regions of interest, ROIs[[#nom-roi|↓]]), are typically created using the [[#sub:Toolbar|Toolbar↓]] [[#sec:IJ-Tools|Tools↓]]. Although ImageJ can display simultaneously several [[#index-Selection|↓]][[#index-ROI|↓]]ROIs (see [[#sub:Overlay-Intro|Overlays↓]] and [[#fig:The-ROI-Manager|ROI Manager↓]]) only one selection can be active at a time. Selections can be measured (<span class="sans"><span class="menuitem"><span class="sans">Analyze ▷ </span>[[#sub:Measure...%5Bm%5D|]]</span></span>
<div class="PlainVisible">

<span class="menuitem"></span>
<div class="PlainVisible">

Measure… [m]

</div>

</div>
↓), drawn (<span class="menuitem"><span class="sans">Edit ▷ </span>[[#sub:Draw-%5Bd%5D|Draw [d]↓]]</span>), filled (<span class="sans"><span class="menuitem"><span class="sans">Edit ▷ </span>[[#sub:Fill-%5Bf%5D|Fill [f]↓]]</span></span>) or filtered (<span class="menuitem"><span class="sans">Process ▷ </span>[[#sub:Filters|<span class="menuitem">Filters ▷ </span>↓]]</span> submenu), in the case of area selections. In addition it is also possible to hold multiple ROIs as non-destructive [[#sub:Overlay-Intro|Overlays↓]].

Selections can be initially outlined in one of the nine ImageJ default colors (''Red'', ''Green'', ''Blue'', ''Magenta'', ''Cyan'', ''Yellow'', ''Orange'', ''Black'' and White). Once created, selections can be contoured or painted with any other color using<span class="sans"> <span class="menuitem"><span class="sans">Edit ▷ Selection ▷ </span>[[#sub:Properties...|]]</span></span>
<div class="PlainVisible">

<span class="menuitem"></span>
<div class="PlainVisible">

Properties… [y]

</div>

</div>
↓. Selection Color can be changed in <span class="menuitem"><span class="sans">Edit ▷ Options ▷ </span>[[#sub:Colors...|Colors…↓]]</span>, by double clicking on the [[#sec:Point-Tool|Point Tool↓]], or using hot keys (''see'' [[#lis:ChangeSelectionColor|(27.13.9↓)]] [[#lis:ChangeSelectionColor|Colors…↓]]). It is highlighted in the center of the [[#sec:Point-Tool|Point Tool↓]] and [[#sec:Multi-point-Tool|Multi-point Tool↓]].
<div class="float">

[[|]]
<div class="figure" style="max-width: 88%;">

[[File:images/Selections.png|class=figure|figure images/Selections.png]]
<div class="caption">

Figure 5 '''Three types of area selections In ImageJ.''' Notice the cursor changes: to an ''arrow'' when it is within the selection, to a ''cross-hair'' when outside the selection, to a ''hand'' when over a selection vertex or ‘handler’. Notice also the filled handler in the polygon selection and the absence of point handlers in [[#sub:Composite-selections|Composite Selections↓]]. [[#sub:Overlay-Intro|Overlays↓]], i.e., non-active selections displayed in the non-destructive image overlay, are also displayed without handlers.

</div>

</div>

</div>

===Manipulating ROIs===

Most of commands that can be useful in defining or drawing selections are available in the <span class="sans"><span class="menuitem"><span class="sans">Edit ▷ </span>[[#sub:SelectionSubMenu|<span class="menuitem">Selection ▷ </span>↓]]</span></span> submenu and summarized in [[#fig:ROI-manipulations|ROI manipulations↓]]. Listed below are the most frequent manipulations involving [[#index-ROI|↓]]selections:

<div class="Labeling">

'''Adjusting''' Area selections can be adjusted with the [[#sub:Brush-Selection-Tool|Brush Selection Tool↓]]. In addition, vertexes of selections created with the [[#sub:Polygon-Selection-Tool|Polygon Selection Too<span class="sans">l</span>↓]] and [[#sub:Segmented-Line-Selection|Segmented Line Selection Tool↓]] can be adjusted by Alt/Shift-clicking.

</div>
<div class="Labeling">

'''Deleting''' Choose any of the selection tools and click outside the selection, or use <span class="sans"><span class="menuitem"><span class="sans">Edit ▷ Selection ▷ </span>[[#sub:Select-None-%5BA%5D|Select None [A]↓]]</span></span>. Use<span class="sans"> <span class="menuitem"><span class="sans">Edit ▷ Selection ▷ </span>[[#sub:Restore-Selection-%5BE%5D|Restore Selection [E]↓]]</span></span> to restore a selection back after having deleted it. With [[#sub:Overlay-Intro|Overlays↓]], an activated ROI can be deleted by pressing the <span class="Keystroke">Backspace</span> (<span class="Keystroke">Delete</span> on Mac) key.

</div>
<div class="Labeling">

'''Managing''' A selection can be transferred from one image window to another by activating the destination window and runnig <span class="sans"><span class="menuitem"><span class="sans">Edit ▷ Selection ▷ </span>[[#sub:Restore-Selection-%5BE%5D|Restore Selection [E]↓]]</span></span>. Alternatively, <span class="sans"><span class="menuitem"><span class="sans">Analyze ▷ Tools ▷ </span>[[#sub:SynchronizeWindows|<span class="menuitem">Synchronize Windows</span>↓]]</span></span> to create ROIs across multiple images. Multiple selections can be stored as [[#sub:Overlay-Intro|Overlays↓]] or in the [[#fig:The-ROI-Manager|ROI Manager↓]] list (<span class="sans"><span class="menuitem"><span class="sans">Analyze ▷ Tools ▷ </span>[[#sub:ROI-Manager...|<span class="menuitem">ROI Manager…</span>↓]]</span></span>).

</div>
<div class="Labeling">

'''Moving''' Selections can be moved by clicking and dragging as long as the cursor is within the selection and has changed to an [[File:images/pointers/Pointer-Arrow.png|class=embedded|figure images/pointers/Pointer-Arrow.png]] . The status bar displays the coordinates of the upper left corner of the selection (or the bounding rectangle for non-rectangular selections) as it is being moved. To move the contents of a selection, rather than the selection itself, <span class="sans"><span class="menuitem"><span class="sans">Edit ▷ [[#sub:Copy%5Bc%5D|Copy [c]↓]]</span></span></span>, <span class="sans"><span class="menuitem"><span class="sans">Edit ▷ [[#sub:Paste%5Bv%5D|Paste [v]↓]]</span></span></span>, and then click within the selection and drag.

</div>
<div class="Labeling">

'''Nudging''' Selections can be ‘nudged’ one pixel at a time in any direction using the arrow keys. Note that the up and down keys zoom the image in and out in the absence of selections (''see'' [[#Arrow-Keys|Arrow Keys↓]] shortcuts).

</div>
<div class="Labeling">

'''Resizing''' The [[#sub:Brush-Selection-Tool|Brush Selection Tool↓]] can be used to perform fine adjustments of ROI contours. Most ROIs can be resized one pixel at a time by holding <span class="Keystroke">Alt</span> while using the arrow keys. In general (''see'' [[#sec:Area-selection-tools|Area Selection Tools↓]] and [[#sec:Line-Selection-Tools|Line Selection Tools↓]] for details), selections are resized by dragging one of the selection handlers. While dragging, holding <span class="Keystroke">Ctrl</span> resizes the selection around its center, holding <span class="Keystroke">Alt</span> imposes a fixed aspect ratio and holding <span class="Keystroke">Shift</span> forces a 1:1 aspect ratio.

<div class="See">

[[#sec:Key-Modifiers|Key Modifiers↓]]

</div>
===Composite Selections===

<div class="wrap-l">

<div class="figure">

[[File:images/compositeROI.png|class=embedded|figure images/compositeROI.png]]

</div>

</div>
Composite selections are non-contiguous ROIs containing more than one cluster of pixels and/or ROIs containing internal holes. Composite ROIs are typically originated with the [[#sub:Brush-Selection-Tool|Brush Selection Tool↓]] but they can be defined with any other selection tool using key modifiers.

The following modifier keys can be use to create composite selections:[[#index-Selection-Composite|↓]]

<div class="Labeling">

<span class="Keystroke">Shift</span> Drawing outside current selection while pressing Shift creates new content. To add a non-square rectangle or ellipse, the Shift key must be released after adding the selection

</div>
<div class="Labeling">

<span class="Keystroke">Alt</span> Drawing inside current selection while pressing Alt creates a hole removing content from the ROI

</div>
Note that some operations may not be performed properly on complex ROIs. In these cases, it may be useful to convert a composite ROI into a polygon using the <span class="menuitem">Edit ▷ Selection ▷ [[#sub:Enlarge...|Enlarge…↓]]</span> command as explained in [[#infobox:Composites|14↓]] [[#infobox:Composites|Converting Composite Selections↓]].

<div class="See">

[[#sub:Wand-Tool|Wand Tool↓]], [http://imagejdocu.tudor.lu/doku.php?id=wishlist:completed:freehand_and_selection_brush_roi_conversion ROI2PolylineROI] macro

</div>
===Selections With Sub-pixel Coordinates[[#index-Sub-pixel-selections|↓]]<span class="unknown">\feature</span>Selections with sub-pixel resolution===

Since ImageJ 1.46, selections can be defined with [http://en.wikipedia.org/wiki/Sub-pixel_resolution subpixel accuracy], beyond the nominal pixel resolution of the image: [[#fig:Subpixel-selections|Floating point selections↓]]. Line Selections (''see'' [[#sec:Line-Selection-Tools|Line Selection Tools↓]]) are created with floating-point coordinates if the ''Sub-pixel resolution'' checkbox is active in <span class="menuitem">Edit ▷ Options ▷ [[#sub:Profile-Plot-Options...|<span class="menuitem">Profile Plot Options…</span>↓]]</span> Sub-pixel coordinates of pre-existing selections can be interpolated using the <span class="menuitem">Edit ▷ Selection ▷ [[#sub:Interpolate|<span class="menuitem">Interpolate</span>↓]]</span> command. Interpolated points are easily noticeable on small selections created on images zoomed 1200% or greater.
<div class="float">

[[|]]
<div class="figure">

[[File:images/SubPixel.png|class=embedded|figure images/SubPixel.png]]
<div class="caption">

Figure 7 '''Interpolated selections.''' ROIs drawn with (left) or without (middle) sub-pixel accuracy. For line selections (''see'' [[#sec:Line-Selection-Tools|Line Selection Tools↓]]), this option can be enabled in '''''' <span class="menuitem">Edit ▷ Options ▷ [[#sub:Profile-Plot-Options...|<span class="menuitem">Profile Plot Options…</span>↓]]</span> by activating the ''Sub-pixel resolution'' checkbox. Pixel coordinates of area selections (''see'' [[#sec:Area-selection-tools|Area Selection Tools↓]]), can be interpolated using <span class="menuitem">Edit ▷ Selection ▷ [[#sub:Interpolate|<span class="menuitem">Interpolate</span>↓]]</span>. The image on the right is the output of <span class="Filename">[http://imagej.nih.gov/ij/macros/js/SubPixelSelections.js SubPixelSelections.js]</span>, a script that demonstrates how to create selections at sub-pixel resolution without the need of setting any option in ImageJ.

</div>

</div>

</div>

<div class="See">

[[#sub:Zoom|Zoom ▷ ↓]], [[#sec:Magnifying-Glass|Magnifying Glass↓]]

</div>
==Overlays[[|]]<span class="unknown">\improvement</span>Improved handling of Overlays==

[[#index-Overlay|↓]][[#index-Non-destructive-annotations|↓]][[#index-Annotations-Non-destructive-image-overlay|↓]]Overlays are non-active selections displayed ‘over’ the pixel data, on the image overlay, and are the core of non-destructive image processing in ImageJ. In a way you can think of the image overlay as an invisible [[#fig:The-ROI-Manager|ROI Manager↓]] in which selections are being added, allowing ROIs to be on ‘hold’. This concept of multiple distinct selections has been dramatically improved in [[#sub:ImageJ2intro|ImageJ2↑]] so we urge you to download IJ2 if multiple ROIs are important in your workflows.
<div class="float">

[[|]]
<div class="figure" style="max-width: 75%;">

[[File:images/OverlayShowcase.png|class=figure|figure images/OverlayShowcase.png]]
<div class="caption">

Figure 8 '''Non-destructive operations using the image overlay.''' Overlays can be used to annotate images, store ROIs and blend images (ImageROIs) at multiple opacity levels. Refer to the <span class="menuitem">Image ▷ [[#sub:Overlay|Overlay ▷ ↓]]</span>documentation for further [[#fig:image-overlays|examples↓]]. You can [http://imagej.nih.gov/ij/docs/guide/images/ImageWithOverlay.tif download the frontmost] image to practice overlay editing.

</div>

</div>

</div>

Importantly, overlay selections are [http://en.wikipedia.org/wiki/Vector_graphics vector graphics] composed of mathematically-defined paths (as opposed to [http://en.wikipedia.org/wiki/Raster_graphics raster graphics] in which objects are defined by pixels) and are not affected by scaling, i.e., do not become pixelated. Most of overlay-related commands are listed in the <span class="menuitem">Image ▷ [[#sub:Overlay|Overlay ▷ ↓]]</span>, and in the ROI Manager window (<span class="menuitem">Analyze ▷ Tools ▷ [[#sub:ROI-Manager...|<span class="menuitem">ROI Manager…</span>↓]]</span>). Appearance of overlay selections can be adjusted using <span class="menuitem">Image ▷ Overlay ▷ [[#sub:Overlay-Options...|<span class="menuitem">Overlay Options…</span>↓]]</span>/<span class="menuitem">[[#sub:Labels...|<span class="menuitem">Labels…</span>↓]]</span>

As mentioned in [[#infobox:Formats|3↑]] [[#infobox:Formats|Image Types: Lossy Compression and Metadata↑]], overlays are saved in the header of tif images, and do not need to be saved externally when using TIFF, the default file format of ImageJ. The major advantages of overlays are summarized below:

<div class="Description">

<span class="Description-entry">Storage of ROIs</span> In ImageJ it is only possible to have a single ROI at a time. However, it is possible to add selections to the image overlay using <span class="Keystroke">B</span> (<span class="menuitem">Image ▷ Overlay ▷ [[#sub:Add-Selection...%5Bb%5D|]]</span>
<div class="PlainVisible">

<span class="menuitem"></span>
<div class="PlainVisible">

Add Selection… [b]

</div>

</div>
↓).<span class="unknown">\feature</span> Once added to the image overlay, ROIs can be re-activated by Alt-clicking, Control-clicking or long-pressing (<span class="formula"><span class="fraction"><sup>1</sup>⁄<sub>4</sub></span></span> second or longer). Activated ROIs can be deleted by pressing the <span class="Keystroke">Backspace</span> key. Selections can also be added and recovered in bulk, using the <span class="menuitem">Image ▷ Overlay ▷ [[#sub:From-ROI-Manager|From ROI Manager↓]]</span>/<span class="menuitem">[[#sub:To-ROI-Manager|To ROI Manager↓]]</span> commands.

</div>
<div class="Description">

<span class="Description-entry">Non-destructive annotations</span> Overlays are the best way of annotating images in ImageJ ([[#fig:image-overlays|examples↓]]). As vector graphics, overlays do not change pixel values, can be scaled without loss of quality even at high zoom levels (''see'' [[#infobox:ZoomedCanvas|19↓]] [[#infobox:ZoomedCanvas|Working with Zoomed Canvases↓]]) and can be displayed at different opacity values (''see'' [[#infobox:HEX|20↓]] [[#infobox:HEX|Hexadecimal Color Values↓]]). RGB snapshots of the image with embedded overlays can be created by holding <span class="Keystroke">Shif</span> <span class="Keystroke">F</span>, the shortcut for <span class="menuitem">Image ▷ Overlay ▷ [[#sub:Flatten-%5BF%5D|Flatten [F]↓]]</span>. ‘Flattened’ images with the overlay rendered as pixel data are also created when saving the image as PNG or JPEG (<span class="menuitem">File ▷ [[#sub:SaveAs|Save As ▷ ↓]]</span>), or when printing the image canvas (<span class="menuitem">File ▷ [[#sub:Print...%5Bp%5D|Print… [p]↓]]</span>). The <span class="menuitem">Flatten</span> command is also listed in the [[#fig:The-ROI-Manager|ROI Manager↓]].

</div>
<div class="Description">

<span class="Description-entry">Image ROIs</span> An [[#index-Image-selection|↓]][[#index-ImageROI|↓]]imageROI (image selection) is a ROI that displays an image as an overlay. As described in <span class="menuitem">Edit ▷ Selection ▷ [[#sub:Image-to-Selection...|<span class="menuitem">Image to Selection…</span>↓]]</span> and <span class="menuitem">Image ▷ Overlay ▷ [[#sub:Add-Image...|<span class="menuitem">Add Image…</span>↓]]</span>, this allows multiple images to be [[#index-Blend|↓]]blended on a single image canvas.

</div>
==3D Volumes==

Currently, the support for [[#index-ThreeD-ROIs_3D-ROIs|↓]][[#index-3D-ROIs|↓]]3D ROIs (selections containing contiguous cluster of voxels) is somewhat limited in ImageJ. This limitation has been addressed by [[#sub:ImageJ2intro|ImageJ2↑]] and several IJ1 plugins. The list below summarizes some of the ImageJ plugins that deal effectively with multi-dimensional objects. Note that a manual installation of these tools as standalone ImageJ plugins is a challenging task given their special dependencies, reason why they are all bundled as part of [[#index-Fiji|↓]][[#sub:Fiji-intro|Fiji↑]].
<div class="float">

[[|]]
<div class="figure" style="max-width: 70%;">

[[File:images/3Dviewer.png|class=figure|figure images/3Dviewer.png]]
<div class="caption">

Figure 9 '''3D Viewer (Fiji 1.46o), bringing hardware-accelerated 3D visualization to ImageJ.''' As explained in [[#sub:3D-Intro|3D Volumes↑]], most of plugins that truly extend ImageJ functionally to multi-dimentional data are bundled as part of Fiji.

</div>

</div>

</div>

<div class="Description">

<span class="Description-entry">3D Filters</span> Specialized [[#index-ThreeD-Filters_3D-Filters|↓]][[#index-3D-Filters|↓]]3D filters such as <span class="menuitem">Process ▷ Filters ▷ [[#sub:Gaussian-Blur-3D...|<span class="menuitem">Gaussian Blur 3D…</span>↓]]</span> can be installed to perform 3D operations. Examples are the [http://imagejdocu.tudor.lu/doku.php?id=plugin:morphology:3d_binary_morphological_filters:start 3D processing package] by Thomas Boudier <span class="bibcites">[[[#biblio-84|<span class="bib-index">34</span>]]]</span> and the [https://fiji.sc/wiki/index.php/3D_Binary_Filters 3D binary filters] by Benjamin Schmid.

</div>
<div class="Description">

<span class="Description-entry">3D Object Counter</span> [http://imagejdocu.tudor.lu/doku.php?id=plugin:analysis:3d_object_counter:start 3D Object Counter] (3D-OC) [[#index-ThreeD-Object-Counter_3D-Object-Counter|↓]][[#index-3D-Object-Counter|↓]]counts and qualifies 3D objects in a stack <span class="bibcites">[[[#biblio-147|<span class="bib-index">97</span>]]]</span>, similarly to the 2D analysis performed by <span class="menuitem">Analyze ▷ [[#sub:Analyze-Particles...|Analyze Particles…↓]]</span> It is complemented by [http://imagejdocu.tudor.lu/doku.php?id=plugin:stacks:3d_roi_manager:start 3D Roi Manager] <span class="bibcites">[[[#biblio-84|<span class="bib-index">34</span>]]]</span>, a companion plugin that adds a 3D [[#fig:The-ROI-Manager|ROI Manager↓]] to ImageJ

</div>
<div class="Description">

<span class="Description-entry">3D Viewer</span> [http://3dviewer.neurofly.de/ 3D Viewer] [[#index-ThreeD-Viewer_3D-Viewer|↓]][[#index-3D-Viewer|↓]]brings powerful hardware-accelerated 3D visualization to ImageJ <span class="bibcites">[[[#biblio-65|<span class="bib-index">15</span>]]]</span>, extending the limited functionality of <span class="menuitem">Image ▷ Stacks ▷ [[#sub:3D-Project...|<span class="menuitem">3D Project…</span>↓]]</span> In the ImageJ [[#fig:-3D-Viewer|3D Viewer↑]] stacks can be displayed as texture-based volume renderings, surfaces or orthoslices. It is macro-recordable and can be used by other plugins as a high-level programming library for 3D visualization

</div>
<div class="Description">

<span class="Description-entry">Simple Neurite Tracer</span> [https://fiji.sc/wiki/index.php/Simple_Neurite_Tracer Simple Neurite Tracer] [[#index-Simple-Neurite-Tracer|↓]]allows semi-automated segmentation of tubular structures in 3D <span class="bibcites">[[[#biblio-128|<span class="bib-index">78</span>]]]</span>

</div>
<div class="Description">

<span class="Description-entry">TrakEM2</span> As mentioned earlier, [[#misc:TrakEM2|Software Packages Built on Top of ImageJ↑]] features powerful tools for multi-dimensional regions of interest <span class="bibcites">[[[#biblio-57|<span class="bib-index">7</span>]]]</span>

</div>
<div class="See">

<span class="menuitem">Image ▷ Stacks ▷ [[#sub:3D-Project...|<span class="menuitem">3D Project…</span>↓]]</span>/<span class="menuitem">[[#sub:Orthogonal-Views|Orthogonal Views [H]↓]]</span>, <span class="menuitem">Analyze ▷ [[#sub:Surface-Plot...|Surface Plot…↓]]</span>, [[#infobox:Skeletonize-vs-Skeletonize3D|22↓]] [[#infobox:Skeletonize-vs-Skeletonize3D|Skeletonize vs Skeletonize 3D↓]], [https://fiji.sc/wiki/index.php/Special:Search?search=3d&fulltext=Search 3D tools in Fiji], [http://www.longair.net/edinburgh/imagej/three-pane-crop/ Three Pane Crop], [http://imagejdocu.tudor.lu/doku.php?id=tutorial:working:3d_image_processing_and_analysis_with_imagej 3D image processing tutorials] on the ImageJ wikipage

</div>
==Settings and Preferences[[|]]<span class="unknown">\improvement</span>==

[[#index-Settings|↓]][[#index-Preferences|↓]][[#index-Options|↓]]ImageJ preferences are automatically saved in a preferences file, the<code> </code><span class="Filename">IJ_prefs.txt</span> text file. This file is stored in <span class="Directory"><span class="formula"> ~ </span>/Library/Preferences/</span> on Mac OS X, in <span class="Directory"><span class="formula"> ~ </span>/.imagej/</span> on Linux and Windows (with <span class="formula"> ~ </span> referring to the user’s home directory). Several macros and plugins also write parameters to this file. If the <span class="Filename">IJ_prefs.txt</span> is erased using <span class="menuitem">Edit ▷ Options ▷ [[#sub:ResetOptions|<span class="menuitem">Reset…</span>↓]]</span>, ImageJ will create a new one the next time it is opened resetting all parameters to their default values.

Sometimes, it may be useful to override (or restore) certain settings that may have been changed during a working session. For example, the ''Limit to threshold'' option (<span class="menuitem"><span class="sans">Analyze ▷ </span>[[#sub:Set-Measurements...|<span class="menuitem">Set Measurements…</span>↓]]</span>) will affect most measurements performed on thresholded images. Thus, it may be wise to check the status of this parameter before each analysis, specially when working on multiple computers.

<div class="listing">

<div class="caption">

[[|]]Ensuring Specific Settings at Launch

</div>
<pre class="listing"> macro &quot;AutoRun&quot; {
   setOption(&quot;DebugMode&quot;, true);
   setOption(&quot;Bicubic&quot;, true);
   setOption(&quot;Display Label&quot;, true);
   setOption(&quot;Limit to Threshold&quot;, false);
   setOption(&quot;BlackBackground&quot;, true);
   run(&quot;Colors...&quot;, &quot;foreground=white background=black&quot;); //this line could be substituted by: setBackgroundColor(0,0,0); setForegroundColor(255,255,255);
   run(&quot;Profile Plot Options...&quot;, &quot;width=350 height=200 draw&quot;);
   run(&quot;Brightness/Contrast...&quot;);
 }</pre>

</div>
The <code>setOption()</code> [http://imagej.nih.gov/ij/developer/macro/functions.html#setOption macro function] can be used to set this and several other ImageJ options. Calling this function from the [[#index-StartupMacros|↓]][[#index-AutoRun|↓]]“AutoRun” macro in the <span class="Filename">StartupMacros.txt</span> file ensures preferences are set each time ImageJ starts. The macro [[#lis:setOption|(13↑)]] [[#lis:setOption|Settings and Preferences↑]] exemplifies this approach ensuring that the following settings are enforced at startup:

# TIFF tag values are displayed by ImageJ (''Debug Mode'' in <span class="sans"><span class="menuitem"><span class="sans">Edit ▷ Options ▷ </span>[[#sub:Misc...|Misc…↓]]</span></span>)
# Bicubic interpolation is preferred over bilinear (e.g.,<span class="sans"> </span><span class="menuitem"><span class="sans">Edit ▷ Selection ▷ </span>[[#sub:Straighten...|Straighten…↓]]</span>)
# The name of the measured image name is recorded in the first column of the [[#sec:Results-Table|Results Table↓]] (''Display Label'' in <span class="menuitem"><span class="sans">Analyze ▷ </span>[[#sub:Set-Measurements...|<span class="menuitem">Set Measurements…</span>↓]]</span>)
# Measurements are not restricted to thresholded pixels (''Limit to Threshold'' in <span class="menuitem"><span class="sans">Analyze ▷ </span>[[#sub:Set-Measurements...|<span class="menuitem">Set Measurements…</span>↓]]</span>)
# Binary images are processed assuming white objects on a black background (''Black background'' in <span class="menuitem"><span class="sans">Process ▷ Binary ▷ </span>[[#sub:BinaryOptions...|<span class="menuitem">Options…</span>↓]]</span>, ''see'' [[#infobox:blackBackground|23↓]] [[#infobox:blackBackground|Interpreting Binary Images↓]])
# ''Background color'' is black and ''foreground color'' is white (<span class="sans"><span class="menuitem"><span class="sans">Edit ▷ Options ▷ </span>[[#sub:Colors...|Colors…↓]]</span></span>)
# ImageJ plots contain grid lines and are always <span class="formula">350 × 200</span> pixels in size (<span class="sans"><span class="menuitem"><span class="sans">Edit ▷ Options ▷ </span>[[#sub:Profile-Plot-Options...|<span class="menuitem">Profile Plot Options…</span>↓]]</span></span>)
# Open the B&amp;C widget at its last saved screen position (<span class="sans"><span class="menuitem"><span class="sans">Image ▷ Adjust ▷ </span>[[#sub:Brightness/Contrast...%5BC%5D|Brightness/Contrast… [C]↓]]</span></span>)

<div class="See">

[[#sec:GUIcustomization|Customizing the ImageJ Interface↓]], FAQs[[#nom-faq|↓]] on [http://imagejdocu.tudor.lu/doku.php?id=faq:technical:how_do_i_set_up_imagej_to_deal_with_white_particles_on_a_black_background_by_default ImageJ wikipage], [[#infobox:Organizing-Commands|8↓]] [[#infobox:Organizing-Commands|Organizing Commands in the Menu Bar↓]]

</div>
