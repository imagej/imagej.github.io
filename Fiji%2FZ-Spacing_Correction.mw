{{Infobox
| name                   = Z-Spacing Correction
| software               = Fiji
| author                 = Philipp Hanslovsky, {{Person|Saalfeld}} ([mailto:saalfelds@janelia.hhmi.org])
| maintainer             = Philipp Hanslovsky, {{Person|Saalfeld}}
| source                 = [https://github.com/saalfeldlab/em-thickness-estimation]
| released               = April 16<sup>th</sup>, 2015
| latest version         = April 16<sup>th</sup>, 2015
| status                 = experimental, active
| category               = [[:Category:Plugins|Plugins]], [[:Category:TrakEM2|TrakEM2]], [[:Category:Transform|Transform]]
}}

== Citation ==
Please note that the z-spacing correction plugin available through Fiji, is based on a publication. If you use it successfully for your research please cite our work:

P. Hanslovsky, J. Bogovic, S. Saalfeld (2015) Post-acquisition image based compensation for thickness variation in microscopy section series, In ''International Symposium on Biomedical Imaging (ISBI'15)'', New York [http://arxiv.org/abs/1411.6970]

==Introduction==

Serial section Microscopy, using either optical or physical sectioning, is an established method for volumetric anatomy reconstruction.  Section series imaged with Electron Microscopy are currently vital for the reconstruction of the synaptic connectivity of entire animal brains such as that of ''Drosophila melanogaster''.  The process of removing ultrathin layers from a solid block containing the specimen, however, is a fragile procedure and has limited precision with respect to section thickness.  Optical sectioning techniques often suffer from increasing distortion as sections deeper inside the tissue are imaged.  On summary, section thickness that is supposed to be constant, in practice is not and has to be corrected where precise measurement is desired.  We have developed a method to estimate the relative ''z''-position of each individual section as a function of signal change across the section series.  The Fiji plugin '''Transform''' > '''Z-Spacing Correction''' and the [[TrakEM2]] plugin '''Plugins''' > '''LayerZPosition''' implement this method.

==Parameters==

;Neighborhood range
:Specifies the neighborhood around each section for which pairwise similarities are calculated. 
;Outer iterations
:Specifies the number of iterations in the outer loop of the optimizer.
;Outer regularization
:Specifies the amount of regularization in the outer loop of the optimizer. 0 means no regularization, 1 means full regularization (no change).  The regularizer in the outer loop damps the updates during each iteration by the specified fraction.
;Inner Iterations
:Specifies the number of iterations in inner loops of the optimizer.
;Inner Regularization
:Specifies the amount of regularization in the outer loop of the optimizer. 0 means no regularization, 1 means full regularization (no change).  The per-section quality weight requires regularization to avoid trivial solutions.  We use a Tikhonov regularizer towards 1.0 weight.
;Allow reordering
:Specifies whether layers/ sections can change their relative order in the series.

[[Category:Plugins]]
[[Category:TrakEM2]]
[[Category:Transform]]
[[Category:Citable]]
