---
mediawiki: Debugging
title: Debugging
section: Extend:Development
---


 {% include notice icon="info" content='This page has approaches for *software developers* to use for debugging ImageJ and Fiji.
If you are a *user* looking to troubleshoot issues, see the [Troubleshooting](/learn/troubleshooting) page.' %}

## Launching in debug mode

To debug problems, it is often helpful to launch in debug mode. See the [Troubleshooting](/learn/troubleshooting#launching-imagej-from-the-console) page for instructions.

### Attaching to running instances

Sometimes, we need to debug things directly in ImageJ, for example because there might be issues with the plugin discovery (ImageJ wants to find the plugins in `ImageJ/plugins/`, and often we want to bundle them as `.jar` files, both of which are incompatible with Eclipse debugging). JDWP (*Java Debug Wire Protocol*) to the rescue!

After starting the Java Virtual Machine in a special mode, debuggers (such as Eclipse's built-in one) can attach to it. To start in said mode, you need to pass the `--debugger=<port>` option:

```shell
./fiji --debugger=8000
```

In Eclipse (or whatever {% include wikipedia title='JDWP' text='JDWP'%}-enabled debugger) select the correct project so that the source code can be found, mark the break-points where you want execution to halt (e.g. to inspect variables' values), and after clicking on {% include bc path="Run|Debug Configurations..." %} right-click on the *Remote Java Application* item in the left-hand side list and select *New*. Now you only need to make sure that the port matches the value that you specified (in the example above, `8000`, Eclipse's default port number).

If you require more control over the debugger configuration, you can also use the `-agentlib:jdwp=...` Java option directly (`--debugger=<port>` is just a shortcut for convenience):

```
./fiji -agentlib:jdwp=server=y,suspend=y,transport=dt_socket,address=localhost:8000 --
```
(the `--` marker separates the Java options—if any—from the program options). Once started that way, ImageJ will wait for the debugger to be attached, after printing a message such as:
```
> Listening for transport dt\_socket at address: 46317
```
{% include notice icon='info' content="Calling `imagej -agentlib:jdwp=help --` will print nice usage information with documentation of other JDWP options." %}

### Attach ImageJ to a waiting Eclipse

Instead of making ImageJ [the debugging server](#attaching-to-imagej-instances), when debugging startup events and headless operations it is easier to make ImageJ the client and Eclipse (or equivalent) the server.

In this case you start the debugging session first, e.g. in Eclipse debug configurations you specify "Standard (Socket Listen)" as the connection type. Then, simply start ImageJ without the `server=y` flag to connect and debug:

```shell
./fiji -agentlib:jdwp=suspend=y,transport=dt_socket,address=localhost:8000 --
```

## Monitoring system calls

### Linux

On Linux, you should call ImageJ using the [strace command](http://www.linuxmanpages.com/man1/strace.1.php):

```shell
strace -Ffo syscall.log ./fiji <args>
```

### macOS

Use the `dtruss` wrapper around [dtrace](http://developer.apple.com/documentation/Darwin/Reference/ManPages/man1/dtrace.1.html) to monitor system calls:

```shell
dtruss ./fiji <args>
```

### Windows

To monitor all kinds of aspects of processes on Windows, use [Sysinternal's Process Monitor](http://technet.microsoft.com/en-us/sysinternals/bb896645.aspx).

## Debugging shared (dynamic) library issues

### Linux

Set the `LD_DEBUG` environment variable before launching ImageJ:

```shell
LD_DEBUG=1 ./fiji <args>
```

### macOS

Set the `DYLD_PRINT_APIS` environment variable before launching ImageJ:

```shell
DYLD_PRINT_APIS=1 ./fiji <args>
```

### Windows

Often, dynamic library issues are connected to a dependent .dll file missing. Download [depends.exe](http://www.dependencywalker.com/) and load the .dll file you suspect is missing a dependency.

## Debugging JVM hangs

When the Java VM hangs, the reason might be a dead-lock. Try taking a [stack trace](/learn/troubleshooting#if-imagej-freezes-or-hangs). If you have trouble, you can try one of the following advanced techniques:

1.  You can use the `jstack` command (you don't need to run ImageJ from the command line in this case). This requires that you first find the PID (process ID) of ImageJ. You can do so by running:
    ```shell
    jps
	```

    from the command line to print a list of running Java processes. If you're not sure which PID is ImageJ's, you can close ImageJ, run `jps`, open ImageJ and run `jps` again. Whichever PID is present in the second run but not the first is ImageJ's. Then, to acquire a stack trace, just run:
    ```shell
    jstack <ImageJ's PID>
	```
2.  For GUI-based debugging, can also attach to the ImageJ PID using the `jvisualvm` program that you can find in `java/<platform>/<jdk>/bin/`. Here you can simply press a big *Thread Dump* button to view the stack trace.

Regardless of which method you use to acquire the stack trace, to debug you will want to acquire multiple stack traces over time and compare. If all the stack traces are in the same method execution, then that's the source of the deadlock (or slowdown).

## Debugging memory leaks

Sometimes, memory is not released properly, leading to `OutOfMemoryException`.

One way to find out what is happening is to use `jvisualvm` (see [\#Debugging JVM hangs](#debugging-jvm-hangs)) to connect to the ImageJ process, click on *Heap Dump* in the *Monitor* tab, in said tab select the sub-tab *Classes* and sort by size. Double-clicking on the top user should get you to a detailed list of *Instances* where you can expand the tree of references to find out what is holding a reference still.

## Debugging hard JVM crashes

When you have found an issue that crashes the JVM, and you can repeat that crash reliably, there are a number of options to find out what is going on.

### Using gdb

Typically when you debug a program that crashes, you start it in a debugger, to inspect the stack trace and the variables at the time of the crash. However, there are substantial problems with gdb when starting the Java VM; either gdb gets confused by segmentation faults (used by the JVM to handle NullPointerExceptions in an efficient manner), or it gets confused by the threading system—unless you compile gdb yourself.

But there is a very easy method to use gdb to inspect serious errors such as segmentation faults or trap signals nevertheless:

```shell
./fiji -XX:OnError="gdb - %p" --
```

### Using lldb

On newer macOS versions, gdb has been replaced with lldb. For those familiar with gdb already, there is an [LLDB to GDB Command Map](http://lldb.llvm.org/lldb-gdb.html) cheat sheet which may be useful.

### Using the `hs_err_pid<pid>.log` files

The Java virtual machine (JVM) frequently leaves files of the format `hs_err_pid<number>.log` in the current working directory after a crash. Such a file starts with a preamble similar to this:

```shell
#
# A fatal error has been detected by the Java Runtime Environment:
#
#  SIGSEGV (0xb) at pc=0x00007f3dc887dd8b, pid=12116, tid=139899447723792
#
# JRE version: 6.0_20-b02
# Java VM: Java HotSpot(TM) 64-Bit Server VM (16.3-b01 mixed mode linux-amd64 )
# Problematic frame:
# C  [libc.so.6+0x86d8b]  memcpy+0x15b
#
# If you would like to submit a bug report, please visit:
#   http://java.sun.com/webapps/bugreport/crash.jsp
# The crash happened outside the Java Virtual Machine in native code.
# See problematic frame for where to report the bug.
#
```

followed by thread dumps and other useful information including the command-line arguments passed to the JVM.

The most important part is the line after the line `# Problematic frame:` because it usually gives you an idea in which component the crash was triggered.

### Out of memory error

If the specific exception you're receiving (or you suspect) is an `OutOfMemoryError`, there are JVM flags that can be enabled when running ImageJ to help pinpoint the problem:

```shell
./fiji -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/desired/path/
```

The first option:

```shell
-XX:+HeapDumpOnOutOfMemoryError
```

tells the JVM to create a heap dump (.hprof file) if an `OutOfMemoryError` is thrown. This is basically a snapshot of the JVM state when memory ran out.

The second option:

```shell
-XX:HeapDumpPath=/desired/path/
```

is not required, but convenient for controlling where the resulting `.hprof` file is written. Note that these heap dumps are named by PID, and thus are not easily human distinguishable.

After acquiring a heap dump, you can analyze it yourself, e.g. with a [memory analyzer](http://www.eclipse.org/mat/), or post on the [Image.sc Forum](/discuss) with a brief explanation of your problem.

## Debugging Java code with jdb

### How to attach the Java debugger jdb to a running process

This requires two separate processes, ImageJ itself and the debugger. You can do this either in one shell, backgrounding the first process or in two shells, this is recommended. In the two shells do the following:

Shell 1
In the first shell, start ImageJ with special parameters to open a port (8000 in this case) to which jdb can connect afterwards:

```shell
./fiji --debugger=8000,suspend=y --
```

Shell 2
In the second shell, tell `jdb` to attach to that port:

```shell
jdb -attach 8000
```

### This is an ultra quick start to jdb, the default Java debugger

Hopefully you are a little familiar with gdb, since jdb resembles it lightly.

Notable differences:

-   a breakpoint is set with "stop in <class>.<method>" or "<class>:<line>". Just remember that the class must be fully specified, i.e. <package>.&lt;subpackages...&gt;.<classname>
-   no tab completion
-   no readline (cursor up/down)
-   no shortcuts; you have to write "run", not "r" to run the program
-   no listing files before the class was loaded
-   much easier method to specify the location of the source: "use
    <dir>

    "
-   "until" is "step", "step" is "stepi"

Okay, so here you go, a little demonstration:

(If you attach jdb to a running ImageJ process, you have to use the line from the previous section instead.)

```java
$ jdb -classpath ij.jar ij.ImageJ
> stop in ij.ImageJ.main
Deferring breakpoint ij.ImageJ.main.
It will be set after the class is loaded.
> run
run ij.ImageJ
Set uncaught java.lang.Throwable
Set deferred uncaught java.lang.Throwable
>
VM Started: Set deferred breakpoint ij.ImageJ.main

Breakpoint hit: "thread=main", ij.ImageJ.main(), line=466 bci=0

main[1] use .
main[1] list
462             //prefs.put(IJ_HEIGHT, Integer.toString(size.height));
463     }
464
465     public static void main(String args[]) {
466 =>          if (System.getProperty("java.version").substring(0,3).compareTo("1.4")<0) {
467                     javax.swing.JOptionPane.showMessageDialog(null,"ImageJ "+VERSION+" requires Java 1.4.1 or later.");
468                     System.exit(0);
469             }
470             boolean noGUI = false;
471             arguments = args;
main[1] print args[0]
java.lang.IndexOutOfBoundsException: Invalid array range: 0 to 0
 args[0] = null
main[1] print args.length
 args.length = 0
main[1] step
>
Step completed: "thread=main", ij.ImageJ.main(), line=470 bci=28
470             boolean noGUI = false;

main[1] step
>
Step completed: "thread=main", ij.ImageJ.main(), line=471 bci=30
471             arguments = args;

main[1] set noGUI = true
 noGUI = true = true
main[1] cont
>
The application exited
```

## Inspecting serialized objects

If you have a file with a serialized object, you can use this BeanShell in the [Script Editor](/scripting/script-editor) to open a tree view of the object (double-click to open/close the branches of the view):

```java
import fiji.debugging.Object_Inspector;

import ij.io.OpenDialog;

import java.io.FileInputStream;
import java.io.ObjectInputStream;

dialog = new OpenDialog("Classifier", null);
if (dialog.getDirectory() != null) {
    path = dialog.getDirectory() + "/" + dialog.getFileName();
    in = new FileInputStream(path);
    in = new ObjectInputStream(in);
    object = in.readObject();
    in.close();
    Object_Inspector.openFrame("classifier", object);
}
```

## Debugging Swing (Event Dispatch Thread) issues

Swing does not allow us to call all the methods on all UI objects from wherever we want. Some things, such as `setVisible(true)` or `pack()` need to be called on the Event Dispatch Thread (AKA EDT). See Sun's [detailed explanation](http://java.sun.com/products/jfc/tsc/articles/threads/threads1.html) as to why this is the case.

There are a couple of ways to test for such EDT violations, see [this blog post by Alexander Potochkin](http://weblogs.java.net/blog/alexfromsun/archive/2006/02/debugging_swing.html) (current versions of debug.jar can be found [here](http://java.net/projects/swinghelper/sources/svn/show/trunk/www/bin)).

## Debugging Java 3D issues

See [Troubleshooting Java 3D](/libs/java-3d#troubleshooting-java-3d).

## Interactive debugging using a shared Terminal session

For users running [Linux](/platforms/linux) and [macOS](/platforms/macos) computers (or on [Windows](/platforms/windows), [Cygwin](http://www.cygwin.com/) with an OpenSSH server), one can use an SSH tunnel for a debugging session shared between a user and a developer. All that is needed is a shared account on a public SSH server.

The user should execute this command:

```shell
ssh -R 2222:127.0.0.1:22 -t $ACCOUNT@$SSHSERVER screen
```

Once connected, the command

```shell
ssh -p 2222 $LOCALACCOUNT@127.0.0.1
```

will open a connection back to the local machine.

The developer should then execute this command:

```shell
ssh -t $ACCOUNT@$SSHSERVER 'screen -x'
```

Since this provides a shared [GNU screen](http://savannah.gnu.org/projects/screen/) session, both the user and the developer can execute commands and see the output. It is even quite common to use the terminal window as sort of a private chat room by typing out what you have to say, ending the line with a {% include key keys='Ctrl|C' %} (lest it get executed as a command).

After the debugging party is over, the user can log out securely by pressing {% include key keys='Ctrl|D' %} to log out from the local machine (since the user typed in their password in the GNU screen session herself, there is no way for the developer to log back in without the user's explicit consent). Another {% include key keys='Ctrl|D' %} will terminate the GNU screen session, and yet another {% include key keys='Ctrl|D' %} will log out from the shared account on the SSH server.
