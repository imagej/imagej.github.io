---
mediawiki: Comparison_of_Matlab_functions_and_Ops
title: Comparison of MATLAB functions and Ops
project: /software/imagej2
---

{% include notice icon="info" content='This page is under active development.' %}

This page is intended to help developers switch from MATLAB to Ops by showing equivalent operations.

## Import, Export, and Conversion

### Read and Write Image Data from Files

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td>
        <p>{% include matlab path='matlab/ref' function='imread' %}</p>
      </td>
      <td>
        <p>Read image from graphics file</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='matlab/ref' function='imwrite' %}</p>
      </td>
      <td>
        <p>Write image to graphics file</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='matlab/ref' function='imfinfo' %}</p>
      </td>
      <td>
        <p>Information about graphics file</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='nitfinfo' %}</p>
      </td>
      <td>
        <p>Read metadata from National Imagery Transmission Format (NITF) file</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='nitfread' %}</p>
      </td>
      <td>
        <p>Read image from NITF file</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='dpxinfo' %}</p>
      </td>
      <td>
        <p>Read metadata from DPX file</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='dpxread' %}</p>
      </td>
      <td>
        <p>Read DPX image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='analyze75info' %}</p>
      </td>
      <td>
        <p>Read metadata from header file of Analyze 7.5 data set</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='analyze75read' %}</p>
      </td>
      <td>
        <p>Read image data from image file of Analyze 7.5 data set</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='interfileinfo' %}</p>
      </td>
      <td>
        <p>Read metadata from Interfile file</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='interfileread' %}</p>
      </td>
      <td>
        <p>Read images in Interfile format</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

### Read and Write Image Data from DICOM Files

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='dicomanon' %}</p>
      </td>
      <td>
        <p>Anonymize DICOM file</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='dicomdict' %}</p>
      </td>
      <td>
        <p>Get or set active DICOM data dictionary</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='dicomdisp' %}</p>
      </td>
      <td>
        <p>Display DICOM file structure</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='dicominfo' %}</p>
      </td>
      <td>
        <p>Read metadata from DICOM message</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='dicomlookup' %}</p>
      </td>
      <td>
        <p>Find attribute in DICOM data dictionary</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='dicomread' %}</p>
      </td>
      <td>
        <p>Read DICOM image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='dicomuid' %}</p>
      </td>
      <td>
        <p>Generate DICOM unique identifier</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='dicomwrite' %}</p>
      </td>
      <td>
        <p>Write images as DICOM files</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

### High Dynamic Range Images

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='hdrread' %}</p>
      </td>
      <td>
        <p>Read high dynamic range (HDR) image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='hdrwrite' %}</p>
      </td>
      <td>
        <p>Write Radiance high dynamic range (HDR) image file</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='makehdr' %}</p>
      </td>
      <td>
        <p>Create high dynamic range image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='tonemap' %}</p>
      </td>
      <td>
        <p>Render high dynamic range image for viewing</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

### Large Image Files

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imageadapter-class' %}</p>
      </td>
      <td>
        <p>Interface for image I/O</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='isrset' %}</p>
      </td>
      <td>
        <p>Check if file is R-Set</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='openrset' %}</p>
      </td>
      <td>
        <p>Open R-Set file</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='rsetwrite' %}</p>
      </td>
      <td>
        <p>Create reduced resolution data set from image file</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

### Image Type Conversion

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='gray2ind' %}</p>
      </td>
      <td>
        <p>Convert grayscale or binary image to indexed image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='ind2gray' %}</p>
      </td>
      <td>
        <p>Convert indexed image to grayscale image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='mat2gray' %}</p>
      </td>
      <td>
        <p>Convert matrix to grayscale image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='matlab/ref' function='rgb2gray' %}</p>
      </td>
      <td>
        <p>Convert RGB image or colormap to grayscale</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='ind2rgb' %}</p>
      </td>
      <td>
        <p>Convert indexed image to RGB image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='label2rgb' %}</p>
      </td>
      <td>
        <p>Convert label matrix into RGB image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='demosaic' %}</p>
      </td>
      <td>
        <p>Convert Bayer pattern encoded image to truecolor image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imbinarize' %}</p>
      </td>
      <td>
        <p>Binarize image by thresholding</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imquantize' %}</p>
      </td>
      <td>
        <p>Quantize image using specified quantization levels and output values</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='multithresh' %}</p>
      </td>
      <td>
        <p>Multilevel image thresholds using Otsu's method</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='adaptthresh' %}</p>
      </td>
      <td>
        <p>Adaptive image threshold using local first-order statistics</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='otsuthresh' %}</p>
      </td>
      <td>
        <p>Global histogram threshold using Otsu's method</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='graythresh' %}</p>
      </td>
      <td>
        <p>Global image threshold using Otsu's method</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='grayslice' %}</p>
      </td>
      <td>
        <p>Convert grayscale image to indexed image using multilevel thresholding</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='matlab/ref' function='im2double' %}</p>
      </td>
      <td>
        <p>Convert image to double precision</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='im2int16' %}</p>
      </td>
      <td>
        <p>Convert image to 16-bit signed integers</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='im2java2d' %}</p>
      </td>
      <td>
        <p>Convert image to Java buffered image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='im2single' %}</p>
      </td>
      <td>
        <p>Convert image to single precision</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='im2uint16' %}</p>
      </td>
      <td>
        <p>Convert image to 16-bit unsigned integers</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='im2uint8' %}</p>
      </td>
      <td>
        <p>Convert image to 8-bit unsigned integers</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

