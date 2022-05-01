---
mediawiki: Developing_ImageJ_in_IntelliJ_IDEA
title: Developing ImageJ2 in IntelliJ IDEA
section: Extend:Development:Tools:IDEs
project: /software/imagej2
---

This article explains how to install and configure IntelliJ IDEA for use with [ImageJ2](/software/imagej2) development. Directions correspond to IntelliJ IDEA 11.1, and may need adjustment for other versions.

## Install and configure IDEA

-   **Install OpenJDK.** Download and install [OpenJDK](https://www.azul.com/downloads/?package=jdk). Or install it via a package manager, if possible.

-   **Install IDEA.** Download and install IDEA from the [IDEA website](http://www.jetbrains.com/idea/download/).

## Import the ImageJ2 source

1.  From the IDEA menu, choose {% include bc path='Version Control|Checkout from Version Control|Git'%}
2.  For the Git Repository URL, enter: [`git://github.com/imagej/imagej`](git://github.com/imagej/imagej2)
3.  Specify a Parent Directory, click Clone, and wait
4.  When prompted, click Yes to create an IntelliJ IDEA project from the sources

On some platforms, the first time you perform this procedure, you may be prompted to select the project JDK:

1.  Click the plus sign and choose "JSDK"
2.  Navigate to the directory containing your JDK installation

## Launch the program

1.  Choose {% include bc path='Run|Edit Configurations'%} from the menu
2.  Click the Plus icon and choose Application
3.  In the Name field, type ImageJ2
4.  Type "net.imagej.Main" for the Main class
5.  For "Use classpath and JDK of module" select "imagej2" from the list
6.  Click OK
7.  Choose {% include bc path='Run|Run ImageJ2'%} from the menu

The project automatically builds before launching, so it may take a little while the first time.

## Code style profiles

This section is a short guide on how to start using the Eclipse code style profile of ImageJ2.

### Installing Eclipse code formatter plugin

The first step is to install the Eclipse code formatter (ECF) plugin to your IntelliJ:

1.  Open {% include bc path="File | Settings" %}
2.  Select *Plugins* from the left-hand pane
3.  Click *Browse repositories...*
4.  Type *Eclipse code formatter* to the search field
5.  Select the plugin from the list and click *install* on the right-hand pane
6.  Click *Restart IntelliJ*

A tutorial on IntelliJ plugins can be found [here](https://www.jetbrains.com/help/idea/2016.2/installing-updating-and-uninstalling-repository-plugins.html).

### Plugin setup

After installing the ECF plugin you need to set it to use the Eclipse code styles file of the ImageJ project:

1.  Download [eclipse-preferences.epf](https://github.com/scijava/scijava-coding-style/blob/master/preferences.epf)
2.  Open Eclipse and follow [these](http://help.eclipse.org/luna/index.jsp?topic=%2Forg.eclipse.platform.doc.user%2Ftasks%2Ftimpandexp.htm) steps to import an `.epf` file
3.  Open {% include bc path="Window | Preferences | Java | Code Style | Formatter" %}
4.  Set *Active Profile* to *ImageJ*
5.  Click *Export All...* and save the XML file
6.  Open IntelliJ
7.  Open your project
8.  Open {% include bc path="File | Settings | Eclipse Code Formatter" %}
9.  Check the *Use the Eclipse code formatter* radio button
10. Set *Eclipse Java Formatter config file* to the XML file you just created
11. Set *Java formatter profile* to *ImageJ*
12. Check *Optimize Imports*
13. Set *Import order* to *Manual configuration* and write `com;io;java;javax;net;org;`

**NB** You can skip the first five steps if you use [this XML file](https://github.com/imagej/imagej2/blob/bcb4eddf41e90ffba6d520b83e691d3a02d65739/config/eclipse-code-clean-up-profile.xml). But note that it is old and possibly out of date.

More information on setting up the ECF plugin can be found [here](https://github.com/krasa/EclipseCodeFormatter#instructions).

## Troubleshooting

### Renaming SciJava `@Plugin` annotated classes

When renaming a classname which was annotated with SciJava's `@Plugin` annotation, an error may occur during launch of the application looking like:

    [ERROR] Exception during event handling:
        [Event] org.scijava.module.event.ModulesUpdatedEvent
        context = org.scijava.Context@1a05aced
        consumed = false
        items[0] = label='About ImageJ...', iconPath='/icons/commands/information.png', priority=0.0, enabled=true, pluginType=Command
        items[1] = label='Preferences', priority=0.0, enabled=true, pluginType=Command
        items[2] = label='Quit', iconPath='/icons/commands/door_in.png', priority=0.0, enabled=true, pluginType=Command
        [Subscriber] org.scijava.menu.DefaultMenuService [priority = 0.0]
        [Method] protected void org.scijava.menu.DefaultMenuService.onEvent(org.scijava.module.event.ModulesUpdatedEvent)
    java.lang.IllegalStateException: Can't overwrite cause with org.scijava.InstantiableException: Class not found:

    the.plugin.you.just.Renamed

The error may be related to some caching mechanism in the IDE. The solution is to clear the caches, e.g. by running `mvn clean` from the maven panel.

 
