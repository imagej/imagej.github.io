---
title: AnDi-J › Trajectory Analysis
name: AnDi-J
icon: /media/plugins/andi-j/logo.png
description: Per-trajectory anomalous-diffusion observables in AnDi-J - tMSD, diffusion coefficient, anomalous exponent, D vs α, diffusion model, turning angles, PSD and summary table.
nav-title: Trajectory Analysis
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

This tool allows to perform single-trajectory analysis of the input experiments. Every tab has a side **Experiments** panel where each experiment can be toggled on/off and, where relevant, restricted to the **2D**, **X**, or **Y** component.

{% include notice icon="info" content="**Saving data.** Every tab has a **Save plot** button that exports its plot as a vector image (`svg`), which you can edit in tools such as Inkscape or Illustrator. The **Diffusion coefficient**, **Anomalous exponent**, **Diffusion Model**, **Turning Angles**, **PSD** and **Summary** tabs also save their values as a `csv` file for further analysis (**Save D…**, **Save α…**, **Save models…**, **Save angles…**, **Save PSD…** and **Save table…**). Their first columns are `experiment` and, for per-trajectory values, `track_id`; commas in experiment names are written as semicolons. In **D vs α**, tagged populations can be saved as trajectory files (see [Population tagging](#d-vs-alpha))." %}

{% include notice icon="info" content="**Units.** The **Units** button of the tMSD Visualization, Diffusion coefficient, D vs α, PSD and Summary tabs opens a window to choose the time (frames, ns, μs, ms, s) and space (nm, μm, mm, m) units of the plots and `csv` exports, whose column headers name them. Physical units need the calibration of the [Data Manager](/plugins/andi-j/input-data#units); without it, the window shows px and frames and cannot change them." %}

## tMSD Visualization

This tab shows the time-averaged MSD curves for each experiment, allowing for an initial visual inspection of the diffusive properties of the loaded experiments.

*   Per-experiment selectors for **Avg** (the average tMSD), **All** (every individual trajectory, faint), and **eMSD** (ensemble MSD, dashed).
*   The lag axis is controlled by **Min lag**, **Max lag** (in frames) and **Log-spaced**. The number of lag points is chosen automatically (every integer lag when linear; capped, log-spaced sampling when log-spaced is selected). When the window opens, the tMSD is computed with min lag 1, max lag a quarter of the longest trajectory length and linear lags, the values shown in the fields.
*   **Draw line** lets you place a reference line and read its slope live; in log–log mode the slope is labelled *α*, since it corresponds to the anomalous exponent.
*   **eMSD vs tMSD as an ergodicity test:** comparing the eMSD curve to the Avg tMSD shows whether the process is ergodic (the two coincide) or non-ergodic (they differ).

{% include img align="center" name="tMSD tab" src="/media/plugins/andi-j/tmsd-tab.png" caption="**tMSD Visualization** tab with the eMSD overlay." %}

## Diffusion coefficient

