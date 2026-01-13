---
title: Launcher
nav-links: true
nav-title: Launcher
---

[Jaunch](https://github.com/apposed/jaunch) is a native application for launching Java and Python programs, including [ImageJ](/software/imagej) and [Fiji](/software/fiji).

## Introduction

The launcher is a native executable whose purpose is to start up a Java Virtual Machine (and optionally Python) and run ImageJ or Fiji inside of it.

Fiji switched from the previous [ImageJ Launcher](https://github.com/imagej/imagej-launcher) to Jaunch [in February 2025](https://forum.image.sc/t/fiji-2024-year-in-review-milestones-and-roadmap/109418). Jaunch is a modern native launcher that supports both JVM and Python runtimes, with a flexible TOML-based configuration system.

## Source

The Jaunch launcher source code lives {% include github org='apposed' repo='jaunch' %}.

The legacy ImageJ launcher source code also lives {% include github org='imagej' repo='imagej-launcher' %}, but will no longer be updated.

## Purpose

The launcher provides a platform-specific entry point into the ImageJ application. A major function is to facilitate the ImageJ Updater feature by taking care of pending updates when the program is first launched.

## Usage

For an overview of supported options, run:

```
./fiji --help
```

This invocation will call the correct plaform-specific launcher executable (`linux-x64` on Linux x86-64, `macos-arm64` on macOS Apple Silicon, `windows-x64` on Windows x86-64, etc.) via the `fiji` shell script (non-Windows) or `fiji.bat` (on Windows).

### Basic Usage

The Jaunch-based launcher can do all kinds of things, like:

-   Launch Fiji with a different amount of memory: `./fiji --mem=4g`
-   Run [macros and scripts in headless mode](/learn/headless)
-   Control the [Updater](/plugins/updater) from the command line: `./fiji --update`
-   Open images: `./fiji example.jpg`
-   Call scripts: `./fiji example.py` (works for Python, Jython, JRuby `.rb`, Beanshell `.bsh`, Clojure `.clj`, and JavaScript `.js`)
-   Show the java command line instead of running ImageJ: `./fiji --dry-run`
-   Run a custom Java class' main() method: `./fiji --main-class=com.example.MyClass`
-   Pass [Java options](#java-options): `./fiji -server --` (everything before `--` is interpreted as a Java option)
-   Link Fiji into the PATH: `ln -s $(pwd)/fiji $HOME/bin/fiji && fiji`
-   Start Fiji and run a menu entry directly: `./fiji --run System_Clipboard` (the underscore is used in place of a space to avoid quoting)
-   Edit files in the Script Editor: `./fiji --edit myscript.py`

### Python Mode

Fiji's Jaunch launcher supports running in Python mode, which starts a Python interpreter with PyImageJ:

-   Launch in Python mode: `./fiji --python`
-   Set default to Python mode: Edit `config/jaunch/fiji.cfg` and set `launch-mode = 'PYTHON'`

When in Python mode, Fiji uses PyImageJ to provide seamless access to ImageJ functionality from Python.

## Download

The launcher is bundled with Fiji. There is no need to download anything additionally.

## Configuration

### Jaunch Configuration

Fiji's Jaunch launcher uses TOML configuration files located in the `config/jaunch/` directory:

-   `config/jaunch/fiji.cfg` - User configuration file (overrides defaults)
-   `config/jaunch/fiji.toml` - Main Fiji configuration (Fiji-specific launcher behavior)
-   `config/jaunch/jvm.toml` - Configuration for JVM programs
-   `config/jaunch/python.toml` - Configuration for Python programs
-   `config/jaunch/common.toml` - Foundational configuration defaults

#### Example fiji.cfg

Create or edit `config/jaunch/fiji.cfg` to customize your Fiji installation:

```toml
# Fiji user configuration

# Set maximum heap size (default: 75% of available RAM)
max-heap = '8g'

# Set default launch mode: 'JVM' or 'PYTHON'
launch-mode = 'JVM'
```

In the program GUI:
* You can edit the `max-heap` value via the {% include bc path="Edit|Options|Memory and Threads..." %} dialog.
* You can switch the `launch-mode` between JVM and Python, as well as the `python-dir`, using the {% include bc path="Edit|Options|Python..." %} dialog.

#### Available Configuration Options

- `max-heap` - Maximum JVM heap size (e.g., `'4g'`, `'75%'`, `'50%'`)
- `launch-mode` - Default runtime mode: `'JVM'` or `'PYTHON'`
- `python-dir` - Custom Python environment directory

### Legacy ImageJ.cfg (ImageJ Launcher)

For older versions of Fiji and ImageJ using the legacy ImageJ Launcher, configuration is done via `ImageJ.cfg`:

```
# ImageJ startup properties
maxheap.mb = 1024
jvmargs = -XX:+HeapDumpOnOutOfMemoryError -Xincgc
legacy.mode = false
```

Note: The first "# ImageJ startup properties" comment line is required for legacy `ImageJ.cfg` files.

## Java Options

### Passing Java Options

You can pass Java Virtual Machine options to customize runtime behavior.

When passing Java options on the command line, you can use a `--` separator to disambiguate launcher and JVM options from program arguments:

```bash
# Pass a single launcher option (no double-dash required):
./ImageJ-linux64 --mem=4g

# Pass a single Java option (with double-dash disambiguation):
./ImageJ-linux64 -Xms2g --

# Pass both launcher and Java options (with disambiguation):
./ImageJ-linux64 --mem=4g -XX:+UseG1GC --

# Pass program arguments (no disambiguation):
./ImageJ-linux64 --run script.groovy

# Pass both launcher options, Java options and program arguments (with disambiguation):
./ImageJ-linux64 --mem=4g -Xms2g -- --run script.groovy
```

{% include notice icon="note" content="Launcher options (like `--mem`, `--update`, `--python`) and JVM options (like `-Xmx`, `-XX:+UseG1GC`) both go before the `--` separator. Arguments to the program itself, such as files to open at startup, go after the `--`.

Jaunch makes a best effort to classify each argument as launcher option, JVM option, or program argument, even without the `--` being present, so in most cases you won't need it. But if Jaunch misclassifies any of your arguments, you can use it to correct the issue." %}

### Common Java Options

Here are some common memory-related options you may want to tweak:

-   `-Xms` and `-Xmx` set the minimum and maximum sizes for the heap. Use these flags like `-Xmx8g` (8 GB) or `-Xmx512m` (512 MB). Setting minimum higher can provide a minor startup performance boost since the heap doesn't need to grow gradually. Or for max heap, you can use the `--mem` option instead: `--mem=8g`.
-   `-XX:+UseG1GC` enables the G1 garbage collector, which works better for large heaps (>4GB). Fiji enables this by default unless you pass `--default-gc`.
-   `-XX:+HeapDumpOnOutOfMemoryError` creates a heap dump file when running out of memory, useful for debugging memory issues.

There are also some basic flags for logging runtime information:

-   `-verbose:gc` logs garbage collector runs and how long they're taking. I generally use this as my first tool to investigate if GC is a bottleneck for a given application.
-   `-Xprof` turns on a low-impact sampling profiler. I've had Hotspot engineers recommend I "don't use this" but I still think it's a decent (albeit very blunt) tool for finding bottlenecks. Just don't use the results as anything more than a guide.
-   `-Xrunhprof` turns on a higher-impact instrumenting profiler. The default invocation with no extra parameters records object allocations and high-allocation sites, which is useful for finding excess object creation. `-Xrunhprof:cpu=times` instruments all Java code in the JVM and records the actual CPU time calls take.

### Examples

Here are some examples are based on recommendations from [Headius's blog](http://blog.headius.com/2009/01/my-favorite-hotspot-jvm-flags.html):

#### Example 1: Set heap size and garbage collector

```bash
# Using Jaunch (Fiji 2.15.0+):
./fiji --mem=4g --gc-g1

# Or with the old ImageJ Launcher:
./ImageJ-linux64 -Xms4g -Xmx4g -XX:+UseG1GC --
```

The G1 garbage collector works well for large heaps, providing lower pause times than the default collector.

#### Example 2: Run a macro on startup

```bash
./fiji --mem=4g -- -eval "open('/path/to/project.xml');"
```

#### Example 3: Launch in Python mode with custom heap size

```bash
./fiji --python --mem=8g
```

This starts Fiji in Python mode using PyImageJ with an 8GB heap size for the JVM backend.

#### Example 4: Enable debugging agent

```bash
./fiji --debugger=8010
```

To connect the debugger, use `jdb` or your IDE's debugger at port 8010:

```bash
jdb -attach 8010
```

See examples on using jdb to [inspect the state of threads](https://albert.rierol.net/java_tricks.html#How%20to%20debug%20a%20multithreaded%20java%20program). This is useful to suspend threads, print stack traces, and check thread status (sleeping, waiting, dead-locked, etc.).

#### Example 5: Create a launch script

You can create a shell script to combine multiple options:

```bash
#!/bin/bash
/path/to/Fiji/fiji \
  --mem=8g --gc-g1 \
  --debugger=8010 \
  -- "$@"
```

The `-- "$@"` passes any script arguments through to Fiji.

### Advanced Java Options

For advanced tuning, you may want to adjust deeper JVM settings:

#### Garbage Collection Tuning

-   `-XX:+UseParallelGC` - Parallel garbage collector (good for throughput)
-   `-XX:+UseG1GC` - G1 garbage collector (good for large heaps, low pause times) - **Fiji's default**
-   `-XX:+UseZGC` - Z garbage collector (ultra-low pause times, Java 11+)
-   `-XX:NewRatio=#` - Sets ratio of "new" to "old" generations in the heap

For more details, see Oracle's [Java HotSpot Virtual Machine Garbage Collection Tuning Guide](https://docs.oracle.com/en/java/javase/21/gctuning/).

#### Memory Tuning

-   `-XX:MaxMetaspaceSize=###M` - Maximum metaspace size (replaced PermGen in Java 8+)
-   `-XX:+UseCompressedOops` - Use compressed pointers (reduces memory overhead on 64-bit JVMs)

#### Logging and Diagnostics

-   `-XX:+PrintCompilation` - Prints each method the JIT compiler compiles
-   `-Xlog:gc*` - Detailed garbage collection logging (Java 9+)
-   `-XX:+TraceClassLoading` / `-XX:+TraceClassUnloading` - Track class loading/unloading
-   `-XX:+HeapDumpOnOutOfMemoryError` - Generate heap dump on OOM errors
-   `-XX:HeapDumpPath=/path/to/dumps` - Specify location for heap dumps

#### Performance Tuning (Diagnostic Mode)

Some options require `-XX:+UnlockDiagnosticVMOptions`:

-   `-XX:+LogCompilation` - Detailed JIT compilation logging
-   `-XX:CompileThreshold=#` - Method invocations before JIT compilation
-   `-XX:MaxInlineSize=#` - Maximum method size for inlining (default: 35 bytes)

For deep performance analysis, consider using modern profiling tools like:
- [JDK Flight Recorder (JFR)](https://docs.oracle.com/en/java/javase/21/jfrcg/index.html) - Low-overhead production profiling
- [async-profiler](https://github.com/async-profiler/async-profiler) - Sampling CPU and heap profiler

## Fiji-Specific Launcher Options

Fiji's Jaunch launcher provides several options tailored to Fiji's needs:

### Memory Management

-   `--mem=<size>` - Set maximum heap size (e.g., `--mem=8g`, `--mem=75%`)
-   `--gc-g1` - Enable G1 garbage collector with optimized settings
-   `--default-gc` - Disable automatic G1 GC configuration
-   `--debug-gc` - Show detailed garbage collection information

### Runtime Selection

-   `--python` - Launch in Python mode using PyImageJ
-   `--no-python` - Force JVM-only mode (disable Python)

### Logging and Debugging

-   `--info` - Enable informational logging
-   `--debug` - Enable debug logging
-   `--dry-run` - Show launch command without executing

### User Interface

-   `--no-splash` - Suppress the splash screen
-   `--headless` - Run in [headless](/scripting/headless) mode (without using the screen at all)

### Development Options

-   `--jdb` - Launch within the Java debugger (jdb)

### Plugin and Update Management

-   `--plugins=<dir>` - Use custom plugins directory
-   `--update` - Launch the command-line Updater

### Running Commands

-   `--run <plugin> [<arg>]` - Run a specific plugin with optional arguments
-   `--edit [<file>...]` - Open files in the Script Editor
-   `--main-class=<class>` - Run a custom main class instead of Fiji

## Jaunch Architecture

Jaunch uses a two-stage architecture:

1. **Native Launcher** (C executable) - Minimal native code that discovers and loads runtime libraries
2. **Configurator** (Kotlin Native) - Handles complex configuration logic, processes TOML config files, and generates launch directives

This separation keeps the native launcher small and maintainable while providing powerful configuration capabilities through TOML files. The configurator runs as a subprocess and outputs directives that the native launcher executes.

### Configuration Files

Fiji's Jaunch configuration is organized as:

-   `config/jaunch/fiji.toml` - Main Fiji configuration (includes jvm.toml and python.toml)
-   `config/jaunch/jvm.toml` - JVM-specific settings
-   `config/jaunch/python.toml` - Python-specific settings
-   `config/jaunch/common.toml` - Base Jaunch configuration
-   `config/jaunch/fiji.cfg` - User overrides (TOML format)

For more details about Jaunch, see the [Jaunch documentation](https://github.com/apposed/jaunch).
