{{ExtendingTrackMateTutorials}}

== Introduction. ==

Developing a custom view for [[TrackMate]] is ''hard'' and painful. Of course it must be a graphical representation of the model: the tracking results with all intermediate steps. If you want to build something really useful, it has to be interactive and should allow modifying the model. And be aware that modifications might happen somewhere else. Performance is also critical: since it stands at the user interface, it must be responsive, and possibly deal with large models (millions of detections). 

Honestly, I think that one of the main good reason to extend TrackMate is that there is ready some views available.

Still, it is perfectly possible to build something useful without fulfilling all these requirements. And I still hope that someday someone will contribute a view that displays the model in the orthogonal slicer of Fiji.

This tutorial introduces the <u>view interfaces</u> of TrackMate, and since they deal with user interactions, we will also review the <u>TrackMate event system</u>. As for the [[SciJava]] discovery system, we will see how to make a TrackMate module available in TrackMate, but not visible to the user, using the <code>visible</code> parameter.



== A custom TrackMate view. ==

Like for the [[How_to_write_your_own_spot_feature_analyzer_algorithm_for_TrackMate|spot feature analyzers]], a TrackMate view is separated in two parts, that each extends a different interface:
* The  {{GitHub|org=fiji|repo=TrackMate|source=fiji/plugin/trackmate/visualization/TrackMateModelView.java|label=TrackMateModelView}}, that is the actual view of the model. All the hard work is done here.
* The {{GitHub|org=fiji|repo=TrackMate|source=fiji/plugin/trackmate/visualization/ViewFactory.java|label=ViewFactory}} that is a factory in charge of instantiating the view and of the integration in TrackMate. This interface extends the {{GitHub|org=fiji|repo=TrackMate|source=fiji/plugin/trackmate/TrackMateModule.java|label=TrackMateModule}} interface, so we expect to find there some of the methods we discussed earlier, and the [[SciJava]] annotation. 

In this tutorial, we will build something simple. We will limit ourselves to develop a view that simple messages the user every time something happens in TrackMate. For instance, when the spots are detected, how many there are; if he selects spots and edges, how many of them; etc. And we will just reuse the Fiji log window for this, which will save us from the full development of a graphical view of the model. 

But because this is a bit limited, we will not let the user pick this view as the main one, just after the detection step. A [[SciJava]] parameter will be used to make it invisible in the view selection menu. To make good use of it, we still need some way to launch this view, but this will be the subject of the next tutorial. 

Right now, we just focus on building the view. 



== The {{GitHub|org=fiji|repo=TrackMate|source=fiji/plugin/trackmate/visualization/ViewFactory.java|label=ViewFactory}}. ==

The factory itself has nothing particular. On top of the TrackMateModule methods, it just has a method to instantiate the view it controls:

<source lang="java">
@Override
public TrackMateModelView create( final Model model, final Settings settings, final SelectionModel selectionModel )
</source>

You can see that we can possibly pass 3 parameters to the constructor of the view itself: the model of course, but also the settings object, so that we can find there a link to the image object. The {{GitHub|org=fiji|repo=TrackMate|source=fiji/plugin/trackmate/visualization/hyperstack/HyperStackDisplayerFactory.java|label=HyperStackDisplayer}} uses it to retrieve the ImagePlus over which to display the TrackMate data.

The selection model is also offered, and the instance passed is the common one used in the GUI, so that a selection made by the user can be shared amongst all views.

== The {{GitHub|org=fiji|repo=TrackMate|source=fiji/plugin/trackmate/visualization/TrackMateModelView.java|label=TrackMateModelView}} interface. ==


=== Methods. ===

This is where the hard work takes place and there is a lot to say. However, the method you find in this interface are scarce and relate just to general use, and most of them are not mandatory: 

* <u><code>public void render();</code></u> This is the initialization method for your view. Your view should not show up to the user when it is instantiating, but only when this method is called. This allows TrackMate to properly manage the rendering. 

