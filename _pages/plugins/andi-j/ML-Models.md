# Machine learning models

AnDi-J uses deep-learning models at different levels:

- [Trajectory Analysis](Trajectory-Analysis): ML is optional for computing the anomalous exponent *α* and required for predicting the diffusion model.
- [Trajectory Segmentation](Trajectory-Segmentation): all predictions here are made with ML models: per-frame *α*, log₁₀(*D*), diffusive state and change-point detection along each trajectory.

Both tasks come with bundled default models that work out of the box. You can also use your own models for any of the tasks above (see [Custom models for Trajectory Analysis](#custom-models-for-trajectory-analysis) and [Custom models for Trajectory Segmentation](#custom-models-for-trajectory-segmentation)).

---

## Bundled models

Two models ship with AnDi-J:

| Model | Used in | Output | Reference |
|---|---|---|---|
| **andi-j-analysis** | Anomalous exponent (ML), Diffusion Model | one *α* per trajectory **and** the diffusion-model class (one network, two heads) | Uses as backbone a [STEP](https://arxiv.org/abs/2302.00410)-like model + further advances of [KISTEP](https://github.com/GabrielFernandezFernandez/kistep). |
| **andi-j-segmentation** | Trajectory Segmentation | per-frame *α*, *D* and diffusive state, plus change points | Based on [U-AnD-ME](https://iopscience.iop.org/article/10.1088/2515-7647/adf9aa). |

Inference runs both in **CPU** and **GPU** support. See [Installation](Home#installation) for details.

### andi-j-analysis

A single-trajectory network that ingests the variable-length relative-polar
sequence (as proposed in [KISTEP](https://github.com/GabrielFernandezFernandez/kistep)) and, through two output heads, jointly predicts the **anomalous
exponent α** (regression) and the **diffusion-model class** (5-way
classification: ATTM, CTRW, FBM, LW, SBM). It is a 1-D residual convolutional network with a self-attention block, and returns a single length-11 vector per trajectory (per-class α + class logits + a combined α). The backbone architecture has been inherited from [STEP](https://arxiv.org/abs/2302.00410).

### andi-j-segmentation

A 1-D **U-Net 3+** ([U-AnD-ME](https://iopscience.iop.org/article/10.1088/2515-7647/adf9aa)), trained for the 2nd AnDi Challenge, containing an
encoder–decoder with full-scale skip connections (6 depth levels). It takes the
2-channel displacement sequence and produces, for every frame, a
**change-point probability** and a 3-channel vector **[α, log₁₀(D), diffusive state]** —
the third channel is the model's per-frame diffusive-state class (0 = immobile,
1 = confined, 2 = free diffusion, 3 = directed). Each trajectory is zero-padded
to the next multiple of **32**, and trajectories are **batched by padded
length** for speed. An optional **test-time augmentation** (averaging 8
symmetry views: 4 rotations × 2 flips) trades ~8× compute for a small accuracy
gain and is **off by default**.

A detected segment's diffusive state is the **majority vote** of its frames'
predicted states; its α and D are the segment's mean.

---

## What is ONNX (and why)

**ONNX** (Open Neural Network Exchange) is a portable, framework-independent file
format for a trained neural network: the graph of operations plus the learned
weights, in a single `.onnx` file. It allows you to train in whichever Python framework you like (PyTorch, TensorFlow, scikit-learn…), then *export* the trained model to ONNX.

The bundled models have all been trained using PyTorch. However, AnDi-J runs `.onnx` files with **ONNX Runtime** (the Java build), so at
inference time **no Python is needed** — the model runs inside Fiji. This also means that when developing a custom model, you must export it to `.onnx` afterwards. Below you will find how to do that for the different options available.

---

## Custom models for Trajectory Analysis

AnDi-J ships with a default deep-learning model, but you can plug in **your
own** model for either per-trajectory prediction task:

- **Anomalous exponent** (`Anomalous exponent` tab → **Type: Load**) — a model
  that predicts the exponent *α* for a trajectory.
- **Diffusion model classification** (`Diffusion Model` tab → **Type: Load**) —
  a model that classifies a trajectory into one of the five diffusion models.

> The bundled **Default** model predicts α *and* the diffusion model in one
> network. A model you **Load** is single-purpose: an α model updates only α; a
> classifier model updates only the diffusion-model tab.

### Input

For every trajectory the plugin builds one input tensor and calls your model:

| | |
|---|---|
| **Shape** | `(1, T, 2)` — batch 1, one row per **frame**, two features |
| **Type** | `float32` |
| **Dynamic axis** | the `T` (sequence-length) axis **must be dynamic** |

The two features are the **raw trajectory coordinates**:

- column `0` = `x`
- column `1` = `y`

i.e. exactly the (x, y) positions from your loaded data, one row per
frame. The plugin feeds these directly — it does **no** preprocessing.

> **Choose your own representation inside the model.** If your method works on
> displacements, relative-polar features `(dr, dθ)`, images, etc., compute that
> transform as the first layers of your model (or in the exported graph). That
> way training and inference stay identical and the plugin's contract stays
> simple. The bundled *Default* model, for example, converts (x, y) to
> relative-polar internally. That choice lives inside the model, not the
> plugin.

### Output

**Anomalous-exponent model**

| | |
|---|---|
| **Shape** | `(1, 1)` (or `(1,)`) |
| **Meaning** | the predicted exponent α; the plugin reads element `[0]` |

α should lie in `[0, 2]` (values outside are dropped from the histogram).
The α prediction is a single value for the 2D trajectory, so the X / Y component
buttons are disabled while ML α results are shown.

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

The **`dynamic_axes`** entry for the sequence-length axis is essential —
trajectories have different lengths, and without it the exported graph is locked
to `50`.

> **Watch out: values derived from the sequence length.** If your `forward` uses
> the length as a Python integer — e.g. `T = x.shape[1]` then `math.log(T)`,
> `1/T`, or slicing like `x[:, T//2:]` — the ONNX tracer **bakes those in as
> constants** for the dummy length, and the model is then wrong for other
> lengths. Fixes: derive such quantities from the tensor shape at runtime (e.g.
> build a length tensor with `torch.ones_like(...).sum(dim=1)` and a position
> index with `torch.cumsum(torch.ones_like(...), dim=1) - 1`, then use masks
> instead of fixed slices), or expose the extra scalar as an additional model
> input. 

### Verify an analysis model before loading

Check the exported graph in Python with ONNX Runtime, at **two different
lengths**, before loading it in Fiji:

```python
import numpy as np, onnxruntime as ort

sess = ort.InferenceSession("my_alpha.onnx")
for T in (12, 137):                              # different trajectory lengths
    x = np.random.randn(1, T, 2).astype(np.float32)   # (1, T, 2) raw (x, y)
    out = sess.run(["output"], {"input": x})[0]
    print(T, out.shape, out.ravel()[:5])
```

You want the output shape to be `(1, 1)` for an α model or `(1, 5)` for a
classifier, and no error at either length.

A ready-made pair of **test models** (an α estimator and a classifier) is
provided in `utils/pythons_helpers/make_traj_analysis_test_onnx_models.py`:

```bash
python make_traj_analysis_test_onnx_models.py     # -> test_alpha.onnx, test_model.onnx
```

Use them to confirm the Load path works end-to-end before wiring your own model.

### Loading an analysis model in the plugin

1. Run **Perform Analysis** so the trajectories are loaded.
2. Open the relevant tab:
   - **Anomalous exponent** → set **Type: Load** → **Choose model…** → pick your
     α `.onnx` → **Compute α**.
   - **Diffusion Model** → set **Type: Load** → **Choose model…** → pick your
     classifier `.onnx` → **Compute models (ML)**.
3. Each runs with a progress bar over the number of trajectories.

Switching **Type** back to **Default** restores the bundled model (which fills
both α and the diffusion model, and keeps the two tabs in sync).

---

## Custom models for Trajectory Segmentation

Trajectory Segmentation can run your own ONNX model(s) instead of the bundled
one. Pick **Load** in the *ML model options* box of the
[segmentation Data Manager](Input-data#selecting-the-segmentation-model), then
either:

- **Combined model** — one `.onnx` that outputs α, log₁₀(D) and change points
  (plus, optionally, the diffusive state), or
- **Per output** — one `.onnx` per output (**α**, **D**, **Change points**,
  **Diffusive state**); any of α, D or change points you leave as *default* is
  produced by the bundled model. The diffusive state is the exception: it is
  only backed by the bundled model when the bundled model is *already* running
  for one of the other three; if you supply custom α, D and change-point
  models and simply leave diffusive state unset, segments get no diffusive
  state rather than triggering an extra model run just for that.

The plugin does no pre- or post-processing for your model: it feeds the raw trajectory in and reads your per-frame outputs out verbatim. Any processing must be added within your `.onnx` file.

### Input: the raw trajectory

| name | shape | dtype | meaning |
|------|-------|-------|---------|
| `input` | `(1, T, 2)` | float32 | raw positions — column 0 = x, column 1 = y, one row per frame |

`T` (the number of frames) is **dynamic** — export the length axis as dynamic so
your model accepts any trajectory length. If your architecture needs
displacements, a fixed length, or padding, do it **inside** your model.

### Outputs: per-frame α, log D, change points and diffusive state

Every output is **per frame**, length `T`, in the same frame order as the input.
Shape `(1, T)` or `(1, T, 1)` are both accepted (`(1, T, 4)` for `model_type`, see
below).

| output | shape | meaning | used as-is? |
|--------|-----------|---------|-------------|
| `alpha` | `(1, T)` | anomalous exponent α per frame | yes, verbatim |
| `logD`  | `(1, T)` | **log₁₀(D)** per frame | yes, verbatim (use `NaN` for undefined/immobile) |
| `cp`    | `(1, T)` | change-point flag per frame, **0 or 1** | the plugin marks a change point at every interior frame where `cp ≥ 0.5` |
| `model_type` | `(1, T, 4)` or `(1, T)` | **optional** — per-frame diffusive state: either class probabilities over the four diffusive states (`0 = immobile, 1 = confined, 2 = free diffusion, 3 = directed`), or the class index directly | `(1, T, 4)` → per-frame `argmax`; `(1, T)` → per-frame rounded value. A segment's state is the **majority vote** of its frames' values, shown in the *Diffusive state* tab |

Notes:

- **D must be output as `log₁₀(D)`**, not linear D — that is exactly what the
  plugin stores and plots, so nothing is transformed. If a frame has no
  meaningful D (immobile / trapped), emit `NaN`; it will be shown as a gap and
  left out of segment means.
- **`cp` is a 0/1 flag**, one per frame. Frame 0 and the last frame are ignored
  (they are trajectory ends, not change points). Emit `1` at the first frame of
  each new segment.
- **`model_type` is optional.** Without it, a segment's diffusive state is left
  undefined and it is simply not counted in the *Diffusive state* tab.
- Segments (used by the *D vs α*, *Segment Stats* and *Diffusive state* tabs)
  are assembled by the plugin from your `cp` output and the interval means /
  majority vote of your `alpha` / `logD` / `model_type`.

**Output names**

- **Combined model**: name the outputs `alpha`, `logD`, `cp` and, optionally,
  `model_type`. If unnamed, the plugin falls back to output order 0 = alpha,
  1 = logD, 2 = cp, 3 = model_type.
- **Per-output model**: a single output; its name does not matter. 

### Exporting a segmentation model to ONNX (PyTorch example)

```python
import torch, torch.nn as nn

class CombinedSeg(nn.Module):
    def forward(self, x):                 # x: (1, T, 2) raw x,y
        # ... your architecture; must handle a dynamic T ...
        alpha      = ...                  # (1, T)
        logD       = ...                  # (1, T)     = log10(D)
        cp         = ...                  # (1, T)     in {0,1}
        model_type = ...                  # (1, T, 4)  softmax, optional
        return alpha, logD, cp, model_type

m = CombinedSeg().eval()
dummy = torch.zeros(1, 200, 2)            # any length; the axis is dynamic
torch.onnx.export(
    m, dummy, "my_seg.onnx",
    input_names=["input"],
    output_names=["alpha", "logD", "cp", "model_type"],
    dynamic_axes={"input": {1: "T"}, "alpha": {1: "T"}, "logD": {1: "T"},
                  "cp": {1: "T"}, "model_type": {1: "T"}},
    opset_version=13, do_constant_folding=True,
)
```

For a **per-output** model, return a single `(1, T)` (or `(1, T, 4)` for the
diffusive-state slot) tensor and give it one `output_names` / `dynamic_axes`
entry.

> **Length-derived-constants pitfall.** Do not bake the dummy length (200 here)
> into any reshape/constant. Derive `T` from the input at runtime (`x.shape[1]`)
> so the exported graph is truly length-agnostic.

### Verify a segmentation model before loading

```python
import numpy as np, onnxruntime as ort
s = ort.InferenceSession("my_seg.onnx", providers=["CPUExecutionProvider"])
for T in (37, 128, 240):
    out = s.run(None, {"input": np.random.randn(1, T, 2).astype("float32")})
    for name, arr in zip([o.name for o in s.get_outputs()], out):
        print(T, name, arr.shape)     # (1, T) or (1, T, 1); (1, T, 4) for model_type
```

If every output is length `T` for every `T`, it will load in the plugin.

`utils/pythons_helpers/make_traj_seg_test_onnx_models.py` builds small **dummy** models
(`seg_alpha.onnx`, `seg_logd.onnx`, `seg_cp.onnx`, `seg_modeltype.onnx`, and
`seg_combined.onnx`, the last with all four outputs) that follow this contract,
so you can exercise both the *Combined* and *Per output* Load modes before
dropping in your real models.

---

## Troubleshooting

Applies to both analysis and segmentation models.

| Symptom | Likely cause |
|---|---|
| "Output '…' not found" / wrong values | output not named as expected, or wrong shape |
| Works for one dataset, wrong for another | sequence-length axis not dynamic, or length-derived constants baked in |
| Classes look shuffled | classifier class order ≠ `ATTM, CTRW, FBM, LW, SBM` |
| α histogram empty | α outside `[0, 2]`, or NaNs — clamp/validate your output |
| Load fails immediately | not a valid `.onnx`, or an opset ONNX Runtime 1.17 doesn't support (use opset ≤ 17) |
