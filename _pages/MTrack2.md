{{ComponentStats:sc.fiji:MTrack2_}}
This plugin is for tracking objects in 2D over time. 

Mtrack2 is based on the MultiTracker plugin by Jeffrey Kuhn which is based on the Object tracker plugin by {{Person|Rasband}}. In contrast to the Multitracker plugin, the number of objects may vary between successive frames (objects may appear or disappear). Mtrack2 will identify the objects in each frame, and then determine which objects in successive frames are closest together. If theses are within a user-defined distance (the maximum velocity of the objects) they are assembled into tracks. When multiple objeccts are within the distance determined by the maximum velocity, the closest object is selected and the object is flagged in the output.

Only tracks larger than the user-defined 'Minimum track length' are reported.

Results can be saved to file instead of being displayed in the results window (for large datasets, this can speedup the plugin considerably).

Results are displayed over no more than 225 columns, so that also the most widely used spread-sheet program can deal with the output.

The variables in the initial dialogue can be set from a macro, and the dialogue can be bypassed altogether. The following macro shows how to do this and also lists all the parameters that can be set from a macro:

<source lang="java">
call("MTrack2_.setProperty","minSize","2");
call("MTrack2_.setProperty","maxSize","20");
call("MTrack2_.setProperty","minTrackLength","3");
call("MTrack2_.setProperty","maxVelocity","4");
call("MTrack2_.setProperty","saveResultsFile","false");
call("MTrack2_.setProperty","showPaths","true");
call("MTrack2_.setProperty","showPathLengths","true");
call("MTrack2_.setProperty","showLabels","false");
call("MTrack2_.setProperty","showPositions","true");
call("MTrack2_.setProperty","skipDialogue","true");

run("MTrack2 ");
</source>

== See also ==
* http://valelab.ucsf.edu/~nico/IJplugins/MTrack2.html

[[Category:Plugins]]
[[Category:Tracking]]
