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
      <li><b>From Trained Model</b>: for using the model that you just trained</li>
      <li><b>Load Model from Disk</b>: for loading a trained model from disk</li>
    </ul>

    <div>
    <h3>Data</h3>
    Like Training, you can select an image from those already opened in Fiji, or you can select image(s) from disk.
    {% include notice class="fa fa-exclamation-circle"
        content="If images for prediction, were selected from the disk, then the results will be saved on disk as well."
    %}
    </div>

    <h3>Configuration</h3>
    <ul>
      <li><b>Tile Prediction</b>: if checked, the prediction will happen tile-by-tile, instead of over the whole image at once.</li>
      <li><b>XY Tile Size</b>: the prediction tile size</li>
      <li><b>3D Prediction</b>: check this for 3D data prediction.</li>
      <li><b>Z Tile Size</b>: tile size in Z dimesion</li>
      <li><b>Batch Size</b>: sets how many image (or tiles) at a time.</li>
    </ul>
  </div>

  <div style="display: block; max-width: 100%;">
    <img src="/media/plugins/careamics/prediction.png" alt="Prediction tab" height="700px">
  </div>
  <div style="clear: both"></div>

</div>