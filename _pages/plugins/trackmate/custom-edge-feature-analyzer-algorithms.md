---
title: How to write your own edge feature analyzer algorithm for TrackMate
nav-links:
- title: Edge Feature Analyzers
  url: /plugins/trackmate/custom-edge-feature-analyzer-algorithms
- title: Track Feature Analyzers
  url: /plugins/trackmate/custom-track-feature-analyzer-algorithms
- title: Spot Feature Analyzers
  url: /plugins/trackmate/custom-spot-feature-analyzer-algorithms
- title: Viewers
  url: /plugins/trackmate/custom-viewers
- title: Actions
  url: /plugins/trackmate/custom-actions
- title: Detection Algorithms
  url: /plugins/trackmate/custom-detection-algorithms
- title: Segmentation Algorithms
  url: /plugins/trackmate/custom-segmentation-algorithms
- title: Particle-Linking Algorithms
  url: /plugins/trackmate/custom-particle-linking-algorithms
---

## Introduction

This page is a tutorial that shows how to integrate your own edge feature analyzer algorithm in TrackMate. It is the first in the series of tutorials dedicated to TrackMate extension, and should be read first by scientists willing to extend TrackMate.

All these tutorials assume you are familiar with Java development. You should be at ease with java core concepts such as object oriented design, inheritance, interfaces, etc... Ideally you would even know that maven exists and that it can help you to compile software. Beyond this, the tutorials will provide what you need to know.

Edge feature analyzers are algorithms that can associate one or more scalar numerical features to an edge, or a link between two spots in TrackMate. For instance, the instantaneous velocity is an edge feature (you need two linked spots to compute a displacement and a time interval), which happens to be provided by the algorithm named {% include github org='fiji' repo='TrackMate' branch='master' source='fiji/plugin/trackmate/features/edges/EdgeSpeedAnalyzer.java' label='EdgeSpeedAnalyzer.java' %}.

## TrackMate modules

TrackMate is extended by writing *modules*. Modules are just the basic algorithms that provide TrackMate with core functionality, that the GUI and API wrap. There are 7 classes of modules:

-   detection algorithms
-   particle-linking algorithms
-   numerical features for spots (such as mean intensity, etc..)
-   numerical features for links (such as velocity, orientation, etc..)
-   numerical features for tracks (total displacement, length, etc...)
-   visualization tools
-   post-processing actions (exporting, data massaging, etc...)

All of these modules implement an interface, specific to the module class. For instance, an edge analyzer algorithm will implement the {% include github org='fiji' repo='TrackMate' branch='master' source='fiji/plugin/trackmate/features/edges/EdgeAnalyzer.java' label='EdgeAnalyzer' %} interface. There is therefore 7 interfaces. They do have in common that they all extend the mother module interface called {% include github org='fiji' repo='TrackMate' branch='master' source='fiji/plugin/trackmate/plugins/trackmateModule.java' label='TrackMateModule' %}.

`TrackMateModule` is used for two basic purpose:

-   It itself extends the `SciJavaPlugin` interface, which will fuel the automatic discovery of new modules. We will discuss this point last.

-   It has basic methods for the GUI integration:
    1.  `getKey()` returns a unique string identifier that is used internally to reference the algorithm. For instance: `"EDGE_VELOCITY_ANALYZER"`
    2.  `getName()` returns a string suitable to be displayed in the GUI that named the algorithm. For instance `"Edge velocity"`.
    3.  `getIcon()` returns an `ImageIcon` to be displayed in the GUI.
    4.  `getInfoText()` returns a html string that briefly documents what the algorithm does. Basic html markup is accepted, so you can have something like

```html
"<html>Plot the number of spots in each frame as a function <br>of time. Only the
<u>filtered</u> spots are taken into account. </html>"
```

These are the methods used to integrate you module within the GUI. According to the class of the module, some might be plainly ignored. For instance, the edge analyzers subject of this tutorial ignore the icon and info text, since they are used silently within the GUI to provide new features.

## Basic project structure

Before we step into the edge analyzers specific, you want to setup a development environment that will ease TrackMate module development. Rather than listing the requirement, just checkout {% include github org='fiji' repo='TrackMate-examples' label='this github repository' %}, and clone it. It contains the files of this tutorial series and more importantly, is configured to depend on the latest TrackMate version, which will make it available to your code.

