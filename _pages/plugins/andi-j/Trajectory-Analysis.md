This tool allows to perform single-trajectory analysis of the input experiments. Every tab has a side **Experiments** panel where each
experiment can be toggled on/off and, where
relevant, restricted to the **2D**, **X**, or **Y** component.

> **Saving data:** In each tab you can save the relevant quantity as a `csv` file for further analysis.

## tMSD Visualization

This tab shows the time-averaged MSD curves for each experiment, allowing for an initial visual inspection of the diffusive properties of the loaded experiments.

- Per-experiment selectors for **Avg** (the average tMSD), **All** (every
  individual trajectory, faint), and **eMSD** (ensemble MSD, dashed).
- The lag axis is controlled by **Min lag**, **Max lag**, **Log-spaced**, and a
  **Frame interval** / **Unit**. The number of lag points is chosen
  automatically (every integer lag when linear; capped, log-spaced sampling when
  log-spaced is selected).
- **Draw line** lets you place a reference line and read its slope live; in
  log–log mode the slope is labelled *α*, since it corresponds to the anomalous exponent.
- **eMSD vs tMSD as an ergodicity test:** comparing the eMSD curve to the Avg tMSD shows whether the process is ergodic (the two coincide) or non-ergodic (they differ).

![tMSD tab with eMSD overlay](images/tmsd_tab.png)

## Diffusion coefficient

Estimates the diffusion coefficient *D* per trajectory from a linear fit of the
tMSD vs lag-time (mirroring `andi_datasets` `get_diff_coeff`), shown as a
histogram. Dashed lines show the mean over the experiment.

You can configure the time lags at will, depending on the conditions of your experiment. For guidance on what to choose, we recommend:

- Kepten, E., Weron, A., Sikora, G., Burnecki, K., & Garini, Y. (2015). Guidelines for the fitting of anomalous diffusion mean square displacement graphs from single particle tracking experiments. [PLOS ONE, 10(2), e0117722.](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0117722)

You can analyse the **2D / X / Y** components independently, which makes it possible, for instance, to detect anisotropic diffusion in your experiment. Frame interval and units can be chosen based on your setup.

![Diffusion coefficient histogram](images/diff_coeff_tab.png)

## Anomalous exponent

Estimates the anomalous exponent *α* with **two interchangeable methods**,
selected from the **Method** drop-down:

<details markdown="1">
<summary><b>TMSD</b> — log–log fit of the tMSD curve (click to expand)</summary>

The anomalous exponent is obtained from a **log–log fit** of the time-averaged MSD (tMSD) versus the time lag Δ: α is the slope of `log(tMSD)` vs `log(Δ)`. The **Time lags** field controls which lags enter that fit. It accepts three formats:

1. **`[min, max]` — a fixed integer range.** When the second value is an integer ≥ 1 and larger than the first, the fit uses every lag from `min` to `max`, the **same for all trajectories**. Example: `[1, 20]` uses lags 1, 2, …, 20.

2. **`[min, fraction]` — a per-trajectory (adaptive) range.** When the second value is between 0 and 1, it is read as a *fraction of each trajectory's
   length*: the fit uses lags from `min` up to `floor(fraction × length)` (with a
   small lower bound of 4), computed **independently for every trajectory**, so
   short trajectories automatically get a shorter maximum lag. Example (and
   default): `[1, 0.1]` fits from lag 1 up to 10 % of each trajectory's length.

3. **`[t₁, t₂, t₃, …]` — an explicit list.** Any comma-separated list of positive
   integers is used verbatim as the set of lags for every trajectory. Example:
   `[1, 2, 4, 8]`.

**How to choose.** The key trade-off is statistics versus bias. At a lag Δ, the
tMSD of a trajectory of length `L` is averaged over only `L − Δ` time origins, so
**large lags are noisy** and can distort the slope; conversely you need enough
points to define a slope reliably.

- **Keep the maximum lag small relative to the trajectory length** (roughly
  10–25 %). The adaptive form `[1, 0.1]` (the default) is the safest general
  choice because it scales automatically with each trajectory — recommended when
  your dataset mixes different lengths.
- **Use a fixed `[min, max]`** only when all trajectories are of similar length
  and you want identical lags across them (e.g. for reproducibility).
- **Start at lag 1** for clean/simulated data. For experimental data affected by
  localization noise or motion blur at the shortest lag, starting at 2 (e.g.
  `[2, 0.1]`) can give a cleaner slope.
- Make sure the range spans **at least a few lags** (two is the minimum for a
  slope, but more gives a more stable fit).
- Because the fit is in log–log space, the **frame interval does not affect α**
  (it only rescales the lag axis); the interval matters for *D*, not for the
  exponent.

</details>

