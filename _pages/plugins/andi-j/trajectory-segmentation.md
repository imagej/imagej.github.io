---
title: AnDi-J › Trajectory Segmentation
name: AnDi-J
icon: /media/plugins/andi-j/logo.png
description: Per-frame predictions of alpha, D and diffusive state along each trajectory, with change-point detection and segment statistics.
nav-title: Trajectory Segmentation
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

This tool runs a per-frame segmentation model that predicts, **for every frame** of every trajectory, the local anomalous exponent *α*, the diffusion coefficient *D* (shown as log₁₀(*D*), due to its wide range of values) and the **diffusive state** — immobile, confined, free diffusion, or directed. It then detects **change points** to split each trajectory into homogeneous segments, each with its own α, *D* and diffusive state (see [ML models](/plugins/andi-j/ml-models#andi-j-segmentation) for how the default model computes them). The window has four tabs: [Visualization](#visualization), [D vs α](#d-vs-alpha), [Segment Stats](#segment-stats) and [Diffusive state](#diffusive-state).

{% include notice icon="info" content="**Saving data.** Per-frame predictions and per-segment statistics can be exported as `csv` files from the [Visualization](#visualization) tab (see below). The **D vs α**, **Segment Stats** and **Diffusive state** tabs have a **Save plot** button that exports the plot, with all its panels, as a vector image (`svg`)." %}

## Visualization

A **4 × 4 grid** of prediction plots, one per trajectory. Each plot shows the per-frame predictions for one trajectory:

1.  Two lines showcasing **α** (red, right axis, range [0, 2]) and **log₁₀(D)** (blue, left axis, auto-scaled).
2.  A coloured strip showing the predicted diffusive state, with colour code:
    <span style="display:inline-block;width:12px;height:12px;background:#787878;"></span> Immobile,
    <span style="display:inline-block;width:12px;height:12px;background:#E69F00;"></span> Confined,
    <span style="display:inline-block;width:12px;height:12px;background:#009E73;"></span> Free diffusion and
    <span style="display:inline-block;width:12px;height:12px;background:#CC79A7;"></span> Directed.

For α and D, two layers are overlaid:

*   The **raw per-frame prediction**, whose opacity is controlled by the **Raw α/D** slider.
*   The **segment step-line**, i.e. the value of that variable for each detected segment, toggled independently with **α_seg** / **D_seg**.

The **CP** toggle shows/hides the dashed vertical lines marking the detected change points; the **State** toggle shows/hides the diffusive-state strip.

Tools:

*   **Sample random 16** picks 16 random trajectories; **Choose trajectories** opens a popup to enter specific `TRACK_ID`s.
*   **Save raw preds.** exports every trajectory's per-frame α, D and diffusive state to a `csv` (`experiment, track_id, frame, alpha, D, state`); `frame` is the `FRAME` of the input file and `state` is the per-frame diffusive state, coded as `0 = immobile, 1 = confined, 2 = free diffusion, 3 = directed`.
*   **Save segments** exports the detected segments, with starting frame, length, α, D, and state (`experiment, track_id, segment, start_frame, length, alpha, D, state`); `start_frame` is the `FRAME` of the input file at which the segment starts.

{% include img align="center" name="Visualization tab" src="/media/plugins/andi-j/seg-visualization-tab.png" caption="**Visualization** grid with the raw prediction and segment step-line overlaid." %}

## D vs α
{: #d-vs-alpha}

This tab shows a **2-D density heatmap** for the per-frame tuple (α, log₁₀*D*). Each selected experiment is overlaid as its own semi-transparent colour.

The side plots show the **marginal histograms + KDEs** along the top (α) and right (log₁₀*D*) edges. Drag the plot's top or right border to resize either marginal strip.

Tools:

*   Hovering the heatmap shows the (α, log₁₀*D*) value under the cursor.
*   Rubber-band **Zoom**, **Pan**, **Reset view**; a draggable **legend**.
*   Experiment multi-select in the side panel.

{% include img align="center" name="D vs alpha tab" src="/media/plugins/andi-j/seg-dvsa-tab.png" caption="**D vs α** density heatmap of the per-frame predictions." %}

## Segment Stats

This tab shows the temporal statistics of the identified segments, together with their relation to the extracted α and *D*.

Plots:

*   **Segment-length histogram** — the distribution of segment lengths separated per experiment.
*   **Segment length vs α** and **Segment length vs D** — 2-D density heatmaps, overlaid per experiment, each with a side marginal KDE of the *y* variable (α on the left, *D* on the right).

Tools:

*   **Length bins**, **α bins** and **D bins** are set independently; all three plots share the segment-length *x* axis.
*   Rubber-band **Zoom**, **Pan**, **Reset view** on every plot.

{% include img align="center" name="Segment Stats tab" src="/media/plugins/andi-j/seg-stats-tab.png" caption="**Segment Stats** tab." %}

## Diffusive state

This tab gathers the diffusive-state analysis. It contains two plots:

*   **Top** — a grouped bar chart of the **percentage of segments** in each diffusive state, per experiment.
*   **Bottom** — the **segment-length distribution**, one colour-coded line per diffusive state, pooled over the selected experiments. A **Normalize (%)** checkbox switches between raw segment counts and each state's distribution normalised to its own total (useful to compare the *shape* of the length distributions regardless of how many segments each state has).

The right-hand column mirrors that split: it lets you select the **Experiments** as well as which **Diffusive states** are shown in the segment-length plot. A state with no segments draws a flat line at zero.

{% include img align="center" name="Diffusive state tab" src="/media/plugins/andi-j/seg-diffusive-state-tab.png" caption="**Diffusive state** tab." %}
