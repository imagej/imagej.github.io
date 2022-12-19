---
mediawiki: Miji
title: Miji
project: /software/fiji
categories: [Tutorials,MATLAB]
---

{% include notice icon="info" content='This page covers the original compatibility layer for running ImageJ within MATLAB.  
The current library for ImageJ/MATLAB integration is [ImageJ-MATLAB](/scripting/matlab); it has many advantages over this legacy project.' %}

[MIJ](http://bigwww.epfl.ch/sage/soft/mij/) is a java package to exchange images between [MATLAB](/scripting/matlab) and the original [ImageJ](/software/imagej). It is written by {% include person id='dasv74' %} (Biomedical Image Group (BIG), Ecole Polytechnique Fédérale de Lausanne (EPFL), Switzerland) and {% include person id='dprodanov' %} (Department of Physiology and Pharmacology, Université Catholique de Louvain (UCL), Brussels, Belgium). It allows to start a instance of ImageJ inside [MATLAB](/scripting/matlab) and exchange images back and forth with it. It takes advantage of the fact that the user interface of [MATLAB](/scripting/matlab) is written in Java.

For your convenience, Jacques Pecreaux & {% include person id='dscho' %} wrote `Miji.m`, which makes it super-easy to use [Fiji](/software/fiji) and the libraries and functions provided by Fiji's components from within [MATLAB](/scripting/matlab). Simply make sure that the `scripts/` directory of your `Fiji.app/` is in [MATLAB](/scripting/matlab)'s search patch, via {% include bc path='File | Set Path...'%} (on Mac, the file chooser doesn't let you choose directories within .app packages, so you have to use the [MATLAB](/scripting/matlab) command `addpath('/Applications/Fiji.app/scripts')`). Then a simple

```matlab
Miji;
```

will start a Fiji inside [MATLAB](/scripting/matlab).

{% include notice icon="warning" content='There are over 300 jar and plugin files that ship with Fiji, and depending on your operating system and configuration, you may run into **too many files open** errors (for example, on macOS [MATLAB](/scripting/matlab) seems to use the default soft limit for open files, which is typically 256). If this happens you will need to increase the open file limit per-session or system-wide. See [this guide](http://docs.basho.com/riak/latest/ops/tuning/open-files-limit/) for helpful instructions on doing so for macOS and Linux.' %}

# Getting started

## Using MATLAB as processing core and sending results to Fiji

An example how to work with MIJ is provided here:

```matlab
MIJ.run('Embryos (42K)');
I = MIJ.getCurrentImage;
E = imadjust(wiener2(im2double(I(:,:,1))));
imshow(E);
MIJ.createImage('result', E, true);
```

If you get an error saying that some Plugin related classes cannot be found, please update your Fiji with {% include bc path='Help | Update Fiji'%}!

## Running ImageJ commands

In ImageJ, you can [record macros](https://imagej.net/ij/docs/guide/146-31.html#sub:Record...), one of the most powerful ways to use the program. Most of the recorded statements will look like this:

```javascript
run("Command", "key1=7 key2 key3=[C:\\Documents and Settings\\Fiji\\Test.png]");
```

The first parameter to the `run()` method is the menu item's label which identifies the plugin to run (in this example, the label would read: *Command*).

The second parameter is a String containing values the user specified via an [ImageJ dialog](http://javadoc.scijava.org/ImageJ1/ij/ij/gui/GenericDialog.html). Every value is identified by a label, and except for checkboxes (such as `key2` in the example above), they have values. If the values contain spaces, you need to enclose the value in square brackets (such as `key3` in the example above).

Note that the backslash is a so-called *escape character*, i.e. it can be used to insert special characters such as line breaks or tabs. To insert a plain backslash, it has to be repeated therefore (as in the `key3` value: `C:\\Documents and Settings` becomes `C:\\\\Documents and Settings`).

You can use those recorded statements in a slightly modified form via MIJ:

1.  replace the double quotes by single quotes
2.  prefix the `run` name with `MIJ.`

The above example would read like this:

```matlab
MIJ.run('Command', 'key1=7 key2 key3=[C:\\Documents and Settings\\Fiji\\Test.png]');
```

Note: in [MATLAB](/scripting/matlab), it is not strictly necessary to end the `MIJ.run()` statement with a semicolon, because it does not return anything. However, it is good practice with MIJ to end all statements in semicolons: some functions return images, cluttering the output and taking a very long time to print if the statement does not end in a semicolon.

## Opening images

Normally, the best way to use MIJ is to [use ImageJ's macro recorder](#running-imagej-commands). However, this procedure does not work when opening images because ImageJ records simply: `open("/path/to/image.png");`

Instead, one needs to keep in mind how `run()` statements are constructed and imitate it for the `Open...` command:

```matlab
MIJ.run('Open...', 'path=[C:\\Documents and Settings\\Fiji\\Test.png]');
```

## Using Fiji as a 3D viewer for MATLAB

A set of demos made for [MATLAB](/scripting/matlab) users, and introducing how to install and use Fiji as a visualization tool for [MATLAB](/scripting/matlab) is published on the [fex](http://www.mathworks.com/matlabcentral/fileexchange/32344-hardware-accelerated-3d-viewer-for-matlab).

# Getting help

To get a quick help on the available functions, call

```matlab
MIJ.help
```

Further descriptions and example code can be found on [the home page for MIJ](http://bigwww.epfl.ch/sage/soft/mij/). Eventually, detailed documentation about the class MIJ can be found [here](http://bigwww.epfl.ch/sage/soft/mij/doc/index.html) (suitable if you have a bit of experience with Java).

  
![](/media/plugins/mij-splash.jpg)

# Alternative: do not start the Fiji GUI

If you want to use the functions without starting Fiji's graphical interface, just call

```matlab
Miji(false);
```

# Links

A related project is [MatlabControl](http://code.google.com/p/matlabcontrol/) which allows you to start [MATLAB](/scripting/matlab) conveniently from within Java.