### Color

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='rgb2lab' %}</p>
      </td>
      <td>
        <p>Convert RGB to CIE 1976 L*a*b*</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='rgb2ntsc' %}</p>
      </td>
      <td>
        <p>Convert RGB color values to NTSC color space</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='rgb2xyz' %}</p>
      </td>
      <td>
        <p>Convert RGB to CIE 1931 XYZ</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='rgb2ycbcr' %}</p>
      </td>
      <td>
        <p>Convert RGB color values to YCbCr color space</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='lab2rgb' %}</p>
      </td>
      <td>
        <p>Convert CIE 1976 L*a*b* to RGB</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='lab2xyz' %}</p>
      </td>
      <td>
        <p>Convert CIE 1976 L*a*b* to CIE 1931 XYZ</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='xyz2lab' %}</p>
      </td>
      <td>
        <p>Convert CIE 1931 XYZ to CIE 1976 L*a*b*</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='xyz2rgb' %}</p>
      </td>
      <td>
        <p>Convert CIE 1931 XYZ to RGB</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='ycbcr2rgb' %}</p>
      </td>
      <td>
        <p>Convert YCbCr color values to RGB color space</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='ntsc2rgb' %}</p>
      </td>
      <td>
        <p>Convert NTSC values to RGB color space</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='lab2double' %}</p>
      </td>
      <td>
        <p>Convert L*a*b* data to double</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='lab2uint16' %}</p>
      </td>
      <td>
        <p>Convert L*a*b* data to uint16</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='lab2uint8' %}</p>
      </td>
      <td>
        <p>Convert L*a*b* data to uint8</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='xyz2double' %}</p>
      </td>
      <td>
        <p>Convert XYZ color values to double</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='xyz2uint16' %}</p>
      </td>
      <td>
        <p>Convert XYZ color values to uint16</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='iccfind' %}</p>
      </td>
      <td>
        <p>Search for ICC profiles</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='iccread' %}</p>
      </td>
      <td>
        <p>Read ICC profile</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='iccroot' %}</p>
      </td>
      <td>
        <p>Find system default ICC profile repository</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='iccwrite' %}</p>
      </td>
      <td>
        <p>Write ICC color profile to disk file</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='isicc' %}</p>
      </td>
      <td>
        <p>True for valid ICC color profile</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='makecform' %}</p>
      </td>
      <td>
        <p>Create color transformation structure</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='applycform' %}</p>
      </td>
      <td>
        <p>Apply device-independent color space transformation</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='matlab/ref' function='imapprox' %}</p>
      </td>
      <td>
        <p>Approximate indexed image by reducing number of colors</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='colorcloud' %}</p>
      </td>
      <td>
        <p>Display 3-D color gamut as point cloud in specified color space</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='whitepoint' %}</p>
      </td>
      <td>
        <p>XYZ color values of standard illuminants</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

### Synthetic Images

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='checkerboard' %}</p>
      </td>
      <td>
        <p>Create checkerboard image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='phantom' %}</p>
      </td>
      <td>
        <p>Create head phantom image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imnoise' %}</p>
      </td>
      <td>
        <p>Add noise to image</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

## Display and Exploration

### Basic Display

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imshow' %}</p>
      </td>
      <td>
        <p>Display image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='montage' %}</p>
      </td>
      <td>
        <p>Display multiple image frames as rectangular montage</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='immovie' %}</p>
      </td>
      <td>
        <p>Make movie from multiframe image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='implay' %}</p>
      </td>
      <td>
        <p>Play movies, videos, or image sequences</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='warp' %}</p>
      </td>
      <td>
        <p>Display image as texture-mapped surface</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='iptgetpref' %}</p>
      </td>
      <td>
        <p>Get values of Image Processing Toolbox preferences</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='iptprefs' %}</p>
      </td>
      <td>
        <p>Display Image Processing Toolbox Preferences dialog box</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='iptsetpref' %}</p>
      </td>
      <td>
        <p>Set Image Processing Toolbox preferences or display valid values</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

### Interactive Exploration with the Image Viewer App

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imtool' %}</p>
      </td>
      <td>
        <p>Image Viewer app</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imageinfo' %}</p>
      </td>
      <td>
        <p>Image Information tool</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imcontrast' %}</p>
      </td>
      <td>
        <p>Adjust Contrast tool</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imdisplayrange' %}</p>
      </td>
      <td>
        <p>Display Range tool</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imdistline' %}</p>
      </td>
      <td>
        <p>Distance tool</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='impixelinfo' %}</p>
      </td>
      <td>
        <p>Pixel Information tool</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='impixelinfoval' %}</p>
      </td>
      <td>
        <p>Pixel Information tool without text label</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='impixelregion' %}</p>
      </td>
      <td>
        <p>Pixel Region tool</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='immagbox' %}</p>
      </td>
      <td>
        <p>Magnification box for scroll panel</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imoverview' %}</p>
      </td>
      <td>
        <p>Overview tool for image displayed in scroll panel</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='iptgetpref' %}</p>
      </td>
      <td>
        <p>Get values of Image Processing Toolbox preferences</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='iptprefs' %}</p>
      </td>
      <td>
        <p>Display Image Processing Toolbox Preferences dialog box</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='iptsetpref' %}</p>
      </td>
      <td>
        <p>Set Image Processing Toolbox preferences or display valid values</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

### Build Interactive Tools

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imageinfo' %}</p>
      </td>
      <td>
        <p>Image Information tool</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imcolormaptool' %}</p>
      </td>
      <td>
        <p>Choose Colormap tool</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imcontrast' %}</p>
      </td>
      <td>
        <p>Adjust Contrast tool</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imcrop' %}</p>
      </td>
      <td>
        <p>Crop image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imdisplayrange' %}</p>
      </td>
      <td>
        <p>Display Range tool</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imdistline' %}</p>
      </td>
      <td>
        <p>Distance tool</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='impixelinfo' %}</p>
      </td>
      <td>
        <p>Pixel Information tool</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='impixelinfoval' %}</p>
      </td>
      <td>
        <p>Pixel Information tool without text label</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='impixelregion' %}</p>
      </td>
      <td>
        <p>Pixel Region tool</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='impixelregionpanel' %}</p>
      </td>
      <td>
        <p>Pixel Region tool panel</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='immagbox' %}</p>
      </td>
      <td>
        <p>Magnification box for scroll panel</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imoverview' %}</p>
      </td>
      <td>
        <p>Overview tool for image displayed in scroll panel</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imoverviewpanel' %}</p>
      </td>
      <td>
        <p>Overview tool panel for image displayed in scroll panel</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imsave' %}</p>
      </td>
      <td>
        <p>Save Image Tool</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imscrollpanel' %}</p>
      </td>
      <td>
        <p>Scroll panel for interactive image navigation</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imellipse' %}</p>
      </td>
      <td>
        <p>Create draggable ellipse</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imfreehand' %}</p>
      </td>
      <td>
        <p>Create draggable freehand region</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imline' %}</p>
      </td>
      <td>
        <p>Create draggable, resizable line</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='impoint' %}</p>
      </td>
      <td>
        <p>Create draggable point</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='impoly' %}</p>
      </td>
      <td>
        <p>Create draggable, resizable polygon</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imrect' %}</p>
      </td>
      <td>
        <p>Create draggable rectangle</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imroi' %}</p>
      </td>
      <td>
        <p>Region-of-interest (ROI) base class</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='getline' %}</p>
      </td>
      <td>
        <p>Select polyline with mouse</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='getpts' %}</p>
      </td>
      <td>
        <p>Specify points with mouse</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='getrect' %}</p>
      </td>
      <td>
        <p>Specify rectangle with mouse</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='getimage' %}</p>
      </td>
      <td>
        <p>Image data from axes</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='getimagemodel' %}</p>
      </td>
      <td>
        <p>Image model object from image object</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imagemodel' %}</p>
      </td>
      <td>
        <p>Image Model object</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='axes2pix' %}</p>
      </td>
      <td>
        <p>Convert axes coordinates to pixel coordinates</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imattributes' %}</p>
      </td>
      <td>
        <p>Information about image attributes</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imgca' %}</p>
      </td>
      <td>
        <p>Get current axes containing image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imgcf' %}</p>
      </td>
      <td>
        <p>Get current figure containing image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imgetfile' %}</p>
      </td>
      <td>
        <p>Display Open Image dialog box</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imhandles' %}</p>
      </td>
      <td>
        <p>Get all image objects</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='iptaddcallback' %}</p>
      </td>
      <td>
        <p>Add function handle to callback list</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='iptcheckhandle' %}</p>
      </td>
      <td>
        <p>Check validity of handle</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='iptgetapi' %}</p>
      </td>
      <td>
        <p>Get Application Programmer Interface (API) for handle</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='iptgetpointerbehavior' %}</p>
      </td>
      <td>
        <p>Retrieve pointer behavior from graphics object</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='ipticondir' %}</p>
      </td>
      <td>
        <p>Directories containing IPT and MATLAB icons</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='iptpointermanager' %}</p>
      </td>
      <td>
        <p>Create pointer manager in figure</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='iptremovecallback' %}</p>
      </td>
      <td>
        <p>Delete function handle from callback list</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='iptsetpointerbehavior' %}</p>
      </td>
      <td>
        <p>Store pointer behavior structure in graphics object</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='iptwindowalign' %}</p>
      </td>
      <td>
        <p>Align figure windows</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='makeconstraintorectfcn' %}</p>
      </td>
      <td>
        <p>Create rectangularly bounded drag constraint function</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='truesize' %}</p>
      </td>
      <td>
        <p>Adjust display size of image</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

