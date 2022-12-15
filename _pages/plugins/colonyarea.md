---
title: ColonyArea
description: ImageJ-plugin that is optimized to perform standard analysis of colony formation assays conducted in 6- to 24-well dishes.
categories: [Segmentation]
doi: 10.1371/journal.pone.0092444

name: ColonyArea
initial-release-date: "2014"
team-founder: "@turkubioimaging"
team-maintainer: '@turkubioimaging'
support-status: Active
source-label: GitHub
source-url: https://github.com/Turku-BioImaging/ColonyArea
---


<p float='left'>
    <img src='images/ColonyArea-Figure1.jpg' style="height:125px;width:auto;"/>
    <img src='images/ColonyArea-Figure4.jpg' style="height:125px;width:auto;margin-left:15px;"/>
    <img src='images/ColonyArea-Figure7.png' style="height:125px;width:auto;margin-left:15px;"/>
</p>

# ColonyArea ImageJ plugin
[![DOI:10.1371/journal.pone.0092444](http://img.shields.io/badge/DOI-10.1371/journal.pone.0092444-00AEEF.svg)](https://doi.org/10.1371/journal.pone.0092444)

**Camilo Guzmán<sup>1,2</sup>, Manish Bagga<sup>1,2</sup>, Amanpreet Kaur<sup>1</sup>, Jukka Westermarck<sup>1</sup>, and Daniel Abankwa<sup>1</sup>**

<sup>1</sup>Turku Bioscience, University of Turku, Åbo Akademi University  
<sup>2</sup>Equal contribution


## Abstract:

Clonogenic assays measure the survival and growth of a single mammalian cell into a colony. These colony or focus formation assays are widely used in radiation biology and cancer biology, where they are employed to study resistance of cancer cells to radiation or the transforming potential of genes, respectively.

We have developed _ColonyArea_, an ImageJ-plugin that is optimized to perform standard analysis of colony formation assays conducted in 6- to 24-well dishes. The plugin processes each well individually and determines not the colony number, but the area of the well covered with cells, also taking the intensity into account.

## Installation

_ColonyArea_ can be installed either through Fiji Update Sites or manually.

### Fiji Update Site (recommended)

In the Fiji menu, go to _Help -> Update... -> Manage update sites_ and select the _ColonyArea_ site. Click _Close_ then _Apply Changes_. Restart Fiji. In the _Plugins_ dropdown of the Fiji menu, _ColonyArea_ should now be available.

### Manual install

Download the [latest release](https://github.com/Turku-BioImaging/ColonyArea/releases) from the repository. Copy the following files to your Fiji plugins directory:

- Colony_area.class
- Colony_measurer.ijm
- Colony_thresolder.ijm
- Manual_colony_thresholder.ijm

Restart Fiji. In the _Plugins_ dropdown of the Fiji menu, _ColonyArea_ should now be available.

## Usage

Detailed usage instructions and examples [here](https://github.com/Turku-BioImaging/ColonyArea/blob/main/USAGE.md).

Sample image files used in the manual can be downloaded [here](https://b2share.eudat.eu/records/39fa39965b314f658e4a198a78d7f6b5).

## Citation

If you use this tool, please cite this paper:

```
Guzmán C, Bagga M, Kaur A, Westermarck J, Abankwa D.
ColonyArea: an ImageJ plugin to automatically quantify colony formation in clonogenic assays.
PLoS One. 2014 Mar 19;9(3):e92444. doi: 10.1371/journal.pone.0092444. PMID: 24647355; PMCID: PMC3960247.
```

### Bibtex

```
@article{Guzman_ColonyArea_An_ImageJ_2014,
author = {Guzmán, Camilo and Bagga, Manish and Kaur, Amanpreet and Westermarck, Jukka and Abankwa, Daniel},
doi = {10.1371/journal.pone.0092444},
journal = {PloS ONE},
month = {3},
number = {3},
title = {{ColonyArea: An ImageJ plugin to automatically quantify colony formation in clonogenic assays}},
volume = {9},
year = {2014}
}
```

## Maintenance

Beginning in October 2022, maintenance of this plugin is handled by [Turku BioImaging](https://bioimaging.fi), a broad-based, interdisciplinary science and infrastructure umbrella that aims to unite bioimaging expertise in Turku and elsewhere in Finland. Turku BioImaging is jointly operated by the [University of Turku](https://utu.fi) and [Åbo Akademi University](https://abo.fi).

For more information and support, email [image-data@bioimaging.fi](mailto:image-data@bioimaging.fi)

