{{Project|SNT}}{{Infobox
| software   = Fiji
| name       = Neuroanatomy update site
| author     = {{Person|Tiago}}
| maintainer = {{Person|Tiago}}
| source     = {{GitHub|org=morphonets|}}
| status     = Active
| category   = [[:Category:Plugins|Plugins]], [[:Category:Analysis|Analysis]], [[:Category:Neuroanatomy|Neuroanatomy]]
}}
The Neuroanatomy update site is used for distribution of [[SNT]]. A few other (legacy) plugins for ''Image Processing for NeuroAnatomy and Tree-like Structures'' are also included. For a list of all pages in this wiki related to Neuroanatomy have a look at [[:Category:Neuroanatomy]].

= Installation =
The requirements to run the Neuroanatomy suite of plugins are twofold: i) [[Fiji]] (i.e., an ImageJ installation subscribed to the Fiji update site) running at least Java 8. If you are running an older version of Java, you can either i) [[Fiji/Downloads|Download the latest Fiji release]] (newer releases come pre-bundled with Java 8); or ii) If you have downloaded Fiji while ago and want to keep your existing installation, you will have to download Java 8 and make your [[Troubleshooting#Checking_the_Java_version|Fiji installation aware of it]].

'''Subscribing to the Neuroanatomy update site:'''
# Run [[Update_Sites|{{bc|Help|Update...}}]]
# Click ''Manage update sites''
# Select the ''Neuroanatomy'' checkbox (see also {{ListOfUpdateSites}})
# Click ''Apply changes'' and Restart ImageJ

== Notes ==
SNT has its own [[sNT|documentation]]. The list of ''Image Processing for NeuroAnatomy and Tree-like Structures'' ({{GitHub|org=tferr|repo=hIPNAT|label=source}}) is as follows:
{| class="wikitable"
|style="width:10%;vertical-align: middle;text-align:center;"|'''Name'''
|style="width:20%;vertical-align: middle;text-align:center;"|'''Menu Path'''
|style="width:70%;vertical-align: middle;text-align:center;"|'''Description'''
|-
|colspan="3" style="background: #ddd; border-top: 1px solid gray; padding: 5px; text-align: center"|''Topological Skeletons''
|- valign="top"
|Strahler classifier
|{{bc|Analyze|Skeleton|Strahler Analysis...}}
|Described in [[Strahler Analysis]].
Implemented as a {{GitHub|org=tferr|repo=hIPNAT|path=src/main/java/ipnat/skel|label=Java plugin}}.
|- valign="top"
|Summarize Skeleton
|{{bc|Analyze|Skeleton|Summarize Skeleton}}
|Bulk statistics of skeletonized images.
Implemented as a {{GitHub|org=tferr|repo=hIPNAT|path=src/main/java/ipnat/skel|label=Java plugin}}.
|- valign="top"
|Particles classifier
|{{bc|Analyze|Skeleton|Classify Particles Using Skeleton}}
|Tags particles according to skeleton features. Detects maxima on a masked image and clusters detected maxima using features of the skeletonized mask. A maxima is considered to be associated to a skeleton feature  (e.g., a junction or end-point, see  [[AnalyzeSkeleton]]) if the distance between its centroid and the feature is less than or equal to a cuttoff ("snap to") distance. Implemented as a {{GitHub|org=tferr|repo=hIPNAT|path=src/main/resources/scripts/|label=Python script}}.
|-
|colspan="3" style="background: #ddd; border-top: 1px solid gray; padding: 5px; text-align: center"|''Utilities''
|- valign="top"
|Fractal Trees
| {{bc|File|Open Samples|Fractal Tree}}
| Synthetic images ([https://en.wikipedia.org/wiki/L-system L-System] Trees) useful for debugging, testing or prototyping.
Implemented as a {{GitHub|org=tferr|repo=hIPNAT|path=src/main/java/ipnat/skel|label=Java plugin}}.
|}

= Further information =
* A list of all pages in this wiki related to image processing in the neurosciences can be found [[:Category:Neuroanatomy|here]].


[[Category:Neuroanatomy]]
