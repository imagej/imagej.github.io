---
title: 2011-07-22 - Updates to the ImageJ extensibility framework
---

[ImageJ2](/software/imagej2) has a flexible "extensibility framework" for managing plugins and their cousins, modules. Lately we have been making big improvements that are too numerous to mention here. But we wanted to make note of some of the progress that we made within the past couple of days. Be warned: it is very technical and will likely only be of interest to other ImageJ2 developers.

1.  We now have a fully working way to create plugins with dynamic numbers of input and output parameters, by extending the `DynamicPlugin` class. `DynamicPluginTest` shows an example. (Feedback on the code is welcome; use {% include key keys="Ctrl|Shift|T" %} in Eclipse to Open Type and jump straight to it. To try it out in the GUI, open a couple of datasets first and then run {% include bc path='Plugins|Sandbox|Dynamic Plugin Test'%}. It will produce one output dataset per input, of the specified size squared.)
2.  There is now a `ModuleService` that tracks all known modules (plugins or otherwise). It publishes `ModulesChangedEvent` (in the case of new modules added, `ModulesAddedEvent`, and in the case of modules removed, `ModulesRemovedEvent`) whenever the list of known modules changes. This is similar to the `ObjectService`'s `ObjectsUpdatedEvent`, so we expanded that to have the same hierarchy (`Changed` at base, `Added` and `Removed` as subtypes).
3.  The `ObjectService`'s index was split out into its own class called `ObjectIndex`, which maintains the objects on every list that is part of its type hierarchy. For example, an object of type `Integer` would be registered onto the following lists: `Integer`, `Number`, `Object`, `Serializable`, `Comparable`.
4.  We implemented a subclass of `ObjectIndex` called `SortedObjectIndex` which does the same thing, but keeps all the lists sorted. Then we subclassed that as `PluginIndex`, and used it with the `PluginService`. So the plugin service now keeps an index of all its plugins including supertype hierarchies, which it didn't before. So for example, you can now ask the plugin service for all `RunnablePlugins`, and get `ImageJPlugins` (a subtype) included in that.
5.  `ModuleService` also uses a `SortedObjectIndex` subclass called `ModuleIndex` to maintain its list of modules.
6.  `ModuleService` has run methods for executing any `Module` or `ModuleInfo`, with or without spawning a new thread, and with or without a specified set of pre- and postprocessors.
7.  Similarly, `PluginService` has run methods for executing any `Module` or `ModuleInfo` with its known `PreprocessorPlugins` and `PostprocessorPlugins`. These methods are the central way to run a module programmatically.
8.  The `ShadowMenu`, a UI-agnostic menu tree structure, now has each leaf linked to a `ModuleInfo`. This means that menu entries will now be capable of running scripts and other modules, not just plugins.

What's next:

1.  Dynamic plugin implementations:
    -   We are going to update various core plugins which need the dynamic plugin mechanism, to give it a test drive.
2.  Dynamic menus:
    -   Update `ShadowMenu` to listen to `ModulesChangedEvent` and `ModuleUpdatedEvent` and change its internal structure accordingly. This will generally entail surgical changes to its structure rather than a full menu rebuild.
    -   Update the UI-toolkit-specific menu builders to keep the resultant menu structures (e.g., `JMenuBar`) linked to the `ShadowMenu`. When the `ShadowMenu` publishes events indicating menu items have changed, the actual UI menu needs to automatically update to reflect that as well.
    -   Maybe: update `ModuleService` to maintain a `ShadowMenu` data structure, which can be obtained for whatever purpose.
3.  More module invocation routines:
    -   It would be nice to have run methods of `ModuleService` and `PluginService` that accept parameters programmatically, either as a list or as a map. Grant's `InvokePluginTest` shows what we are going for.

 
