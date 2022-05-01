---
title: Building a POM
section: Extend:Development:Guides
---

When you start a new [Maven](/develop/maven) project, one of the first things you will do is create an appropriate [pom.xml](https://maven.apache.org/pom.html). The POM determines what resources are available to your project. Given the scope of the ImageJ project, there are several possible starting points. The purpose of this guide is to help you select a pom.xml based on your individual project's goals.

# Using ImageJ

```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <project xmlns="http://maven.apache.org/POM/4.0.0"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
            http://maven.apache.org/xsd/maven-4.0.0.xsd">
        <modelVersion>4.0.0</modelVersion>

        <parent>
            <groupId>org.scijava</groupId>
            <artifactId>pom-scijava</artifactId>
            <version>12.0.0</version>
            <relativePath />
        </parent>

        <groupId>[MY-GROUP-ID]</groupId>
        <artifactId>[MY-ARTIFACT-ID]</artifactId>
        <version>0.1.0-SNAPSHOT</version>

        <name>[MY-PROJECT]</name>
        <description>[MY-DESCRIPTION]</description>
        <url>https://github.com/[MY-ORG]/[MY-REPO]</url>
        <inceptionYear>[MY-PROJECT'S-FIRST-YEAR]</inceptionYear>
        <organization>
            <name>[MY-ORGANIZATION-NAME]</name>
            <url>[MY-ORGANIZATION-WEB-SITE]</url>
        </organization>
        <licenses>
            <license>
                <name>CC0 1.0 Universal License</name>
                <url>http://creativecommons.org/publicdomain/zero/1.0/</url>
                <distribution>repo</distribution>
            </license>
        </licenses>

        <developers>
            <developer>
                <id>[MY-GITHUB-ID]</id>
                <name>[MY-FULL-NAME]</name>
                <url>https://imagej.net/people/[MY-GITHUB-ID]</url>
                <roles>
                    <!-- see https://imagej.net/Team -->
                    <role>founder</role>
                    <role>lead</role>
                    <role>developer</role>
                    <role>debugger</role>
                    <role>reviewer</role>
                    <role>support</role>
                    <role>maintainer</role>
                </roles>
            </developer>
        </developers>
        <contributors>
            <contributor>
                <name>None</name>
            </contributor>
        </contributors>

        <mailingLists>
            <mailingList>
                <name>Image.sc Forum</name>
                <archive>https://forum.image.sc/</archive>
            </mailingList>
        </mailingLists>

        <scm>
            <connection>scm:git:git://github.com/[MY-ORG]/[MY-REPO]</connection>
            <developerConnection>scm:git:git@github.com:[MY-ORG]/[MY-REPO]</developerConnection>
            <tag>HEAD</tag>
            <url>https://github.com/[MY-ORG]/[MY-REPO]</url>
        </scm>
        <issueManagement>
            <system>GitHub Issues</system>
            <url>http://github.com/[MY-ORG]/[MY-REPO]/issues</url>
        </issueManagement>
        <ciManagement>
            <system>None</system>
        </ciManagement>

        <properties>
            <main-class>[MY-MAIN-CLASS-INCLUDING-PACKAGE]</main-class>
            <package-name>[MY-PACKAGE-PREFIX]</package-name>
            <license.licenseName>cc0</license.licenseName>
            <license.copyrightOwners>N/A</license.copyrightOwners>
        </properties>

        <repositories>
            <repository>
                <id>scijava.public</id>
                <url>https://maven.scijava.org/content/groups/public</url>
            </repository>
        </repositories>

        <dependencies>
            <!-- ImageJ dependencies -->
            <dependency>
                <groupId>net.imagej</groupId>
                <artifactId>imagej</artifactId>
            </dependency>

            <!-- Test dependencies -->
            <dependency>
                <groupId>junit</groupId>
                <artifactId>junit</artifactId>
                <scope>test</scope>
            </dependency>
        </dependencies>
    </project>
```
-   Replace the `[MY-...]` blocks with appropriate information.
-   Replace license-related blocks with your chosen project license.

## Optional dependencies

Simply copy and paste any or all of these into your POM's <dependency> block to add the indicated functionality.


    <!-- User-facing commands -->
    <dependency>
        <groupId>net.imagej</groupId>
        <artifactId>imagej-plugins-commands</artifactId>
    </dependency>

    <!-- Run graphically with the classic ImageJ user interface -->
    <dependency>
        <groupId>net.imagej</groupId>
        <artifactId>imagej-legacy</artifactId>
    </dependency>

    <!-- Include all Fiji plugins when running -->
    <dependency>
        <groupId>sc.fiji</groupId>
        <artifactId>fiji</artifactId>
    </dependency>
