---
mediawiki: SEM_FEI_metadata_scale
title: SEM FEI metadata scale
categories: [Uncategorized]
---

## **Overview**

This tool reads FEI SEM acquistion metadata from tiff tags and set image scale based on pixel size.

Note: This macro use Bio-formats plugin to read metadata. Fiji should include the plugin in default. Otherwise, install Bio-formats manually in ImageJ.

## **How to use**

1. Open a ".tif" file acquired from a FEI SEM/FIB (currently acquired by Thermofisher), and make the image window active. Note that the image dimensions are not calibrated.

<figure><img src="/media/plugins/emtool-04.jpg" title="EMtool_04.jpg" width="550" alt="EMtool_04.jpg" /><figcaption aria-hidden="true">EMtool_04.jpg</figcaption></figure>

2. Click "SEM/FEI SEM metadata Scale", the metadata for the image will be displayed in the log window.

<figure><img src="/media/plugins/emtool-05.jpg" title="EMtool_05.jpg" width="300" alt="EMtool_05.jpg" /><figcaption aria-hidden="true">EMtool_05.jpg</figcaption></figure>

3. The image dimensions are also calibrated based on the pixel size in the metadata. Scale bar can be added using the ImageJ tool {% include bc path="Analyze|Tools|Scale Bar..." %}.

<figure><img src="/media/plugins/emtool-06.jpg" title="EMtool_06.jpg" width="550" alt="EMtool_06.jpg" /><figcaption aria-hidden="true">EMtool_06.jpg</figcaption></figure>
