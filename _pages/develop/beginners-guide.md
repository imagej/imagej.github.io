---
title: "A beginner's guide to starting a Fiji project"
---


{% capture  content %}
The following article is modified from [this article](/news/2016-04-19-writing-imagej2-plugins-a-beginners-perspective) originally written by {% include person id='kkunzelm' %} as he researched how to write plugins for [ImageJ2](/software/imagej2), currently being rebranded to Fiji. It was updated by {% include person id='andmccall' %} after going through the same process several years later. This new version is written assuming the user is interested in writing a project for [Fiji](/develop/plugins), which relies heavily on the [Scijava plugin framework](/develop/plugins#what-makes-up-the-scijava-plugin-framework). Some no-longer-recommended alternative methods were also removed from this guide to keep it as simple as possible. 
{% endcapture %}
{% include notice icon="info" content=content %}

# Writing Fiji Plugins: An updated Beginner's Perspective

## Preamble

Before you consider to write your own [plugin](/plugins) for [Fiji](/software/Fiji), please note that writing a [script](/scripting/script-editor) has a much lower barrier to entry than Java plugin development.

Also you may want to have a look at [Introduction\_into\_Macro\_Programming](/scripting/macro) as an easy way to automate repetitive tasks with existing tools and plugins.

Most of this guide is written from the perspective of using IDEA IntelliJ as your IDE. While everything can be done when using the other recommended IDEs, the specifics may differ from what you see here.

Lastly, this new guide exclusively covers Scijava-based Fiji projects, and will not cover or link to any information on ImageJ-1.x plugin development. Appropriately leveraging the tools in Scijava and Imglib2 makes plugin development, particularly handling input and output, significantly easier and more efficient. This guide is meant as a rough overview of the entire process and deliberately does not go into great detail on any single topic. If you are interested in ImageJ-1.x plugin development, see the [ImageJ-1.x plugin development page](/develop/ij1-pluins). 

## Finding information

-   The top-level source of information is [the ImageJ wiki](/).
-   The [Development](/develop) page is the best portal for aspiring ImageJ developers.
-   [Fiji](/software/fiji) is available at: {% include github org='fiji' repo='fiji' label='fiji/fiji' %}
- 	Use the [Javadoc](/develop/javadoc) to find class documentation
-   For additional help, use the [ImageJ Forum](/discuss).

## Overview of terminology
Most of the links of this section are to much more detailed explanations of these terms elsewhere on the wiki. The discussion here is to give a broad overview of these for those who may have never seen them before.

### ImgLib2
ImgLib2 is one of the foundational Java libraries used by Fiji, responsible for all the underlying data structures used for images. Basically, when you open an image in Fiji, the underlying data structure is a type of ImgLib2 [Img](https://javadoc.scijava.org/ImgLib2/net/imglib2/img/Img.html) class, though with many layers piled on top of it. ImgLib2 also has many useful tools for data access and processing. It's highly recommended to read the [ImgLib2 publication](https://doi.org/10.1093/bioinformatics/bts543) to get an idea of how data is stored and accessed at its most fundamental level. 

### Scijava
[Scijava](/libs/scijava) is a collection of different libraries that provides very useful interfaces between you as a developer, and the user, as well as between you and the underlying data structrues and tools. This includes many powerful [services](/libs/scijava#services) that are available as [parameters](/scripting/parameters) through any instance of Fiji. 

### IDE (Intgrated Development Environment)
An [IDE](/develop/ides) is where you will write your code. It's highly recommended to use [IntelliJ\_IDEA](/develop/intellij), [NetBeans](/develop/netbeans) or [Eclipse](/develop/eclipse). 

### Maven
[Maven](/develop/maven) is a build tool that packages the java code into jar files that the Fiji can recognize, and helps with library management for your project. Maven comes bunlded with the major java IDEs. Maven properties are managed through the [pom.xml](/develop/building-a-pom) file, discussed further below. 

### Git and Github
[Git](/develop/git) is a version control tool that can be used to upload projects to a repository, and which also comes bundled with the major IDEs. [Github](/develop/github) is an online repository for storing and managing git repositories, many of which are open-source.

### Scijava Maven Repository
The [Scijava Maven Repository](https://maven.scijava.org/#welcome) is a repository of Maven built projects, called artifacts, with included jar files. While Maven repositories, including the Scijava repository, are related to the Maven build tool and elements of the pom.xml file are important for creating a Maven Repository artifact, it can be helpful to think of these as fairly distinct from one another (similar to Git and Github). Especially since you can use the Maven build tool, but not store your builds in any Maven repository. Packaging and storing your project into the Scijava Maven Repository is not essential, as you can distribute your project strictly via an [update site](/update-sites), but it is useful to have one available for other developers and [PyImageJ](/scripting/pyimagej) users.

## Configure your environment

You will need:

-   Java 1.8 JDK (version 1.8 is also referred to as Java 8). It's recommended to use [Azul Zulu](https://www.azul.com/downloads/?package=jdk#zulu) JDK.
-   [IDE](/develop/ides) (recommended: [IntelliJ\_IDEA](/develop/intellij), [NetBeans](/develop/netbeans) or [Eclipse](/develop/eclipse))
-	[Github](https://github.com/) account.
-   If you want to release to a Maven Repository: unbundled [Git](https://git-scm.com/downloads)
-   If you want to release to a Maven Repository: bundled [Apache Maven](/develop/maven)
-   [Fiji source code](/develop/source) is an optional help

Environments used for testing this guide:

-   Windows 10 and 11, x86_64
-   Azul Zulu 1.8.x
-   IntelliJ IDEA 2019.2.3 and 2024.3.1 (Community Edition)
-   Git 2.x
-   Apache Maven 3.x

All [source code](/develop/source) is on [GitHub](/develop/github). As Fiji nowadays is a rather complex project its development is split into several [subprojects](/develop/architecture). For a beginner it is hard to understand the interaction of the different available projects which all contribute under the label "[SciJava](/libs/scijava)" to Fiji. The nice thing is, that Maven will help to pull in the necessary code from all Fiji subprojects automatically with the help of configurations files which are supplied by the Fiji developer community. The ImageJ wiki provides a very first overview of the [SciJava ecosystem](/develop/architecture) of Fiji.

To make Maven work we need the so called `pom.xml` files. This configuration file contains information about the project and various configuration details used by Maven to build the project(s). The `pom.xml` files help to organize everything needed to build your project. You can use any Maven-based project you want with that approach, not just Fiji. So e.g. you can import {% include github org='fiji' repo='fiji' label='fiji/fiji' %} that way, or an individual plugin such as {% include github org='NicoKiaru' repo='LimeSeg' label='LimeSeg' %}.

In general, there are two alternative strategies to develop your plugin:

-   Use your IDE without Maven
-   Use your IDE with Maven (recommended)

## Testing your environment using the Fiji Tutorial Plugin with IntelliJ IDEA, Git and Maven

**Setup IntelliJ**

-   Make sure you have a version of JDK 1.8.x installed (Note: this version may change in the near future, to JDK 21)

**Import and build the project:**

-   Run IntelliJ IDEA
-   Choose {% include bc path='File|New|Project from Version Control|Git'%} from the main menu

*Fiji Plugin*

-   For the Repository URL, enter: [`https://github.com/imagej/tutorials.git`](https://github.com/imagej/tutorials.git) and choose a local folder you want the project to be stored in

**Import**

-   Click Clone and all sources will be downloaded and opened as a new Project
-   If IntelliJ asks to import all Maven changes you have to allow this
-   Using the project files viewer, open the class file tutorials/java/howtos/src/main/java/howto/ui/SwingExample. 
-	Near the upper right corner, you should see a play button next to a drop-down. Set the drop-down to 'Current File' and click the play button. This should run the class and open the Fiji UI.
-	Note: if the play button is grayed out, you probably need to setup your JDK in IntelliJ. Go to {% include bc path='File|Project Structure...|Project' %} and set the SDK to the JDK you installed.

The howtos project consists of many tutorials and guides, many of which can be run in a similar way as the Swing UI example. Any class with a `public static void main(final string args[])` method can be attempted to be run, though not all of them will do something that can be directly observed. These tutorials are a great resource for learning various aspects of Fiji and Scijava code writing.

Another project in this git repository is more illustrative of what a simple plugin project would look like, the `swing-example` project. Within the java folder of this project, you should find three non-runnable classes, and a runnable `SwingExample` class. The `DeconvolutionCommand` and `DeconvolutionCommandSwing` are both implementing the `Plugin` interface, making them discoverable by the `PluginService` of Scijava when Fiji is opened. You can add these commands to your Fiji by:

-	Expand the Maven window which can be found on one of the edges, usually the right side, in the IntelliJ window. Expand through {% include bc path='ImageJTutorials|Swing UI Command|Lifecycle' %} then run install. This builds just the `swing-example` project, rather than building every project as green arrow button at the top would. 
-	Once the project is built, there should be a new `target` directory within the file viewer that contains two `.jar` files. Transfer the jar file that does not end in -sources to a Fiji intallation's jars directory. Files can be dragged from the IntelliJ file viewer directly to Windows explorer. 
-	Open Fiji and you should now see a new `Deconvolution` menu option at the top that has both commands available. 

# Basic workflow for a new Fiji project

## Tutorials

-   For Fiji: [Writing plugins](/develop/plugins) (Note: The instruction "Update your parent POM" in [Writing plugins\#Update\_your\_POM](/develop/plugins#update-your-pom) just means that the version number should be adjusted to reflect the latest available version of the parent POM file on GitHub.)
-   [ImgLib2 Examples](/libs/imglib2/examples)
-   [Developing ImgLib2](/libs/imglib2/developing)
-   [ImageJ Ops](/libs/imagej-ops)

## Getting Started

Create a new Java project:

-   IntelliJ: {% include bc path='File|New|Project...'%}

Set your build system to Maven, and set your JDK to the Java 8 SDK that you installed. Creating the project will automatically generate a standard folder structure that is used by Fiji and Scijava projects, as well as the pom.xml file. 

You will need to edit your pom.xml file to work properly for Fiji development. Base your POM off of [this POM guide](develop/building-a-pom) with the following considertations:

-	Update the pom-scijava version. To determine the pom-scijava version to use: first determine the current Fiji version (update Fiji and click the Status bar, the first version number is the Fiji version), then navigate to {% include github repo='fiji' label='Fiji github' %}, click the drop-down where it says 'master', go to the tags section and find the current Fiji version. Finally, select the pom.xml file for this release of Fiji, and the listed pom-scijava version is the one you would want to use for your project. 
-   Your `artifactId`: This should match the name of your project, but without any spaces or special characters. If you wish to follow the style used by Fiji and Scijava developers, it would be your project name in all lower-case characters and '-' for spaces.
-   Your `groupId`: The groupId is generally the reversed domain name of the group your are developing for. If you are solo-developing a project, the current typical convention is to use net.<github username> as the groupId. 
-   the `version`: It's recommended to use [Semantic versioning](semver.org) for your projects. Note that you typically want to use a version number ending in `-SNAPSHOT` to mark it as a work in progress, the removal of this SNAPSHOT tag can happen automatically through version release to the Maven Repository (covered below). 
-   Add your `dependencies`: Common dependencies are listed in the POM guide. 
-   Add the `developer` information
-   Add the `scm` information based on the project's github repo.

Once you have your pom.xml file configured, you can add a new Java class file to the src/main/java folder to start writing your code. The structure of this file will be similar to that in the SwingExample discussed above, and for more details, see the guies in the Tutorials section. For guidance on how to write Java code for SciJava plugins, see the tutorials above. 

### Further readings

-   Learn more about [ImageJ/SciJava dependencies](/develop/maven#how-to-find-a-dependencys-groupidartifactidversion-gav)
-   [ImageJ Maven FAQ](/develop/maven-faq)

## Building and testing your project
Unlike the [Fiji tutorials repository](https://github.com/imagej/tutorials.git), your project probably does not have multiple build targets, thus when your code is ready, you can just use the green arrow in the Maven panel to build your project. This will package your classes into a `jar` file in the `target` folder. The generated `jar` file (the one with no additional extension) can be placed in Fiji's `jars` folder, and if your project is a Command with the proper @Plugin annotation it should be automatically recognized the next time Fiji is started.

In addition to testing your project by running it through Fiji, you can usually access and test your project directly from your IDE by utilizing runnable Java classes, structured like the `SwingExample` file from the [Fiji tutorials](https://github.com/imagej/tutorials.git). Such classes are generally placed in the `src/test/java/` folder so that they are not distirubted with the main `.jar` file generated when building. These files can be run directly from IntelliJ IDEA using the green arrow `run` button at the very top of the window (different than the Maven panel run button).

Going a step further, testing can be done automatically on every build using the [JUnit5](https://junit.org/junit5/) testing framework. For these unit tests to work properly, the pom.xml file will need to be modified as demonstrated in the Appendix "Tests wit JUnit5" section below.

## Using Github
Most of the GitHub functionality can be managed directly within IntelliJ under the `Git` menu. The most common ones: {% include bc path='Git|Commit'%} is used to mark changes that have been made to your project as a `commit`. {% include bc path='Git|Push'%} is used to upload those changes to the GitHub repository. You can also manage your branches through the IDE's `Git` menu. After your initial release, it's recommended that you push any in-progress commits to a non-master branch and only merge this branch onto `master` once the code is in a working state.

### Add a license
Establishing the copyright rules for your project is a very important step, and is done by setting the project's license, generally done through setting properties in the pom.xml file and adding the license text in a LICENSE.TXT file that is uploaded to your github repository. A great overview of copyright and licensing, and why it is important, can be found [here](https://focalplane.biologists.com/2023/05/06/if-you-license-it-itll-be-harder-to-steal-it-why-we-should-license-our-work/), and information on the licensing of Fiji and related projects can be found [here](/licensing).

## Releasing your project
Once your project is in a ready state (don't forget the [SciJava philosophy](/develop/releasing) of release early, release often), there are a couple of options for releasing your project to others. Doing both of them is recommended, though they are no interdepedent so you may do only one. 

### To Maven Repository with Github actions
Deploying to the [Scijava Maven Repository](https://maven.scijava.org/#welcome) is most commonly done by, and also important for, libraries to be used by other developers, since this makes them easy to add as a dependency for other projects. However, depositing your project into a Maven Repositroy has some benefits for small plugins as well, the most notable being that it allows [PyImageJ](/scripting/pyimagej) to be easily [initialized with access to your plugin](https://py.imagej.net/en/latest/Initialization.html#including-fiji-plugins). It also maintains a backlog of all previously released instances and source code for your plugin, allowing users to specifically download older versions. Below you will find a streamlined overview of the standard process for uploading your project to the SciJava Maven Repository for the first time. This overview deliberately makes some probably-true assumptions and omits unnecessary details based on those assumptions. For a much more detailed overview of this process see the [development lifecycle page](/develop/releasing).

First, you will need to do the following:

-	Add `<releaseProfiles>deploy-to-scijava</releaseProfiles>` to the `<Properties>` section of your pom.xml file. This marks the project as being released to the SciJava repository. 
-	If your project is currently on a personal Github account, [create a Github organization](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/creating-a-new-organization-from-scratch) and transfer your project to it. Creating a GitHub organization is free, easy, and does not require a separate account. Once the project is transfered, request that the new organization be granted the authorization secrets to deploy to the Scijava Maven Repository on the [Image.sc forum](https://forum.image.sc/). 

After these are both complete, you need to (in order):
1.	Clone the [Scijava Scripts](https://github.com/scijava/scijava-scripts) GitHub repository to your local computer. 
2.	Add the folder containing the cloned Scijava Scripts to your operating system's PATH environment variable. 
3.	Navigate to your project's folder containing the `pom.xml` file, right-click and select `Git Bash Here`. 
4.	Type `github-actionify.sh` to run a simulation of the github actionify script. If necessary, address any issues or errors. Once everything looks good, type `github-actionify.sh -f` to run the real action. The github actionify script will create new files in your project, push them to your project's GitHub repository.

Once you have completed all these steps, your project is ready to regularly be deployed as an artifact to the SciJava Maven Repository. All pushes to your GitHub repository `master` branch will result in the new GitHub actions, created by the github-actionify script, to deploy an artifact to the Snapshots section of SciJava Maven. To release a complete version, open Git Bash at your projects pom.xml folder again, and run `release-version.sh`. You will be asked which version you want to release (typically your current version number without `-SNAPSHOT`), and the script will do several things:

-	Check the format of your pom.xml file to ensure everything is in order. You may need to add the --skip-version-check option when running the script if the [SciJava Parent POM](https://github.com/scijava/pom-scijava) Maven deployment is ahead of the current Fiji version, which it often is.
-	Create and push a GitHub tag, consisting of the source code for that specific version.
-	Deploy the Maven artifact for the version provided to the Releases section of the SciJava Maven Repository.
-	Automatically iterate to the next -SNAPSHOT version for your `master` branch, and push this to GitHub.

After releasing a new version, your plugin should be available through the SciJava Maven Repository, and you are ready to work on your next version. 

### To ImageJ update site
Unlike the Maven Repository, an [ImageJ update site](/update-sites/index) does not store multiple versions of your project, only the most recently uploaded one. However, an update site is the means through which a typical Fiji user would be acquiring the tool you created, particularly for plugins. Detailed instructions on how to create and upload to an update site can be found [here](/update-sites/setup). Instructions to add your update site to the standard Fiji update manager list can be found in the introduction [here](/list-of-update-sites).

## Other References

-   [ImageJ Forum Thread 1290](http://forum.imagej.net/t/guide-to-make-a-plugin-as-official-fiji-plugin/1290)
-   Git tutorial: [Git in 15 min](https://try.github.io/levels/1/challenges/1)

and all other links cited in the text!

# Appendix

## How do I find dependencies?

You can search [maven.scijava.org](https://maven.scijava.org/) by class for Maven artifacts. For example, [search for `ij.plugin.PlugIn`](https://maven.scijava.org/#nexus-search;classname~ij.plugin.PlugIn).

If you are comfortable with command-line tools, you can also use the [Maven Dependency Plugin](https://maven.apache.org/plugins/maven-dependency-plugin/) which enables you to do things like download local copies of the dependency jars for inspection.

Also [mvnrepository.com](https://mvnrepository.com) is a good resource to find repositories with code you can easily copy and paste in your `pom.xml`.

## Manage Java versions

{% include notice icon="info" content="This section is unmodified and untested from the original beginner's guide"  %}
On Linux several java version can be installed. Select the preferred version in a terminal window (e.g. bash):

```sh
update-alternatives --config java
```

Note: It might be necessary to use `sudo`.

If necessary, tell NetBeans to use JDK 1.8 as the default JRE for new projects (i. e. on Debian Linux: {% include bc path='Project Properties|Build|Compile...'%} `/usr/lib/jvm/java-1.8.0-openjdk-amd64`) or alternatively set the `netbeans_jdkhome` property in your NetBeans config file. It should be in the local NetBeans directory, for example `./netbeans-8.0/netbeans.conf`.


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
|   !-- test
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

Put your `.java` files under `src/main/java/` and the other files you need to be included into `src/main/resources/`. Any ancillary classes or scripts used for testing your project would be placed in the `src/test` folder. 

Should you want to apply the best practices called "regression tests" or even "test-driven development" put your tests' `.java` files to `src/test/java/` and the non-`.java` files you might require go into `src/test/resources/`.

More information about Maven's standard directory layout can be found on the [Maven website](https://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html).

## Are the underscores still needed for plugins to be visible in Fiji?

If you write a Fiji command plugin (i.e.: implement the `org.scijava.command.Command` interface with an `@Plugin` annotation) then the underscore is no longer necessary.

## How to migrate an existing project to a Maven project?

{% include notice icon="info" content="This section is unmodified and untested from the original beginner's guide"  %}

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
