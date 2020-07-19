{{PlatformsMenu}}{{Minibox | logo=Osx.png | blurb=[[wikipedia:Think different|Think different]].}}[[wikipedia:macOS|macOS]] (formerly called Mac OS X, then OS X) is [[wikipedia:Apple Inc.|Apple]]'s desktop operating system. It is [https://www.netmarketshare.com/operating-system-market-share.aspx the second most common desktop computing platform] after [[Windows]]. This page details issues specific to using [[ImageJ]] on macOS systems.


{{TOC}}
= Installation =
See also the [[Java 8]] page for OS-X-specific issues.

= Troubleshooting =
See also the [[Troubleshooting]] page.

== ImageJ becomes very slow after running for a while ==
There are several reasons ImageJ can run slowly on macOS.

=== Java painting bug ===
On OS X, older versions of Java 8 (prior to 1.8.0_45)—as well as all versions of Java 7 (including 1.7.0_80)—are extremely slow at displaying images. You should either upgrade to the latest version of Java 8, or revert to Java 6 (see "Frequently Asked Questions" below).

=== Window menu bar bug ===
There is a bug in Java 8 on MacOS which causes the application to drastically slow down as many windows are opened and closed over time. Make sure you are using the latest version of Java 8, as well as the latest version of ImageJ.

=== App Nap ===
On recent versions of OS X—10.9 "Mavericks" and later—there is an "App Nap" feature which dramatically slows down applications that are not in the foreground. Leave ImageJ in the foreground while it is processing to avoid this issue. (There are also [http://osxdaily.com/2014/05/13/disable-app-nap-mac-os-x/ various] [http://www.cultofmac.com/274396/disable-app-nap-specific-apps-os-x-tips/ ways] to disable App Nap on your machine, but we have not had much success with them. If you find a solution that works, allowing ImageJ to run fast in the background, please [http://forum.imagej.net/ tell us on the forum]!)

== No title bar in file chooser dialogs ==

On macOS 10.11 "El Capitan" and later, the operating system no longer includes a title bar for file chooser dialogs. See e.g. [https://bugs.openjdk.java.net/browse/JDK-8136427 this JDK bug] discussing the issue.

As a workaround, you can check "Use JFileChooser to open/save" in the {{bc | Edit | Options | Input/Output...}} dialog.

= Frequently Asked Questions =
See also the [[Frequently Asked Questions]] page.

== How do I run ImageJ with Java 6? ==

It is unfortunately no longer feasible to install Apple Java 6 on current versions of macOS. However, ImageJ should work OK with Java 8. If you have difficulties, please post on the [https://forum.image.sc/ Image.sc Forum].

At any time, you can verify which Javas are installed on your system using {{GitHub|org=ctrueden|repo=ctr-scripts|path=java-info|label=this script}}.

== How do I run ImageJ on Yosemite? ==

Install the [http://java.com/ Java 8 JRE] or [http://www.oracle.com/technetwork/java/javase/downloads/ Java SE 8].

== How do I run ImageJ on El Capitan? ==

Unfortunately, El Capitan has some new java-related issues. If you upgraded to El Capitan and your Java 8 installation is not being detected properly:

# Try installing the [http://www.oracle.com/technetwork/java/javase/downloads/index.html Java SE JDK].
# If that does not work, see [https://oliverdowling.com.au/2015/10/09/oracles-jre-8-on-mac-os-x-el-capitan/ this guide] for steps which could get things working again.
# Alternately, ImageJ still works on El Capitan with Java 6 (see above).

[[Category:Platforms]]
