We are happy to announce the first stable release version of the [[ImgLib2]] core library!

This release was a central goal of the recent [[hackathon]] at [[LOCI]] in Madison, during the week of October 13 - 17.

The ImgLib2 core library is now [http://search.maven.org/#search%7Cga%7C1%7Cg%3A%22net.imglib2%22 available on Maven Central], and the [[source code]] for all ImgLib2 projects is [https://github.com/imglib accessible on GitHub].

Like the [[SciJava]] and [[ImageJ2]] projects, ImgLib2 releases now follow the [[semantic versioning]] scheme. Also, the project and [[git]] repository structure has changed. The main imglib repository has been [[Architecture#Git_repositories|split into multiple repositories]], named consistently with the artifact names and java package prefixes. Projects are now coupled using non-SNAPSHOT versions, in order to achieve [[reproducible builds]].

For further technical details on project structure, see the [[Architecture]] page.

Before coming out of beta, we have made several last-minute changes to the code:
* All <code>@Deprecated</code> methods and classes have been removed.
* All metadata handling (formerly <code>imglib2-meta</code> subproject) is being moved into {{GitHub | org=imagej | repo=imagej-common | label=imagej-common}}. From ImgLib2 core, the classes <code>AnnotatedSpace</code>, <code>AbstractAnnotatedSpace</code>, and <code>Axis</code> were moved to {{GitHub | org=imagej | repo=imagej-common | label=imagej-common}}.
* The current ROI representation was not considered stable enough to be included in a release. The <code>net.imglib2.roi</code> and <code>net.imglib2.labeling</code> packages were moved to the new {{GitHub | org=imglib | repo=imglib2-roi | label=imglib2-roi}} subproject which will remain in beta for now.
* The <code>net.imglib2.multithreading</code> package was moved to {{GitHub | org=imglib | repo=imglib2-algorithm | label=imglib2-algorithm}} and deprecated.
* We merged work by Albert Cardona and Stephan Preibisch on "fractional" types. ImgLib2 <code>NativeType</code>s map pixels into primitive arrays, where often the mapping is one-to-one. For example, an <code>UnsignedByteType</code> pixel maps into one byte of a primitive <code>byte[]</code> array. With fractional types this mapping maybe non-integral, for example <code>Unsigned12BitType</code> maps pixels into a <code>long[]</code> array, where each pixel occupies 12/64 longs.
* Superfluous generic parameters were removed from <code>Projector<A,B></code> interface which is now only <code>Projector</code>. Projector implementations were fixed accordingly.
* Several classes were renamed or moved to more suitable places:
** <code>Extended[Real]RandomAccessibleInterval</code> moved to the <code>net.imglib2.view</code> package.
** <code>RandomAccessibleOnRealRandomAccessible</code> moved to the <code>net.imglib2.view</code> package.
** <code>Binning</code> moved to the <code>net.imglib2.util</code> package.
** The contents of package <code>net.imglib2.collection</code> (<code>KDTree</code> etc.) moved to the <code>net.imglib2</code> package.
** <code>net.imglib2.concatenate.Util</code> was renamed to <code>net.imglib2.concatenate.ConcatenateUtils</code>.
** <code>Bounded</code> moved to the <code>net.imglib2.outofbounds</code> package.
** The class <code>NearestNeighborInterpolator</code> from package <code>net.imglib2.interpolation.neighborsearch</code> was renamed to <code>NearestNeighborSearchInterpolator</code> (to avoid confusion with the <code>net.imglib2.interpolation.randomaccess.NearestNeighborInterpolator</code> class).
** The <code>Pair</code> interface moved to the <code>net.imglib2.util</code> package.
* The <code>net.imglib2.util.Util</code> class was cleaned up:
** Methods <code>getTypeFromRandomAccess()</code> and <code>getTypeFromRealRandomAccess()</code> were removed. We considered them too dangerous because the <code>RandomAccess</code> may be pointing to invalid position.
** Unused methods <code>setCoordinateRecursive()</code> and <code>getRecursiveCoordinates()</code> were removed.
** Some variants of <code>computeLength()</code> and <code>computeDistance()</code> were removed. Use methods <code>distance()</code> and <code>length()</code> from <code>net.imglib2.util.LinAlgHelpers</code> instead.
** Methods <code>computeMedian()</code>, <code>computeAverage()</code>, etc. were renamed to <code>median()</code>, <code>average()</code>, etc.
* These unused classes were removed:
** <code>IterableIntervalSubsetT</code>
** <code>Triple</code>
** <code>RealPositionableFloorPositionable</code>
** <code>RealPositionableRoundPositionable</code>
** <code>ImgTranslationAdapter</code>
* Packages <code>net.imglib2.img.constant</code> and <code>net.imglib2.sampler.special</code> were removed (<code>ConstantImg</code>, <code>ConstantRandomAccessible</code>, etc). Similar functionality can now be achieved through the <code>net.imglib2.util.ConstantUtils</code> class and <code>Views</code>.

All ImgLib2 subprojects have been adapted to these changes and released (in some cases as new beta versions).

One thing still pending is to upload these new ImgLib2 releases to the ImageJ and [[Fiji]] [[update sites]], making them available to users of ImageJ and Fiji. This change has been rather involved, since there is a lot of downstream code affected by the API changes. But we expect to make the new ImgLib2 available to users before the end of the calendar year. Stay tuned for further announcements!

[[Category:News]]
[[Category:ImageJ2]]
