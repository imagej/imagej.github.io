Just in time for the new year, we are proud to announce a new release of [[ImageJ2]] version 2.0.0-rc-64.

The most significant improvement is a new search bar integrated with the main ImageJ window:

[[File:Search-bar.png|600px]]

In this initial incarnation, the search bar finds commands, and can search the ImageJ wiki as well as the [http://forum.imagej.net/ ImageJ Forum] if you check those respective checkboxes.

For power users and developers, the search bar supports execution of "code snippets"—single lines of code for performing tasks—by starting the query with <code>!</code>. Any code that works in the [[Script Interpreter]] should be usable as a code snippet.

Developers can extend the capabilities of the search bar by writing [https://github.com/scijava/scijava-search/blob/scijava-search-0.3.1/src/main/java/org/scijava/search/Searcher.java#L36-L46 Searcher] plugins. Future plans include results for "Recent Files" as well as ImageJ Ops. If you have ideas for additional search capabilities, please share them on the [http://forum.imagej.net/ ImageJ Forum]!

ImageJ 2.0.0-rc-64 has many other updates as well, including an updated Console/Log window, as well as an updated macOS launcher compatible with Java 9.

[[Category:ImageJ2]]
[[Category:Fiji]]
[[Category:News]]
