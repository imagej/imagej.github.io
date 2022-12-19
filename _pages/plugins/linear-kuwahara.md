---
mediawiki: Linear_Kuwahara
title: Linear Kuwahara
project: /software/fiji
categories: [Tutorials]
artifact: sc.fiji:Linear_Kuwahara
---

This plugin extends the idea of the [original Kuwahara](https://imagej.net/ij/plugins/kuwahara.html) filter from rectangular kernels to (straight) linear ones.

You can specify how large the generated kernels should be, and for how many different angles they are generated. Additionally, you can specify what criterion is used to select the best orientation.

Example:

![](/media/plugins/noisy-lines.png)

With 30 angles at line length 17 with the criterion *Variance*, the filtered image looks like this:

![](/media/plugins/noisy-lines-kuwahara.png)

 
