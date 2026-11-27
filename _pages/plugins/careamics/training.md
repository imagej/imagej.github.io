---
title: Noise2Void Training

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
    <p>
    Noise2Void is self-supervised, meaning that it trains on the noisy data itself without requiring clean target data. It relies on a classical UNet architecture, and applies a special augmentation called <i>N2V manipulate</i> that replaces the value of randomly-selected pixels with the value of one of their neighbours.
    </p>

    <h3>Data</h3>
    <p>In this section you can select the data for training from any images that already opened in Fiji, or you can select a file or a folder containing images.  
    </p>
    {% include notice icon="tip" 
        content="You can also, select a `zarr` dataset (folder) as for the training data."
    %}

    <h3>Configuration</h3>
    <ul>
      <li><b>Experiment Name</b>: the name of experiment (mandatory for <code>CAREamics</code>)</li>
      <li><b>Input Axes</b>: to select the input image(s) axes, necessary to correctly reshape the data</li>
      <li><b>XY Patch Size</b>: the training patch size in X and Y</li>
      <li><b>3D Patching</b>: whether the data is 3D.</li>
      <li><b>Z Patch Size</b>: the patch size in the Z dimension</li>
      <li><b>Batch Size</b>: training batch size (use a small number if you have a GPU with a small memory)</li>
      <li><b>Number of Epochs</b>: the number of iterations that the model will be trained over</li>
      <li><b>Number of Steps</b>: the number of steps (batches) for each epoch (ignored if larger than the number of available batches)</li>
      <li><b>Use n2v2</b>: whether to use the Noise2Void v2 training strategy</li>
    </ul>

    <p>After setting the configuration, hit the "<b>Train</b>" button to start the training process.
    </p>

    {% include notice class="fa fa-exclamation-circle"
        content="If you are using the plugin for the first time, before the training begins, a python environment will be created using [`uv`](https://docs.astral.sh/uv/), which will take a few minutes."
    %}

    <p>
    You can stop the training process by hitting the <b>"Stop"</b> button.<br>
    The details of the training process will be logged into the plugin's logging window.
    </p>

    {% include notice icon="tip" 
        content="The training is better suited for **GPU** and it supports macOS silicon chips as well. 
        You can also use **CPU** for training, but it will be significantly *slower*."
    %}
  
  </div>

  <div style="display: block; max-width: 100%;">
    <img src="/media/plugins/careamics/training.png" alt="Training tab" height="700px">
  </div>

</div>
