---
title: FLIMKit-Bridge
icon: https://raw.githubusercontent.com/FLIMKit/FLIMKit/main/flimkit/UI/icon.png
---

FLIMKit-Bridge provides direct image and ROI exchange between [FLIMKit](https://github.com/FLIMKit/FLIMKit) and Fiji (ImageJ), and brings FLIMKit's tools -- fitting, phasor analysis, and stitching -- to Fiji.

## Installation

In the Fiji Updater, tick **FLIMKit-Bridge**. If it is not in the list yet, use `Add unlisted site` with name `FLIMKit-Bridge` and URL `https://sites.imagej.net/FLIMKit-Bridge/`.

FLIMKit-Bridge needs the [flimkit-bridge](https://github.com/FLIMKit/flimkit-bridge) server running in the background to talk to Fiji:

- If you already have FLIMKit's desktop app open, you're set -- the bridge starts automatically and its status is shown under `Tools > FLIMKit Bridge...`.
- Otherwise (e.g. a headless machine, or Fiji-only use), run:

```
pip install flimkit-bridge
flimkit-bridge
```

## How it works

Once connected, FLIMKit-Bridge adds commands under `Plugins > FLIMKit`:

- **ROIs** -- draw a region of interest in Fiji as usual, then **Send ROIs to FLIMKit** to push the ROI Manager contents back as GeoJSON (no image is returned, just a confirmation). **Fetch ROIs from FLIMKit** does the reverse: it loads FLIMKit's Regions table into Fiji's ROI Manager as new ROIs.
- **Images** -- **Fetch FLIMKit images** pulls the current intensity and lifetime images across as float32 TIFFs, opened directly as Fiji windows, with their measurement units carried in an `X-FLIMKit-Value-Unit` header.
- **Fitting** -- **Fit per-pixel lifetimes...** runs a per-pixel exponential fit and returns the resulting lifetime maps as new Fiji images. **Fit ROI decays...** sums the decay within each ROI first and returns the fit results per region -- useful when per-pixel data is too noisy.
- **Phasor plots** -- **Phasor plot...** opens an interactive phasor window for the current image; this is a visualization, not an exported image.
- **Stitching** -- **Stitch and fit a mosaic...** stitches a multi-position/tiled acquisition and returns the fitted result across the assembled mosaic.

## Supported file formats

**Fitting + phasor:** PicoQuant PTU (`.ptu`), Becker & Hickl SDT (`.sdt`), Photonscore LINCam (`.photons`), PicoQuant BIN (`.bin`), PicoQuant PHU (`.phu`), SimFCS B&H (`.b&h`), SimFCS BHZ (`.bhz`), ImSpector FLIM TIFF (`.tif`, `.tiff`), ISS Vista TDFLIM (`.iss-tdflim`, `.tdflim`), FLIM LABS imaging (`.json`), ISS time-tag (`.tagtime`, `.tagchannel`, `.tagdecay`).

**Phasor only:** ISS FD-FLIM (`.ifli`), SimFCS referenced (`.ref`, `.r64`), PhasorPy OME-TIFF (`.ome.tif`), FLIM LABS phasor (`.json`).

**Intensity only:** ISS intensity image (`.ifi`).

Measured IRFs can be supplied as `.xlsx`, `.csv`, or `.pck` files.

## Requirements

- Fiji 2.16 or newer with bundled JDK 21
- Python 3.12 or newer (only needed for the standalone bridge)

## Source

[FLIMKit/flimkit-fiji-bridge](https://github.com/FLIMKit/flimkit-fiji-bridge)
