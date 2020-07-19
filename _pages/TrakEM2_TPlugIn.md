
== TPlugIn Implementation ==
Interface ini.trakem2.plugin.TPlugIn allows for TrakEM2 plugins to be called from either the Display menu or the Project Tree menu. Suppose that we would like to add a plugin in class SomePlugIn, named "Some PlugIn". TPlugIn specifies the following methods

=== public boolean setup(Object... params) ===
Called through Plugins->Setup Some PlugIn

params contains 1 null element when nothing is selected, or the first of any selected elements when the call is made. Return true for success.

=== public Object invoke(Object... params) ===
Called through Plugins->Some PlugIn

Similar to setup. The returned Object appears not to be used.

=== public boolean applies(Object ob) ===
Determines whether the menu item for the given TPlugIn is active.

Before the right-click menu is displayed, TPlugIn.applies(Object) is called for all registered TPlugIns. Object ob is the currently selected Object, or null if there isn't one. If this method returns true, the menu item Plugins->Some PlugIn will be active. If it returns false, it will be inactive and grey.

== Registering With TrakEM2 ==
To register a TPlugIn with TrakEM2, include a file SomePlugIn.trakem2 in the jar file containing SomePlugIn, with the following format:

Display, "Some PlugIn", full.package.and.class.to.SomePlugIn

to add to the Display menu, or

Project Tree, "Some PlugIn", full.package.and.class.to.SomePlugIn

to add to the Project Tree menu. This file may contain multiple lines.

[[Category:TrakEM2]]
