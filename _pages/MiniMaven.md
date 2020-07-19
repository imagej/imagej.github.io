MiniMaven is a minimal build and dependency management system. It reads project configurations in the same format as [[Maven]] (''pom.xml'' files).

== Why Maven? ==

In the Fiji project, we need an easy way to define projects and their dependencies. We also want to support the widest variety of development tools, such as IntelliJ, Netbeans or Eclipse.

Maven is a standard way to do exactly that.

== Why MiniMaven? ==

The only reason for MiniMaven to exist is that Maven -- while powerful -- is also pretty resource-hungry. In contrast to MiniMaven, Maven requires many more CPU cycles, takes longer, and downloads many more bytes (due to downloading and running requiring Maven plugins and their dependencies).

Therefore we needed a system to build [[ImageJ1]], [[ImageJ2]] and [[Fiji]] quickly from the same type of project description files as Maven interprets, to be maximally flexible and interoperable.

== Command-line options ==

MiniMaven can be called via the main class ''org.scijava.minimaven.MiniMaven''. Just like real ''Maven'', you can start it directly in the directory:

<source lang="bash">
ImageJ-<platform> --mini-maven <command>
</source>

To get a list of supported commands, use the command <code>help</code>.

By default, MiniMaven will build the project specified by the ''pom.xml'' file in the current directory, recursing if it is an aggregate project. However, you can ask MiniMaven to look for a specific artifactId in an aggregate project's tree:

<source lang="bash">
ImageJ-<platform> --mini-maven -DartifactId=<artifactId> <command>
</source>

MiniMaven also heeds these properties:

* ''minimaven.offline'': do not try to connect to remote Maven repositories
* ''minimaven.updateinterval'': minimum age (in seconds) of a -SNAPSHOT artifact for MiniMaven to look for a newer one
* ''minimaven.verbose'': show more detailed log messages
* ''minimaven.debug'': show very detailed log messages, meant to debug MiniMaven itself
* ''mainClass'': used with the <code>run</code> command to override or set the main class to execute