## Geometric Transformation, Spatial Referencing, and Image Registration

### Geometric Transformations

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imcrop' %}</p>
      </td>
      <td>
        <p>Crop image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imresize' %}</p>
      </td>
      <td>
        <p>Resize image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imrotate' %}</p>
      </td>
      <td>
        <p>Rotate image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imtranslate' %}</p>
      </td>
      <td>
        <p>Translate image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='impyramid' %}</p>
      </td>
      <td>
        <p>Image pyramid reduction and expansion</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imwarp' %}</p>
      </td>
      <td>
        <p>Apply geometric transformation to image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='fitgeotrans' %}</p>
      </td>
      <td>
        <p>Fit geometric transformation to control point pairs</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imtransform' %}</p>
      </td>
      <td>
        <p>Apply 2-D spatial transformation to image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='findbounds' %}</p>
      </td>
      <td>
        <p>Find output bounds for spatial transformation</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='fliptform' %}</p>
      </td>
      <td>
        <p>Flip input and output roles of TFORM structure</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='makeresampler' %}</p>
      </td>
      <td>
        <p>Create resampling structure</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='maketform' %}</p>
      </td>
      <td>
        <p>Create spatial transformation structure (TFORM)</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='tformarray' %}</p>
      </td>
      <td>
        <p>Apply spatial transformation to N-D array</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='tformfwd' %}</p>
      </td>
      <td>
        <p>Apply forward spatial transformation</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='tforminv' %}</p>
      </td>
      <td>
        <p>Apply inverse spatial transformation</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='checkerboard' %}</p>
      </td>
      <td>
        <p>Create checkerboard image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='affine2d' %}</p>
      </td>
      <td>
        <p>2-D Affine Geometric Transformation</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='affine3d' %}</p>
      </td>
      <td>
        <p>3-D Affine Geometric Transformation</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='projective2d' %}</p>
      </td>
      <td>
        <p>2-D Projective Geometric Transformation</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='images.geotrans.piecewiselineartransformation2d' %}</p>
      </td>
      <td>
        <p>2-D piecewise linear geometric transformation</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='images.geotrans.polynomialtransformation2d' %}</p>
      </td>
      <td>
        <p>2-D Polynomial Geometric Transformation</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='images.geotrans.localweightedmeantransformation2d' %}</p>
      </td>
      <td>
        <p>2-D Local Weighted Mean Geometric Transformation</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

### Spatial Referencing

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imwarp' %}</p>
      </td>
      <td>
        <p>Apply geometric transformation to image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imregister' %}</p>
      </td>
      <td>
        <p>Intensity-based image registration</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imregtform' %}</p>
      </td>
      <td>
        <p>Estimate geometric transformation that aligns two 2-D or 3-D images</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imshow' %}</p>
      </td>
      <td>
        <p>Display image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imshowpair' %}</p>
      </td>
      <td>
        <p>Compare differences between images</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imfuse' %}</p>
      </td>
      <td>
        <p>Composite of two images</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imref2d' %}</p>
      </td>
      <td>
        <p>Reference 2-D image to world coordinates</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imref3d' %}</p>
      </td>
      <td>
        <p>Reference 3-D image to world coordinates</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

### Automatic Registration

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imregister' %}</p>
      </td>
      <td>
        <p>Intensity-based image registration</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imregconfig' %}</p>
      </td>
      <td>
        <p>Configurations for intensity-based registration</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imregtform' %}</p>
      </td>
      <td>
        <p>Estimate geometric transformation that aligns two 2-D or 3-D images</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imregcorr' %}</p>
      </td>
      <td>
        <p>Estimates geometric transformation that aligns two 2-D images using phase correlation</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imregdemons' %}</p>
      </td>
      <td>
        <p>Estimate displacement field that aligns two 2-D or 3-D images</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imfuse' %}</p>
      </td>
      <td>
        <p>Composite of two images</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imshowpair' %}</p>
      </td>
      <td>
        <p>Compare differences between images</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='registration.metric.mattesmutualinformation' %}</p>
      </td>
      <td>
        <p>Mattes mutual information metric configuration object</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='registration.metric.meansquares' %}</p>
      </td>
      <td>
        <p>Mean square error metric configuration object</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='registration.optimizer.regularstepgradientdescent' %}</p>
      </td>
      <td>
        <p>Regular step gradient descent optimizer configuration object</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='registration.optimizer.oneplusoneevolutionary' %}</p>
      </td>
      <td>
        <p>One-plus-one evolutionary optimizer configuration object</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

### Control Point Registration

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='cpselect' %}</p>
      </td>
      <td>
        <p>Control Point Selection Tool</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='fitgeotrans' %}</p>
      </td>
      <td>
        <p>Fit geometric transformation to control point pairs</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='cpcorr' %}</p>
      </td>
      <td>
        <p>Tune control-point locations using cross correlation</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='cpstruct2pairs' %}</p>
      </td>
      <td>
        <p>Convert CPSTRUCT to valid pairs of control points</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='normxcorr2' %}</p>
      </td>
      <td>
        <p>Normalized 2-D cross-correlation</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='cp2tform' %}</p>
      </td>
      <td>
        <p>Infer spatial transformation from control point pairs</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

## Image Enhancement

