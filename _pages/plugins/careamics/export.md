---
title: Noise2Void Model Export

nav-links:
- title: Overview
  url: /plugins/careamics/index
- title: Training
  url: /plugins/careamics/training
- title: Prediction
  url: /plugins/careamics/prediction
- title: Export
  url: /plugins/careamics/export
---

<img src="/media/plugins/careamics/export.png" alt="Training tab" height="460px" align="right">

<br>

- **Export as PyTorch Lightning Checkpoint**: export the trained model as a PyTorch Lightning checkpoint file (*.ckpt).

- **Export as Bioimage.io Model**: export the trained model in the BioImage.io model format, which includes additional metadata.

CAREamics is a partner of the [BioImage.io model zoo](https://bioimage.io/#/models) and contributes models to the community. You can export your trained models to the BioImage.io model format by filling out the required information in the export dialog.

<img src="/media/plugins/careamics/bmz.png" alt="Export tab" height="680px">

{% include notice icon="tip" 
    content="You can load the exported models back into CAREamics using python code. Check the CAREamics [documentation](https://careamics.github.io/latest/content/guides/current/careamist_predicting/) for details."
%}
