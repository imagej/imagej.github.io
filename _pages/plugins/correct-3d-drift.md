---
mediawiki: Correct_3D_Drift
title: Correct 3D Drift
project: /software/fiji
categories: [Registration]
artifact: sc.fiji:Correct_3D_Drift
---

This Fiji menu command is implemented by the script {% include github org='fiji' repo='Correct_3D_Drift' branch='master' path='src/main/resources/scripts/Plugins/Registration/Correct_3D_drift.py' label='Correct_3D_Drift.py' %}.

1.  The script expects the currently open and active image to be a hyperstack (or virtual hyperstack) consisting of 2D or 3D volumes over time. The script registers the time points to each other using the phase correlation implementation of [ImgLib 1](/libs/imglib1).
2.  Once implemented a dialogue box will request the use to select the color channel to use for registration.
3.  If memory is limiting on the system then the user can select to use a virtualstack for the result.
4.  If a virtualstack is selected the a folder save the aligned stack to needs to be selected.
5.  After some processing (there are progress bars), the resulting, registered volumes are opened. If a virtualstack was selected the registered volume will already be saved in the chosen target folder.

The script was originally written by {% include person id='acardona' %} and [Robert Bryson-Richardson](http://monash.edu/science/about/schools/biological-sciences/staff/bryson-richardson/) while attending the [Developmental Imaging EMBO course](http://cwp.embo.org/pc10-37/) organized by [Gabriel](http://www.igc.gulbenkian.pt/research/photo/556/) [G. Martins](http://www.igc.gulbenkian.pt/research/unit/51).

## Publication

-   [Parslow A, Cardona A and Bryson-Richardson RJ (2014) Sample drift correction following 4D confocal time-lapse imaging. J Vis Exp. 2014 Apr 12;(86). doi: 10.3791/51086](http://http://www.jove.com/video/51086/sample-drift-correction-following-4d-confocal-time-lapse-imaging).