### Contrast Adjustment

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imadjust' %}</p>
      </td>
      <td>
        <p>Adjust image intensity values or colormap</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imcontrast' %}</p>
      </td>
      <td>
        <p>Adjust Contrast tool</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imsharpen' %}</p>
      </td>
      <td>
        <p>Sharpen image using unsharp masking</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='locallapfilt' %}</p>
      </td>
      <td>
        <p>Fast Local Laplacian Filtering of images</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='localcontrast' %}</p>
      </td>
      <td>
        <p>Edge-aware local contrast manipulation of images</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='localtonemap' %}</p>
      </td>
      <td>
        <p>Render HDR image for viewing while enhancing local contrast</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='histeq' %}</p>
      </td>
      <td>
        <p>Enhance contrast using histogram equalization</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='adapthisteq' %}</p>
      </td>
      <td>
        <p>Contrast-limited adaptive histogram equalization (CLAHE)</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imhistmatch' %}</p>
      </td>
      <td>
        <p>Adjust histogram of image to match N-bin histogram of reference image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='decorrstretch' %}</p>
      </td>
      <td>
        <p>Apply decorrelation stretch to multichannel image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='stretchlim' %}</p>
      </td>
      <td>
        <p>Find limits to contrast stretch image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='intlut' %}</p>
      </td>
      <td>
        <p>Convert integer values using lookup table</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imnoise' %}</p>
      </td>
      <td>
        <p>Add noise to image</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

### Image Filtering

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imfilter' %}</p>
      </td>
      <td>
        <p>N-D filtering of multidimensional images</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imgaussfilt' %}</p>
      </td>
      <td>
        <p>2-D Gaussian filtering of images</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imgaussfilt3' %}</p>
      </td>
      <td>
        <p>3-D Gaussian filtering of 3-D images</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='fspecial' %}</p>
      </td>
      <td>
        <p>Create predefined 2-D filter</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imguidedfilter' %}</p>
      </td>
      <td>
        <p>Guided filtering of images</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='normxcorr2' %}</p>
      </td>
      <td>
        <p>Normalized 2-D cross-correlation</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='wiener2' %}</p>
      </td>
      <td>
        <p>2-D adaptive noise-removal filtering</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='medfilt2' %}</p>
      </td>
      <td>
        <p>2-D median filtering</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='medfilt3' %}</p>
      </td>
      <td>
        <p>3-D median filtering</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='ordfilt2' %}</p>
      </td>
      <td>
        <p>2-D order-statistic filtering</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='stdfilt' %}</p>
      </td>
      <td>
        <p>Local standard deviation of image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='rangefilt' %}</p>
      </td>
      <td>
        <p>Local range of image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='entropyfilt' %}</p>
      </td>
      <td>
        <p>Local entropy of grayscale image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='nlfilter' %}</p>
      </td>
      <td>
        <p>General sliding-neighborhood operations</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='gabor' %}</p>
      </td>
      <td>
        <p>Create Gabor filter or Gabor filter bank</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imgaborfilt' %}</p>
      </td>
      <td>
        <p>Apply Gabor filter or set of filters to 2-D image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imboxfilt' %}</p>
      </td>
      <td>
        <p>2-D box filtering of images</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imboxfilt3' %}</p>
      </td>
      <td>
        <p>3-D box filtering of 3-D images</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='integralimage' %}</p>
      </td>
      <td>
        <p>Calculate integral image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='integralimage3' %}</p>
      </td>
      <td>
        <p>Calculate 3-D integral image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='integralboxfilter' %}</p>
      </td>
      <td>
        <p>2-D box filtering of integral images</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='integralboxfilter3' %}</p>
      </td>
      <td>
        <p>3-D box filtering of 3-D integral images</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='bwareafilt' %}</p>
      </td>
      <td>
        <p>Extract objects from binary image by size</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='bwpropfilt' %}</p>
      </td>
      <td>
        <p>Extract objects from binary image using properties</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='padarray' %}</p>
      </td>
      <td>
        <p>Pad array</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='freqz2' %}</p>
      </td>
      <td>
        <p>2-D frequency response</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='fsamp2' %}</p>
      </td>
      <td>
        <p>2-D FIR filter using frequency sampling</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='ftrans2' %}</p>
      </td>
      <td>
        <p>2-D FIR filter using frequency transformation</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='fwind1' %}</p>
      </td>
      <td>
        <p>2-D FIR filter using 1-D window method</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='fwind2' %}</p>
      </td>
      <td>
        <p>2-D FIR filter using 2-D window method</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='convmtx2' %}</p>
      </td>
      <td>
        <p>2-D convolution matrix</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

### Morphological Operations

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='bwhitmiss' %}</p>
      </td>
      <td>
        <p>Binary hit-miss operation</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='bwmorph' %}</p>
      </td>
      <td>
        <p>Morphological operations on binary images</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='bwulterode' %}</p>
      </td>
      <td>
        <p>Ultimate erosion</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='bwareaopen' %}</p>
      </td>
      <td>
        <p>Remove small objects from binary image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imbothat' %}</p>
      </td>
      <td>
        <p>Bottom-hat filtering</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imclearborder' %}</p>
      </td>
      <td>
        <p>Suppress light structures connected to image border</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imclose' %}</p>
      </td>
      <td>
        <p>Morphologically close image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imdilate' %}</p>
      </td>
      <td>
        <p>Dilate image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imerode' %}</p>
      </td>
      <td>
        <p>Erode image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imextendedmax' %}</p>
      </td>
      <td>
        <p>Extended-maxima transform</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imextendedmin' %}</p>
      </td>
      <td>
        <p>Extended-minima transform</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imfill' %}</p>
      </td>
      <td>
        <p>Fill image regions and holes</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imhmax' %}</p>
      </td>
      <td>
        <p>H-maxima transform</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imhmin' %}</p>
      </td>
      <td>
        <p>H-minima transform</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imimposemin' %}</p>
      </td>
      <td>
        <p>Impose minima</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imopen' %}</p>
      </td>
      <td>
        <p>Morphologically open image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imreconstruct' %}</p>
      </td>
      <td>
        <p>Morphological reconstruction</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imregionalmax' %}</p>
      </td>
      <td>
        <p>Regional maxima</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imregionalmin' %}</p>
      </td>
      <td>
        <p>Regional minima</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imtophat' %}</p>
      </td>
      <td>
        <p>Top-hat filtering</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='watershed' %}</p>
      </td>
      <td>
        <p>Watershed transform</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='conndef' %}</p>
      </td>
      <td>
        <p>Create connectivity array</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='iptcheckconn' %}</p>
      </td>
      <td>
        <p>Check validity of connectivity argument</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='applylut' %}</p>
      </td>
      <td>
        <p>Neighborhood operations on binary images using lookup tables</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='bwlookup' %}</p>
      </td>
      <td>
        <p>Nonlinear filtering using lookup tables</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='makelut' %}</p>
      </td>
      <td>
        <p>Create lookup table for use with bwlookup</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='strel' %}</p>
      </td>
      <td>
        <p>Morphological structuring element</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='offsetstrel' %}</p>
      </td>
      <td>
        <p>Morphological offset structuring element</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

