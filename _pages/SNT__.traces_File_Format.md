[[Category:SNT]][[Category:Neuroanatomy]][[Category:Import-Export]][[Category:Data]]
{{SNTNavBar}}__NOTOC__ 
== SNT's File Format ==

The .traces files that are saved by [[SNT]] are gzipped compressed XML. SNT will also load uncompressed XML files, but by default, they are saved in the compressed form.

The XML DTD is included in the DOCTYPE of each file. The root element is always &lt;tracings&gt;, and this can contain the following elements:

* [[#.3Cimagesize.3E|&lt;imagesize&gt;]]
* [[#.3Csamplespacing.3E|&lt;samplespacing&gt;]]
* [[#.3Cpath.3E|&lt;path&gt;]]
* [[#.3Cfill.3E|&lt;fill&gt;]]
* [[#.3Cnode.3E|&lt;node&gt;]]

=== &lt;imagesize&gt; ===

There must be exactly one of these elements present, with attributes that describe the size of the image in terms of number of voxels across, up and down, e.g.:

<tt>&nbsp;&nbsp;&nbsp;&lt;imagesize width="520" height="434" depth="117"/&gt;</tt>

=== &lt;samplespacing&gt; ===

There must be exactly one of these elements present, with attributes that describe the spacing of the samples in the image (voxels) in world-coordinates, e.g.:

<tt>&nbsp;&nbsp;&nbsp;&lt;samplespacing x="0.28838738962693633" y="0.28838738962693633" z="1.2" units="micrometers"/&gt;</tt>

=== &lt;path&gt; ===

The <tt>&lt;path&gt;</tt> element can have the following attributes:

* <tt>id</tt><nowiki>: a non-negative integer ID unique among the </nowiki><tt>&lt;path&gt;</tt>s in this file
* <tt>startson</tt><nowiki>: if this is present, it gives the ID of the path which the beginning of this path branches off from. If </nowiki><tt>startson</tt> is specified, then either the deprecated attribute <tt>startsindex</tt> or the recommended attributes <tt>startsx</tt>, <tt>startsy</tt> <tt>startsz</tt> must be specified as well.
* '''[deprecated]''' <tt>startsindex</tt><nowiki>: This attribute used to indicate the 0-based index of the point in the other Path where the branch occurred. Please use </nowiki><tt>startsx</tt>, <tt>startsy</tt> and <tt>startsz</tt> instead.
* <tt>startsx</tt>, <tt>startsy</tt> and <tt>startsz</tt><nowiki>: These attributes indicate where on the path specified by </nowiki><tt>startson</tt> the branch occurs. If one of these is attributes is specified, all must be specified.
* <tt>endson</tt><nowiki>: if this is present, it gives the ID of the path which the branch ends on. If </nowiki><tt>endson</tt> is specified, then either the deprecated attribute <tt>endsindex</tt> or the recommended attributes <tt>endsx</tt>, <tt>endsy</tt> <tt>endsz</tt> must be specified as well.
* '''[deprecated]''' <tt>endsindex</tt><nowiki>: This attribute used to indicate the 0-based index of the point in the other Path where this path joins it. Please use </nowiki><tt>endsx</tt>, <tt>endsy</tt> and <tt>endsz</tt> instead.
* <tt>endsx</tt>, <tt>endsy</tt> and <tt>endsz</tt><nowiki>: These attributes indicate where on the path specified by </nowiki><tt>endson</tt> this path ends. If one of these is attributes is specified, all must be specified.
* <tt>name</tt><nowiki>: A string giving the name of this path</nowiki>
* <tt>reallength</tt><nowiki>: The length of this path found by summing the Euclidean distance between each consecutive pair of points, in the units specified in &lt;samplespacing&gt;</nowiki>
* <tt>fitted</tt><nowiki>: If present, this attribute gives the ID of another path which is a version of this path after the centre-line has been adjusted and radiuses at each point found. If this attribute is present, the </nowiki><tt>fittedversionof</tt> attribute may not be.
* <tt>fittedversionof</tt><nowiki>: If present, this attribute gives the ID of another path which was the source version for this one. Typically the path specified does not have radiusese defined for each point, although this is not always the case. If this attribute is present, the </nowiki><tt>fitted</tt> attribute may not be.
* <tt>usefitted</tt><nowiki>: This attribute must be present if either the </nowiki><tt>fitted</tt> or <tt>fittedversionof</tt> attributes are. This attribute is either <tt>"true"</tt> or <tt>"false"</tt>. It should only be "true" for paths that have a fitted version, when it implies that the user wants the fitted path to be display in favour of this (the unfitted) one. If "false" and this path has a fitted version, it means that this path should not be displayed. It should always be "false" for paths that are fitted versions of other paths. '''Note:''' this is confusing and regrettable; in later versions this will be replaced by attributes with simpler semantics.
* <tt>swctype</tt><nowiki>: This should be an integer from 0 to 7 inclusive, indicating what the SWC type of the path is. If not present, the default value is 0. The conventional meaning of these values is: </nowiki>
** 0: UNDEFINED
** 1: SOMA
** 2: AXON
** 3: DENDRITE
** 4: APICAL_DENDRITE
** 5: FORK_POINT
** 6: END_POINT
** 7: CUSTOM

The &lt;path&gt; element may contain zero or more &lt;point&gt; elements. These are described below:

=== &lt;point&gt; ===

This represents a point in a path. A point element may have the following attribes:

* <tt>xd</tt>, <tt>yd</tt>, <tt>zd</tt><nowiki>: These three attributes give the position of the point in world coordinates. e.g. you can use these coordinates directly to calculate the length of paths.</nowiki>
* '''[deprecated]''' <tt>x</tt>, <tt>y</tt>, <tt>z</tt><nowiki>: These attributes represent the position of the point in image coordinates (i.e. indices of voxels in each axis). They are still generated for backwards compatability, but it's better to use </nowiki><tt>xd</tt>, <tt>yd</tt> and <tt>zd</tt>.
* <tt>r</tt><nowiki>: If present, this attribute gives the radius of the neuron at that point.</nowiki>
* <tt>tx</tt>, <tt>ty</tt>, <tt>tz</tt><nowiki>: If present, these attributes give the tangent vector along the neuron at (</nowiki><tt>xd</tt>, <tt>yd</tt>, <tt>zd</tt>)

=== &lt;fill&gt; ===

The <tt>&lt;fill&gt;</tt> element represents a fill around a path. It contains all the points found in the search starting from points on the path, but those that actually make up the fill are just those below the threshold specified in the attributes. (This is so that the search can be restarted if the fill is reloaded.) The <tt>&lt;fill&gt;</tt> element can have the following attributes:

* <tt>id</tt><nowiki>: The ID of the fill, a non-negative integer unique among all the other fill IDs in this file.</nowiki>
* <tt>frompaths</tt><nowiki>: A comma ( optional space) separated IDs of the paths from which this fill started. e.g. if this attribute is </nowiki><tt>frompaths="2, 0"</tt> then there are nodes with distance 0 at each of the points on <tt>&lt;path id="2" ...</tt> and <tt>&lt;path id="0" ...</tt> in this fill.
* <tt>metric</tt><nowiki>: this can either be </nowiki><tt>reciprocal-intensity-scaled</tt> or <tt>256-minus-intensity-scaled</tt>. The former means that the cost of moving to a point from an adjacent one is the Euclidean distance between the two divide by the intensity value at the the latter. The former means that the cost of moving to a point from an adjacent one is the 256 minus the intensity value at the latter point all multiplied by the Euclidean distance between the two. '''Note:''' <tt>metric</tt> is a bad name for this attribute since these are not metrics in the strict sense: for example, they are not symmetric.
* <tt>threshold</tt><nowiki>: all the points with a "distance" less than this path are considered to be part of the fill.</nowiki>

=== &lt;node&gt; ===

* <tt>id</tt><nowiki>: Each node in the search has a non-negative integer ID which is unique within the enclosing fill.</nowiki>
* <tt>x</tt>, <tt>y</tt>, <tt>z</tt><nowiki>: the position of the node in the image stack in image co-ordinates, i.e. 0-based indices in voxels.</nowiki>
* <tt>previousid</tt><nowiki>: If present, this ID gives you previous node on the shortest route from the original paths to this point. It is not present for the points on the original paths, which also have a </nowiki><tt>distance</tt> attibute equal to 0.
* <tt>distance</tt><nowiki>: This is the minimum "distance" so far found for any route moving from any point on the original paths to this node. (The complete route can be reconstructed by following </nowiki><tt>previousid</tt>s.)
* <tt>status</tt><nowiki>: this attribute can either have the value </nowiki><tt>open</tt> or <tt>closed</tt>, which have their conventional meanings in A* search.
{{SNTNavBar}}