* <u><code>public void refresh();</code></u> This method should be in charge of updating the view whenever it is sensible to do so. Careful: it is '''not''' called automatically when the model has changed. You have to listen to model change yourself, and call this method manually if you want your view to be in sync. However, it '''is''' called automatically whenever the user changes a display setting (because views are not made to listen to GUI changes). But more on that below. 

* <u><code>public void clear();</code></u> This one is rather explicit. It ensures a way to clear a view in case it is not kept in sync with the model changes.

* <u><code>public void centerViewOn( final Spot spot );</code></u> This is a non-mandatory convenience tool that allow centering a view (whatever it means) on a specific Spot. It is called for instance when the user selects '''one''' spot in the GUI: all the views that implement this method move and pan to show this spot.

* The three methods related to display settings: <u><code>public Map< String, Object > getDisplaySettings();</code></u>, <u><code>public void setDisplaySettings( final String key, final Object value );</code></u>  and  <u><code>public Object getDisplaySettings( final String key );</code></u> are explained below.

* <u><code>public Model getModel();</code></u> exposes the model this view renders. 

* <u><code>public String getKey();</code></u>  Returns the unique key that identifies this view. Careful: this key <b>must</b> be the same that for the ViewFactory that can instantiates this view. This is used to save and restore the views present in a TrackMAte session.


=== Display settings. ===

It should be possible to configure the look and feel of your view, or even to set what is visible or not. This is made through display settings, and 3 methods are used to pass then around: 

* <u><code>public Map< String, Object > getDisplaySettings();</code></u>
* <u><code>public void setDisplaySettings( final String key, final Object value );</code></u>  
* <u><code>public Object getDisplaySettings( final String key );</code></u>.

Display settings are passed using a pair of key (as String) / value (as Object, that should be cast upon the right class). 

The TrackMate GUI allows the user to edit a limited series of display settings that ought to be common to all views. These are the settings you can tune on the antepenultimate panel of the GUI (spot visible or not, color by feature, etc...). If you feel like it, your view can just ignore them. Otherwise, their keys and desired classes are defined in the {{GitHub|org=fiji|repo=TrackMate|source=fiji/plugin/trackmate/visualization/TrackMateModelView.java|label=TrackMateModelView}} interface. Check the static fields there.

Everytime the user changes a setting in the GUI, the new setting value is passed with the <code>setDisplaySettings()</code> method, then the <code>refresh()</code> method is called as well. 


=== Listening to model changes. ===

You don't ''have to'' keep your view in sync with the model. You can make something useful that would just capture a snapshot of the model as it is when you launch the view and be happy about it. But, TrackMate is about allowing both automatic and manual annotation of the image data, so most likely a very useful view will echoes the changes made to the model. Ideally it would even ''enable'' these changes to be made. But this is out of the scope of this tutorial.

If you want to listen to changes made to the model, you have to register as a listener to it. This is made through
<source lang = "java">
Model.addModelChangeListener( YourViewInstance );
</source>

and then you get a new method:
<source lang="java">
public void modelChanged( final ModelChangeEvent event )
</source>

The event itself can report 5 types of changes: 
* The spots detection is done. In the GUI, this is sent just after the detection step, before the initial filtering step.
* The spots are filtered reversibly. This is sent everytime you change anything on the spot filtering panel (a new filter, a threshold value, etc..).
* The tracking step is done. That just follows the tracking step in the GUI. 
* The tracks are filtered. Like for the spots.
* The model is ''modified''. By modification, we mean an incremental, manual modification of the model. The user might have deleted a spot, or moved it in space, or changed its size, or add an edge between two spots, etc... In that case, the {{GitHub|org=fiji|repo=TrackMate|source=fiji/plugin/trackmate/ModelChangeEvent.java|label=ModelChangeEvent}} instance can be interrogated to know what was changed, deleted, added, etc...


=== Listening to selection changes. ===

The TrackMate GUI shares a common instance of {{GitHub|org=fiji|repo=TrackMate|source=fiji/plugin/trackmate/SelectionModel.java|label=SelectionModel}} that stores the selection the user made. This is convenient when exploring the tracking results. 

