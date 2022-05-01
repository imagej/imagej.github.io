---
mediawiki: CSIMLab
title: CSIMLab
section: Contribute:Organizations
categories: [Filtering,Noise]
extensions: ["mathjax"]
---


{% capture author%}
{% include person id='acsenrafilho' %} ([1](mailto:acsenrafilho@gmail.com))
{% endcapture %}

{% capture maintainer%}
{% include person id='acsenrafilho' %}
{% endcapture %}

{% capture source%}
{% include github org='CSIM-Toolkits' repo='ImageJ' label='GitHub CSIM-ImageJ repository' %}
{% endcapture %}
{% include info-box name='CSIM Laboratory ImageJ' software='Fiji' author=author maintainer=maintainer source=source released='February 01<sup>st</sup>, 2015' latest-version='February 01<sup>st</sup>, 2015' status='experimental, active' category='Plugins, Filtering, Noise' %}== Purpose ==

Promote plugins, macros and scripts created by the Computing in Signal and Image in Medicine research group (CSIM). All the code implemented here have a specific applications, where are related with the basic image analysis such as image filtering, registration, feature extraction and others. Please, be free to install our plugins, macros and scripts from the ImageJ Updater or even contribute with our codes on GitHub repository ({% include github org='CSIM-Toolkits' repo='ImageJ' label='GitHub CSIM-ImageJ repository' %}).

{% include thumbnail src='/media/icons/csim.png' title='CSIM Laboratory. See more details about our research group in the website: http://dcm.ffclrp.usp.br/csim'%}

## Available Methods

Here is a list of the available methods for ImageJ. If you want use any of these methods, please see the CSIM Laboratory option in the Update manager menu.

### Anomalous Filters

