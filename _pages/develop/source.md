---
title: Source code
section: Extend:Development
---

# ImageJ

The source code of the original [ImageJ](/software/imagej) is available at:

{% include link-banner url='https://github.com/imagej/imagej1' %}

And there is a version with clean [Git](/develop/git) history and release tags, with a [Maven](/develop/maven)-based build system, available at:

{% include link-banner url='https://github.com/imagej/ImageJA' %}

## ImageJ unit tests

There are a substantial number of [unit tests to exercise ImageJ functionality](/develop/ij1-unit-tests).

# ImageJ2

The source code of [ImageJ2](/software/imagej2) is very modular; i.e., it is organized into [well-separated](/develop/architecture#modularity) projects. This separation offers many advantages for efficient software development and it is well worth investing a little bit of time to understand.

## Where is the code?

{% include notice icon="tip" content='You can search the source code at [search.imagej.net](https://search.imagej.net/) using the GitHub button!' %}

All source code is on [GitHub](/develop/github).

-   Each project exists in its own GitHub organization.
-   Each organization contains multiple source code repositories.
-   Each repository corresponds to one Java library (.jar file).

| Logo                                       | Organization                          | Purpose                                                         |
|--------------------------------------------|---------------------------------------|-----------------------------------------------------------------|
| ![](/media/icons/scijava.png){:width="28"} | [SciJava](https://github.com/scijava) | Common utilities, plugin infrastructure, scripting, the context |
| ![](/media/icons/imagej2.png){:width="28"} | [ImageJ2](https://github.com/imagej)  | A general-purpose image processing application                  |
| ![](/media/icons/imglib2.png){:width="28"} | [ImgLib2](https://github.com/imglib)  | Generic multi-dimensional data processing                       |
| ![](/media/icons/scifio.png){:width="28"}  | [SCIFIO](https://github.com/scifio)   | Extensible image file I/O                                       |
| ![](/media/icons/fiji.png){:width="28"}    | [Fiji](https://github.com/fiji)       | A "batteries-included" distribution of ImageJ                   |

See the [Architecture](/develop/architecture) page for more information about the relationship between these projects.

## What is the license?

Most is [BSD-2](/licensing/bsd) (permissive); some is [GPL](/licensing/gpl) (copyleft). See the [Licensing](/licensing) page.

## Building from source

Virtually all of these repositories have a top-level `pom.xml` file, identifying them as [Maven](/develop/maven) projects.

To build a Maven project:

1.  [Install Maven](http://maven.apache.org/guides/getting-started/maven-in-five-minutes.html).
2.  Clone the source repository of interest.
3.  Type `mvn` from the top-level directory.

Advanced instructions for building, or modifying, the source code are available for specific development environments:

{% include develop/ide-links %}

Note that these tutorials are targeted towards [ImageJ2](/software/imagej2), but would apply to any Maven-based project.

# Javadocs

Javadoc for all SciJava-related projects can be found online:

{% include link-banner url='https://javadoc.scijava.org/' %}

You can also search the javadocs at
[https://search.imagej.net/](https://search.imagej.net/)
using the Javadoc button.
