---
title: Video
description: Details of supported video formats and how to transcode unsupported formats
section: Learn:ImageJ Basics:File Formats
categories: [Import-Export]
---


Out of the box, ImageJ has limited support for some video formats such as AVI and [QuickTime](/formats/quicktime).

## Plugins

There are several ways to enable support for more video formats:

-   [Bio-Formats](/formats/bio-formats) includes support for reading additional codecs for some video formats. See the Bio-Formats [AVI](https://www.openmicroscopy.org/site/support/bio-formats5.4/formats/avi.html) and [QuickTime](https://www.openmicroscopy.org/site/support/bio-formats/formats/quicktime-movie.html) pages for the list of supported codecs. Bio-Formats is included with the [Fiji](/software/fiji) distribution of ImageJ.

<!-- -->

-   Enable the *beta-quality* FFMPEG [update site](/update-sites), which uses native bindings to the {% include wikipedia title='FFmpeg' text='FFmpeg'%} library to read many video formats. The source code for this update site is [embedded in the scifio-javacv history](https://github.com/scifio/scifio-javacv/tree/ffmpeg).

<!-- -->

-   For exporting video, you could try the [Save As Movie](https://sites.google.com/site/qingzongtseng/save-as-movie) plugin. Unfortunately, there is no update site for it; you must perform a complex installation procedure manually.

## Transcoding

Another strategy is to transcode your video to an uncompressed format using a tool such as QuickTime Pro, VirtualDub or FFmpeg on the command line. The uncompressed video stream can then easily be opened in ImageJ without the need for additional plugins. Similarly, for saving video, you can write to an uncompressed format, then compress it afterward using an external tool.

For files larger than 4GB, you may run into trouble with otherwise excellent transcoders like FFmpeg. For cases like that, check out [media player](https://www.videolan.org/vlc/VLC) and the [k-lite codec pack](https://www.codecguide.com/download_kl.htm).

## Future directions

The {% include github org='scifio' repo='scifio-javacv' label='SCIFIO-JavaCV' %} project will offer out-of-the-box support for video formats supported by [OpenCV](/software/opencv) including those supported by FFmpeg. At the moment, the SCIFIO-JavaCV project is inactive due to lack of development resources.


