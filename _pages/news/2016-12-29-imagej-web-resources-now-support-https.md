---
title: 2016-12-29 - ImageJ web resources now support HTTPS
---

Over the past many months, we have been incrementally working toward support for HTTPS (i.e., secure) web traffic for ImageJ's web-based resources. At the [recent hackathon at MPI-CBG](/news/2016-12-20-fiji-knip-hackathon), we largely completed these efforts. Some of the domains which now fully support HTTPS include:

- [https://imagej.net/](https://imagej.net/)
- [https://downloads.imagej.net/](https://downloads.imagej.net/)
- [https://javadoc.imagej.net/](https://javadoc.imagej.net/)
- [https://jenkins.imagej.net/](https://jenkins.imagej.net/)
- [https://maven.imagej.net/](https://maven.imagej.net/)
- [https://mirror.imagej.net/](https://mirror.imagej.net/)
- [https://search.imagej.net/](https://search.imagej.net/)
- [https://sites.imagej.net/](https://sites.imagej.net/)
- [https://status.imagej.net/](https://status.imagej.net/)
- [https://update.imagej.net/](https://update.imagej.net/)
- [https://wsr.imagej.net/](https://wsr.imagej.net/)
- [https://fiji.sc/](https://fiji.sc/)
- [https://samples.fiji.sc/](https://samples.fiji.sc/)
- [https://update.fiji.sc/](https://update.fiji.sc/)

More work is still needed to make the [ImageJ Updater](/plugins/updater) always prefer talking to update sites via HTTPS rather than HTTP; see [the relevant forum thread](http://forum.imagej.net/t/https-to-make-imagej-fiji-more-secure/398) for further details.

This work will make ImageJ and Fiji more secure, preventing potential man-in-the-middle attacks and arbitrary code injection.

 
