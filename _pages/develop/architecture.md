---
title: Architecture
section: Extend:Development
project: /software/imagej2
---

{% include notice icon="info" content='This page describes the *technical* structure of [SciJava](/libs/scijava) projects.

-   For information on the *social* structure, see [Governance](/contribute/governance).
-   For information on the *legal* structure, see [Licensing](/licensing).' %}


This page describes the technical structure of [SciJava](/libs/scijava) projects, including [ImageJ2](/software/imagej2), [ImgLib2](/libs/imglib2), [SCIFIO](/libs/scifio), and other projects built on their foundations. For maximum benefit, we suggest readers familiarize themselves with [Maven](/develop/maven), [Git](/develop/git) and [GitHub](/develop/github) before reading the sections here.

# Definitions

Throughout this article, and elsewhere on this wiki, we use the following terms:

-   A software **component** is a program, such as a [plugin](/plugins), or a {% include wikipedia title='Library (computing)' text='library'%} of reusable functions. Components are typically designed to work together, and combined to form a {% include wikipedia title='Application software' text='software application'%} such as [ImageJ](/software/imagej). In [Maven](/develop/maven) terms, a component is a single *artifact*, typically a {% include wikipedia title="JAR (file format)" %}.
-   A software **project** is a more general term referring to either a single component or a *collection* of related components. For example, the phrase "ImageJ2 project" refers to several components including [ImageJ Common](/libs/imagej-common), [ImageJ Ops](/libs/imagej-ops), [ImageJ Legacy](/libs/imagej-legacy) and the [ImageJ Updater](/plugins/updater).
-   The **SciJava component collection** is the set of all components managed by the `pom-scijava` Bill of Materials. Such **SciJava components** reside across several different architectural layers. See "Bill of Materials" below for details.
-   **SciJava core components** are SciJava components of the SciJava component layer itself. See "Organizational structure" below.
-   The **ImageJ2 software stack** is the set of components upon which [ImageJ2](/software/imagej2) is built. It includes components from the [SciJava](/libs/scijava), [ImgLib2](/libs/imglib2), [ImageJ](/software/imagej)+[ImageJ2](/software/imagej2), and [SCIFIO](/libs/scifio) foundational layers; see "Organizational structure" and "Core libraries" below for details.

# SciJava project structure

The [ImageJ2](/software/imagej2) project, and related projects in the [SciJava](/libs/scijava) software ecosystem, are carefully structured to foster [extensibility](#extensibility).

## Organizational structure

There are four organizations on [GitHub](https://github.com/) which form the backbone of the [SciJava](/libs/scijava) ecosystem:

-   [scijava](https://github.com/scijava) - for [SciJava](/libs/scijava) core components: general-purpose, non-image-specific libraries.
-   [imglib](https://github.com/imglib) - for [ImgLib2](/libs/imglib2) components: flexible N-dimensional image processing.
-   [imagej](https://github.com/imagej) - for [ImageJ](/software/imagej)+[ImageJ2](/software/imagej2) components: metadata-rich image library and application.
-   [scifio](https://github.com/scifio) - for [SCIFIO](/libs/scifio) components: scientific image I/O and file formats.

Each organization contains several related components under its respective umbrella: a core library (see below) and several extensions. In social terms, each organization represents a collection of conceptually related components developed by a distinct [team of developers](/people).

Additional organizations can further extend this structure. For example, the [Fiji](/software/fiji) project has several organizations as follows:

-   [fiji](https://github.com/fiji) - for [Fiji](/software/fiji) components
-   [bigdataviewer](https://github.com/bigdataviewer) - for [BigDataViewer](/plugins/bdv) components
-   [trakem2](https://github.com/trakem2) - for [TrakEM2](/plugins/trakem2) components

Furthermore, many groups maintain their own GitHub organizations with components built on SciJava et al. Here are a few examples:

-   [LOCI](/orgs/loci) – [uw-loci](https://github.com/uw-loci)
-   [FLIMJ](/plugins/flimj) – [flimlib](https://github.com/flimlib)
-   [DAIS](/orgs/dais) – [TrnDy](https://github.com/TrnDy)
-   {% include person id='fjug' %} – [juglab](https://github.com/juglab)
-   {% include person id='axtimwalde' %} – [saalfeldlab](https://github.com/saalfeldlab)
-   {% include person id='StephanPreibisch' %} – [PreibischLab](https://github.com/PreibischLab)
-   &lt;your organization here!&gt;

## Git repositories

Each component is contained in its own [Git](/develop/git) repository, so that interested developers can cherry-pick only those parts of interest. Version control is an indispensable tool to ensure *scientific reproducibility* (see below) by tracking known-working states of the source code, and maintain a written record of how and why the code has changed over time. For technical details, see the [Git](/develop/git) section.

### Why separate Git repositories?

With [Maven](/develop/maven) it is possible to create a [multi-module reactor](http://maven.apache.org/guides/mini/guide-multiple-modules.html) that unifies several component artifacts into a single build, typically within a single Git repository.

While many SciJava components used to be structured this way, we found that lumping multiple components into a single Git repository with a multi-module build has disadvantages compared to separate Git repositories with single-module builds:

-   Typically, components of a multi-module project are all versioned together, but we have opted for individual [versioning](/develop/versioning) of components, for reasons of [rapid iteration](/develop/philosophy#release-early-release-often), [extensibility](#extensibility) and [modularity](#modularity).
-   Individual repositories make it easier for developers to cherry-pick only those components of interest, without building the rest of the code, since dependencies are fetched on demand from remote [Maven](/develop/maven) repositories.
-   Concerns are better separated, with each component encapsulating its own codebase, issues, pull requests and technical documentation.
-   Since every component follows a consistent structure, the supporting tools (e.g., [these scripts](https://github.com/scijava/scijava-scripts)) are simpler to develop and maintain.

Of course, there are downsides, too:

-   Changes affecting multiple components must be done as separate patch sets (i.e., commits or pull requests).
-   Issues relevant to multiple components must be filed separately in each issue tracker and cross-referenced.
-   It can be more difficult to locate code of interest, since the codebase is spread across so many repositories.

As a rule of thumb, we find that multi-module [Maven](/develop/maven) projects stored within a single Git repository are a natural fit for "big bang" software which is versioned in lockstep and carefully tested before each [release](/develop/releasing), whereas single-module projects stored in separate Git repositories work well for the [RERO](/develop/philosophy#release-early-release-often)-style [release](/develop/releasing) paradigm.

## Maven component structure

All components in these organizations use [Maven](/develop/maven) for [project management](/develop/project-management). Each organization has its own Maven [groupId](http://books.sonatype.com/mvnref-book/reference/pom-relationships-sect-project-relationships.html#pom-relationships-sect-more-coordinates). Each component extends the {% include github org='scijava' repo='pom-scijava' label='pom-scijava' %} [parent POM](http://books.sonatype.com/mvnref-book/reference/pom-relationships-sect-project-relationships.html#pom-relationships-sect-project-inheritance), which provides sensible build defaults and compatible dependency versions (see "Bill of Materials" below).

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td>
        <p><strong>Logo</strong></p>
      </td>
      <td>
        <p><strong>Project</strong></p>
      </td>
      <td>
        <p><strong>Organization</strong></p>
      </td>
      <td>
        <p><strong>groupId</strong></p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include icon name='SciJava' %}</p>
      </td>
      <td>
        <p><a href="/libs/scijava">SciJava</a></p>
      </td>
      <td>
        <p><a href="https://github.com/scijava">scijava</a></p>
      </td>
      <td>
        <p><a href="https://maven.scijava.org/index.html#nexus-search;gav~org.scijava">org.scijava</a></p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include icon name='ImageJ2' %}</p>
      </td>
      <td>
        <p><a href="/software/imagej2">ImageJ2</a></p>
      </td>
      <td>
        <p><a href="https://github.com/imagej">imagej</a></p>
      </td>
      <td>
        <p><a href="https://maven.scijava.org/index.html#nexus-search;gav~net.imagej">net.imagej</a></p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include icon name='ImgLib2' %}</p>
      </td>
      <td>
        <p><a href="/libs/imglib2">ImgLib2</a></p>
      </td>
      <td>
        <p><a href="https://github.com/imglib">imglib</a></p>
      </td>
      <td>
        <p><a href="https://maven.scijava.org/index.html#nexus-search;gav~net.imglib2">net.imglib2</a></p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include icon name='SCIFIO' %}</p>
      </td>
      <td>
        <p><a href="/libs/scifio">SCIFIO</a></p>
      </td>
      <td>
        <p><a href="https://github.com/scifio">scifio</a></p>
      </td>
      <td>
        <p><a href="https://maven.scijava.org/index.html#nexus-search;gav~io.scif">io.scif</a></p>
      </td>
    </tr>
    <tr>
      <td rowspan="3" style="vertical-align: middle">
        <p>{% include icon name='Fiji' %}</p>
      </td>
      <td>
        <p><a href="/software/fiji">Fiji</a></p>
      </td>
      <td>
        <p><a href="https://github.com/fiji">fiji</a></p>
      </td>
      <td>
        <p><a href="https://maven.scijava.org/index.html#nexus-search;gav~sc.fiji">sc.fiji</a></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><a href="/plugins/bdv">BigDataViewer</a></p>
      </td>
      <td>
        <p><a href="https://github.com/bigdataviewer">bigdataviewer</a></p>
      </td>
      <td>
        <p><a href="https://maven.scijava.org/index.html#nexus-search;gav~sc.fiji">sc.fiji</a></p>
      </td>
      <td></td>
    </tr>
    <tr>
      <td>
        <p><a href="/plugins/trakem2">TrakEM2</a></p>
      </td>
      <td>
        <p><a href="https://github.com/trakem2">trakem2</a></p>
      </td>
      <td>
        <p><a href="https://maven.scijava.org/index.html#nexus-search;gav~sc.fiji">sc.fiji</a></p>
      </td>
      <td></td>
    </tr>
  </tbody>
</table>
{:/}

## Bill of Materials

The `pom-scijava` parent includes a [Bill of Materials](http://howtodoinjava.com/maven/maven-bom-bill-of-materials-dependency/) (BOM) which declares compatible versions of all components of the **SciJava component collection** in its [dependencyManagement section](http://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html#dependency-management). These versions are intended to be used together in downstream projects, preventing version skew (symptoms of which include `ClassNotFoundException` and `NoSuchMethodError`, as well as erroneous behavior in general). This BOM is especially important while some components are still in beta, since they may sometimes break [backwards compatibility](/libs/imagej-legacy).

## Core libraries

{% include img src="/media/develop/graph.png" align="right" width="400px" %}

The ImageJ2 software stack is composed of the following core libraries:

-   [SciJava Common](/libs/scijava#scijava-common) - The [SciJava](/libs/scijava) application container and plugin framework.
-   [ImgLib2](/libs/imglib2) - The N-dimensional image data model.
-   [ImageJ Common](/libs/imagej-common) - Metadata-rich image data structures and SciJava extensions.
-   [ImageJ Ops](/libs/imagej-ops) - The framework for reusable image processing operations.
-   [SCIFIO](/libs/scifio) - The framework for N-dimensional image I/O.

These libraries form the basis of ImageJ-based software.

The dependency hierarchy of library artifacts is shown in the diagram to the right.

### Modularity

Much effort has been expended to ensure the design of these libraries provides a good {% include wikipedia title='Separation of concerns' text='separation of concerns'%}. Developers in need of specific functionality may choose to depend on only those components which are relevant, rather than needing to add a dependency to the entire ImageJ2 software stack.

Along those lines, the libraries take great pains to be **UI agnostic**, with no dependencies on packages such as `java.awt` or `javax.swing`. The idea is that it should be possible to build a {% include wikipedia title='Graphical user interface' text='user interface'%} (UI) on top of these libraries, without needing to change the library code itself. We have developed several proof-of-concept UIs for ImageJ using different UI frameworks, including [Swing](https://github.com/imagej/imagej-ui-swing), [AWT](https://github.com/imagej/imagej-ui-awt), [Eclipse SWT](https://github.com/imagej/imagej-ui-swt) and [Apache Pivot](https://github.com/imagej/imagej-ui-pivot).

### Extensibility

Extensibility is [ImageJ](/software/imagej)'s greatest strength. ImageJ provides many different types of plugins, and it is possible to extend the system with your own new types of plugins. See the [CreateANewPluginType tutorial](https://github.com/imagej/tutorials/tree/master/howtos/src/main/java/howto/plugins/create) for an illustration.

The [SciJava Common](/libs/scijava#scijava-common) (SJC) library provides a plugin framework with {% include wikipedia title='Strong and weak typing' text='strong typing'%}, and makes extensive use of plugins itself, to allow core functionality to be [customized easily](http://c2.com/cgi/wiki?SoftwareSeam). SJC has an powerful plugin discovery mechanism that finds all plugins available on the Java classpath, without knowing in advance what they are or where they are located. It works by indexing the plugins at compile time via an {% include wikipedia title='Java annotation\#Processing' text='annotation processor'%} (inspired by the [SezPoz](https://github.com/jglick/sezpoz) project) which writes the plugin metadata inside the JAR file (in `META-INF/json/org.scijava.plugin.Plugin`). Reading this index allows the system to discover plugin metadata at runtime very quickly *without* loading the plugin classes in advance.

# Reproducible builds

{% include aside title="Why are reproducible builds so essential for science?"
  content="Arguably **the most important thing** in science is to gain insights
about nature **that can be verified by other researchers**. It is this
mission for which [ImageJ2](/software/imagej2) and [Fiji](/software/fiji) stand,
and it is the central reason why they are [open source](/licensing/open-source).

To verify results, it is absolutely necessary to be able to reproduce results
claimed in scientific articles, and in the interest of efficiency, it should be
**easy** to reproduce the results, and it should **also** be easy to scrutinize
the used methods—incorrect results can be artifacts of flawed algorithms, after
all.

To that end, it should be obvious that researchers **need** to have the ability
to inspect the exact source code corresponding to the software used to generate
the results to be verified. In other words, reproducible builds are required
for sound scientific research." %}

A software *version* (or *build*) is called **reproducible** if it is easy to regenerate the exact same software application from the source code.

For example, you can refer to "ImageJ 1.49g" as a *reproducible build*, or to *Sholl Analysis 3.4.3*, while referring to "ImageJ" is irreproducible.

It gets more subtle when making heavy use of software libraries (sometimes called *dependencies*). It is known, for example, that many plugins in the now-defunct [MacBiophotonics distribution of ImageJ](/software/mbf-imagej) worked fine with ImageJ 1.42l, but stopped working somewhere between that version and ImageJ 1.44e. That is: referring to, say, *the Colocalisation Analysis plugin* does **not** refer to a reproducible build because it is very hard to regenerate a working Colocalisation Analysis and ImageJ version that could be used to verify previously published results.

## Advantages of reproducible builds

Some cardinal reasons to strive for reproducible builds are:

-   Reproducible builds are essential for the scientific method (see sidebar right).
-   It becomes possible to use a [feature branch workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow) development style where the main branch is always release ready—or even a {% include wikipedia title='Continuous delivery' text='continuous delivery'%} approach.
-   [Debugging with git-bisect](/develop/git/pinpoint-regressions) becomes feasible.
-   As a consequence, it avoids {% include wikipedia title='Technical debt' text='technical debt'%} in favor of a robust development style.
-   It attracts more developers to the project, since things "just work" out of the box.

## How SciJava achieves reproducible builds

For the reasons stated above, the SciJava software components strive for reproducible builds. The goal is to ensure that code which builds and runs today will continue to do so in exactly the same way for many years to come.

Each component depends on release [versions](http://books.sonatype.com/mvnref-book/reference/pom-relationships-sect-pom-syntax.html#pom-reationships-sect-versions) of *all* its dependencies—never on [snapshots](http://books.sonatype.com/mvnref-book/reference/pom-relationships-sect-pom-syntax.html#pom-relationships-sect-snapshot-versions) or [version ranges](http://books.sonatype.com/mvnref-book/reference/pom-relationships-sect-project-dependencies.html#pom-relationships-sect-version-ranges). A Maven snapshot is a moving target, and depending on one results in an irreproducible build. Similarly, all Maven plugins used, as well as the parent POM, are also declared at release versions. In short: all `<version>` tags specify release versions, never `SNAPSHOT` or `LATEST` versions. We use the [Maven Enforcer Plugin](http://maven.apache.org/enforcer/maven-enforcer-plugin/) to enforce this requirement (though it can be temporarily disabled by setting the `enforcer.skip` property).

We sometimes use `SNAPSHOT` versions temporarily on topic branches. However, we always [rewrite them](/develop/git#rewriting-history) before merging to main, to purge all `SNAPSHOT` references, so that all commits in the history build reproducibly. We use SciJava's [check-branch.sh](https://github.com/scijava/scijava-scripts/blob/1386a7b0bc9e832d45f925202e1382717cf4a706/check-branch.sh) script to ensure all commits on a topic branch build cleanly with passing tests.

## Using snapshot couplings during development

For developing several components in parallel, it can be useful to switch to `SNAPSHOT` dependency couplings.

You can override the version property of the dependency for which you wish to use a snapshot:

```xml
<properties>
  <scijava-common.version>LATEST</scijava-common.version>
  <enforcer.skip>true</enforcer.skip> <!-- ONLY while depending on a SNAPSHOT -->
</properties>
```

In the case of Eclipse, you may need to "Update Maven project" in order to see the snapshot couplings go into effect; the shortcut {% include key keys='Alt|F5' %} while selecting the affected project(s) accomplishes this quickly.

{% include notice icon="warning" content='Current versions of the Eclipse Maven integration (tested with Eclipse Mars) fail to correctly resolve the `LATEST` version tag to `SNAPSHOT`s. If this happens to you, try specifying the version explicitly e.g. `2.0.0-SNAPSHOT` instead of using `LATEST`.' %}

***Be sure to work on a topic branch while developing code in this fashion.*** You will need to clean up your Git history afterwards before merging things to the main branch, in order to achieve [reproducible builds](#reproducible-builds).

# Versioning

SciJava components use the [Semantic Versioning](/develop/versioning) system. This scheme communicates information about the [backwards compatibility](/libs/imagej-legacy) (or lack thereof) between versions of each individual software component. In a nutshell:

> Given a version number MAJOR.MINOR.PATCH, increment the:
>
> -   MAJOR version when you make incompatible API changes,
> -   MINOR version when you add functionality in a backwards-compatible manner, and
> -   PATCH version when you make backwards-compatible bug fixes.

See the [Versioning](/develop/versioning) page for a detailed discussion of SciJava versioning.
