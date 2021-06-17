---
title: 2015-02-09 - ImageJ 2.0.0-rc-24 released
---

Today, the [ImageJ team](/people) is pleased to announce a new public release candidate for [ImageJ2](/software/imagej2): version 2.0.0-rc-24.

{% include img align="right" width="450px" alt="SCIFIO rc-23 vs. rc-24 performance comparison" src="/media/news/scifio-rc23-rc24.png" %} {% include img align="right" width="450px" title="ImageJ 1.x vs. SCIFIO performance comparison" src="/media/news/imagej-scifio-rc24.png" %}

## What's new

First pass to reduce [SCIFIO](/libs/scifio) overhead:

-   Fixed a bug resulting in 2-second timeouts when calling SCIFIO from a macro ([b83c41e5](https://github.com/imagej/imagej-legacy/commit/b83c41e532ff5e17c9cb57ee93188b2b4dae0bba)).
-   Improved caching of common data (boosts performance throughout ImageJ2) ([7ae4103a...24051249](https://github.com/scijava/scijava-common/compare/7ae4103ac2d4503a6291c73dd3cd90f16656e821%5E...240512492ea754576819e681d1d79ce1db5270c3)).
-   SCIFIO configurations use more sensible defaults, favoring performance.
-   For some highly unscientific benchmarks of performance, see right.

First wave of improvements from 2015-01 Konstanz [ImageJ Ops](/libs/imagej-ops) [hackathon](/events/hackathons)

-   Better op code generation layer via Groovy parser ([c51ce639](https://github.com/imagej/imagej-ops/commit/c51ce639261c78922ff461267fd6e0e4522e85eb)).
-   Divide built-in op implementations into namespaces ([4e4a9e2f](https://github.com/imagej/imagej-ops/commit/4e4a9e2fc55736dfa96316f77c575bd46afda59f)).
-   Improve the project's build time ([1c9d1d05](https://github.com/imagej/imagej-ops/commit/1c9d1d05f418c1019a7e8e0674bfa6ee53365752)).
-   Better error messages when ops don't match ([4de825c6](https://github.com/imagej/imagej-ops/commit/4de825c6810eec43306093119dd6547b9c4d699c)).
-   Support for unary & binary arithmetic with primitives ([af05aff6](https://github.com/imagej/imagej-ops/commit/af05aff6f628155d12352a0c5fabaec0843c8d8b)).
-   New kernel implementations + FFT ops ([6c01f0ba](https://github.com/imagej/imagej-ops/commit/6c01f0ba6e67f21814c876f05d3bd490c7286a1e), [61062163](https://github.com/imagej/imagej-ops/commit/61062163bd4049348e78354a28371bf56d90e1ac), [e5567c3e](https://github.com/imagej/imagej-ops/commit/e5567c3e92fec104a13fa619317a597312831687)).

Updated messages for Refresh Menus & related commands to be more user-friendly (hopefully).

## What's next

Looking ahead at short-term goals:

-   Fixes/improvements for command-line functionality.
-   More SCIFIO performance improvements.
-   An automated troubleshooter to improve the average user experience.

## How to update

Use the {% include bc path='Help | Update...'%} command to update your [ImageJ](/software/imagej) installation. Please send any comments to the [ImageJ mailing list](/discuss/mailing-lists). Thanks for the continued feedback and support!

 