<h3 id="btdrz6j-1">

Deblurring

</h3>

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='deconvblind' %}</p>
      </td>
      <td>
        <p>Deblur image using blind deconvolution</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='deconvlucy' %}</p>
      </td>
      <td>
        <p>Deblur image using Lucy-Richardson method</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='deconvreg' %}</p>
      </td>
      <td>
        <p>Deblur image using regularized filter</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='deconvwnr' %}</p>
      </td>
      <td>
        <p>Deblur image using Wiener filter</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='edgetaper' %}</p>
      </td>
      <td>
        <p>Taper discontinuities along image edges</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='otf2psf' %}</p>
      </td>
      <td>
        <p>Convert optical transfer function to point-spread function</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='psf2otf' %}</p>
      </td>
      <td>
        <p>Convert point-spread function to optical transfer function</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='padarray' %}</p>
      </td>
      <td>
        <p>Pad array</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

### ROI-Based Processing

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='roipoly' %}</p>
      </td>
      <td>
        <p>Specify polygonal region of interest (ROI)</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='poly2mask' %}</p>
      </td>
      <td>
        <p>Convert region of interest (ROI) polygon to region mask</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='regionfill' %}</p>
      </td>
      <td>
        <p>Fill in specified regions in image using inward interpolation</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='roicolor' %}</p>
      </td>
      <td>
        <p>Select region of interest (ROI) based on color</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='roifilt2' %}</p>
      </td>
      <td>
        <p>Filter region of interest (ROI) in image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imellipse' %}</p>
      </td>
      <td>
        <p>Create draggable ellipse</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imfreehand' %}</p>
      </td>
      <td>
        <p>Create draggable freehand region</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='impoly' %}</p>
      </td>
      <td>
        <p>Create draggable, resizable polygon</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imrect' %}</p>
      </td>
      <td>
        <p>Create draggable rectangle</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imroi' %}</p>
      </td>
      <td>
        <p>Region-of-interest (ROI) base class</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

### Neighborhood and Block Processing

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imageadapter-class' %}</p>
      </td>
      <td>
        <p>Interface for image I/O</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='blockproc' %}</p>
      </td>
      <td>
        <p>Distinct block processing for image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='bestblk' %}</p>
      </td>
      <td>
        <p>Determine optimal block size for block processing</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='nlfilter' %}</p>
      </td>
      <td>
        <p>General sliding-neighborhood operations</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='col2im' %}</p>
      </td>
      <td>
        <p>Rearrange matrix columns into blocks</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='colfilt' %}</p>
      </td>
      <td>
        <p>Columnwise neighborhood operations</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='im2col' %}</p>
      </td>
      <td>
        <p>Rearrange image blocks into columns</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

### Image Arithmetic

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imabsdiff' %}</p>
      </td>
      <td>
        <p>Absolute difference of two images</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imadd' %}</p>
      </td>
      <td>
        <p>Add two images or add constant to image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imapplymatrix' %}</p>
      </td>
      <td>
        <p>Linear combination of color channels</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imcomplement' %}</p>
      </td>
      <td>
        <p>Complement image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imdivide' %}</p>
      </td>
      <td>
        <p>Divide one image into another or divide image by constant</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imlincomb' %}</p>
      </td>
      <td>
        <p>Linear combination of images</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='immultiply' %}</p>
      </td>
      <td>
        <p>Multiply two images or multiply image by constant</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imsubtract' %}</p>
      </td>
      <td>
        <p>Subtract one image from another or subtract constant from image</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

## Image Analysis

### Object Analysis

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='bwboundaries' %}</p>
      </td>
      <td>
        <p>Trace region boundaries in binary image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='bwtraceboundary' %}</p>
      </td>
      <td>
        <p>Trace object in binary image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='visboundaries' %}</p>
      </td>
      <td>
        <p>Plot region boundaries</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='edge' %}</p>
      </td>
      <td>
        <p>Find edges in intensity image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imfindcircles' %}</p>
      </td>
      <td>
        <p>Find circles using circular Hough transform</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='viscircles' %}</p>
      </td>
      <td>
        <p>Create circle</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imgradient' %}</p>
      </td>
      <td>
        <p>Gradient magnitude and direction of an image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imgradientxy' %}</p>
      </td>
      <td>
        <p>Directional gradients of an image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imgradient3' %}</p>
      </td>
      <td>
        <p>Find 3-D gradient magnitude and direction of images</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imgradientxyz' %}</p>
      </td>
      <td>
        <p>Find the directional gradients of a 3-D image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='hough' %}</p>
      </td>
      <td>
        <p>Hough transform</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='houghlines' %}</p>
      </td>
      <td>
        <p>Extract line segments based on Hough transform</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='houghpeaks' %}</p>
      </td>
      <td>
        <p>Identify peaks in Hough transform</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='qtdecomp' %}</p>
      </td>
      <td>
        <p>Quadtree decomposition</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='qtgetblk' %}</p>
      </td>
      <td>
        <p>Block values in quadtree decomposition</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='qtsetblk' %}</p>
      </td>
      <td>
        <p>Set block values in quadtree decomposition</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

### Region and Image Properties

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='regionprops' %}</p>
      </td>
      <td>
        <p>Measure properties of image regions</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='bwarea' %}</p>
      </td>
      <td>
        <p>Area of objects in binary image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='bwareafilt' %}</p>
      </td>
      <td>
        <p>Extract objects from binary image by size</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='bwconncomp' %}</p>
      </td>
      <td>
        <p>Find connected components in binary image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='bwconvhull' %}</p>
      </td>
      <td>
        <p>Generate convex hull image from binary image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='bwdist' %}</p>
      </td>
      <td>
        <p>Distance transform of binary image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='bwdistgeodesic' %}</p>
      </td>
      <td>
        <p>Geodesic distance transform of binary image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='bweuler' %}</p>
      </td>
      <td>
        <p>Euler number of binary image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='bwperim' %}</p>
      </td>
      <td>
        <p>Find perimeter of objects in binary image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='bwpropfilt' %}</p>
      </td>
      <td>
        <p>Extract objects from binary image using properties</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='bwselect' %}</p>
      </td>
      <td>
        <p>Select objects in binary image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='graydist' %}</p>
      </td>
      <td>
        <p>Gray-weighted distance transform of grayscale image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imcontour' %}</p>
      </td>
      <td>
        <p>Create contour plot of image data</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imhist' %}</p>
      </td>
      <td>
        <p>Histogram of image data</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='impixel' %}</p>
      </td>
      <td>
        <p>Pixel color values</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='improfile' %}</p>
      </td>
      <td>
        <p>Pixel-value cross-sections along line segments</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='corr2' %}</p>
      </td>
      <td>
        <p>2-D correlation coefficient</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='mean2' %}</p>
      </td>
      <td>
        <p>Average or mean of matrix elements</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='std2' %}</p>
      </td>
      <td>
        <p>Standard deviation of matrix elements</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='bwlabel' %}</p>
      </td>
      <td>
        <p>Label connected components in 2-D binary image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='bwlabeln' %}</p>
      </td>
      <td>
        <p>Label connected components in binary image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='labelmatrix' %}</p>
      </td>
      <td>
        <p>Create label matrix from bwconncomp structure</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='bwpack' %}</p>
      </td>
      <td>
        <p>Pack binary image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='bwunpack' %}</p>
      </td>
      <td>
        <p>Unpack binary image</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

