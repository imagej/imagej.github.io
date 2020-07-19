'''JavaFX''' is the new graphical toolkit that will on the long term probably '''replace Swing'''. This page aims to give some guidelines to be able to build ImageJ2 plugin with JavaFX.

''Please don't hesitate to edit this page and add your tricks and/or experience about JavaFX and ImageJ2.''

== Some things to know == 

* JavaFX is only available since '''Java 8'''.
* JavaFX is '''not shipped''' with OpenJDK but it is with the '''Oracle JDK'''.
* JavaFX development seems to move to the OpenJFX project : http://openjdk.java.net/projects/openjfx. But it's unclear what is going on for now...
* '''SceneBuilder''' is a graphical interface that help creating JavaFX FXML files. Oracle stopped distributing SceneBuilder binaries (I don't know why). You can find new binaries from the '''Gluon project''' there : http://gluonhq.com/open-source/scene-builder

== Under the hood ==

Usually a JavaFX program needs to declare a <tt>javafx.application.Application</tt>. Because only '''one''' <tt>Application</tt> instance can exist at runtime, I think under IJ1/IJ2 interface (using Swing), if you want to use JavaFX you need to use the <tt>javafx.embed.swing.JFXPanel</tt> class which make the link/bridge between a <tt>JFrame</tt> and JavaFX.

* An example of the usual <tt>javafx.application.Application</tt> can be found here : https://github.com/hadim/imagej-plugin-javafx/blob/master/src/main/java/net/imagej/plugin/minimalJavaFXPlugin/gui/MainApp.java

* An example of how to use <tt>javafx.embed.swing.JFXPanel</tt> can be found here : https://github.com/hadim/imagej-plugin-javafx/blob/master/src/main/java/net/imagej/plugin/minimalJavaFXPlugin/gui/MainAppFrame.java

== A minimal ImageJ 2 JavaFX plugin ==

I have created a '''minimal ImageJ plugin''' that show how to use JavaFX for the UI of a plugin there : https://github.com/ctrueden/imagej-plugins-javafx (this plugin should maybe moved to the imagej GitHub organization so any IJ devs can more easly edit).