A PlugInFilter for the two different methods for image filtering: Anisotropic Anomalous Diffusion and Isotropic Anomalous Diffusion. Both methods description can be found in the Physics in Medicine and Biology [journal article](http://doi.org/10.1088/0031-9155/60/6/2355), which is also referenced in [wiki page](/plugins/anomalous-diffusion-filters). In summary, both image filter are discrete solution of generalized diffusion heat equation (also know as a porous media equation).

Please, see our reference articles to find out more details about the parameters necessary to run properly the anomalous diffusion filters.

### Perfusion Metrics in MRI

In this specific PlugInFilter we offer a tool to measure the main parameters involved in Dynamic Perfusion MRI images such as: Time to peak, Peak, CBV and CBF values. It could be useful in medical studies where are used contrast dynamic enhanced perfusion images. Here we only create a simple implementation for these metrics and more detailed approach should be implemented in a near future.

Please see the [Perfusion MRI wiki page](/plugins/mri-perfusion) for this specific method.

### Noise Generator

In this specific PlugIn we offer a tool to add different noise on a image with several different probability distributions, where could be useful in some biological and medical studies. Some noise probability examples are the Uniform, Gaussian, Rayleigh and Colored noises (Brown, Pink, Blue and other $$1/f^\beta$$ noises).

See the [Noise Generator wiki page](/plugins/noise-generator) to find out more information about this PlugIn.

### Sample Entropy 2D (SampEn2D)

In this PlugIn we offer a tool to calculate the two-dimensional sample entropy (SampEn2D) on digital image.

See the [SampEn2D wiki page](/plugins/sampen2d) to find out more information about this PlugIn.

## Source code

The ImageJ plugins source codes are available on GitHub repository: {% include github org='CSIM-Toolkits' repo='ImageJ' label='GitHub-ImageJ source codes' %}. If you want contribute with our applications, please enter in contact.

## Who we are

We are a computational laboratory dedicated with biomedical image and signal processing and analysis. Our group is held in the Ribeirão Preto city, São Paulo state, Brazil. Our research group works directly with several applications related to image and signal issues, namely registration, tissue segmentation, filtering, analysis and feature extraction. Also, our goal is to improve and create suitable tools for image and signal applications in medical and biological research. Please, see the reference articles cited here in this wiki to see some of our publications. If you want to know more about our group and research opportunities, be free to enter in contact with us in our [website](http://dcm.ffclrp.usp.br/csim)

## Publications

Here it will be found some publications of our research group with respect the image processing methods developed in our laboratory. If you used any of these methods, please cite the published articles bellow.

### Journal Articles

#### Anomalous Diffusion Filters

-   Da S Senra Filho, A.C., Salmon, C.E.G. & Junior, L.O.M., 2015. Anomalous diffusion process applied to magnetic resonance image enhancement. Physics in Medicine and Biology, 60(6), p.2355. DOI: 10.1088/0031-9155/60/6/2355.

#### SampEn2D

-   Silva, L. E. V. ; Senra Filho, A. C. da S. ; Fazan, V. P. S. ; Felipe, J. C. ; Murta Junior, L. O., 2016. Two-dimensional sample entropy: assessing image texture through irregularity. Biomedical Physics & Engineering Express

### Procedings

#### Anomalous Diffusion Filters

-   Filho, A.C. da S.S., Junior, L.O.M. & Santos, A.C. dos, 2014. Anisotropic Anomalous Filter Applied to Multimodal Magnetic Resonance Image in Multiple Sclerosis. In I Transatlantic Workshop on Methods for Multimodal Neurosciences Studies. São Pedro, SP.

<!-- -->

-   Filho, A.C. da S.S. et al., 2014. Brain Activation Inhomogeneity Highlighted by the Isotropic Anomalous Diffusion Filter. In Annual International Conference of the IEEE Engineering in Medicine and Biology Society. Chicago: IEEE, pp. 3313–3316. Available at: http://ieeexplore.ieee.org/lpdocs/epic03/wrapper.htm?arnumber=6944331

<!-- -->

-   Filho, A.C. da S.S. et al., 2014. Anisotropic Anomalous Diffusion Filtering Applied to Relaxation Time Estimation in Magnetic Resonance Imaging. In Annual International Conference of the IEEE Engineering in Medicine and Biology Society. IEEE, pp. 3893–3896. Available at: http://ieeexplore.ieee.org/lpdocs/epic03/wrapper.htm?arnumber=6944474

<!-- -->

-   Filho, A.C. da S.S., Barizon, G.C. & Junior, L.O.M., 2014. Myocardium Segmentation Improvement with Anisotropic Anomalous Diffusion Filter Applied to Cardiac Magnetic Resonance Imaging. In Annual Meeting of Computing in Cardiology. Available at: http://www.cinc.org/archives/2014/pdf/0929.pdf
-   Filho, A.C. da S.S. et al., 2014. Brain Activation Inhomogeneity Highlighted by the Isotropic Anomalous Diffusion Filter. In Annual International Conference of the IEEE Engineering in Medicine and Biology Society. Chicago: IEEE, pp. 3313–3316. Available at: http://ieeexplore.ieee.org/lpdocs/epic03/wrapper.htm?arnumber=6944331

<!-- -->

-   Senra Filho, A.C. da S., Duque, J.J. & Murta, L.O., 2013. Isotropic anomalous filtering in Diffusion-Weighted Magnetic Resonance Imaging. I. E. in M. and B. Society, ed. Conference proceedings : ... Annual International Conference of the IEEE Engineering in Medicine and Biology Society. IEEE Engineering in Medicine and Biology Society. Conference, 2013, pp.4022–5. Available at: http://ieeexplore.ieee.org/lpdocs/epic03/wrapper.htm?arnumber=6610427

#### SampEn2D

-   Silva, L.E.V. da et al., 2014. Two-dimensional sample entropy analysis of rat sural nerve aging. In Annual International Conference of the IEEE Engineering in Medicine and Biology Society. IEEE, pp. 3345–3348. Available at: http://ieeexplore.ieee.org/lpdocs/epic03/wrapper.htm?arnumber=6944339 \[Accessed December 9, 2014\].

#### Other Journal and Proceeding Publications

-   Senra Filho, A.C. da S. et al., 2014. A computational tool as support in B-mode ultrasound diagnostic quality control. Revista Brasileira de Engenharia Biomédica, 30, pp.402–405. Available at: http://www.scielo.br/scielo.php?script=sci_arttext&pid=S1517-31512014000400010&lng=en&nrm=iso&tlng=en.

<!-- -->

-   Barizon, G.C. et al., 2014. Tissue characterization from myocardial perfusion and autonomic innervation using MRI and SPECT images in Chagas disease. In Annual Meeting of Computing in Cardiology. Cambrigde.
