= Introduction =
The following [[Beanshell_Scripting|Beanshell script]] allows you to evaluate the performance of your [[:Category:Segmentation|segmentation]] method after thinning the borders of the image segments to 1-pixel width.

Retrospective evaluation of the original [http://brainiac2.mit.edu/isbi_challenge/ ISBI-2012 segmentation challenge] scoring system revealed that it was not sufficiently robust to variations in the widths of neurite borders. After evaluating all of these metrics and associated variants, it was found that specially normalized versions of the [[Rand error]] and [https://en.wikipedia.org/wiki/Variation_of_information Variation of Information] best matched our qualitative judgements of segmentation quality:

*Foreground-restricted Rand Scoring after border thinning: V<sup>Rand</sup><sub>(thinned)</sub>
*Foreground-restricted Information Theoretic Scoring after border thinning: V<sup>Info</sup><sub>(thinned)</sub>

'''This script calculates the best V<sup>Rand</sup><sub>(thinned)</sub> and V<sup>Info</sup><sub>(thinned)</sub> over a set of threshold values of the input image (proposed segmentation).''' The proposed labels can be either binary or a probability image ([0.0-1.0] values).

Further details about the metrics can be found in the [http://journal.frontiersin.org/article/10.3389/fnana.2015.00142/abstract challenge publication].

= Use =
Just copy/paste it in the [[Script Editor]] or save it into a .bsh file and run it ({{bc | File | Open}}):

<source lang=java>
/**
 * Script to calculate the segmentation error between some 2D 
 * original (binary) labels and their corresponding proposed labels (binary or
 * probability -0-1- values).
 * 
 * The evaluation metrics are:
 *  - Maximal foreground-restricted Rand score after thinning
 *  - Maximal foreground-restricted information theoretic score after thinning
 * 
 * These are the final official metrics for the ISBI-2012 challenge
 * on segmentation of neuronal structures in EM stacks (http://brainiac2.mit.edu/isbi_challenge/).
  * 
 * @author Ignacio Arganda-Carreras (ignacio.arganda@ehu.eus)
 * @version January 12, 2016
 */
  
import trainableSegmentation.metrics.*;
import ij.WindowManager;
import ij.gui.GenericDialog;
import ij.IJ;
  
// Get the list of images that are open
ids = WindowManager.getIDList();
  
if ( ids == null || ids.length < 2 )
{
    IJ.showMessage( "You should have at least two images open." );
    return;
}
  
// Get all the titles of the open images        
titles = new String[ ids.length ];
for ( int i = 0; i < ids.length; ++i )
{
    titles[ i ] = ( WindowManager.getImage( ids[ i ] ) ).getTitle();
}
  
// Create dialog        
gd = new GenericDialog( "Evaluate segmentation results" );
          
gd.addMessage( "Image Selection:" );
current = WindowManager.getCurrentImage().getTitle();
gd.addChoice( "Original_labels", titles, current );
gd.addChoice( "Proposal", titles, current.equals( titles[ 0 ] ) ? titles[ 1 ] : titles[ 0 ] );
          
gd.addMessage( "Segmentation error metrics:" );
gd.addCheckbox( "Maximal foreground-restricted Rand score after thinning", true );
gd.addCheckbox( "Maximal foreground-restricted information theoretic score after thinning", true );

gd.addMessage( "Data selection:" );
gd.addCheckbox( "Binary proposal", false );
 
gd.showDialog();
          
if (gd.wasCanceled()) 
    return;
          
originalLabels = WindowManager.getImage( ids[ gd.getNextChoiceIndex() ] );
proposedLabels = WindowManager.getImage( ids[ gd.getNextChoiceIndex() ] );
  
calculateVRandAfterThinning = gd.getNextBoolean();
calculateVInfoAfterThinning = gd.getNextBoolean();

binaryProposal = gd.getNextBoolean();
  
IJ.log("---");
IJ.log("Evaluating segmentation...");
IJ.log("  Original labels: " + originalLabels.getTitle());
IJ.log("  Proposed labels: " + proposedLabels.getTitle() + "\n");

// Calculate segmentation error with the selected metrics
  
if( calculateVRandAfterThinning )
{   
    IJ.log("\nCalculating maximal foreground-restricted Rand score after thinning...");
    metric = new RandError( originalLabels, proposedLabels );
    maxThres = binaryProposal ? 0.0 : 1.0;
    maxScore = metric.getMaximalVRandAfterThinning( 0.0, maxThres, 0.1, true );  
    IJ.log("  Maximum foreground-restricted Rand score after thinning: " + maxScore );     
}

if( calculateVInfoAfterThinning )
{   
    IJ.log("\nCalculating maximal foreground-restricted information theoretic score after thinning...");
    metric = new VariationOfInformation( originalLabels, proposedLabels );
    maxThres = binaryProposal ? 0.0 : 1.0;
    maxScore = metric.getMaximalVInfoAfterThinning( 0.0, maxThres, 0.1 );  
    IJ.log("  Maximum foreground-restricted information theoretic score after thinning: " + maxScore );     
}
</source>

If you run it while two images are open, the following dialog will pop up:

[[Image:Script-segmentation-evaluation-thinning-dialog.png]]

Here you can select among the open images which ones are the original and the proposed labels, along with the specific metrics you want to apply to evaluate the segmentation results. If the proposed labels are binary (not a probability image) then you can click on "Binary proposal" to avoid using many threshold values.

After clicking OK the metrics will be applied and the results will be shown in the Log window:

[[Image:Script-segmentation-evaluation-thinning-log.png]]

= References =
* Ignacio Arganda-Carreras, Srinivas C. Turaga, Daniel R. Berger, Dan Ciresan, Alessandro Giusti, Luca M. Gambardella, Jürgen Schmidhuber, Dmtry Laptev, Sarversh Dwivedi, Joachim M. Buhmann, Ting Liu, Mojtaba Seyedhosseini, Tolga Tasdizen, Lee Kamentsky, Radim Burget, Vaclav Uher, Xiao Tan, Chanming Sun, Tuan D. Pham, Eran Bas, Mustafa G. Uzunbas, Albert Cardona, Johannes Schindelin, and H. Sebastian Seung. [http://journal.frontiersin.org/article/10.3389/fnana.2015.00142/abstract Crowdsourcing the creation of image segmentation algorithms for connectomics]. Frontiers in Neuroanatomy, vol. 9, no. 142, 2015.

[[Category:Segmentation]]
[[Category:Scripting]]
