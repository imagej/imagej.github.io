---
mediawiki: Super_Sloppy_Surface_Reconstruction
title: Super Sloppy Surface Reconstruction
---

Super sloppy surface reconstruction from planetary surface photographs or {% include wikipedia title='Scanning electron microscope' text='Scanning Electron Micrographs (SEM)'%}.

## Motivation

Sometimes, you have a picture of a surface and you want to see how it looks in 3-D. If your picture meets a few requirements, then reconstruction of an approximation of this surface is possible and, indeed, very simple. These requirements are:

-   The surface has no variance in illumination and color (like in SEM where everything is gold or at the moon where everything is cheese).
-   The surface is illuminated by a single parallel light-source from the left (rotate it if it comes from a different side).
-   The light-source illuminates the surface from an angle steeper or as steep as the steepest slope at the surface (that means: no shadows).
-   There is no occlusion of objects.

If these requirements are met, your picture is an arbitrarily scaled <em>x</em>-gradient of your surface. That is, integrating it alongside <em>x</em> will give you the surface at an arbitrary scale.

## Example

See here a photograph of the [lunar crater Hohmann](http://commons.wikimedia.org/wiki/File:Hohmann_crater.png) original, integrated, and rendered as a [3D Surface Plot](/plugins/3d-surface-plot).

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td>
        <p>style="vertical-align:top" |{% include thumbnail src='/media/tutorials/hohmann-crater.jpg' title='Original image'%}</p>
      </td>
      <td>
        <p>style="vertical-align:top" |{% include thumbnail src='/media/tutorials/hohmann-crater-xintegral.jpg' title='Integral in <em>x</em>'%}</p>
      </td>
      <td>
        <p>style="vertical-align:top" |{% include thumbnail src='/media/tutorials/hohmann-crater-surfaceplot.jpg' title='3D Surface Plot'%}</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

## Shortcomings

-   The approach is very sensitive to noise. Noise will result in a stripy pattern, because it is accumulated independently for each pixel row.
-   Lacking the constant initializer for integration, we assume that the average height for all pixel rows is equal and that the average slope per row is 0. Rows with a large mountain without a compensating valley will thus appear lower than they should.

## Code

This is BeanShell and can be executed via [Script Editor](/scripting/script-editor) or [BeanShell Interpreter](/scripting/interpreter) or by dragging it as a file with extension \`.bsh' into the Fiji toolbar. This script performs per-pixel operations in an interpreted language and, therefore, is very slow. If you really need more speed, compile the source into a Java class which is straight forward for BeanShell code.

    import ij.*;
    import ij.process.*;

    float mean( FloatProcessor source, int first, int last ) {
        double sum = 0;
        for ( int i = first; i < last; ++i )
            sum += source.getf( i );
        return ( float )( sum / ( last - first ) );
    }

    /** source and target are assumed to have identical dimensions. */
    void integrateRow( FloatProcessor source, FloatProcessor target, int row ) {
        final int first = row * source.getWidth();
        final int last = first + source.getWidth();
        final float dxMean = mean( source, first, last );
        
        /* integrate */
        double x = 0;
        double xMean = 0;
        for ( int i = first; i < last; ++i ) {
            final float dx = source.getf( i );
            x += dx - dxMean;
            target.setf( i, ( float )x );
            xMean += x;
        }
        xMean /= last - first;
        
        /* normalize */
        for ( int i = first; i < last; ++i )
            target.setf( i, target.getf( i ) - ( float )xMean );    
    }

    ImagePlus impSource = IJ.getImage();
    FloatProcessor source = impSource.getProcessor().convertToFloat();
    FloatProcessor target = new FloatProcessor( source.getWidth(), source.getHeight() );
    ImagePlus impTarget = new ImagePlus( "I " + impSource.getTitle(), target );
    impTarget.show();

    for ( int i = 0; i < source.getHeight(); ++i ) {
        integrateRow( source, target, i );
        impTarget.updateAndDraw();  
    }

## See also

-   [Scripting Help](/scripting)
-   [Scripting\_comparisons](/scripting/comparisons)
-   [Script Editor](/scripting/script-editor)