### Texture Analysis

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='entropy' %}</p>
      </td>
      <td>
        <p>Entropy of grayscale image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='entropyfilt' %}</p>
      </td>
      <td>
        <p>Local entropy of grayscale image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='rangefilt' %}</p>
      </td>
      <td>
        <p>Local range of image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='stdfilt' %}</p>
      </td>
      <td>
        <p>Local standard deviation of image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='graycomatrix' %}</p>
      </td>
      <td>
        <p>Create gray-level co-occurrence matrix from image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='graycoprops' %}</p>
      </td>
      <td>
        <p>Properties of gray-level co-occurrence matrix</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

### Image Quality

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='immse' %}</p>
      </td>
      <td>
        <p>Mean-squared error</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='psnr' %}</p>
      </td>
      <td>
        <p>Peak Signal-to-Noise Ratio (PSNR)</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='ssim' %}</p>
      </td>
      <td>
        <p>Structural Similarity Index (SSIM) for measuring image quality</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

### Image Segmentation

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='activecontour' %}</p>
      </td>
      <td>
        <p>Segment image into foreground and background using active contour</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imsegfmm' %}</p>
      </td>
      <td>
        <p>Binary image segmentation using Fast Marching Method</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imseggeodesic' %}</p>
      </td>
      <td>
        <p>Segment image into two or three regions using geodesic distance-based color segmentation</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='gradientweight' %}</p>
      </td>
      <td>
        <p>Calculate weights for image pixels based on image gradient</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='graydiffweight' %}</p>
      </td>
      <td>
        <p>Calculate weights for image pixels based on grayscale intensity difference</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='grayconnected' %}</p>
      </td>
      <td>
        <p>Select contiguous image region with similar gray values</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='graythresh' %}</p>
      </td>
      <td>
        <p>Global image threshold using Otsu's method</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='multithresh' %}</p>
      </td>
      <td>
        <p>Multilevel image thresholds using Otsu's method</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='otsuthresh' %}</p>
      </td>
      <td>
        <p>Global histogram threshold using Otsu's method</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='adaptthresh' %}</p>
      </td>
      <td>
        <p>Adaptive image threshold using local first-order statistics</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='boundarymask' %}</p>
      </td>
      <td>
        <p>Find region boundaries of segmentation</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='superpixels' %}</p>
      </td>
      <td>
        <p>2-D superpixel oversegmentation of images</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='superpixels3' %}</p>
      </td>
      <td>
        <p>3-D superpixel oversegmentation of 3-D image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imoverlay' %}</p>
      </td>
      <td>
        <p>Burn binary mask into 2-D image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='label2idx' %}</p>
      </td>
      <td>
        <p>Convert label matrix to cell array of linear indices</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

### Image Transforms

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='bwdist' %}</p>
      </td>
      <td>
        <p>Distance transform of binary image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='bwdistgeodesic' %}</p>
      </td>
      <td>
        <p>Geodesic distance transform of binary image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='graydist' %}</p>
      </td>
      <td>
        <p>Gray-weighted distance transform of grayscale image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='hough' %}</p>
      </td>
      <td>
        <p>Hough transform</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='dct2' %}</p>
      </td>
      <td>
        <p>2-D discrete cosine transform</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='dctmtx' %}</p>
      </td>
      <td>
        <p>Discrete cosine transform matrix</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='fan2para' %}</p>
      </td>
      <td>
        <p>Convert fan-beam projections to parallel-beam</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='fanbeam' %}</p>
      </td>
      <td>
        <p>Fan-beam transform</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='idct2' %}</p>
      </td>
      <td>
        <p>2-D inverse discrete cosine transform</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='ifanbeam' %}</p>
      </td>
      <td>
        <p>Inverse fan-beam transform</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='iradon' %}</p>
      </td>
      <td>
        <p>Inverse Radon transform</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='para2fan' %}</p>
      </td>
      <td>
        <p>Convert parallel-beam projections to fan-beam</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='radon' %}</p>
      </td>
      <td>
        <p>Radon transform</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='matlab/ref' function='fft2' %}</p>
      </td>
      <td>
        <p>2-D fast Fourier transform</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='matlab/ref' function='fftshift' %}</p>
      </td>
      <td>
        <p>Shift zero-frequency component to center of spectrum</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='matlab/ref' function='ifft2' %}</p>
      </td>
      <td>
        <p>2-D inverse fast Fourier transform</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='matlab/ref' function='ifftshift' %}</p>
      </td>
      <td>
        <p>Inverse FFT shift</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

## 3D Volumetric Image Processing

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imboxfilt3' %}</p>
      </td>
      <td>
        <p>3-D box filtering of 3-D images</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imgaussfilt3' %}</p>
      </td>
      <td>
        <p>3-D Gaussian filtering of 3-D images</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imgradient3' %}</p>
      </td>
      <td>
        <p>Find 3-D gradient magnitude and direction of images</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imregdemons' %}</p>
      </td>
      <td>
        <p>Estimate displacement field that aligns two 2-D or 3-D images</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='integralboxfilter3' %}</p>
      </td>
      <td>
        <p>3-D box filtering of 3-D integral images</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='integralimage3' %}</p>
      </td>
      <td>
        <p>Calculate 3-D integral image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='medfilt3' %}</p>
      </td>
      <td>
        <p>3-D median filtering</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='superpixels3' %}</p>
      </td>
      <td>
        <p>3-D superpixel oversegmentation of 3-D image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imref3d' %}</p>
      </td>
      <td>
        <p>Reference 3-D image to world coordinates</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='affine3d' %}</p>
      </td>
      <td>
        <p>3-D Affine Geometric Transformation</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

