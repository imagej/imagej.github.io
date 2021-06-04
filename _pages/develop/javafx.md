---
title: Build ImageJ2 Plugin With JavaFX
categories: [Development]
section: Extend:Development:Tools
---

{% include wikipedia title="JavaFX" %} is Java's new graphical toolkit
that will in the long term probably
**replace {% include wikipedia title="Swing (Java)" label="Swing" %}**.

## Some things to know

-   JavaFX is only available since **Java 8**.
-   JavaFX 8 is shipped with Oracle JDK 8, but **not with OpenJDK 8** so 
-   JavaFX is not currently included with some ImageJ and Fiji distributions
    but the Azul distribution can be used. For further details see this [forum thread](https://forum.image.sc/t/feedback-needed-bundled-java-future-directions/44030/17).
-   Starting with Java 11, JavaFX was open sourced as
    [OpenJFX](https://openjfx.io/), and was split out from OpenJDK as
    separate components, which can be depended upon like any other library.
-   `SceneBuilder` is a graphical interface that help creating JavaFX FXML
    files. Oracle stopped distributing `SceneBuilder` binaries. You can find
    [new binaries from the Gluon project](https://gluonhq.com/products/scene-builder/).

## Under the hood

Usually a JavaFX program needs to declare a `javafx.application.Application` 
and only *one* `Application` instance can exist at runtime. Therefore, the 
`javafx.embed.swing.JFXPanel` class which makes the link/bridge between a
`JFrame` and JavaFX is the preferred way to build a JavaFX project within the
IJ1/IJ2 interface (using Swing).

-   An example of how to use the `javafx.embed.swing.JFXPanel` in a Fiji project can be found
    [here](https://github.com/fiji/OMEVisual/blob/master/src/main/java/sc/fiji/omevisual/gui/MainAppFrame.java)
    
The ImageJ UI is written in Swing and JavaFX will run in a different thread. This adds some additional considerations
when building JavaFX projects that will run in ImageJ. Extra care must be taken to ensure changes in the swing UI are
done on the Swing thread and changes to the JavaFX UI are done using the JavaFX thread. For example, the JXPanel is 
created on the JavaFX thread using the following Platform.runLater approach:

```java
Platform.runLater(new Runnable() {
    @Override
    public void run() {
        //launch the JFXPanel placed inside a JFrame running in ImageJ.
    }
});
```

To update Swing UI elements from the JavaFX thread the following approach is used:

```java
SwingUtilities.invokeLater(new Runnable() {
    @Override
    public void run() {
    	//Update something on the swing thread.
    }
});
```

Further explanation can be found [here](https://docs.oracle.com/javafx/2/swing/swing-fx-interoperability.htm).

## Building ImageJ plugins with JavaFX

This section aims to give some guidelines to be able to build ImageJ plugins with JavaFX.

*Please don't hesitate to edit this page and add your tricks and/or experience about JavaFX and ImageJ.*

### Examples of ImageJ2 JavaFX plugins

Here are some projects that use JavaFX in ImageJ:

-   [OMEVisual](https://github.com/fiji/OMEVisual)
-   [FilamentDetector](https://github.com/fiji/FilamentDetector)

Another example of a large JavaFX image processing application that uses several related 
libraries is [qupath](https://github.com/qupath/qupath)

And finally, there is a **minimal, incomplete ImageJ plugin** that
shows how to use JavaFX for the UI of a plugin:

{% include link-banner url="https://github.com/ctrueden/imagej-plugins-javafx" %}