Compiling this project with maven will generate a jar, that you will be able to drop in the fiji plugins folder. Your modules will then be automatically detected and integrated in TrackMate.

But more on that later.

## Let's get started

But let's get back on our edge analyzer.

For this tutorial, we are going to do something simple, at least mathematically. We will write an edge analyzer that can return the angle (in radians) of a link in the XY plane. Nothing more.

So create a package for your new analyzer in our project, for instance `fiji.plugin.trackmate.examples.edgeanalyzer`.

In this package, create a class `EdgeAngleAnalyzer` and let it implement the {% include github org='fiji' repo='TrackMate' branch='master' source='fiji/plugin/trackmate/features/edges/EdgeAnalyzer.java' label='EdgeAnalyzer' %} interface. You should be getting something like this:

```java
    package plugin.trackmate.examples.edgeanalyzer;
    
    import fiji.plugin.trackmate.features.edges.EdgeAnalyzer;
    
    public class EdgeAngleAnalyzer implements EdgeAnalyzer
    {}
```

It is important to note that we provide a blank constructor. This is very important: with the way we use SciJavaPlugin integration, we cannot use the constructor to pass any object reference. If your analyzer needs some objects which are not provided through the interface methods, then you cannot code it with TrackMate directly. However we should cover most use-cases with what we have.

## Feature analyzers specific methods

Eclipse will immediately complain (I suppose you are using Eclipse; but when it comes to complaining, everything tends to be general) that your class needs to implement some abstract method. A variety of methods popup.

We see the general module methods we discussed above, plus some specific to edge analyzers. Actually, most of the new methods are generic for <i>all</i> the feature analyzers (spot, track or edge). These methods belong to the {% include github org='fiji' repo='TrackMate' branch='master' source='fiji/plugin/trackmate/features/FeatureAnalyzer.java' label='FeatureAnalyzer' %} interface, which `EdgeAnalyzer` extends, of course.

They exist because TrackMate needs to know what your feature analyzer does. Since it computes numerical features, it needs to know what features it computes, their name, their short name (when we want to show them in crowded part of the GUI) and their physical dimension. Indeed, TrackMate wants to know the dimension of the feature you generate, for it was coded in part by a conflicted physicist who does not want angles and velocities to be plotted on the same graph.

These 6 methods are:

-   `getFeatures()` returns a list of string that identifies the features the analyzer generate. There can be more than one. This list must contain strings that can be used in a XML file. Historically, we use capitalized strings, in the shape of java constants, such as `DISPLACEMENT`. We call them feature keys.

-   `getFeatureNames()` returns a map that links the feature keys to the feature names. For instance in the GUI, we want to display "Displacement" rather than "DISPLACEMENT", so that is what this map is about. It is important that the keys of this map are the keys defined in the list above.

-   `getFeatureShortNames()` returns another map with the same rules. We just use its value to display short names of features when this is needed in the GUI. There are no general advice on how to shorten your feature names; just try until it fits.

-   `getFeatureDimensions()` returns a last map, that gives a dimension to your features. Physical dimensions are listed in the {% include github org='fiji' repo='TrackMate' branch='master' source='fiji/plugin/trackmate/Dimension.java' label='Dimension enum' %}.

-   `getIsIntFeature()` is just about sugar coating. It returns a map that tells what features are integer mapped. For instance, if you have a feature that count things, such as number of neighbors, you should map this feature to `true` here. This one is actually not *really* useful; there will be no problem, no loss of precision if you do not set it right. It's just about having numbers displayed correctly. I wanted that when there were 2 neighbors, the number of neighbors displayed was "2" and not "2.0000000000001". In our case, we measure an angle, so this feature should map to `false`.

-   `isManualFeature()` returns a single flag that affects **all** the features calculated by this analyzer. Manual features are special features that were introduced in TrackMate v2.3.0. Let's leave that aside for now. Our angle feature is calculated automatically by the code we are just about to write. So this method should return `false`.

In this tutorial, our analyzer just returns one feature, which is an angle. So a concrete implementation could be:

```java
    package plugin.trackmate.examples.edgeanalyzer;
    
    import java.util.ArrayList;
    import java.util.Collection;
    import java.util.Collections;
    import java.util.HashMap;
    import java.util.List;
    import java.util.Map;
    
    import javax.swing.ImageIcon;
    
    import fiji.plugin.trackmate.Dimension;
    import fiji.plugin.trackmate.features.edges.EdgeAnalyzer;
    
    public class EdgeAngleAnalyzer implements EdgeAnalyzer
    {
    
        // The string key that identifies our analyzer.
        private static final String KEY = "Edge angle";
    
        // The only feature we compute here.
        private static final String EDGE_ANGLE = "EDGE_ANGLE";
    
        private static final List< String > FEATURES = new ArrayList< String >( 1 );
    
        private static final Map< String, Boolean > IS_INT = new HashMap< String, Boolean >( 1 );
    
        public static final Map< String, String > FEATURE_NAMES = new HashMap< String, String >( 1 );
    
        public static final Map< String, String > FEATURE_SHORT_NAMES = new HashMap< String, String >( 1 );
    
        public static final Map< String, Dimension > FEATURE_DIMENSIONS = new HashMap< String, Dimension >( 1 );
    
        // Let's set the feature list, names, short names and dimensions.
        static
        {
            FEATURES.add( EDGE_ANGLE );
            IS_INT.put( EDGE_ANGLE,  false );
            FEATURE_NAMES.put( EDGE_ANGLE, "Link angle" );
            FEATURE_SHORT_NAMES.put( EDGE_ANGLE, "Angle" );
            FEATURE_DIMENSIONS.put( EDGE_ANGLE, Dimension.ANGLE );
        }
    
        private long processingTime;
    
        /*
         * TRACKMATEMODULE METHODS
         */
    
        @Override
        public String getKey()
        {
            return KEY;
        }
    
        // Return a user-compliant name for this analyzer.
        @Override
        public String getName()
        {
            return "Edge angle";
        }
    
        // We do not use info texts for any feature actually.
        @Override
        public String getInfoText()
        {
            return "";
        }
    
        // The same: we don't use icons for features.
        @Override
        public ImageIcon getIcon()
        {
            return null;
        }
    
        @Override
        public List< String > getFeatures()
        {
            return FEATURES;
        }
    
        @Override
        public Map< String, String > getFeatureShortNames()
        {
            return FEATURE_SHORT_NAMES;
        }
    
        @Override
        public Map< String, String > getFeatureNames()
        {
            return FEATURE_NAMES;
        }
    
        @Override
        public Map< String, Dimension > getFeatureDimensions()
        {
            return FEATURE_DIMENSIONS;
        }
    
        @Override
        public Map<String, Boolean> getIsIntFeature()
        {
            return Collections.unmodifiableMap(IS_INT);
        }
    
        @Override
        public boolean isManualFeature() 
        {
            // This feature is calculated automatically.
            return false;
        }
```

## Multithreading & Benchmarking methods

There are also 4 methods which we will skip right now. They are related to the multi-threading aspect of the analyzer. You can code your analyzer to exploit a multithreaded environment, and TrackMate will configure it through the following methods:

```java
        @Override
        public void setNumThreads()
        {
            // We ignore multithreading for this tutorial.
        }
    
        @Override
        public void setNumThreads( final int numThreads )
        {
            // We ignore multithreading for this tutorial.
        }
    
        @Override
        public int getNumThreads()
        {
            // We ignore multithreading for this tutorial.
            return 1;
        }
```
       
There is also

```java
    public long getProcessingTime()
```

that returns how much milliseconds was spent on computing the features.

## The core methods

What is really important is the two methods that actually perform the work:

-   `isLocal()`
-   `process( final Collection< DefaultWeightedEdge > edges, final Model model )`

Let's see how they would look for our example angle analyzer.

### `isLocal()`

This method simply returns a boolean that states whether the features you compute are *local* ones or not. By local I mean the following: Does your feature value for an edge depends on the other edges? If no, then it is a local feature: it does not affect the other edges. If yes, then it is non local. Note that it applies to all the features provided by an analyzer.

This distinction fosters some optimization in TrackMate. You know that TrackMate does automated and manual tracking. Doing both in the same software proved challenging to code, particularly when you want to offer good performance when manually correcting very large datasets. When you do a manual modification of the data, TrackMate recomputes all the feature live, so that they are always in sync. But if you make a single punctual modification of an edge, you want to recompute features only for this edge, not for all the others if they are not affected. TrackMate can do that if the feature is local. This is why this method exists.

