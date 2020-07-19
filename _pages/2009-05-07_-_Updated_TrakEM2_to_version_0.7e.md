TrakEM2 has been updated to version 0.7e

Please call "Help - Update Fiji" to get the new TrakEM2_.jar into your plugins folder.

The update includes:

*Fixed profiles 'b','n' for "Duplicate, Link and Send to [previous/next] Layer" functionality to select the new profile in the target layer, so that it can be immediately edited, its points deleted with 'x' and redrawn at ease.
*Fixed stack-index ordering of AreaList, Pipe, etc. Z-objects. So now Home/End and PgUp/PgDn keys will do the right thing with ZDisplayable objects. For very large and complex AreaList, sending the AreaList to the top will repaint it much more smoothly (faster).
*Extended AreaList fill-add ({{key|Shift}}+{{key|click}}) and fill-erase ({{key|Shift}}+{{key|Alt}}+{{key|click}}) to look for delimited areas in other AreaList, in the intersection of other AreaList, or the combined areas delimited by several AreaLists.
* Undoing no longer zooms out (oops).

Thanks to [http://www.ini.uzh.ch/people/german German Koestinger] and [http://www.ini.uzh.ch/people/ndacosta Nuno da Costa] for testing and bug reports.

[[Category:News]]
