---
title: 2009-12-23 - ImageJ development discussion
---

Recently there has been a large amount of discussion about ImageJ development. This dialogue has been great, but in a few cases similar points have been sprinkled across several different threads. We have filtered through the recent threads of interest (within the past 2-3 months) and have identified a few key topics. To better organize the discussion, we are creating new threads, one per topic, and sending each to the appropriate mailing list:

-   ImageJ for discussion in which non-programmers have expressed substantial interest
-   ImageJX for highly technical discussion regarding software engineering (technologies, source code, etc.)

The threads we are sending to the [ImageJ users list](https://imagej.net/ij/list.html) are:

1.  [**Backwards compatibility**](https://list.nih.gov/cgi-bin/wa.exe?A2=IMAGEJ;78ecf36e.0912) – What does "near 100% backwards compatibility" mean? And is it a reasonable, warranted goal?
2.  [**ImageJ project structure**](https://list.nih.gov/cgi-bin/wa.exe?A2=IMAGEJ;ff078265.0912) – What are ImageJ, Fiji, ImageJX and ImageJDev, and how are they related? What about project forks? How can people contribute?
3.  [**ImageJDev.org website**](https://list.nih.gov/cgi-bin/wa.exe?A2=IMAGEJ;cf12215d.0912) – What is the role of this website? How can we improve it?
4.  [**ImageJ mailing lists**](https://list.nih.gov/cgi-bin/wa.exe?A2=IMAGEJ;a5b07f4c.0912) – There are an increasing number of ImageJ-related mailing lists. Are they all useful and necessary? Do we need any additional lists?
5.  [**Scripting languages and API**](https://list.nih.gov/cgi-bin/wa.exe?A2=IMAGEJ;8c622001.0912) – Some people want ImageJ to support several different scripting languages based on a common underlying API, while others argue for a single, easy to learn macro language. What the pros and cons of each approach?

And the threads for [ImageJX](https://groups.google.com/g/imagejx):

1.  **[Image data types](https://groups.google.com/g/imagejx/c/lD4s32M5als?pli=1)** – Images are typically represented with a "data type" such as 8-bit unsigned integer, 32-bit floating point, etc. How can we allow developers to write image processing routines without worrying about data types? And what is the best way to generically support new data types (e.g., complex numbers)? Scala @specialized tags?
2.  **[Coordinate systems](https://groups.google.com/g/imagejx/c/_yaczl4UWK4)** – Image data in some scientific domains (e.g., astronomy) can have domain sets more complex than evenly spaced rectangular grids. Should we work to support these sorts of data?
3.  **[Separation of concerns (MVC, AWT/Swing/etc.)](https://groups.google.com/g/imagejx/c/gz7cgytSRuA)** – Can we fully decouple the ImageJ user interface from its data structures? Why do we want to?
4.  **[Plugins infrastructure](https://groups.google.com/g/imagejx/c/F3gWc_Ndz_U)** – Multiple proposals have been presented for enhancing the plugin model—e.g., allowing for explicit declaration of input and output types to more easily chain plugins into a workflow. Some have even suggested eliminating the idea of "plugins" entirely (as opposed to scripts/macros). Various frameworks also exist to facilitate data processing workflows (e.g., KNIME and Cell Profiler)—what can we learn from them, and does it make sense to integrate? OSGi?
5.  **[Performance](https://groups.google.com/g/imagejx/c/ox2ooizORA4)** – How can we improve ImageJ's algorithmic performance? Language translation? Performance packs? OpenCL?

Please reply on whichever threads are of interest to you. {% include person id='ctrueden' %} will be on holiday for the rest of the year, but will be back before January 7th, and will try to chime in as time allows. Hopefully this great dialogue will continue as we all refine the roadmap for ImageJ over the next few weeks and months!

 
