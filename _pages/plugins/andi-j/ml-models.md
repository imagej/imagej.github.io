---
title: AnDi-J › ML models
name: AnDi-J
icon: /media/plugins/andi-j/logo.png
description: The deep-learning models bundled with AnDi-J, the ONNX contract they follow, and how to plug in your own models.
nav-title: ML models
nav-links:
- title: Overview
  url: /plugins/andi-j
- title: Input data
  url: /plugins/andi-j/input-data
- title: Trajectory Analysis
  url: /plugins/andi-j/trajectory-analysis
- title: Trajectory Segmentation
  url: /plugins/andi-j/trajectory-segmentation
- title: ML models
  url: /plugins/andi-j/ml-models
---

AnDi-J uses deep-learning models at different levels:

*   [Trajectory Analysis](/plugins/andi-j/trajectory-analysis) — ML is optional for computing the anomalous exponent *α* and required for predicting the diffusion model.
*   [Trajectory Segmentation](/plugins/andi-j/trajectory-segmentation) — all predictions here are made with ML models: per-frame *α*, log₁₀(*D*), diffusive state and change-point detection along each trajectory.

Both tasks come with bundled default models that work out of the box. You can also use your own models for any of the tasks above (see [Custom models for Trajectory Analysis](#custom-models-for-trajectory-analysis) and [Custom models for Trajectory Segmentation](#custom-models-for-trajectory-segmentation)).

{% include notice icon="info" content="Benchmark your custom models with this [online tool](https://gorkamunoz.github.io/andi-j/)." %}

## Bundled models

Two models ship with AnDi-J:

| Model | Used in | Output | Reference |
|---|---|---|---|
| **andi-j-analysis** | Anomalous exponent (ML), Diffusion Model | one *α* per trajectory **and** the diffusion-model class (two networks in one model file) | Based on the convolutional networks of [Granik et al. (2019)](https://doi.org/10.1016/j.bpj.2019.06.015). |
| **andi-j-segmentation** | Trajectory Segmentation | per-frame *α*, *D* and diffusive state, plus change points | Based on [U-AnD-ME](https://iopscience.iop.org/article/10.1088/2515-7647/adf9aa). |

Inference runs on **CPU** or **GPU**. See [Installation](/plugins/andi-j#installation) for details.

### andi-j-analysis

Two convolutional networks with the same architecture, after [Granik et al. (2019)](https://doi.org/10.1016/j.bpj.2019.06.015): five parallel blocks of dilated causal convolutions, max-pooled over time and followed by dense layers. One predicts the **anomalous exponent α** as a probability distribution over the 40 values 0.05, 0.10, …, 2.00; the other the **diffusion-model class** (ATTM, CTRW, FBM, LW, SBM). Both ship in a single `.onnx` file that follows the same input contract as custom models (raw `(1, T, 2)` positions) and returns two outputs, `alpha` `(1, 1)` and `model` `(1, 5)`.

Inside the model, each trajectory is:

1.  cut to its last 1000 positions and shifted to start at the origin;
2.  zero-padded at the front, turned into displacements and divided by the mean step size;
3.  run through both networks for the 8 symmetric views of the trajectory (sign flips of *x* and *y*, and swapping *x* and *y*), whose probabilities are averaged;
4.  read out: *α* is the median of the exponent distribution; the class scores of ATTM and CTRW are multiplied by the probability that *α* ≤ 1, and that of LW by the probability that *α* > 1.

On the 2D trajectories of the 1st AnDi Challenge benchmark it reaches an *α* MAE of 0.137 and a classification F1 of 0.892, above every challenge participant in both tasks. Compute grows with the trajectory length, and the plugin runs one trajectory per CPU core in parallel (on an 8-core CPU, about 35 ms per trajectory for lengths of 10–400 frames).

### andi-j-segmentation

A 1-D **U-Net 3+** ([U-AnD-ME](https://iopscience.iop.org/article/10.1088/2515-7647/adf9aa)): an encoder–decoder with full-scale skip connections (6 depth levels) on the trajectory's displacements, with dedicated heads for *α* (including a temporal branch of dilated convolutions), log₁₀(*D*) and the diffusive state. It follows the same contract as custom models: raw `(1, T, 2)` positions in, every output below out, with all processing inside the model:

*   **Test-time augmentation, always on:** the network runs on the 8 symmetric views of the trajectory (4 rotations × 2 reflections) and the per-frame predictions are averaged, so the result does not depend on the orientation of your data.
*   **Per frame:** *α* (clipped to [0, 1.999]), log₁₀(*D*) and the probabilities of the four diffusive states (0 = immobile, 1 = confined, 2 = free diffusion, 3 = directed); frames with *α* > 1.9 are directed.
*   **Change points:** the local maxima of the change-point probability above 0.32, one flag at the first frame of each new segment.
*   **Segments** (`seg_*` outputs): each segment's *α*, log₁₀(*D*) and diffusive-state probabilities are the **median** over its frames; its state is the most probable one.
*   **Immobile rule:** to improve the detection of immobile trajectories in experimental data, this model assigns the immobile state to every frame and segment with predicted *α* < 0.1.

The plugin runs 4 trajectories at a time in parallel. On an 8-core CPU this takes about 175 ms per trajectory of 10–400 frames; compute grows with the trajectory length.

## What is ONNX (and why)

**ONNX** (Open Neural Network Exchange) is a portable, framework-independent file format for a trained neural network: the graph of operations plus the learned weights, in a single `.onnx` file. It allows you to train in whichever Python framework you like (PyTorch, TensorFlow, scikit-learn…), then *export* the trained model to ONNX.

The bundled models have all been trained using PyTorch. However, AnDi-J runs `.onnx` files with **ONNX Runtime** (the Java build), so at inference time **no Python is needed** — the model runs inside Fiji. This also means that when developing a custom model, you must export it to `.onnx` afterwards. Below you will find how to do that for the different options available.

## Custom models for Trajectory Analysis

AnDi-J ships with a default deep-learning model, but you can plug in **your own** model for either per-trajectory prediction task:

*   **Anomalous exponent** (*Anomalous exponent* tab → **Type: Load**) — a model that predicts the exponent *α* for a trajectory.
*   **Diffusion model classification** (*Diffusion Model* tab → **Type: Load**) — a model that classifies a trajectory into one of the five diffusion models.

{% include notice icon="note" content="
The bundled **Default** model predicts α *and* the diffusion model in one run. A model you **Load** is single-purpose: an α model updates only α; a classifier model updates only the diffusion-model tab.
" %}

### Input

For every trajectory the plugin builds one input tensor and calls your model:

| | |
|---|---|
| **Shape** | `(1, T, 2)` — batch 1, one row per **frame**, two features |
| **Type** | `float32` |
| **Dynamic axis** | the `T` (sequence-length) axis **must be dynamic** |

The two features are the **raw trajectory coordinates**:

*   column `0` = `x`
*   column `1` = `y`

i.e. exactly the (x, y) positions from your loaded data, one row per frame. The plugin feeds these directly — it does **no** preprocessing.

{% include notice icon="info" content="
**Choose your own representation inside the model.** If your method works on displacements, relative-polar features `(dr, dθ)`, images, etc., compute that transform as the first layers of your model (or in the exported graph). That way training and inference stay identical and the plugin's contract stays simple. The bundled *Default* model, for example, shifts each trajectory to the origin and converts it to normalised displacements internally. That choice lives inside the model, not the plugin.
" %}

### Output

**Anomalous-exponent model**

| | |
|---|---|
| **Shape** | `(1, 1)` (or `(1,)`) |
| **Meaning** | the predicted exponent α; the plugin reads element `[0]` |

α should lie in `[0, 2]` (values outside are dropped from the histogram). The α prediction is a single value for the 2D trajectory, so the X / Y component buttons are disabled while ML α results are shown.

**Diffusion-model classifier**

| | |
|---|---|
| **Shape** | `(1, K)` — one score/logit per class |
| **Meaning** | predicted class = `argmax(output)` |

`K = 5` and the class order **must** be:

```
0 = ATTM   1 = CTRW   2 = FBM   3 = LW   4 = SBM
```

(A scalar output `(1, 1)` is accepted too and taken as a rounded class index.)

### Exporting an analysis model to ONNX (PyTorch example)

```python
import torch

model = MyModel()                     # your trained nn.Module
model.load_state_dict(torch.load("my_weights.pth", map_location="cpu"))
model.eval()

dummy = torch.zeros(1, 50, 2)         # (1, T, 2) raw (x, y); 50 is arbitrary here

torch.onnx.export(
    model, dummy, "my_alpha.onnx",
    input_names=["input"],
    output_names=["output"],
    dynamic_axes={"input":  {0: "batch", 1: "seq_len"},   # length must be dynamic!
                  "output": {0: "batch"}},
    opset_version=13,
    do_constant_folding=True,
)
```

The **`dynamic_axes`** entry for the sequence-length axis is essential — trajectories have different lengths, and without it the exported graph is locked to `50`.

{% include notice icon="warning" content="
**Watch out: values derived from the sequence length.** If your `forward` uses the length as a Python integer — e.g. `T = x.shape[1]` then `math.log(T)`, `1/T`, or slicing like `x[:, T//2:]` — the ONNX tracer **bakes those in as constants** for the dummy length, and the model is then wrong for other lengths. Fixes: derive such quantities from the tensor shape at runtime (e.g. build a length tensor with `torch.ones_like(...).sum(dim=1)` and a position index with `torch.cumsum(torch.ones_like(...), dim=1) - 1`, then use masks instead of fixed slices), or expose the extra scalar as an additional model input.
" %}

### Verify an analysis model before loading

Check the exported graph in Python with ONNX Runtime, at **two different lengths**, before loading it in Fiji:

```python
import numpy as np, onnxruntime as ort

sess = ort.InferenceSession("my_alpha.onnx")
for T in (12, 137):                              # different trajectory lengths
    x = np.random.randn(1, T, 2).astype(np.float32)   # (1, T, 2) raw (x, y)
    out = sess.run(["output"], {"input": x})[0]
    print(T, out.shape, out.ravel()[:5])
```

You want the output shape to be `(1, 1)` for an α model or `(1, 5)` for a classifier, and no error at either length.

A ready-made pair of **test models** (an α estimator and a classifier) is provided in `utils/pythons_helpers/make_traj_analysis_test_onnx_models.py`:

```bash
python make_traj_analysis_test_onnx_models.py     # -> test_alpha.onnx, test_model.onnx
```

Use them to confirm the Load path works end-to-end before wiring your own model.

### Loading an analysis model in the plugin

1.  Run **Perform Analysis** so the trajectories are loaded.
2.  Open the relevant tab:
    *   **Anomalous exponent** → set **Type: Load** → **Choose model…** → pick your α `.onnx` → **Compute α**.
    *   **Diffusion Model** → set **Type: Load** → **Choose model…** → pick your classifier `.onnx` → **Compute models (ML)**.
3.  Each runs with a progress bar over the number of trajectories.

Switching **Type** back to **Default** restores the bundled model (which fills both α and the diffusion model, and keeps the two tabs in sync).

## Custom models for Trajectory Segmentation

Trajectory Segmentation can run your own ONNX model(s) instead of the bundled one. Pick **Load** in the *ML model options* box of the [segmentation Data Manager](/plugins/andi-j/input-data#selecting-the-segmentation-model), then either:

*   **Combined model** — one `.onnx` that outputs α, log₁₀(*D*), change points and the diffusive state, and optionally its own segments (see [Model segments](#optional-outputs-segment-level-predictions)), or
*   **Per output** — one `.onnx` per output (**α**, **D**, **Change points**, **Diffusive state**); any of α, D or change points you leave as *default* is produced by the bundled model. The diffusive state is the exception: it is only backed by the bundled model when the bundled model is *already* running for one of the other three; if you supply custom α, D and change-point models and simply leave diffusive state unset, segments get no diffusive state rather than triggering an extra model run just for that. Outputs that come from the bundled model keep its [immobile rule](#andi-j-segmentation).

The plugin does no pre- or post-processing for your model: it feeds the raw trajectory in and reads your outputs out verbatim. Any processing must be added within your `.onnx` file.

### Input: the raw trajectory

| name | shape | dtype | meaning |
|------|-------|-------|---------|
| `input` | `(1, T, 2)` | float32 | raw positions — column 0 = x, column 1 = y, one row per frame |

`T` (the number of frames) is **dynamic** — export the length axis as dynamic so your model accepts any trajectory length. If your architecture needs displacements, a fixed length, or padding, do it **inside** your model.

### Required outputs: per-frame α, log D, change points and diffusive state

All four outputs below are **required**. Each is **per frame**, length `T`, in the same frame order as the input. Shape `(1, T)` or `(1, T, 1)` are both accepted (`(1, T, 4)` for `diffusive_state`, see below).

| output | shape | meaning | used as-is? |
|--------|-------|---------|-------------|
| `alpha` | `(1, T)` | anomalous exponent α per frame | yes, verbatim (the plots cover α in `[0, 2]`) |
| `logD` | `(1, T)` | **log₁₀(D)** per frame | yes, verbatim (use `NaN` for undefined/immobile) |
| `cp` | `(1, T)` | change-point flag per frame, **0 or 1** | the plugin marks a change point at every interior frame where `cp ≥ 0.5` |
| `diffusive_state` | `(1, T, 4)` or `(1, T)` | per-frame diffusive state: either class probabilities over the four states (`0 = immobile, 1 = confined, 2 = free diffusion, 3 = directed`), or the class index directly | `(1, T, 4)` → per-frame `argmax`; `(1, T)` → per-frame rounded value |

Notes:

*   **D must be output as log₁₀(D)**, not linear D — that is exactly what the plugin stores and plots, so nothing is transformed. If a frame has no meaningful D (immobile / trapped), emit `NaN`; it will be shown as a gap and left out of segment means.
*   **`cp` is a 0/1 flag**, one per frame. Frame 0 and the last frame are ignored (they are trajectory ends, not change points). Emit `1` at the first frame of each new segment, and apply whatever peak-picking or thresholding your method needs *inside* the model.
*   **`diffusive_state` is shown per frame** in the *Visualization* tab's state strip, so every predicted state is visible even when it is short-lived.

**Output names.** Name the outputs `alpha`, `logD`, `cp` and `diffusive_state`. If unnamed, the plugin falls back to output order 0 = alpha, 1 = logD, 2 = cp, 3 = diffusive_state. A per-output model exposes a single output and its name does not matter.

### Optional outputs: segment-level predictions

A combined model may also report its own segments, for methods whose segment-level values are not a simple summary of the per-frame ones. The **Model segments** checkbox, shown under **Combined model** in the *ML model options* box and ticked by default, decides how segments are built:

*   **ticked:** the plugin reads the `seg_*` outputs below and uses them verbatim as the segments. `seg_start` and `seg_length` must be present; if either is missing, the plugin derives the segments from `cp` as when unticked.
*   **unticked:** the plugin ignores any `seg_*` output and derives the segments from `cp`, taking each segment's α and log₁₀(D) as the interval mean and its state as the majority vote of the frames it covers.

*Per output* mode always derives the segments from `cp`. `S` is the number of segments and is dynamic.

| output | shape | meaning |
|--------|-------|---------|
| `seg_start` | `(1, S)` | first frame of each segment, 0-based |
| `seg_length` | `(1, S)` | number of frames in each segment |
| `seg_alpha` | `(1, S)` | anomalous exponent α of each segment |
| `seg_logD` | `(1, S)` | **log₁₀(D)** of each segment |
| `seg_state` | `(1, S)` | diffusive-state class index of each segment, 0–3 |

*   `seg_start` and `seg_length` are what identify a segment; a row whose `seg_length` is `≤ 0`, or whose `seg_start` falls outside the trajectory, is skipped, so the arrays may be padded to a fixed length. A segment that runs past the last frame is cut at the end of the trajectory.
*   `seg_alpha`, `seg_logD` and `seg_state` are optional: a missing value is left empty for that segment (not plotted, no diffusive state).
*   `seg_state` is rounded to the nearest class and limited to 0–3.
*   Integer (`int32`/`int64`) or float arrays are both accepted.

Inference runs one trajectory per call, so the batch axis is always 1.

### Exporting a segmentation model to ONNX (PyTorch example)

```python
import torch, torch.nn as nn

class CombinedSeg(nn.Module):
    def forward(self, x):                 # x: (1, T, 2) raw x,y
        # ... your architecture; must handle a dynamic T ...
        alpha           = ...             # (1, T)
        logD            = ...             # (1, T)     = log10(D)
        cp              = ...             # (1, T)     in {0,1}
        diffusive_state = ...             # (1, T, 4)  softmax over the 4 states
        return alpha, logD, cp, diffusive_state

m = CombinedSeg().eval()
dummy = torch.zeros(1, 200, 2)            # any length; the axis is dynamic
torch.onnx.export(
    m, dummy, "my_seg.onnx",
    input_names=["input"],
    output_names=["alpha", "logD", "cp", "diffusive_state"],
    dynamic_axes={"input": {1: "T"}, "alpha": {1: "T"}, "logD": {1: "T"},
                  "cp": {1: "T"}, "diffusive_state": {1: "T"}},
    opset_version=13, do_constant_folding=True,
)
```

A model that also reports its own segments returns the `seg_*` tensors after these four, naming them in `output_names` and marking their length axis dynamic with `{1: "S"}`.

For a **per-output** model, return a single `(1, T)` (or `(1, T, 4)` for the diffusive-state slot) tensor and give it one `output_names` / `dynamic_axes` entry.

{% include notice icon="warning" content="
**Length-derived-constants pitfall.** Do not bake the dummy length (200 in the example above) into any reshape or constant. Derive `T` from the input at runtime (`x.shape[1]`) so the exported graph is truly length-agnostic.
" %}

### Verify a segmentation model before loading

```python
import numpy as np, onnxruntime as ort
s = ort.InferenceSession("my_seg.onnx", providers=["CPUExecutionProvider"])
for T in (37, 128, 240):
    out = s.run(None, {"input": np.random.randn(1, T, 2).astype("float32")})
    for name, arr in zip([o.name for o in s.get_outputs()], out):
        print(T, name, arr.shape)     # (1, T) or (1, T, 1); (1, T, 4) for diffusive_state
```

If every output is length `T` for every `T`, it will load in the plugin.

`utils/pythons_helpers/make_traj_seg_test_onnx_models.py` builds small **dummy** models (`seg_alpha.onnx`, `seg_logd.onnx`, `seg_cp.onnx`, `seg_state.onnx`, and `seg_combined.onnx`, the last with all four required outputs) that follow this contract, so you can exercise both the *Combined* and *Per output* Load modes before dropping in your real models.

## Troubleshooting

Applies to both analysis and segmentation models.

| Symptom | Likely cause |
|---|---|
| "Output '…' not found" / wrong values | output not named as expected, or wrong shape |
| Works for one dataset, wrong for another | sequence-length axis not dynamic, or length-derived constants baked in |
| Classes look shuffled | classifier class order ≠ `ATTM, CTRW, FBM, LW, SBM` |
| α histogram empty | α outside `[0, 2]`, or NaNs — the plugin uses custom α verbatim, so clip/validate it inside your model |
| Load fails immediately | not a valid `.onnx`, or exported with an opset newer than the bundled ONNX Runtime 1.26 supports — re-export with a lower `opset_version` |
