---
mediawiki: Developing_ImgLib2
title: Developing ImgLib2
section: Explore:Libraries:ImgLib2
---




## Introduction

The [ImgLib2](/libs/imglib2) library uses [Maven](/develop/maven) to manage project dependencies. One advantage of this approach is nice integration with various development environments ([IDEs](/develop/ides)).

Because people tend to have differing IDE configurations, we do not put project metadata files (e.g., `.classpath`, `.project` and `.settings` for Eclipse) into the git repository. Instead, the IDE can use Maven's `pom.xml` file directly to manage your dependencies in a better way.

## Getting the code

You can clone the ImgLib2 code using Git with the URL: **<git://github.com/imglib/imglib2>**

## Developing ImgLib2 with Eclipse

To develop ImgLib2 in Eclipse, follow these steps:

1.  [Install the Maven plugin](/develop/maven-and-eclipse)
2.  Choose {% include bc path='File | Import'%} from the Eclipse menu
3.  Select "Existing Maven Projects" and click Next
4.  For the Root Directory, specify the path where you cloned ImgLib2
5.  From the projects list, leave all items checked
6.  Click Finish

For fresh installs, it will initially take some time (a few minutes) for Maven to download all the dependencies for both its own plugins, and for ImgLib2. This is a one-time cost. After that, Maven will check for module updates once a day, which is generally fast.

Once you have the ImgLib2 projects within Eclipse, you can reap the benefits of the improved dependency management. For example, if you have the `imglib2` and `imglib2-algorithms` projects open, the `imglib2-algorithms` project will have an Eclipse project build dependency on `imglib2`. If you then close the `imglib2` project, the dependency within `imglib2-algorithms` with automatically become a library dependency to `imglib2-2.0-SNAPSHOT.jar`, rather than the project.

## Developing ImgLib2 with IDEA

IntelliJ IDEA comes with built-in support for Maven.

See [Developing ImageJ in IntelliJ IDEA](/develop/intellij).

## Developing ImgLib2 with NetBeans

NetBeans comes with built-in support for Maven.

See [Developing ImageJ in NetBeans](/develop/netbeans).

## Developing ImgLib2 with command line tools

You can use the mvn command line tool to build ImgLib2. Just type "mvn" with no arguments. By default, Maven will compile the code, run unit tests, create a JAR file and install it in your local Maven repository (typically found in `~/.m2/repository`). Maven does its work in a subfolder called `target` which is where you'll find compiled classes and JAR artifacts.

For more on using the Maven command line tool, see [Building a Project with Maven](http://maven.apache.org/run-maven/index.html) on the Maven web site.

  
