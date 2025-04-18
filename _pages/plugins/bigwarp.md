---
title: BigWarp
project: /software/fiji
categories: [Visualization,Transform,Registration]
artifact: sc.fiji:bigwarp_fiji
extensions: ["mathjax"]
doi: 10.1109/ISBI.2016.7493463
---

BigWarp is a tool for manual, interactive, landmark-based deformable image
alignment. It uses the [BigDataViewer](/plugins/bdv) for visualization and
navigation, and uses a
{% include wikipedia title='Thin plate spline' text='Thin Plate Spline' %}
implemented
{% include github org='saalfeldlab' repo='bigwarp' label='in Java' %} to
build a deformation from point correspondences.

The interface enables landmark pair placement and displays the effects of
the warp on-the-fly.

## Installation

BigWarp comes with Fiji. You can access it via {% include bc path="Plugins | BigDataViewer | Big Warp Command" %} 
for the newer startup dialog, or {% include bc path="Plugins | BigDataViewer | Big Warp" %} 
for the legacy dialog. If this is not visible in your installation, try updating Fiji with
{% include bc path="Help | Update..." %}.

## Starting BigWarp

### `Big Warp Command`

{::nomarkdown}
<table>
  <tbody>
    <tr>
        <td style="padding: 5px;"> <img src="/media/plugins/bigwarp/bigwarp-init-dialog.png" width="500"/> </td>
        <td style="padding: 5px;">
            <ul>
            <li><b>BigWarp project or landmarks</b> : Select a saved BigWarp project file (json) or landmarks file (csv).</li>
            <li><b>Add open image</b>: Select an image open in ImageJ to add to BigWarp. Click the {% include button label='+' %} button to add the selected image to the table.</li> 
            <li><b>Add image file/folder</b>: Select an file or folder. Click the {% include button label='+' %} button to add the selected image to the table.
                You can {% include button label='Browse' %} your file system, or explore {% include button label='H5/N5/Zarr' %} containers.</li>
            <li><b>Add transformation</b>: Select a transformation. Click the {% include button label='+' %} to add the selected transformation to the currrently selected row of the table.
                You can {% include button label='Browse' %} your file system, or explore {% include button label='H5/N5/Zarr' %} containers.</li>
            </ul>
        </td>
    </tr>
  </tbody>
</table>
{:/}

Selected images are displayed in a table at the bottom of the dialog.  Indicate an image as
moving by checking the box in the "Moving" column.  Only *moving images* will be transformed by
BigWarp. Any number of images can be set as moving. Clicking {% include button label='remove' %}
will remove a row from the table.

