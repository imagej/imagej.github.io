---
title: 2015-04-15 - ImageJ 2.0.0-rc-29, plus Bio-Formats 5.1.0 in Fiji
---

Today, the [ImageJ team](/people) has made a new release of [ImageJ2](/software/imagej2): version 2.0.0-rc-29. This release includes bug-fixes and improvements by several members of the ImageJ community.

In addition, the [Fiji team](/people) has updated several components of the [Fiji](/software/fiji) distribution. Notably, Fiji was updated to the [Bio-Formats](/formats/bio-formats) 5.1.0 release, which includes many bug-fixes and improvements to several file formats.

## What's new

These releases include new versions of several components:

| [SciJava](https://github.com/scijava) | [ImageJ](https://github.com/imagej) | [Fiji](https://github.com/fiji) |
|---|---|---|
| [scijava-plugins-commands-0.2.0](https://github.com/scijava/scijava-plugins-commands/compare/scijava-plugins-commands-0.1.8...scijava-plugins-commands-0.2.0)<br /> [scijava-ui-swing-0.6.0](https://github.com/scijava/scijava-ui-swing/compare/scijava-ui-swing-0.5.0...scijava-ui-swing-0.6.0)<br /> [scripting-java-0.3.1](https://github.com/scijava/scripting-java/compare/scripting-java-0.3.0...scripting-java-0.3.1) | [ij1-patcher-0.12.1](https://github.com/imagej/ij1-patcher/compare/ij1-patcher-0.12.0...ij1-patcher-0.12.1)<br /> [imagej-2.0.0-rc-29](https://github.com/imagej/imagej/compare/imagej-2.0.0-rc-28...imagej-2.0.0-rc-29)<br /> [imagej-common-0.14.0](https://github.com/imagej/imagej-common/compare/imagej-common-0.13.0...imagej-common-0.14.0)<br /> [imagej-ops-0.11.0](https://github.com/imagej/imagej-ops/compare/imagej-ops-0.10.0...imagej-ops-0.11.0)<br /> [imagej-plugins-commands-0.5.0](https://github.com/imagej/imagej-plugins-commands/compare/imagej-plugins-commands-0.4.1...imagej-plugins-commands-0.5.0)<br /> [imagej-ui-swing-0.11.1](https://github.com/imagej/imagej-ui-swing/compare/imagej-ui-swing-0.11.0...imagej-ui-swing-0.11.1)<br /> [imagej-updater-0.7.3](https://github.com/imagej/imagej-updater/compare/imagej-updater-0.7.2...imagej-updater-0.7.3) | [scifio-bf-compat-2.0.0](https://github.com/scifio/scifio-bf-compat/compare/scifio-bf-compat-1.11.0...scifio-bf-compat-2.0.0)<br /> [scifio-cli-0.3.2](https://github.com/scifio/scifio-cli/compare/scifio-cli-0.3.1...scifio-cli-0.3.2)<br /> [scifio-hdf5-0.1.1](https://github.com/scifio/scifio-hdf5/compare/scifio-hdf5-0.1.0...scifio-hdf5-0.1.1)<br /> [scifio-ome-xml-0.13.0](https://github.com/scifio/scifio-ome-xml/compare/scifio-ome-xml-0.12.0...scifio-ome-xml-0.13.0)<br /> [legacy-imglib1-1.1.4-DEPRECATED](https://github.com/fiji/legacy-imglib1/compare/c475242394a7f59a4d857fe71d29068c611e3211...legacy-imglib1-1.1.4-DEPRECATED)<br /> [Stitching\_-3.0.2](https://github.com/fiji/Stitching/compare/64bab29dfdc4d0bdcd014df7384f18077730400d...Stitching_-3.0.2)<br /> [SPIM\_Registration-2.1.10](https://github.com/bigdataviewer/SPIM_Registration/compare/SPIM_Registration-2.1.9...SPIM_Registration-2.1.10) |

### What's new in ImageJ

-   Joe Hsiao fixed a bug with boolean parameters in headless mode ({% include github org='imagej' repo='ij1-patcher' pr='36' label='ij1-patcher\#36' %}).
-   Brian Northan improved deconvolution and FFT code in [ImageJ Ops](/libs/imagej-ops) ({% include github org='imagej' repo='imagej-ops' pr='114' label='imagej-ops\#114' %}).
-   Jan Eglinger added a small enhancement to the Manage Update Sites dialog UI ({% include github org='imagej' repo='imagej-ui-swing' pr='38' label='imagej-ui-swing\#38' %}).
-   Jan Eglinger and Curtis Rueden improved the Console to scroll to the bottom to follow any new output ({% include github org='scijava' repo='scijava-ui-swing' pr='8' label='scijava-ui-swing\#8' %}).
-   Stephan Saalfeld fixed a problem with the Console where it stole the focus ({% include github org='scijava' repo='scijava-ui-swing' pr='9' label='scijava-ui-swing\#9' %}, {% include github repo='fiji' issue='118' label='fiji\#118' %}).
-   Curtis Rueden fixed bugs in [ImageJ2](/software/imagej2)'s About dialog box (\[{% include github org='imagej' repo='imagej-common' commit='d0ec5d8b4659670ee51c0127ccfe8dc7d4a70b08' label='1' %}\], \[{% include github org='imagej' repo='imagej-common' commit='738b165cfb41bf473ab3e1233149b8a07731993c' label='2' %}\], \[{% include github org='imagej' repo='imagej-common' commit='286e0771291a9faaf51b7c08c758d302e5e2124f' label='3' %}\]), thanks to Vaughn Miller's {% include github repo='fiji' issue='115' label='bug report' %}.
-   Mark Hiner added an option to toggle min/max computation in [SCIFIO](/libs/scifio)'s {% include bc path='File | Import | Image...'%} command ({% include github org='imagej' repo='imagej-plugins-commands' issue='23' label='imagej-plugins-commands\#23' %}).
-   Curtis Rueden fixed a critical bug when running Java code in the [Script Editor](/scripting/script-editor) ({% include github org='scripting' repo='scripting-java' commit='1e9c9fd2906c54def1adeb59c2197954db698d69' label='scripting-java@1e9c9fd2' %}).

### What's new in Fiji

-   Curtis Rueden updated Fiji to the [Bio-Formats](/formats/bio-formats) 5.1.0 release. Relevant components ({% include github org='bigdataviewer' repo='SPIM_Registration' commit='e272ba84733b8ac0e1fcb7bea89a84ec568c0a35' label='SPIM\_Registration' %}, {% include github org='fiji' repo='legacy-imglib1' commit='27a1c3c5ac9e63660b68012ee3057e8790f07975' label='legacy-imglib1' %}, {% include github org='fiji' repo='Stitching' commit='171cc57b10bdd89ee8e0236e29281b090b9498b1' label='Stitching' %}, {% include github org='scifio' repo='scifio-bf-compat' commit='c74fcce71569c2090be65bf0fdae47d2196fc8c3' label='scifio-bf-compat' %} and {% include github org='scifio' repo='scifio-ome-xml' commit='aed9fd332dd7281793ded91d9c4960af13a4017b' label='scifio-ome-xml' %}) now use the Bio-Formats 5.1 API.
-   Stephan Preibisch, Tobias Pietzsch and Peter Steinbach improved and fixed bugs in [SPIM Registration](/plugins/spim-registration).

## How to update

Use the {% include bc path='Help | Update...'%} command to update your [ImageJ](/software/imagej) installation. Please send any comments to the [ImageJ mailing list](/discuss/mailing-lists). Thanks for the continued feedback and support!

  
