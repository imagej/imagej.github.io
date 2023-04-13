---
title: Contributing to Fiji
section: Contribute
project: /software/fiji
nav-links: true
nav-title: Fiji
---

{% include notice icon="info" content='There is another good way to distribute your extension: your own [update site](/update-sites). See the [Distribution](/contribute/distributing) page for details.' %} 

Distributing your software component as part of [Fiji](/software/fiji) is an effective way to immediately and easily put it into the hands of many users, as well as to actively participate in the community of ImageJ software development. However, doing so comes with a few corresponding rules.

The following document describes these requirements, as well as associated best practices, for shipping your component as part of the [Fiji](/software/fiji) update site.

# Definition

A "core" [Fiji](/software/fiji) project is one distributed on the [Fiji update site](http://update.fiji.sc). Such projects are subject to the requirements discussed below. Conversely, if you distribute your extension on a separate update site, this page does not apply.

# Requirements

## Freely accessible source code

A key principle of the Fiji project is:

> If you want to go fast, go alone. If you want to go far, go together.
>
> \- African proverb

There are many corollaries to this wisdom, the most prominent: if you write software in your endeavor to discover new insights, [Open Source](/licensing/open-source) is the way that brings you farthest. Withholding the source code—like any other method to obstruct other researchers' work, e.g. refusing to share materials and methods—will [invariably have the opposite effect](/licensing/closed-source) in the long run. Likewise, working with interested parties to improve one's project will invariably lead to a much better and stronger result.

As such, components distributed with Fiji must be licensed in a way [compatible with the GNU General Public License](https://www.gnu.org/licenses/license-list.html).

## Source hosted on GitHub

Core Fiji development takes place on [GitHub](/develop/github). This ensures continuity and visibility, and facilitates collaboration.

There are two possibilities for where to host your project:

1.  **Standard.** Repository is hosted in the [fiji organization](https://github.com/fiji), or a descendant organization (e.g., [trakem2](https://github.com/trakem2)). [Fiji maintainers](/contribute/governance) help maintain the project.
2.  **External.** Repository is hosted in a GitHub organization you control. You alone maintain the project (though Fiji maintainers may submit PRs to help).

### Standard projects

The following criteria apply to projects hosted in the [fiji organization](https://github.com/fiji):

-   Each component (i.e., JAR file) lives in its own repository.
-   Components use [Maven](/develop/maven) to build:
    -   As single-module projects
    -   With the standard Maven directory layout
    -   Extending the [pom-scijava parent POM](/develop/architecture#maven-component-structure)
-   Components use the groupId `sc.fiji`.
-   Components are [versioned according to SemVer](/develop/versioning).
-   The project uses [GitHub Issues](/develop/project-management#issue-tracking) for issue tracking.
-   The project has a dedicated page here on the ImageJ wiki.
-   The [Fiji maintainers](/contribute/governance) may make commits and [release new versions](/develop/releasing) of the component as needed, so that Fiji as a whole continues to work as intended.
-   The `master` branch is considered *release ready* at all times, meaning it compiles with passing tests, and is ready for downstream consumption.

### External projects

Projects that reside outside the [fiji organization](https://github.com/fiji) are not subject to the requirements above. But it is then the project maintainer's responsibility to ensure the project continues to function properly in up-to-date installations of Fiji. This might entail code changes as ImageJ and Fiji evolve.

## Continuous integration: GitHub Actions

To verify that the Fiji components build without problems, and that all regression tests pass, every Fiji project's source code repository is connected to a [GitHub Actions](/develop/github-actions) job that builds and tests the source code, and deploys the [Maven artifacts](#maven-artifacts), whenever a new revision is made available.

Have a look at the [GitHub Actions](/develop/github-actions) page for instructions on setting it up.

## Versioning and dependency convergence

Most Fiji projects use the [SemVer versioning scheme](/develop/versioning): a standard to encourage API consistency without obstructing API improvements.

The minimum requirement for core Fiji projects is to abide by the **MAJOR** digit portion of [SemVer](http://semver.org/)—i.e., if the first digit of the version string increases, it means that the new version is *not* backwards compatible with the old version. Conversely, if any later digit of the version string increases, it means that the new version *is* backwards compatible.

This requirement exists to facilitate automated tooling for dependency convergence: the use of compatible dependency versions across all of Fiji. When two (or more) components of Fiji depend on different versions of the same component, it must be possible to verify which version is newer, and whether the newer version is backwards compatible with the old one. As long as the newest required dependencies are indeed backwards compatible, those dependencies are said to *converge*.

From example, Apache Commons Math v3.x breaks backwards compatibility with Apache Commons Math v2.x. Since both versions share the same package and class names, only one of these versions can be shipped with Fiji. Therefore, all components of Fiji must rely on the same major version: either v2 or v3.

In general, if the rest of the Fiji distribution upgrades to a new major version of a library on which your component depends, your component must also be upgraded to use the new version. Such decisions are typically reached after [discussion on public channels](/discuss/#ways-to-get-help).

### Best practice: version constants

Many plugins in Fiji contain explicit version constants. Without [Maven](/develop/maven), in-code constants may make sense as a way to track compatibility. But by Mavenizing for contribution to Fiji, the pom.xml provides a standard mechanism for versioning, allowing migration away from constants in the source code.

Versioning through the pom.xml has several advantages to facilitate [reproducible builds](/develop/architecture#reproducible-builds), including:

-   Standardized scripts to increment versions appropriately.
-   No risk of accidentally double-releasing a given version.
-   Users and developers see the same version information.

Furthermore, for backwards-compatibility a version can be automatically deduced:

-   From the POM. This is the most reliable option. For convenience, [scijava-common](https://github.com/scijava/scijava-common) provides a utility class to assist in version retrieval: [VersionUtils](https://github.com/scijava/scijava-common/blob/scijava-common-2.39.0/src/main/java/org/scijava/util/VersionUtils.java#L51).
-   Alternatively, the [specification](http://docs.oracle.com/javase/7/docs/api/java/lang/Package.html#getSpecificationVersion%28%29) or [implementation](http://docs.oracle.com/javase/7/docs/api/java/lang/Package.html#getImplementationVersion%28%29) version can be used - for example, as in the [LSMReader](https://github.com/fiji/LSM_Reader/commit/a6b26290ad71667efd75d77f3eef95d445d6eaff). Core Fiji libraries follow a convention of setting these versions to match the pom version, and they are set at the manifest level to ensure they are they same for all packages in a given component. **However**, the two versions are allowed to differ - each package is allowed its own specification and implementation version! Furthermore, classes in a default package will not be able to retrieve either version. So these functions can not be relied on as a general solution.

## Maven artifacts

[Fiji](/software/fiji) and related [SciJava](/libs/scijava) software uses [Maven](/develop/maven), an industry standard to declare metadata about a project, to build projects using said metadata, and to *deploy* the resulting artifacts to a [Maven repository](/develop/project-management#maven). Such repositories are essentially for developers what [update sites](/update-sites) are for users.

-   The minimum requirement for core Fiji projects is to use a build system (e.g., [Maven](/develop/maven) or Gradle) that automatically deploys required artifacts to the [SciJava Maven repository](/develop/project-management#maven), such that they can be consumed by downstream code, including other Fiji projects. Required artifacts to deploy include the main JAR and POM files, `-tests` JAR, `-sources` JAR and `-javadoc` JAR.
-   To facilitate this, most Fiji projects inherit a common Maven configuration from the [pom-fiji](https://github.com/fiji/pom-fiji) parent project. This configuration ensures that not only the compiled *.jar* files are deployed, but also the Javadocs and the sources. Therefore, it is strongly encouraged to extend this parent; see the [Maven component structure](/develop/architecture#maven-component-structure) section for details.
-   All of Fiji's components are deployed by [CI/CD](/develop/ci) to the [SciJava Maven repository](/develop/project-management#maven) or to [OSS Sonatype](http://oss.sonatype.org/). That way, all Fiji components can be added easily as dependencies to downstream projects.
-   All Fiji components are declared in the toplevel [fiji](https://github.com/fiji/fiji) project's POM as dependencies, and declared in the [pom-fiji](https://github.com/fiji/pom-fiji) parent as *managed dependencies*, as part of Fiji's [Bill of Materials](/develop/architecture#bill-of-materials).

# Guidelines

The following guidelines are less technical and more philosophical, but represent best practice for core Fiji components.

## Open development process

Developers of Fiji components should invite others to contribute. That entails welcoming developers, acknowledging and working on pull requests, encouraging improvements, working together, enhancing upon each others' work, share insights, etc.

To leverage the power of [open source](/licensing/open-source), the default for discussions should be to use [public channels](/discuss/#ways-to-get-help). In other words, the question to ask should be "Is there any good reason why this conversation should be private?" instead of the opposite.

## Active bug management

Bug reports need to be acknowledged, participation in resolving bugs should be encouraged whenever possible, bugs should not go uncommented for months (we all have times when we are busy e.g. writing a paper; a little message helps the involved people understand), explanations are due when bugs go unresolved for years, etc

## Reusability and reliability

Whenever possible, source code should be reused. If necessary, improve the existing source code. Only rewrite from scratch when absolutely necessary.

Make code reusable, i.e. define APIs to use the functionality. This requires a little bit of discipline so that third parties can rely on the interfaces.

## Regression tests

Writing regression tests is [easy](https://github.com/junit-team/junit/wiki/Getting-started): create a class in the *src/test/java/* directory structure and annotate methods with *@Test*, testing for various [assertions](https://github.com/junit-team/junit/wiki/Assertions) (the most common ones are *assertEquals()*, *assertTrue()* and *assertNotNull()*).

In particular when fixing a bug, it is a good idea to write a regression test *first*, making sure that it actually fails. After that, one should develop the fix, getting a cozy and warm feeling once the regression test passes.

## Separation of concerns

New features should be put into the appropriate component. E.g., when adding a general purpose utility, consider contributing to [SciJava Common](/libs/scijava#scijava-common) or [ImageJ Common](/libs/imagej-common) instead of bundling it with your specific extension.

# Examples

The following table provides a few examples of how various Fiji components are structured.

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td style="text-align: center">
        <p><strong>Basics</strong></p>
      </td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>
        <p><strong><a href="/develop/github">GitHub</a></strong></p>
      </td>
      <td></td>
      <td>
        <p><strong><a href="/develop/maven">Maven</a></strong></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><strong>Classification</strong></p>
      </td>
      <td>
        <p><strong>Component</strong></p>
      </td>
      <td>
        <p><strong>Core?<sup>1</sup></strong></p>
      </td>
      <td>
        <p><strong>Update site</strong></p>
      </td>
      <td>
        <p><strong>License<sup>2</sup></strong></p>
      </td>
      <td>
        <p><strong>Organization</strong></p>
      </td>
      <td>
        <p><strong>Repository</strong></p>
      </td>
      <td>
        <p><strong>groupId</strong></p>
      </td>
    </tr>
    <tr>
      <td rowspan=4>
        <p><strong>Standard</strong></p>
      </td>
      <td>
        <p><a href="/plugins/3d-viewer">3D Viewer</a></p>
      </td>
      <td>
        <p>&#9989;</p>
      </td>
      <td style="text-align: center">
        <p><a href="http://update.fiji.sc/">Fiji</a></p>
      </td>
      <td>
        <p><a href="/licensing/gpl">GPLv3</a></p>
      </td>
      <td>
        <p><a href="https://github.com/fiji">fiji</a></p>
      </td>
      <td>
        <p>{% include github org='fiji' repo='3D_Viewer' label='3D_Viewer' %}</p>
      </td>
      <td>
        <p><code>sc.fiji</code></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><a href="/plugins/coloc-2">Coloc 2</a></p>
      </td>
      <td>
        <p>&#9989;</p>
      </td>
      <td style="text-align: center">
        <p><a href="http://update.fiji.sc/">Fiji</a></p>
      </td>
      <td>
        <p><a href="/licensing/gpl">GPLv3</a></p>
      </td>
      <td>
        <p><a href="https://github.com/fiji">fiji</a></p>
      </td>
      <td>
        <p>{% include github org='fiji' repo='Colocalisation_Analysis' label='Colocalisation_Analysis' %}</p>
      </td>
      <td>
        <p><code>sc.fiji</code></p>
      </td>
      <td></td>
    </tr>
    <tr>
      <td>
        <p><a href="/plugins/snt">Simple Neurite Tracer</a></p>
      </td>
      <td>
        <p>&#9989;</p>
      </td>
      <td style="text-align: center">
        <p><a href="http://update.fiji.sc/">Fiji</a></p>
      </td>
      <td>
        <p><a href="/licensing/gpl">GPLv3</a></p>
      </td>
      <td>
        <p><a href="https://github.com/fiji">fiji</a></p>
      </td>
      <td>
        <p>{% include github org='fiji' repo='Simple_Neurite_Tracer' label='Simple_Neurite_Tracer' %}</p>
      </td>
      <td>
        <p><code>sc.fiji</code></p>
      </td>
      <td></td>
    </tr>
    <tr>
      <td>
        <p><a href="/plugins/trackmate">TrackMate</a></p>
      </td>
      <td>
        <p>&#9989;</p>
      </td>
      <td style="text-align: center">
        <p><a href="http://update.fiji.sc/">Fiji</a></p>
      </td>
      <td>
        <p>?</p>
      </td>
      <td>
        <p><a href="https://github.com/fiji">fiji</a></p>
      </td>
      <td>
        <p>{% include github org='fiji' repo='TrackMate' label='TrackMate' %}</p>
      </td>
      <td>
        <p><code>sc.fiji</code></p>
      </td>
      <td></td>
    </tr>
    <tr>
      <td rowspan=2>
        <p><strong>External</strong></p>
      </td>
      <td>
        <p><a href="/plugins/sholl-analysis">Sholl Analysis</a></p>
      </td>
      <td>
        <p>&#9989;</p>
      </td>
      <td style="text-align: center">
        <p><a href="http://update.fiji.sc/">Fiji</a></p>
      </td>
      <td>
        <p><a href="/licensing/gpl">GPLv3</a></p>
      </td>
      <td>
        <p><a href="https://github.com/tferr">tferr</a></p>
      </td>
      <td>
        <p>{% include github org='tferr' repo='ASA' label='ASA' %}</p>
      </td>
      <td>
        <p><code>ca.mcgill</code></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><a href="/formats/bio-formats">Bio-Formats</a></p>
      </td>
      <td>
        <p>&#9989;</p>
      </td>
      <td style="text-align: center">
        <p><a href="http://update.fiji.sc/">Fiji</a></p>
      </td>
      <td>
        <p><a href="/licensing/gpl">GPLv2</a></p>
      </td>
      <td>
        <p><a href="https://github.com/openmicroscopy">openmicroscopy</a></p>
      </td>
      <td>
        <p>{% include github org='openmicroscopy' repo='bioformats' label='bioformats' %}</p>
      </td>
      <td>
        <p><code>ome</code></p>
      </td>
      <td></td>
    </tr>
    <tr>
      <td rowspan=2>
        <p><strong>Subproject</strong></p>
      </td>
      <td>
        <p><a href="/plugins/bdv">BigDataViewer</a></p>
      </td>
      <td>
        <p>&#9989;</p>
      </td>
      <td style="text-align: center">
        <p><a href="http://update.fiji.sc/">Fiji</a></p>
      </td>
      <td>
        <p><a href="/licensing/gpl">GPLv3</a></p>
      </td>
      <td>
        <p><a href="https://github.com/bigdataviewer">bigdataviewer</a></p>
      </td>
      <td>
        <p>{% include github org='bigdataviewer' repo='bigdataviewer_fiji' label='bigdataviewer_fiji' %}</p>
      </td>
      <td>
        <p><code>sc.fiji</code></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><a href="/plugins/trakem2">TrakEM2</a></p>
      </td>
      <td>
        <p>&#9989;</p>
      </td>
      <td style="text-align: center">
        <p><a href="http://update.fiji.sc/">Fiji</a></p>
      </td>
      <td>
        <p><a href="/licensing/gpl">GPLv3</a></p>
      </td>
      <td>
        <p><a href="https://github.com/trakem2">trakem2</a></p>
      </td>
      <td>
        <p>{% include github org='trakem2' repo='TrakEM2' label='TrakEM2' %}</p>
      </td>
      <td>
        <p><code>sc.fiji</code></p>
      </td>
      <td></td>
    </tr>
    <tr>
      <td rowspan=3>
        <p><strong>Third party</strong></p>
      </td>
      <td>
        <p><a href="/imaging">Cookbook</a></p>
      </td>
      <td>
        <p>&#10060;</p>
      </td>
      <td style="text-align: center">
        <p><a href="http://sites.imagej.net/Cookbook/">Cookbook</a></p>
      </td>
      <td>
        <p><a href="/imaging#credits">Various</a></p>
      </td>
      <td>
        <p><a href="https://github.com/fiji">fiji</a></p>
      </td>
      <td>
        <p>{% include github org='fiji' repo='cookbook' label='cookbook' %}</p>
      </td>
      <td>
        <p><code>sc.fiji</code></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><a href="/plugins/mamut">MaMuT</a></p>
      </td>
      <td>
        <p>&#10060;</p>
      </td>
      <td style="text-align: center">
        <p><a href="http://sites.imagej.net/MaMuT/">MaMuT</a></p>
      </td>
      <td>
        <p><a href="/licensing/gpl">GPLv3</a></p>
      </td>
      <td>
        <p><a href="https://github.com/fiji">fiji</a></p>
      </td>
      <td>
        <p>{% include github org='fiji' repo='MaMuT' label='MaMuT' %}</p>
      </td>
      <td>
        <p><code>sc.fiji</code></p>
      </td>
      <td></td>
    </tr>
    <tr>
      <td>
        <p><a href="/plugins/slim-curve">SLIM Curve</a></p>
      </td>
      <td>
        <p>&#10060;</p>
      </td>
      <td>
        <p><a href="http://sites.imagej.net/SLIM-Curve/">SLIM-Curve</a></p>
      </td>
      <td>
        <p><a href="/licensing/gpl">GPLv3</a></p>
      </td>
      <td>
        <p><a href="https://github.com/slim-curve">slim-curve</a></p>
      </td>
      <td>
        <p>{% include github org='slim-curve' repo='slim-plugin' label='slim-plugin' %}</p>
      </td>
      <td>
        <p><code>slim-curve</code></p>
      </td>
      <td></td>
    </tr>
  </tbody>
</table>
{:/}

<sup>1</sup> A "core" project is one distributed on the Fiji update site. These projects are subject to the requirements discussed on this page.  
<sup>2</sup> See the [Licensing](/licensing) page for further details.


