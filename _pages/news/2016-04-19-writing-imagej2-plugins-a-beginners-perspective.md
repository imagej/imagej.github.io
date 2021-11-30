---
title: "2016-04-19 - Writing ImageJ2 Plugins: A Beginner's Perspective"
---


{% capture  content %}
The following article was written by {% include person id='kkunzelm' %} as he researched how to write plugins for [ImageJ2](/software/imagej2). It is reproduced here as a [News](/news) post in the hope that it may help others, particularly during 2016 while the information continues to be most accurate and relevant.
{% endcapture %}
{% include notice icon="info" content=content %}




# Writing ImageJ2 Plugins: A Beginner's Perspective

## Preamble

Before you consider to write your own [plugin](/plugins) for [ImageJ](/software/imagej), please note that writing a [script](/scripting/script-editor) has a much lower barrier to entry than Java plugin development.

Also you may want to have a look at [Introduction\_into\_Macro\_Programming](/scripting/macro) as an easy way to automate repetitive tasks with existing tools and plugins.

## Finding information

-   The top-level source of information is [the ImageJ wiki](/).
-   The [Development](/develop) page is the best portal for aspiring ImageJ developers.
-   [ImageJ2](/software/imagej2) is available at: {% include github org='imagej' repo='imagej' label='imagej/imagej' %}
-   [Fiji](/software/fiji) is available at: {% include github org='fiji' repo='fiji' label='fiji/fiji' %}
-   For additional help, use the [ImageJ Forum](/discuss).

The search engines will point you to both `imagej.net` and `developer.imagej.net`. Avoid using `developer.imagej.net` for anything these days. It is a legacy site, in the process of being totally phased out. If you are looking for downloads, see the [Downloads](/downloads) page.

## Configure your environment

You will need:

-   Java
-   [IDE](/develop/ides) (for example: [Eclipse](/develop/eclipse), [NetBeans](/develop/netbeans) or [IntelliJ\_IDEA](/develop/intellij)) is highly recommended
-   [Git](/develop/git)
-   [Apache Maven](/develop/maven)
-   [ImageJ2 source code](/develop/source) is an optional help

Environments used for testing this guide:

-   Debian Jessie \| macOS 10.14.x
-   OpenJDK 1.8.x
-   NetBeans IDE version 8.0.2 \| IntelliJ IDEA 2019.2.2 (Community Edition)
-   Git 2.x
-   Apache Maven 3.x

[Git](/develop/git) is a source-code-management system with revision control.

[Maven](/develop/maven) is a build automation tool used primarily for Java projects.

Both Git and Maven have build in support in current versions of the IDEs mentioned above.

Earlier versions of the ImageJ wiki [mentioned another software tool](/develop/project-management), called [Jenkins](/develop/jenkins), which is according to Wikipedia "an open source continuous integration tool written in Java". This tool was later replaced by a similar working service called [Travis CI](/develop/travis). Tools like Maven and Travis CI make it more complicated for casual developers to understand the workflow of ImageJ Plugin development at the beginning. However, these tools are well maintained by the community so that you will not have to think about them too much initially and they facilitate the programming process. For example, concerning "Travis CI" it is enough to know that "Continuous Integration" means merging all developer working copies to a shared mainline several times a day. Here the work of multiple developers is compiled and tested on a single machine to ensure that the combined code produces a working project at any time. For the development of a single plugin for our personal use we can ignore "Travis CI" for the moment. It will be important if you want to share your plugin in the ImageJ updater or even contribute to the ImageJ project.

All [source code](/develop/source) is on [GitHub](/develop/github). As ImageJ nowadays is a rather complex project its development is split into several [ImageJ subprojects](/develop/architecture). For a beginner it is hard to understand the interaction of the different available projects which all contribute under the label "[SciJava](/libs/scijava)" to ImageJ2. The nice thing is, that Maven will help to pull in the necessary code from all ImageJ subprojects automatically with the help of configurations files which are supplied by the ImageJ2 developer community. The ImageJ wiki provides a very first overview of the [SciJava ecosystem](/develop/architecture) of ImageJ2.

