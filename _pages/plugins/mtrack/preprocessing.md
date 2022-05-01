---
mediawiki: Preprocessing(MTrack)
title: Preprocessing(MTrack)
---

If the original movie is not flat field corrected by the microscope, the program offers to do a pseudo-flat field correction by applying a Gaussian of radius a twentieth the size of the image and subtracting it from the original image to create a preprocessed movie which would be used for tracking.

Please note that the preprocessed movie is only used for tracking and not for doing sub-pixel localization which is done on the original movie only.

The user can also choose to apply a median filter of a certain user chosen radius on the movie.

If the user chooses to upload their own preprocessed movie they can do so and upload it using the "Load preprocessed movie option".

To do a pseudo-flat field correction in Fiji the user has to do the following steps:

-   Open movie and duplicate it by selecting {% include bc path='Image|Duplicate|Duplicate Stack'%}.

<!-- -->

-   Apply a Gaussian blur on the duplicated movie by selecting {% include bc path='Process|Filters|Gaussian Blur'%}.

The radius should be around a tenth or a twentieth of the size of the image. For example if the image is 512 by 512 pixels, the blur radius would be 25-50.

-   Subtract the blurred movie from the original movie by selecting {% include bc path='Process|Image Calculator'%}.

In this menu choose Image 1 (original) and Image 2 (blurred). The operation to be chosen in the menu is "Subtract" and check the box "Create new window". This operation opens a new stack of flat field corrected images.

-   Finally, enhance the edges of the microtubules by applying a median filter. Select {% include bc path='Process| Filters | Median FIlter'%} and enter the radius of 1 or 2 pixels.
-   Save the pre-processed movie to be uploaded into the tracker.
