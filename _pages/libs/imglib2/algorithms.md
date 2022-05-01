---
mediawiki: ImgLib2_Algorithms
title: ImgLib2 Algorithms
---

## Conventions for algorithm development in ImgLib2

-   Algorithms should either implement **java.lang.Runnable** if they do not return an object or **java.util.concurrent.Callable** if they do; no further interface hierarchy will provided for now

<!-- -->

-   Multithreading will be solved through the **ops package** for easily parallelizable algorithms

<!-- -->

-   More complicated algorithms that can provide significantly increased performance by implementing their own multithreading scenarios should implement the **MultiThreading interface** which allows to adjust the number of threads

<!-- -->

-   Algorithms should take **RandomAccessible**, **RandomAccessibleInterval** and/or **Iterable** as input, **Img** should be only used as temporary data structure
    -   **RandomAccessible** should be used if the OutOfBounds is defined externally (e.g. for gaussian convolution), an **Interval** should be passed as an extra parameter which defines the area that should be processed
    -   **RandomAccessibleInterval** should be used if the algorithm defines its own OutOfBounds strategy (e.g. FFT) outside the given boundary; an **Interval** should be passed as an extra parameter which defines the area that should be processed
    -   **Iterable** should be used if per-pixel operations are performed, here multithreading is delegated upstream

<!-- -->

-   Algorithms will be split into Maven subpackages where each subpackage can manage its own dependencies and licenses
    -   [ Gauss](/Gauss_Package_ImgLib2)
    -   [ FFT](FFT_ImgLib2)
    -   [ FourierConvolution](FourierConvolution_ImgLib2)
    -   [ IntegralImg](IntegralImg_ImgLib2)
    -   [ ScaleSpace](ScaleSpace_ImgLib2)
    -   ...

<!-- -->

-   **JUnit** tests should be placed in the respective subpackages and must not require any additional imports

<!-- -->

-   **Human tests** that might display images, show graphs or require any other imports than the algorithm itself should be placed in the **ImgLib2-Tests** project following the path convention of the algorithm

<!-- -->

-   Standard images for Human tests will not be part of the git repository but will be available as http-link; a special opener class **net.imglib2.io.ImgIOUtils** will provide download and permanent caching in the temporary directory of each computer

<!-- -->

-   Algorithms will have no direct dependency on the ImageJ2 plugin framework as they are generic; extra classes will provide access to the functionality of those algorithms

<!-- -->

-   A **Benchmarker class** will be implemented to measure the performance for different *containers*, *types*, *operating systems* and *machines*
