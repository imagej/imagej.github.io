== Citation ==
Please note that the SPIM registration plugin available through Fiji, is based on a publication. If you use it successfully for your research please be so kind to cite our work:
* S. Preibisch, S. Saalfeld, J. Schindelin and P. Tomancak (2010) "Software for bead-based registration of selective plane illumination microscopy data", ''Nature Methods'', '''7'''(6):418-419. [http://www.nature.com/nmeth/journal/v7/n6/full/nmeth0610-418.html Webpage] [[Media:Nmeth0610-418.pdf|PDF]] [[Media:Nmeth0610-418-S1.pdf|Supplement]]

== Important Note ==

<span style="color:#A52A2A">
'''''For details about the SPIM registration, fusion & deconvolution please have a look at the [[Multiview-Reconstruction|Multiview Reconstruction Plugin]]. It is much more powerful, flexible and completely integrated with the [[BigDataViewer]]. Documentation on the outdated [[SPIM Registration]] is still available.'''''
</span>

==Introduction==
===SPIM principles===

[[Image:SPIMScheme.png|thumb|right|300px|<b>Figure&nbsp;1:</b> Schematic drawing of a Selective Plane Illumination Microscope]]
A Selective Plane Illumination Microscope<ref name="HuiskenAl2004">{{cite journal
| author = J. Huisken and J. Swoger and F. D. Bene and J. Wittbrodt and E. H. K. Stelzer
| title = Optical Sectioning Deep Inside Live Embryos by Selective Plane Illumination Microscopy
| journal = Science
| volume = 305
| number = 5686
| pages = 1007&nbsp;1010
| year = 2004
}}</ref>
([[Media:SPIMScheme.png|Figure&nbsp;1]]), achieves optical
sectioning by focusing the excitation laser into a thin laser light sheet that reaches its minimal thickness in the middle of the field of view.  The light sheet enters the water filled sample chamber and illuminates the sample 
which is embedded in an agarose column. The agarose protrudes from the end of a glass capillary attached to a motor that rotates the sample.
The objective lens is arranged perpendicular to the light sheet. The perpendicular orientation of the illumination and detection optics ensures that only a section of the specimen in-focus is illuminated, minimizing photo-bleaching and laser damage of the living samples and allowing
for very long time-lapse recordings. Two-dimensional images of emitted
fluorescent light are captured by a CCD camera focussed on the center of the light-sheet. The CCD camera captures the light-sheet-illuminated section in a single exposure enabling a very fast acquisition rate important for capturing dynamic developmental events. In order to acquire 3d image stacks, the sample is moved through the light sheet in increments of 0.5&nbsp;&mu;m to 5&nbsp;&mu;m depending on the objective and the light sheet thickness.

The SPIM instrument can, in principle, achieve an isotropic, high resolution along <math>x</math>, <math>y</math> and <math>z</math>-axis allowing ''in toto''  imaging of large 3d specimens. In order to achieve an isotropic resolution uniformly across the sample volume in all three dimensions, it is necessary to rotate the sample and record image stacks of the same specimen from different angles (usually 3 to 12, see [[Media:Supplementary_Video_1_SPIM_in_Action.mov‎|Video&nbsp;1]]).

===Related work===

Multi-view microscopy techniques, such as tilted confocal acquisitions,<ref name="ShawAl89">
{{cite journal
| author =  P. Shaw, D. Agard, Y. Hiraoka, and J. Sedat
| title = Tilted view reconstruction in optical microscopy. Three-dimensional reconstruction of Drosophila melanogaster embryo nuclei
| journal = Biophysical Journal
| volume = 55
| number = 1
| year = 1989
| pages = 101&ndash;110 }}
</ref>
SPIM<ref name="HuiskenAl2004" /> and Ultramicroscopy<ref name="Dodt2007">
{{cite journal
| author = H. U. Dodt, U. Leischner, A. Schierloh, N. Jährling, C. P. Mauch, K. Deininger, J. M. Deussing, M. Eder, W. Zieglgänsberger, and K. Becker
| title = Ultramicroscopy: three-dimensional visualization of neuronal networks in the whole mouse brain
| doi = 10.1038/nmeth1036
| journal = Nature Methods
| number = 4
| pages = 331&ndash;336
| volume = 4
| year = 2007 }}</ref>
(2 views), can increase the resolution along the <math>z</math>-axis and thus enable the analysis of objects smaller than the axial resolution limit.<ref name="ShawAl89" /><ref name="Swoger2007">
{{cite journal
| author = J. Swoger, P. Verveer, K. Greger, J. Huisken, and E. H. K. Stelzer 
| journal = Opt. Express
| number = 13
| pages = 8029&ndash;8042
| title = Multi-view image fusion improves resolution in three-dimensional microscopy
| volume = 15
| year = 2007 }}</ref>
Image reconstruction based on the image intensities requires significant overlap of image content which is often difficult to achieve particularly in live imaging of dynamically changing samples.

The idea to incorporate fiduciary markers to facilitate sample independent reconstruction is widely used in medical imaging<ref name="Gullekson1974">{{citation
| title = Three Dimensional X-Ray Opaque Foreign Body Marker Device
| author = E. H. Gullekson
| year = Patent number: 3836776, Filing date: 1 Mar 1973, Issue date: Sep 1974
}}</ref><ref name="Erickson1993">{{cite journal
| author = B.J.  Erickson and Jack C.R. Jr. 
| title = Correlation of single photon emission CT with MR image data using fiduciary markers
| journal = American Journal of Neuroradiology
| volume = 14
| number = 3
| pages = 713&nbsp;720
| year = 1993
}}</ref><ref name="Fitzpatrick2001">{{cite journal
| author = J. M. Fitzpatrick and J. B. West 
| title = The distribution of target registration error in rigid-body point-based registration
| journal = IEEE Transactions on Medical Imaging
| volume = 20
| number = 9
| year = 2001
| month = September
| pages = 917&nbsp;927
}}</ref><ref name="Wiles2008">{{cite journal
| author = A. D. Wiles, A. Likholyot, D. D. Frantz, and T.M.Peters 
| title = A Statistical Model for Point-Based Target Registration Error With Anisotropic Fiducial Localizer Error
| journal = IEEE Transactions on Medical Imaging
| volume = 27
| number = 3
| year = 2008
| month = March
| pages = 378&nbsp;390
}}</ref><ref name="Moghari2008">{{cite conference
| author = M. H. Moghari, B. Ma, and P. Abolmaesumi
| title = A Theoretical Comparison of Different Target Registration Error Estimators
| booktitle = MICCAI '08: Proceedings of the 11th International Conference on Medical Image Computing and Computer-Assisted Intervention, Part II
| year = 2008
| isbn = 978-3-540-85989-5
| pages = 1032&nbsp;1040
| doi = 10.1007/978-3-540-85990-1_124
| publisher = Springer-Verlag
| location = Berlin, Heidelberg
}}</ref>
and electron tomography.<ref name="Dierksen1992">{{cite journal
| title = Towards automatic electron tomography
| journal = Ultramicroscopy
| volume = 40
| number = 1
| pages = 71&nbsp;87
| year = 1992
| author = K. Dierksen, D. Typke, R. Hegerl, A. J. Koster, and W. Baumeister
}}</ref><ref name="Koster1997">{{cite journal
| author = A. J. Koster, R. Grimm, D. Typke, R. Hegerl, A. Stoschek, J. Walz, and W. Baumeister 
| title = Perspectives of molecular and cellular electron tomography
| journal = J Struct Biol
| year = 1997
| volume = 120
| number = 3
| pages = 276&nbsp;308
}}</ref>
Due to the low amount of fiduciary markers available for registration, research is focused on error analysis rather than efficiency of matching of thousands of markers with only partial overlap.<ref name="Fitzpatrick2001" />

In contrast, in the robotics and automation field, there is interest in localization of large amounts of different objects. Points of interest are extracted from photos and checked against databases to determine their type and orientation.<ref name="HarrisS88">{{cite conference
| title = A Combined Corner and Edge Detector
| author = C. Harris and M. Stephens
| locaiton = Plessey Research Roke Manor, UK
| booktitle = Proceedings of The Fourth Alvey Vision Conference
| location = Manchester
| year = 1988
| pages = 147&nbsp;151
}}</ref><ref name="Canny86">{{cite journal
| title = A computational approach to edge detection
| author = J. Canny
| journal = IEEE Transactions on Pattern Analysis Machine Intelligence
| volume = 8
| number = 6
| year = 1986
| pages = 679&nbsp;698
}}</ref>
To enable real time object recognition, Lamdan et al.<ref name="LamdanAl88">{{cite conference
| author = Y. Lamdan, J. Schwartz, and H. Wolfson 
| title = On recognition of 3D objects from 2D images
| booktitle = Proceedings of the IEEE International Conference on Robotics and Automation
| year = 1988
| pages = 1407&nbsp;1413
| publisher = IEEE Computer Society
| location = Los Alamitos, CA
}}</ref>
introduced &lsquo;geometric hashing'&rsquo;  which uses an intrinsic invariant local coordinate system to match objects against database entries in a viewpoint independent manner. The geometric hashing principle is reused in the fields of astronomy<ref name="Hogg2008">{{cite conference
| author =  D. W. Hogg, M. Blanton, D. Lang, K. Mierle, and S. Roweis
| title = Automated Astrometry
| booktitle = Astronomical Data Analysis Software and Systems XVII
| year = 2008
| series = Astronomical Society of the Pacific Conference Series
| volume = 394
| editor = R. W. Argyle, P. S. Bunclark, and J. R. Lewis 
| month = August
| pages = 27-+
}}</ref>
and protein structure alignment and comparison<ref name="Nussinov91">{{cite journal
| author = R. Nussinov and H. J. Wolfson
| journal = Proc Natl Acad Sci U S A
| number = 23
| pages = 10495&nbsp;10499
| title = Efficient detection of three-dimensional structural motifs in biological macromolecules by computer vision techniques.
| volume = 88
| year = 1991
}}</ref><ref name="Fischer94">{{cite journal
| author = D. Fischer, H. Wolfson, S. L. Lin, and R. Nussinov 
| title = Three-dimensional, sequence order-independent structural comparison of a serine protease against the crystallographic database reveals active site similarities: Potential implications to evolution and to protein folding
| journal = Protein Science
| volume = 3
| number = 5
| pages = 769&nbsp;778
| year = 1994
}}</ref><ref name="Wallace1997">{{cite journal
| author = A.C. Wallace, N. Borkakoti, and J. M. Thornton 
| title = Tess: A geometric hashing algorithm for deriving 3D coordinate templates for searching structural databases. Application to enzyme active sites
| journal = Protein science
| year = 1997
| volume = 6
| number = 11
| pages = 2308
}}</ref><ref name="Stark2003">{{cite journal
| title = A Model for Statistical Significance of Local Similarities in Structure
| journal = Journal of Molecular Biology
| volume = 326
| number = 5
| pages = 1307&nbsp;1316
| year = 2003
| author = A. Stark, S. Sunyaev, and R. B. Russell
}}</ref>
where efficient searching in massive point clouds is required.

