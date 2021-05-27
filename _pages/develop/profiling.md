---
mediawiki: Profiling_Java_Code
title: Profiling Java Code
---

If your Java code seems to have bottlenecks that make it run slow, you need to *profile* the code. There are a couple of options you have for that.

## JProfiler

[JProfiler](http://www.ej-technologies.com/products/jprofiler/overview.html) is a commercial program, but you can evaluate a trial version.

## HPROF

Use [HPROF](http://java.sun.com/developer/technicalArticles/Programming/HPROF.html), a profiler included in Sun's Java since version 1.5.

## Java Mission Control

Starting with Java 1.7 update 40, Oracle bundles [Java Mission Control](http://www.oracle.com/technetwork/java/javaseproducts/mission-control/index.html) with their JREs/JDKs. This provides incredibly powerful monitoring/profiling capabilities, but it is notably lacking from OpenJDK.

The most important part of Java Mission Control to enable efficient profiling is the *Flight Recorder*. The flight recorder has to be enabled explicitly at startup:

    java -XX:+UnlockCommercialFeatures -XX:+FlightRecorder [...]

The easiest way to use the flight recorder to profile a certain code path, say, from Eclipse, is to write a JUnit test (make sure that the time it runs is dominated by the code paths you want to profile!) and then add a run configuration for it whose JVM arguments include:

    -Dscijava.log.level=error \
    -XX:+UnlockCommercialFeatures -XX:+FlightRecorder \
    -XX:StartFlightRecording=name=MyRecording,duration=999s,filename=/tmp/a1.jfr,settings=profile

(Of course you want to avoid copying this blindly and adjust in particular the **duration** and the **filename** parameters.)

After the JUnit test finishes, call *Java Mission Control* via the `jmc` executable (it lives in the JDK's *bin/* directory), {% include bc path='File | Open File'%} the *.jfr* file, click on the *Code* button in the center of the Mission Control window, select the *Hot Methods* tab of the big panel (confusingly, the tabs are at the bottom) and inspect the stack traces.

## VisualVM

Use [VisualVM](http://download.oracle.com/docs/cd/E17409_01/javase/6/docs/technotes/guides/visualvm/index.html) (a tutorial can be found [here](http://java.dzone.com/articles/profile-your-applications-java)), which is a graphical alternative to HPROF, available in Sun's Java since version 6 update 7.

See also [Rejeev Divakaran's detailed instructions on memory profiling with VisualVM](http://rejeev.blogspot.com/2009/04/analyzing-memory-leak-in-java.html).

## OProfile

If you are on Linux, you can use [OProfile](http://oprofile.sourceforge.net/news/), a low-overhead profiler which uses a kernel module to minimize its impact.

You need to [recompile OProfile](http://oprofile.sourceforge.net/doc/setup-jit.html#setup-jit-jvm) for Java support (at least on Ubuntu, there is no precompiled OProfile package with Java support). On Linux, you can use this shell script to compile and install it:

    sudo apt-get install libpopt-dev binutils-dev checkinstall && 
    git clone git://oprofile.git.sourceforge.net/gitroot/oprofile/oprofile && 
    cd oprofile && 
    ./autogen.sh && 
    ./configure --with-kernel-support \
            --with-java=/path/to/fiji/java/linux-amd64/jdk1.6.0_24/ &&
    make && 
    sudo checkinstall

You should make sure that the path to the JDK is correct. (But you do not need to use *checkinstall*, but it will make it easy to remove the package once you do not want it anymore.)

### Start the profiler

    sudo opcontrol --start --no-vmlinux

Recent versions of OProfile require that a user account *oprofile* with default group *oprofile* exist before starting the OProfile daemon. On current Ubuntu systems, you can make one by calling **sudo adduser oprofile** (Ubuntu creates a default group of the same name for each new user account). If you do not have such an account, you will get something like *anon (tgid:10014 range:0x100000-0x103000)* in the report.

### Start Fiji with support for profiling

`fiji -agentpath:/usr/local/lib/oprofile/libjvmti_oprofile.so --`

### Stop the profiler

    sudo opcontrol --stop

### Getting at the profiling data

    sudo opcontrol --dump && 
    opreport -l image:\*/fiji

If you get entries like *"anon (tgid:10014 range:0x100000-0x103000)* you probably did not create a user account *oprofile* in a group *oprofile* before starting the OProfile daemon.

To get information about source files and line numbers, also pass the *-g* option to *opreport*.

### Further reading

See the [OProfile manual](http://oprofile.sourceforge.net/doc/) for more information.

## Shark (for macOS)

You might find [Shark 4](http://developer.apple.com/tools/sharkoptimize.html) useful if you're on macOS.

# Memory profiling

Even if Java's memory management prevents most memory issues (unaligned writes, access to uninitialized/released memory), there is a chance of memory leaks: constant accumulation of objects over time, most likely because there are stale references to them.

Note: *heap* is Java speak for *memory*.

## Javassist-based

A quite versatile method is to use (and possibly modify) the class {% include github org='fiji' repo='fiji-compat' source='fiji/MemoryProfiler.java' label='fiji.MemoryProfiler' %} in *fiji-compat.jar*.

This memory profiler instruments all method entries and exists using javassist. At each exit, it reports the relative memory usage, the total memory usage, and the exit point of the current method. Call it like this:

    ./fiji --main-class fiji.MemoryProfiler fiji.Main

Since the memory profiling slows down execution dramatically due to the synchronous output to stderr, you may want to limit the classes to be instrumented by setting the environment variable *MEMORY\_PROFILE\_ONLY* to a space-delimited list of classes.

If you want to instrument any class handled by {% include github org='imagej' repo='imagej-legacy' label='imagej-legacy' %}, you need to use the slightly more complicated command line:

    ./fiji -Dpatch.ij1=false --cp jars/javassist.jar --cp jars/fiji-compat.jar \
        --cp jars/ij.jar --main-class fiji.MemoryProfiler -- ij.ImageJ

## Using JVisualVM

JDK6 and newer come with a quite useful tool called *jvisualvm*. It is in the *bin/* directory of the Java Development Kit (it does not come with the JRE, also known as *Java Runtime Environment*).

JVisualVM lets you attach to any local Java process and inspect the state. The most useful parts for memory profiling are the *Memory* section in the *Monitor* tab, showing the overall heap usage (where you can also make a Heap Dump which produces a double-clickable list of objects and their references), and the *Memory* button on the *Sampler* tab, which opens kind of a live version of the Heap Dump.

When looking at a Heap Dump, make sure you click on the *Classes* button in the top row. This shows the list of classes that currently have referenced instances in the Java Virtual Machine. Double-clicking on the class name will open a detailed list of instances of that class, and when clicking on one item in that list, the upper right panel will show that instance's fields while the lower right panel will show the objects holding references to that particular instance.

Note: at no time will JVisualVM stop the virtual machine it is attached to, so if the issues you experience are time-sensitive, you definitely want to put stop-gaps into the code to be able to look at things closely.