BigWarp can also apply "external" transformations to images. These are shown in the *Transform*
column of the table. They can be added with the "Add transformation" option above, or by writing
a path or [N5URL](https://github.com/saalfeldlab/n5/wiki/URLs) directly into the table.

### `Big Warp`

{::nomarkdown}
<table>
  <tbody>
    <tr>
        <td style="padding: 5px;"> <img src="/media/plugins/bigwarp/bigwarp-dialog-legacy.png" width="250"/> </td>
        <td style="padding: 5px;">
            <ul>
            <li><b>moving image</b> : Select an image open in ImageJ to be transformed.</li>
            <li><b>target image</b>: Select an image open in ImageJ as a reference image. Will not be transformed.</li>
            <li><b>N5/Zarr/HDF5/BDV-XML</b>: The four options below let you selected chunked storage containers for moving and target images</li>
                <ul>
                    <li><b>Moving</b>: The root of of the storage container for the moving image (ususally ends with ".h5", ".n5", or ".zarr")</li>
                    <li><b>Moving dataset</b>: The path to the moving image relative to the root ("/" refers to the container root)</li>
                    <li><b>Target</b>: The root of of the storage container for the target image (ususally ends with ".h5", ".n5", or ".zarr")</li>
                    <li><b>Target dataset</b>: The path to the target image relative to the root ("/" refers to the container root)</li>
                </ul>
            <li><b>Landmarks file</b>: A csv file containing landmarks</li>
            <li><b>Apply transform from landmarks</b>: if selected and landmarks are provided, BigWarp will transform the moving image(s) on startup.</li>
            </ul>
        </td>
    </tr>
  </tbody>
</table>
{:/}

Note: The moving or target images open in ImageJ may be multi-channel. Chunked file formats let you open images that are too large for "traditional" ImageJ, or stream image data on the fly from cloud storage.

## Usage

Open two images in ImageJ, one *moving* and the other *target* and navigate to
{% include bc path="Plugins | BigDataViewer | Big Warp" %}. A dialog will
appear prompting selection of the moving and target images. 

Alternatively, save your images with
[N5](https://github.com/saalfeldlab/n5-ij),
[Zarr](https://zarr.readthedocs.io/en/stable/), or as a
[bigdataviewer-xml](/plugins/bdv#exporting-datasets-for-the-bigdataviewer),
and specify the paths to those images in the BigWarp dialog. See the section on
[working with large images](#working-with-large-images) below. 

Once the two image windows and one table window open, press
{% include key key='Spacebar' %} to enter "landmark mode". Next, click on a
point in the moving image, then click on the corresponding point in the target
image. After you have a few moving-target point pairs, press
{% include key key='T' %} to transform the moving image (you may need to
re-navigate if the two image are very far apart: see the
{% include key key='Q' %} and {% include key key='W' %} hotkeys below).

### Getting Help

Press {% include key key='F1' %} at any time to open a help page with a listing
of navigation and editing commands. For detailed help, create a post on the
[image.sc forum](https://forum.image.sc/) with a bigwarp tag. Report bugs
[on github](https://github.com/saalfeldlab/bigwarp/issues).

### Landmark point placement and display in the viewer

Landmark placements is done in *Landmark mode* which you enter by pressing
{% include key key='Spacebar' %}. Users place pairs of corresponding points on
the moving and target images.

The following table shows the available commands and keystrokes for landmark
placement, warping.

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td style="padding: 5px;">
        <p>{% include key key='T' %}</p>
      </td>
      <td style="padding: 5px;">
        <p>Toggle between warped view and raw view or moving image.</p>
      </td>
    </tr>
    <tr>
      <td style="padding: 5px;">
        <p>{% include key keys='Ctrl|O' %}</p>
      </td>
      <td style="padding: 5px;">
        <p>Open landmarks from saved file.</p>
      </td>
    </tr>
    <tr>
      <td style="padding: 5px;">
        <p>{% include key keys='Ctrl|S' %}</p>
      </td>
      <td style="padding: 5px;">
        <p>Save current landmarks to a file.</p>
      </td>
    </tr>
    <tr>
      <td style="padding: 5px;">
        <p>{% include key key='Spacebar' %}</p>
      </td>
      <td style="padding: 5px;">
        <p>Toggle <em>Landmark mode</em></p>
      </td>
    </tr>
    <tr>
      <td style="padding: 5px;">
        <p>&lt;<em>Landmark mode</em>&gt;+{% include key key='left-click' %}</p>
      </td>
      <td style="padding: 5px;">
        <p>Clicking while in landmark mode adds a landmark point or selects and existing landmark.</p>
      </td>
    </tr>
    <tr>
      <td style="padding: 5px;">
        <p>&lt;<em>Landmark mode</em>&gt;+{% include key keys='left-drag' %}</p>
      </td>
      <td style="padding: 5px;">
        <p>Clicking an existing point and dragging changes it's position.</p>
      </td>
    </tr>
    <tr>
      <td style="padding: 5px;">
        <p>&lt;<em>Landmark mode</em>&gt;+{% include key keys='Shift|left-drag' %}</p>
      </td>
      <td style="padding: 5px;">
        <p>"Move" a point. The initial click places a landmark point for the moving image. The release places a landmark point for the target image.</p>
      </td>
    </tr>
    <tr>
      <td style="padding: 5px;">
        <p>&lt;<em>Landmark mode</em>&gt;+{% include key keys='Ctrl|left-click' %}</p>
      </td>
      <td style="padding: 5px;">
        <p>"Pin" a point. Add a landmark at the same location for both moving and target images.</p>
      </td>
    </tr>
    <tr>
      <td style="padding: 5px;">
        <p>&lt;<em>Landmark mode</em>&gt;+{% include key keys='Ctrl|Shift|left-click' %}</p>
      </td>
      <td style="padding: 5px;">
        <p>Place a point in the "other" space. Place a moving landmark from the fixed window, and vice versa.</p>
      </td>
    </tr>
    <tr>
      <td style="padding: 5px;">
        <p>{% include key keys='Ctrl|Z' %}</p>
      </td>
      <td style="padding: 5px;">
        <p>Undo the last landmark point change.</p>
      </td>
    </tr>
    <tr>
      <td style="padding: 5px;">
        <p>{% include key keys='Ctrl|Y' %}</p>
      </td>
      <td style="padding: 5px;">
        <p>Redo the last landmark point change.</p>
      </td>
    </tr>
    <tr>
      <td style="padding: 5px;">
        <p>{% include key key='V' %}</p>
      </td>
      <td style="padding: 5px;">
        <p>Toggle point visibility in the viewer.</p>
      </td>
    </tr>
    <tr>
      <td style="padding: 5px;">
        <p>{% include key key='N' %}</p>
      </td>
      <td style="padding: 5px;">
        <p>Toggle point name visibility in the viewer.</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

### Landmark selection and editing in the table

Some changes to landmarks can be done by interacting with the landmark table.

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td style="padding: 5px;">
        <p>{% include key key='left-click' %}</p>
      </td>
      <td style="padding: 5px;">
        <p>Select row.</p>
      </td>
    </tr>
    <tr>
      <td style="padding: 5px;">
        <p>{% include key keys='Ctrl|left-click' %}</p>
      </td>
      <td style="padding: 5px;">
        <p>Add row to selection.</p>
      </td>
    </tr>
    <tr>
      <td style="padding: 5px;">
        <p>{% include key keys='Shift|left-click' %}</p>
      </td>
      <td style="padding: 5px;">
        <p>Select range of rows.</p>
      </td>
    </tr>
    <tr>
      <td style="padding: 5px;">
        <p>{% include key key='Esc' %}</p>
      </td>
      <td style="padding: 5px;">
        <p>Deselect all rows.</p>
      </td>
    </tr>
    <tr>
      <td style="padding: 5px;">
        <p>{% include key key='right-click' %} &rarr; Delete</p>
      </td>
      <td style="padding: 5px;">
        <p>Deletes a landmark pair (row in the table).</p>
      </td>
    </tr>
    <tr>
      <td style="padding: 5px;">
        <p>{% include key key='right-click' %} &rarr; Delete all selected</p>
      </td>
      <td style="padding: 5px;">
        <p>Deletes all selected landmark pairs (row in the table).</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

### Notes on point addition and landmark pair selection

-   Adding a new landmark pair selects that pair (row) in the table.
-   If a row is "missing" a moving (target) landmark point, then it must be selected in order to add that missing point by clicking in the moving (target) viewer. Then BigWarp will find the "next" row that is missing a moving (target) landmark, and select that row automatically.
-   If the selected row is not missing a landmark, the next click will add a new landmark pair.
-   If multiple rows are selected when a viewer is clicked, the result will be as though only the first row was selected.

### Selecting transformation types

Press {% include key key='F2' %} to bring up a transformation type selection window, or {% include key key='U' %} to open the BigWarp options dialog (versions 4.0.0 or later support multiple options for transformations).

|                                                |                                                   |
|------------------------------------------------|---------------------------------------------------|
| <img src="/media/plugins/bigwarp/bigwarp-selecttps.png" width="400"/> | <img src="/media/plugins/bigwarp/bigwarp-selectaffine.png" width="400"/> |
| Example of a thin plate spline transformation  | Example of an affine transformation               |

#### Table of transformation types

|                                               |                                                                                                                                               |
|-----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Thin Plate Spline | The smoothest deformable transformation that maps moving landmarks exactly to the corresponding target landmarks. |
| Affine            | Linear transform with translation, rotation, independent scales and shear (12 degrees of freedom)                 |
| Similarity        | Linear transform with translation, rotation, and one scale parameter (7 degrees of freedom)                       |
| Rotation          | Linear transform with translation, and rotation (6 degrees of freedom)                                            |
| Translation       | Translation only (3 degrees of freedom)                                                                           |

#### Masked transformations

It is sometimes useful to limit the transformation to a certain area, for example, when fine-tuning another transformation.
Options for masked transformations can be found in the BigWarp options dialog {% include bc path="Settings | BigWarp Options" %} 
or shortcut {% include key key='U' %}. (*Available in version 9.0.0 or later*)

Turn on a transformation mask by setting the "Mask interpolation option to one of `LINEAR`, `ROTATION`, or `SIMILARITY`.

{% include img name="spirals" src="/media/plugins/bigwarp/bigwarp-mask-1.png" width="500px" %} {% include img name="spirals" src="/media/plugins/bigwarp/bigwarp-mask-2.png" width="500px" %}

##### Details

* **Mask interpolation**
    * NONE : no masking
    * LINEAR : mask with "linear" interpolation
    * ROTATION : mask "rotation" interpolation
    * SIMILARITY : mask "similarity" interpolation

We generally recommend the `SIMILARITY` option when using a transform mask, though all options should give similar results in
most cases.

* **Mask falloff**: The shape of the falloff curve of the spherical mask from the center (where it equals one) to the outside where it equals zero. Not relevant for imported masks.
    * COSINE
    * GAUSSIAN
    * LINEAR 

* **Auto-estimate mask**: The size and position of the spherical mask will be automatically estimated as the smallest sphere
  that contains the clicked landmarks. Any manual edtis to the mask will turn this option off. Not relevant for imported masks.

* **Show mask overlay**: Overlays two circles on the fixed image window indicating mask size and position. Transformations are
  fully applied inside the inner circle, the transform is partly applied in between the two circles, and not at all applied
  outside the outer circle. Not relevant for imported masks.

It is also possible to import a mask from a file with {% include bc path="File | Import Mask" %}, or remove an imported mask
with {% include bc path="File | Remove Mask" %}. Masks should take values between zero and one, where a value of one indicates
the transform will be fully applied, a value of zero indicates the transform will not be applied, and partially applied for
values in between. For masks with an intensity range that is not $$[0,1]$$, use the *Imported mask intensity range* (see below) to
map its intensities as desired.

* **Imported mask intensity range**: Linearly map the intensity of an imported mask to $$[0,1]$$. The left (right) intensity will
  be mapped to zero (one). The Only relevant for imported masks.


### Navigation and Visualization

BigWarp inherits many image [navigation](/plugins/bdv#basic-navigation), [visualization](/plugins/bdv#adjusting-brightness-and-color), and [grouping](/plugins/bdv#grouping-sources) features with BigDataViewer, the details of which can be found on the [BigDataViewer](/plugins/bdv) page or on the help page. BigWarp specific features are documented below.

The following table shows the available navigation commands using the mouse:

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td style="padding: 5px;">
        <p>{% include key key='Q' %}</p>
      </td>
      <td style="padding: 5px;">
        <p>Align the non-active viewer with the active viewer.</p>
      </td>
    </tr>
    <tr>
      <td style="padding: 5px;">
        <p>{% include key key='W' %}</p>
      </td>
      <td style="padding: 5px;">
        <p>Align the active viewer with the non-active viewer.</p>
      </td>
    </tr>
    <tr>
      <td style="padding: 5px;">
        <p>{% include key key='E' %}</p>
      </td>
      <td style="padding: 5px;">
        <p>Centers the active viewer to the nearest landmark (considers 3D when applicable).</p>
      </td>
    </tr>
    <tr>
      <td style="padding: 5px;">
        <p>{% include key keys='Ctrl|D' %}</p>
      </td>
      <td style="padding: 5px;">
        <p>Centers the active viewer to the next landmark.</p>
      </td>
    </tr>
    <tr>
      <td style="padding: 5px;">
        <p>{% include key keys='Ctrl|Shift|D' %}</p>
      </td>
      <td style="padding: 5px;">
        <p>Centers the active viewer to the previous landmark.</p>
      </td>
    </tr>
    <tr>
      <td style="padding: 5px;">
        <p>{% include key key='R' %}</p>
      </td>
      <td style="padding: 5px;">
        <p>Resets the active viewer.</p>
      </td>
    </tr>
    <tr>
      <td style="padding: 5px;">
        <p>{% include key key='U' %}</p>
      </td>
      <td style="padding: 5px;">
        <p>Show warp visualization / grid dialog.</p>
      </td>
    </tr>
    <tr>
      <td style="padding: 5px;">
        <p>{% include key key='F3' %}</p>
      </td>
      <td style="padding: 5px;">
        <p>Show moving image panel Visibility & and Grouping dialog.</p>
      </td>
    </tr>
    <tr>
      <td style="padding: 5px;">
        <p>{% include key key='F4' %}</p>
      </td>
      <td style="padding: 5px;">
        <p>Show target image panel Visibility & and Grouping dialog.</p>
      </td>
    </tr>
    <tr>
      <td style="padding: 5px;">
        <p>{% include key keys='Ctrl|E' %}</p>
      </td>
      <td style="padding: 5px;">
        <p>Export moving image as an ImagePlus.</p>
      </td>
    </tr>
    <tr>
      <td style="padding: 5px;">
        <p>{% include key keys='Ctrl|Shift|E' %}</p>
      </td>
      <td style="padding: 5px;">
        <p>Export moving image as a Virtual ImagePlus.</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

### Commands shared with BigDataViewer

-   [Displaying multiple stacks ("sources")](/plugins/bdv#displaying-multiple-sources)
-   [Grouping sources](/plugins/bdv#grouping-sources)
-   [Adjusting brightness and color](/plugins/bdv#adjusting-brightness-and-color)
-   [Bookmarking views (locations and orientations)](/plugins/bdv#bookmarking-locations-and-orientations)

#### Mouse navigation

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td style="padding: 5px;">
        <p>{% include key keys='left-drag' %}</p>
      </td>
      <td style="padding: 5px;">
        <p>Rotate (pan and tilt) around the point where the mouse was clicked.</p>
      </td>
    </tr>
    <tr>
      <td style="padding: 5px;">
        <p>{% include key keys='right-drag' %} or {% include key keys='middle-drag' %}</p>
      </td>
      <td style="padding: 5px;">
        <p>Translate in the XY-plane.</p>
      </td>
    </tr>
    <tr>
      <td style="padding: 5px;">
        <p>{% include key key='mouse-wheel' %}</p>
      </td>
      <td style="padding: 5px;">
        <p>Move along the z-axis.</p>
      </td>
    </tr>
    <tr>
      <td style="padding: 5px;">
        <p>{% include key keys='Cmd|mouse-wheel' %} or {% include key keys='Shift|Ctrl|mouse-wheel' %}</p>
      </td>
      <td style="padding: 5px;">
        <p>Zoom in and out.</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

#### Keyboard navigation

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td style="padding: 5px;">
        <p>{% include key key='X' %}, {% include key key='Y' %}, {% include key key='Z' %}</p>
      </td>
      <td style="padding: 5px;">
        <p>Select keyboard rotation axis.</p>
      </td>
    </tr>
    <tr>
      <td style="padding: 5px;">
        <p>{% include key key='Left' %}, {% include key key='Right' %}</p>
      </td>
      <td style="padding: 5px;">
        <p>Rotate clockwise or counter-clockwise around the choosen rotation axis.</p>
      </td>
    </tr>
    <tr>
      <td style="padding: 5px;">
        <p>{% include key key='Up' %}, {% include key key='Down' %}</p>
      </td>
      <td style="padding: 5px;">
        <p>Zoom in or out.</p>
      </td>
    </tr>
    <tr>
      <td style="padding: 5px;">
        <p>{% include key key=',' %}, {% include key key='.' %}</p>
      </td>
      <td style="padding: 5px;">
        <p>Move forward or backward along the Z-axis.</p>
      </td>
    </tr>
    <tr>
      <td style="padding: 5px;">
        <p>{% include key keys='Shift|X' %}</p>
      </td>
      <td style="padding: 5px;">
        <p>Rotate to the ZY-plane of the current source. (Look along the X-axis of the current source.)</p>
      </td>
    </tr>
    <tr>
      <td style="padding: 5px;">
        <p>{% include key keys='Shift|Y' %} or {% include key keys='Shift|A' %}</p>
      </td>
      <td style="padding: 5px;">
        <p>Rotate to the XZ-plane of the current source. (Look along the Y-axis of the current source.)</p>
      </td>
    </tr>
    <tr>
      <td style="padding: 5px;">
        <p>{% include key keys='Shift|Z' %}</p>
      </td>
      <td style="padding: 5px;">
        <p>Rotate to the XY-plane of the current source. (Look along the Z-axis of the current source.)</p>
      </td>
    </tr>
    <tr>
      <td style="padding: 5px;">
        <p>{% include key key='[' %} or {% include key key='N' %}</p>
      </td>
      <td style="padding: 5px;">
        <p>Move to previous timepoint.</p>
      </td>
    </tr>
    <tr>
      <td style="padding: 5px;">
        <p>{% include key key=']' %} or {% include key key='M' %}</p>
      </td>
      <td style="padding: 5px;">
        <p>Move to next timepoint.</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

For all navigation commands you can hold {% include key key='Shift' %} to
rotate and browse 10x faster, or hold {% include key key='Ctrl' %} to rotate
and browse 10x slower. For example, {% include key key='Left' %} rotates by 1°
clockwise, while {% include key keys='Shift|Left' %} rotates by 10°, and
{% include key keys='Ctrl|Left' %} rotates by 0.1°.

### Save and load landmarks

Landmarks can be exported and imported from plain text files using the drop
down menu in the landmark table panel
({% include bc path="File | Export (Import) landmarks" %}).

### Export warped images

Export the warped moving image by clicking
{% include bc path="File | Export as ImagePlus" %} or using the
{% include key keys='Ctrl|E' %} keyboard shortcut.

![](/media/plugins/bigwarp/bigwarp-export.png)

The default parameters will result in the exported image having the same
dimensions as the target image.

{% include notice icon="info" content="Take care when exporting very large data sets as they can cause out-of-memory exceptions." %}

-   Resolution
    -   Target: *The output will have the same resolution as the target image*
    -   Moving: *The output will have the same resolution as the moving image*
    -   Specified: *The output will have the resolution given in the fields below (in the same units as the moving and target images).*

<!-- -->

-   Field of view
    -   Target: *The output will have the same field of view as the target image*
    -   Moving: *The output field of view will be the smallest bounding box that contains the warped moving images (approximated)*
    -   Specified (pixel): *The output field of view will be that given by the Offset and Field of View parameter fields where both are in units of pixels*
    -   Specified (physical): *The output field of view will be that given by the Offset and Field of View parameter fields where both are in the physical units of the moving and target images*

The warped moving image can be exported as an in-memory or [virtual](https://imagej.net/ij/docs/guide/146-8.html) ImagePlus. A virtual ImagePlus is generally faster to generate but slower to browse, whereas an in-memory ImagePlus will be slower to generate but faster to browse.

<img src="/media/plugins/bigwarp/bigwarplandmarkcenteredexport.png" width="600"/>

### Apply transforms

Often, it is important to apply transforms estimated with one image to other images in the same space.

If you have moving and target images open in Fiji [this script](https://github.com/saalfeldlab/bigwarp/blob/-/scripts/Apply_Bigwarp_Xfm.groovy) to transform the moving image into the space of the target image. You will need to provide a file containing the saved landmark point pairs.

To manually specify the field-of-view (FOV) of the target space, use [this script](https://github.com/saalfeldlab/bigwarp/blob/-/scripts/Apply_Bigwarp_Xfm_FOV.groovy)

To make the scripts above appear in your Fiji Plugins menu, simply copy them into the `/plugins/Scripts folder` in your Fiji installation.

### Export transforms

Export a transformation with {% include bc path="File | Export transformation" %}.  BigWarp can export non-linear
transformations as displacement fields that can either be displayed as a window in ImageJ or written to a file. BigWarp uses the
[OME-NGFF](https://github.com/ome/ngff) format to store transformations. 

{::nomarkdown}
<table>
  <tbody>
    <tr>
        <td style="padding:5px;">
            <ul>
            <li><b>Type</b> 
                <ul>
                    <li>Flat: Compose all transformatations BigWarp knows about into one single displacement field.</li>
                    <li>Sequence: If a transformation was imported on startup, this option saves a reference to it,
                        and newly created displacement field contains only the part of the transformation editable by BigWarp.</li>
                </ul>
            </li>
            <li><b>Direction</b> 
                <ul>
                    <li>FORWARD: The "forward" transform needed to transform image data.</li>
                    <li>INVERSE: The "inverse" transform needed to transform coordinate data.</li>
                    <li>BOTH: Exports both the forward and inverse transform when possible.</li>
                </ul>
            </li>
            <li><b>Split affine</b>: If selected, separates the affine from the deformable parts when exporting a thin-plate-spline.
            <li><b>Threads</b>: The number of parallel threads to use for computation.
            <li><b>Format</b> 
                <ul>
                    <li>NGFF: The recommended option uses <a href="https://github.com/ome/ngff">OME-NGFF</a>.</li>
                    <li>TPS: A temporary option that will hopefully one day join the NGFF standard.</li>
                </ul>
            </li>
            <li><b>Virtual</b>: If exporting to ImageJ, uses a <a href="https://imagej.net/ij/docs/guide/146-8.html#toc-Section-8">virtual stack</a>, i.e., the transformation will be computed on-the-fly, 
                so the transform will initially appear faster, but navigation will be slower when new parts of the images need to be computed.
            <li><b>N5 options</b>: The parameters for writing to chunked file formats. Read about them in <a href="https://github.com/saalfeldlab/n5-ij?tab=readme-ov-file#export-n5">the N5 documentation</a>.</li>
            <li><b>Field of view</b> : 
                <ul>
                    <li><b>Reference</b>
                        <ul>
                            <li>Moving (warped): BigWarp will set the spacing option to match the moving image, and will
                                estimate the physical size to the smallest bounding box that fits the entire warped moving image.</li>
                            <li>Target: BigWarp will set the field of view options to values matching the target image.</li>
                        </ul>
                    </li>
                    <li><b>units</b>: the physical unit for the field-of-view of the image.</li>
                    <li><b>min(unit)</b>: the physical coordinates of the top-left pixel.</li>
                    <li><b>size(unit)</b>: the physical extent in each dimension.</li>
                    <li><b>spacing(unit/px)</b> : the physical spacing between adjacent pixels along each dimension.</li>
                    <li><b>size(px)</b>: the number of pixels in each dimension.</li>
                </ul>
            </li>
            </ul>
        </td>
        <td style="padding: 5px;"> <img src="/media/plugins/bigwarp/bigwarp-export-transform-dialog.png" width="500"/> </td>
    </tr>
  </tbody>
</table>
{:/}



#### Warp 2d ImageJ ROIs

Download and install [this script](https://raw.githubusercontent.com/saalfeldlab/bigwarp/master/scripts/Apply_Bigwarp_Xfm_IjRoi2d.groovy).

Usage:

1.  Run the script downloadable above.
2.  Indicate which open images correspond to the moving and fixed images in bigwarp.
3.  Select the csv file that stores bigwarp landmarks.
4.  Indicate whether you want to transform an ROI from moving to target space or vice versa.
5.  Click OK.

Note that the resulting ROI will be densely sampled. This is because an ROI with a particular shape may not have the same shape after being warped (i.e., a circle may not still be circular after being warped).

Example: In this example, we've chosen the boats sample as the moving image, the bridge sample as the target image, and have added some landmarks that transform the boats image.

To warp an ROI from the moving boats image to the fixed bridge image, we run the script with the options:

> -   Fixed image: boats
> -   Moving image: bridge
> -   Landmark file: <our landmarks file>
> -   Moving to target

The results are shown in the "Forward example" below.

To warp an ROI from the moving boats image to the fixed bridge image, we run the script with the options:

> -   Fixed image: boats
> -   Moving image: bridge
> -   Landmark file: <our landmarks file>
> -   Target to moving

The results are shown in the "Inverse example" below.

|                                                   |                                                   |
|---------------------------------------------------|---------------------------------------------------|
| <img src="/media/plugins/bigwarp/bigwarp-warp-roi-fwd.png" width="600"/> | <img src="/media/plugins/bigwarp/bigwarp-warp-roi-inv.png" width="600"/> |
| Forward example                                                  | Inverse example                                                  |

Note, at this time ImageJ ROIs are 2D objects. We recommend using another approach for 3D regions of interest.

#### Warp points in a csv file

Download and install [this script](https://raw.githubusercontent.com/saalfeldlab/bigwarp/master/scripts/Apply_Bigwarp_Xfm_csvPts.groovy).

Usage:

1.  Run the script download-able above.
2.  Select the csv file that stores bigwarp landmarks.
3.  Select the csv file storing the points you want to transform.
4.  Select the location for csv file you want the results to be stored in.
5.  Indicate whether you want to transform the points from moving to target space or vice versa.
6.  Click OK.

Note the input csv must be formatted:

```
x1,y1,z1
x2,y2,z2
...
xN,yN,zN
```

without quotation marks, spaces, or any other characters. Csv files storing bigwarp landmarks will not work as input to this script.

## Working with large images

For very large images, we recommend first
[converting the volume to bigdataviewer's xml/hdf5 format](/plugins/bdv#exporting-datasets-for-the-bigdataviewer),
or to [N5](https://github.com/saalfeldlab/n5) using the [N5 plugin for Fiji](https://github.com/saalfeldlab/n5-ij).
Bigwarp now supports both bdv/xml and n5 formats (versions 7.0.0 and later).

Older versions of BigWarp supported these scripts:
* [Script for bdv/xml](https://raw.githubusercontent.com/saalfeldlab/bigwarp/master/scripts/BigWarp_ImagePlus_or_Xml.groovy)
 [(see also this forum post)](https://forum.image.sc/t/issue-with-big-warp/31472)
* [Script for N5](https://raw.githubusercontent.com/saalfeldlab/bigwarp/master/scripts/BigWarp_N5.groovy)

# Tutorials

-   A vitual tutorial given by {% include person id="bogovicj" %} in April 2022.

{% include video platform='youtube' id='EApotxnnQD8' %}

-   An example of a 2d warping by
    [Nicolas Chiaruttini](http://kiaru.eu/cv-rapide/) in response to
    [this forum post](https://forum.image.sc/t/superimpose-atlas-image-onto-microscope-picture/20593).

{% include video platform='youtube' id='zNur6mk9VXg' %}

# Publication

{% include citation %}

# Publications using BigWarp

1.  Russell et al. ["3D correlative light and electron microscopy of cultured cells using serial blockface scanning electron microscopy"](https://www.ncbi.nlm.nih.gov/pubmed/27445312) J Cell Sci 130: 278-291 2017.
2.  Collinson et al. ["Correlating 3D light to 3D electron microscopy for systems biology"](https://www.sciencedirect.com/science/article/pii/S2468451117300685) Current Opinion in Biomedical Engineering 2017 3:49-55
3.  Lerner et al. ["Mycobacterium tuberculosis replicates within necrotic human macrophages"](http://jcb.rupress.org/content/216/3/583) J Cell Biol 2017
4.  Hildebrand et al. ["Whole-brain serial-section electron microscopy in larval zebrafish"](https://www.nature.com/articles/nature22356) Nature 545:345–349 2017.
5.  Zhang et al. ["A Complete Electron Microscopy Volume Of The Brain Of Adult Drosophila melanogaster"](https://www.cell.com/cell/fulltext/S0092-8674(18)30787-6) Cell 174:3 P730-743.e22, 2018.
6.  Gao et al. ["Cortical column and whole-brain imaging with molecular contrast and nanoscale resolution."](http://science.sciencemag.org/content/363/6424/eaau8302.abstract) Science 363 (6424) 2019.
7.  Wan et al. ["Single-Cell Reconstruction of Emerging Population Activity in an Entire Developing Circuit."](https://www.sciencedirect.com/science/article/pii/S0092867419309584) Cell 179(2) 2019.
8.  Hoffman, Shtengel et al. ["Correlative three-dimensional super-resolution and block-face electron microscopy of whole vitreously frozen cells."](https://science.sciencemag.org/content/367/6475/eaaz5357) Science 367 (6475) 2020.
9.  Weigel et al. [“ER-to-Golgi protein delivery through an interwoven, tubular network extending from ER”](https://doi.org/10.1016/j.cell.2021.03.035) Cell 184:9 2021.
10. Chiaruttini et al. ["An Open-Source Whole Slide Image Registration Workflow at Cellular Precision Using Fiji, QuPath and Elastix"](https://www.frontiersin.org/articles/10.3389/fcomp.2021.780026/full) Frontiers In Computer Science 2021.
11. Ritter et al. ["ESCRT-mediated membrane repair protects tumor-derived cells against T cell attack"](https://doi.org/10.1126/science.abl3855) Science 376 (6591) 2022.
