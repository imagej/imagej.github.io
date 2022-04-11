---
title: Continuous Integration
section: Extend:Development:Tools
---

{% include wikipedia title="Continuous integration" %} (CI) and *continuous delivery* (CD), collectively referred to as the *CI/CD pipeline*, together comprise a software engineering technique to perform automated tasks in response to code changes.

## Benefits

[SciJava](/libs/scijava) projects including [ImageJ2](/software/imagej2) and [Fiji](/software/fiji) use CI/CD in several ways, including:

- Building the code. A CI job deploys `SNAPSHOT` builds to the [SciJava Maven repository](https://maven.scijava.org/) in response to pushes to each code repository's mainline branch (e.g. `main` or `master`). So any downstream projects depending on a version of `LATEST` for a given component will match the last successful CI build—i.e., the latest code on the mainline branch.
- Run associated {% include wikipedia title='Unit testing' text='unit tests' %}. CI is instrumental in early detection of new bugs introduced to the codebase.
- Making [releases](/develop/releasing). A CI job deploys release builds to the appropriate Maven repository—typically either the SciJava Maven repository or [OSS Sonatype](https://s01.oss.sonatype.org/).
- Keeping  resources up-to-date.
- Keeping web resources such as the [javadoc](/develop/source#javadocs) up to date.

Deploying your library to a [Maven](/develop/maven) repository makes it available for other developers. It is also a [contribution requirement for the Fiji project](/contribute/fiji).

## Platforms

There are several popular options for performing CI builds in the cloud, or on your own self-hosted infrastructure:

* [GitHub Actions](/develop/github-actions) - Used by most SciJava projects for builds, testing, and deployment.
* [AppVeyor](/develop/appveyor) - Used by a few SciJava projects for builds on the Windows platform.
* [Travis CI](/develop/travis-ci) - Used by SciJava projects from 2017 until 2021.
* [Jenkins](/develop/jenkins) - Used by SciJava projects from 2010 until 2019.

Just to name a few that are or were used within the ImageJ community.
