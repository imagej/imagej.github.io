---
mediawiki: Colour_Deconvolution
title: Colour Deconvolution
project: /software/fiji
categories: [Color Processing]
artifact: sc.fiji:Colour_Deconvolution
---

Similarly to the command {% include bc path='Image | Color | RGB split' %}, this plugin unmixes an RGB image produced by subtractive mixing (inks, histological dyes) into separate channels corresponding to up to 3 determined colors. This is useful e.g. to do pigment separation.

## Documentation

See [Gabriel Landini webpage](https://blog.bham.ac.uk/intellimic/g-landini-software/colour-deconvolution-2/) for an updated version of the plugin.
You can install an updated version in Fiji via the Colour Deconvolutio2 update site.

This plugin implements the method described in the following paper:

{% include citation last='Ruifrok' first='A.C.' last2='Johnston' first2='D.A.' title='Quantification of histochemical staining by color deconvolution' journal='Anal. Quant. Cytol. Histol.' volume='23' pages='291-299' year='2001' PMID='11531144' %} <!-- TODO: No doi for this article. Decide whether to hardcode AMA style, or do something fancier. -->

## Version history

-   30/Mar/2004 released - based on macro code from A.C. Ruifrok.
-   03/Apr/2004 resolved ROI exiting
-   07/Apr/2004 added Methyl Green DAB vectors
-   08/Jul/2004 shortened the code
-   01/Aug/2005 added fast red/blue/DAB vectors
-   02/Nov/2005 changed code to work with image stacks (DLC - dchao at fhcrc org)
-   02/Nov/2005 changed field names so user-defined colours can be set within macros (DLC - dchao at fhcrc org)
-   04/Feb/2007 1.3 disable popup menu when right clicking
-   23/May/2009 added Feulgen-light green vectors
-   14/Apr/2010 v 1.4 added Giemsa vector (Methylene blue & eosin). The images are now names "title"-(Colour\_1) etc so there are not clash of names when using \[ \]. The log window now prints the java code of the translation matrix to include new vectors in the plugin. Added "Hide legend" option.
-   22/Jun/2010 v 1.5 added Masson Trichrome vector (Methyl blue & Ponceau Fuchsin only (this does not have Iron Haematoxylin vector!). Fixed bug: check for 0 components before hiding legend (otherwise there was no image shown if legend hidden)
-   26/Mar/2011 v.1.6 added Brilliant\_Blue stain.
-   03/Aug/2011 v1.7 added progress bar (thanks to Oskari Jaaskelainen), added warning about immunostains.
-   17/Oct/2015 v 1.8 B. Pavie refactorized the code into multiple classes and made some public method to generate the result ImageStacks without displaying them so it can be called from scripts.

## Menu path

{% include bc path='Image | Color | Colour Deconvolution'%}