<details markdown="1">
<summary><b>ML</b> — deep-learning prediction (click to expand)</summary>

Uses a neural network to predict the exponent, typically a much more accurate technique than the tMSD approach (as shown in the [AnDi 1 Challenge](https://arxiv.org/abs/2105.06766)). Two options:

1) **Default**: uses a pre-trained model of comparable accuracy to the best models in the AnDi 1 Challenge. This model internally also predicts the diffusion model, so running it automatically populates the **Diffusion Model** tab (see below).
2) **Load**: allows you to load a custom α predictor. See [ML Models](ML-Models) for details on this.

</details>

Once the exponent is calculated, a histogram of the exponent per trajectory is shown. The table below it reports the exponent computed from an ensemble MSD fit, the most robust method **IF** the dataset is homogeneous. If ML is used to predict α, a new column appears with the average over those predictions.

![Anomalous exponent histogram (ML)](images/anomalous_exponent_tab.png)

## D vs α

A scatter of **one point per trajectory** in the *D*–*α* plane. Both quantities are taken from the *last* computation in their respective tabs; change the parameters or methods there and this tab updates too.

Features:

- **Marginal KDEs:** the plots along the top and right edges show a kernel density estimate of the population for α and *D*, respectively.
- **Population tagging:** In **Select** mode, *circle* (lasso) a cluster of points (see blue area in the figure below), type a name in **Population tag:** and click **Tag population**. The enclosed trajectories are recoloured to a shade of their parent colour and added as a new dataset to the **Turning Angles** and **Diffusion Model** tabs. A management table below the plot lists each population (tag, source datasets, colour — click the colour to change it).
- **Plot manipulation:** Log D axis toggle, rubber-band **Zoom**, **Pan**, **Reset view**.

![D vs α scatter with marginal KDEs and a tagged population](images/D_vs_alpha_tab.png)

## Diffusion Model

Classifies each trajectory into one of the five canonical anomalous-diffusion
models: **ATTM, CTRW, FBM, LW, SBM** (see [this paper](https://arxiv.org/abs/2105.06766) for more details). The predictions are done through an ML model (see details [here](ML-Models)), and shown a **grouped bar chart** of the percentage of trajectories per experiment assigned
to each model.

> If a population was selected in the D vs α plot, it will appear as its own experiment in this tab.

![Diffusion-model classification bar chart](images/diffusion_model_tab.png)

## Turning Angles

A **polar rose histogram** of turning angles between successive displacement
vectors, pooled per experiment and normalised to a fraction, so that experiments with different track counts are
comparable.

> If a population was selected in the D vs α plot, it will appear as its own experiment in this tab (example: population_normal_fast is a population containing few trajectories from exp_FBM_normal).

![Turning-angle polar rose](images/turning_angles_tab.png)

## PSD

Ensemble-averaged **power spectral density** of the trajectories, based on
[`andi_datasets.analysis.psd`](https://andichallenge.github.io/andi_datasets/lib_nbs/analysis.html#psd) (which wraps `scipy.signal.periodogram` with its
defaults: unit sampling, boxcar window, constant detrend, one-sided, density
scaling).

- Each shown periodogram is averaged over all trajectories of an
  experiment on a shared log-frequency grid (from `1/max-length` up to the
  Nyquist frequency 0.5). Only the **global average** is shown — no per-track
  curves — with independent **2D / X / Y** selectors per experiment.
- **Freq. points** sets the number of frequency bins; **Log–log** toggles the
  axes.
- A **Draw line** tool (as in the tMSD tab) reports the slope of a reference
  line — useful since the PSD of an anomalous process scales as a power law in
  frequency (the spectral slope is related to the anomalous exponent).

**Resources:** to learn about the PSD for anomalous diffusion analysis, we recommend reading the following publications:

- Krapf, D., et al. (2018). Power spectral density of a single Brownian trajectory: what one can and cannot learn from it. [New Journal of Physics, 20(2), 023029.](https://iopscience.iop.org/article/10.1088/1367-2630/aaa67c)

- Krapf, D., Lukat, N., Marinari, E., Metzler, R., Oshanin, G., Selhuber-Unkel, C., ... & Xu, X. (2019). Spectral content of a single non-Brownian trajectory. [Physical Review X, 9(1), 011019.](https://journals.aps.org/prx/abstract/10.1103/PhysRevX.9.011019)

- Sposini, V., Krapf, D., Marinari, E., Sunyer, R., Ritort, F., Taheri, F., ... & Oshanin, G. (2022). Towards a robust criterion of anomalous diffusion. [Communications Physics, 5(1), 305.](https://www.nature.com/articles/s42005-022-01079-8)

![PSD tab with a drawn slope line](images/psd_tab.png)
