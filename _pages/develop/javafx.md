---
mediawiki: Build_ImageJ2_Plugin_With_JavaFX
title: Build ImageJ2 Plugin With JavaFX
categories: [development]
section: Extend:Development:Tools
---

{% include wikipedia title="JavaFX" %} is Java's new graphical toolkit
that will in the long term probably
**replace {% include wikipedia title="Swing (Java)" label="Swing" %}**.

## Some things to know

-   JavaFX is only available since **Java 8**.
-   JavaFX 8 is shipped with Oracle JDK 8, but **not with OpenJDK 8**.
-   Starting with Java 11, JavaFX was open sourced as
    [OpenJFX](https://openjfx.io/), and was split out from OpenJDK as
    separate components, which can be depended upon like any other library.
-   `SceneBuilder` is a graphical interface that help creating JavaFX FXML
    files. Oracle stopped distributing `SceneBuilder` binaries. You can find
    [new binaries from the Gluon project](https://gluonhq.com/products/scene-builder/).

## Under the hood

Usually a JavaFX program needs to declare a `javafx.application.Application`.
Because only *one* `Application` instance can exist at runtime, I think under
IJ1/IJ2 interface (using Swing), if you want to use JavaFX you need to use the
`javafx.embed.swing.JFXPanel` class which make the link/bridge between a
`JFrame` and JavaFX.

-   An example of the usual `javafx.application.Application` can be found
    [here](https://github.com/hadim/imagej-plugin-javafx/blob/master/src/main/java/net/imagej/plugin/minimalJavaFXPlugin/gui/MainApp.java)

-   An example of how to use `javafx.embed.swing.JFXPanel` can be found
    [here](https://github.com/hadim/imagej-plugin-javafx/blob/master/src/main/java/net/imagej/plugin/minimalJavaFXPlugin/gui/MainAppFrame.java)

## Building ImageJ plugins with JavaFX

This section aims to give some guidelines to be able to build ImageJ plugins with JavaFX.

*Please don't hesitate to edit this page and add your tricks and/or experience about JavaFX and ImageJ.*

### A minimal ImageJ2 JavaFX plugin

There is a **minimal, incomplete ImageJ plugin** that
shows how to use JavaFX for the UI of a plugin:

{% include link-banner url="https://github.com/ctrueden/imagej-plugins-javafx %}
