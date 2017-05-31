Today, a lot of work on [[ImageJ]], [[Fiji]] and [[SciJava]] came to fruition all at once.

== ImageJ in Jupyter notebooks ==

The most exciting news is that, as [http://forum.imagej.net/t/jupyter-notebook-for-imagej/5421 announced on the ImageJ forum], there is now a {{GitHub | org=hadim | repo=scijava-jupyter-kernel | label=SciJava Jupyter Kernel}} enabling ImageJ to be used with [https://jupyter.org/ Jupyter Notebook] in all of the [[Scripting#Supported_languages|supported scripting languages]].

Please peruse the [https://imagej.github.io/tutorials/ ImageJ Tutorial notebooks] for examples of this kernel in action!

== Sweeping component updates ==

Nearly all components of the [[Architecture#Definitions|ImageJ software stack]], as well nearly all [[Fiji]] plugins, saw new releases [http://forum.imagej.net/t/split-boms-from-parent-configuration/2563 unifying and updating metadata] to better document [[Team|who is responsible for maintaining each component of the software]]. This metadata update has been in the works for more than 18 months; the next step will be to [https://github.com/scijava/mediawiki-maven-info autogenerate the sidebars of component wiki pages] so that plugin authors no longer need to manually keep wiki pages in sync. For technical details, see {{GitHub | org=fiji | repo=fiji | issue=121 | label=fiji/fiji#121}}.

This update also brings Fiji much closer to complete synchronization with the {{GitHub | org=fiji | repo=fiji | label=fiji/fiji}} source repository. Historically, there have been differences between the exact versions of components specified in the Fiji sources, versus those actually present on the Fiji update site at any given time. But we have been working very hard to reconcile those differences, such that the Fiji update site can ultimately be driven directly by what the source code specifies. For technical details, see {{GitHub | org=fiji | repo=fiji | issue=37 | label=fiji/fiji#37}}, {{GitHub | org=fiji | repo=fiji | issue=38 | label=fiji/fiji#38}} and {{GitHub | org=fiji | repo=fiji | issue=39 | label=fiji/fiji#39}}.

Finally, this update upgrades nearly all of Fiji's third party dependencies to their latest available release versions.

== New Fiji Life-Line versions ==

To guard against regressions which might result from such a big update, we updated the [[Fiji/Downloads#Life-Line_Fiji_versions|Life-Line downloads of Fiji]] with two new versions dated today: one for Java 8, and another for Java 6.

The Java 6 version in particular is notable because it provides a version of Fiji with the latest Java-6-compatible versions of all components. If you need to stick with Java 6 for some reason—e.g., you want to use Fiji with [[BoneJ]], and/or with the [[3D Viewer]] + [[Java 3D]] 1.5—then you can use this download as a starting point for your needs.

== Legacy Fiji components moved to their own update site ==

Several [https://sites.imagej.net/Fiji-Legacy/plugins/ legacy Fiji plugins] as well as [https://sites.imagej.net/Fiji-Legacy/jars/ no-longer-needed dependent libraries] have been retired from the ImageJ and Fiji update sites, migrating to a dedicated [https://sites.imagej.net/Fiji-Legacy/ Fiji-Legacy update site]. None of these plugins completed the transition to reproducible builds in late 2014. Many of them are dedicated script interpreters, which have now been replaced by a unified SciJava Script Interpreter which allows dynamic language switching.

Note that the primary intent of the Fiji-Legacy update site is to be used in combination with a Java-6 installation of Fiji—see "New Fiji Life-Line versions" above. Enabling both the Java-8 and Fiji-Legacy sites will result in some components with overlapping classes—e.g., the batik uber-JAR plus all individual batik components.

[[Category:News]]
[[Category:Fiji]]
