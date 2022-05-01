---
mediawiki: Downsample
title: Downsample
---

Gaussian downsampling of an image with ImageJ on-board tools.

## Motivation

Sound downsampling of an image requires the elimination of image frequencies higher than half the sampling frequency in the result image (see the {% include wikipedia title='Nyquist%E2%80%93Shannon sampling theorem' text='Nyquist–Shannon sampling theorem'%}). The exclusive tool for this is {% include wikipedia title='Gaussian function' text='Gaussian convolution'%}.

## Download

Get a snapshot from the git repository here: [downsample\_.js](https://github.com/fiji/fiji/blob/master/plugins/Examples/downsample_.js).

## Documentation

This script calculates the required Gaussian kernel for a given target **width** or **height**, smooths the image and resamples it. The target size must be smaller than the source image size.

Furthermore, you can define the "intrinsic" Gaussian kernel of the source and target images. An optimal sampler is identified by sigma=0.5. If your source image was blurred already, you may set a higher **source sigma** for a sharper result. Setting **target sigma** to values smaller than 0.5 makes the result appear sharper and therefore eventually aliased.

This script is maintained by Stephan Saalfeld.

## Example

A picture is worth a thousand words, so here is an example. You see a 2,048×2,048px transmission electron micrograph downsampled to 100×100px. For better illustration, the examples are shown at 200%.

{% include img style="display:inline-block; margin-right:1em" src="downsample-imagej.png" caption="ImageJ interpolated scaling" %}
{% include img style="display:inline-block; margin-right:1em" src="downsample-ts-0.25.png" caption="Gaussian downsampling with target sigma=0.25" %}
{% include img style="display:inline-block" src="downsample-ts-0.5.png" caption="Gaussian downsampling with target sigma=0.5" %}

## Code

```javascript
/**
 * Gaussian downsampling of an image with ImageJ on-board tools.
 *
 * Motivation:
 * Sound downsampling of an image requires the elimination of image frequencies
 * higher than half the sampling frequency in the result image (see the
 * Nyquist-Shannon sampling theorem).  The exclusive tool for this is Gaussian
 * convolution.
 *
 * This script calculates the required Gaussian kernel for a given target size,
 * smoothes the image and resamples it.
 *
 * Furthermore, you can define the "intrinsic" Gaussian kernel of the source and
 * target images.  An optimal sampler is identified by sigma=0.5.  If your
 * source image was blurred already, you may set a higher source sigma for a
 * sharper result.  Setting target sigma to values smaller than 0.5 makes the
 * result appear sharper and therefore eventually aliased.
 */
var imp = WindowManager.getCurrentImage();
var width = 0;
var height = 0;
var sourceSigma = 0.5;
var targetSigma = 0.5;
var widthField;
var heightField;
var fieldWithFocus;

var textListener = new java.awt.event.TextListener(
  {
    textValueChanged : function( e )
    {
      var source = e.getSource();
      var newWidth = Math.round( widthField.getText() );
      var newHeight = Math.round( heightField.getText() );
      
      if ( source == widthField && fieldWithFocus == widthField && newWidth )
      {
        newHeight = Math.round( newWidth * imp.getHeight() / imp.getWidth() );
        heightField.setText( newHeight );
      }
      else if ( source == heightField && fieldWithFocus == heightField && newHeight )
      {
        newWidth = Math.round( newHeight * imp.getWidth() / imp.getHeight() );
        widthField.setText( newWidth );
      }
    } 
  } );

var focusListener = new java.awt.event.FocusListener(
  {
    focusGained : function ( e )
    {
      fieldWithFocus = e.getSource();
    },
    focusLost : function( e ){} 
  } );

if ( imp )
{
  width = imp.getWidth();
  height = imp.getHeight();
  
  gd = new GenericDialog( "Downsample" );
  gd.addNumericField( "width :", width, 0 );
  gd.addNumericField( "height :", height, 0 );
  gd.addNumericField( "source sigma :", sourceSigma, 2 );
  gd.addNumericField( "target sigma :", targetSigma, 2 );
  gd.addCheckbox( "keep source image", true );
  var fields = gd.getNumericFields();
  
  widthField = fields.get( 0 );
  heightField = fields.get( 1 );
  fieldWithFocus = widthField;
  
  widthField.addFocusListener( focusListener );
  widthField.addTextListener( textListener );
  heightField.addFocusListener( focusListener );
  heightField.addTextListener( textListener );
    
  gd.showDialog();
  if ( gd.wasOKed() )
  {
    width = gd.getNextNumber();
    height = gd.getNextNumber();
    sourceSigma = gd.getNextNumber();
    targetSigma = gd.getNextNumber();
    keepSource = gd.getNextBoolean();
    
    if ( width <= imp.getWidth() )
    {
      var s;
      if ( fieldWithFocus == widthField )
        s = targetSigma * imp.getWidth() / width;
      else
        s = targetSigma * imp.getHeight() / height;
      
      if ( keepSource )
        IJ.run( "Duplicate...", "title=" + imp.getTitle() + " duplicate" );
      IJ.run( "Gaussian Blur...", "sigma=" + Math.sqrt( s * s - sourceSigma * sourceSigma ) + " stack" );
      IJ.run( "Scale...", "x=- y=- width=" + width + " height=" + height + " process title=- interpolation=None" );
      IJ.run( "Canvas Size...", "width=" + width + " height=" + height + " position=Center" );
    }
    else
      IJ.showMessage( "You try to upsample the image.  You need an interpolator for that not a downsampler." );
  }
}
else
  IJ.showMessage( "You should have at least one image open." );
```

## See also

-   [Javascript Scripting](/scripting/javascript)
-   [Scripting Help](/scripting)
-   [Scripting\_comparisons](/scripting/comparisons)


