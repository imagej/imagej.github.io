The following is a status update as of 2 August 2011. Yesterday we [[2011-08-01 - ImageJ v2.0.0-alpha4|released ImageJ 2.0.0-alpha4]], and we have made great progress in many areas since the last major status update in December.

=== Data and display ===

[[File:image-types.png|283px|thumb|'''ImageJ2 pixel types:''' ImageJ2 supports many more types of image data.]] ImageJ2 uses the [[ImgLib2]] library for its N-dimensional [[ImageJ Common|data model]]. As such, it natively supports many more types of images than ImageJ1, including: signed and unsigned integers of 8, 16 and 32 bits; 1-bit packed binary images (see right); 12-bit packed unsigned integers, which are increasingly common in scientific imaging; 64-bit signed integers; and floating point (i.e., real) images of 32 or 64 bits.

[[File:binary-image.png|255px|thumb|'''Binary image:''' A 1-bit image displayed in ImageJ2.]] ImageJ2 provides full support for color lookup tables (LUTs), with one LUT per image plane when available in the original data, or else one LUT per channel, similar to ImageJ1's CompositeImage. For 24-bit packed RGB data, ImageJ2 transforms it into 8-bit unsigned integer data with three channels (which requires no extra memory), then uses appropriate lookup tables to composite the image as RGB—that is, the first channel has a black-to-red LUT, the second black-to-green, and the third black-to-blue. Hence, RGB images display as expected while providing individual access to each channel. ImageJ2 does support ImageJ1's "RGB Color" images for compatibility purposes—you can flag an image as "RGB Color" and legacy plugins will see 24-bit packed RGB data. But the distinction exists only for the benefit of ImageJ1 legacy plugins.

The data and display architecture allows for multiple datasets to be added to a single display, or for the same dataset to be displayed in different ways in multiple displays. We are still finalizing this architecture, but fundamentally it works, though these capabilities are not yet exposed through the user interface. Our goal with this functionality is to enable more use cases we have seen in the scientific community, such as tile-based image registration a la [[TrakEM2]], and [[wikipedia:Multiview orthographic projection|multiview orthographic projections]] by reference (i.e., without maintaining multiple copies of the image data in memory).

We have also expanded support for ROIs and overlays. Rather than allowing only a single ROI at a time, ImageJ2 has built-in support for multiple distinct overlays, both for defining regions of interest for processing, as well as annotating images for publication and sharing. The ROI portion of the code (i.e., is this pixel "in" or "out" of my ROI?) is defined in the ImgLib2 layer, while the overlay portion (i.e., what color is my floating text?) is part of the ImageJ display layer.

=== ImageJ2 plugins ===

[[File:math-plugins.png|326px|thumb|'''Math plugins:''' ImageJ2 math plugins.]] We have reimplemented many ImageJ1 plugins within the ImageJ2 [[extensibility|extensibility framework]]. These plugins illustrate some of the features of ImageJ2, and serve as examples for how to bring legacy plugins up to date.

ImageJ2 supports several types of plugins depending on what you are trying to do. The most straightforward is the <code>ImageJPlugin</code>, which is as simple to implement as IJ1's <code>Plugin</code> interface—there is a single method, <code>run()</code>, that executes the plugin command. The difference is that the plugin's inputs and outputs are explicitly declared using instance fields annotated with <code>@Parameter</code>. This eliminates the need to write UI-centric <code>GenericDialog</code> code as was needed in IJ1, and provides automatic scripting capabilities for all such plugins.

ImageJ2 2.0.0-alpha4 introduces another more flexible type of <code>ImageJPlugin</code>: the <code>DynamicPlugin</code>. By extending this abstract class, it is possible for a plugin to dynamically add, modify and remove its inputs and outputs at runtime. This is useful for plugins that must, for example, prompt for information about each axis of the current dataset.

Another type of plugin is the <code>Display</code>, which is a more complex piece of code capable of visualizing data in some way. The core ImageJ image viewer is implemented as a <code>Display</code>.

Lastly, there are <code>PreprocessorPlugin</code>s and <code>PostprocessorPlugin</code>s that operate on an <code>ImageJPlugin</code>. Available <code>PreprocessorPlugin</code>s are applied just prior to a plugin being run, allowing them to prepare the plugin for execution. For example, one <code>PreprocessorPlugin</code> called the "input harvester" pops up a dialog box prompting the user to input values for the plugin's inputs, similar to <code>GenericDialog</code> in IJ1. Analogously, <code>PostprocessorPlugin</code>s execute just after a plugin runs, and are useful to handle the results. One <code>PostprocessorPlugin</code> called the "display postprocessor" takes care of displaying any output datasets that the plugin produced.

