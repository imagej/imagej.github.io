{{Outdated}}

So you want to know how ImageJ determines what plugins are available, and how to call them?  If so, you came to the right place.

== What are ImageJ plugins? ==

ImageJ plugins are classes implementing the ''ij.plugin.PlugIn'' or ''ij.plugin.filter.PlugInFilter'' interface.  The latter will only work when it has an input image, and it has a ''setup()'' method that returns information about which types of images the plugin can handle.

If a plugin class implements both the ''PlugIn'' and the ''PlugInFilter'' interface, the ''PlugIn'' interface will be preferred.

== How does ImageJ find the plugins? ==

Plugins must be stored as either ''.class'' or ''.jar'' files in the ''plugins/'' directory in ImageJ's root directory.

The contract is that the name of the file contains an underscore.  If the file is a ''.jar'' file, its contents are searched for ''.class'' files whose names have underscores in them.  The underscores will be replaced by spaces and the resulting names (without the ''.class'' extension) will be added to the ''Plugins'' menu.

The ''.class'' file discovery in ''.jar'' files is <u>not</u> performed if the ''.jar'' file contains a file called ''plugins.config''.  If that file exists, it is parsed to obtain the labels of the menu items and the corresponding Java classes instead.  A ''plugins.config'' file looks like this:

 # This is a comment (empty lines are also ignored)
 
 # This line will add "Blob" to the "New" submenu of the "File" menu.
 # Clicking on "Blob" will call the plugin class "my.test.Test"
 File>New, "Blob", my.test.Test

''Technical note:'' the plugins are loaded via an instance of ''ij.io.PluginClassLoader'', which is available by calling ''ij.IJ.getClassLoader()''.

''Fiji note:'' while the plugins' ''.jar'' files are stored in the ''plugins/'' directory, the third-party libraries are not.  They are stored in the ''jars/'' directory, so that e.g. the file ''jai_codec.jar'' (which also contains classes with underscores in their names) is not mistaken for a plugin ''.jar''. Plugins share all third party-libraries located in the ''jars'' directory. Every plugin has all third-party libraries in its classpath.

== Can plugins be reloaded? ==

Yes.  By clicking on ''Update Menus'' in the ''Help'' menu, ImageJ's plugin class loader is replaced with a new instance.  Plugins which are already running are not reloaded, though.

''Technical note:'' for class reloading to work, it is necessary that the ''plugins/'' directory is <u>not</u> in the classpath, lest the system class loader take care of the classes (in which case they cannot be unloaded, and therefore not be reloaded, either).

''Fiji note:'' as third-party libraries cannot be in the ''plugins/'' directory, they must be in the class path (otherwise, the PluginClassLoader will not be able to resolve those classes).

''Another Fiji note:'' for scripting languages to work, the interpreters' class loaders have to be replaced or augmented by ImageJ's plugin class loader.

== How can a plugin specify input/output parameters? ==

A plugin typically instantiates ''ij.gui.GenericDialog'' in its ''run()'' method.  This class serves three purposes:

* it shows a dialog with the given parameters of the given types,

* if there is a running macro recorder, and the dialog was not canceled, the key/values are recorded (using the labels of the dialog as keys), and

* if the dialog is "shown" in the context of a macro, the values are retrieved by the same keys from the parameters specified in the macro.

''Technical note:'' if a plugin uses the recommended GenericDialog way to ask for parameters, there is currently no other way to find out what parameters the plugin offers than to run the method and look what the dialog offers. In other words, this method is only useful when ImageJ is used as a desktop application, not when you want to use it as a library.

''Another technical note:'' as a GenericDialog extends an AWT class, it cannot be instantiated in a headless mode on Linux.  The reason is that text dimensions (and therefore the dimensions of the dialog itself) can only be inferred using functionality of X11's font manager.  So you cannot run parameterized macros in ImageJ on Linux without a graphical user interface.

''Fiji note:'' we have a workaround, where we have ''alternative'' implementations of some classes, which no longer extend AWT classes.  These implementations live in ''misc/headless.jar'', and are prepended to the class path when Fiji was called in headless mode, so that those implementations are found before ImageJ's.  The downside is that plugins relying on the AWT classes being base classes will stop working, but at least some plugins run that way even without a graphical user interface.

[[Category:Development]]
