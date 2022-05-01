---
title: Project management
section: Extend:Development
---


The [ImageJ2](/software/imagej2) and related [SciJava](/libs/scijava) projects take advantage of several project management tools.

## Git

SciJava projects use the [Git](/develop/git) revision control system to manage its [source code](/develop/source).

See the [Git](/develop/git) pages for more information, tutorials, etc.

## Maven

SciJava projects use [Maven](/develop/maven) for its project infrastructure. They use the [SciJava Maven repository](https://maven.scijava.org/) (which runs [Sonatype Nexus](http://www.sonatype.com/nexus)) for deploying components and accessing dependencies. Such a repository serves two main purposes:

### Deployment

The main purpose of the SciJava Maven repository is to serve the artifacts that are not yet ready to be deployed to OSS Sonatype. Typically, these components are [versioned at 0.x](/develop/versioning)—i.e., still in incubation. Once components reach 1.0.0, we try to [release them to the central Maven repository via OSS Sonatype](http://maven.apache.org/guides/mini/guide-central-repository-upload.html).

This purpose is also crucial for agile development across multiple components. For more details, see [Nine Reasons to Use a Repository Manager](http://blog.sonatype.com/2008/11/nine-reasons-to-use-a-repository-manager-sonatype-nexus/) and [Repository Management with Nexus](http://books.sonatype.com/nexus-book/reference/repoman.html).

### Proxying

The SciJava Maven repository's secondary purpose is to serve as a fast, local mirror of Maven Central as well as several useful third-party repositories.

It acts as a unified, on-demand mirror for these public Maven repositories, reducing load on the remote servers and potentially reducing local build times.

Developers can benefit from the mirror by adding the following section to their `$HOME/.m2/settings.xml` file:

    <settings>
            ...
            <mirrors>
                    <mirror>
                            <id>scijava-mirror</id>
                            <name>SciJava public mirror repository</name>
                            <url>https://maven.scijava.org/content/groups/public</url>
                            <mirrorOf>*</mirrorOf>
                    </mirror>
            </mirrors>
    </settings>

## Continuous integration

SciJava projects use [Github Actions](/develop/github-actions), a cloud-based workflow automation system that is part of Github and supports [continuous integration](/develop/ci) (CI). Github Actions automatically check the code for build and test errors.

## Issue tracking

SciJava software projects manage tasks and priorities using [GitHub Issues](https://guides.github.com/features/issues/):

You can search issues using the ImageJ search portal's GitHub button here:

{% include link-banner url='https://search.imagej.net/' %}

Previously, some projects used different issue trackers. These old issues are still available as read-only archives:

| [ImageJ2 Trac](/tickets)                                    |
| [LOCI/Bio-Formats Trac](https://uw-loci.github.io/tickets/) |
| [Fiji BugZilla](https://fiji.sc/bug/)                       |

### What are issues for?

Issues and milestones are public-facing entities, yet their content can be highly technical to serve as a roadmap and implementation guide for developers. As we see it, the various audiences for issues and milestones, and their needs, are as follows:

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <th>Who</th>
      <th>What</th>
      <th>How?</th>
    </tr>
    <tr>
      <th>Users<br>want...</th>
      <td>to know what's already been reported</td>
      <td>Browse and search <a href="https://github.com/issues?q=is%3Aopen+no%3Amilestone+user%3Abigdataviewer+user%3Afiji+user%3Aimagej+user%3Aimglib+user%3Ascifio+user%3Ascijava+user%3Atrakem2">all open issues</a>.</td>
    </tr>
    <tr>
      <td></td>
      <td>to keep track of issues of interest</td>
      <td>Subscribe to desired issues using <a href="https://guides.github.com/features/issues/#notifications">notifications</a>.</td>
    </tr>
    <tr>
      <td></td>
      <td>to know which issues were fixed in a release</td>
      <td>Browse issues at a particular <a href="https://guides.github.com/features/issues/#filtering">milestone</a><br>
        (e.g., <a href="https://github.com/issues?q=milestone%3A1.0.0+is%3Aclosed+user%3Abigdataviewer+user%3Afiji+user%3Aimagej+user%3Aimglib+user%3Ascifio+user%3Ascijava+user%3Atrakem2">1.0.0 issues</a>, <a href="https://github.com/issues?q=milestone%3A1.0.0+is%3Aclosed+label%3Abug+user%3Abigdataviewer+user%3Afiji+user%3Aimagej+user%3Aimglibaven-nar+user%3Ascifio+user%3Ascijava+user%3Atrakem2">1.0.0 bugs</a>, <a href="https://github.com/issues?q=milestone%3A1.0.0+is%3Aclosed+label%3Aenhancement+user%3Abigdataviewer+user%3Afiji+user%3Aimagej+user%3Aimglib+user%3Ascifio+user%3Ascijava+user%3Atrakem2">1.0.0 enhancements</a>).</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>to ask questions and report new issues</td>
      <td>Report new issues using the big green "New issue" button,<br>
        or via ImageJ's <a href="/discuss/bugs">Report a Bug</a> plugin.
      </td>
    </tr>
    <tr>
      <th>Developers<br>want...</th>
      <td>to track their current tasks</td>
      <td>Browse issues assigned to a particular developer<br>
        (e.g., <a href="https://github.com/issues?q=is%3Aopen+assignee%3Actrueden+user%3Abigdataviewer+user%3Afiji+user%3Aimagej+user%3Aimglib+user%3Ascifio+user%3Ascijava+user%3Atrakem2">ctrueden</a>, <a href="https://github.com/issues?q=is%3Aopen+assignee%3Ahinerm+user%3Abigdataviewer+user%3Afiji+user%3Aimagej+user%3Aimglib+user%3Ascifio+user%3Ascijava+user%3Atrakem2">hinerm</a>).</td>
    </tr>
    <tr>
      <td></td>
      <td>
        <p>to find new tasks to work on</p>
      </td>
      <td>
        <p>Browse the <a href="https://github.com/issues?q=is%3Aopen+label%3A%22help+wanted%22+user%3Abigdataviewer+user%3Afiji+user%3Aimagej+user%3Aimglib+user%3Ascifio+user%3Ascijava+user%3Atrakem2">"help wanted" label</a> or <a href="https://github.com/issues?q=is%3Aopen+no%3Aassignee+user%3Abigdataviewer+user%3Afiji+user%3Aimagej+user%3Aimglib+user%3Ascifio+user%3Ascijava+user%3Atrakem2">unassigned issues</a>.</p>
      </td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>
        <p>a place to discuss implementation details, etc.</p>
      </td>
      <td>
        <p>Use <a href="https://help.github.com/articles/using-pull-requests/">pull requests</a>.</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><strong>Maintainers<br>
        want...</strong></p>
      </td>
      <td>
        <p>to easily see what needs attention</p>
      </td>
      <td>
        <p>Browse <a href="https://github.com/issues?q=is%3Aopen+no%3Amilestone+user%3Abigdataviewer+user%3Afiji+user%3Aimagej+user%3Aimglib+user%3Ascifio+user%3Ascijava+user%3Atrakem2">issues without a milestone</a>.</p>
      </td>
    </tr>
    <tr>
      <td></td>
      <td>
        <p>to ignore inactive issues without closing them</p>
      </td>
      <td>
        <p>Use the <a href="https://github.com/issues?q=is%3Aopen+milestone%3Aunscheduled+user%3Abigdataviewer+user%3Afiji+user%3Aimagej+user%3Aimglib+user%3Ascifio+user%3Ascijava+user%3Atrakem2">"unscheduled" milestone</a>.</p>
      </td>
    </tr>
    <tr>
      <td></td>
      <td>
        <p>to plan development timelines</p>
      </td>
      <td>
        <p>Use future <a href="https://guides.github.com/features/issues/#filtering">milestones</a> (e.g., <a href="https://github.com/imagej/imagej/milestones">imagej</a>, <a href="https://github.com/scifio/scifio/milestones">scifio</a>).</p>
      </td>
    </tr>
    <tr>
      <td></td>
      <td>
        <p>to report completed features</p>
      </td>
      <td>
        <p>Use completed <a href="https://guides.github.com/features/issues/#filtering">milestones</a> (e.g., <a href="https://github.com/imagej/imagej/milestones?state=closed">imagej</a>, <a href="https://github.com/scifio/scifio/milestones?state=closed">scifio</a>).</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

To meet these needs, we use the following conventions with GitHub issues:

**Milestones**

-   For short-term active development, use names m1, m2, etc.
    -   These milestones themselves have no due date and never close, and contain only open issues
    -   When an issue is closed, it is moved to match its corresponding release milestone.
-   Future planned breaking changes should go in [SemVer](/develop/versioning)-named milestones.
-   All projects should have an "unscheduled" milestone.
    -   Issues in "unscheduled" are things that core developers and maintainers cannot make time to address.

**Issues**

-   Use the standard GitHub labels.
-   For repositories with multiple components (e.g., [imagej-ui-swing](https://github.com/imagej/imagej-ui-swing)) add "component:XXXX" labels, in orange, as needed.
-   Every issue must belong to a milestone.
    -   Use the "unscheduled" milestone for inactive issues.
-   If you are currently working on an issue, assign it to yourself.
-   All issues in near-term milestones should have an assignee.

Using these conventions gives rise to a workflow where new issues come in with no assignee and no milestone, and the project maintainers either assign them to a developer who will carry out the work, or put the issue in "unscheduled" with no assignee.

As issues are closed, they are sorted into milestones which match each project's release tags, making it easy to browse which issues were addressed as part of each release.

The high-level topics of interest (i.e., [bugs](https://github.com/issues?q=is%3Aopen+label%3Abug+user%3Abigdataviewer+user%3Afiji+user%3Aimagej+user%3Aimglib+user%3Ascifio+user%3Ascijava+user%3Atrakem2) and [enhancements](https://github.com/issues?q=is%3Aopen+label%3Aenhancement+user%3Abigdataviewer+user%3Afiji+user%3Aimagej+user%3Aimglib+user%3Ascifio+user%3Ascijava+user%3Atrakem2)) can easily be filtered by label, while milestones establish the timeline and functional development.

Note that the relationship between milestones and software releases can be one-to-many: e.g., bug-fix releases, or even the addition of new features, may not necessitate their own milestones. Good milestone structure should read similarly to a good [git](http://chris.beams.io/posts/git-commit/) [history](https://robots.thoughtbot.com/5-useful-tips-for-a-better-commit-message): informative without being overly verbose.

## Patch submissions

The preferred mechanism to contribute improvements to SciJava projects is using [GitHub pull requests](https://help.github.com/articles/using-pull-requests/)! See the [Contributing](/contribute) page for details.

## Roadmap links

-   [News](/news) about ImageJ2 and Fiji developments, including status updates, observations and comments about programming.
-   [Recent changes](https://github.com/imagej/imagej.github.io/commits/main) to this website (*not* the source code itself).

## Citable code

Many of these tools are employed to facilitate [reproducibility](/develop/architecture#reproducible-builds) from a technical perspective. From a social perspective, we are writing software for science - in which [scholarly citations](/contribute/citing) provide another currency for reproducibility.

To this end, developers can now use [digital archives like Zenodo](https://guides.github.com/activities/citable-code/) to provide consistent methods for citation.

## See also

-   The [Releases](/develop/releasing) page, for more about how these resources are used to release SciJava software artifacts.


