---
mediawiki: ImgLib2_FAQ
title: ImgLib2 FAQ
section: Explore:Libraries:ImgLib2
---




## What *is* ImgLib2 anyway?

It is a library that helps you to implement algorithms for multi-dimensional data processing. The idea is that you can concentrate on the essence of your algorithm rather than syntactic sugar. It is possible to implement an algorithm without specifying what the image's data type is, how many dimensions it has, and how the image is stored.

ImgLib2 is also the foundation of the [ImageJ2](/software/imagej2) data model.

## How do I migrate my ImgLib1 code to ImgLib2?

There is some [rudimentary documentation](/libs/imglib2/migrate-from-imglib1), but you will most likely need to ask more detailed questions on the [ImageJ Forum](http://forum.imagej.net).

## How to create a new image from scratch?

    int w = 768, h = 512, timepoints = 20;
    Img<FloatType> img = ArrayImgs.floats(w, h, timepoints);


