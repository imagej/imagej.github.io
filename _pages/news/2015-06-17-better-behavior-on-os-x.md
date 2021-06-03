---
mediawiki: 2015-06-17_-_Better_behavior_on_OS_X
title: 2015-06-17 - Better behavior on OS X
---

Recent versions of OS X have seen a radical shift in how Java works. Apple no longer ships their own version of Java, but instead recommends users install Oracle's Java 7 or Java 8 runtime themselves. In recent years, these changes have made ImageJ deployment on OS X more difficult.

Fortunately, the ImageJ team is happy to announce that [ImageJ2](/software/imagej2) now behaves better on recent versions of OS X:

-   The ImageJ [Launcher](/learn/launcher) now makes a best effort to use the newest installed version of Java.
-   You no longer have to install Apple Java 6 just to run ImageJ—it is enough to just install Java 8.
-   A [critical bug](https://github.com/imagej/imagej-launcher/commit/4e1e688906d140c3ea6313ca2a0f9cc3b5879644) was fixed preventing Java platform extensions (in particular, [JavaScript](/scripting/javascript)) from working properly on OS X with Java 7 and 8.

There may still be some kinks to iron out. If you are running OS X, please update your installation and [let us know](/discuss/mailing-lists) how it works for you!

 
