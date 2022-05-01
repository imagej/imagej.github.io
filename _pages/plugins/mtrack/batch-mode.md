---
mediawiki: Batch_mode(MTrack)
title: Batch mode(MTrack)
---

If the user has run the program in either simple or advanced mode and chosen to save the set of parameters, they can run the program in batch mode for those movies which have similar intensity profiles of the microtubules and similar signal to noise ratio. In this mode the user has to select a directory of movies they want to be tracked, the program then executes all the choices the user made for their run in simple or advanced mode on its own.

By default it starts a parallel run of the number of movies equal to the number of CPU cores, so if the user had 10 movies and 4 CPU cores then tracking for 4 movies would be started at the same time and only after a movie gets completely tracked is the next movie in the queue loaded for the tracking module.
