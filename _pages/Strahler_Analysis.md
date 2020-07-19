<seo metak="strahler,plugin,arbor,neuron,morphometry,dendrite" metad="strahler,plugin,arbor,neuron,morphometry,dendrite" />
<div style="float:right;">
{{Infobox
| software = Fiji
| name = Strahler Analysis
| maintainer = {{Person|Tiago}}
| author =  {{Person|Tiago}}
| filename = hIPNAT_.jar ([[User:Neuroanatomy|Neuroanatomy update site]])
| source = {{GitHub|org=tferr|repo=hIPNAT}}
| released = April 2016
| category = [[:Category:Plugins|Plugins]], [[:Category:Neuroanatomy|Neuroanatomy]], [[:Category:Analysis|Analysis]], [[:Category:Skeleton|Skeleton]]
}}
</div>


A plugin from the [[User:Neuroanatomy|Neuroanatomy update site]] that performs Strahler analysis on topographic skeletons (2D/3D). [[wikipedia:Strahler number|Strahler numbering]] is a numerical procedure that summarizes the branching complexity of mathematical trees.

{{ambox | text =This page describes how to perform Strahler Analysis on skeletonized images. For analysis of traced structures have a look at [[SNT]].
}}

== Description ==
<span id="StrahlerAnimation"></span>[[Image:StrahlerAnimation.gif|300px|thumb|right|Strahler Analysis by iterative elimination of end-point branches]]
The analysis occurs through progressive pruning of terminal branches, ''iterative tree simplification'', a method that requires detecting all terminal branches (i.e., branches that contain an end-point) and all the degree-one paths leading to them.

