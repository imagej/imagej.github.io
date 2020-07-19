Ransac models used in the MTrack include the line and polynomial models to perform the determination of inliers. SInce the underlying process of Microtubule dynamics is a random walk process, in order to determine the inliers it is essential to choose a polynomial to determine the inliers from the length versus time plots. The user has the option of choosing either a second order or a third order polynomial regularized with a linear function. 

The regularization parameter determines how much linearity is present in the polynomial function used for the fitting.


* Polynomial model y = ax^3 + bx^2 + cx + d, would be the form of polynomial used to find the inliers with the coefficients determined via regression. Once the inliers have been found a line model is fit onto the inliers via regression.


* Line model y = cx + d, is the form of line model used to fit on the inliers to determine the growth and shrinkage rates.
