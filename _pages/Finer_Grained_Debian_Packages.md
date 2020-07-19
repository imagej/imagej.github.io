'''This page is only of interest for people who are interested in how the scripts under the debian subdirectory work - this is probably no one, so this page is largely here as a reminder to myself.'''

FIXME: add information about the weekly build script to this page

At the March 2010 Hackathon, I made lots of changes to the old package building machinery.  There were a number of problems with the old system, including:

* Building one monolithic package; in particular, this meant that many Free Software licenses mixed up in the one package.
* Bundling too many components that were already available in Debian main / Ubuntu.
* There were some non-free components included in the monolithic package.
* Each time I made a new release, I had to rebase the previous release branch.  This was tedious, sometimes difficult and there's no particular reason not to build straight from master.

Since then, one our Google Summer of Code students, Yap Chin Kiet, and Johannes Schindelin worked on inferring dependencies between the jar and class files created in Fiji for the Fiji Updater, so we can reuse this code to infer package based dependencies.

The improved system is described below.

<b>WARNING: this build process will delete files from your git repository, remove submodules with "rm -rf" and take various other steps that you don't want to happen in your working repository.  You need a good reason to take these steps - if you just want to rebuild the Debian packages, then "apt-get source fiji" is your friend - don't follow these steps.</b>

The relevant lines for /etc/apt/sources.list, if you don't mind trying the experimental versions of these packages, are:

<code>
    deb https://fiji.sc/downloads/apt-experimental/ ./
    deb-src https://fiji.sc/downloads/apt-experimental/ ./
</code>

The packages are targetting Ubuntu 10.04 (Lucid Lynx) and Debian testing (squeeze) later than August 2010.

== Short Version ==

Mostly as a reminder to myself, the quick way to build new packages is:

* Clone a new fiji.git, initialize and update the right submodules [FIXME: document which submodules are required, mentioned in the {{GitHub|repo=fiji|path=debian/TODO|label=TODO}} at the moment]
* Run <tt>debian/complete-build</tt>.  If anything doesn't work, then you can retry the build with <tt>debian/build-command</tt>.  Before retrying <tt>debian/complete-build</tt>, make sure that you've committed your changes, since afterwards you'll need to run <tt>git reset --hard</tt> to clean the tree so that <tt>debian/complete-build</tt> is happy to try again...
* Assuming that you're building on an amd64 machine, run <tt>debian/build-in-i386-chroot</tt> to build the i386 packages.  (The chroot can be created as a one-off with debian/create-i386-chroot.py but you will still need to carefully customize /etc/schroot/schroot.conf )
* Upload the new versions of the packages with <tt>debian/upload-to-pacific</tt>.

== Longer Version ==

=== Clone a new copy of fiji.git ===

(This may strike you as not a very git-ish first step, but the build process rather brutally removes submodules and ignored files, and I don't want people to risk losing work as a result of following these instructions.)

Clone the respository afresh with:

    git clone git://fiji.sc/fiji.git

... and then initialize and update the following submodules:

    git submodule update --init modules/AutoComplete \
            modules/ImageJA \
            modules/RSyntaxTextArea \
            modules/TrakEM2 \
            modules/bio-formats \
            modules/commons-math \
            modules/ij-plugins \
            modules/imglib \
            modules/mpicbg \
            modules/tcljava \
            modules/weka

=== What debian/complete-build calls ===

==== Check that git status is clean ====

This shouldn't be necessary if you've just cloned a new copy, as above, but in other situations it might be useful:

  debian/update-debian.py --check-git-clean

==== Remove non-free and unneeded components ====

Run the following command:

   debian/update-debian.py  --clean

This should remove the non-free and unnecessary components, and rewrite the Fakefile to remove references to these components.

==== Generate the build-command script ====

The build-command script, which will actually be used to build Fiji, needs to be generated from the Fakefile.  You do this with:

   debian/update-debian.py --generate-build-command

==== Build the source tree (to generate the control file from) ====

Unfortunately, in order to accurately generate the Debian package-based dependencies from the file-based dependencies in [http://update.fiji.sc/db.xml.gz] we need to build the complete tree in order to find all the generated files which need to be assigned to packages.  So, build Fiji with the command that debian/rules will use with:

  debian/build-command

(We need to use a modified build command since we need to override some of the CLASSPATHs defined in Fakefile which refer to bundled jars which are now in dependent packages.)

==== Generate the debian/control file ====

Create a debian/control file with the right dependencies and package definitions:

  debian/update-debian.py --generate-complete-control

This is based on the generated files and db.xml.gz.

==== Clean the build tree ====

Before building the tree for the final packaging, we need to clean it so that only source files are included in the source archive:

  debian/update-debian.py --clean

==== Build the debian packages ====

   dpkg-buildpackage -rfakeroot 

If you're not able to sign the packages, add the parameters "-us -uc".  If you don't want to generate the source package (because dpkg-source takes *ages* to run with dpkg-dev prior to 1.15.5) add "-b".

The debian/rules Makefile which is called by that command will call debian/update-debian.py --install to copy parts of the built tree to the right locations.

=== Building the i386 version and Uploading ===

These steps are as described in the "Short Version" above.
