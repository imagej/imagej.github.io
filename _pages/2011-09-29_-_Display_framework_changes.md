{{Notice | The following is a blog post from {{Person|Rueden}} originally published on the ImageJDev web site.}}

The following is a quick technical update on some work I am doing on ImageJ2's display hierarchy. It will mostly be of interest to other IJ2 developers, but I am posting here to give the community a rough idea of where we are going with the display code.

Today I investigated how to refactor the display hierarchy to eliminate the UI-specific SwingDatasetView and SwingOverlayView classes. The logic they provide needs to be preserved in the codebase somewhere, but the motivation for the change is that a "DataView" was originally conceived as a UI-agnostic bag of display settings for a Data object. For example, a view on a data object (such as a dataset) can contain per-channel LUTs. It also tracks the current position within the data object in N space, unlike the data object itself.

Refactoring these Swing-specific classes will make implementing plugins that need to output DataViews much easier, in that creating new data views will then be possible in a UI-agnostic way, without adding any potentially clunky DataView factory logic to the system. All the Swing-specific logic can be wrapped into SwingImageDisplay and related helper classes. The relevant code from SwingDatasetView and SwingOverlayView might end up in one or more SwingDataDisplayLink classes or similar—I am still working through it, but expect to have a solution implemented within the next few days.

As part of this refactoring, the Display.update() method will become the workhorse for updating displays onscreen, including any pending structural changes or rebuilds that need to occur. That is, displays must keep track of when/how their constituent data objects change, but not update themselves until update() is called. This allows users of the API to do things like add multiple data objects without triggering an automatic update with each addition.

After the above goals are met, the next steps are:

# Reevaluate how DisplayPanel and DisplayWindow fit in to the hierarchy—e.g., there is currently some inconsistency with display logic delegating to the panel and/or the window, and vice versa. We need to have a clear hierarchy and execution flow between these classes, and a clean dependency hierarchy as well with respect to them.
# Remove as much Dataset- and Overlay-specific logic from the ImageDisplay code as possible, generalizing it to the Data interface level. This work is in preparation for the addition of a CompositeData or DataList or similar that will be a tuple of multiple Data objects, allowing the construction of tree structures of data. Such a construct will let us model things like mosaics consisting of tiles, as well as clearly delineate which overlays belong to which datasets, and much more. This goal is really the essence of [http://trac.imagej.net/ticket/660 ticket 660], but the rest of the above all goes hand in hand as well.

[[Category:News]]
[[Category:ImageJ2]]
