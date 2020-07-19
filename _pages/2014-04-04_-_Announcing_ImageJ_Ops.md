Today, the [[ImageJ]] and [[KNIME]] teams are pleased to announce {{GitHub|org=imagej|repo=imagej-ops|label=ImageJ Ops}}: a framework for reusable image processing operations. This library is the direct result of an extremely successful hackathon hosted by Michael Berthold's team at the University of Konstanz, Germany.

[[Image:Konstanz-hackathon.jpg|320px|thumb|right|Happy hackers: 502 commits in five days!]]
== Motivation ==

The ImageJ2 vision is to extend Java's mantra of &quot;write once, run anywhere&quot; to image processing algorithms. With that goal at its heart, ImageJ2 introduces extensible {{GitHub|org=scijava|repo=scijava-common|label=plugin}} and {{GitHub|org=imagej|repo=tutorials|path=maven-projects/working-with-modules/src/main/java/WorkingWithModules.java|label=module}} frameworks which make ImageJ commands richer, more powerful and easier to share across applications. Already, these modules are accessible from [[CellProfiler]], [[KNIME]], [[OMERO]] and [[Alida]].

But still notably missing was the next crucial layer: a framework for ''image processing'' specifically. To address that, we set out to create a framework for reusable image processing algorithms, with the following characteristics:

# '''Easy to use and extend.''' It is of paramount importance that there be a wealth of easy-to-use image processing operations (&quot;ops&quot;), as well as an easy framework for extending those ops in new directions. One of our observations from the workshops at the [[Conference 2012|ImageJ Conference 2012]] was that ImageJ2 still needs to do much more to realize such ease of use, both for users writing scripts, as well as for developers creating robust and reusable image processing algorithms.
# '''Powerful and general.''' An op should be able to consist of any number of typed input and output parameters, operating on arbitrary data structures, including images of N dimensions stored in a myriad of different ways: as files on disk, programmatically generated in memory, or in remote databases. Using the powerful [[ImgLib2]] library achieves this ambitious goal.
# '''Very fast.''' Even though ImgLib2 is vastly more general than ImageJ 1.x's data model, that generality should not come at the expense of performance. Otherwise, users must pay a time tax to do the same things they could already do in ImageJ 1.x. The ImageJ Ops framework needs to provide a means to override ''any'' general-but-slow op with a faster-but-more-specific alternative, fully transparently to the user.

When it comes to ease of use, generality and performance in computer programs, the usual rule of thumb is “pick two.” Yet we are happy to say that we believe Ops strikes a favorable balance between all three criteria.

== Getting started ==

An op is just an ImageJ module, but with some additional structure and requirements: you can think of an op as a function which takes a list of typed inputs, produces a list of typed outputs, and has no side effects. There are over 80 ops implemented so far, with {{GitHub|org=imagej|repo=imagej-ops|tag=ij-ops-0.1.0|path=operations.txt|label=many more to come}}; see this ImageJ tutorial to learn about some of them:

