{{ImgLibMenu}}
== Introduction ==

The [[ImgLib2]] library uses [[Maven]] to manage project dependencies. One advantage of this approach is nice integration with various development environments ([[IDEs]]).

Because people tend to have differing IDE configurations, we do not put project metadata files (e.g., <code>.classpath</code>, <code>.project</code> and <code>.settings</code> for Eclipse) into the git repository. Instead, the IDE can use Maven's <code>pom.xml</code> file directly to manage your dependencies in a better way.

== Getting the code ==

You can clone the ImgLib2 code using Git with the URL: '''git://github.com/imglib/imglib2'''

== Developing ImgLib2 with Eclipse ==

To develop ImgLib2 in Eclipse, follow these steps:

# [[Using Maven with Eclipse|Install the Maven plugin]]
# Choose {{bc | File | Import}} from the Eclipse menu
# Select "Existing Maven Projects" and click Next
# For the Root Directory, specify the path where you cloned ImgLib2
# From the projects list, leave all items checked
# Click Finish

For fresh installs, it will initially take some time (a few minutes) for Maven to download all the dependencies for both its own plugins, and for ImgLib2. This is a one-time cost. After that, Maven will check for module updates once a day, which is generally fast.

Once you have the ImgLib2 projects within Eclipse, you can reap the benefits of the improved dependency management. For example, if you have the <code>imglib2</code> and <code>imglib2-algorithms</code> projects open, the <code>imglib2-algorithms</code> project will have an Eclipse project build dependency on <code>imglib2</code>. If you then close the <code>imglib2</code> project, the dependency within <code>imglib2-algorithms</code> with automatically become a library dependency to <code>imglib2-2.0-SNAPSHOT.jar</code>, rather than the project.


== Developing ImgLib2 with IDEA ==

IntelliJ IDEA comes with built-in support for Maven.

See [[Developing ImageJ in IntelliJ IDEA]].


== Developing ImgLib2 with NetBeans ==

NetBeans comes with built-in support for Maven.

See [[Developing ImageJ in NetBeans]].

== Developing ImgLib2 with command line tools ==

You can use the mvn command line tool to build ImgLib2. Just type "mvn" with no arguments. By default, Maven will compile the code, run unit tests, create a JAR file and install it in your local Maven repository (typically found in <code>~/.m2/repository</code>). Maven does its work in a subfolder called <code>target</code> which is where you'll find compiled classes and JAR artifacts.

For more on using the Maven command line tool, see [http://maven.apache.org/run-maven/index.html Building a Project with Maven] on the Maven web site.

[[Category:ImgLib]]
[[Category:Tutorials]]
[[Category:Development]]