Estimates the diffusion coefficient *D* per trajectory from a linear fit of the tMSD vs lag-time (mirroring `andi_datasets`' `get_diff_coeff`), shown as a histogram. Dashed lines show the mean over the experiment.

You can configure the time lags at will, depending on the conditions of your experiment. Three formats are accepted:

1.  **`[min, max]` — a fixed integer range.** When the second value is an integer ≥ 1 and larger than the first, the fit uses every lag from `min` to `max`, the **same for all trajectories**. Example: `[1, 20]` uses lags 1, 2, …, 20.

2.  **`[min, fraction]` — a per-trajectory (adaptive) range.** When the second value is between 0 and 1, it is read as a *fraction of each trajectory's length*: the fit uses lags from `min` up to `floor(fraction × length)` (with a small lower bound of 4), computed **independently for every trajectory**, so short trajectories automatically get a shorter maximum lag. Example (and default): `[1, 0.1]` fits from lag 1 up to 10 % of each trajectory's length.

3.  **`[t₁, t₂, t₃, …]` — an explicit list.** Any comma-separated list of positive integers is used verbatim as the set of lags for every trajectory. Example: `[1, 2, 4, 8]`.

For guidance on what to choose, we recommend:

*   Kepten, E., Weron, A., Sikora, G., Burnecki, K., & Garini, Y. (2015). Guidelines for the fitting of anomalous diffusion mean square displacement graphs from single particle tracking experiments. [PLOS ONE, 10(2), e0117722](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0117722).

You can analyse the **2D / X / Y** components independently, which makes it possible, for instance, to detect anisotropic diffusion in your experiment. The values shown when the window opens use the default time lags `[1,2]`. The histogram toolbar has **Normalize (%)** and **Log D axis**; the latter shows *D* on a logarithmic axis with log-spaced bins (values *D* ≤ 0 are left out).

{% include img align="center" name="Diffusion coefficient tab" src="/media/plugins/andi-j/diff-coeff-tab.png" caption="**Diffusion coefficient** histogram." %}

## Anomalous exponent

Estimates the anomalous exponent *α* with **two interchangeable methods**, selected from the **Method** drop-down:

<details markdown="1">
<summary><b>TMSD</b> — log–log fit of the tMSD curve (click to expand)</summary>

The anomalous exponent is obtained from a **log–log fit** of the time-averaged MSD (tMSD) versus the time lag Δ: α is the slope of `log(tMSD)` vs `log(Δ)`. The **Time lags** field controls which lags enter that fit, and follows the same format as for [*D*](#diffusion-coefficient) above.

**How to choose.** The key trade-off is statistics versus bias. At a lag Δ, the tMSD of a trajectory of length `L` is averaged over only `L − Δ` time origins, so **large lags are noisy** and can distort the slope; conversely you need enough points to define a slope reliably.

*   **Keep the maximum lag small relative to the trajectory length** (roughly 10–25 %). The adaptive form `[1, 0.1]` (the default) is the safest general choice because it scales automatically with each trajectory — recommended when your dataset mixes different lengths.
*   **Use a fixed `[min, max]`** only when all trajectories are of similar length and you want identical lags across them (e.g. for reproducibility).
*   **Start at lag 1** for clean/simulated data. For experimental data affected by localization noise or motion blur at the shortest lag, starting at 2 (e.g. `[2, 0.1]`) can give a cleaner slope.
*   Make sure the range spans **at least a few lags** (two is the minimum for a slope, but more gives a more stable fit).
*   Because the fit is in log–log space, the **frame interval does not affect α** (it only rescales the lag axis); the interval matters for *D*, not for the exponent.

</details>

<details markdown="1">
<summary><b>ML</b> — deep-learning prediction (click to expand)</summary>

Uses a neural network to predict the exponent, typically a much more accurate technique than the tMSD approach (as shown in the [1st AnDi Challenge](https://arxiv.org/abs/2105.06766)). Two options:

1.  **Default** — uses a pre-trained model that outperforms every method of the 1st AnDi Challenge on 2D trajectories (see [ML models](/plugins/andi-j/ml-models#andi-j-analysis)). This model internally also predicts the diffusion model, so running it automatically populates the [Diffusion Model](#diffusion-model) tab (see below).
2.  **Load** — allows you to load a custom α predictor. See [ML models](/plugins/andi-j/ml-models#custom-models-for-trajectory-analysis) for details.

</details>

Once the exponent is calculated, a histogram of the exponent per trajectory is shown. The table below it reports the exponent computed from an ensemble MSD fit, the most robust method **if** the dataset is homogeneous. If ML is used to predict α, a new column appears with the average over those predictions.

{% include img align="center" name="Anomalous exponent tab" src="/media/plugins/andi-j/anomalous-exponent-tab.png" caption="**Anomalous exponent** histogram, computed with the ML method." %}

## D vs α
{: #d-vs-alpha}

A scatter of **one point per trajectory** in the *D*–*α* plane, or a density of the same points. Both quantities are taken from the *last* computation in their respective tabs; change the parameters or methods there and this tab updates too.

The dropdown at the start of the toolbar chooses the view:

*   **Scatter** — one point per trajectory, with the **Select** tool for population tagging (below).
*   **Density** — a 2-D histogram of the same points, overlaid per experiment and tagged population in their colours, as in the [Trajectory Segmentation D vs α tab](/plugins/andi-j/trajectory-segmentation#d-vs-alpha), with **α bins**, **D bins** and **Log count scale**; the legend gives the number of trajectories of each. Selection and tagging are not available in this view; tagged populations appear as their own colour.

Features:

*   **Marginal KDEs** — the plots along the top and right edges show a kernel density estimate of the population for α and *D*, respectively.
*   **Population tagging** — in **Select** mode, *circle* (lasso) a cluster of points (see blue area in the figure below), type a name in **Population tag:** and click **Tag population**. The enclosed trajectories are recoloured to a shade of their parent colour and added as a new dataset to the [Turning Angles](#turning-angles) and [Diffusion Model](#diffusion-model) tabs. A trajectory can belong to several populations; where they overlap, the latest population is drawn on top. A management table below the plot lists each population (tag, source datasets, number of trajectories, **Show**, colour — click the colour to change it in every tab). Untick **Show** to hide a population from this plot only: its points take their parent's colour again. **Delete selected** deletes the highlighted populations (click, Ctrl- or Shift-click a row) from every tab, after a confirmation. Click **Save…** in the **Save** column to export the population's trajectories as a `csv` in the [input format](/plugins/andi-j/input-data) (`TRACK_ID, POSITION_X, POSITION_Y, POSITION_T, FRAME`), plus an `EXPERIMENT` column naming the experiment each trajectory comes from. The file can be loaded again in the Data Manager, which ignores the extra column; with a calibration, positions are written in μm and `POSITION_T` in seconds, so the file loads back calibrated. `TRACK_ID` keeps the trajectory's id when the population comes from one experiment and is renumbered from 0 when it mixes several, so ids stay unique; commas in experiment names are written as semicolons.
*   **Plot manipulation** — Log *D* axis toggle, rubber-band **Zoom**, **Pan**, **Reset view**, in both views.

{% include img align="center" name="D vs alpha tab" src="/media/plugins/andi-j/d-vs-alpha-tab.png" caption="**D vs α** in Scatter view, with marginal KDEs, a tagged population and the population table (top), and in Density view (bottom)." %}

## Diffusion Model

Classifies each trajectory into one of the five canonical anomalous-diffusion models: **ATTM, CTRW, FBM, LW, SBM** (see [Muñoz-Gil et al. (2021)](https://arxiv.org/abs/2105.06766) for more details). The predictions are done through an [ML model](/plugins/andi-j/ml-models), and shown as a **grouped bar chart** of the percentage of trajectories per experiment assigned to each model.

{% include notice icon="info" content="If a population was selected in the [D vs α](#d-vs-alpha) plot, it will appear as its own experiment in this tab." %}

{% include img align="center" name="Diffusion Model tab" src="/media/plugins/andi-j/diffusion-model-tab.png" caption="**Diffusion Model** classification bar chart." %}

## Turning Angles

A **polar rose histogram** of turning angles between successive displacement vectors, pooled per experiment and normalised to a fraction, so that experiments with different track counts are comparable.

{% include notice icon="info" content="If a population was selected in the [D vs α](#d-vs-alpha) plot, it will appear as its own experiment in this tab. In the example below, `population_normal_fast` is a population containing a few trajectories from `exp_FBM_normal`." %}

{% include img align="center" name="Turning Angles tab" src="/media/plugins/andi-j/turning-angles-tab.png" caption="**Turning Angles** polar rose." %}

## PSD

Ensemble-averaged **power spectral density** of the trajectories, based on [`andi_datasets.analysis.psd`](https://andichallenge.github.io/andi_datasets/lib_nbs/analysis.html#psd) (which wraps `scipy.signal.periodogram` with its defaults: unit sampling, boxcar window, constant detrend, one-sided, density scaling).

*   Each shown periodogram is averaged over all trajectories of an experiment on a shared log-frequency grid (from `1/max-length` up to the Nyquist frequency 0.5). Only the **global average** is shown — no per-track curves — with independent **2D / X / Y** selectors per experiment.
*   **Freq. points** sets the number of frequency bins; **Log–log** toggles the axes.
*   A **Draw line** tool (as in the [tMSD](#tmsd-visualization) tab) reports the slope of a reference line — useful since the PSD of an anomalous process scales as a power law in frequency (the spectral slope is related to the anomalous exponent).

To learn about the PSD for anomalous diffusion analysis, we recommend reading the following publications:

*   Krapf, D., et al. (2018). Power spectral density of a single Brownian trajectory: what one can and cannot learn from it. [New Journal of Physics, 20(2), 023029](https://iopscience.iop.org/article/10.1088/1367-2630/aaa67c).
*   Krapf, D., Lukat, N., Marinari, E., Metzler, R., Oshanin, G., Selhuber-Unkel, C., … & Xu, X. (2019). Spectral content of a single non-Brownian trajectory. [Physical Review X, 9(1), 011019](https://journals.aps.org/prx/abstract/10.1103/PhysRevX.9.011019).
*   Sposini, V., Krapf, D., Marinari, E., Sunyer, R., Ritort, F., Taheri, F., … & Oshanin, G. (2022). Towards a robust criterion of anomalous diffusion. [Communications Physics, 5(1), 305](https://www.nature.com/articles/s42005-022-01079-8).

{% include img align="center" name="PSD tab" src="/media/plugins/andi-j/psd-tab.png" caption="**PSD** tab with a drawn slope line." %}

## Summary

A table with **one row per experiment** and values aggregated over its trajectories. Click the ▸ next to an experiment's name to show its **X** and **Y** rows. Click a column header marked ⓘ for a description of the value; the descriptions are listed below.

*   Values from the other tabs (*D*, α, eMSD) appear when the tab opens and are updated each time it is shown, so they follow the parameters chosen in those tabs.
*   **Compute** fills the trajectory statistics of every experiment: α₂, VACF, mean speed, step anisotropy, FMI, centre of mass and directness.
*   **α (ML)** and **Diffusion model** come from the ML model of the [Anomalous exponent](#anomalous-exponent) or [Diffusion Model](#diffusion-model) tab. Run it there to fill or update these values; **Compute** does not run it.
*   Yellow cells are not computed yet; hover over one to see where to compute it. Empty cells are values not defined for that row (for example FMI in 2D).
*   **Units** sets the units of *D*, mean speed and centre of mass. **Save table…** saves a `csv` with one row per experiment and component (`2D`, `X`, `Y`); values not defined or not computed are left empty.

{% include img align="center" name="Summary tab" src="/media/plugins/andi-j/summary.png" caption="**Summary** tab with two experiments expanded to their X and Y rows, after **Compute** and the ML model." %}

In the formulas, r(t) = (x(t), y(t)) is a trajectory sampled every Δt (one frame), and ⟨…⟩ is the average over all times and trajectories of the experiment.

*   **N**, **Length** — number of trajectories, and their length in frames as median (min–max).
*   **D** — mean over the trajectories of *D* from the [Diffusion coefficient](#diffusion-coefficient) tab.
*   **Dₓ / Dᵧ** — ratio of the diffusion coefficients along x and y, computed from the X and Y values of **D**. A value of 1 means isotropic diffusion; values far from 1 mean faster motion along one axis.
*   **α (tMSD)** — mean of the anomalous exponents of the trajectories, each from a log–log linear fit of the trajectory's tMSD with the time lags of the [Anomalous exponent](#anomalous-exponent) tab. α < 1: subdiffusion · α = 1: normal diffusion · α > 1: superdiffusion.
*   **α (eMSD)** — anomalous exponent from a log–log linear fit of the ensemble MSD, eMSD(Δ) ∝ Δ<sup>α</sup>, over the lags of the [tMSD Visualization](#tmsd-visualization) tab. The eMSD averages the squared displacement from the first frame of each trajectory. If α (eMSD) ≠ α (tMSD), the time and ensemble averages differ (see **Ergodicity gap**). *Reference:* R. Metzler, J.-H. Jeon, A. G. Cherstvy, E. Barkai, [*Phys. Chem. Chem. Phys.* **16**, 24128 (2014)](https://doi.org/10.1039/C4CP03465A).
*   **α (ML)** — mean of the α predicted by the ML model for each trajectory.
*   **Diffusion model** — the most frequent diffusion model among the trajectories, with the percentage of trajectories assigned to it.
*   **Ergodicity gap** — ratio of the time-averaged and ensemble-averaged MSDs, averaged over the lags of the [tMSD Visualization](#tmsd-visualization) tab: G = mean over Δ of ⟨tMSD(Δ)⟩ / eMSD(Δ). G ≈ 1: time and ensemble averages agree, as for an ergodic process such as Brownian motion or fractional Brownian motion. G ≠ 1: weak ergodicity breaking, as for continuous-time random walks (CTRW), annealed transient time motion (ATTM) or ageing systems. *References:* Y. He, S. Burov, R. Metzler, E. Barkai, [*Phys. Rev. Lett.* **101**, 058101 (2008)](https://doi.org/10.1103/PhysRevLett.101.058101); R. Metzler *et al.* (2014), above.
*   **α₂ (non-Gaussian)** — measures whether the displacements over one frame are Gaussian: α₂ = ⟨\|r\|⁴⟩ / ((1 + 2/d) ⟨\|r\|²⟩²) − 1, where d is the number of dimensions: 2 for 2D, 1 for X or Y. In 1D this is α₂ = ⟨Δx⁴⟩ / (3⟨Δx²⟩²) − 1. α₂ = 0 for Gaussian displacements. α₂ > 0 means heavier tails than a Gaussian. This typically comes from heterogeneity: particles, or parts of trajectories, with different diffusion coefficients ("Fickian yet non-Gaussian" diffusion). *Reference:* B. Wang, J. Kuo, S. C. Bae, S. Granick, [*Nat. Mater.* **11**, 481 (2012)](https://doi.org/10.1038/nmat3308).
*   **VACF** — correlation between consecutive steps, normalised by the step variance: C = ⟨v(t) · v(t+Δt)⟩ / ⟨\|v(t)\|²⟩, with v(t) = r(t+Δt) − r(t). C ≈ 0: uncorrelated steps (Brownian motion, continuous-time random walk). C < 0: anti-persistent steps (fractional Brownian motion with α < 1 gives C = 2<sup>α−1</sup> − 1, confinement). C > 0: persistent steps (directed or superdiffusive motion). Static localisation noise pushes C towards −0.5. A strongly negative C can therefore also mean noisy data. *Reference:* S. Burov, J.-H. Jeon, R. Metzler, E. Barkai, [*Phys. Chem. Chem. Phys.* **13**, 1800 (2011)](https://doi.org/10.1039/C0CP01879A).
*   **Mean speed** — accumulated distance of each trajectory divided by its duration, averaged over the trajectories: v = ⟨ Σ \|r(t+Δt) − r(t)\| / (T Δt) ⟩. For X and Y, \|Δx\| or \|Δy\| replaces the step length. The value depends on the frame rate and on localisation noise, which adds apparent motion, so compare it only between experiments recorded the same way.
*   **Step anisotropy** — orientation order of the steps. With φ = atan2(Δy, Δx) the direction of each one-frame step: S = ⟨cos 2φ⟩. S = 1: all steps along x. S = −1: all steps along y. S = 0: no preferred axis. Opposite steps (φ and φ + 180°) count the same, so S measures alignment along an axis, not drift in one direction (see **FMI** and **Centre of mass**).
*   **FMI** (forward migration index) — net displacement along one axis relative to the path length, averaged over the trajectories: FMI<sub>x</sub> = ⟨ (x<sub>end</sub> − x<sub>start</sub>) / d<sub>acc</sub> ⟩, with d<sub>acc</sub> = Σ \|r(t+Δt) − r(t)\|. FMI<sub>y</sub> is the same with y. It ranges from −1 to 1. Values near 0 mean no drift along that axis. In a chemotaxis assay with the gradient along one axis, FMI along the gradient measures how efficiently the cells follow it.
*   **Centre of mass** — mean end point of the trajectories, each shifted to start at the origin: M<sub>end</sub> = ⟨ r<sub>end</sub> − r<sub>start</sub> ⟩. M<sub>end</sub> close to (0, 0) means no net drift. Its x and y components give the direction of the drift; the 2D value is its distance from the origin.
*   **Directness** — straight-line distance between start and end divided by the path length, averaged over the trajectories: Directness = ⟨ \|r<sub>end</sub> − r<sub>start</sub>\| / d<sub>acc</sub> ⟩. It ranges from 0 to 1, where 1 is a straight line. It decreases with trajectory length: for Brownian motion, Directness ≈ 1/√T for trajectories of T frames, since the net displacement grows as √T and the path length as T. Localisation noise also lowers it. Compare it only between experiments with similar lengths and frame rates, for example by setting the same **Max. length** for all files in the [Data Manager](/plugins/andi-j/input-data#loading-trajectories).

*Reference* for mean speed, FMI, centre of mass and directness: P. Zengel *et al.*, [*BMC Cell Biol.* **12**, 21 (2011)](https://doi.org/10.1186/1471-2121-12-21).