[https://github.com/imagej/tutorials/tree/master/maven-projects/using-ops/src/main/java/UsingOps.java Using Ops]

And for algorithm developers, there is another tutorial briefly demonstrating how it works to create a new one:

[https://github.com/imagej/tutorials/tree/master/maven-projects/create-a-new-op/src/main/java/CreateANewOp.java Create a new op]

== Caveats ==

Today marks the Ops project's very first beta release: [https://github.com/imagej/imagej-ops/tree/ij-ops-0.1.0 0.1.0]. As such, it is still under heavy development, with aspects of the design still subject to change. That said, we are quite confident in the core API, and do not expect it to change too much. What is more likely to change are the specific individual ops, how they work, which ones are available, and other finer details which will become apparent as the library continues to be developed and used.

== Conclusion ==

We sincerely hope that the Ops project will make it much easier for various software tools (e.g.: [[KNIME]], CellProfiler, OMERO, Alida, Icy, Vaa3D and of course ImageJ itself) to provide drop-in support for ImageJ's image processing operations, allowing scientists to truly &quot;write once, run anywhere&quot; and share with the world!

<br/>
-----

P.S. Here is a detailed list of accomplishments during the hackathon:

* Curtis, Martin, Christian & Johannes: Defined a framework for ops
** Discovery and selection
** Interfaces
** Unit tests
** Extensible optimization framework
** Code is short, easy to read, fast & general!
* Defined coding conventions and the process for imagej-ops development
* Martin, Christian et al: Ported existing ops from [[ImgLib2]] and [[KNIME]] to imagej-ops
** Christian, Michael Z: base for multithreaded ops
** Martin: lots and lots of ops
** Christian: meta ops: map, join, loop
** Christian: proof-of-concept descriptors
** Christian & Johannes: unified benchmark framework
** Johannes: proof-of-concept acceleration (on-the-fly code generation)
** Andreas G & Daniel: reimplemented several JFeatureLib implementations, evaluated existing implementations

Hackathons are great opportunities to Get Things Done, so we also worked on related projects:

* Andreas G & Daniel: new KNIP node for features
* Gabriel: SCIFIO writer integration
* Daniel: axis selection widget
* Andreas B. & Jonathan: Generalization of TrackMate interfaces
* Christian: Started porting all descriptors
* Christian, Martin & Johannes: Set-up Maven/Jenkins to automatically create OSGi bundles

Thank you so much to the [[KNIME]] team for making all of this possible!!

P.P.S. There is even an <code>ascii</code> op to dump an image to the console. This is surprisingly useful for unit testing, validating expectations and general debugging:

<source lang="java">
// create a new blank image
final long[] dims = {78, 23};
final Object blank = ij.op().create(dims);

// fill in the image with a sinusoid using a formula
final String formula = "10 * (Math.cos(0.3*p[0]) + Math.sin(0.3*p[1]))";
final Object sinusoid = ij.op().equation(blank, formula);

// add a constant value to an image
ij.op().add(sinusoid, 13.0);

// generate a gradient image using a formula
final Object gradient = ij.op().equation(ij.op().create(dims), "p[0]+p[1]");

// add the two images
final Object composite = ij.op().add(sinusoid, gradient);

// dump the image to the console
final Object ascii = ij.op().ascii(composite);
ij.log().info("Composite sinusoidal gradient image:\n" + ascii);

Composite sinusoidal gradient image:
               ...,,,,,,,,,,,...,,,,---++++++++++-----+++ooo**********ooooo***
.....         ...,,,-----,,,,,,,,,,---++++oooo++++++++++ooo****OOO************
.......      ...,,,--------,,,,,,,---+++oooooooo+++++++ooo***OOOOOOO********OO
......... .....,,,-----------,,,----+++oooooooooo+++++ooo***OOOOOOOOOO*****OOO
,,,,..........,,,----+++------------++ooooo*ooooooooooooo***OOOOOOOOOOOO**OOOO
,,,,,.........,,,---+++++----------+++oooo****oooooooooo***OOOO###OOOOOOOOOOOO
,,,,,.........,,,---++++++---------+++ooo*****oooooooooo***OOOO###OOOOOOOOOOO#
,,,,,.........,,,---++++++---------+++ooo*****oooooooooo***OOOO###OOOOOOOOOOO#
,,,,,.........,,,---+++++----------+++oooo****oooooooooo***OOOO###OOOOOOOOOOOO
,,,,..........,,,----+++------------++ooooo*ooooooooooooo***OOOOOOOOOOO***OOOO
.,.............,,,------------,,----+++ooooooooooo++++ooo***OOOOOOOOOO*****OOO
........    ...,,,----------,,,,,----++oooooooooo++++++ooo***OOOOOOOO*******OO
.......      ...,,,--------,,,,,,,---+++oooooooo+++++++ooo***OOOOOOO********OO
......       ...,,,-------,,,,,,,,---++++oooooo+++++++++ooo***OOOOO**********O
......       ...,,,,------,,,,,,,,,---+++ooooo++++++++++ooo***OOOOO**********O
......       ...,,,,------,,,,,,,,,---+++ooooo++++++++++ooo***OOOOO**********O
......       ...,,,-------,,,,,,,,---++++oooooo+++++++++ooo***OOOOO**********O
.......      ...,,,--------,,,,,,,---+++oooooooo+++++++ooo***OOOOOOO********OO
........   ....,,,-----------,,,,---+++oooooooooo+++++oooo**OOOOOOOOO*******OO
,,,,..........,,,----+++------------++ooooo*ooooooooooooo***OOOOOOOOOOOO**OOOO
,,,,,,.......,,,---+++++++--------+++oooo******ooooooooo***OOO#####OOOOOOOOOO#
,,,,,,,,...,,,,---+++++++++++----+++ooo**********ooooo****OO#########OOOOOOO##
----,,,,,,,,,,---+++ooooo++++++++++ooo****OOO************OO###################
</source>

And it looks très cool.

[[Category:News]]
[[Category:ImageJ2]]
[[Category:Ops]]
