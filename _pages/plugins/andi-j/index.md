---
title: AnDi-J
name: AnDi-J
description: Anomalous-diffusion analysis of single-particle tracking (SPT) data in Fiji, combining statistical and machine-learning methods.
categories: [Analysis, Tracking, Track analysis, Machine Learning]
icon: /media/plugins/andi-j/logo.png
update-site: AnDi-J
nav-title: Overview
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
source-url: https://github.com/gorkamunoz/andi-j
release-url: https://github.com/gorkamunoz/andi-j/releases/latest
dev-status: Active
support-status: Active
team-founders: 'Gorka Muñoz-Gil | https://github.com/gorkamunoz'
team-maintainers: 'Gorka Muñoz-Gil | https://github.com/gorkamunoz'
---

{% include img align="center" src="/media/plugins/andi-j/logo.png" alt="AnDi-J logo" width="160" %}

**AnDi-J** is a [Fiji](/software/fiji)/ImageJ plugin for **anomalous-diffusion analysis of single-particle tracking (SPT) data**. Given input trajectories, it provides state-of-the-art machinery to analyse them, combining statistical and machine learning (ML) analysis. The plugin works at two scales: from single-trajectory analysis, returning properties for each of the input trajectories, to "*per-frame*" predictions, allowing for a fine-grained analysis and the segmentation of trajectories with expected diffusion changes.

