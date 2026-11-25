---
title: Noise2Void Prediction

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

<div style="
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
">
  <div>
    <h3>Model Checkpoint</h3>
    <ul>
      <li><b>From Trained Model</b>: to use the model that you just trained</li>
      <li><b>Load Model from Disk</b>: to load a previously trained model from disk</li>
    </ul>

    <div>
    <h3>Data</h3>
    As during training, you can select an image from those already opened in Fiji, or you can select image(s) from disk.
    {% include notice class="fa fa-exclamation-circle"
        content="If you selected files from the disk, then the results will be saved on disk as well."
    %}
    </div>

    <h3>Configuration</h3>
    <ul>
      <li><b>Tile Prediction</b>: if checked, the prediction will happen tile-by-tile, instead of over the whole image at once. Necessary when the data is too large to fit in memory</li>
      <li><b>XY Tile Size</b>: prediction tile size in X and Y</li>
      <li><b>3D Prediction</b>: whether the data and the model are 3D</li>
      <li><b>Z Tile Size</b>: tile size in Z dimension</li>
      <li><b>Batch Size</b>: number of tiles to predict on at each iteration (use a low number for small GPUs)</li>
    </ul>
  </div>

  <div style="display: block; max-width: 100%;">
    <img src="/media/plugins/careamics/prediction.png" alt="Prediction tab" height="700px">
  </div>
  <div style="clear: both"></div>

</div>
