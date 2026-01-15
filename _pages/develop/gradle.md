---
mediawiki: Gradle
title: Gradle
---

[Gradle](http://gradle.org/getting-started-gradle-java/) is an open-source build system using a Groovy-based script syntax as a succinct alternative to the XML of [Ant](http://ant.apache.org/) or [Maven](/develop/maven).

[QuPath](https://qupath.github.io/) for instance uses gradle, and if you want to develop an extension for QuPath, you will most probably need to use gradle instead of maven.


## Deploying on Scijava Maven using Gradle and GitHub actions

Any maven project depending on [`pom-scijava`](https://github.com/scijava/pom-scijava) can be deployed on scijava maven pretty easily using [`scijava-scripts`](https://github.com/scijava/scijava-scripts). See [Maven](/develop/maven) and [GitHub actions](/develop/github-actions) for more information.

If, for some reason, you have a gradle managed project instead of a maven project (for a QuPath extension for instance), it's nonetheless possible to upload it to scijava maven, with some limitations.

**Warning** most probably transitive dependencies will not be handled correctly if you mix maven and gradle projects.

### Requirements for maven deployment
Suppose that you have a gradle project with minimal dependencies and you want to upload the resulting built jar to scijava maven. First you need to host your project on github, and your github organisation needs to be allowed to deploy on scijava maven:

-   Host your [open-source](/licensing/open-source) project on [GitHub](/develop/github).
-   Contact a SciJava admin (@ctrueden, @hinerm, @tpietzsch) on the [Image.sc Zulip](https://imagesc.zulipchat.com/) or the [Image.sc Forum](http://forum.image.sc/) and request that they add the authentication secrets for deployment to your organization.


Then you need to amend your build script and add a github workflow, as specified below:

### Setting up scripts: `build.gradle` file and GitHub `publish.yml`

You will need to make a few modifications to your build.gradle file. 


**Warning: examples below are written in kotlin instead of groovy (help needed for translation...)**

#### build.gradle file

Make sure that the following parts are present in your `build.gradle` file:

* Specify a `group` and `version` to your artifact, for instance:
```java
# ! KOTLIN LANGUAGE !
group = "ch.epfl.biop"
version = "0.2.3-SNAPSHOT"
```

* (The artifact name is defined in the `settings.gradle` file), for instance:
```java
# ! KOTLIN LANGUAGE !
rootProject.name = "qupath-extension-warpy"
```
Leading, in this example to the GAV: `ch.epfl.biop:qupath-extension-warpy:0.2.3-SNAPSHOT`, which you want to deploy.

* Declare the `maven-publish` plugin:
```java
# ! KOTLIN LANGUAGE !
plugins {
    `java-library`
    `maven-publish`
}
```

* Add publishing settings:

```java

#! KOTLIN LANGUAGE !
publishing {
    publications.create<MavenPublication>("maven") {
        from(components.java)
    }
    repositories {
        maven {
            name = "scijava"
            url = if (version.toString().endsWith("SNAPSHOT"))
                 uri("https://maven.scijava.org/content/repositories/snapshots")
            else uri("https://maven.scijava.org/content/repositories/releases")
            credentials {
                username = System.getenv("MAVEN_USER")
                password = System.getenv("MAVEN_PASS")
            }
        }
    }
}

```

#### publish.yml Github workflow

Second you can add in your project within the folder `.github/workflows` the script `publish.yml`:


```groovy
# This workflow will publish jars to maven.scijava.org.
# Currently, it must be triggered manually and uses Java 11
# (because there is no requirement for jpackage).

name: Publish release to SciJava Maven

on: 
  workflow_dispatch:

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-java@v2
        with:
          java-version: '11'
          distribution: 'adopt-hotspot'
      - name: Grant execute permission for gradlew
        run: chmod +x gradlew
      - name: Publish package
        run: ./gradlew publish -P toolchain=11 -P release=true
        env:
          MAVEN_USER: $ { { secrets.MAVEN_USER } }
          MAVEN_PASS: $ { { secrets.MAVEN_PASS } }
```

To deploy, you can run the workflow 'manually' from github. Click actions, select the publish workflow, and hit run. If everything is successful, your new repository should appear on [scijava maven](https://maven.scijava.org/). If not, check the log of the github workflow, and if you do not find the issue, post an issue on [the Image.sc Forum](http://forum.image.sc/) with the failing log!

#### Naming your versions!

You can put a `-SNAPSHOT` suffix to your repo to deploy a snapshot version of it. To make a release, commit the repo without the SNAPSHOT suffix, run the publish workflow, then immediately make a new commit with a higher version and a SNAPSHOT version. All of this is automated with scijava-scripts, but you currently have to do it manually with gradle projects.

Example of developpement:

* initial commit > org.my:myrepo:0.1.0-SNAPSHOT > publish snapshot
* commit "add stuff" > org.my:myrepo:0.1.0-SNAPSHOT
* commit "add a fancy feature" > org.my:myrepo:0.1.0-SNAPSHOT > publish snapshot ( because you want to erase the previous snapshot)
* commit "small fix" > org.my:myrepo:0.1.0-SNAPSHOT
* commit "release v0.1.0, remove SNAPSHOT suffix" > org.my:myrepo:0.1.0 > **publish 0.1.0** release
* commit "bumps to next development cycle, adds SNAPSHOT suffix 0.1.1-SNAPSHOT" > org.my:myrepo:0.1.1-SNAPSHOT > publish 0.1.1-SNAPSHOT
* and so on.

You will need to change the version number manually, and also run the github publish workflow manually.

#### Example

If you want to see a project which uses all of this, have a look at [https://github.com/BIOP/qupath-extension-warpy](https://github.com/BIOP/qupath-extension-warpy)

## Consuming a SciJava artifact in a Gradle build.gradle script

The core artifacts in the SciJava software stack (e.g. [SciJava](/libs/scijava), [ImgLib2](/libs/imglib2), [ImageJ2](/software/imagej2), [SCIFIO](/libs/scifio), [Fiji](/software/fiji)) are built with [Maven](maven), but can also be consumed in a Gradle build script.

Contributed<sup>[1](https://github.com/imagej/tutorials/issues/24)</sup> by {% include person id='reckbo' %}

```groovy
buildscript {
    repositories {
        maven {
            url "https://plugins.gradle.org/m2/"
        }
    }
    dependencies {
        classpath "io.spring.gradle:dependency-management-plugin:0.5.4.RELEASE"
    }
}
apply plugin: "io.spring.dependency-management"

repositories {
    mavenCentral()
    maven {
            url "https://maven.scijava.org/content/groups/public/"
    }
}
dependencyManagement {
    imports {
        mavenBom 'org.scijava:pom-scijava:43.0.0'
    }
}

dependencies {
    compile 'net.imagej:imagej'
}
```
