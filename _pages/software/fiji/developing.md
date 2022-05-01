---
title: Developing Fiji
section: Explore:Software:Fiji
---


{% include warning/outdated %}


Fiji is a community effort. So we are happy whenever we see new people developing Fiji!

## Purpose

The purpose of this tutorial is to get you started hacking on [Fiji's source code](https://github.com/fiji/) (i.e., the core Fiji plugins). If you need to develop a *new plugin* for ImageJ, you do not actually need Fiji's source. Rather, see these resources:

-   {% include github org='imagej' repo='example-legacy-plugin' label='example-legacy-plugin' %} project template
-   [Introduction into Developing Plugins](/develop/ij1-plugins) tutorial
-   [Developing ImageJ 1.x plugins with NetBeans](https://www.youtube.com/watch?v=Ac-6gJ2eRb0) screencast

See also [Developing Fiji in Eclipse](/develop/eclipse) for a tutorial specific to the Eclipse IDE.

## Getting started

First, you have to [download and build Fiji](/software/fiji/building-from-source). If you do not know Git yet, we have a [concise introduction](/develop/git) for you.

## Building Fiji

Fiji is organized into a set of [Maven](/develop/maven) projects. For convenience and speed, there is [SciJava](/libs/scijava)'s minimal Maven-lookalike [MiniMaven](/develop/minimaven) to build Fiji, but it is recommended to use an [Integrated Development Environment](/develop/ides), or at least real Maven.

For details, please see [Downloading and Building Fiji From Source](/software/fiji/building-from-source). See also the [Supported Compilers](/develop/supported-compilers) page for more information.

## Testing

It is strongly recommended to write regression tests (also known as *unit tests*). It is [easy](/contribute/fiji#regression-tests).

Furthermore, it is highly recommended to write and run unit tests in an [Integrated Development Environment](/develop/ides) for efficient debugging. You may also want to measure the {% include wikipedia title="code coverage" %} of your tests.

At some point, you might want to debug whatever you wrote. There's a small [Debugging intro](/develop/debugging) page.

## Discussing code

When you want to propose and/or discuss changes to some source code, the preferred way is to [submit a PR on GitHub](/contribute).

## Contributing

Please have a look at the excellent *[How to contribute to an existing plugin or library](/develop/improving-the-code)* tutorial.

## Providing documentation

A plugin wants to be used. Therefore you want to give users some information about it, and most likely also a tutorial how to use it.

If you have an account on this Wiki, you can easily create new tutorials with the [Tutorial Maker](/plugins/tutorial-maker).

## Further reading for developers

-   [Overview of Fiji's source code](/software/fiji/source)
-   [Description of ImageJ's plugin architecture](/develop/plugin-architecture)
-   [Tips for developers](/develop/tips)
-   [Developers HowTo](/develop/using-weka)
-   [ImageJ plugin writing tutorial](http://www.imagingbook.com/index.php?id=102)
-   [ImageJ programming tutorials](http://albert.rierol.net/imagej_programming_tutorials.html)
-   [Uploading plugins](/develop/uploading-plugins)
-   [Developing Fiji in Eclipse](/develop/eclipse)
-   [Git](/develop/git)
-   [Project ideas](Project_ideas)
-   [Introduction to debugging](/develop/debugging)
-   [Profiling Java Code](/develop/profiling)
-   [Tips for C++ developers](/develop/cpp-tips)

 