An example of a local edge feature would be the instantaneous velocity. The velocity of an edge only depends on this edge and not on the rest. You might say that if you modify the position of a spot, all the edges touching this spot will be affected, so it is not local. But no: all the edges touching the spot will be modified, therefore will be marked for update, but the other edges that are not modified will not have their velocity affected. So the velocity is a local feature.

An example of a non-local edge feature would be the distance of an edge to its closest neighbor. If you move an edge, its own feature value will be affected. But this will also affect the closest distance to many other edges. So it is non-local and we *a priori* have to recompute it for all edges.

In our case, we are coding an analyzer that returns the angle of a single edge, regardless of the angles of the other edges. It is therefore a local feature.

### `process( final Collection< DefaultWeightedEdge > edges, final Model model )`

The method that actually performs the work is the less elaborated. The concrete implementation is provided with `edges`, the collection of the edge whose features are to be calculated, and `model`, the TrackMate model that holds all the information you need.

There is just one thing to know: Once you computed the numerical value of your feature, you need to store it in the {% include github org='fiji' repo='TrackMate' branch='master' source='fiji/plugin/trackmate/FeatureModel.java' label='FeatureModel' %}. The feature model is a part of the main model.

It works like a 2D Map:

```java
        final FeatureModel fm = model.getFeatureModel();
        Double val = Double.valueOf(3.1451564);
        String FEATURE = "MY_AWESOME_EDGE_FEATURE";
        fm.putEdgeFeature( edge, FEATURE, val );
```

And for our XY edge angle, here are the methods content:

```java
        @Override
        public void process( final Collection< DefaultWeightedEdge > edges, final Model model )
        {
            final FeatureModel fm = model.getFeatureModel();
            for ( final DefaultWeightedEdge edge : edges )
            {
                final Spot source = model.getTrackModel().getEdgeSource( edge );
                final Spot target = model.getTrackModel().getEdgeTarget( edge );
    
                final double x1 = source.getDoublePosition( 0 );
                final double y1 = source.getDoublePosition( 1 );
                final double x2 = target.getDoublePosition( 0 );
                final double y2 = target.getDoublePosition( 1 );
    
                final double angle = Math.atan2( y2 - y1, x2 - x1 );
                fm.putEdgeFeature( edge, EDGE_ANGLE, Double.valueOf( angle ) );
            }
        }
    
        @Override
        public boolean isLocal()
        {
            return true;
        }
```

## Making the analyzer discoverable

Right now, your analyzer is functionnal. It compiles and would return expected results. Everything is fine.

Except that TrackMate doesn't even know it exists. It sits in his lonely corner and is perfectly useless.

Until TrackMate v2.2.0, there was no other way to extend TrackMate than to modify it or fork it, then recompile and redeploy it from scratch. With v2.2.0 we beneficiated from the effort of the ImageJ2 team who built a very simple and very clever discovery mechanism, that allow to simply drop a jar in the plugins folder of Fiji and have TrackMate be aware of it. On top of it all, it is plain and simple.

Just add the following line before the class declaration:

```java
    @Plugin( type = EdgeAnalyzer.class )
    public class EdgeAngleAnalyzer implements EdgeAnalyzer
    {
    ...
```

and that's it. Let me repeat:

{% include notice icon="info" content='To make a TrackMate module discoverable in TrackMate, just annotate its class with `@Plugin( type = TheTrackMateModuleClassYouAreExtending.class )`.' %}

Just the line `@Plugin( type = EdgeAnalyzer.class )` is enough. There are also mechanisms that allow fine tuning of priority, visibility (in the GUI menus), or enabling/disabling, but we will see this later.

Right now, just compile your project, and drop the resulting jar in the Fiji plugins folder. Here is what you get:

![](/media/plugins/trackmate/trackmate-develop-edge-analyzer.png)

## Wrapping up

Great, no?

You can find the full source for this example {% include github org='fiji' repo='TrackMate-examples' branch='master' source='plugin/trackmate/examples/edgeanalyzer/EdgeAngleAnalyzer.java' label='here' %}. It can also be used as a template for your analyzer.

{% include person id='tinevez' %}  January 2014 

