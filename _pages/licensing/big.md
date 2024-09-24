---
title: BIG Licensing
section: Contribute:Licensing:Open Source
---

{% include notice icon="info" content='For a summary of [SciJava](/libs/scijava) licensing, see the [Licensing](/licensing) page.' %} 

Components distributed via the [BIG-EPFL update site](/update-sites/big-epfl) were developed by the [Biomedical Imaging Group](https://bigwww.epfl.ch/) (BIG) at the [École Polytechnique Fédérale de Lausanne](http://epfl.ch/) (EPFL).

## List of BIG components

The following components are expressly or implicitly licensed according to the [GNU General Public License v3](/licensing/gpl#gnu-general-public-license-v3) (GPLv3):

| **Project**                                                     | **License text**                                                    |
|-----------------------------------------------------------------|---------------------------------------------------------------------|
| **[Differentials](/plugins/differentials)**                     | [GPLv3+](https://bigwww.epfl.ch/thevenaz/differentials/#LegalBlurb) |
| **[Extended Depth of Field](/plugins/extended-depth-of-field)** | [Proprietary](https://bigwww.epfl.ch/demo/edf/)                     |
| **imageware**                                                   | Implicit                                                            |
| **[MIJ](/plugins/miji)**                                        | [Proprietary](https://bigwww.epfl.ch/sage/soft/mij/#term)           |
| **[MosaicJ](/plugins/mosaicj)**                                 | [GPLv3+](https://bigwww.epfl.ch/thevenaz/mosaicj/#LegalBlurb)       |
| **[PointPicker](/plugins/point-picker)**                        | Implicit                                                            |
| **[Shepp-Logan Phantom](/plugins/shepp-logan-phantom)**         | [GPLv3+](https://bigwww.epfl.ch/thevenaz/shepplogan/#LegalBlurb)    |
| **[Snakuscule](/plugins/snakuscule)**                           | [GPLv3+](https://bigwww.epfl.ch/thevenaz/snakuscule/#LegalBlurb)    |
| **[StackReg](/plugins/stackreg)**                               | [GPLv3+](https://bigwww.epfl.ch/thevenaz/stackreg/#LegalBlurb)      |
| **[TurboReg](/plugins/turboreg)**                               | [GPLv3+](https://bigwww.epfl.ch/thevenaz/turboreg/#LegalBlurb)      |
| **[UnwarpJ](/plugins/unwarpj)**                                 | [Proprietary](https://bigwww.epfl.ch/thevenaz/UnwarpJ/#LegalBlurb)  |
| **wavelets**                                                    | Implicit                                                            |

Note that components above labeled "proprietary" currently still have old non-open-source license terms on their respective websites, but the copyright holders have expressed their intent to open-source them; see below for details.

## Transition to open-source licensing

Until April 2023, these components were licensed under proprietary terms, incompatible with the [GPL](/licensing/gpl) and similar licenses, with [Fiji](/software/fiji) having been granted special permission to redistribute them:

> Date: Mon, 26 Jul 2010 10:58:20 +0200  
> From: Michael Unser
>
> [...] we are happy that Fiji distributes our software: you have
> my formal authorization for this (in my quality of lab chief).
> "You'll be free to use this software for research purposes,  but you
> must not transmit and distribute it without our consent":  this means
> that from now on, you are authorized to distribute any ImageJ pluging
> listed at https://bigwww.epfl.ch/algorithms.html since you have our
> consent.

Fortunately, the plugins have since been updated to use an [open-source](https://imagej.net/licensing/open-source) license: the [GPLv3](/licensing/gpl#gnu-general-public-license-v3):

> Date: Mon, 3 Apr 2023 10:54:54 +0000
> From: Michaël Unser  
> Subject: BIG's plugins for FIJI / licenses
>
> [...] I am pleased to confirm that all of our software are
> open-source, in line with the FAIR principles promoted by EPFL. Our
> licensing follows the GPLv3 and we are currently updating our terms to
> reflect this.
>
> In addition, we also strongly encourage users to properly cite our
> research papers in any publications that make use of our software.
