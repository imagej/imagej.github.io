---
mediawiki: Sub-pixel_localization_parameter_selection
title: Sub-pixel localization parameter selection
---

<img src="/media/plugins/mtrack/modelchoice.png" width="800"/>

The first choice the users see in the panel is regarding the model to be used for performing the sub-pixel Localization with. If the microtubules grow only linearly and do not bend just a linear growth model is sufficient to track the growth of such microtubules. If the microtubules only just bend like a beam then a beam model is sufficient to track them. The most advanced model here, the higher order beam mode, takes into account some more complicated microtubule bending actions and is recommended as the default model to be used during the tracking.

The user also has the option of doing Gaussian mask fits after optimization to further improve the localization accuracy of the tracker and if they want to see the tracks superimposed on individual microtubules, they can select the displayroi stack option.

For the model parameters itself the parameters that can be changed include initial guess for the minimum pixel intensity as a ratio of the maximum intensity along the microtubule, this helps the optimizer recognize the pixels that should be considered as belonging to the microtubule in terms of a percent of the maximum intensity.

Other model parameter is the initial spacing between the Gaussians which make up the model, the number entered is the percentage of the min(sigmaX, sigmaY) of the PSF of the microscope.

Furthermore the parameter of maximum direction change caps the maximum direction change, it can happen that during the collisions the optimizer makes a mistake in doing the assignment of the growing end of the microtubule, this would be recognized by the program as an angular change of more than this preset value and for that time frame no assignment of end points would be done.

The parameter of number of Gaussians are the number of Gaussians used to make the mask that is then fitted to the growing ends after optimization is performed, in our experience 2 Gaussian mask fits work best for noisy images and if the signal to noise ratio is high then even 3 Gaussians can be used to do this fitting.
