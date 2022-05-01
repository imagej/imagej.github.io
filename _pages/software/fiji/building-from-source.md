---
mediawiki: Downloading_and_Building_Fiji_From_Source
title: Downloading and Building Fiji From Source
section: Explore:Software:Fiji
---


The complete Fiji distribution of ImageJ consists of over a hundred individual components. Most of these components are ImageJ [plugins](/plugins); the rest are core libraries, [scripts](/scripting) and several other resources (such as the [Fiji logo](_File_Fiji-icon.png) and the README).

In the past, Fiji used to be built from one monolithic source code repository, which became unmanageable over time. These days, therefore, developers start from a fully-populated *Fiji.app/* directory and build only the parts they would like to change.

# Download Fiji

The first step is the same for developers as it is for users: [Download](/downloads) Fiji, and unpack it. The Desktop is the recommended location.

# Install Java

The next step is to install [OpenJDK 8](https://adoptopenjdk.net/). You will need a JDK in order to develop Java code.

# Check out and build individual plugins/libraries

To develop a plugin, the developer first needs to find out in which file it is contained. To do that, simply call the *Command Finder* (shortcut {% include key keys='Ctrl|L' %}), type (part of) the label of the menu entry in whose function you are interested, and look at the *File* column.

Each individual component is maintained in its own repository in the [*fiji* org on GitHub](https://github.com/fiji/). The name of the repository corresponding to a given *.jar* file is essentially identical with the file name, except that trailing underscores are stripped. Example: *Stitching\_.jar* is maintained in the repository at <https://github.com/fiji/Stitching>, *Time\_Lapse.jar* in the repository at <https://github.com/fiji/Time_Lapse>.

If in doubt about the location of the repository, just call {% include bc path='Plugins | Debug | System Information'%} and find the section corresponding to the file in question.

Once the developer has identified which plugin or library she wants to modify or develop further, it is very easy to build and contribute by following [this tutorial](/develop/improving-the-code).

## Example

Let's assume that we want to develop the Skeletonize3D plugin. Its source code is maintained at <https://github.com/fiji/Skeletonize3D>. The first step is to clone the source code:

```shell
$ git clone https://github.com/fiji/Skeletonize3D
Cloning into 'Skeletonize3D'...
remote: Counting objects: 115, done.
remote: Compressing objects: 100% (58/58), done.
remote: Total 115 (delta 46), reused 115 (delta 46)
Receiving objects: 100% (115/115), 22.81 KiB | 0 bytes/s, done.
Resolving deltas: 100% (46/46), done.
Checking connectivity... done.
```

You only need to type the part after the *$* prompt, i.e you would type `git clone `[`https://github.com/fiji/Skeletonize3D`](https://github.com/fiji/Skeletonize3D). The rest is shown only for reference, so that you know what to expect.

Then let's use the command-line Maven to build the project:

```shell
$ cd Skeletonize3D/
$ mvn
[INFO] Scanning for projects...
[... lots and lots of interesting and useful information ...]
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 52.574s
[INFO] Finished at: Tue Dec 02 10:27:00 CET 2014
[INFO] Final Memory: 20M/81M
[INFO] ------------------------------------------------------------------------
```

And finally, let's build the project and install it into the *Fiji.app/* directory:

```shell
$ mvn -Dimagej.app.directory=$HOME/Desktop/Fiji.app/ -Ddelete.other.versions=true
[INFO] Scanning for projects...
[... lots and lots of interesting and useful information ...]
[INFO]
[INFO] --- imagej-maven-plugin:0.5.4:copy-jars (copy-jars) @ Skeletonize3D_ ---
[INFO] Copying Skeletonize3D_-1.0.2-SNAPSHOT.jar to $HOME/Desktop/Fiji.app/plugins
[INFO] Deleted overridden Skeletonize3D_-1.0.1.jar
[INFO] Copying ij-1.49j.jar to $HOME/Desktop/Fiji.app/jars
[INFO] Deleted overridden ij-1.49m.jar
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 21.331s
[INFO] Finished at: Tue Dec 02 10:30:02 CET 2014
[INFO] Final Memory: 14M/81M
[INFO] ------------------------------------------------------------------------
```

Of course, this assumes that you followed the suggestion and unpacked your Fiji onto the Desktop. If you unpacked it somewhere else, you *have* to adjust the command-line accordingly.

Note that the exact dependency versions, as specified by the project in the *pom.xml* file, are copied into the *Fiji.app/* directory, possibly replacing other versions. You will want to make sure to use not-too-different versions from the current versions.
