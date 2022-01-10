---
title: 2015-03-26 - ImageJ 2.0.0-rc-28 released
---

Today, the [ImageJ team](/people) is pleased to announce a new public release candidate for [ImageJ2](/software/imagej2): version 2.0.0-rc-28.

{% include img width="450px" align="right" alt="The ImageJ Console window" src="/media/news/no-more-dev-null.png" %}

## What's new

### Console window

The main new feature of this release is a Console window that tracks all output to the {% include wikipedia title='Standard streams' text='standard output and error streams'%}. Previously, all messages to these streams were silently discarded unless the Debug option in {% include bc path='Edit | Options | Misc'%} was enabled prior to any issues.

Now, all that has changed: the [SciJava Common](/libs/scijava#scijava-common) library gained a new feature to track the standard streams ([scijava-common/28f717b9](https://github.com/scijava/scijava-common/commit/28f717b9684047f9df5e3deee10cbcee81334b97)), and the relevant ImageJ user interfaces added a dedicated Console window which pops up whenever output is sent to the error stream ([scijava-ui-swing/361bc585](https://github.com/scijava/scijava-ui-swing/commit/361bc585d9ae833bb0d4b47c0a6cda7485d40357), [imagej-legacy/0956b341](https://github.com/imagej/imagej-legacy/commit/0956b34185c16c9f5ca82504d24e27371e3249ed)).

This change has important consequences for users. Previously, if a script or plugin issued an error message, it would often be silently discarded with the user never seeing it. For example, see script right: that buggy [Python](/scripting/python) script tries to open a non-existent file. Prior to the Console window, the script would appear to "hang" with no feedback to indicate it crashed. Now, an error appears in red to make it clear to that something went wrong.

Note that messages on the standard *output* stream do not cause the Console to appear, because there are many ImageJ plugins in the wild (e.g., [Bio-Formats](/formats/bio-formats)) that emit information on that stream. The Console will only appear automatically when messages to the standard *error* stream occur. However, you can bring it up any time by choosing Console from the bottom of the Window menu.

The Console feature still has some rough edges ([scijava-common\#155](https://github.com/scijava/scijava-common/issues/155), [scijava-ui-swing\#5](https://github.com/scijava/scijava-ui-swing/issues/5), [scijava-ui-swing\#6](https://github.com/scijava/scijava-ui-swing/issues/6))—as always, [bug reports](/discuss/bugs) are welcome. But we believe this change is an important step forward to avoid confusion and improve the [quality of bug reports](/discuss/bugs#bug-reporting-best-practices) overall.

### Better ImageJ2 data structure syncing

The "Enable ImageJ2 data structures" option in {% include bc path='Edit | Options | ImageJ2'%} has been removed, and is now off by default ([imagej-legacy/231b7651](https://github.com/imagej/imagej-legacy/commit/231b76517f45993b5dfc4b1ddcaf8a14ff04491d)). We have not had time to complete this feature, and it currently causes substantial performance issues when enabled, so we want to be absolutely certain that no one enables it naively or by accident. It is still possible for interested developers to toggle the feature on by setting the `imagej.legacy.sync` environment variable.

Regardless, that feature is also less important now that we do on-demand syncing when encountering an ImageJ2 command or script parameter, such as a `net.imagej.Dataset`. This release also fixes a bug surrounding that on-demand syncing, which caused it to be triggered unnecessarily ([imagej-common/92e59826](https://github.com/imagej/imagej-common/commit/92e59826bde0642f217e07b38c161087b15538d0)).

Thanks to Greg for the [bug report on the ImageJ mailing list](https://list.nih.gov/cgi-bin/wa.exe?A2=IMAGEJ;e60027e9.1503)!

### Bug fixes

Lastly, as usual, this release includes various small enhancements and fixes (e.g., [imagej-legacy/4ab51325](https://github.com/imagej/imagej-legacy/commit/4ab513259fa85bef083eae8923b3755a0ac0703d)).

## How to update

Use the {% include bc path='Help | Update...'%} command to update your [ImageJ](/software/imagej) installation. Please send any comments to the [ImageJ mailing list](/discuss/mailing-lists). Thanks for the continued feedback and support!

 
