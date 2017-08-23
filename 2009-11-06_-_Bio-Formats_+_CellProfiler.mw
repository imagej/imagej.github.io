{{Notice | The following is a blog post from {{Person|Leek}} originally published on the ImageJDev web site.}}

Hi all,

As long as this is here, I'll go ahead and describe what I've done as a first post. The code is available via [https://svn.broadinstitute.org/CellProfiler/trunk/CellProfiler/pyCellProfiler our SVN repository].

I've broken the Java/Python interface into 3 pieces:

* Low-level wrapping of the JNI (cellprofiler.utilities.javabridge): this layer is pretty close to a 1-to-1 mapping between method calls on the JNI environment and JVM instance and Python method calls. It's written in Cython which lets you reference C structures within a Python-like language. At present, I have about 60% coverage of the JNI methods; you can instantiate classes and objects, call methods on objects and on classes, get static field values and convert object and byte arrays from Java to Python. Everything operates in a single-threaded environment at present; I will probably put in the hooks needed to run multi-threaded within the next month.
* Utility routines for the JNI (cellprofiler.utilities.jutil): this module has functions for calling methods on classes and objects with exception handling and has utilities that let a programmer construct a Python wrapper for a Java object. You get to bind the object's methods to a Python class and then call into the object as if it were Python. There are wrappers for java.lang.Class, java.util.Dictionary and java.util.Enumeration.
* [[Bio-Formats]] wrapper (bioformats.formatreader): this module has wrappers for some of the Bio-Formats classes. It's pretty easy to create both ImageReaders and FormatReaders (for instance ChannelSeparator).

We can build on both the PC and the Mac and are pretty close to having something that builds for any processor on Linux. CellProfiler is currently using Bio-Formats to read all images.

As a programmer, you get a feel for the stability of a piece of technology and it's trustworthyness. It's easy to make a bad choice that mostly works at the outset, but turns out to have so many problems that it becomes impossible to support. JNI and Bio-Formats under JNI feel very stable. Both run crisply and predictably, are straightforward to use and work exactly as described, as far as I can tell. I could make tools that use Java reflection to automatically wrap Java objects in Python. The approach that I've taken works well for the context in which I use it, though. I need a small number of classes, so it makes sense right now to hand-craft each wrapper and test that it works; it's all a small amount of code that operates simply and predictably.

We've set aside some time, hopefully in December to try to use Bio-Formats to write files; I'll let people know when we've made progress.

--Lee

[[Category:News]]
[[Category:ImageJ2]]
