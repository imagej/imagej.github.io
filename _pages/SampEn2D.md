{{Infobox
| name                   = Two-dimensional Sample Entropy (SampEn2D) PlugIn
| software               = Fiji
| author                  = {{Person|Acsenrafilho}} ([mailto:acsenrafilho@gmail.com])
| maintainer             = {{Person|Acsenrafilho}}
| source                 = {{GitHub | org = CSIM-Toolkits | repo = ImageJ/tree/master/plugins/SampleEntropy-2D | label = GitHub CSIM-ImageJ SampEn2D repository}}
| released               = June 23<sup>rd</sup>, 2016
| latest version         = June 23<sup>rd</sup>, 2016
| status                 = experimental, active
| category               = [[:Category:Plugins|Plugins]], [[:Category:Pattern Recognition|Pattern Recognition]]
}}
== Two-dimensional Sample Entropy ==

A PlugIn for the two-dimensional Sample Entroy method, which the algorithm was published at Biomedical Physics & Engineering Express article [http://dx.doi.org/10.1088/2057-1976/2/4/045002 weblink]. 

== Description ==

The extension of SampEn for a two-dimensional method was developed so as to maintain the original purpose of SampEn, i.e. an irregularity measure. In short, SampEn. quantifies the probability that m-length similar patterns will still be similar for m+1. Two patterns are considered similar if each corresponding point within the patterns are distant at most r from each other. This probability can be achieved by computing the total number of m and (m+1)- length patterns matches. The ratio between those values gives the conditional probability of finding (m+1)-length similar patterns, given they are similar for m.


== Parameters set==

[[Image:SampEn2D-gui.png|thumb|300px|SampEn2D GUI.]]

Basically, the common parameters that are used for adjust the SampEn2D method are the m and r. The m parameters is responsible to set the window size that is used to search the matching patterns all over the image. The r parameters is the tolerance parameter, i.e. as r rises the matching criteria became more permissive. Also, the r parameter is given is relationship with the stantard variation (SD) given by the image pixels intensity, where it is set by the percentual allowance over the image SD.
Usually, the pair (m,r) is set with the values m=1 and r=0.1, but the correct parameter adjust is crucial to each application. See the [http://dx.doi.org/10.1088/2057-1976/2/4/045002 journal article] and [http://dx.doi.org/10.1109/EMBC.2014.6944339 conference report] to have an starting point to correctly choose those parameters.
 
== Indicated Usage ==

Some studies were already made with different image set. At this moment, the SampEn2D obtained a promising results over histological images, which could be seem in the Reference section.
In general, the SampEn2D method is a method that measure the regularity level presented as a global feature. Also, this method is able to be applied over any 2D digital image, which offer an broad range of applications. 

== References ==

Here is a list of paper related with the SampEn2D method. Please, cite our method if you use it in your own research.

* Silva, L.E.V. et al., 2016. Two-dimensional sample entropy: assessing image texture through irregularity. Biomedical Physics & Engineering Express, 2(4), p.45002. DOI: 10.1088/2057-1976/2/4/045002.

* Silva, L.E.V. da et al., 2014. Two-dimensional sample entropy analysis of rat sural nerve aging. In Annual International Conference of the IEEE Engineering in Medicine and Biology Society. IEEE, pp. 3345–3348. DOI: 10.1109/EMBC.2014.6944339
