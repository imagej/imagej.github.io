---
title: 2014-08-08 - ImageJ 2.0.0-rc-11 released
---

Today, the [ImageJ team](/people) is pleased to announce a new public release candidate for [ImageJ2](/software/imagej2): version 2.0.0-rc-11.

## New features

-   Usage tracking! We can now track and upload (anonymously) use counts at the plugin level, along with information about the environment of use (country, java version, language, operating system, time zone). Although we are taking care not to expose any user data with these statistics, this feature can be disabled via a new {% include bc path='Edit | Options | Privacy...'%} setting. Expect great things coming to the usage page! (note: "great things" = statistics graphs)

<!-- -->

-   [Groovy](/scripting/groovy) scripting! The Groovy scripting language is [one of the most popular available for the JVM](http://bloodredsun.com/2011/10/04/scala-groovy-clojure-jython-jruby-java-jobs/). Hence, ImageJ now has built-in support for Groovy as a [scripting](/scripting) option.

<!-- -->

-   All images, whether opened with the [SCIFIO](/libs/scifio) option enabled or not, should now be automatically populated in `@Dataset` annotations in scripts and plugins. This will make parameterized scripting much more consistent and useful. See the [ scripting guide](/scripting) for more information and tutorials.

<!-- -->

-   More plugin types! Continuing our dedication to making ImageJ2 a flexible and extensible platform, we converted some lower level utilities to pluggable services: {% include github org='scijava' repo='scijava-common' tag='scijava-common-2.29.0' source='org/scijava/convert/ConvertService.java' label='type conversion' %} and {% include github org='scijava' repo='scijava-common' tag='scijava-common-2.29.0' source='org/scijava/prefs/PrefService.java' label='preference storage' %}. This won't mean much to users right now, but it gives developers new ways to tap in to the functionality of ImageJ, and plays a key role in extensions like our upcoming [MATLAB](/scripting/matlab) scripting language!

## Bug-fixes

-   We resolved a significant [memory leak](https://fiji.sc/bugzilla/show_bug.cgi?id=819) due to images not being closed properly. This was also causing naming errors (e.g., the second time you opened "Data" it would display a title "Data-1" even after closing the first image) and other terrible gotchas. As a consequence, the linkage between ImageJ2 and [ImageJ 1.x](/software/imagej) data structures maintained by the {% include github org='imagej' repo='imagej-legacy' label='legacy layer' %} is now more robust.
-   We fixed several bugs in [SCIFIO](/libs/scifio); e.g., ImageJ slice labels should now be preserved after saving and reopening in TIFF format.
-   Quite a few other small bug-fixes; for example, the languages shown in the `Languages` menu of the [Script Editor](/scripting/script-editor) now appear in a consistent and alphabetical order.

## How to test the release candidate?

Use the {% include bc path='Help | Update'%} command to update your [ImageJ](/software/imagej) installation.

Please send any comments to the [ImageJ mailing list](/discuss/mailing-lists). And thank you very much for trying ImageJ2!

 
