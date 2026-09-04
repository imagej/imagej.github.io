<p align="center">
<img width="100" src="https://github.com/gorkamunoz/andi-j/blob/main/utils/images/logo.png">
</p>

**AnDi-J** is a [Fiji](https://fiji.sc/)/ImageJ plugin for **anomalous-diffusion analysis of single-particle tracking (SPT) data**. Given input trajectories, it provides state-of-the-art machinery to analyse them, combining statistical and machine learning (ML) analysis. The plugin works at two scales: from single-trajectory analysis, returning properties for each of the input trajectories, to "*per-frame*" predictions, allowing for a fine-grained analysis and the segmentation of trajectories with expected diffusion changes.

---

## Contents

- [Overview](#overview)
- [Installation](#installation)
- [Input data](Input-data)
  - [Data Manager](Input-data#data-manager)
- [Trajectory Analysis](Trajectory-Analysis)
  - [tMSD Visualization](Trajectory-Analysis#tmsd-visualization)
  - [Diffusion coefficient](Trajectory-Analysis#diffusion-coefficient)
  - [Anomalous exponent](Trajectory-Analysis#anomalous-exponent)
  - [D vs α](Trajectory-Analysis#d-vs-α)
  - [Diffusion Model](Trajectory-Analysis#diffusion-model)
  - [Turning Angles](Trajectory-Analysis#turning-angles)
  - [PSD](Trajectory-Analysis#psd)
- [Trajectory Segmentation](Trajectory-Segmentation)
  - [Visualization](Trajectory-Segmentation#visualization)
  - [D vs α (density)](Trajectory-Segmentation#d-vs-α-density)
  - [Segment Stats](Trajectory-Segmentation#segment-stats)
  - [Diffusive state](Trajectory-Segmentation#diffusive-state)
- [Machine learning models](ML-Models)
- [Citing AnDi-J](#citing-andi-j)
- [More resources](#more-resources)

---

## Overview

AnDi-J is organised around two menu commands under **`Plugins ▸ AnDi`**:

| Command | Purpose |
|---|---|
| [**Trajectory Analysis**](Trajectory-Analysis) | Per-trajectory observables: mean squared displacement (MSD) analysis, diffusion coefficient *D*, anomalous exponent *α*, the *D*–*α* plane, diffusion-model classification, and turning angles. |
| [**Trajectory Segmentation**](Trajectory-Segmentation) | Per-frame predictions of *α* and *D* along each trajectory, change-point detection that splits it into homogeneous segments, and the diffusive state (immobile, confined, free diffusion, or directed) of each segment. |

Both commands share the same **Data Manager** for loading and grouping data, and
both can analyse several experiments (conditions) at once, each with its own
colour, overlaid for comparison.

---

## Installation

### Recommended

1. Go to the [**Releases**](https://github.com/gorkamunoz/andi-j/releases) page of this repository.
2. Under the latest plugin release, download the file **`andi-j-X.Y.Z.jar`**.
3. This plugin uses **ONNX Runtime** for its machine-learning predictions. It provides support both **CPU** and **GPU** (CUDA) support. The latter allows for much faster computations. The current release requires CUDA Toolkit 12.x and cuDNN 9.x for CUDA 12 (see below for other CUDA versions). You can download the corresponding file directly from Maven Central:
   - CPU:
   [`onnxruntime-1.26.0.jar`](https://repo1.maven.org/maven2/com/microsoft/onnxruntime/onnxruntime/1.26.0/onnxruntime-1.26.0.jar)
   - GPU/CUDA: [`onnxruntime_gpu-1.26.0.jar`](https://repo1.maven.org/maven2/com/microsoft/onnxruntime/onnxruntime_gpu/1.26.0/onnxruntime_gpu-1.26.0.jar) 
   
4. Copy **both** `andi-j` and `onnxruntime` jars into the
   **`Fiji.app/jars/`** folder. 
5. **Restart Fiji.**
6. The plugin is now available under **Plugins › AnDi-J**.

### Build from scratch

```bash
git clone https://github.com/gorkamunoz/andi-j.git
```
You will then need to download the two default ML models (see [Releases](https://github.com/gorkamunoz/andi-j/releases), look for the latest model release). Place these models in `andi-j/src/main/resources/models/`. Then:

```bash
cd andi-j
mvn clean package
# then copy target/andi-j-*.jar into Fiji.app/jars/
```

`mvn clean package` also resolves `onnxruntime-1.26.0.jar` into your local
Maven cache, so you can copy it from there instead of downloading it again:

```bash
cp ~/.m2/repository/com/microsoft/onnxruntime/onnxruntime_gpu/1.26.0/onnxruntime-1.26.0.jar Fiji.app/jars/
```

Requires Java 8+ and Maven. The build uses the [pom-scijava](https://github.com/scijava/pom-scijava) parent POM.

**Debug mode:** AnDi-J keeps its diagnostics quiet by default. To see them, enable ImageJ's debug mode:

**`Edit ▸ Options ▸ Misc… ▸ Debug mode`**

and open **`Window ▸ Console`**. With debug mode on, the plugin prints information about the ML-models (ONNX model input/output tensor shapes and CPU/GPU usage). Genuine anomalies (e.g. a custom model returning an unexpected output type) are always reported, debug mode or not.

#### Custom CUDA installation

If your machine has a different CUDA toolkit installed than the recommended one, you must find the matching `onnxruntime_gpu` release: 

1. Check your installed CUDA version: `nvcc --version` .
2. Look up which `onnxruntime_gpu` release supports that CUDA version in the
   [ONNX Runtime CUDA Execution Provider compatibility table](https://onnxruntime.ai/docs/execution-providers/CUDA-ExecutionProvider.html).
3. Download the matching jar from Maven Central:
   `https://repo1.maven.org/maven2/com/microsoft/onnxruntime/onnxruntime_gpu/<version>/onnxruntime_gpu-<version>.jar`
4. Place that file in `Fiji.app/jars/`.
5. Update the `andi-j` `pom.xml` file with the downloaded version: 
```xml
<artifactId>onnxruntime_gpu</artifactId>
<version>1.xx.0</version>
```
6. Build the plugin from scratch. 
5. Restart Fiji.

---

## Citing AnDi-J

If you found this package useful and used it in your projects, you can
use the following to directly cite the package:

```
soon
```

---

## More resources

This package relies on previous work done in the context of the AnDi Challenge and related projects. To learn more about them, you can use the following references:

- [`andi_datasets`](https://github.com/AnDiChallenge/andi_datasets): Python library used as backbone for many of the methods underlying AnDi-J.

- [Objective comparison of methods to decode anomalous diffusion, G. Muñoz-Gil et al. (2021)](https://www.nature.com/articles/s41467-021-26320-w): paper gathering the results of the 1st AnDi Challenge. Related to the analysis performed in [Trajectory Analysis](Trajectory-Analysis).

- [Quantitative evaluation of methods to analyze motion changes in single-particle experiments, G. Muñoz-Gil et al. (2025)](https://www.nature.com/articles/s41467-025-61949-x): paper gathering the results of the 2nd AnDi Challenge. Related to the analysis performed in [Trajectory Segmentation](Trajectory-Segmentation).

- [Inferring pointwise diffusion properties of single trajectories with deep learning, B. Requena et al. (2023)](https://www.cell.com/biophysj/fulltext/S0006-3495(23)00651-3): paper proposing step-wise prediction of anomalous diffusion trajectories. The default ML models used in both tabs are based on the architecture developed for this paper and the [KISTEP](https://github.com/GabrielFernandezFernandez/kistep) extension by G. Fernández-Fernández.

- [U-Net 3+ for anomalous diffusion analysis enhanced with mixture estimates (U-AnD-ME) in particle-tracking data, S. Agshar et al. (2025)](https://iopscience.iop.org/article/10.1088/2515-7647/adf9aa): paper of the winners of the 2nd AnDi challenge. The default model of the segmentation tab is a direct update of their model.