The use of local descriptors instead of complete scenes for matching is proposed in many fields comprising image registration,<ref name="Stanski2005">{{cite conference
| author = A. Stanski and O. Hellwich
| title = Spiders as Robust Point Descriptors
| booktitle = DAGM-Symposium
| year = 2005
| pages = 262&nbsp;268
}}</ref><ref name="Lowe04">{{cite journal
| author = D. G. Lowe
| title = Distinctive image features from scale-invariant keypoints
| journal = Int J Comput Vis
| volume = 60
| number = 2
| pages = 91&nbsp;110
| year = 2004
}}</ref>
robotics and autonomous systems,<ref name="Kuipers91">{{cite journal
| author = B. Kuipers and Yung-tai Byun
| title = A Robot Exploration and Mapping Strategy Based on a Semantic Hierarchy of Spatial Representations
| journal = Journal of Robotics and Autonomous Systems
| year = 1991
| volume = 8
| pages = 47&nbsp;63
}}</ref><ref name="Bradley04">{{cite conference
| author = D. Bradley, D. Silver, and S. Thayer
| title = A regional point descriptor for global localization in subterranean environments
| booktitle = IEEE conference on Robotics Automation and Mechatronics (RAM 2005)
| pages = 440&nbsp;445
| month = December
| year = 2004
| volume = 1
}}</ref>
and computer vision.<ref name="Frome04">{{cite conference
| author = A. Frome, D. Huber, R. Kolluri, T. Bulow, and J. Malik
| title = Recognizing objects in range data using regional point descriptors
| booktitle = Proceedings of the European Conference on Computer Vision (ECCV)
| month = May
| year = 2004
}}</ref>