[[File:command-finder.png|459px|thumb|'''ImageJ2 Command Finder:''' ImageJ2's version of the Command Finder plugin, one of the most useful plugins in ImageJ1. This tool can quickly locate and run any plugin by name. We have updated it to support both IJ1 and IJ2 plugins, as well as report more information on the plugins if desired.]] All of the above types of plugins are automatically discovered at runtime. The menu bar is constructed from available <code>ImageJPlugin</code>s, the <code>Display</code>s are automatically invoked as appropriate when a dataset is created, and the preprocessor and postprocessor plugins are applied automatically as well when a plugin is executed. Changing the behavior of ImageJ is as simple as providing the desired functionality on the Java classpath. As such, ImageJ2 is capable of running in a fully headless environment.

There are also a full set of events that get generated whenever a command is executed. When a command is first invoked, a <code>ModuleStartingEvent</code> is fired; the preprocessors are called one by one, each firing a <code>ModulePreprocessEvent</code> upon completion; a <code>ModuleExecutingEvent</code> is then fired indicating the command itself is running; a <code>ModuleExecutedEvent</code> fires when the command is finished running; the postprocessors are called one by one, each firing a <code>ModulePostprocessEvent</code> upon completion; and finally a <code>ModuleFinishedEvent</code> signals the completion of the entire process.

Like in IJ1, and as you may have guessed from the terminology above, plugins are not the only type of command that can be executed. There are also scripts, IJ1 macros, and other custom code that implements the base ImageJ command interfaces: <code>Module</code> and <code>ModuleInfo</code>. Hence, not all commands are plugins (e.g., a command might be a script or custom module), and not all plugins are commands (e.g., a plugin might be a <code>Display</code>, a <code>PreprocessorPlugin</code> or a <code>PostprocessorPlugin</code>).

[[File:event-debugger.png|543px|thumb|'''Event Debugger:''' The Event Watcher plugin monitors various ImageJ events.]] To help keep track of all these details, we have created several plugins useful for debugging ImageJ2 during development. With these plugins (located in the {{bc | Plugins > Debug}} submenu), you can monitor every event published, every object being tracked including <code>Dataset</code>s and <code>Display</code>s, inspect the details of an image's data structure, and more. Of course, you can do many of these things with an IDE such as Eclipse or NetBeans, but providing these tools from the ImageJ application itself provides more ''a posteriori'' debugging capabilities to end users when problems occur.

Our eventual goal is to translate all existing core IJ1 plugins into the IJ2 framework. For now, much of the functionality present in IJ1 is accessible in IJ2 through the legacy layer (see below), but by reimplementing the plugins in "pure IJ2" we can slowly phase out the legacy layer. Doing so is important because there are problems running ImageJ1 [[headless]], and thus it is difficult to use as a library. In contrast, ImageJ2's plugin framework has been designed with headless operation in mind.

=== ImageJ2 modularity ===

We have put substantial effort into encapsulating the various parts of ImageJ2 as separate "services" that operate as independently as possible. As of this writing, the major core services are as follows:

* '''<code>EventService</code>''' - Publishes events to the [https://mvnrepository.com/artifact/org.bushe/eventbus/1.4 event bus], and allows interested parties to subscribe to them. The service provides the central means of communication between various parts of the codebase.
* '''<code>ObjectService</code>''' - Tracks available objects of various types, including <code>Dataset</code>s and <code>Display</code>s.
* '''<code>PlatformService</code>''' - Provides hooks for extending ImageJ's behavior depending on the deployment platform (operating system, version of Java, etc.)
* '''<code>ModuleService</code>''' - Tracks available modules, and provides the infrastructure for executing them.
* '''<code>PluginService</code>''' - Tracks available plugins, and provides the infrastructure for executing them (using the <code>ModuleService</code>).
* '''<code>DisplayService</code>''' - Tracks available displays, as well as the active display, and provides the means to create new displays to visualize data.
* '''<code>LegacyService</code>''' - Enables compatibility with ImageJ1, translating IJ2 data structures back and forth between IJ1 as needed to run legacy IJ1 commands.
* '''<code>ToolService</code>''' - Tracks available tools—logic binding user input to behavior—as well as the active tool (selected on the toolbar).
* '''<code>UIService</code>''' - Discovers and launches a user interface for interacting with ImageJ.
* '''<code>OverlayService</code>''' - Tracks available overlays.

An instance of the <code>ImageJ</code> class is nothing more than a collection of these services; this instance is referred to as the "application context." Whereas ImageJ1 is a singleton, with static methods to access much of its functionality, we have completed most of the groundwork needed to allow multiple simultaneous ImageJ application contexts in the same JVM.

=== ImageJ2 interoperability ===

While the core Java APIs are available on a wide variety of platforms, certain subsets of the API can be problematic in some contexts. In particular, usage of AWT can cause problems when running headless (even with <code>java.awt.headless=true</code> set). We have taken great pains to avoid all references to the AWT packages in the ImageJ2 core project. We have even gone so far as to invent our own event class hierarchy rather than reuse the events in <code>java.awt.event</code> (e.g., for mouse and keyboard events).

All use of AWT and Swing is contained outside of the <code>core</code> projects, in the <code>ui</code> projects, which implement the ImageJ2 user interfaces. Most of our development effort has gone into the Swing user interface, but we also have a prototype for pure AWT (similar to IJ1), as well as [http://pivot.apache.org/ Apache Pivot] and [http://www.eclipse.org/swt/ Eclipse SWT], with a console-driven "headless" UI planned too.

We hope that in the future, this careful separation of concerns makes it easier to interoperate with ImageJ from a variety of development environments, such as the [http://code.google.com/webtoolkit/ Google Web Toolkit] for web development, [http://developer.android.com/ Android] for mobile devices, or [http://www.ikvm.net/ IKVM.NET] for use within .NET applications. However, there are still remaining challenges—for example, ImageJ2 and ImgLib2 make liberal use of generics, which can limit code portability. Nonetheless, as long as ImageJ2 is fully usable from a headless context, we can expose it via a client/server architecture such as web services to enable its use from non-Java code.

=== Compatibility with ImageJ1 ===

The ImageJ2 legacy layer provides compatibility with ImageJ1, allowing ImageJ2 to discover and populate legacy IJ1 plugins just as IJ1 did, with legacy plugins shown in the menu structure with a small microscope icon. ImageJ2 uses a bytecode engineering library called [http://www.javassist.org/ Javassist] to intercept important IJ1 events as they occur and adjust the behavior to fit in seamlessly with IJ2. The legacy layer takes care of translating data structures back and forth between ImageJ1 (e.g., <code>ImagePlus</code> and <code>ROI</code>) and ImageJ2 (e.g., <code>Dataset</code>, <code>Overlay</code> and <code>Display</code>) as needed, by reference when possible. This technique allows IJ1 commands to be invoked on IJ2 data structures and vice versa, without the user needing to worry too much about which plugins came from where.

=== Spectral lifetime image analysis ===

[[File:slim-plugin.png|505px|thumb|'''Slim Plugin:''' Analyzing spectral lifetime data in ImageJ.]] For the past several months we have been developing an [[SLIM Curve|ImageJ plugin for visualization and analysis of combined spectral lifetime data]]. While this plugin is functional in ImageJ1, we plan to update it to an ImageJ2 plugin in time for the ImageJ2 release. The plugin will benefit from the more flexible design of ImageJ2 in several ways. First, it utilizes dimensions beyond space and time, so can take advantage of IJ2's N-dimensional data capabilities. Second, it presents several views into the same data, so will benefit from IJ2's separation of data and display. Lastly, it demonstrates IJ2's pluggable display architecture by implementing its own custom display.

=== Future directions ===

We still have more work to do on the display architecture to fully realize all the goals and ideas described above. There are also still many bugs and limitations, particularly with overlays, that we must overcome.

Once the API is largely stabilized, and the application behaves like ImageJ1 as much as possible, we will release a beta version for community feedback. We view the community as a spectrum, with one end consisting of end users who do not program and want to be able to do everything through the UI, and the other consisting of developers who wish to call ImageJ features programmatically and embed parts of it in their own applications. Many people fall somewhere in the middle, having written a few scripts or macros to automate their analysis but also making good use of the UI. With ImageJ2 we are targeting the entire spectrum across the community.

We will also improve the means by which plugins are distributed and shared. This fall, ImageJ2 will merge with the [[Fiji]] distribution of ImageJ to provide an automatic updater, including multiple update sites that each provide their own plugins. In this way, developers can start their own collections of ImageJ plugins which are easier than ever for end users to install and keep updated—no more manually downloading JAR files from various web sites and dropping them into the plugins folder (though that will still work if you prefer).

We also plan to update the ImageJ web site. In particular, we will deploy a new section of the site with a centralized plugin listing. This listing will be as seamless as possible, with all plugins from registered update sites appearing automatically, for users to comment, rate, tag and discuss, making it much easier to find ImageJ plugins, scripts and other extensions that provide functionality across many areas.

For more information on future directions, see the [http://trac.imagej.net/roadmap ImageJ roadmap].

[[Category:News]]
[[Category:ImageJ2]]
