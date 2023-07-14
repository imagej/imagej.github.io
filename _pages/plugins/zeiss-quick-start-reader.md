---
title: Zeiss Quick Start Reader
artifact: ch.epfl.biop:quick-start-czi-reader
nav-links: true
toc: true
---

The ZeissQuickStartCZIReader is an alternative to the default ZeissCZIReader provided by Bio-Formats. 
It is a major rewrite to the original one, the rewrite aiming at increasing the speed of the reader initialisation, which was too slow for files that contains a lot of planes, typically lattice light-sheet dataset.

It can be enabled in a two step procedure:
- activating the `Zeiss Quick Start Reader` update site
- and by enabling this reader in `Bio-Formats Plugins Configuration > Formats > Zeiss CZI (Quick Start)`.
