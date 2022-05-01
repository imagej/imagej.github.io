---
title: Development Lifecycle
section: Extend:Development:Guides
project: /libs/scijava
---

{% include notice icon="info" content='This page describes the core [SciJava](/libs/scijava) *software release process*.

-   For an overview of *distribution methods*, see [Distribution](/contribute/distributing).
-   To *download* software releases, see [Downloads](/downloads).' %}

The SciJava [philosophy](/develop/philosophy) is to [release early, release often](/develop/philosophy#release-early-release-often). At the same time, we always want to preserve [scientific reproducibility](/develop/architecture#reproducible-builds). To make this possible we lean on several [project management](/develop/project-management) tools. The purpose of this guide is to take you through the process of using these tools with the goal of releasing new versions of your software, and then providing those releases to users.

# Phases of development

[ImageJ2](/software/imagej2) and [Fiji](/software/fiji) are developed according to the [SciJava philosophy](/develop/philosophy), thus these applications are used throughout this tutorial to illustrate the development lifecycle.

Whether adding new features, fixing bugs, improving performance, etc... **development** is the process of making changes, with the goal of exposing these changes to users. To accomplish this, actively developed projects cycle through five general "phases":

{% capture maven-artifacts %}
Artifacts are files, most commonly a
**{% include wikipedia title='JAR (file format)' text='JAR' %}**
encapsulating the compiled classes for a component.
Other files that may be produced as artifacts include:

- The project's **[POM](https://maven.apache.org/pom.html)**
- A jar with the original source files
- A jar with any generated javadoc
- A jar with any test files
{% endcapture %}
{% include aside title="What are Maven artifacts?" content=maven-artifacts %}

1.  **In development.** The source code is modified to add new features, fix bugs, etc... these modifications are expressed as *commits* by [Git](/develop/git), whether on your local filesystem, a topic branch, or a repository fork.
2.  **On master.** When you have a set of one or more *commits* that you are happy with (i.e. the feature is complete, or the bug is fixed) they are moved to the `master` branch of the project's repository on GitHub. This ensures the `master` branch is always *release ready*.
3.  **Released.** When there is a need to make the current `master` branch public (i.e. it has a critical bug fix or cool new feature that users have requested) [Maven](/develop/maven) is used to *cut a release*, which is then *deployed as an artifact* to the [SciJava Maven repository](https://maven.scijava.org/). Developers can now use the new version in their own projects.
4.  **Managed.** The new release artifact must be verified to work in the combined runtime environment with other SciJava components. Once it has been tested to work, the version listed in the SciJava component collection [Bill of Materials (BOM)](/develop/architecture#bill-of-materials) can be updated accordingly.
5.  **Uploaded.** Finally, the new release artifact can be uploaded to its associated ImageJ [update site](/update-sites), making it available to end users.

The following sections will discuss these phases, and their associated tools and workflows, in more depth.

# Relationship with Maven SNAPSHOTs

Another way of thinking about the development cycle is through the Maven version number given associated with the code. The idea behind reproducible builds is that from a given version of a plugin, the state of the code producing that version can be determined unambiguously. Typically, that state is determined by a unique [Git](/develop/git) commit. However, it would be impractical and unrealistic to change the Maven version with every single Git commit.

This is why [SNAPSHOT](https://docs.oracle.com/middleware/1212/core/MAVEN/maven_version.htm#MAVEN401) versions are used while "in development" (phases 1 and 2 - "SNAPSHOT coupling"). Using a SNAPSHOT version is saying "no guarantees are made as to the reproducibility of this artifact." For this reason, to best facilitate reproducible science, SNAPSHOT versions of code are not provided to users (except potentially for testing).

To provide users with an updated version of an artifact (phases 3, 4 and 5) the version is changed to a unique, non-SNAPSHOT, version for a single Git commit. Then the next commit returns to SNAPSHOT versioning for further development. Thus the cycle repeats.

# Phases in-depth

{% include aside title="When to use a topic branch?"
  content="[Core SciJava components](/develop/architecture) employ a \"release
ready main branch\" approach:

- The tip of the main branch is always stable enough to be released, \"as
  good or better\" than the state of its last release.
- Each commit on the main branch should compile with passing tests.
  This has several advantages—e.g., better
  [bisect-style debugging](https://git-scm.com/book/en/v2/Git-Tools-Debugging-with-Git#Binary-Search).

Topic branches are great for isolating potentially disruptive and/or unfinished
changes from the main branch, so that it always remains release ready.
However, pushing directly to main has a huge time savings over filing a PR
and awaiting review for days, weeks or months. Getting changes onto main
quickly has many advantages:

- **Fewer conflicts.** It avoids conflicts between multiple long-running topic
  branches.
- **SNAPSHOT builds.** [GitHub Actions](/develop/github-actions) builds the
  change into the latest SNAPSHOT build, making it available from the
  [SciJava Maven repository](/develop/project-management#maven).
- **Faster support.** Supporting the community is less convoluted, with changes
  released to users more rapidly. Yes, you can link to changes on a topic
  branch. And yes, you can upload binary builds from that branch. But each
  extra manual step costs time—better to link directly to the latest SNAPSHOT
  build. There are even ImageJ [update sites](/update-sites) which serve the
  latest builds from main, to make it easier for non-technical users to test
  changes.
- **Less complex.** The more topic branches you have—and in particular, the
  more integration branches you have—the more complex the system becomes, the
  more supporting tooling, CI jobs, etc. are needed. And the more developer
  time is needed to maintain the tooling, sort through topic branches, keep
  track of open PRs... leaving less time for developing new features and fixing
  bugs.

Hence, when exactly to use a topic branch is a judgment call, but some good
times to use a topic branch are:

- **Breaking.** The changes break
  [backwards compatibility](/libs/imagej-legacy).
- **New API.** The changes introduce significant new API which will need to
  remain backwards compatible in the future, and review is desired before
  committing to that API.
- **Unfinished.** The changes are unfinished.
- **Regressing.** The changes leave the codebase in a \"worse\" state somehow.
- **Discussion.** To solicit discussion from the [community](/discuss),
  especially if the changes might be contentious.

Conversely, some situations to push directly to main:

- **Correct.** Bug-fixes where the developer is confident the fix is correct.
- **No new API.** Small new additions which do not introduce significant future
  maintenance burden.
- **Unstable.** Changes to unstable or experimental components still in their
  \"incubation\" period of development (i.e., versioned at 0.x), since there is
  no promise of backwards compatibility.
- **Unsupported.** Changes to \"unsupported\" components which make no
  guarantee of backwards compatibility.

Lastly, keep in mind that SciJava favors the
[release early, release often](/develop/philosophy#release-early-release-often)
style of development, to maximize iterations of community feedback. Just
because a change makes it to the main branch, does not mean it is set in stone:
if a problem is later found, the change can be amended or reverted as quickly
as it was added—easy come, easy go." %}

## Phase 1: In development

Repositories on GitHub are referred to as **remotes**; when you *[clone](https://help.github.com/articles/cloning-a-repository/)*, or *check out*, a remote you get a local copy of the repository. Development progresses by making changes to your local copy and pushing them back to the remote. GitHub provides tools for controlling [user permission levels](https://help.github.com/articles/permission-levels-for-a-user-account-repository/) for each remote repository, therefore how you develop a project depends on whether you are able to *push* (write) to that project's remote repository or not.

-   **Collaborating developer.** If you have permission to push directly to the project's remote repository, then you can simply use [Git](/develop/git) and [GitHub](/develop/github) to [clone the repository](https://help.github.com/articles/cloning-a-repository/) and make your changes. For non-trivial changes, you will typically [create a topic branch](/develop/git/topic-branches) to develop and test the changes. This also provides a forum for discussion and review with your fellow developers.

<!-- -->

-   **External developer.** If you do not have push rights, then you need to go through an additional step called **[Forking the repository](http://www.dataschool.io/simple-guide-to-forks-in-github-and-git/)**. This will create a remote copy of the repository, to which you have push rights. Your remote fork is referred to as *downstream* of the original remote repository (which is *upstream* of your fork). Your development will then take place on your fork, with an additional step later to reconcile with the upstream repository.

## Phase 2: On master

Once a feature or fix is complete it can move to the `master` branch of the repository. How you accomplish this depends on how the changes were developed in Phase 1.

-   **Collaborating developer.** Minimal changes can be pushed back directly to `master` on the remote repository. If your work is on a [topic branch](/develop/git/topic-branches) then you should use a [pull request](https://help.github.com/articles/using-pull-requests/) (PR) so that the topic branch can be reviewed before being merged to `master`.

<!-- -->

-   **External developer.** First push your changes back to a branch of your forked repository (it doesn't necessarily have to be `master`). Then you can file a [pull request](https://help.github.com/articles/using-pull-requests/) (PR) on [GitHub](/develop/github) to merge your branch back to the official repository. This invites code review from other interested developers. Reviewers might ask for changes to the code to address any issues. After any needed revisions have been made, a [project maintainer](/contribute/governance) will accept your changes and then merge to the official `master` branch.

## Phase 3: Released

Once the `master` branch of a component has your desired new functionality, the next step is to cut a *release* version of the component. Normally, the Maven version (in the [pom.xml](https://maven.apache.org/pom.html#Introduction)) on master is a [*SNAPSHOT* version](http://stackoverflow.com/q/5901378), meaning it is [unstable](/develop/architecture#reproducible-builds) and not yet released. However, a [stable](/develop/architecture#reproducible-builds) *release* artifact can be deployed to the appropriate remote Maven repository.

The [release-version.sh](https://github.com/scijava/scijava-scripts/blob/master/release-version.sh) script automates the steps to performing a release. It relies on the [Maven Release plugin](http://maven.apache.org/maven-release/maven-release-plugin/) to do most of the heavy lifting, but also does some extra work (e.g., to ensure releases are deployed to the correct repository).

### Advantages

-   A tag is created on GitHub to easily reference the release commit.
-   The "bump to next release cycle" commit is done automatically.
-   The Maven POM references the correct tag rather than `HEAD`.
-   [GitHub Actions](/develop/github-actions) performs the actual release for you, using credentials which are encrypted in the repository itself.

### Prerequisites

-   Install the `release-version.sh` script. The best way to do this is to clone the [SciJava-scripts](https://github.com/scijava/scijava-scripts) repository. That will give you access to other useful scripts and help keep them all up to date.
-   (**optional**) If you want to easily use these scripts from any directory, you can [add the scijava-scripts folder to your PATH](http://askubuntu.com/q/97897).
-   Verify that your project's parent is pom-scijava version 17.1.1 or newer. If the parent version is too old, or is not pom-scijava, then upgrade it. Ask on the [forum](/discuss) if you need assistance.
-   If your component is to be released to the SciJava Maven repository, then add the following line to the properties section of your POM: <releaseProfiles>`deploy-to-imagej`</releaseProfiles>
-   Ensure the repository for your project is linked with a [GitHub Actions](/develop/github-actions) workflow that automatically builds and deploys Maven artifacts in response to changes on GitHub. If you're not sure if your project has this automation, ask for help on the [forum](/discuss).

### Steps to release

From your project's directory, simply run:

    release-version.sh

The script will verify that your master branch is ready to go, then create and push a [tag](http://git-scm.com/book/en/v2/Git-Basics-Tagging) for the release. [GitHub Actions](/develop/github-actions) will then notice the tag and complete the release for you. You should receive an email from GitHub after the release is complete indicating whether the build was successful.

{% include notice icon="info" content='If your project is a [multi-module build](https://maven.apache.org/guides/mini/guide-multiple-modules.html), first make a commit commenting out any modules that should not be released. Then run the script from the aggregator pom directory.' %}

## Phase 4: Managed

For core projects, there is an intermediate layer tying User-facing and Developer-facing components together: the [Bill of Materials](/develop/architecture#bill-of-materials) (BOM). To ensure users and developers see the same functionality, components should only be uploaded to the core update sites when their version is also updated in the {% include github org='scijava' repo='pom-scijava' label='pom-scijava' %} BOM.

To update the version of your component listed in the {% include github org='scijava' repo='pom-scijava' label='pom-scijava' %} BOM, you should follow the [External developer](#Phase_1:_In_development) instructions for contributing to {% include github org='scijava' repo='pom-scijava' label='pom-scijava' %}. By [submitting a pull request](https://help.github.com/articles/using-pull-requests/) that simply modifies the managed version of your component, you will signal to the core SciJava developers that your project is ready for upload. For example, {% include github org='scijava' repo='pom-scijava' pr='40' label='this PR' %} updates the managed version of [Bio-Formats](/formats/bio-formats) to 5.5.0.

## Phase 5: Uploaded

{% include aside title="What are ImageJ update sites?"
  content="ImageJ [update sites](/update-sites) are what ImageJ actually
queries to download updates. These update sites are versioned, but do not rely
on other tools (e.g., [Git](/develop/git) or [Maven](/develop/maven)) in order
to function. Rather, component developers upload new versions of their
component(s) using the [ImageJ Updater](/plugins/updater), which makes them
available to end users. Typically, update sites are available as websites via
HTTP, with uploads functioning via
[WebDAV](https://github.com/imagej/imagej-plugins-uploader-webdav) or
[SSH/SFTP/SCP](https://github.com/imagej/imagej-plugins-uploader-ssh)." %}

Deploying to the Maven repository creates a stable release artifact of a
software component usable by other developers. But for ImageJ-related
components, that alone does not put it into the hands of users. To do that, the
component must then be *uploaded* to an ImageJ [update site](/update-sites).

### ImageJ and Fiji update sites

-   The core ImageJ update site reflects the state of the newest {% include github org='imagej' repo='imagej' label='net.imagej:imagej' %} release.
-   The core Fiji update site reflects the state of the newest {% include github org='fiji' repo='fiji' label='sc.fiji:fiji' %} release.
-   Actually, for the moment, both of the above statements are untrue, but they represent the direction we are heading. Right now, core components of both ImageJ and Fiji are distributed manually via the Java-8 update site. See the [Java 8](/news/2016-05-10-imagej-howto-java-8-java-6-java-3d) page for details.

### External update sites

An update site can be hosted anywhere, although `sites.imagej.net` provides a [hosted update site](/update-sites/setup#creating-a-hosted-update-site) service.

See the **[distribution](/contribute/distributing)** page for a discussion of pros and cons of distributing your plugin on a core versus a separate update site.

If you do manage [your own update site](/update-sites/setup), you can upload your release yourself.

See the [documentation on update sites](/update-sites) for further instructions.

# Further reading

-   The SciJava [versioning guidelines](/develop/architecture#versioning) will help you choose appropriate version numbers for your software when performing Maven releases.

 
