---
title: Android
section: Learn:ImageJ Basics:Supported Platforms
---

{% include img src='icons/android' align='right' width=150 caption='Inne cute?' %}

Android is a mobile operating system developed by Google, which commonly runs on Android phones and tablets.

## Status of ImageJ on Android

The Android operating system uses a modified version of the Java virtual machine. So in principle, running ImageJ on Android devices is feasible. However, running ImageJ on Android does not currently work, because:

-   [ImageJ 1.x](/software/imagej) uses AWT, which is not available on Android.
-   [ImageJ2](/software/imagej2) was built with a separation of concerns in mind (see [Architecture](/develop/architecture) page for technical details), but there is no infrastructure in place to ensure that all ImageJ2 APIs are Android-compatible. It would be a feasible project, but potentially a lot of work, to do that. The community would welcome efforts in this direction!

See [this forum thread](https://forum.image.sc/t/using-imagej-with-android/2517) for further details and discussion.