Matula et al.<ref name="Matula2003">{{cite journal
| author = P. Matula, M. Kozubek, F. Staier, and M. Hausmann 
| journal = Journal of microscopy
| pages = 126&nbsp;42
| title = Precise 3D image alignment in micro-axial tomography.
| volume = 209
| year = 2003
}}</ref>
suggest segmentation based approaches for reconstruction of multi-view microscopy images.  The center of mass of the cloud of segmented objects is used as a reference point for a cylindrical coordinate system facilitating the registration between two views.  Similarly to intensity based approaches, this method requires significant overlap between the images and furthermore supports alignment of only two stacks at a time.

Our approach combines the idea of using fiduciary markers, local descriptors and geometric hashing and applies global optimization.  It can register an arbitrary number of partially overlapping point clouds.  It is robust with respect to the amount of incorporated beads, bead distribution, amount of overlap, and can reliably detect non-affine disturbances (e.g. abrupt agarose movement) that might occur during imaging ([[#Table1|Table&nbsp;1]]).

==The Method==

===Bead Segmentation===

The incorporated sub-resolution beads appear as the Point Spread Function (PSF) of the microscopic system in each image&nbsp;<math>I(x,y,z)</math>. To detect beads, one would ideally convolve it with the impulse response&nbsp;(PSF) of the microscope yielding highest correlation at the sub-pixel location of each bead. However, the PSF is not constant over different experiments due to changing exposure times, laser power, bead types, objectives and agarose concentration. Furthermore, the PSF is not constant across the field of view due to the concavity of the light sheet and thus the convolution operation is computationally very demanding.  

We found that an appropriately smoothed 3d LaPlace filter&nbsp;<math>\nabla^2</math> detects all beads with sufficient accuracy while effectively suppressing high frequency noise.  As suggested in the Computer Vision literature,<ref name="Lindeberg94">{{cite journal
| author = T. Lindeberg
| title = Scale-space theory: A basic tool for analysing structures at different scales
| journal = Journal of Applied Statistics
| volume = 21
| number = 2
| pages = 224&nbsp;270
| year = 1994
}}</ref><ref name="Lowe04" />
we approximate <math>\nabla^2I</math> by the difference of two Gaussian convolutions (DoG) of the image&nbsp;<math>I</math> with a standard deviation&nbsp;<math>\sigma</math> of 1.4&nbsp;px and 1.8&nbsp;px respectively.  All local minima in a 3&times;3&times;3 neighborhood in <math>\nabla^2I</math> represent intensity maxima whose sub-pixel location is then estimated by fitting a 3d quadratic function to this neighbourhood.<ref name="BrownLowe02">{{cite conference
| author = M. Brown and D. Lowe
| title = Invariant Features from Interest Point Groups
| booktitle = In British Machine Vision Conference
| year = 2002
| pages = 656&nbsp;665
}}</ref>
The DoG detector identifies beads even if they are close to each other, close to the sample or those with an unexpected shape.  It also massively oversegments the image detecting &lsquo;blob-like&rsquo; structures, corners and various locations alongside edges or planes within the imaged sample. However, those detections do not interfere with the registration process as the descriptors that incorporate them are filtered out by local descriptor matching (see [[Media:DescriptorBuildup.png|Figure&nbsp;2]]).  Only beads are repeatably detected in different views.

===Establishing Bead Correspondences===

[[Image:DescriptorBuildup.png|thumb|right|300px|<b>Figure&nbsp;2:</b> Rotation invariant local geometric descriptor]]
To register two views&nbsp;<math>A</math> and <math>B</math> the corresponding bead pairs <math>(\vec{a},\vec{b})</math> have to be identified invariantly to translation and rotation. To this end, we developed a ''geometric local descriptor'' . The local descriptor of a bead is defined by the locations of its 3&nbsp;nearest neighbors in 3d image space ordered by their distance to the bead. To efficiently extract the nearest neighbors in image space we use the ''kd''-tree implementation of the WEKA framework.<ref name="WEKA">{{cite book
| author = I. H. Witten and E. Frank
| title = Data Mining: Practical machine learning tools and techniques
| publisher = Morgen Kaufmann
| location = San Francisco
| isbn = 0-12-088407-0
| edition = second
| year = 2005
}}</ref>
Translation invariance is achieved by storing locations relative to the bead.  That is, each bead descriptor is an ordered 3d point cloud of cardinality 3 with its origin <math>\vec{o} = (0,0,0)^T</math>} being the location of the bead.

Local descriptor matching is performed invariantly to rotation by mapping the ordered point cloud of all beads <math>\vec{a}\in A</math> to that of all beads <math>\vec{b}\in B</math> individually by means of least square point mapping error using the closed-form unit quaternion-based solution.<ref name="Horn87">{{cite journal
| author = B. K. P. Horn
| title = Closed-form solution of absolute orientation using unit quaternions
| journal = Journal of the Optical Society of America A
| volume = 4
| number = 4
| pages = 629&nbsp;642
| year = 1987
}}</ref>
The similarity measure <math>\epsilon</math> is the average point mapping error. Each candidate in <math>A</math> is matched against each candidate in <math>B</math>.  Corresponding descriptors are those with minimal <math>\epsilon</math>. This approach, however, is computationally very demanding as it has a complexity of <math>O(n^2)</math> regarding the number of detections.<ref name="Preibisch2009a">{{cite conference
| author = S.  Preibisch and S.  Saalfeld and T.  Rohlfing and P. Tomancak 
| title = Bead-based mosaicing of single plane illumination microscopy images using geometric local descriptor matching
| booktitle = Medical Imaging 2009: Image Processing
| year = 2009
| editor = J. P. W.  Pluim and B. M. Dawant 
| volume = 7259
| number = 1
| pages = 72592S
| location = Orlando, FL, USA
| doi = 10.1117/12.812612
| series = Proceedings of SPIE
}}</ref>

We therefore employed a variation of geometric hashing<ref name="LamdanAl88" /> to speed up the matching process. Instead of using one reference coordinate system for the complete scene we define a local coordinate system for each of the descriptor as illustrated and described in [[Media:DescriptorBuildup.png|Figure&nbsp;2]]. All remaining bead coordinates not used for defining the local coordinate system become rotation invariant which enables us to compare descriptors very efficiently using ''kd''-trees to index remaining bead coordinates in the local coordinate system.
Again, we employ the ''kd''-tree implementation of the WEKA framework<ref name="WEKA" /> on a six-dimensional tree to identify nearest neighbors in the descriptor space, i.e. descriptors which are most similar. The most similar descriptors that are significantly better (10&times;) than the second nearest neighbor in descriptor space are designated correspondence candidates.<ref name="Lowe04" />

Descriptors composed of only four beads are not completely distinctive and similar descriptors can occur by chance. Increasing the number of beads in the descriptor would make it more distinctive to the cost of less identified correspondences and increased computation time. All true correspondences agree on one transformation model for optimal view registration, whereas each false correspondence supports a different transformation. Therefore, we used the minimal descriptor size (4 beads) and rejected false correspondences from candidate sets with the Random Sample Consensus (RANSAC)<ref name="FischlerB81">{{cite journal
| author = M. A. Fischler and R. C. Bolles
| title = Random sample consensus: a paradigm for model fitting with applications to image analysis and automated cartography
| journal = Communications of the ACM
| volume = 24
| number = 6
| pages = 381&nbsp;395
| year = 1981
}}</ref>
on the affine transformation model followed by robust regression.

===Global Optimization===

The identified set of corresponding beads <math>C_{AB} = \{(\vec{a}_i,\vec{b}_i) : i=\{1,2, \dots, \left| C\right|\}\}</math> for a pair of views <math>A</math> and <math>B</math> defines an affine transformation&nbsp;<math>\mathbf{T}_{AB}</math> that maps <math>A</math> to <math>B</math> by means of least square bead correspondence displacement
<center><math>
\arg\min_{\mathbf{T}_{AB}}\sum_{(\vec{a},\vec{b})\in C_{ab}}{\left\|\mathbf{T}_{AB}\vec{a} - \vec{b}\right\|^2}.
</math></center>

We use an affine transformation to correct for the anisotropic <math>z</math>-stretching of each view introduced by the differential refraction index mismatch between water and agarose<ref name="Hell1993">{{cite journal
| title = Aberrations in Confocal Fluorescence Microscopy Induced by Mismatches in Refractive Index
| journal = Journal of Microscopy
| volume = 169
| number = 3
| pages = 341&nbsp;405
| year = 1993
| author = S.  Hell and G.  Reiner and C.  Cremer and E.H.K. Stelzer 
}}</ref><ref name="Matula2003" /> as the sample is never perfectly centered in the agarose column.

Registration of more than two views requires groupwise optimization of the configuration <math>T_{VF} = \{\mathbf{T}_{AF} : A,F\in V\}</math> with <math>V</math> being the set of all views and <math>F</math> being a fixed view that defines the common reference frame.  Then, the above Equation extends to
<center><math>
\arg\min_{T_{VF}}\sum_{A\in V\setminus\{F\}}\left(\sum_{B\in V\setminus\{A\}}\left(\sum_{(\vec{a},\vec{b})\in C_{AB}}{\left\|\mathbf{T}_{AF}\vec{a} - \mathbf{T}_{BF}\vec{b}\right\|^2}\right)\right)
</math></center>
with <math>C_{AB}</math> being the set of bead correspondences <math>(\vec{a},\vec{b})</math> between view&nbsp;<math>A</math> and view&nbsp;<math>B</math> whereas <math>\vec{a}\in A</math> and <math>\vec{b}\in B</math>.  This term is solved using an iterative optimization scheme.  In each iteration, the optimal affine transformation&nbsp;<math>\mathbf{T}_{AF}</math> for each single view&nbsp;<math>A\in V\setminus\{F\}</math> relative to the current configuration of all other views is estimated and applied to all beads in this view.  The scheme terminates on convergence of the overall bead correspondence displacement.  This solution allows us to perform the global optimization with any transformation model in case the microscopy set-up has different properties (e. g. translation<ref name="Preibisch2009b">{{cite journal
| author = S.  Preibisch and S.  Saalfeld and P. Tomancak 
| title = Globally Optimal Stitching of Tiled 3D Microscopic Image Acquisitions
| journal = Bioinformatics
| volume = 25
| number = 11
| pages = 1463&nbsp;1465
| doi = 10.1093/bioinformatics/btp184
| year = 2009
}}</ref>, rigid<ref name="Preibisch2009a" />).

===Time-lapse registration===

During extended time-lapse imaging, the whole agarose column may move. To compensate the drift, we used the bead-based registration framework to register individual time-points to each other. We select a single view <math>A_t</math> from an arbitrary time-point <math>t</math> in the middle of the series as reference. Subsequently, we use the stored DoG detections to identify the true corresponding local geometric descriptors for all pairs of views <math>A_t</math> and
<math>A_{a\in{\{1,2, \dots \}\setminus\{t\}}}</math> and calculate an affine transformation&nbsp;<math>\mathbf{T}_{A_aA_t}</math> that maps <math>A_a</math> to <math>A_t</math> by means of least square bead correspondence displacement. The identified transformation matrices are then applied to all remaining views in the respective time-points resulting in a registered time series ([[Media:ErrorAnalysis.png|Figure&nbsp;4a]]).

===Image Fusion and blending===

[[Image:Blending.jpg|thumb|right|300px|<b>Figure&nbsp;3:</b> Image fusion]]
The registered views can be combined to create a single isotropic 3d image. An effective fusion algorithm must ensure that each view contributes to the final fused volume only useful sharp image data acquired from the area of the sample close to the detection lens.  Blurred data visible in other overlapping views should be suppressed.  We use Gaussian Filters to approximate the image information at each pixel in the contributing views ([[Media:Blending.jpg|Figure&nbsp;3c,f]]).<ref name="PreiRohlHasa2008">{{cite conference
| author = S.  Preibisch and T.  Rohlfing and M. P.  Hasak and P. Tomancak 
| title = Mosaicing of Single Plane Illumination Miscroscopy Images Using Groupwise Registration and Fast Content-Based Image Fusion
| booktitle = Medical Imaging 2008: Image Processing
| year = 2008
| editor = J. M.  Reinhardt and J. P. W. Pluim 
| volume = 6914
| number = 1
| pages = 69140E
| location = San Diego, CA, USA
| url = http://link.aip.org/link/?PSI/6914/69140E/1
| doi = 10.1117/12.770893
| series = Proceedings of SPIE
}}</ref>

For strongly scattering and absorbing specimen like ''Drosophila'' , we typically do not image the entire specimen in each single view, but instead stop at roughly two thirds of its depth as the images become increasingly blurred and distorted. In the reconstructed 3d image, this introduces line artifacts in areas where a view ends abruptly ([[Media:Blending.jpg|Figure&nbsp;3a,d]]). To suppress this effect for the purposes of data display, we apply non-linear blending close to the edges of each border between the views ([[Media:Blending.jpg|Figure&nbsp;3b,e]]).<ref name="Preibisch2009b" />

Precise registration of multi-view data is the prerequisite for multi-view deconvolution of the reconstructed image which can potentially increase the resolution.<ref name="Swoger2007" /><ref name="Engelbrecht2006">{{cite journal
| author = C. J. Engelbrecht and E. H. K. Stelzer
| title = Resolution enhancement in a light-sheet-based microscope (SPIM)
| journal = Optics  Letters
| volume = 31
| number = 10
| pages = 1477&nbsp;1479
| year = 2006
}}</ref><ref name="Verveer2007">{{cite journal
| title = High-resolution three-dimensional imaging of large specimens with light sheet-based microscopy
| journal = Nature Methods
| volume = 4
| number = 4
| pages = 311&nbsp;313
| year = 2007
| author = P.J. Verveer and J. Swoger and F. Pampaloni and K. Greger and M. Marcello and E.H.K.Stelzer 
}}</ref>
Having sub-resolution fluorescent beads around the sample facilitates the estimation of a spatially dependent point spread function and validates the deconvolution results.

===Strategies for bead removal===

The presence of sub-resolution fluorescent beads used for the registration of the views might interfere with subsequent analysis of the dataset. To computationally remove the beads from each view we compute the average bead shape by adding the local image neighborhood of all true correspondences (beads used for registration) of the respective view. The acquired template is subsequently used to identify other beads; to speed up the detection we compare this template only to all maxima detected by the Difference-of-Gaussian operator during the initial bead segmentation step. These DoG-detections contain all image maxima and therefore all beads of the sample. The beads are then removed by subtracting a normalized, Gaussian-blurred version of the bead template. This method reliably removes beads which are clearly separated from the sample judged by the average intensity in the vicinity of the detected bead. Therefore, some beads that are positioned very close to the sample are not removed as the bead-subtraction would interfere with the samples' intensities.

To completely remove all beads from the sample we adapt the intensities of the beads to the imaged sample. Therefore we simply embed beads excitable by a different wavelength then the fluorescent maker in the sample and use a long-pass filter for detection ([[Media:Showcase.jpg|Figure&nbsp;6e,g]]). In such acquisition the intensity of the beads is around 2-4.

==Evaluation==

===Evaluation of the performance of the bead-based registration framework===

[[Image:ErrorAnalysis.png|thumb|right|300px|<b>Figure&nbsp;4:</b> Analysis of the registration error]]
We created a visualization of the optimization procedure. For each view, we display its bounding box and the locations of all corresponding descriptors in a 3d visualization framework<ref name="Bene2007">{{cite conference
| author = B. Schmidt 
| title = Hardware-accelerated 3D visualization for ImageJ
| booktitle = ImageJ User and Developer Conference
| year = 2008
| volume = 2
| editor = Pierre Plumer 
}}</ref>.
Correspondences are color coded logarithmically according to their current displacement ranging from red (&gt;100&nbsp;px) to green (&lt;1&nbsp;px). The optimization is initialized with a configuration where the orientation of the views is unknown; all views are placed on top of each other and thus the corresponding descriptor displacement is high (red). As the optimization proceeds, the average displacement decreases (yellow) until convergence at about one pixel average displacement (green) is achieved. [[Media:Supplementary_Video_2_Global_Opt.mov‎|Video&nbsp;2]]  shows the optimization progress for an 8 angle acquisition of fixed ''C.elegans'' . The outline of the worm forms in the middle (grey), since many worm nuclei were segmented by the DoG detector but discarded during establishment of bead correspondences.

The global optimization scheme can be seamlessly applied to tiled multi-view acquisitions. In such a set-up, different parts of a large 3d sample are scanned with a high-magnification lens from multiple angles separately. All such acquisitions can be mixed, discarding all information about their arrangement and the global optimization recovers the correct configuration. An example of such optimization is shown in [[Media:Supplementary_Video_3_Global_Opt_with_Tiling.mov‎|Video&nbsp;3]]  containing a fixed ''Drosophila''  embryo imaged from 8 angles across two or three tiles per angle on a single photon confocal microscope with a 40&times;/0.8 Achroplan objective.

To prove the accuracy of the bead-based registration framework, we created a simulated bead-only dataset with beads approximated by a Gaussian filter response with &sigma;=1.5&nbsp;px.  We generated 8 different views related by an approximately rigid affine transformation with isotropic resolution. The reconstruction of this dataset yielded an average error of 0.02&nbsp;px ([[#Table1|Table&nbsp;1]]).
For real-life datasets, the registration typically results in errors of about 1&nbsp;px or slightly lower ([[Media:ErrorAnalysis.png|Figure&nbsp;4b]]  and [[#Table1|Table&nbsp;1]]) where the remaining error is introduced by the localization accuracy of the bead detector and small non-affine disturbances induced by elastic deformation of the agarose.  In the <math>xy</math>-plane of each view, the beads can be localized very precisely, however, alongside <math>z</math>, the localization accuracy drops due to a lower sampling rate and an asymmetric PSF. This is supported by the dimension dependent error shown in [[Media:ErrorAnalysis.png|Figure&nbsp;4c,d]].

[[#Table1|Table&nbsp;1]] shows that for the registration we usually use significantly more beads than necessary to solve an affine transformation (4 beads). It is necessary to use many beads for registration due to the following reasons:
* If the overlap between stacks is&mdash;as in many examples shown&mdash;very small, it has to be ensured that in these small overlapping areas there are still enough fiduciary markers to align the stacks. 
* If two stacks are extensively overlapping, the beads have to be evenly distributed around the sample to ensure an even error distribution throughout the sample. Otherwise, small errors in, for example, the lower left corner do not control the registration error in the upper right corner where there are no fiduciary markers.	
* The localization error of the beads is normally distributed as shown in [[Media:ErrorAnalysis.png|Figure&nbsp;4c,d]]. That means, the more beads are included in the registration, the more accurate is the average localization of the beads. Consequently, the affine transformation for each individual stack yields lower residual error the more beads are used.


Due to the optical properties of the sample it might occur that beads are distorted and aberrated and therefore detected in the wrong location. Typically, such beads are excluded as they do not form repeatable descriptors between the different stacks. If the distortions are minor, they will contribute to the residual error of the affine transformation. However, the contribution is small as those beads represent a very small fraction of all beads. This is supported by the maximal transfer error of &nbsp;1 px of the affine model (see also inset of [[Media:Intensity_vs_Beads.jpg|Figure&nbsp;5c,d]]).

Examples of within and across time-points registered time-series of ''Drosophila''  embryonic development are shown in [[Media:Supplementary_Video_4_Drosophila_Gastrulation.mov‎|Video&nbsp;4]]  and [[Media:Supplementary_Video_5_Drosophila_Embryogenesis.mov‎|Video&nbsp;5]]. The videos show 3d renderings of the developing embryos expressing His-YFP in all cells.  The 3d rendered single embryo is shown from four and three arbitrary angles to highlight the complete coverage of the specimen. [[Media:Supplementary_Video_4_Drosophila_Gastrulation.mov‎|Video&nbsp;4]] shows in 42 time-points (7 angles) the last two synchronous nuclear divisions followed by gastrulation. [[Media:Supplementary_Video_5_Drosophila_Embryogenesis.mov‎|Video&nbsp;5]] captures in 249 time-points (5 angles) ''Drosophila''  embryogenesis from gastrulation to mature embryo when muscle activity effectively prevents further imaging.

===Performance of the bead-based registration framework in comparison with intensity-based methods===

[[Image:Intensity_vs_Beads.jpg|thumb|right|300px|<b>Figure&nbsp;5:</b> Comparison of bead-based and intensity-based multi-view reconstruction on 7-view acquisition of Drosophila embryo expressing His-YFP]]
Existing muti-view SPIM registration approaches that use sample intensities to iteratively optimize the quality of the overlap of the views do not work reliably and are computationally demanding.<ref name="Swoger2007">{{cite journal 
| author = Jim Swoger and Peter Verveer and Klaus Greger and Jan Huisken and Ernst H. K. Stelzer
| journal = Opt. Express
| number = 13
| pages = 8029&nbsp;8042
| publisher = OSA
| title = Multi-view image fusion improves resolution in three-dimensional microscopy
| volume = 15
| year = 2007
}}</ref><ref name="PreiRohlHasa2008">{{cite conference
| author = S.  Preibisch and T.  Rohlfing and M. P.  Hasak and P. Tomancak 
| title = Mosaicing of Single Plane Illumination Miscroscopy Images Using Groupwise Registration and Fast Content-Based Image Fusion
| booktitle = Medical Imaging 2008: Image Processing
| year = 2008
| editor = J. M.  Reinhardt and J. P. W. Pluim 
| volume = 6914
| number = 1
| pages = 69140E
| location = San Diego, CA, USA
| url = http://link.aip.org/link/?PSI/6914/69140E/1
| doi = 10.1117/12.770893
| series = Proceedings of SPIE
}}</ref><ref name="Preibisch08a">{{cite conference
| author = S. Preibisch and R. Ejsmont and T. Rohlfing and P. Tomancak
| title = Towards Digital Representation of Drosophila Embryogenesis
| booktitle = Proceedings of 5th IEEE International Symposium on Biomedical Imaging
| pages = 324&nbsp;327
| year = 2008
}}</ref>
Alternatively, the registration can be achieved by matching of segmented structures, such as cell nuclei, between views<ref name="Keller08">{{cite journal
| author = P. J.  Keller and A. D.  Schmidt and J.  Wittbrodt and E. H. Stelzer 
| title = Reconstruction of zebrafish early embryonic development by scanned light sheet microscopy
| journal = Science
| volume = 322
| number = 5904
| pages = 1065-9
| year = 2008
}}</ref>
However, such approaches are not universally applicable, as the segmentation process has to be adapted to the imaged sample.

To evaluate the precision and performance of the bead-based registration framework we compared it against the intensity-based registration method that we developed previously.<ref name="Preibisch08a">{{cite conference
| author = S. Preibisch and R. Ejsmont and T. Rohlfing and P. Tomancak
| title = Towards Digital Representation of Drosophila Embryogenesis
| booktitle = Proceedings of 5th IEEE International Symposium on Biomedical Imaging
| pages = 324&nbsp;327
| year = 2008
}}</ref>
This method identifies the rotation axis common to all views by iterative optimization of FFT-based phase correlation between adjacent views. We applied both methods (bead-based and intensity-based) to a single time-point of live 7-view acquisition of ''Drosophila''  embryo expressing His-YFP in all cells embedded in agarose with beads. We chose a time-point during blastoderm stage where the morphology of the embryo changes minimally over time. We evaluated the precision of both methods by the average displacement of the corresponding beads and concluded that the bead-based registration framework clearly outperformed the intensity-based registration in terms of bead registration accuracy (0.98&nbsp;px versus 6.91&nbsp;px, see [[#Table1|Table&nbsp;1]], [[Media:Intensity_vs_Beads.jpg|Figure&nbsp;5]]). The increased precision in the bead alignment achieved by the bead-based registration framework is reflected in noticeably improved overlap of the nuclei in the sample (see [[Media:Intensity_vs_Beads.jpg|Figure&nbsp;5c–h]]). Moreover, the intensity-based method required approximately 9 hours of computation time compared to 2.5&nbsp;minutes for the bead-based registration framework executed on the same computer hardware (Intel Xeon E5440 with 64GB of RAM), i.e. the bead-based framework is about 200&nbsp; faster for this dataset.

----

{| id="Table1" style="text-align:center"
|+ style="margin-top:1em; margin-bottom:1em;" |'''Table&nbsp;1:''' Statistics of multi-view registration of various datasets
|-
! Dataset
! min/avg/max error [px]
! DoG detections
! True correspondence number (ratio)
! processing time [min:sec]
|-
| Fixed ''C.elegans'', 8 views<br />SPIM 40&times;/0.8NA
| 1.02/1.12/1.31
| 4566
| 1717 (98%)
| 11:09
|-
| Live ''Drosophila'', 5 views<br />SPIM 20&times;/0.5NA
| 0.76/0.81/1.31
| 9267
| 1459 (97%)
| 2:31
|-
| Fixed ''Drosophila'', 10 views<br />SPIM 20&times;/0.5NA
| 0.65/0.78/0.97
| 9035
| 1301 (93%)
| 20:10
|-
| Fixed ''Drosophila'', 11 views<br />Spinning Disc 20&times/0.5NA
| 1.10/1.33/1.86
| 6309
| 978 (92%)
| 6:15
|-
| Simulated Dataset, 8 views<br />Isotropic Resolution
| 0.02/0.02/0.02
| 2594
| 2880 (96%)
| 15:54
|-
| Live ''Drosophila'', 7 views<br />SPIM 20&times;/0.5NA<br />'''bead-based'''
| 0.87/0.98/1.17
| 6232
| 603 (97%)
| 2:27
|-
| Live ''Drosophila'', 7 views<br />SPIM 20&times;/0.5NA<br />'''intensity-based'''
| 0.93/6.91/9.59
| n.a.
| n.a.
| 515:10
|}

We show minimal, average and maximal displacement of all true correspondences (beads) after convergence of the global optimization. The simulated dataset shows very low registration errors. The total number of DoG detections is typically much higher than the number of extracted correspondence candidate pairs although a DoG detection can participate in more than one correspondence pair. The ratio of true correspondences versus correspondence candidates is typically above 90%.  Lower ratios indicate a registration problem, for example caused by movement of the agarose during stack acquisition. The processing time (segmentation and registration) was measured on a dual quad-core Intel Xeon E5440 system.

----

==Samples imaged by SPIM==

===Overview of imaged specimens===

[[Image:Showcase.jpg|thumb|right|300px|<b>Figure&nbsp;6:</b> Examples of various reconstructed multi-view datasets]]
We demonstrated the performance of our registration framework on multi-view ''in toto''  imaging of fixed and living specimen of various model organisms ([[Media:Showcase.jpg|Figure&nbsp;6]]), in particular ''Drosophila'' . Fixed ''Drosophila''  embryos were stained with Sytox-Green to label all nuclei. For live imaging, we used a developing ''Drosophila''  embryo expressing fluorescent His-YFP under the control of endogenous promoter visualizing all nuclei. ''Drosophila''  specimens were imaged with a SPIM prototype equipped with a Zeiss 20&times;/0.5 Achroplan objective.

===Sample mounting for SPIM===

We matched the fluorescence intensity of the beads to the signal intensity of the sample. For live imaging of His-YFP which is relatively dim and requires longer exposure times (0.3&nbsp;s), we used red or yellow fluorescent beads that are suboptimal for the GFP detection filter set and therefore typically less bright than the sample. Conversely, for the imaging of the bright, fixed specimen, we used green fluorescent beads which give adequate signal at very short exposure times (0.01&nbsp;s).

Despite the fact that our algorithm is robust with respect to the amount of beads available for registration, too many beads unnecessarily increase the computation time, while too few beads may result in an inadequate number of correspondences due to incomplete overlap of the views. Therefore, we determined empirically the optimal concentration of beads for each magnification (ideally 1,000&ndash;2,000 beads per imaged volume).  We prepared a 2&times; stock solution of beads (13&nbsp;μl of concentrated bead solution (Estapor Microspheres FXC050))

===Sample independent registration===

We applied the bead-based registration framework to various samples derived from major model organisms. These include ''Drosophila''  embryo, larva ([[Media:Showcase.jpg|Figure&nbsp;6a–c]]) and oogenesis ([[Media:Showcase.jpg|Figure&nbsp;6d]]), ''C. elegans''  adult (data not shown), larval stages ([[Media:Showcase.jpg|Figure&nbsp;6e]]) and early embryo ([[Media:Showcase.jpg|Figure&nbsp;6f]]), whole mouse embryo ([[Media:Showcase.jpg|Figure&nbsp;6g]]), and dual color imaging of zebrafish embryo ([[Media:Showcase.jpg|Figure&nbsp;6h]]). Despite the fact that the samples range significantly in their size, fluorescent labeling, optical properties and mounting formats the bead-based registration framework was invariably capable of achieving the registration. Therefore, we conclude that our method is sample independent and is universally applicable for registration of any multi-view SPIM acquisition where the sample movement does not disturb the rigidity of the agarose.


==Broad applicability of the bead-based framework to multi-view imaging==

[[Image:Rotation_chamber.png|thumb|right|300px|<b>Figure&nbsp;7:</b> Multi-view imaging with spinning disc confocal microscopy]]
Having the bead-based registration framework for multi-view reconstruction established, we sought to expand its application beyond SPIM, to other microscopy techniques capable of multi-view acquisition.<ref name="Bradl92">{{cite journal
| author = J. Bradl and M. Hausmann and V. Ehemann and D. Komitowski and C. Cremer
| title = A tilting device for three-dimensional microscopy: application to in situ imaging of interphase cell nuclei.
| journal = Journal of Microscopy
| year = 1992
| volume = 168
| pages = 47&nbsp;57
}}</ref>
We designed a sample-mounting set-up that allows imaging of a sample embedded in a horizontally positioned agarose column with fluorescent beads ([[Media:Rotation_chamber.png|Figure&nbsp;7a]]). The agarose column was manually rotated mimicking the SPIM multi-view acquisition. We acquired multiple views of fixed Drosophila embryos stained with nuclear dye on a spinning disc confocal microscope and reconstructed the views using the bead-based registration framework. By mosaicking around the sample, we captured the specimen in toto and achieved full lateral resolution in areas that are compromised by the poor axial resolution of a single-view confocal stack ([[Media:Rotation_chamber.png|Figure&nbsp;7b,c,d]] and [[Media:Supplementary_Video_6_Drosophila_Spinning_Disc.mov‎|Video&nbsp;6]]  ). The combination of multi-view acquisition and bead-based registration is applicable to any imaging modality as long as the fluorescent beads can be localized and the views overlap.

===Sample mounting for multi-view imaging on an upright microscope===

We constructed a sample chamber for multi-view imaging on an upright microscope that consists of a teflon dish equipped with a hole in the side wall which has the diameter of a standard glass capillary ([[Media:Rotation_chamber.png|Figure&nbsp;7a]]). The capillary mounting hole continues on the bottom of the dish as a semi-circular trench of approximately half the thickness of the capillary diameter, extending about 2/3 of the dish radius towards the center of the dish. This trench serves as a bed for the glass capillary inserted through the capillary mounting hole. The trench is extended by a second, shallower trench whose bottom is elevated with respect to the deeper trench by the thickness of the capillary glass wall. The second trench serves as a bed for the agarose column which is pushed out of the capillary by a tightly fitted plunger (not shown). The teflon dish is equipped on one side with a plastic window enabling visual inspection of the sample and the objective lens.

For imaging, the capillary with the sample embedded in agarose containing appropriate amount of fluorescent beads was inserted into the capillary mounting hole until it reached the end of the capillary bed. The teflon dish was filled with water and the agarose was pushed out of the capillary into the agarose bed by the plunger. Water dipping objective was lowered into the dish and focussed on the ''Drosophila''  embryo specimen in agarose. A confocal stack was acquired using variety of optical sectioning techniques (spinning disc confocal ([[Media:Rotation_chamber.png|Figure&nbsp;7]]), single photon confocal (see [[Media:Supplementary_Video_3_Global_Opt_with_Tiling.mov‎|Video&nbsp;3]]), two photon confocal, apotome (data not shown). Next, to achieve multi-view acquisition, the agarose column was retracted into the capillary by the plunger and the capillary was manually rotated. The angle of the rotation was only very roughly estimated by the position of a tape piece attached to the capillary. The agarose was again pushed out into the agarose bed and another confocal stack was collected. In this way arbitrary number of views can be collected as long as the sample does not bleach.

==Implementation==

[[Image:Screenshot.png|thumb|right|300px|<b>Figure&nbsp;8:</b> Screenshot of SPIM registration plugin in Fiji]]
The bead-based registration framework is implemented in the Java programming language and provided as a fully open source plugin packaged with the ImageJ distribution [[Fiji]] (Fiji Is Just ImageJ, that is actively developed by an international group of developers. The plugin ([[Media:Screenshot.png|Figure&nbsp;8]]) performs all steps of the registration pipeline: bead segmentation, correspondence analysis of bead-descriptors, outlier removal (RANSAC and global regression), global optimization including optional visualization, several methods for fusion, blending and time-lapse registration.

The tutorial on how to use the plugin in basic and advanced mode is available at [[SPIM Registration]]. The test data containing 7-view SPIM acquisitions of ''Drosophila''  embryo can be downloaded from [http://fly.mpi-cbg.de/preibisch/nm/HisYFP-SPIM.zip].

==Acknowledgments==

We want to thank [http://www.zeiss.de/micro Carl Zeiss Microimaging] for access to the SPIM demonstrator, Radoslav Kamil Ejsmont<ref group="A" name="MPI-CBG">Max Planck Institute of Molecular Cell Biology and Genetics, Dresden, Germany</ref> for His-YFP flies, Dan White,<ref group="A" name="MPI-CBG" />, Jonathan Rodenfels,<ref group="A" name="MPI-CBG" /> Ivana Viktorinova,<ref group="A" name="MPI-CBG" /> Mihail Sarov,<ref group="A" name="MPI-CBG" /> Steffen Jänsch,<ref group="A" name="MPI-CBG" /> Jeremy Pulvers,<ref group="A" name="MPI-CBG" /> and Pedro Campinho<ref group="A" name="MPI-CBG" /> for providing various biological samples for imaging with SPIM shown in [[Media:Showcase.jpg|Figure&nbsp;6]].

<references group="A" />

== References ==

<references />

[[Category:Plugins]]
[[Category:Registration]]
