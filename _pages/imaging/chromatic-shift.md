---
title: Chromatic shift origins, measurement and correction
description: How chromatic shift arrises in a microscope, how to measure it and correct an image with a chromatic shift.
categories: [Colocalization,Tutorials]
section: Imaging
nav-links: true
nav-title: Chromatic Shift
---

For fluorescence images from optical microscopes, from a colocalization perspective....

1.  Objective lenses are never perfect, not even really expensive ones that claim multi color chromatic correction. When imaging diffraction limited objects with an eg. 1.4 NA lens on a widefield/confocal/SPIM/super resolution system there will still be a unique colour shift in all three spatial dimensions, xyz, for that particular lens/opics combination, and even for what angle it is screwed into the stand.
2.  Also, the alignment of the fluorescence filters in different cubes might bend different channels to slightly different places on the detector. On the API OMX you can even adjust this... normally its fixed on most systems but might also be tweakable.
3.  Olympus does all the chromatic correction in the lens, but others do some in the tube lens.
    
    1.  This is why its not a good idea to screw a Zeiss c-apochromat 100x 1.4 oil into an Olympus stand.
4.  So we are left with a systematic error that can be measured, actually to a precision of 10s of nm by Gaussian fitting bead images, or some other calibration sample (like you do in PALM/STORM type super resolution and single molecule tracking. )
5.  On a single point scanning confocal the matter can be made worse by the more complicated optics.
    
    1.  The Zeiss 510 has a different pinhole per channel... and depending on their positions and correct setup, the images of the bead in different channels is also affected by pinhole position settings.
6.  Nowadays with the Zeiss 7xx, 8xx series and on the Olympus FV1000 and other modern point scanners there is only 1 pinhole for the emission light, so that problem is suppressed.
7.  BUT, the 405 lasers come in through a different fibre than the Vis lasers.. and so there is a collimation adjustment to make
8.  Same for 2photon lasers.... getting the near UV and IR laser spots to coincide exactly with the visible lines is hard...
9.  So its best to get is as close as is reasonably possible to do in hardware adjustments, then measure the residual error then correct for it.
10. There always remain measurable errors (unless you were really really lucky and happen to have a perfect lens, which is a 1 in a 1000 chance at best, plus perfectly aligned fluorescence mirrors/filters)
11. OK, so at the simple level, we can assume that the whole field of view is shifted by some 3D shift per channel compared to the reference, usually green channel (ignoring any geometrical distortions or different magnifications or image rotations for different colours.)
    
    1.  So if we measure a few 1 or 0.5 or so micron beads (no need to use tiny beads here) near the centre of the field of view (where optics are best) we can calculate or guestimate the center of mass of the bead images in each colour channel, and work out the shift vectors needed.
    2.  These will be between 10-1000 nm in xy and up to 500 or even 2000 micron in z.
    3.  BUT, they will never be whole xy pixels or z slice shifts... forget that idea its too crude.
    4.  see the 2 slides titled "Check with multi-colour beads" at [Colocalization analysis course notes](https://www.biodip.de/w/images/f/fa/QuantitativeColocAnalysis-10-2011.pdf)
12. How to measure the colour channel shift systematic error?
    
    1.  [psfJ](https://github.com/cmongis/psfj) from Knop lab can make the measurement.
    2.  Use imageJ to do gaussian fits of the bead images and find the shidsts in x y and z.
13. Now we can use software to fix this systematic error by shifting one image colour channel relative to the other.
    
    1.  Erik M's TransformJ Translate plugin in Fiji/ImageJ can do a sub pixel resolution shift for for each channel, as we have measured those shifts [TransformJ Translate](https://imagescience.org/meijering/software/transformj/translate/)
    2.  Use a nice interpolation method to avoid smashing the information in your images - eg quintic B-spline interpolation
    3.  Or one could imagine a Fourier based method... (using a phase shift?) The Fiji \[Stitching\_2D/3D\]\] plugin contains stuff that might do this but its not exposed in the GUIs... so scripting would be required there?
14. Moving the images using a whole pixel or z plane shift will not be precise enough for high resolution colocalization analysis.
15. At a higher level there may also be a magnification difference between the different colour channels.
    
    1.  Further, On multi camera systems, like OMX or some HCS system there WILL be a rotation angle difference between the channel images.
    2.  The [TransformJ Affine plugin](https://imagescience.org/meijering/software/transformj/affine/) might do the job, which can also expand or shrink the image to accommodate different magnification as well as shift and rotation.
16. Even worse could be a non linear warp of the image that is different per channel.
    
    1.  Eg using a fancy beam splitter, dual view, W-view etc. gadget for dual camera imaging.
    2.  Again these are measurable and fixable with some effort, eg using bUnwarpJ
17. So depending how precise you need to be, over how large a field of view... the difficulty of the correction varies.
18. We could add this kind of colour shift correction to the new Coloc\_2 plugin... by reusing TransformJ and maybe also bUnwarpJ. Any takers?
