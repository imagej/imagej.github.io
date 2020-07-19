From Monday, December 3, 2018 through Friday, December 7, 2018, the [https://mpi-cbg.de/ Max Planck Institute of Molecular Cell Biology and Genetics] hosts ~10 developers at the [http://www.csbdresden.de/ Center for Systems Biology] in Dresden, Germany for a [[hackathon]] to develop KNIME Image Processing and [[ImageJ2]]/[[Fiji]] core infrastructure and [[plugins]].

Gitter channel: https://gitter.im/juglab/Hack1812

== Topics / Technical Discussions ==

=== TensorFlow (Debo, Curtis, Benny) ===

* Plan for TensorFlow: ship native libs both CPU and GPU in lib/<platform> directly; 
* TensorFlow update sites and reconcile to new TF version -- add tests

=== SCIFIO (Gabriel, Curtis) ===

* Create samples.scif.io, migrate LOCI samples, update scif.io website with a table of samples
* Update scifio-bf-compat to split the mega-format into one per reader/writer

=== Governance ===

* Code of conduct - https://help.github.com/articles/adding-a-code-of-conduct-to-your-project/ - http://openrespect.org/ (It's written by the author of The Art of Community)
* Update fiji.sc, imagej.net/Fiji, etc. with revised maintainership info
Google Scholar: citation count badges on wiki pages
* What to do about NanoJ using google analytics -- i.e. should we have usage stats?
** [Action item] Ask Ricardo Henriques about it
** Consider what to write onto code of conduct about what should be allowed
Meet at later point in time—and who is going to do it
* What to do about the two different logos: ImageJ vs. Fiji
* Upstream Java issues -- send something shortly after January 15
** [Action item for Ulrik] Writeup from Ulrik and Stephan S. about JavaFX
** [Action item for Ulrik] Writeup from Tobias about Unsafe

=== Wiki ===

* doi in maven pom
* citation badge on wiki pages

=== Servers (Gaby, Debo, Curtis) ===

* Server infrastructure overview with Gaby
rsync mirror to pacific.mpi-cbg.de

=== Labkit as Labeling Editor for KNIME Image Processing ===

* Node for editing labels in KNIME based on [[Labkit]] was created.
* Work is not entirely finish. We plan to finish this work during the  Ostrava Hackathon.
* Labkit was extended, and is now able to handle multiple images.
* A labeling datatype to store labels, and track modifications was developed.

=== Simple ImageJ API ===

* Discussion between: Deborah, Robert, Curtis, Matthias
* How can we make the scripting in ImageJ2 easier?
* Setup a table, of scripting examples in IJ1 and IJ2. Improve the IJ2 API where ever it's obviously required.
* Write a SimpleIJ gateway, that provides really simple methods for the most frequent tasks in ImageJ.
* A ImageJ2 script recorder could improve the IJ2 API, as it clearly shows where the API is to verbos. 

=== Big Data Server ===

* Discussion Tobias, Gabriella and Matthias about a mechanism for secure user authentication in Big Data Server (and ImageJ Server).
* It's needed by biologists, that want to share there data with specific users.
* ImageJ Server would also benefit, if the access to the API could be authenticated in a similar way.

=== Octtree Like, Compressed, Fast, Bitmaps for Imglib2 ===

* Tobias develops a data structure to store bitmap. For iteration, efficient pixels access and little memory foot print at the same time.
* Such data structures can be used to better express labels in imglib2. Even instance segmentations that consist of millions of labels, can be accessed efficiently if a cell image like cache is used.

=== HTTPS (Debo, Curtis, Gaby, Tobi) ===

* HTTPS java-version-check
* move list of update sites to a GitHub repository -- off the wiki

=== Updater/Launcher (Debo, Curtis) ===

* Add version to db.xml.gz schema
* Make the updater smart enough to support serving maven artifacts
* Migrate "make fiji package" to imagej updater
* improve "make package" to only zip up non-update-site things ("online mode")
* Eliminate native launcher in favor of javafx + java-launches-java scheme

=== Plot Service (Matthias, Curtis) ===

* Get it merged to scijava-common / scijava-ui-swing
* https://forum.image.sc/t/error-noclassdeffounderror-net-imagej-table-table/21369/7

=== Curtis ===

* Merge script editor PRs
add "browse javadoc" and "browse source" options for selected code? e.g. on IOService opens DefaultIOService on GitHub or javadoc.scijava.org
* Finish algorithms branch of imagej-mesh -- Move imagej-ops mesh package and algorithms into imagej-mesh -- See WIP commit message on algorithms branch -- Update imagej-ops to call migrated routines

=== Other ===
* Remove modern mode from GUI (Debo, Curtis)
* Labkit + KNIME (Matthias, Tim-Oliver, others)
* KNIME+TensorFlow+Server (Tim-Oliver, Benny)
* Ilastik tracking (Carsten, Mangal)
* Scenery + KNIME including BigVolumeViewer (Ulrik, Gabriel)
* Image metadata (Carsten, Marcel)
