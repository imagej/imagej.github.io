---
mediawiki: Logging
title: Logging
section: Extend:Development:Guides
project: /libs/scijava
---

If you are a Java developer, then it is very likely you *love* logging. At least, that's the conclusion new Java developers inevitably must draw, based on the fact that 97.3% of all Java libraries in the wild are logging frameworks. Given the jungle of logging complexity out there, it's easy to get confused about how logging works for any given project, and in fact how logging works in general across the Java software ecosystem. Fortunately, this friendly wiki page is here to help you understand logging once and for all.

## What is logging?

Logging is a technique for reporting messages and/or events during program execution. It can be useful for many purposes: debugging, informing the user of things, keeping a permanent record of what transpired, etc.

See {% include wikipedia title='Java logging framework' text='Wikipedia\'s article on Java logging frameworks'%} for further reading.

See also this nice article: [The State of Logging in Java](https://stackify.com/logging-java/) (May 2018).

## Why use a logging framework? What's wrong with `System.out.println`?

First of all, `System.out.println` is rather verbose. But more importantly, it is a bit inflexible: you cannot explicitly specify metadata such as the "severity" or "level" of the message, an associated exception stack trace, the source of the message, or other details. And you cannot customize the logging behavior based on context (e.g., log certain kinds of messages to a file, while others go to stdout).

For these reasons, nearly everyone and their dog either uses a logging framework, or invents their own. The [SciJava Common](/libs/scijava#scijava-common) project has opted to do both: the SciJava application framework provides a {% include github org='scijava' repo='scijava-common' branch='master' path='src/main/java/org/scijava/log/LogService.java' label='LogService' %} to abstract and encapsulate all logging. The default core implementation of this service is called {% include github org='scijava' repo='scijava-common' branch='master' path='src/main/java/org/scijava/log/StderrLogService.java' label='StderrLogService' %}, and simply emits all log messages to the standard error stream. This is done to avoid dependencies on any external logging frameworks or facades, as well as to offer a sufficiently rich logging API.

## What about SLF4J?

{% include aside content="To be precise, the
[Jakarta/Apache Commons Logging](https://commons.apache.org/proper/commons-logging/)
project did the whole \"facade\" thing before SLF4J did. But the community
seems to have largely standardized on SLF4J." %}

The [SLF4J](http://slf4j.org/) project is a great idea: rather than yet another logging framework, it is a facade for logging frameworks. That is: it is an interface-driven API which can be backed by any logging framework you wish, via a dedicated *binding* library. In theory, if everyone just used SLF4J, they'd simply add a compile-time dependency on org.slf4j:slf4j-api, and ship the binding of their choice at runtime so that their application would then log using, say, [Apache Log4j](http://logging.apache.org/log4j/2.x/) or [java.util logging](http://docs.oracle.com/javase/7/docs/api/java/util/logging/package-summary.html) or [Logback](http://logback.qos.ch/). Because every developer wants to decide that for themselves, right?

Unfortunately, SLF4J suffers from a couple of downsides:

-   The API is very minimal. In particular, there is no way to set the log level at runtime in a framework-agnostic way.
-   It complicates application deployment by requiring the inclusion of a logging binding [not explicitly declared in the project's dependency tree](http://slf4j.org/faq.html#maven2).
-   By inventing a new standard for logging, there is [now one more competing standard](http://xkcd.com/927/).

Still, SLF4J is a nice thing, so the SciJava project does provide a {% include github org='scijava' repo='scijava-log-slf4j' branch='master' path='src/main/java/org/scijava/log/slf4j/SLF4JLogService.java' label='LogService implementation backed by SLF4J' %}, which zealous developers can use to redirect all SciJava logging to the SLF4J framework, which they can then {% include wikipedia title='Fundamental theorem of software engineering' text='further redirect'%} using an SLF4J binding of their choosing!

## How does logging work in ImageJ2?

{% include aside content="
The six standard near-universal log levels are:

* `NONE` - Do not log any messages.
* `ERROR` - Log only execution errors.
* `WARN` - Log errors and warnings.
* `INFO` - Log informational messages.
* `DEBUG` - Log detailed debugging messages.
* `TRACE` - Log everything possible, including debugging stack traces." %}

[ImageJ2](/software/imagej2) uses the SciJava logging framework for all core logging. And the vanilla ImageJ2 distribution uses the `StderrLogService` which emits those messages to the standard error stream. The default log level is **`INFO`**.

That said, there is a problem with using the standard output and/or error streams in a GUI-driven application: such messages are not visible by default. To work around this fact, many GUI-driven applications implement their own UI component for log messages, typically a "Log window" of some sort. This solution is how the original [ImageJ](/software/imagej) addresses the logging problem on the GUI side: plugins are expected to call the static `IJ.log` and `IJ.handleException` methods to emit log messages and report exceptions to the user, respectively.

ImageJ2 runs using the [ImageJ](/software/imagej) legacy user interface by default, meaning it inherits this Log window. But in addition, it also provides a separate Console window which logs all messages to stdout and stderr, so that no potentially valuable console output is hidden from the user. The Console window automatically becomes visible whenever any output to stderr occurs. Output to stderr is shown in red, to differentiate it from output to stdout.

Therefore, as long as logging messages end up on stdout or stderr somehow (which they do by default), all is well, and the user will see them. But if you configure your own logging implementation which suppresses the stderr behavior in favor of, e.g., logging to a file somewhere, then you are on your own!

## How does logging work in Fiji?

The [Fiji](/software/fiji) distribution of ImageJ is a more complicated beast, because it ships many plugins, each of which may do its own thing with respect to logging. Rather than {% include wikipedia title='Herding cats' text='herd cats'%}, Fiji simply ships each plugin's required logging framework so that it can function unimpeded.

However, ultimately, the Fiji distribution needs to ship one, and *only* one, SLF4J binding; otherwise, SLF4J-based logging does not function properly. As of this writing, Fiji ships the [logback-classic](http://search.maven.org/#search%7Cga%7C1%7Ca%3A%22logback-classic%22) binding, meaning that SLF4J-based logging can be [configured in all the usual Logback ways](http://logback.qos.ch/manual/configuration.html). Fiji ships a default Logback configuration in the [scijava-config](https://maven.scijava.org/index.html#nexus-search;gav~org.scijava~scijava-config) library, which sends `INFO` level events to stdout, and more serious levels (`WARN`, `ERROR` and `FATAL`) to stderr. If you want to override the configuration, you will need to delete or modify that JAR file, replacing the `logback.xml` with one of your own design. The reason `logback-classic` was chosen is because the [Bio-Formats](/formats/bio-formats) project explicitly depends on it; rather than work around that, Fiji goes with the flow and converges on the same dependency.

## Controlling the logging level

If you are using the standard SciJava `LogService` implementation, you can control the logging level via the `scijava.log.level` system property.

E.g., in Java code:

```java
System.setProperty("scijava.log.level", "debug");
```
Or via the command line when running a specific class:

```java
java -Dscijava.log.level=debug ... myorg.MyMainClass
```

Or via the command line when starting ImageJ2:

```bash
ImageJ-[linux64|macosx|win32.exe|win64.exe] -Dscijava.log.level=debug
```

You can even customize the logging behavior per package/class hierarchy. For example, to switch on debug level logging for classes in the `org.scijava.plugin` package and subpackages only:

```java
System.setProperty("scijava.log.level:org.scijava.plugin", "debug");
```

If you prefer environment variables, setting the `DEBUG` environment variable will cause SciJava logging to default to **`DEBUG`** level instead of the usual **`WARN`**.

## Using the LogService from your code

The `LogService` is accessible from a SciJava plugin in the same way as any other [service](/libs/scijava#services): as a field annotated with `@Parameter`. See the [Writing plugins](/develop/plugins) guide for details.
