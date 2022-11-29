---
title: PyImageJ
project: /software/imagej2
website: https://pypi.org/project/pyimagej/
source-url: https://github.com/imagej/pyimagej
dev-status: Active
team-lead: '@ctrueden'
team-developers: ['@ctrueden', '@elevans', '@gselzer']
team-debuggers: ['@ctrueden', '@elevans', '@gselzer', '@hinerm']
team-reviewers: ['@ctrueden', '@elevans', '@gselzer', '@hinerm']
team-support: ['@ctrueden', '@elevans', '@gselzer', '@hinerm']
team-maintainers: ['@ctrueden', '@elevans', '@hinerm']
doi: 10.1038/s41592-022-01655-4
---

{% include notice content="This page describes **PyImageJ**, a Python package
  making ImageJ functions accessible from Python. To write scripts in Jython,
  the JVM-based flavor of Python, see [Jython scripting](/scripting/jython)." %}

[PyImageJ](https://pypi.org/project/pyimagej/) is a [Python](/scripting/python)
wrapper for [ImageJ2](/software/imagej2). It also supports the
[original ImageJ](/software/imagej) via ImageJ2's
[legacy bridge](/libs/imagej-legacy).

PyImageJ provides a set of wrapper functions for integration between ImageJ and
Python. A major advantage of this approach is the ability to combine ImageJ
with other tools available from the Python software ecosystem, including NumPy,
SciPy, scikit-image, [CellProfiler](/software/cellprofiler),
[OpenCV](/software/opencv), [ITK](/software/itk) and more.

For further details about PyImageJ, including installation and usage
instructions, please see the project page on PyPI:

{% include link-banner url="https://pypi.org/project/pyimagej/" %}

## Publication

To cite PyImageJ, you can use:

{% include citation %}