''Strahler Analysis'' takes a <u>binary</u> or <u>8-bit grayscale</u> image (2D or 3D) containing a <u>single arbor</u>, and calls [[AnalyzeSkeleton]] iteratively to retrieve [[#References|Horton-Strahler numbers]] from the [[Skeletonize3D|skeletonized centerlines]] of the input image. Each iteration includes three operations: 1) a (re)-skeletonization step to ensure that arbor remains represented by its centerlines, 2) an elimination step in which terminal-branches are pruned from the image and 3) an analysis step in which pruned branches are counted and measured. The iteration ceases as soon as all branches have been eliminated or a unresolved [[#Elimination_of_Skeleton_Loops|closed loop]] has been detected in the pruned arbor.


== Parameters ==
;Tree Classification:
:;Infer root end-points from rectangular ROI
::This option is only available when a rectangular ROI is present. It is described in [[#Non-radial arbors|Non-radial arbors]].
:;Ignore single-point arbors (Isolated pixels)
::Elimination of end-point branches may give rise to single point arbors. Such 'debris' have 1 end-point but no slab branches or junctions. When this option is selected, single-point arbors will be discarded on each iteration. If deselected, the total number of end-points may be overestimated.

;Elimination of Skeleton Loops:
:;Method
::''Strahler Analysis'' cannot process skeletons containing closed loops and will output a warning message when such structures have been detected. The available methods in this drop-down menu define how closed loops should be resolved by and are described in  the [[AnalyzeSkeleton#Loop_detection_and_pruning|AnalyzeSkeleton documentation page]].
:;Unsegmented image
::The initial non-thinned image to be used by [[AnalyzeSkeleton]] for [[AnalyzeSkeleton#Loop_detection_and_pruning|intensity-based]] elimination of closed loops. This option is only used if either ''Lowest intensity voxel'' or ''Lowest intensity branch'' is chosen as ''Method''. Note that if an intensity-based method is selected but the chosen image is a binary one, closed loops will not be resolved.

; Output Options:
:;Display Iteration stack
::If checked, an image stack that documents individual pruning cycles will be displayed. End-points and Junction-points positions are appended to the stack.
:;Show detailed information
::If checked, analysis will run in ''verbose'' mode by outputting detailed measurements and by logging debug messages.


== Root Detection ==
The problem with undiscriminated elimination of terminal branches is that a root-branch containing an end-point is always eliminated on the first iteration step. In order to protect root branches from elimination, ''Strahler Analysis'' needs to know where root branches are located. As of version 1.4.0, root-detection is implemented by means of a rectangular ROI containing the root branch and by activating the ''Infer root end-points from rectangular ROI'' option. Here is an example:


<center>
{|
| align="center" width="185" | Arbor with rectangular ROI containing root
| align="center" width="185" | Analysis ignoring ROI: Inaccurate result
| align="center" width="185" | Analysis taking ROI into account: Accurate result
|-
| align="center" colspan="3" width="555" | [[Image:Strahler_RootProtection.png|550px]]
|-
| align="left" colspan="3" width="555" |
Root branches are spared from the iterative elimination procedure if marked by a rectangular ROI. Middle image: ROI is ignored. As a consequence, root-branch is interpreted as any other terminal-branch. Right image: Analysis infers that end-point contained by ROI belongs to a root-branch and marked branch is excluded from the iteration.
|}
</center>

=== Notes on Root Detection ===
* Only a rectangular ROI can be used to mark the root branch. This is intentional: The way the root-detection algorithm works is by ''protecting'' all end-points that are contained by the ROI from end-point elimination. Using complex ROIs (e.g., discontinuous or containing internal holes) would make this task much more cumbersome.
* The ROI only needs to contain root end-point(s) and it should not matter if its boundaries intercept other branches. However, measurements on root-branches may be inaccurate if the ROI contains junction(s) points. The best way to ensure the algorithm ran as expected is to visually inspect all the slices in the ''Iteration stack''. 
* Root detection may not be required in the case of radial arbors (i.e., tree-like structures that branch out evenly in multiple directions), if root(s) remain connected in the center of the arbor (as in [[#StrahlerAnimation|animation above]]). In neurobiology, radial-ramification is an anatomical hallmark of certain cell types such as Retinal Ganglion Cells, Chandelier neurons or Drosophila Class IV sensory neurons.
* If you are batch processing multiple images you should work with .tif files: When saving as TIFF, ImageJ will store the active ROI in the image header, making it immediately available when the image is open.


== Results ==
The plugin produces three types of outputs:

;Strahler Image
:A heat-map image, in which branches are color-coded by their Horton-Strahler numbers. By default, a calibration ramp ({{bc|Analyze|Tools|Calibration Bar...}}) is added as an overlay. WYSIWYG versions (RGB images) of this ''Strahler Color Map'' image  can be obtained by pressing {{key press|Shift|F}} (shortcut for {{bc|Image|Overlay|Flatten}}).

;Strahler table
:Table listing Horton-Strahler counts. The extension and format of this ''Strahler Table'' can be specified in {{bc|Edit|Options|Input/Output...}}. It contains the following data:
:; # End-point Branches
::The number of branches for each Horton-Strahler order.

:; Ramification ratios
:: Ramification or [[wikipedia:Strahler number#Bifurcation_ratio|bifurcation ratios]] are the quotients between branches of consecutive orders. An overall ratio may be obtained by averaging ratios across orders.

;Iteration log
:If ''Show detailed information'' is checked, ''Average branch length'', ''N. of trees'', ''N. of branches'', ''N. of junctions'', ''N. of triple points'', ''N. of quadruple points'' are also retrieved for each iteration. These are described in the AnalyzeSkeleton's [[AnalyzeSkeleton#Table_of_results|documentation page]].


== Installation ==
To install ''Strahler Analysis'' you must use Java 8 and subscribe to the [[User:Neuroanatomy|Neuroanatomy update site]].


== Related Links ==
* [[AnalyzeSkeleton]] and [[Skeletonize3D]], analysis of topographic skeletons 
* [[Sholl Analysis]], bitmap morphometry based on the Sholl technique


== References ==
Original publications by [[wikipedia:Robert E. Horton|Robert E. Horton]] and [[wikipedia:Arthur Newell Strahler|Arthur N. Strahler]]:

*{{citation|first=R. E.|last=Horton|title=Erosional development of streams and their drainage basins: hydro-physical approach to quantitative morphology|journal=Geological Society of America Bulletin|volume=56|issue=3|year=1945|pages=275–370|doi=10.1130/0016-7606(1945)56[275:EDOSAT]2.0.CO;2}}.

*{{citation|last=Strahler|first=A. N.|year=1952|title=Hypsometric (area-altitude) analysis of erosional topology|journal=Geological Society of America Bulletin|volume=63|issue=11|pages=1117–1142|doi=10.1130/0016-7606(1952)63[1117:HAAOET]2.0.CO;2}}.

*{{citation|last=Strahler|first=A. N.|year=1957|title=Quantitative analysis of watershed geomorphology|journal=Transactions of the American Geophysical Union|volume=38|issue=6|pages=913–920}}  ([http://www.uvm.edu/~pdodds/files/papers/others/1957/strahler1957a.pdf PDF]).


== Citing ==
Plugins from the [[User:Neuroanatomy|Neuroanatomy update site]]:
:* Tiago Ferreira (2016)  [http://dx.doi.org/10.5281/zenodo.49399 <img src="https://zenodo.org/badge/doi/10.5281/zenodo.49399.svg" alt="10.5281/zenodo.49399">]

[[Skeletonize3D|Skeletonization]] and [[AnalyzeSkeleton|Skeleton Analysis]]:
:*Ignacio Arganda-Carreras, Rodrigo Fernandez-Gonzalez, Arrate Munoz-Barrutia, Carlos Ortiz-De-Solorzano, [http://www3.interscience.wiley.com/journal/123322233/abstract "3D reconstruction of histological sections: Application to mammary gland tissue"], Microscopy Research and Technique, Volume 73, Issue 11, pages 1019–1029, October 2010.
:* Michael Doube, Michal M. Klosowski, Ignacio Arganda-Carreras, Fabrice P. Cordelieres, Robert P. Dougherty, Jonathan S. Jackson, Benjamin Schmid, John R. Hutchinson, Sandra J. Shefelbine, [http://dx.doi.org/10.1016/j.bone.2010.08.023 BoneJ: Free and extensible bone image analysis in ImageJ], Bone, Volume 47, Issue 6, December 2010, Pages 1076-1079.

== Acknowledgments ==
To all the developers of [https://github.com/fiji/AnalyzeSkeleton/graphs/contributors AnalyzeSkeleton].


== License ==
This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the [http://www.gnu.org/licenses/gpl.txt Free Software Foundation]. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

[[Category:Skeleton]]
[[Category:Analysis]]
[[Category:Plugins]]
[[Category:Neuroanatomy]]