## Code Generation

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='adaptthresh' %}</p>
      </td>
      <td>
        <p>Adaptive image threshold using local first-order statistics</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='boundarymask' %}</p>
      </td>
      <td>
        <p>Find region boundaries of segmentation</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='bwareaopen' %}</p>
      </td>
      <td>
        <p>Remove small objects from binary image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='bwboundaries' %}</p>
      </td>
      <td>
        <p>Trace region boundaries in binary image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='bwconncomp' %}</p>
      </td>
      <td>
        <p>Find connected components in binary image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='bwdist' %}</p>
      </td>
      <td>
        <p>Distance transform of binary image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='bweuler' %}</p>
      </td>
      <td>
        <p>Euler number of binary image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='bwlabel' %}</p>
      </td>
      <td>
        <p>Label connected components in 2-D binary image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='bwlookup' %}</p>
      </td>
      <td>
        <p>Nonlinear filtering using lookup tables</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='bwmorph' %}</p>
      </td>
      <td>
        <p>Morphological operations on binary images</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='bwpack' %}</p>
      </td>
      <td>
        <p>Pack binary image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='bwperim' %}</p>
      </td>
      <td>
        <p>Find perimeter of objects in binary image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='bwselect' %}</p>
      </td>
      <td>
        <p>Select objects in binary image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='bwtraceboundary' %}</p>
      </td>
      <td>
        <p>Trace object in binary image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='bwunpack' %}</p>
      </td>
      <td>
        <p>Unpack binary image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='conndef' %}</p>
      </td>
      <td>
        <p>Create connectivity array</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='demosaic' %}</p>
      </td>
      <td>
        <p>Convert Bayer pattern encoded image to truecolor image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='edge' %}</p>
      </td>
      <td>
        <p>Find edges in intensity image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='fitgeotrans' %}</p>
      </td>
      <td>
        <p>Fit geometric transformation to control point pairs</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='fspecial' %}</p>
      </td>
      <td>
        <p>Create predefined 2-D filter</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='getrangefromclass' %}</p>
      </td>
      <td>
        <p>Default display range of image based on its class</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='grayconnected' %}</p>
      </td>
      <td>
        <p>Select contiguous image region with similar gray values</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='histeq' %}</p>
      </td>
      <td>
        <p>Enhance contrast using histogram equalization</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='hough' %}</p>
      </td>
      <td>
        <p>Hough transform</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='houghlines' %}</p>
      </td>
      <td>
        <p>Extract line segments based on Hough transform</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='houghpeaks' %}</p>
      </td>
      <td>
        <p>Identify peaks in Hough transform</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='matlab/ref' function='hsv2rgb' %}</p>
      </td>
      <td>
        <p>Convert HSV colormap to RGB colormap</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='matlab/ref' function='im2double' %}</p>
      </td>
      <td>
        <p>Convert image to double precision</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='im2int16' %}</p>
      </td>
      <td>
        <p>Convert image to 16-bit signed integers</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='im2single' %}</p>
      </td>
      <td>
        <p>Convert image to single precision</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='im2uint16' %}</p>
      </td>
      <td>
        <p>Convert image to 16-bit unsigned integers</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='im2uint8' %}</p>
      </td>
      <td>
        <p>Convert image to 8-bit unsigned integers</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imabsdiff' %}</p>
      </td>
      <td>
        <p>Absolute difference of two images</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imadjust' %}</p>
      </td>
      <td>
        <p>Adjust image intensity values or colormap</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imbinarize' %}</p>
      </td>
      <td>
        <p>Binarize image by thresholding</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imbothat' %}</p>
      </td>
      <td>
        <p>Bottom-hat filtering</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imboxfilt' %}</p>
      </td>
      <td>
        <p>2-D box filtering of images</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imclearborder' %}</p>
      </td>
      <td>
        <p>Suppress light structures connected to image border</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imclose' %}</p>
      </td>
      <td>
        <p>Morphologically close image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imcomplement' %}</p>
      </td>
      <td>
        <p>Complement image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imcrop' %}</p>
      </td>
      <td>
        <p>Crop image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imdilate' %}</p>
      </td>
      <td>
        <p>Dilate image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imerode' %}</p>
      </td>
      <td>
        <p>Erode image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imextendedmax' %}</p>
      </td>
      <td>
        <p>Extended-maxima transform</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imextendedmin' %}</p>
      </td>
      <td>
        <p>Extended-minima transform</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imfill' %}</p>
      </td>
      <td>
        <p>Fill image regions and holes</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imfilter' %}</p>
      </td>
      <td>
        <p>N-D filtering of multidimensional images</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imfindcircles' %}</p>
      </td>
      <td>
        <p>Find circles using circular Hough transform</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imgaborfilt' %}</p>
      </td>
      <td>
        <p>Apply Gabor filter or set of filters to 2-D image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imgaussfilt' %}</p>
      </td>
      <td>
        <p>2-D Gaussian filtering of images</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imgradient3' %}</p>
      </td>
      <td>
        <p>Find 3-D gradient magnitude and direction of images</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imgradientxyz' %}</p>
      </td>
      <td>
        <p>Find the directional gradients of a 3-D image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imhist' %}</p>
      </td>
      <td>
        <p>Histogram of image data</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imhmax' %}</p>
      </td>
      <td>
        <p>H-maxima transform</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imhmin' %}</p>
      </td>
      <td>
        <p>H-minima transform</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imlincomb' %}</p>
      </td>
      <td>
        <p>Linear combination of images</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='immse' %}</p>
      </td>
      <td>
        <p>Mean-squared error</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imopen' %}</p>
      </td>
      <td>
        <p>Morphologically open image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imoverlay' %}</p>
      </td>
      <td>
        <p>Burn binary mask into 2-D image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='impyramid' %}</p>
      </td>
      <td>
        <p>Image pyramid reduction and expansion</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imquantize' %}</p>
      </td>
      <td>
        <p>Quantize image using specified quantization levels and output values</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='matlab/ref' function='imread' %}</p>
      </td>
      <td>
        <p>Read image from graphics file</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imreconstruct' %}</p>
      </td>
      <td>
        <p>Morphological reconstruction</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imregionalmax' %}</p>
      </td>
      <td>
        <p>Regional maxima</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imregionalmin' %}</p>
      </td>
      <td>
        <p>Regional minima</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imresize' %}</p>
      </td>
      <td>
        <p>Resize image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imrotate' %}</p>
      </td>
      <td>
        <p>Rotate image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imtophat' %}</p>
      </td>
      <td>
        <p>Top-hat filtering</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imtranslate' %}</p>
      </td>
      <td>
        <p>Translate image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imwarp' %}</p>
      </td>
      <td>
        <p>Apply geometric transformation to image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='integralboxfilter' %}</p>
      </td>
      <td>
        <p>2-D box filtering of integral images</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='integralimage' %}</p>
      </td>
      <td>
        <p>Calculate integral image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='intlut' %}</p>
      </td>
      <td>
        <p>Convert integer values using lookup table</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='iptcheckmap' %}</p>
      </td>
      <td>
        <p>Check validity of colormap</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='iptcheckconn' %}</p>
      </td>
      <td>
        <p>Check validity of connectivity argument</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='lab2rgb' %}</p>
      </td>
      <td>
        <p>Convert CIE 1976 L*a*b* to RGB</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='label2rgb' %}</p>
      </td>
      <td>
        <p>Convert label matrix into RGB image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='label2idx' %}</p>
      </td>
      <td>
        <p>Convert label matrix to cell array of linear indices</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='mean2' %}</p>
      </td>
      <td>
        <p>Average or mean of matrix elements</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='medfilt2' %}</p>
      </td>
      <td>
        <p>2-D median filtering</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='multithresh' %}</p>
      </td>
      <td>
        <p>Multilevel image thresholds using Otsu's method</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='ordfilt2' %}</p>
      </td>
      <td>
        <p>2-D order-statistic filtering</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='otsuthresh' %}</p>
      </td>
      <td>
        <p>Global histogram threshold using Otsu's method</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='padarray' %}</p>
      </td>
      <td>
        <p>Pad array</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='psnr' %}</p>
      </td>
      <td>
        <p>Peak Signal-to-Noise Ratio (PSNR)</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='regionprops' %}</p>
      </td>
      <td>
        <p>Measure properties of image regions</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='matlab/ref' function='rgb2gray' %}</p>
      </td>
      <td>
        <p>Convert RGB image or colormap to grayscale</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='matlab/ref' function='rgb2hsv' %}</p>
      </td>
      <td>
        <p>Convert RGB colormap to HSV colormap</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='rgb2lab' %}</p>
      </td>
      <td>
        <p>Convert RGB to CIE 1976 L*a*b*</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='rgb2ycbcr' %}</p>
      </td>
      <td>
        <p>Convert RGB color values to YCbCr color space</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='stretchlim' %}</p>
      </td>
      <td>
        <p>Find limits to contrast stretch image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='superpixels' %}</p>
      </td>
      <td>
        <p>2-D superpixel oversegmentation of images</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='superpixels3' %}</p>
      </td>
      <td>
        <p>3-D superpixel oversegmentation of 3-D image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='watershed' %}</p>
      </td>
      <td>
        <p>Watershed transform</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='ycbcr2rgb' %}</p>
      </td>
      <td>
        <p>Convert YCbCr color values to RGB color space</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imref2d' %}</p>
      </td>
      <td>
        <p>Reference 2-D image to world coordinates</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imref3d' %}</p>
      </td>
      <td>
        <p>Reference 3-D image to world coordinates</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='affine2d' %}</p>
      </td>
      <td>
        <p>2-D Affine Geometric Transformation</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='projective2d' %}</p>
      </td>
      <td>
        <p>2-D Projective Geometric Transformation</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='strel' %}</p>
      </td>
      <td>
        <p>Morphological structuring element</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='offsetstrel' %}</p>
      </td>
      <td>
        <p>Morphological offset structuring element</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

