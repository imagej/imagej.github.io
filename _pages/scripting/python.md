---
title: Python
section: Extend:Scripting:Languages
---

There are several ways to combine [Python](https://python.org/) with the [ImageJ ecosystem](/scripting#terminology). They differ in **process model**, **Python flavor**, and **how dependencies are managed** — each addresses a different use case.

## Ways to use Python with Fiji

| Option | Process model | Python flavor | pip packages | Notes |
|---|---|---|---|---|
| **[Jython](/scripting/jython)** | In-JVM | Python 2.7 syntax | No — Java libs only | Zero spawn overhead; full Java interop; runs as a [SciJava script](/scripting/basics). |
| **Fiji Python mode ([PyImageJ](/scripting/pyimagej))** | Single process: Python ↔ JVM | CPython 3 — one shared env | Yes — all scripts share one env | Launch [Fiji](/software/fiji) in Python mode via the `--python` flag or {% include bc path='Edit|Options|Python...' %}; the environment is built using [Appose](https://apposed.org). |
| **[Appose](https://apposed.org)** | Spawned subprocess | CPython 3 — per-script env | Yes — isolated per script | Each script runs in its own Python environment with its own dependencies. Usable from any SciJava script (a Groovy script can spin up an Appose Python subprocess). A prototype SciJava Python language built directly on Appose lives at [scripting-appose-python](https://github.com/scijava/scripting-appose-python). |
| **GraalPy** (experimental) | In-JVM | CPython 3 — partial compatibility | Partial | Not yet vetted with Fiji. In principle [GraalVM](https://www.graalvm.org/)'s [GraalPy](https://www.graalvm.org/python/) would give us in-JVM Python 3 with broader CPython compatibility than Jython. If you try it, please report back on the [Image.sc Forum](https://forum.image.sc/). |

## When to pick which

- **Want the lightest possible overhead and you're happy with Python 2.7 syntax?** Use [Jython](/scripting/jython). The script runs inside the JVM, so calls into Fiji are just normal Java method calls — no serialization, no process boundary. The catch: no `pip` packages, no `numpy`/`scipy`/`scikit-image`.

- **Want CPython 3 with the full PyPI ecosystem, and you'll be doing several things in one Python session?** Use **Fiji Python mode**. Fiji launches with Python as the host language, sharing a single environment across all scripts you run. Best for interactive sessions where the warm-up cost is paid once.

- **Have scripts with conflicting or heavy dependencies, or need reproducibility per script?** Use **Appose**. Each script declares its environment, Appose builds it on demand, and the script runs in a subprocess. Image data is shared with the JVM via named shared memory buffers, so there's no large copy on the wire.

- **Your host is Python and you want to call Fiji from there** — e.g., from a Jupyter notebook, or as part of a larger Python pipeline? Use [PyImageJ](/scripting/pyimagej). This is the same Python/JVM bridge as Fiji Python mode, but inverted: Python is the host, Fiji is the guest.

## Caveats

- **Jython** is Python 2.7 syntax only, and modules that require native code (`numpy`, `scipy`, …) are unavailable.
- **PyImageJ / Fiji Python mode** shares one environment across all scripts — dependency conflicts are your problem to resolve.
- **Appose** pays a subprocess-spawn cost per script and serializes any non-shared-memory data crossing the boundary.
- **GraalPy** is not currently validated to work with Fiji; this row is a placeholder for an option we expect is feasible but no one has demonstrated yet.

## Further reading

- [Jython Scripting](/scripting/jython) — Python 2.7 in-JVM, the long-standing default.
- [PyImageJ](/scripting/pyimagej) — calling Fiji from Python.
- [Appose](https://apposed.org/) — the cross-language inter-process bridge underlying both Fiji Python mode and per-script Appose use.
- [Appose+Fiji Workshop](https://fiji.github.io/i2k-2025-appose/) — adapt Python image processing into a Fiji script using Appose.
- [Scripting basics](/scripting/basics) — the SciJava scripting framework that hosts Jython (and the prototype Appose-Python language).

{% include notice class="fab fa-python" content='If you are new to Python or image analysis using Python and would like to learn about it, check out the [tutorials](https://imaging.epfl.ch/field-guide/sections/python/#tutorials) and [resources](https://imaging.epfl.ch/field-guide/sections/python/#tutorials) from the [EPFL Center for Imaging - image analysis field guide](https://imaging.epfl.ch/field-guide/) ' %}

