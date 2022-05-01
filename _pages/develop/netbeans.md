---
mediawiki: Developing_ImageJ_in_NetBeans
title: Developing ImageJ2 in NetBeans
section: Extend:Development:Tools:IDEs
project: /software/imagej2
---

{% include warning/outdated %}

This article explains how to install and configure NetBeans for use with [ImageJ2](/software/imagej2) development. Directions correspond to NetBeans 7.1.2, which added integrated Git support, and may need adjustment for other versions.

## Install and configure NetBeans

### Setting up NetBeans on Windows

#### Install Java Development Kit

Download and install [OpenJDK](https://www.azul.com/downloads/?package=jdk).

#### Install NetBeans

Download and install NetBeans from the [NetBeans website](http://netbeans.org/downloads/). Any bundle that includes Java SE should be fine.

### Setting up NetBeans on macOS

#### Install NetBeans

Download and install NetBeans from the [NetBeans website](http://netbeans.org/downloads/). Any bundle that includes Java SE should be fine.

### Setting up NetBeans on Linux

#### Install Java Development Kit

Install Java using the package manager—e.g., for Ubuntu 10.04:

```shell
sudo add-apt-repository "deb http://archive.canonical.com/ lucid partner"
sudo aptitude update
sudo aptitude install sun-java6-jdk sun-java6-plugin
sudo update-java-alternatives -s sun-java6-sun
```

#### Install NetBeans

Install NetBeans using the package manager—e.g., on Ubuntu:

```shell
sudo aptitude install netbeans
```

## Import the ImageJ2 source

1.  Choose {% include bc path="Team | Git | Clone..." %} from the NetBeans menu
2.  For the Repository URL, enter: [`git://github.com/imagej/imagej2`](git://github.com/imagej/imagej2)
3.  Click Next, check the `master\*` branch, then Next again, then Finish
4.  When prompted, click Open Project...
5.  Select the "ImageJ" project in the tree then click Open
6.  Right-click the "ImageJ" project and choose Build

You may receive a warning about Maven when building the project. It is not required, but if you wish to eliminate it, you can install Maven from the [Maven website](http://maven.apache.org/download.html).

## Launch the program

1.  Double-click the "ImageJ" project to open it
2.  Right-click the "ImageJ" project and choose "Run"
3.  On the Main Class dialog, choose `net.imagej.Main`

To expand the projects you can also right click on the top-level "ImageJ" and choose "Open Required Projects" (and "Close Required Projects" to close). During development you must select "Open Required Projects" before you can successfully do "Find Usages" in the "Open Projects" scope.

## See also

To develop the [original ImageJ](/software/imagej), see these resources:

-   [Developing ImageJ 1.x plugins with NetBeans](https://www.youtube.com/watch?v=Ac-6gJ2eRb0) screencast
-   {% include github org='imagej' repo='example-legacy-plugin' label='example-legacy-plugin' %} project template
-   [Developing Plugins for ImageJ 1.x](/develop/ij1-plugins) tutorial
