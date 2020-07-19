We just released a new minor version of [[TrackMate]], pressed by the many bugs that were found and appeared between this version and the [[2014-03-19 - TrackMate v2.2.0 released|previous one]]. It focuses mainly on '''interoperability''' and of course '''bugfixes'''.

== Highlights ==

* It is possible to manually color spots and edges. The colors attributed are saved and retrieved from XML.

[[File:TrackMate ManualColoring.png|400px]]

To use it, select a few cells in TrackScheme and right-click to make the contextual menu appear:

[[File:TrackMate ManualColoring 2.png]]

* There is now an action to export to [http://icy.bioimageanalysis.org/ Icy] track manager. It generates a XML file that can be opened in the [http://icy.bioimageanalysis.org/plugin/Track_Manager Icy track manager].

[[File:TrackMate ExportToIcy.png]]

* Icy XML track files can be opened in TrackMate. Just point the TrackMate loader plugin to such a file, and its type will be detected and it will be opened in TrackMate. 

[[File:TrackMate ImportFromIcy.png]]

We would like to express our thanks to {{Person|Fab14}} for his help in developing these two features. 

* A new action allows merging two TrackMate files into one.

[[File:TrackMate MergeFiles.png]]

* The color scale used to display colored tracks, links and spots can now be manually adjusted. In the display panel of the GUI, double click on the label "color by" and a settings window will open allowing the user to select between manual or automatic scaling. This is great to generate views that are comparable between datasets. This feature is commissioned and offered by Fumio Hayashi, Kobe University.

[[File:TrackMate ManualColorScale.png]]

== Minor improvements ==

* The table in the InfoPane of TrackScheme displays the full spot name.

* Auto-linking mode allows the creation of links backward in time.

* Two new track feature analyzers allow filtering tracks by their spots quality or by their longest gap.


== Bugfixes ==

* Fix a potential (and potentially long standing) bug with numerical input on machine using locales different from the US locale.

* Put back the forgotten Manual Tracker.

* Save and retrieve the tracker used in the XML file.

* Fix crash triggered when the specified ROI had points out of the source image bounds.

* Fix crash when saving with a source image not loaded from disk.

* Do not crash when saving unconfigured detector or tracker.

* Many other bugfixes. 





[[Category:News]]
