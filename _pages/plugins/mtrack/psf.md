---
mediawiki: More_explanation
title: More explanation
---

Point spread function or the PSF is estimated by fitting Gaussian function to the bead images. In our case we only need 2D bead images as the microtubules imaged are in 2 dimension. The mathematical form of the Gaussian used in the program is exp\[-(x - ux)/sx^2 - (y-uy)/sy^2\], here ux and uy are the mean of the 2D Gaussian and sx, sy are the sigmaX and sigmaY of the 2D Gaussian. MTrack takes as input the sx and sy as defined in the form of the 2D gaussian above.
