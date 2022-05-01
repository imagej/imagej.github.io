---
title: Developing ImageJ2 Plugins
section: Extend:Development:Guides
project: /software/imagej2
---

{% include notice icon="info" content='This guide provides a technical overview of [plugins](/plugins), including how to **create new plugins**.  

If you are interested in developing an **existing** plugin instead, see [Contributing to a plugin](/develop/improving-the-code).  

If you have completed a plugin that you would like to **share with the community**, see [Distributing your plugins](/contribute/distributing).

For instructions on plugin development for the original [ImageJ](/software/imagej), see [Developing Plugins for ImageJ](/develop/ij1-plugins).' %}

## Requirements

As ImageJ2 is built using the [SciJava principles of project management](/develop/project-management), this guide assumes a basic familiarity with these topics and tools, especially:

|                                                                                                              |                                                                                                                  |
|--------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| <a href="/develop/git"><img src="/media/icons/git.png" width="64px"/></a> | <a href="/develop/maven"><img src="/media/icons/maven.png" width="64px"/></a> |
| [Git](/develop/git)                                    | [Maven](/develop/maven)                                    |

Additionally, at a minimum, you should clone the {% include github org='imagej' repo='tutorials' label='imagej/tutorials repository' %}. This will give you a local copy of the tutorials discussed in this guide, as well as templates for use in your own development.

For the complete "developer experience", you can go through the [GitHub Bootcamp](https://help.github.com/categories/bootcamp/). At the least, once you've [created your own repository](https://help.github.com/articles/create-a-repo/) and cloned a local copy, you will have a home ready for when your [very own plugin](#starting-your-own-plugin) arrives!

## What is a "plugin"?

Conceptually, a **plugin** is a new piece of functionality added to ImageJ. Nearly all aspects of ImageJ are *pluggable*, meaning plugins can be provided *ad hoc* to perform specified functions. The ImageJ core needs only know what general operations are available; then when the program is running, the options for how to complete a requested operation will be determined by which plugins are available at that time.

Technically, ImageJ is built on the [SciJava Common](/libs/scijava#scijava-common) plugin framework. Within this framework, a plugin is a Java class [annotated](https://docs.oracle.com/javase/tutorial/java/annotations/index.html) with the {% include github org='scijava' repo='scijava-common' tag='scijava-common-2.47.0' source='org/scijava/plugin/Plugin.java' label='@Plugin' %} annotation. Classes annotated in this way are then automatically discovered and indexed at {% include wikipedia title='Run time (program lifecycle phase)' text='"runtime"' %}, when the application is launched by a user (as opposed to {% include wikipedia title='Compile time' text='"compile-time"' %}).

### Plugin types

There is no limit to how many plugins can be discovered at runtime. To allow efficient retrieval of plugins, each class is annotated with a specific **type** - typically a [Java interface](https://docs.oracle.com/javase/tutorial/java/concepts/interface.html) - by which the plugin will be indexed. This indexing follows Java type hierarchies.

For example, given the following plugins:

```java
@Plugin(type=Service.class)
public class MyService implements Service { }

@Plugin(type=SpecialService.class)
public class SpecialService implements Service { }
```

{% include quiz q='Which of these plugins would we expect back if asking the [Context](/develop/plugins#the-context) for plugins of type `Service` plugin?' a='It would give back both the `MyService` and `SpecialService` plugins, since `SpecialService` is a subclass of `Service`.' %}

{% include quiz q='What if we asked for plugins of type `SpecialService`?' a='It would just return the `SpecialService` plugin, since `MyService` is **not** a `SpecialService`.' %}

### Plugin priority

When plugins are retrieved from a [Context](/develop/plugins#the-context) it's possible to get more than one match. In these cases, the plugin classes are returned in order of the **priority** of the class's [@Plugin annotation](https://github.com/scijava/scijava-common/blob/scijava-common-2.47.0/src/main/java/org/scijava/plugin/Plugin.java#L108-L129). Priorities are simply double values; as a starting point, priority constants can be used from the {% include github org='scijava' repo='scijava-common' tag='scijava-common-2.47.0' source='org/scijava/Priority.java' label='Priority' %} class.

For example, given the following plugins:

```java
@Plugin(priority=Priority.HIGH)
public class MyService implements Service { }

@Plugin(priority=224)
public class SpecialService implements Service { }
```

{% include quiz q='Which plugin would be returned first if we asked the Context for a `Service` plugin?' a='The `SpecialService` plugin would come back first. If we look at the `Priority` class we see that `HIGH` simply [resolves to 100](https://github.com/scijava/scijava-common/blob/scijava-common-2.47.0/src/main/java/org/scijava/Priority.java#L54-L55).' %}

We can also use *relative priorities* when referring to particular priority constants. This is a nice way to give the best chance that sorting will remain the same even if these constants change in the future:

```java
@Plugin(priority=Priority.HIGH+124)
public class SpecialService implements Service { }
```

## What makes up the SciJava plugin framework?

### The Context

References to all the `@Plugin`-annotated classes that are discovered are contained in a single, master {% include github org='scijava' repo='scijava-common' tag='scijava-common-2.47.0' source='org/scijava/Context.java' label='Context' %}. Each application is responsible for creating its own `Context` to manage plugins and contextual state.

In ImageJ, a `Context` is automatically created when {% include github org='imagej' repo='imagej' tag='imagej-2.0.0-rc-39' source='net/imagej/ImageJ.java' label='the application starts up' %}, so plugin developers do not need to create their own. In fact, creating your own `Context` typically causes problems, as it will be a different container than ImageJ is using. Instead, plugin instances within a common `Context` are provided automatically by the framework—you just have to ask.

Typically, ImageJ plugin developers will be writing [Service](#Services) and/or [Command](#Commands) plugins. If you need to use another plugin - for example the {% include github org='scijava' repo='scijava-common' tag='scijava-common-2.47.0' source='org/scijava/log/LogService.java' label='LogService' %} - you **should not** manually create it as this effectively disconnects you from your `Context` (Your [Service](#Services) and/or [Command](#Commands) plugins are created by the application container and managed by the plugin framework automatically). Instead, you should ask your `Context` for an instance by adding a field of the desired type and annotating it with the {% include github org='scijava' repo='scijava-common' tag='scijava-common-2.47.0' source='org/scijava/plugin/Parameter.java' label='@Parameter annotation' %}. For example:

```java
@Plugin
public class MyPlugin {
 
  // This @Parameter notation is 'asking' the Context
  // for an instance of LogService.
  @Parameter
  private LogService logService;
 
  public void log(String message) {
    // Just use the LogService!
    // There is no need to construct it, since the Context
    // has already provided an appropriate instance.
    logService.info(message);
  }
}
```

This will allow the `Context` to provide you with the appropriate instance of your requested service.

In some cases, manual plugin construction is unavoidable. Understand that if the `MyPlugin` class above is manually constructed—i.e. via `new MyPlugin()`—the `LogService` parameter will be `null`. Automatic population only occurs if the plugin instance itself is retrieved via the framework. When you must manually construct a plugin instance, you can still re-connect it to an existing `Context` via its *injection* mechanism:

```java
public class MyService {

  // This service will manually create plugin instances
  // So, we need a reference to our containing Context
  // Then we can use it to inject our plugins.
  @Parameter
  private Context context;

  public void doStuff() {
    // Manually create a plugin instance
    // It is not connected to a Context yet
    MyPlugin plugin = new MyPlugin();

    // Inject the plugin instance with our Context,
    // so the logService field of the plugin will be
    // populated.
    context.inject(plugin);

    // Now that our plugin is injected, we can use
    // it with the knowledge that its parameters
    // have been populated
    plugin.log("Success!");
  }
}
```

### Services

Services provide two important functions to the SciJava framework: utility methods and persistent state. If you want to add reusable Java methods that can be used throughout the SciJava framework, then you should create a `Service` to provide this functionality. If you need to track Context-wide variables or configuration, a `Service` should be used to encapsulate that state.

Conceptually, a `Service` satisfies the role of {% include wikipedia title='Utility class' text='static utility classes'%} on a per-Context basis. In this way, only one [instance](http://math.hws.edu/javanotes/c5/s1.html) of each `Service` class can be associated with a given `Context` instance; an association that occurs automatically during `Context` creation. Furthermore, when a `Context` is asked for an implementation of a given `Service`, only the highest priority instance will be returned.

Services often build on or reuse functionality defined in each other. For example, the {% include github org='scijava' repo='scijava-common' tag='scijava-common-2.47.0' source='org/scijava/plugin/PluginService.java' label='PluginService' %} sees ubiquitous use in retrieving and working with plugin instances. For such reuse, {% include github org='scijava' repo='scijava-common' tag='scijava-common-2.47.0' source='org/scijava/plugin/Parameter.java' label='@Parameter annotation' %} can be used to declare inter-service requirements. During `Context` startup, these relationships will be resolved automatically.

### Commands

Whereas [Services](#Services) provide internal functionality, `Commands` are plugins designed to be executed as one-offs, typically interacting with users to achieve some desired outcome. When opening the ImageJ GUI, Commands are what populate your menu structure: exposing functionality and algorithms in a way that can be consumed by non-developers.

When writing `Commands` you will often declare {% include github org='scijava' repo='scijava-common' tag='scijava-common-2.47.0' source='org/scijava/plugin/Parameter.java' label='@Parameters' %} on fields that **can not** be resolved automatically by the `Context`—for example, numeric values or file paths. Instead of being instantiated at `Context` startup as a `Service` would be, `Commands` are created and executed on demand.

When a `Command` is executed, it goes through a series of pre-processing steps to populate its `@Parameters` using its associated [Context](#the-context). If any parameters are left unresolved and a UI is available, the framework will automatically build and display an appropriate dialog to get user input. In this way, input harvesting is decoupled from functional operation—allowing developers to focus on what's really important without repetition of code. This also means that Commands can typically run [headlessly](/learn/headless) without any extra development effort.

A common pattern in `Command` development is to wrap `Service` functionality. For example, opening an image from a path is a fundamental operation in ImageJ. To this end, developers can directly use the {% include github org='scifio' repo='scifio' tag='scifio-0.25.0' source='io/scif/services/DatasetIOService.java' label='DatasetIOService' %}. Users then get this same functionality from the menus via the {% include github org='imagej' repo='imagej-plugins-commands' tag='imagej-plugins-commands-0.6.0' source='net/imagej/plugins/commands/io/OpenDataset.java' label='OpenDataset command' %}—which itself simply calls into the `DatasetIOService`.

### Other plugins

Because virtually everything is a plugin in ImageJ, there are too many to explicitly enumerate, let alone cover in a tutorial. To get ideas for functionality that can be added, a good starting point is to look for services in the [javadoc](/develop/source#javadocs), or the [ImageJ search portal](http://search.imagej.net/). Many service types have supplemental plugins for easy functional extension. In particular, the {% include github org='imagej' repo='imagej-common' label='imagej-common' %} and {% include github org='scijava' repo='scijava-common' label='scijava-common' %} repositories will contain plugin definitions for many essential operations.

A brief list of some of the more useful plugin types to extend:

-   [Ops](/libs/imagej-ops) provide a reusable set of image processing algorithms.
-   [Image formats](/develop/formats) allow new types of images to be opened in ImageJ.
-   {% include github org='scijava' repo='scijava-common' tag='scijava-common-2.47.0' source='org/scijava/convert/Converter.java' label='Converters' %} allow the framework to interchange types, outside of normal Java class hierarchy restrictions.
-   {% include github org='scijava' repo='scijava-common' tag='scijava-common-2.47.0' source='org/scijava/module/process/PreprocessorPlugin.java' label='Input Preprocessors' %} give you control over the population of `@Parameters`.
-   {% include github org='scijava' repo='scijava-common' tag='scijava-common-2.47.0' source='org/scijava/display/Display.java' label='Displays' %} control how UI elements are presented to users.

If you know the function you want to modify but can't determine its location in the code, please [ask other developers.](/discuss) You're part of the community now!

## Example projects

Remember the {% include github org='imagej' repo='tutorials' label='imagej/tutorials repository' %} we [said you should clone](#Requirements)? Now's the time to put it to use!

Because the ImageJ API is designed to be maximally flexible and extensible, if you're just getting started with development it can be overwhelming to figure out exactly which part of the code base you should be working on. The `imagej/tutorials` repository contains a selection of minimal projects illustrating how your own project(s) could be structured to perform common tasks. Most of these projects also have extensive documentation via comments in the code, to highlight particular functions and use cases.

You do not need to understand every project in this repository, nor must you go through them in a particular order! Instead, you should read through the following topics and focus on the projects that look particularly interesting and relevant to your goals. Your target for learning should be to understand the code in these selected projects, and how changes to that code will be reflected in the experiences of users and other developers.

Because these tutorials use [Git](/develop/git) for source control, you have complete freedom to modify and play with the code. Worst-case scenario, you always have a big reset button via the command:

```shell
git reset --hard origin/master
```

There are always other options for saving or restoring your work—[stashing](https://git-scm.com/book/en/v1/Git-Tools-Stashing) or [branching](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell), for example—but their use will depend on your personal comfort and knowledge of Git.

### Tips

-   Most of these examples have a [Main method](https://docs.oracle.com/javase/tutorial/getStarted/application/index.html) to see the code in action.
-   All of these projects are [Mavenized](/develop/maven).
-   You can look at the [pom.xml](https://maven.apache.org/guides/introduction/introduction-to-the-pom.html) to figure out [which libraries](/develop/source) that particular project is using.
-   You can [compile and build](http://maven.apache.org/archives/maven-1.x/start/quick-start.html) from the command line by running `mvn` from any project's top-level directory (any directory containing a `pom.xml`).
-   Building a project results in a `jar` output in the `$PROJECT/target/` directory.
-   For a more "real-world" experience, you can drop the `jar` you built into the `ImageJ2.app/jars/` directory of an [ImageJ installation](/downloads) to try out any of the example plugins.
-   If you're not sure how to find your plugin within ImageJ, use the [search bar](/learn#the-search-bar)!
-   You can also import each project into [Eclipse](/develop/eclipse)/[NetBeans](/develop/netbeans)/[IntelliJ IDEA](/develop/intellij) as a [maven project](https://books.sonatype.com/m2eclipse-book/reference/creating-sect-importing-projects.html).

### First steps

The [IntroToImageJ API](https://github.com/imagej/tutorials/blob/master/java/howtos/src/main/java/howto/adv/IntroToImageJAPI.java) class documents many common functions and structures in ImageJ, and is a great starting point.

### Basic plugins

These projects provide minimal examples with thorough online documentation.

-   [example-imagej-command](https://github.com/imagej/example-imagej-command) - A minimal template for an ImageJ command plugin
-   Look at some [simple commands](https://github.com/imagej/tutorials/tree/master/java/simple-commands/src/main/java) and see how they interact with users
-   [Getting started with modules](https://github.com/imagej/tutorials/blob/master/java/working-with-modules/src/main/java/WorkingWithModules.java)—the foundation of many user-facing plugin types, including [commands](#Commands)

### Targeted tasks

These projects are examples of specific *use cases* within the ImageJ API.

-   [Execute commands programmatically](https://github.com/imagej/tutorials/master/java/execute-commands/src/main/java/ExecuteCommands.java)
-   [Open a dataset](https://github.com/imagej/tutorials/blob/master/java/howtos/src/main/java/howto/datasets/LoadAndDisplayDataset.java)
-   [Combine ROIs](https://github.com/imagej/tutorials/blob/master/java/howtos/src/main/java/howto/images/AddROIs.java)
-   [React to framework events](https://github.com/imagej/tutorials/blob/master/java/listen-to-events/src/main/java/ListenToEvents.java)—such as creating a dataset

### Working with Ops

-   [Using Ops](https://github.com/imagej/tutorials/blob/master/java/howtos/src/main/java/howto/ops/UsingOps.java)
-   [Add datasets](https://github.com/imagej/tutorials/blob/master/java/add-two-datasets/src/main/java/AddTwoDatasets.java)
-   [Create a new Op type](https://github.com/imagej/tutorials/blob/master/java/howtos/src/main/java/howto/ops/CreateANewOp.java)
-   

### Working with user input

-   [Look at all the widgets!](https://github.com/imagej/tutorials/tree/master/java/howtos/src/main/java/howto/ui)
-   [Previewable commands](https://github.com/imagej/tutorials/blob/master/java/howtos/src/main/java/howto/ui/preview/CommandWithPreview.java)

### Plugin development

-   [Create a new plugin type](https://github.com/imagej/tutorials/blob/master/java/howtos/src/main/java/howto/plugins/create/CreateANewPluginType.java)
<!-- -   [Create a new preprocessor](https://github.com/imagej/tutorials/tree/master/java/custom-preprocessor-plugin/src/main/java) -->

## Starting your own plugin

### General guidelines

ImageJ adheres to [interface-driven design](/develop/coding-style#interface-driven-design). From a practical point of view, this means:

If you are **creating** a new plugin type...

-   Use interfaces for base plugin type
-   Create an abstract class implementing this interface that handles all the boilerplate.
-   Your abstract class can likely extend a general abstract class provided in {% include github org='imagej' repo='imagej-common' label='imagej-common' %} or {% include github org='scijava' repo='scijava-common' label='scijava-common' %}

If you are **implementing** an existing plugin type...

-   Just extend the appropriate abstract class! Let your compiler tell you which methods are missing.

### Adopt an existing project

You already [created your own GitHub repository](#Requirements), right??

When you're just getting started with tools like [Git](/develop/git) and [Maven](/develop/maven), it's not easy to comprehend the nuances of how new projects should be set up and configured. It's much easier to copy a working project to use as a starting point and go from there.

The [example projects](#example-projects) are designed precisely to serve as such starting points for new projects. Once you have a solid idea of what kind of plugin you want to write, pick the project that discusses your area of choice and simply copy it to your own GitHub repo. From there, you can make changes as needed.

At this point, if you haven't already, we **STRONGLY RECOMMEND** importing your project into an [IDE](/develop/ides) like [Eclipse](/develop/eclipse). This will make [development](/develop/eclipse) and [refactoring](http://help.eclipse.org/mars/index.jsp?topic=%2Forg.eclipse.jdt.doc.user%2Freference%2Fref-menu-refactor.htm) much easier. Modern IDEs also have excellent [Git](/develop/git) and [Maven](/develop/maven) integration, which will allow you to take advantage of the fact that the example projects are already set up as Mavenized Git repositories.

In addition to modifying and developing the source code itself, there are several things you should do to properly identify and configure your project:

#### Update your POM

-   For your [parent pom](https://maven.apache.org/pom.html#inheritance), we recommend that you extend [`pom-scijava`](https://github.com/scijava/pom-scijava). This will provide [dependency management](https://maven.apache.org/pom.html#dependency-management) of a lot of common useful dependencies, including the entire [ImageJ2 software stack](/develop/architecture#definitions) and all [Fiji](/software/fiji) components. Try to use the newest available version of `pom-scijava`.
-   Update your [groupId](https://maven.apache.org/pom.html#maven-coordinates). ImageJ projects use a `net.imagej` groupId, while Fiji projects use `sc.fiji`—or you may use your own if you do not plan to distribute your plugin with the core ImageJ or Fiji projects.
-   Update your [artifactId](https://maven.apache.org/pom.html#maven-coordinates) to something appropriate based on the intended use of your project.
-   Update your <name> and <description> to something appropriate for your new artifactId.
-   Add a <developer> block to your pom, to identify yourself (see [this example](https://github.com/scijava/pom-scijava/blob/pom-scijava-16.1.0/pom.xml#L32-L47) for formatting).

#### Code changes

-   If you updated your pom's groupId, you should similarly update the [package](https://docs.oracle.com/javase/tutorial/java/package/namingpkgs.html) structure (found in [`src/main/java`](https://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html)) to match.

#### Optional changes

-   If you want to use additional [ImageJ or Fiji projects](/develop/source) as libraries, you will need to add them as dependencies in the [dependency block](https://maven.apache.org/pom.html#Dependencies) of your `pom.xml`. Note that you will not need to specify a <version>, as these are managed by the `pom-scijava` parent pom.
-   If your copied `pom.xml` has a [main method specification](https://github.com/imagej/tutorials/blob/249c699dbdb9308f8a5539f0f39cf84d2612b273/simple-commands/pom.xml#L22-L24) you will likely need to remove or update it as appropriate.
-   If you want to add non-Java files to your plugin, such as sample images or [demo scripts](/scripting), refer to the [standard maven layout](https://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html).

## Next Steps

There are further guides available dedicated to developing particular types of plugins:

-   [Adding new ops](/develop/writing-ops)
-   [Adding new file formats](/develop/formats)

Once you have completed plugins and want to get them out to users, you can familiarize yourself with the articles on:

-   [Plugin distribution](/contribute/distributing)
-   [The development lifecycle](/develop/releasing)
-   [Core contribution requirements](/contribute/fiji)

As always, if you ever need assistance, [just ask](/discuss)!

  
