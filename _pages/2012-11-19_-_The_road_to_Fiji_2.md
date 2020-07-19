This blog post was originally [http://imagejconf.tudor.lu/program/doku.php?id=:program:presentations:johannes_schindelin13920899 a talk at the ImageJ conference 2012] in Luxembourg.

== Introduction ==

It seems that many projects associated with [[Fiji]] attach a "2" to their name... [[TrakEM2]], [[ImgLib2]], [[ImageJ2]]. Not to be left behind, Fiji will do the same: the next big Fiji version will be Fiji2 :-)

In addition, there is a very good, technical reason to go "Fiji2". From the get-go, Fiji set out to make work with ImageJ easier&mdash;both for developers and users. For developers in particular, we wanted to have a good infrastructure that helps developing better plugins faster. As part of that, we explored not only new development techniques such as using a [[Git|source code management tool]], but we also worked toward a more flexible core.

As an example, we provided a way to run some plugins [[Headless|without a graphical desktop]]. Due to the design of [[ImageJ1|ImageJ 1.x]], this "headless" mode can work only to a subset to plugins, though. Fiji also started to address other issues with ImageJ 1.x such as the lack of an [[updater]], a powerful [[Script Editor|editor for macros and scripts]], or extension points e.g. to add new tools (ImageJ 1.46d added a limited version of Fiji's <code>AbstractTool</code> framework).

Happily, these and other design limitations are addressed in the next-generation ImageJ!

== ImageJ2 ==

ImageJ2 (thanks to NIH's funding) provides a new, modular and flexible architecture that will serve us well for decades to come. Fiji started contributing back modules such as the powerful data processing library ImgLib2, the updater and the scripting editor, and can concentrate on life sciences again, its original purpose. Like Fiji, ImageJ2 tries as much as possible to cater to the large and vibrant ImageJ community, testament to which is that the default user interface looks almost exactly like the user interface of ImageJ 1.x:

[[Image:Ij2-screenshot.jpg|665px|center|thumb|'''ImageJ2 screenshot''']]

== Modular architecture ==

But under the hood, ImageJ2 is much more modular. This is something we needed in Fiji, too. As an example, let's look at a subset of Fiji's modules:

[[Image:Fiji-modular.png|665px|center|thumb|'''Modules in Fiji''']]

In this chart, the dark blue boxes denote three of Fiji's plugins, the light blue boxes three of the projects associated with Fiji and the gray boxes stand for third-party projects which are used, but not actively developed, in the Fiji context. The arrows show the relationship "contributing functionality to".

It is obvious that many of the depicted components share their dependencies with other components. For example, both the [[3D Viewer]] and [[TrakEM2]] rely on [[ImgLib2]]. Now, [[ImageJ1|ImageJ 1.x]] (and many plugins written for it) try to avoid such dependencies since it is inconvenient to force users to keep track of them. The downside for the developer is that they have to implement the same functionality as other people provided, again. As a consequence, such support is often incomplete, and sometimes bugs hide in that code for years.

But in Fiji, we have the [[updater]], which makes it easy both for developers and users to manage many dependencies effortlessly.

On the road to Fiji2, we also adopted ImageJ2's use of [[Maven]]&mdash;it is basically an updater for developers, as it makes it easy to keep track of dependencies' different versions and to inspect their source code. It is also superior to the previous approach (the [[Fiji Build System]]) that did not allow integration into the many available developer tools (e.g. [[Eclipse]]).

This modular architecture allows us to integrate many third-party components without hassle, for example machine-learning libraries, database libraries, libraries to read/write PDF files, the powerful [[Bio-Formats]] and [[SCIFIO]] libraries, etc.

== Automated testing ==

Another very important step on the road to Fiji2 is that the components which migrated to ImageJ2 are equipped with automatic regression testing. That is, ImageJ2's trusty server ([[Jenkins]]) runs a series of functions testing certain functionality everytime a developer makes some changes. Whenever these tests break, the developers are notified and can fix the breakage before the respective component is uploaded to the update site.

This procedure helps us ensure that bugs, once fixed, do not rear their ugly heads again. It will make using Fiji much friendlier to users, too, because they will not need to report as many bugs since they will not even see them. The developers can run those tests, too, to test before the changes hit the server. In the ideal case everything will be green:

[[Image:Ij2-jenkins.png|665px|center|thumb|Automated regression testing]]

== Recurrent tasks ==

Using ImageJ2's Jenkins has further benefits: apart from building the complete Fiji and running automatic regression tests, Jenkins can run all kinds of repeating jobs. One of those jobs keeps an up-to-date Fiji version and packages it into what we call [[Downloads|continuous releases]].

[[Image:Fiji-continuous-releases.jpg|665px|center|thumb|Continuous Fiji releases]]

Other tasks involve [http://jenkins.imagej.net/view/Synchronizers/ keeping our source code repositories in sync], [http://jenkins.imagej.net/job/ImageJ-launcher/ building the ImageJ launcher] for all of our supported platforms, keeping an eye on the ImageJ 1.x website, [http://jenkins.imagej.net/view/Synchronizers/job/Synchronize-and-deploy-IJ1/ deploying it as a Mavenized project] and [http://jenkins.imagej.net/job/Upload-IJ1-Into-ImageJ/ uploading the new ImageJ 1.x version to the update site immediately] (thereby making sure that every Fiji/ImageJ2 user always gets the benefit of the latest ImageJ 1.x release), etc.

== Project management ==

A development tool Fiji2 might adopt (inspired by ImageJ2, too) is to [http://trac.imagej.net/roadmap manage the project] by splitting it into milestones that are in turn split into goals (that are in turn split into single tasks). It makes it easier to organize and prioritize what has to be done. Just like the automatic testing, it is part of the open process of ImageJ2:

[[Image:Ij2-trac.jpg|610px|center|thumb|'''ImageJ2 Project Management''']]

== Fiji vs Fiji2 ==

What will change with Fiji2 is best illustrated by this figure:

[[Image:Fiji2-roadmap.png|665px|center|thumb|'''Fiji will become Fiji2''']]

In subfigure ''a'' the status quo is shown: Fiji relies heavily on ImageJ and contributes ImgLib2 and the updater to ImageJ2. In subfigure ''b'', you see the future: Fiji will rely heavily on ImageJ2 to provide the robust core and also the legacy mode which can run any existing ImageJ 1.x plugins and macros. All the improvements going into ImageJ2, including improvements to components that originated from Fiji, will benefit all ImageJ users.

So far, we already integrated the updater:

[[Image:Ij2-updater.png|664px|center|thumb|'''ImageJ2 updater''']]

We also integrated a first version of the Script Editor, using the opportunity to redesign the scripting infrastructure from the ground up:

[[Image:Ij2-script-editor.png|624px|center|thumb|'''ImageJ2 Script Editor''']]

In preparation for the final move to Fiji2 (which will bring up ImageJ2's GUI by default), we will provide a command to switch between the ImageJ2 and the legacy mode. Until Fiji2, the default user interface will still be ImageJ 1.x.

[[Image:ij2-legacy-mode.png|665px|center|thumb|'''ImageJ2 legacy mode''']]

== What does this mean for you? ==

In addition to full support for ImageJ 1.x through ImageJ2's legacy mode, Fiji will benefit from the flexible design of ImageJ2.

Since ImageJ2 plugins can run basically everywhere (one of the design goals), it is likely that more and more developers even outside of the ImageJ community will find it attractive to provide their code as ImageJ2 plugins.

Through funding by the NIH, ImageJ2 will provide a robust, dependable and stable core for Fiji.

Since they no longer have to worry about infrastructure issues, the Fiji developers will be able to focus more on image analysis in the life sciences.

End users will benefit from the more modular approach, too: a single click will tell the ImageJ updater to install/update from a pre-configured list of update sites.
