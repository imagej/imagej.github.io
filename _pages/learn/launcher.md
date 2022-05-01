---
title: ImageJ Launcher
nav-links: true
nav-title: Launcher
---

The ImageJ launcher is a native application for launching ImageJ.

## Introduction

The launcher supports the following flavors of ImageJ:

-   [ImageJ](/software/imagej)
-   [ImageJ2](/software/imagej2)
-   [Fiji](/software/fiji)

The launcher is a native executable whose purpose is to start up a Java Virtual Machine and run ImageJ, ImageJ2, or Fiji in it. It is used in the [Fiji](/software/fiji) distribution as well as in [ImageJ2](/software/imagej2).

## Source

The ImageJ launcher source code lives {% include github org='imagej' repo='imagej-launcher' %}.

## Purpose

The launcher provides a platform-specific entry point into the ImageJ Java application. Its most major function is to facilitate the ImageJ Updater feature by taking care of pending updates when ImageJ is first launched.

## Usage

For an overview of supported options, run:

```
./ImageJ-xyz --help
```

where `xyz` is your platform.

The launcher can do all kinds of things, like:

-   Launch ImageJ with a different amount of memory (`--mem` option)
-   Run [macros and scripts in headless mode](/learn/headless)
-   Control the [Updater](/plugins/updater) from the command line
-   Open images: `./ImageJ-<platform> example.jpg`
-   Call Jython scripts: `./ImageJ-<platform> example.py` (also works for JRuby scripts when they have an `.rb` extension, for Beanshell scripts with `.bsh` extension, `.clj` for Clojure and `.js` for Javascript)
-   Call the Jython interpreter: `./ImageJ-<platform> --jython` (the classpath will be the same as when calling ImageJ), and likewise `--jruby`, `--bsh` and `--js` for the respective language's command-line interpreters
-   Run ImageJ with the system Java instead of its own one: `./ImageJ-<platform> --system`. But beware: this might fail since some plugins need at least Java 1.5, and the 3D viewer needs Java3D.
-   Show the java command line instead of running ImageJ: `./ImageJ-<platform> --dry-run`
-   Compile a Java class: `./ImageJ-<platform> --javac example.java`
-   Run a Java class' main() method: `./ImageJ-<platform> --main-class=example`
-   Pass some [Java options](/Java_Options): `./ImageJ-<platform> -server --` (everything that comes before a `--` is interpreted as Java option)
-   Add `.` to the classpath and execute the given class' `main()` method: `./ImageJ-<platform> Example.class`
-   Link ImageJ into the PATH: `ln -s $(pwd)/ImageJ-<platform> $HOME/bin/fiji && fiji`
-   Start ImageJ and run a menu entry directly: `./ImageJ-<platform> --run System_Clipboard` (the underscore was used in place of a space to avoid having to quote the argument)

## Download

The launcher comes with ImageJ, ImageJ2 and Fiji.

If you want to test the latest UNSTABLE version, it can downloaded here:

* [![Windows (32-bit)](/media/icons/windows.svg){:width="24px"} ImageJ-win32.exe](https://maven.scijava.org/service/local/artifact/maven/redirect?r=snapshots&g=net.imagej&a=imagej-launcher&v=LATEST&e=exe&c=win32)
* ![Windows (64-bit)](/media/icons/windows.svg){:width="24px"} [ImageJ-win64.exe](https://maven.scijava.org/service/local/artifact/maven/redirect?r=snapshots&g=net.imagej&a=imagej-launcher&v=LATEST&e=exe&c=win64)
* ![macOS](/media/icons/macos.png){:width="24px"} [ImageJ-macosx](https://maven.scijava.org/service/local/artifact/maven/redirect?r=snapshots&g=net.imagej&a=imagej-launcher&v=LATEST&e=exe&c=macosx)
* ![Linux (64-bit)](/media/icons/linux.svg){:width="24px"} [ImageJ-linux64](https://maven.scijava.org/service/local/artifact/maven/redirect?r=snapshots&g=net.imagej&a=imagej-launcher&v=LATEST&e=exe&c=linux64)

After download, rename to match the filename given above. For macOS and Linux binaries, set the executable bit using `chmod +x`. Then replace the launcher with the new one, keeping a backup of the previous launcher in case the new one does not work.

## Java options

ImageJ is written mainly in Java. Therefore, we rely on the Java virtual machine to do a good job for us. Sometimes, you have to help it, by providing some Java options to ImageJ.

There are basically two ways to do that:

- By passing the parameters to the ImageJ launcher, separated by `--` from the ImageJ options.

{% include notice icon="note" content="Even if you do not pass ImageJ options at all, you need to add the separator, otherwise ImageJ thinks you passed it an ImageJ option. Example:<br>`./ImageJ-linux64 -XX:+HeapDumpOnOutOfMemoryError --`" %}

- By modifying/creating the file `ImageJ.cfg` in the same directory as the ImageJ launcher.

{% include notice icon="note" content="The options listed in `ImageJ.cfg` will be passed to the virtual machine before the options passed on the command line, so that the command line can override the options specified in `ImageJ.cfg`." %}

Which method is appropriate for you depends on what you want to do: if you want to change ImageJ's default, use the `ImageJ.cfg` method.

### Example ImageJ.cfg

`ImageJ.cfg` will change the default settings for the launcher. The file should be located in the same directory as the launcher, usually `Fiji.app`. An example `ImageJ.cfg` is as follows:

```
# ImageJ startup properties
maxheap.mb = 1024
jvmargs = -XX:+HeapDumpOnOutOfMemoryError -Xincgc
legacy.mode = false
```

#### Keys

- `maxheap.mb` The integer value is passed as a `-Xmx` option to the JVM set the maximum heap size. See below.
- `jvmargs` Arguments passed to the Java Virtual machine.
- `legacy.mode` Deprecated option to disable use of the legacy `ImageJ.cfg`. In recent versions of the launcher, this is [ignored](https://github.com/imagej/imagej-launcher/commit/0c3902642829b40a8ed72edd5ea3fbc1a3872acf).

Note that this differs from an [older legacy format](https://imagej.nih.gov/ij/docs/install/windows.html) and that the first "# ImageJ startup properties" comment line is [required](https://github.com/imagej/imagej-launcher/blob/0c3902642829b40a8ed72edd5ea3fbc1a3872acf/src/main/c/config.c#L116-L123).

### The double-dash

**(or: how to separate Java options and ImageJ options from command line options)**

It can be confusing to pass ImageJ and Java options at the same time as command line options to ImageJ (or other programs). So here are a few simple rules:

-   If you do not specify any Java options, you do not need a `--` at all.
-   If you have a `--` in your command line, the arguments for ImageJ go *after* the double-dash.
-   In the presence of a double-dash, ImageJ options have to go *before* the `--` (this is to allow passing options to the Java program that would be mistaken for ImageJ options otherwise).

Examples:

```
# pass a single ImageJ option (no double-dash needed):
./ImageJ-linux64 --memory=64m

# pass a single Java option (double-dash needed):
./ImageJ-linux64 -Xincgc --

# pass a Java option (requiring a double-dash), a ImageJ option (which must be before the double-dash now) and an option to the program
./ImageJ-linux64 -Xincgc --ant -- --help

# pass an option to the Java program that is actually also available as ImageJ option
./ImageJ-linux64 --ant -- --help
```

{% include notice icon="note" content="In the last example, *Ant* gets to see the option `--help`, which ImageJ would have interpreted itself if it were passed before the double dash." %}

These examples are gleaned from [Headius' blog](http://blog.headius.com/2009/01/my-favorite-hotspot-jvm-flags.html):

### The basics

Most runs will want to tweak a few simple flags:

-   `-server` turns on the optimizing JIT along with a few other "server-class" settings. Generally you get the best performance out of this setting. The default VM is `-client,` unless you're on 64-bit (it only has `-server`).
-   `-Xms` and `-Xmx` set the minimum and maximum sizes for the heap. Touted as a feature, Hotspot puts a cap on heap size to prevent it from blowing out your system. So once you figure out the max memory your app needs, you cap it to keep rogue code from impacting other apps. Use these flags like `-Xmx512M`, where the *M* stands for *MB*. If you don't include it, you're specifying bytes. Several flags use this format. You can also get a minor startup perf boost by setting minimum higher, since it doesn't have to grow the heap right away.
-   `-Xshare:dump` can help improve startup performance on some installations. When run as root (or whatever user you have the JVM installed as) it will dump a shared-memory file to disk containing all of the core class data. This file is much faster to load then re-verifying and re-loading all the individual classes, and once in memory it's shared by all JVMs on the system. Note that `-Xshare:off`, `-Xshare:on`, `-Xshare:auto` set whether "Class Data Sharing" is enabled, and it's not available on the `-server` VM or on 64-bit systems. Mac users: you're already using Apple's version of this feature, upon which Hotspot's version is based.

There are also some basic flags for logging runtime information:

-   `-verbose:gc` logs garbage collector runs and how long they're taking. I generally use this as my first tool to investigate if GC is a bottleneck for a given application.
-   `-Xprof` turns on a low-impact sampling profiler. I've had Hotspot engineers recommend I "don't use this" but I still think it's a decent (albeit very blunt) tool for finding bottlenecks. Just don't use the results as anything more than a guide.
-   `-Xrunhprof` turns on a higher-impact instrumenting profiler. The default invocation with no extra parameters records object allocations and high-allocation sites, which is useful for finding excess object creation. `-Xrunhprof:cpu=times` instruments all Java code in the JVM and records the actual CPU time calls take.

#### Examples

1\. Run the JVM with fixed heap size at 4 Gb, and with incremental garbage collection.

```
./ImageJ-linux64 -Xms4000m -Xmx4000m -Xincgc --
```

-   The fixed heap size prevents out of memory errors because there isn't ever the need to resize it. If you define -Xms256m and -Xmx4000m, then when in need of exceeding 256m, a greater heap is allocated on the fly and the old one copied into the new one, which will fail when the sum of the sizes of the old and the new are bigger than what the computer can handle (or so I've been told, and indeed fixed heap size helps a lot to prevent incomprehensible out of memory errors.)
-   The incremental garbage collection runs a garbage collection in a parallel thread, avoiding long pauses and avoiding heap build-up that could lead to incomprehensible out of memory errors when suddenly attempting to allocate a lot of heap.

2\. Run the JVM as above, but launching a macro that opens a TrakEM2 project on startup.

```
./ImageJ-linux64 -Xms4000m -Xmx4000m -Xincgc -- -eval "open('/path/to/project.xml');"
```

3\. Run the JVM as above, but opening a clojure prompt instead of launching ImageJ:

```
./ImageJ-linux64 -Xms4000m -Xmx4000m -Xincgc --clojure
```

Even better if you have the jline library, enhance the clojure prompt with a up/down arrow history, etc.:

```
./ImageJ-linux64 -Xms4000m -Xmx4000m -Xincgc -cp /path/to/clojure-contrib.jar:/path/to/jline.jar --main-class jline.ConsoleRunner clojure.lang.Repl
```

You may do the same with `--jython` and `--jruby` for the homonimous languages.

4\. Launch the JVM with a debugging agent:

```
./ImageJ-linux64 -Xincgc -server -agentlib:jdwp=transport=dt_socket,address=8010,server=y,suspend=n --
```

To connect the debugger, launch the java debugger <i>jdb</i> at port 8010:

```
jdb -attach 8010
```

See some examples on using the jdb to [inspect the state of threads](http://albert.rierol.net/java_tricks.html#How%20to%20debug%20a%20multithreaded%20java%20program). Very useful to suspend all or one thread, print out their current stack trace, and list their status: sleeping, waiting in a monitor (i.e. likely dead-locked), etc.

I use many of the above combined into a script to launch ImageJ in a bash shell:

```
cd /home/albert/Programming/ImageJ
JAVA_HOME=/home/albert/Programming/ImageJ/java/linux-amd64/jdk1.8.0_172 ./ImageJ-linux64 -Xincgc -server \
-agentlib:jdwp=transport=dt_socket,address=8010,server=y,suspend=n -- "$@"
```

Notice the -- "$@" to pass any script arguments as ImageJ arguments.

### Deeper magic

Eventually you may want to tweak deeper details of the JVM:

-   `-XX:+UseParallelGC` turns on the parallel young-generation garbage collector. This is a stop-the-world collector that uses several threads to reduce pause times. There's also `-XX:+UseParallelOldGC` to use a parallel collector for the old generation, but it's generally only useful if you often have large numbers of old objects getting collected.
-   `-XX:+UseConcMarkSweepGC` turns on the concurrent mark-sweep collector. This one runs most GC operations in parallel to your application's execution, reducing pauses significantly. It still stops the world for its compact phase, but that's usually quicker than pausing for the whole set of GC operations. This is useful if you need to reduce the impact GC has on an application run and don't mind that it's a little slower than the full stop-the-world versions. Also, you obviously would need multiple processors to see full effect. (Incidentally, if you're interested in GC tuning, you should look at [Java SE 6 HotSpot Virtual Machine Garbage Collection Tuning](http://java.sun.com/javase/technologies/hotspot/gc/gc_tuning_6.html). There's a lot more there.)
-   `-XX:NewRatio=#` sets the desired ratio of "new" to "old" generations in the heap. The defaults are 1:12 in the `-client` VM and 1:8 in the `-server` VM. You often want a higher ratio if you have a lot more transient data flowing through your application than long-lived data. For example, Ruby's high object churn often means a lower NewRatio (i.e. larger "new" versus "old") helps performance, since it prevents transient objects from getting promoted to old generations.
-   `-XX:MaxPermSize=###M` sets the maximum "permanent generation" size. Hotspot is unusual in that several types of data get stored in the "permanent generation", a separate area of the heap that is only rarely (or never) garbage-collected. The list of perm-gen hosted data is a little fuzzy, but it generally contains things like class metadata, bytecode, interned strings, and so on (and this certainly varies across Hotspot versions). Because this generation is rarely or never collected, you may need to increase its size (or turn on perm-gen sweeping with a couple other flags).

And there are a few more advanced logging and profiling options as well:

-   `-XX:+PrintCompilation` prints out the name of each Java method Hotspot decides to JIT compile. The list will usually show a bunch of core Java class methods initially, and then turn to methods in your application. In JRuby, it eventually starts to show Ruby methods as well.
-   `-XX:+PrintGCDetails` includes the data from -verbose:gc but also adds information about the size of the new generation and more accurate timings.
-   `-XX:+TraceClassLoading` and `-XX:+TraceClassUnloading` print information class loads and unloads. Useful for investigating if you have a class leak or if old classes are getting collected or not.

### Into the belly

Finally here's a list of the deepest options we use to investigate performance. Some of these require a debug build of the JVM, which you can download from java.net.

Also, some of these may require you also pass `-XX:+UnlockDiagnosticVMOptions` to enable them.

-   `-XX:MaxInlineSize=#` sets the maximum size method Hotspot will consider for inlining. By default it's set at 35 *bytes* of bytecode (i.e. pretty small). This is largely why Hotspot really like lots of small methods; it can then decide the best way to inline them based on runtime profiling. You can bump it up, and sometimes it will produce better performance, but at some point the compilation units get large enough that many of Hotspot's optimizations are skipped. Fun to play with though.
-   `-XX:CompileThreshold=#` sets the number of method invocations before Hotspot will compile a method to native code. The -server VM defaults to 10000 and -client defaults to 1500. Large numbers allow Hotspot to gather more profile data and make better decisions about inlining and optimizations. Smaller numbers reduce "warm up" time.
-   `-XX:+LogCompilation` is like `-XX:+PrintCompilation` on steroids. It not only prints out methods that are being JITed, it also prints out why methods may be deoptimized (like if new code is loaded or a new call target is discovered) and information about which methods are being inlined. There's a caveat though: the output is seriously nasty XML without any real structure to it. I use a Sun-internal tool for rendering it in a nicer format, which I'm trying to get open-sourced. Hopefully that will happen soon. Note, this option requires `-XX:+UnlockDiagnosticVMOptions`.

And finally, my current absolute favorite option, which requires a debug build of the JVM:

-   `-XX:+PrintOptoAssembly` dumps to the console a log of all assembly being generated for JITed methods. The instructions are basically x86 assembly with a few Hotspot-specific instruction names that get replaced with hardware-specific instructions during the final assembly phase. In addition to the JITed assembly, this flag also shows how registers are being allocated, the probability of various branches being followed (along with multiple assembly blocks for the different paths), and information about calls back into the JVM.
