The [[Stitching]] plugin for ImageJ is an extremely useful tool for combining multi-image datasets, such as high-resolution microscopy scans, into a single image for analysis. With the increasing need for operations involving high-resolution data, we are planning to update the plugin and bring it into more prominent focus in [[ImageJ2]].

To that end, we have the following goals:

* '''Improve Stitching performance.''' This work is already completed and [https://github.com/fiji/Stitching/pull/15 pending integration]! By performing additional pre-processing and reducing the per-pixel work, the next version of the Stitching plugin should see as much as an order of magnitude increase in performance.
* '''Update to use [[SCIFIO]] for image I/O.''' This will improve the flexibility of Stitching, allowing new multi-image formats to be supported via plugin, while still providing full [[Bio-Formats]] support. Additionally, many planned improvements in SCIFIO, such as [https://github.com/scifio/scifio/issues/125 caching], should improve interactions with the large datasets created by Stitching.
* '''Conversion to ImageJ2 plugins.''' This will involve breaking Stitching down to its functional components (e.g. computing overlap and fusion) and turning those components into parameterized IJ2 plugins. This will facilitate automatic input harvesting, and should greatly improve the potential for scripted Stitching. Furthermore, by integrating Stitching with the I/O plugin framework for IJ2, a simple File&gt;Open call on part of a multi-image dataset should just &quot;do the right thing&quot; and open the stitched image. With coming legacy layer improvements, this will work in ImageJ as well!

You can find an in-depth writeup on the use of the Stitching plugin on the [[Stitching]] page. Additional questions are welcome on the [[Mailing Lists|ImageJ mailing list]].

We're very excited to have deeper integration with Stitching, and would love to hear your use cases, wish lists and success stories!

[[Category:News]]
[[Category:ImageJ2]]
