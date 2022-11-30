---
title: Running Headless
nav-links: true
nav-title: Headless
---

[ImageJ](/software/imagej) was never meant as anything else than a desktop application with one user in front of one screen attached to one computer.

However, it acquired [macro](/scripting/macro) capabilities, a [batch mode](/scripting/batch) for such macros, and even [scripting](/scripting) support.

Naturally, users want to execute such [macros](/scripting/macro) or [scripts](/scripting) in environments such as clusters where there is no graphical user interface available.

# `--headless` mode

To address all of these needs, [ImageJ2](/software/imagej2) provides the capability to execute ImageJ plugins, macros and scripts in headless mode. This feature uses bytecode manipulation to patch ImageJ's behavior at runtime, making it possible to start ImageJ in batch mode without instantiating GUI components.

**Shortcoming:** There are plugins which are even more bound to a GUI than
ImageJ is. Naturally, these plugins will still try to instantiate GUI
elements when being called in headless mode, failing.

## Running scripts in headless mode

Please see the [headless scripting guide](/scripting/headless).

## Running macros in headless mode

To run a *macro* in headless mode via a command prompt, first open a command prompt in the Fiji.app or ImageJ directory where the .exe (on windows) of ImageJ resides.  Then use the following syntax, with the `-macro` command line argument along with the `--headless` option, as follows:

```shell
ImageJ --headless --console -macro path-to-Macro.ijm
```
The `--console` flag is optional, it only ensures that print statements and error messages are shown in the command prompt.    
However, **it also has a side effect of preventing the command prompt from "returning" after execution**, in effect giving the impression that the code is hanging. This is especially not desirable if calling ImageJ from an external program : the external program would just wait indefinitly for the execution to terminate.   
**An external program can still access the printed statements without the `--console` flag**, by redirecting the standard/error output of the process (ImageJ.exe).  

If you omit the `--headless` flag, the GUI will open and the macro will be executed.  

If the macro resides in ImageJ's macro directory, it is possible to specify the macro name instead of the actual file path. The file extension is always very recommended but for backwards compatibility, it is not strictly required *only* when specifying the macro name instead of a path.


You can even pass parameters to the macro; e.g.:

```shell
./ImageJ-win64.exe --headless --console -macro ./RunBatch.ijm 'folder=../folder1 parameters=a.properties output=../samples/Output'
```

In that case, the RunBatch.ijm file should be something like:

```javascript
arg = getArgument()
print("Running batch analysis with arguments:")
print(arg)
run("Batch process", arg )
print("Done.")
eval("script", "System.exit(0);");
```

the `getArgument()` is used to grab the parameter string itself, and it is then passed to an IJ command.

{% include notice icon="warning" content='Please note that you will not be able to use [script parameters](/scripting/parameters) with `-macro`. Follow instructions in [Scripting Headless](/scripting/headless) instead.' %}

Some ImageJ commands relying on the GUI do not work in headless mode such as : 
- `selectWindow("name")`, use `selectImage(title)` instead for images  
- `Table.Rename("oldTitle", "newTitle")`


{% capture historical-note %}
Headless support was originally a branch in [ImageJA](/libs/imageja); it worked
by putting rewritten versions of three core ImageJ classes into a file called
`headless.jar`, which was put into the class path *before* `ij.jar` so they
would override ImageJ's versions.

Nowadays, we use [Javassist](/develop/javassist) for run-time patching, through
the
{% include github org='imagej' repo='ij1-patcher' label='ImageJ patcher' %}
project. You do not need to do anything special to
take advantage of this feature, except pass the `--headless` flag when
launching ImageJ from the command line.
{% endcapture %}
{% include aside title="Historical note" content=historical-note %}


# Why is `--headless` needed?

Java *does* support a headless mode via the `java.awt.headless` property; setting this property to `true` enables it.

Unfortunately, with X11-based Java (such as on Linux, which is the most prevalent platform for running clusters), headless mode does not allow to instantiate any GUI components that would want to display text. The reason is that the font-metrics on X11 are provided by the X11 server (and are indeed different between servers) and therefore the dimensions of such elements simply cannot be calculated without a graphical desktop.

Since ImageJ was devised as a desktop application, everything -- including macros -- works through the GUI. For example, a simple `run("Open...");` will look for the action in the menu.

On macOS, there is no problem: Aqua provides GUI-independent text rendering (mapping to the actual display using anti-aliasing). There, running in headless mode allows instantiating GUI elements such as the menu bar.

# Other solutions
## Xvfb virtual desktop

Another method is to have a virtual desktop, e.g. {% include wikipedia title='Xvfb' text='Xvfb'%}. This will allow ImageJ to start with a virtualised graphical desktop.

**Advantage:** No run-time patching is required.

**Shortcomings:** It is slower than it needs to be because of the overhead of starting the GUI, it is harder to configure, and plugins might get stuck because they wait for user input which never comes.

### Examples

Here are a couple of simple examples.

Passing direct arguments:

```shell
$ cat hello.js
importClass(Packages.ij.IJ);
IJ.log("hello " + arguments[0]);
$ xvfb-run -a $IMAGEJ_DIR/ImageJ-linux64 hello.js Emerson
hello Emerson
```

With [SciJava script parameters](/scripting/parameters):

```shell
$ cat hello-with-params.js
// @String name
importClass(Packages.ij.IJ);
IJ.log("hello " + name);
$ xvfb-run -a $IMAGEJ_DIR/ImageJ-linux64 --ij2 --headless --run hello-with-params.js 'name="Emerson"'
hello Emerson
```

A more complex shell script that wraps a macro for use with Xvfb (thanks to Nestor Milyaev):

```javascript
export DISPLAY=:1
Xvfb $DISPLAY -auth /dev/null &
(
# the '(' starts a new sub shell. In this sub shell we start the worker processes:

script=$scriptDir"lsmrotate2nrrd.ijm \"dir="$1"&angle-x=$2&angle-y=
$3&angle-z=$4&reverse=$5\" -batch"
$imagejBin -macro $script # running the actual ijm script

wait # waits until all 'program' processes are finished
# this wait sees only the 'program' processes, not the Xvfb process
)
```

See also [this post on the ImageJ mailing list](https://list.nih.gov/cgi-bin/wa.exe?A2=IMAGEJ;5ace1ed0.1508).

## Rewriting as scripts or plugins

The most robust method is to rewrite macros as scripts that do not require interaction with the GUI to begin with. Unfortunately, this is the most involved solution, too, since it usually takes some time to convert macros.