To make Maven work we need so called `pom.xml` files. These configuration file contains information about the project and various configuration details used by Maven to build the project(s). The `pom.xml` files help to organize everything needed to build ImageJ. You can use any Maven-based project you want with that approach, not just ImageJ. So e.g. you can import {% include github org='fiji' repo='fiji' label='fiji/fiji' %} that way, or an individual plugin such as {% include github org='fiji' repo='AnalyzeSkeleton' label='fiji/AnalyzeSkeleton' %}.

In general, there are two alternative strategies to develop your plugin:

-   Use your IDE without Maven
-   Use your IDE with Maven

## Using NetBeans without Maven

When you build your own plugins with an IDE, the ImageJ project will link in all plugins as precompiled JAR dependencies (JAR files are archives for java projects).

Download the current JAR files, e.g. [imagej-2.0.0-SNAPSHOT-all.jar](http://jenkins.imagej.net/job/ImageJ/lastSuccessfulBuild/artifact/target/), which you intend to use as library in your local project.

You could also use the JAR file to compile your own plugins, which are distributed in the `Fiji.app/plugins` directory.

When you [download Fiji](/software/fiji/downloads), take care to select the right version of Fiji. The most prominent download option on top of the page is compiled with JDK 1.8, while you can download so-called "life-line" versions at the bottom of the page which are compiled with JDK 1.6 to ensure compatibility with older plugins not supported by the ImageJ2 Team. For details [look here](/news/2015-12-22-the-road-to-java-8).

In any case you need to open a new project, assign the project name, its directory location and add the JAR files as libraries.

-   {% include bc path='File|New Project'%}: Java Application (Project Name, Project Location)
-   Right click on the Project in the tree view {% include bc path='window|Properties'%}
-   {% include bc path='Libraries|Add JAR/Folder'%}: point to the JAR files you downloaded for ImageJ/Fiji.

A somewhat outdated but rather detailed description how to work with an older version of NetBeans (version 6.7) including bit of customization of the `build.xml` file can be found [here](http://www.dent.med.uni-muenchen.de/~kkunzelm/htdocs/6_software-netbeans.html).

{% include notice icon="warning" content='Please consider:

Using JAR works for local development, but it will cause you various problems later. For example, if you share your source code, you will need to commit this JAR along with your NetBeans project files to your repository, to ensure everyone else uses the same version of ImageJ that you do.' %}

## Build ImageJ with NetBeans, Git and Maven

Using Maven to develop your plugins is a much better approach. You will not have to commit any JAR files to source control. You can pin your code to fixed, known versions of its dependencies that will provide [reproducible builds](/develop/architecture#reproducible-builds) for many years to come.

Getting the ImageJ sources in NetBeans should be as simple as importing the source from the Git repository.

The following was adapted from the [Developing ImageJ in NetBeans](/develop/netbeans) page.

Import and build the project:

-   Run NetBeans
-   Choose {% include bc path='Team|Git|Clone...'%} from the NetBeans menu
-   For the Repository URL, enter: [`https://github.com/fiji/fiji`](https://github.com/fiji/fiji) or alternatively enter [`https://github.com/imagej/imagej`](https://github.com/imagej/imagej)
-   Click Next, check the `master*` branch, then Next again, then Finish
-   When prompted, click Open Project... in case of Error Messages click on "Resolve".

Launch the program:

-   Expand the "ImageJ Projects" project, then "Modules"
-   Expand the "ImageJ POM: User Interface" module
-   Double-click the "ImageJ Application" project to open it
-   Right-click the "ImageJ Application" project and choose "Run"
-   On the Main Class dialog, choose "net.imagej.Main"
-   To expand the projects you can also right click on the top-level "ImageJ Projects" and choose "Open Required Projects" (and "Close Required Projects" to close). During development you must select "Open Required Projects" before you can successfully do "Find Usages" in the "Open Projects" scope.

Do not expect to find the ImageJ sources after cloning {% include github org='imagej' repo='imagej' label='imagej/imagej' %} or {% include github org='fiji' repo='fiji' label='fiji/fiji' %}.

If you want to look at the source code to study how to program image analysis algorithms then you will need to clone other GitHub projects.

The repository {% include github org='imagej' repo='imagej1' label='imagej/imagej1' %}, for example, contains the source code of [ImageJ 1.x](/software/imagej), but it does not use Maven. The [ImageJA](/libs/imageja) project at {% include github org='imagej' repo='ImageJA' label='imagej/ImageJA' %} is a Mavenized version of ImageJ 1.x with a clean Git history. For curious people like me: the "A" in ImageJA was originally used for "Applet" and to differentiate the project from ImageJ itself.

{% include notice icon="info" content='Side note: I am not expert NetBeans user, therefore I could not figure out another way:

To import several projects from GitHub I always had to close all open project in NetBeans before I could import another project. If somebody knows a better way, please add here.' %}

## Build the ImageJ Tutorial Plugin with IntelliJ IDEA, Git and Maven

**Setup IntelliJ**

-   Make sure you have a version of Java SDK 1.8.x installed
-   Make sure to activate Maven and Git Plugins when installing IntelliJ
-   However these plugins can be activated in the main settings at any time

**Import and build the project:**

-   Run IntelliJ IDEA
-   Choose {% include bc path='File|New|Project from Version Control|Git'%} from the main menu

*ImageJ 1.x Plugin*

-   For the Repository URL, enter: [`https://github.com/imagej/example-legacy-plugin.git`](https://github.com/imagej/example-legacy-plugin.git) and choose a local folder you want the project to be stored in

*ImageJ2 Plugin*

-   For the Repository URL, enter: [`https://github.com/imagej/tutorials.git`](https://github.com/imagej/tutorials.git) and choose a local folder you want the project to be stored in

**Import**

-   Click Clone and all sources will be downloaded and opened as a new Project
-   If IntelliJ asks to import all Maven changes you have to allow this
-   Expand the Maven window which can be found on one of the edges in the IntelliJ window and select your project
-   Here you can right-click and "Run Maven Build" or alternatively press the green arrow above it in the Maven window to build your project
-   The build process will generate two `.jar` file under *\[project\_name\]/targets/* that can be installed in your local ImageJ installation

# Details of Writing Plugins

## Tutorials

-   For ImageJ 1.x: [Introduction into Developing Plugins](/develop/ij1-plugins) and [Example Legacy Plugin](https://github.com/imagej/example-legacy-plugin)
-   For ImageJ2: [Writing plugins](/develop/plugins) (Note: The instruction "Update your parent POM" in [Writing plugins\#Update\_your\_POM](/develop/plugins#update-your-pom) just means that the version number should be adjusted to reflect the latest available version of the parent POM file on GitHub.)
-   [ImgLib2 Examples](/libs/imglib2/examples)
-   [Developing ImgLib2](/libs/imglib2/developing)
-   [ImageJ Ops](/libs/imagej-ops)

## Getting Started

Start from an existing plugin as a template:

-   For ImageJ 1.x plugins: {% include github org='imagej' repo='minimal-ij1-plugin' label='imagej/minimal-ij1-plugin' %}
-   For ImageJ2 plugins: {% include github org='imagej' repo='tutorials' branch='master' path='maven-projects/simple-commands' label='simple-commands in imagej/tutorials' %}

Import it as a sample project into your IDE and modify this project according to your needs:

-   NetBeans: {% include bc path='File|Open Project'%}

The following lines are copied/cited from the `README.md` file of the `minimal-ij1-plugin`:

-   Edit the `pom.xml` file and change
    -   the `artifactId`
        -   Note: for ImageJ 1.x plugins the `artifactId` should contain a `_` character. If you write an ImageJ2 command (like the ones linked above in `simple-commands` tutorial) then the underscore is unnecessary.
    -   the `groupId`
        -   You should put a `groupId`. It is misleading to leave it off, because then `net.imagej` (or `sc.fiji` if you used `pom-fiji` as parent) will be inherited. And your project is probably not a core ImageJ project.
    -   the `version` (note that you typically want to use a version number ending in `-SNAPSHOT` to mark it as a work in progress rather than a final version)
    -   the `dependencies` (read how to specify the correct `groupId`/`artifactId`/`version` triplet here)
    -   the `developer` information
    -   the `scm` information
-   Remove the `Process_Pixels.java` file and add your own `.java` files to `src/main/java/<package>/` (if you need supporting files—like icons—in the resulting `.jar` file, put them into `src/main/resources/`)
-   Edit `src/main/resources/plugins.config`
    -   This is only needed for ImageJ 1.x plugins. For ImageJ2 commands, the information is provided by the `@Plugin` annotation at the top of the Java class.
-   Replace the contents of `README.md` with information about your project.

## Additional sample plugins

{% include github org='imagej' repo='tutorials' label='imagej/tutorials' %}

The imagej/tutorials are structured as individual projects. The files can live in a directory on its own outside the ImageJ or Fiji project. The `pom.xml` files of the `imagej/tutorials` pull in all the necessary dependencies for compiling via Maven.

## "One file to bind them all": parent `pom.xml` files

As the projects get more complex, read about the [Maven component structure of ImageJ/SciJava](/develop/architecture#maven-component-structure) and something which is called "[Bill of Materials](/develop/architecture#bill-of-materials)" or just BOM. A "BOM" is a list of dependencies at particular versions which are believed to be mutually compatible. The complexity of ImageJ/SciJava's dependencies is a tribute to the different organizations which are contributing with their independent projects to ImageJ/SciJava. There are several "parent" pom.xml files which are independently maintained for example by the ImageJ, [ImgLib2](/libs/imglib2) or [SCIFIO](/libs/scifio) organizations. Each of these organizations has developed source code components which depend on components within the other two organizations. This complicated network of dependencies is managed with the help of the parent `pom.xml` files, i.e. `pom-imagej`, `pom-fiji`, `pom-imglib2` etc. (see a list of all on the [ImageJ Architecture page](/develop/architecture#maven-component-structure)).

Initially I could not figure out where to put one of these `pom-xxx` files to use it as parent POM. I erroneously thought it should be downloaded from GitHub and copied somewhere in my ImageJ projects folders. However, one does not have to take care of the parent POM file at all! You just have to refer to it in the local `pom.xml` file of your intended plugin project in the section `<parent>`.

```xml
<parent>
  <groupId>net.imagej</groupId>
  <artifactId>pom-imagej</artifactId>
  <version>15.1.0</version>
  <relativePath />
</parent>
```

If `pom-imagej` is the parent POM file, then the local `pom.xml` could override the following configuration sections:

```xml
<name>
<description>
<url>
<inceptionYear>
<organization>
<licenses>
<developers>
<contributors>
<scm>
<issueManagement>
<ciManagement>
```

In the local `pom.xml` at least the sections:

```xml
<groupId>
<artifactId>
<version>
```

should be changed. Optionally also:

```xml
<name>
<description>
<url>
```

Finally add at least one of the following dependencies for ImageJ plugin support:

```xml
<dependencies>
    // support for ImageJ2 plugins
    <dependency>
        <groupId>net.imagej</groupId>
        <artifactId>imagej</artifactId>
    </dependency>
    // support for ImageJ 1.x plugins
    <dependency>
        <groupId>net.imagej</groupId>
        <artifactId>ij</artifactId>
    </dependency>
</dependencies>
```

## Further readings

-   [README.md](https://github.com/imagej/minimal-ij1-plugin/blob/master/README.md) of the [Minimal Maven based ImageJ 1.x plugin](https://github.com/imagej/minimal-ij1-plugin)
-   Learn more about [ImageJ/SciJava dependencies](/develop/maven#how-to-find-a-dependencys-groupidartifactidversion-gav)
-   [ImageJ Maven FAQ](/develop/maven-faq)

# Other References

-   [ImageJ Forum Thread 1151](http://forum.imagej.net/t/java3d-issue-bonej-with-latest-fiji-version-problem-solved/1151)
-   [ImageJ Forum Thread 1290](http://forum.imagej.net/t/guide-to-make-a-plugin-as-official-fiji-plugin/1290)
-   [ImageJ Forum Thread 1364](http://forum.imagej.net/t/ij1-or-ij2-style-for-plugin-development/1364)

<!-- -->

-   Git tutorial: [Git in 15 min](https://try.github.io/levels/1/challenges/1)
-   Web interface for git: [GitHub](/develop/github)

and all other links cited in the text!

# Appendix

## How do I find dependencies?

You can search by class for Maven artifacts. For example, [search for `ij.plugin.PlugIn`](https://maven.scijava.org/#nexus-search;classname~ij.plugin.PlugIn). There is also a "Find Jar For Class" helper script in Fiji which does a similar thing for JAR files currently on ImageJ's classpath.

If you are comfortable with command-line tools, you can also use the [Maven Dependency Plugin](https://maven.apache.org/plugins/maven-dependency-plugin/) which enables you to do things like download local copies of the dependency jars for inspection.

Also [mvnrepository.com](https://mvnrepository.com) is a good resource to find repositories with code you can easily copy and paste in your `pom.xml`.

## Manage Java versions

On Linux several java version can be installed. Select the preferred version in a terminal window (e.g. bash):

```sh
update-alternatives --config java
```

Note: It might be necessary to use `sudo`.

If necessary, tell NetBeans to use JDK 1.8 as the default JRE for new projects (i. e. on Debian Linux: {% include bc path='Project Properties|Build|Compile...'%} `/usr/lib/jvm/java-1.8.0-openjdk-amd64`) or alternatively set the `netbeans_jdkhome` property in your NetBeans config file. It should be in the local NetBeans directory, for example `./netbeans-8.0/netbeans.conf`.

## Where can I find example plugins?

-   [ImageJ Tutorials](https://github.com/imagej/tutorials/)
    -   In NetBeans: {% include bc path='Team|Git|Clone'%}
    -   Repository URL: [https://github.com/imagej/tutorials](https://github.com/imagej/tutorials)
    -   Edit "destination" directory
    -   Next
    -   Select `master*`
    -   Next
    -   Finish

## What is the directory structure for a plugin?

This text was adapted from the [Maven](/develop/maven) page.

The directory structure of a very simple demo project looks like:

```
DemoPlugin
|-- pom.xml
|-- src
|   !-- main
|       |-- java
|       |   !-- MyPlugin.java
|       !-- resources
|           !-- sample-image.tif
```

After compiling your java files, Maven automatically generates the content of the `target` folder. Therefore: never commit any files from `target` to Git! You can tell Git to ignore these files by using a [.gitignore](https://help.github.com/articles/ignoring-files/) file (usually you start by copying [an existing one](https://github.com/imagej/imagej2/blob/95722503b4d2243b2818f8a7b5c2cdf863c5da69/.gitignore) from another project)

```
!-- target
    |-- classes
    |   |-- sample-image.tif
    |   |-- META-INF
    |   |   !-- json
    |   |       !-- org.scijava.plugin.Plugin
    |   !-- MyPlugin.class
    |-- generated-sources
    |   !-- annotations
    |-- maven-status
    |   !-- maven-compiler-plugin
    |       !-- compile
    |           !-- default-compile
    |               |-- createdFiles.lst
    |               !-- inputFiles.lst
    !-- test-classes
```

In general:

Put your `.java` files under `src/main/java/` and the other files you need to be included into `src/main/resources/`.

Should you want to apply the best practices called "regression tests" or even "test-driven development" put your tests' `.java` files to `src/test/java/` and the non-`.java` files you might require go into `src/test/resources/`.

More information about Maven's standard directory layout can be found on the [Maven website](https://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html).

## What does a minimal `pom.xml` look like?

This text was adapted from the [Maven](/develop/maven) page.

This is a very simple example:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
  http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>org.mywebsite</groupId>
  <artifactId>my-uber-library</artifactId>
  <version>2.0.0-SNAPSHOT</version>
</project>
```

The first 6 lines are of course just a way to say "Hi, Maven? How are you today? This is what I would like you to do...".

The only relevant parts are the `groupId`, which by convention is something like the inverted domain name (similar to the Java package convention), the name of the artifact to build (it will be put into `target/`, under the name `<artifactId>-<version>.jar`). And of course the version.

While the example `pom.xml` above shows the general idea, for ImageJ more details have to be considered. Therefore it is better to start with an existing `pom.xml` file, for example the one from {% include github org='imagej' repo='minimal-ij1-plugin' label='imagej/minimal-ij1-plugin' %}. Copy it to your project and modify it as needed.

## Are the underscores still needed for plugins to be visible in IJ or Fiji?

From [ImageJ Forum Thread 1020](http://forum.imagej.net/t/mavenization-and-debugging-in-eclipse/1020):

Underscores are needed if your plugin is an ImageJ 1.x style plugin. I.e.: does it implement `ij.plugin.PlugIn` or `ij.plugin.filter.PlugInFilter?` Then put an underscore in your JAR file and/or in your class name.

If you write an ImageJ2 command plugin (i.e.: implement the `org.scijava.command.Command` interface, with an `@Plugin` annotation) then the underscore is no longer necessary.

## Make the plugins appear in the menus

Example, which sets the `plugins.dir` property so that the plugin appears in the menus when launched from an IDE:

-   {% include github org='imagej' repo='minimal-ij1-plugin' commit='780286866ee67ffdc6506217c3f25d9a0ac15f6d' source='Process_Pixels.java#L176-L180' label='Process_Pixels.java' %}

Setting `plugins.dir` is only necessary for ImageJ 1.x style plugins. If you write an ImageJ2 command, it should appear in the menus regardless.

## NetBeans: what is the difference between Ant and Maven? Or: `build.xml` vs. `pom.xml`

From [StackOverflow \#15121928](http://stackoverflow.com/a/15122181):

> Ant is a build tool primarily, this means it knows how to compile and package source code and run tests, but has no ability to manage project dependencies. Ant uses build.xml files to define where to find the source code and which steps to take to build your project.
>
> Maven is more than just a build tool, it is a project management tool. It allows you to define dependencies in the `pom.xml` proect definition, as well build, test and distribute the application. It also allows sub projects, parent projects and there exist many plugins for many other features. Maven will automatically download the dependencies and manages these dependencies between projects.

Maven is declarative, whereas Ant is procedural. In Ant, you say "do X, then do Y, then do Z." Whereas in Maven, you say "my code is here, my resources are there, and please use these plugins." One advantage of the latter is that Maven provides a standardized build sequence (called the "build lifecycle") making it compatible with all the major IDEs.

## How to migrate an existing project to a Maven project?

**In Netbeans**

Adapted from [StackOverflow \#7548008](http://stackoverflow.com/q/7548008):

-   Backup your project.
-   Create a new project with name `NewMavenProject`.
-   Close your original project.
-   Copy the `pom.xml` from {% include github org='imagej' repo='minimal-ij1-plugin' label='imagej/minimal-ij1-plugin' %} or other appropriate template.
-   Modify the `pom.xml`'s project specific settings (e.g. project name, dependencies).
-   Delete the `build.xml` and the whole `nbproject` folder.
-   Move and rename the folder to `src/main/newproject` (`newproject` is the new name).
-   Move `src/java` to `src/main/java`.
-   Open your project again in NetBeans. It should be a Maven project now.
-   Delete the unnecessary `NewMavenProject` project.

**In IntelliJ IDEA**

-   Create a new Maven Project with {% include bc path='File|New Project'%}
-   Select Maven on the left and click *Next*
-   Choose your custom GroupID (eg. com.yourwebsite) and an ArtifactID as single identifier for this project (eg. project\_name)
-   Note that for ImageJ 1.x Plugins a "\_" in the project name/ identifier is required for ImageJ 1.x Plugins
-   The project structure required by Maven will be created for you
-   For Git support (recommended): {% include bc path='VCS|Import into Version Control|Git'%}
-   Copy all `.java` files into *\[project\_name\]/src/main/java*
-   Copy your `plugins.config` file into *\[project\_name\]/src/main/resources*
-   In the main project directory *\[project\_name\]/* you can find a `pom.xml` which has to be edited like the example shown in the previous chapter
-   If your IDE asks to import all Maven changes you have to allow this
-   Expand the Maven window which can be found on one of the edges in the IntelliJ window and select your project
-   Here you can right-click and *Run Maven Build* or alternatively press the green arrow above it in the Maven window to build your project
-   The build process will generate two `.jar` file under *\[project\_name\]/targets/*

## Enable the ImageJ 1.x UI, instead of the ImageJ2 Swing UI

From [ImageJ Forum Thread 1364](http://forum.imagej.net/t/ij1-or-ij2-style-for-plugin-development/1364/3):

Add the following dependency to your POM:

```xml
<dependency>
  <groupId>net.imagej</groupId>
  <artifactId>imagej-legacy</artifactId>
  <scope>runtime</scope>
</dependency>
```

That will enable the ImageJ 1.x UI, instead of the ImageJ2 Swing UI which is otherwise the default.

## What is it all about with this Java 6 and Java 8 stuff?

From [ImageJ Forum Thread 1151](http://forum.imagej.net/t/java3d-issue-bonej-with-latest-fiji-version-problem-solved/1151/6):

The current situation with respect to Java 6 vs. Java 8, as well as the ramifications there regarding Java 3D, is basically:

-   If you download "vanilla" [ImageJ2](/software/imagej2) (author's note: in the context of software "vanilla" means software used as originally distributed without any customizations or updates applied to them) from the [Downloads](/downloads) page, you get a "Java 8" version from February 2016.
-   If you [download the latest Fiji](/software/fiji/downloads) you get the newest "Java 8" version—i.e., with Java-8 update site. This includes the Java 3D 1.6 (SciJava fork) along with all Fiji plugins (except for [TrakEM2](/plugins/trakem2)) updated to work with it.
-   If you [download a Life-Line version of Fiji](/software/fiji/downloads#life-line-fiji-versions) and fully update it, you'll have the newest (probably the final) "Java 6" version including the latest Java-6-compatible plugin versions. No Java 3D until you run the [3D Viewer](/plugins/3d-viewer) for the first time and it gets auto-installed. Those plugin versions are frozen: the ImageJ/Fiji developers are in the process of migrating everything to Java 8, and are only uploading new versions of everything to the Java-8 update site now, to avoid breaking the stable Java-6 versions of everything.

Ultimately, the ImageJ/Fiji developers will push all the Java-8 stuff back to the core ImageJ and Fiji sites. But not until the ImageJ/Fiji developers add a launch check that verifies your version of Java is new enough—and if not, tells you how to upgrade it. Ihe ImageJ/Fiji developers will definitely archive the final Java-6-compatible versions of ImageJ and Fiji when they complete that transition.

Note: You can check the Java version as [described here](/learn/troubleshooting#checking-the-java-version).

More information can be read here: [2015-12-22 - The road to Java 8](/news/2015-12-22-the-road-to-java-8)

## Make a redistributable package from a locally customized Fiji

Turn your local customized Fiji into a redistributable package that can then be installed on other machines e.g. in your lab: use the [Make Fiji Package](/plugins/make-fiji-package) command.

## Tests wit JUnit5

In IntelliJ IDEA you may want to make sure that the JUnit5 Plugin is activated. The next step would be to append the following lines to your `pom.xml` file:

```xml
<dependency>
<groupId>org.junit.jupiter</groupId>
    <artifactId>junit-jupiter-engine</artifactId>
    <version>5.5.1</version>
    <scope>test</scope>
</dependency>
<dependency>
    <groupId>org.junit.platform</groupId>
    <artifactId>junit-platform-runner</artifactId>
    <version>1.5.1</version>
    <scope>test</scope>
</dependency>

<build>
    <plugins>
        <plugin>
            <!-- fix maven tests -->
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-surefire-plugin</artifactId>
            <version>3.0.0-M3</version>
            <configuration>
                <excludes>
                    <exclude>some test to exclude here</exclude>
                </excludes>
            </configuration>
        </plugin>
    </plugins>
</build>
```

{% include notice icon="note" content="If you want to test GUI tests with TravisCI you have to activate a virtual display as described in the Travis CI chapter." %}

## Continuous Integration with Travis CI

If you want to share your plugin in the ImageJ updater automatically [Automatic Update Site Uploads](/update-sites/automatic-uploads), contribute to the ImageJ project [Fiji/Contribution requirements](/contribute/fiji) or work in a team with multiple developers, you may want to build, test and deploy your Plugin with [Travis CI](/develop/travis). If you are hosting your code in a public [GitHub](/develop/github) repository this service is free for you. After signing in with your [GitHub](/develop/github) account you can activate single repositories for [Travis CI](/develop/travis). Travis then automatically clones your repository with every change and runs a build according to the `.travis.yml` configuration file in your root directory.

```yml
    # specify compiler
    language: java
    sudo: false # faster builds
    jdk: openjdk8

    # maven build
    install: true
    script: mvn clean verify

    # cache maven dir for performance
    cache:
      directories:
        - $HOME/.m2
```

In case you are working with GUI tests, you may want to activate a virtual display as well:

```yml
# virtual display variable for gui tests
    dist: xenial
    services:
      - xvfb
```

## JavaFX JAR not found

Add this to your pom.xml:

```xml
<build>
    <plugins>
        <!-- Fix JavaFX support -->
        <plugin>
            <groupId>com.zenjava</groupId>
            <artifactId>javafx-maven-plugin</artifactId>
            <version>8.8.3</version>
            <configuration>
                <mainClass>your.package.with.Launcher</mainClass>
            </configuration>
        </plugin>
    </plugins>
</build>
```

## Log4j warning in IntelliJ IDEA

Some of the tutorials seem to be missing a configuration file for Log4. IntelliJ will warn you about this as soon as you try to try to build the project:

```
log4j:WARN No appenders could be found for logger (org.bushe.swing.event.EventService).
log4j:WARN Please initialize the log4j system properly.
log4j:WARN See http://logging.apache.org/log4j/1.2/faq.html#noconfig for more info.
```

The missing config file is called `log4j.xml` and has to be located in `.../src/main/resources/`:

```xml
<!DOCTYPE log4j:configuration SYSTEM "log4j.dtd">
<log4j:configuration debug="true" xmlns:log4j='http://jakarta.apache.org/log4j/'>

    <appender name="fileAppender" class="org.apache.log4j.RollingFileAppender">
        <param name="File" value="demoApplication.log"/>
        <layout class="org.apache.log4j.PatternLayout">
            <param name="ConversionPattern" value="%d{yyyy-MM-dd HH:mm:ss} %-5p %c{1}:%L - %m%n" />
        </layout>
    </appender>

    <root>
        <priority value ="debug"></priority>
        <appender-ref ref="fileAppender"></appender-ref>
    </root>

</log4j:configuration>
```