Your view can be kept in sync with the selection changes by implementing the {{GitHub|org=fiji|repo=TrackMate|source=fiji/plugin/trackmate/SelectionChangeListener.java|label=SelectionChangeListener}} interface. It adds a single method:
<source lang="java">
public void selectionChanged(SelectionChangeEvent event);
</source>



== A simple event logger. ==

Let's keep our custom view simple: we will just build an event logger that recycles the IJ logger window to echo what happens to the model. We then of course have to implement the two listener interfaces mentioned above. But the code stays pretty simple: check {{GitHub|org=fiji|repo=TrackMate-examples|source=plugin/trackmate/examples/view/EventLoggerView.java|label=here}} for the details.

As for the factory, nothing fancy:

<source lang="java">
package plugin.trackmate.examples.view;

import ij.ImageJ;
import ij.ImagePlus;

import javax.swing.ImageIcon;

import org.scijava.plugin.Plugin;

import fiji.plugin.trackmate.Model;
import fiji.plugin.trackmate.SelectionModel;
import fiji.plugin.trackmate.Settings;
import fiji.plugin.trackmate.TrackMatePlugIn_;
import fiji.plugin.trackmate.visualization.TrackMateModelView;
import fiji.plugin.trackmate.visualization.ViewFactory;

@Plugin( type = ViewFactory.class )
public class EventLoggerViewFactory implements ViewFactory
{

	private static final String INFO_TEXT = "<html>This factory instantiates an event logger view for TrackMate, that uses the IJ log window to just echo all the event sent by the model.</html>";

	public static final String KEY = "EVENT_LOGGER_VIEW";

	@Override
	public String getInfoText()
	{
		return INFO_TEXT;
	}

	@Override
	public ImageIcon getIcon()
	{
		return null;
	}

	@Override
	public String getKey()
	{
		return KEY;
	}

	@Override
	public String getName()
	{
		return "Event logger view";
	}

	@Override
	public TrackMateModelView create( final Model model, final Settings settings, final SelectionModel selectionModel )
	{
		return new EventLoggerView( model, selectionModel );
	}

	/*
	 * MAIN METHOD
	 */

	public static void main( final String[] args )
	{
		ImageJ.main( args );
		new ImagePlus( "../fiji/samples/FakeTracks.tif" ).show();
		new TrackMatePlugIn_().run( "" );
	}

}
</source>

[[File:TrackMate CustomView 2.png|200px|right]]

Just note that the [[SciJava]] annotation mention the <code>ViewFactory</code> class. This is enough to have the view selectable in the GUI menu:

Note that this time, TrackMate good use of the <code>getName()</code> and <code>getInfoText()</code> methods. 

And here is what you get after a few manipulations:

[[File:TrackMate CustomView 1.png|500px]]


== Controlling the visibility of your view with the SciJava <code>visible</code> parameter. ==

Our view is a good dummy examples. It is not that useful, and the info panel of the GUI could be used instead advantageously. We have nothing against it, but maybe we should not let users select it as the main view in the GUI, otherwise they might get frustrated (well, the HyperStack view is ''always'' used, whatever you choose, so we could not mind, but eh). 

There is way to do that, just by tuning the SciJava annotation:

{{ambox | text = To make a TrackMate module available in TrackMate, but not visible in the GUI menus, use the annotation parameter <code>visible = false</code> }}

So editing the header of our ViewFactory to make it look like:

<source lang="java">
@Plugin( type = ViewFactory.class, visible = false )
public class EventLoggerViewFactory implements ViewFactory
</source>

is enough to hide it in the menu. This is different from the <code>enabled</code> parameter we saw in [[How to write your own track feature analyzer algorithm for TrackMate|one the previous tutorial]]. The factory is instantiated and available in TrackMate; it just does not show up in the menu. 

But how could I make use of it then? you want to ask. Fortunately, this is just the subject of the next tutorial, on TrackMate actions. See you there.


{{Person|JeanYvesTinevez}} ([[User talk:JeanYvesTinevez|talk]]) 10:51, 17 March 2014 (CDT)

[[Category:Tutorials]]