## GPU Computing

  <table>
{::nomarkdown}
  <tbody>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='bwdist' %}</p>
      </td>
      <td>
        <p>Distance transform of binary image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='bwlabel' %}</p>
      </td>
      <td>
        <p>Label connected components in 2-D binary image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='bwlookup' %}</p>
      </td>
      <td>
        <p>Nonlinear filtering using lookup tables</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='bwmorph' %}</p>
      </td>
      <td>
        <p>Morphological operations on binary images</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='corr2' %}</p>
      </td>
      <td>
        <p>2-D correlation coefficient</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='edge' %}</p>
      </td>
      <td>
        <p>Find edges in intensity image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='histeq' %}</p>
      </td>
      <td>
        <p>Enhance contrast using histogram equalization</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='matlab/ref' function='im2double' %}</p>
      </td>
      <td>
        <p>Convert image to double precision</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='im2single' %}</p>
      </td>
      <td>
        <p>Convert image to single precision</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='im2uint8' %}</p>
      </td>
      <td>
        <p>Convert image to 8-bit unsigned integers</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='im2uint16' %}</p>
      </td>
      <td>
        <p>Convert image to 16-bit unsigned integers</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imabsdiff' %}</p>
      </td>
      <td>
        <p>Absolute difference of two images</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imadjust' %}</p>
      </td>
      <td>
        <p>Adjust image intensity values or colormap</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imbothat' %}</p>
      </td>
      <td>
        <p>Bottom-hat filtering</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imclose' %}</p>
      </td>
      <td>
        <p>Morphologically close image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imcomplement' %}</p>
      </td>
      <td>
        <p>Complement image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imdilate' %}</p>
      </td>
      <td>
        <p>Dilate image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imerode' %}</p>
      </td>
      <td>
        <p>Erode image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imfill' %}</p>
      </td>
      <td>
        <p>Fill image regions and holes</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imfilter' %}</p>
      </td>
      <td>
        <p>N-D filtering of multidimensional images</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imgradient' %}</p>
      </td>
      <td>
        <p>Gradient magnitude and direction of an image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imgradientxy' %}</p>
      </td>
      <td>
        <p>Directional gradients of an image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imhist' %}</p>
      </td>
      <td>
        <p>Histogram of image data</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imlincomb' %}</p>
      </td>
      <td>
        <p>Linear combination of images</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imnoise' %}</p>
      </td>
      <td>
        <p>Add noise to image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='ycbcr2rgb' %}</p>
      </td>
      <td>
        <p>Convert YCbCr color values to RGB color space</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imopen' %}</p>
      </td>
      <td>
        <p>Morphologically open image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imreconstruct' %}</p>
      </td>
      <td>
        <p>Morphological reconstruction</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imregdemons' %}</p>
      </td>
      <td>
        <p>Estimate displacement field that aligns two 2-D or 3-D images</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imresize' %}</p>
      </td>
      <td>
        <p>Resize image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imrotate' %}</p>
      </td>
      <td>
        <p>Rotate image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imshow' %}</p>
      </td>
      <td>
        <p>Display image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='imtophat' %}</p>
      </td>
      <td>
        <p>Top-hat filtering</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='iradon' %}</p>
      </td>
      <td>
        <p>Inverse Radon transform</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='mat2gray' %}</p>
      </td>
      <td>
        <p>Convert matrix to grayscale image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='mean2' %}</p>
      </td>
      <td>
        <p>Average or mean of matrix elements</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='medfilt2' %}</p>
      </td>
      <td>
        <p>2-D median filtering</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='normxcorr2' %}</p>
      </td>
      <td>
        <p>Normalized 2-D cross-correlation</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='padarray' %}</p>
      </td>
      <td>
        <p>Pad array</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='radon' %}</p>
      </td>
      <td>
        <p>Radon transform</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='regionprops' %}</p>
      </td>
      <td>
        <p>Measure properties of image regions</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='matlab/ref' function='rgb2gray' %}</p>
      </td>
      <td>
        <p>Convert RGB image or colormap to grayscale</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='rgb2ycbcr' %}</p>
      </td>
      <td>
        <p>Convert RGB color values to YCbCr color space</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='std2' %}</p>
      </td>
      <td>
        <p>Standard deviation of matrix elements</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='stdfilt' %}</p>
      </td>
      <td>
        <p>Local standard deviation of image</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include matlab path='images/ref' function='stretchlim' %}</p>
      </td>
      <td>
        <p>Find limits to contrast stretch image</p>
      </td>
    </tr>
  </tbody>
{:/}
  </table>