{% include notice icon="info" content="
An up-to-date version of this wiki is available in [**Github**](https://github.com/gorkamunoz/andi-j/wiki). We strongly suggest following that, as it is more regularly updated.
" %}



## Overview

AnDi-J is organised around two menu commands under {% include bc path="Plugins|AnDi-J" %}:

| Command | Purpose |
|---|---|
| [**Trajectory Analysis**](/plugins/andi-j/trajectory-analysis) | Per-trajectory observables: mean squared displacement (MSD) analysis, diffusion coefficient *D*, anomalous exponent *α*, the *D*–*α* plane, diffusion-model classification, and turning angles. |
| [**Trajectory Segmentation**](/plugins/andi-j/trajectory-segmentation) | Per-frame predictions of *α* and *D* along each trajectory, change-point detection that splits it into homogeneous segments, and the diffusive state (immobile, confined, free diffusion, or directed) of each segment. |

Both commands share the same [Data Manager](/plugins/andi-j/input-data#data-manager) for loading and grouping data, and both can analyse several experiments (conditions) at once, each with its own colour, overlaid for comparison.

## Documentation

| Page | Contents |
|---|---|
| [Input data](/plugins/andi-j/input-data) | Expected `.csv` layout, the [Data Manager](/plugins/andi-j/input-data#data-manager), and [selecting the segmentation model](/plugins/andi-j/input-data#selecting-the-segmentation-model). |
| [Trajectory Analysis](/plugins/andi-j/trajectory-analysis) | [tMSD](/plugins/andi-j/trajectory-analysis#tmsd-visualization), [diffusion coefficient](/plugins/andi-j/trajectory-analysis#diffusion-coefficient), [anomalous exponent](/plugins/andi-j/trajectory-analysis#anomalous-exponent), [*D* vs *α*](/plugins/andi-j/trajectory-analysis#d-vs-α), [diffusion model](/plugins/andi-j/trajectory-analysis#diffusion-model), [turning angles](/plugins/andi-j/trajectory-analysis#turning-angles) and [PSD](/plugins/andi-j/trajectory-analysis#psd). |
| [Trajectory Segmentation](/plugins/andi-j/trajectory-segmentation) | [Visualization](/plugins/andi-j/trajectory-segmentation#visualization), [*D* vs *α* density](/plugins/andi-j/trajectory-segmentation#d-vs-α), [segment stats](/plugins/andi-j/trajectory-segmentation#segment-stats) and [diffusive state](/plugins/andi-j/trajectory-segmentation#diffusive-state). |
| [ML models](/plugins/andi-j/ml-models) | The bundled models, the ONNX contract, and how to plug in your own models. |

## Installation

### From the update site

The easiest way to install AnDi-J, and to keep it up to date, is to [follow](/update-sites/following) the **AnDi-J** [update site](/update-sites):

1.  Start [Fiji](/software/fiji) (or [download and install it](/software/fiji/downloads) first).
2.  Select {% include bc path="Help|Update..." %} from the menu bar.
3.  Click on the {% include button label="Manage update sites" %} button.
4.  Scroll down the list and tick the checkbox for the **AnDi-J** update site, then click {% include button label="Close" %}. If **AnDi-J** is missing from the list, click {% include button label="Update URLs" %} to refresh it.
5.  Click {% include button label="Apply changes" %} to install the plugin.
6.  Restart Fiji.

The plugin is then available under {% include bc path="Plugins|AnDi-J" %}.

{% include notice icon="note" content="
The update site installs AnDi-J together with the **CPU** build of ONNX Runtime. For GPU (CUDA) acceleration, replace `onnxruntime-1.26.0.jar` with `onnxruntime_gpu-1.26.0.jar` ([download link](https://repo1.maven.org/maven2/com/microsoft/onnxruntime/onnxruntime_gpu/1.26.0/onnxruntime_gpu-1.26.0.jar)) in the `Fiji.app/jars/` folder. See more below.
" %}

### Manual installation

If you prefer not to use the updater, or you want a specific release:

1.  Go to the [Releases](https://github.com/gorkamunoz/andi-j/releases) page of the AnDi-J repository.
2.  Under the latest plugin release, download the file `andi-j-X.Y.Z.jar`.
3.  AnDi-J uses **ONNX Runtime** for its machine-learning predictions, with support for both **CPU** and **GPU** (CUDA). The latter allows for much faster computations. The current release requires CUDA Toolkit 12.x and cuDNN 9.x for CUDA 12 (see [Custom CUDA installation](#custom-cuda-installation) for other CUDA versions). Download the corresponding file directly from Maven Central:
    *   CPU: [`onnxruntime-1.26.0.jar`](https://repo1.maven.org/maven2/com/microsoft/onnxruntime/onnxruntime/1.26.0/onnxruntime-1.26.0.jar)
    *   GPU/CUDA: [`onnxruntime_gpu-1.26.0.jar`](https://repo1.maven.org/maven2/com/microsoft/onnxruntime/onnxruntime_gpu/1.26.0/onnxruntime_gpu-1.26.0.jar)
4.  Copy **both** the `andi-j` and the `onnxruntime` jars into the `Fiji.app/jars/` folder.
5.  Restart Fiji.
6.  The plugin is now available under {% include bc path="Plugins|AnDi-J" %}.

### Build from source

```bash
git clone https://github.com/gorkamunoz/andi-j.git
```

You will then need to download the two default ML models (see [Releases](https://github.com/gorkamunoz/andi-j/releases), look for the latest model release). Place these models in `andi-j/src/main/resources/models/`. Then:

```bash
cd andi-j
mvn clean package
# then copy target/andi-j-*.jar into Fiji.app/jars/
```

`mvn clean package` also resolves `onnxruntime-1.26.0.jar` into your local Maven cache, so you can copy it from there instead of downloading it again:

```bash
cp ~/.m2/repository/com/microsoft/onnxruntime/onnxruntime_gpu/1.26.0/onnxruntime-1.26.0.jar Fiji.app/jars/
```

Requires Java 8+ and [Maven](/develop/maven). The build uses the [pom-scijava](https://github.com/scijava/pom-scijava) parent POM.

{% capture debug-mode %}
**Debug mode.** AnDi-J keeps its diagnostics quiet by default. To see them, enable ImageJ's debug mode at {% include bc path="Edit|Options|Misc..." %} and open {% include bc path="Window|Console" %}. With debug mode on, the plugin prints information about the ML models (ONNX model input/output tensor shapes and CPU/GPU usage). Genuine anomalies (e.g. a custom model returning an unexpected output type) are always reported, debug mode or not.
{% endcapture %}
{% include notice icon="tech" content=debug-mode %}

### Custom CUDA installation

If your machine has a different CUDA toolkit installed than the recommended one, you must find the matching `onnxruntime_gpu` release:

1.  Check your installed CUDA version: `nvcc --version`.
2.  Look up which `onnxruntime_gpu` release supports that CUDA version in the [ONNX Runtime CUDA Execution Provider compatibility table](https://onnxruntime.ai/docs/execution-providers/CUDA-ExecutionProvider.html).
3.  Download the matching jar from Maven Central: `https://repo1.maven.org/maven2/com/microsoft/onnxruntime/onnxruntime_gpu/<version>/onnxruntime_gpu-<version>.jar`
4.  Place that file in `Fiji.app/jars/`.
5.  Update the AnDi-J `pom.xml` file with the downloaded version:

    ```xml
    <artifactId>onnxruntime_gpu</artifactId>
    <version>1.xx.0</version>
    ```
6.  Build the plugin from source.
7.  Restart Fiji.

## Citing AnDi-J

{% include notice icon="info" content="A citable reference for AnDi-J is coming soon. In the meantime, please cite the [papers listed below](#more-resources) that underpin the analyses you used." %}

## More resources

AnDi-J relies on previous work done in the context of the AnDi Challenge and related projects. To learn more about them, you can use the following references:

*   [`andi_datasets`](https://github.com/AnDiChallenge/andi_datasets): Python library used as backbone for many of the methods underlying AnDi-J.
*   [Objective comparison of methods to decode anomalous diffusion, G. Muñoz-Gil et al. (2021)](https://www.nature.com/articles/s41467-021-26320-w): paper gathering the results of the 1st AnDi Challenge. Related to the analysis performed in [Trajectory Analysis](/plugins/andi-j/trajectory-analysis).
*   [Quantitative evaluation of methods to analyze motion changes in single-particle experiments, G. Muñoz-Gil et al. (2025)](https://www.nature.com/articles/s41467-025-61949-x): paper gathering the results of the 2nd AnDi Challenge. Related to the analysis performed in [Trajectory Segmentation](/plugins/andi-j/trajectory-segmentation).
*   [Inferring pointwise diffusion properties of single trajectories with deep learning, B. Requena et al. (2023)](https://www.cell.com/biophysj/fulltext/S0006-3495(23)00651-3): paper proposing step-wise prediction of anomalous diffusion trajectories. The default ML models used in both tabs are based on the architecture developed for this paper and the [KISTEP](https://github.com/GabrielFernandezFernandez/kistep) extension by G. Fernández-Fernández.
*   [U-Net 3+ for anomalous diffusion analysis enhanced with mixture estimates (U-AnD-ME) in particle-tracking data, S. Asghar et al. (2025)](https://iopscience.iop.org/article/10.1088/2515-7647/adf9aa): paper of the winners of the 2nd AnDi Challenge. The default model of the segmentation tab is a direct update of their model.

## See also

*   [TrackMate](/plugins/trackmate) — produces the `.csv` trajectory files AnDi-J reads.
*   [TraJClassifier](/plugins/trajclassifier) — another Fiji tool for classifying diffusion trajectories.
