---
title: Python
section: Extend:Scripting:Languages
---

You can use ImageJ from [Python](https://python.org/):

-   If you want to write ImageJ [scripts](/scripting) in the Python language, which run from inside ImageJ similar to other scripts, check out the [Jython Scripting](/scripting/jython) page.
    -   **Advantage:** Such scripts are able to take advantage of SciJava [script parameters](/scripting/parameters) and run within several tools that support [SciJava](/libs/scijava).
    -   **Disadvantage:** You will not be able to use many of the Python modules requiring native code such as numpy or scipy.
    -   **Disadvantage:** As of this writing, Jython implements only Python 2, not Python 3.

-   If you want to embed [ImageJ2](/software/imagej2) inside of your Python code, such as within a [Jupyter notebook](https://jupyter.org/) using the Python kernel, check out the [PyImageJ](/scripting/pyimagej) Python package. It allows you to create an ImageJ2 gateway with full access to its API from Python. See the [ImageJ2 tutorial notebooks](/tutorials/notebooks) for an introduction.
    -   **Advantage:** It is possible to combine ImageJ with other image analysis libraries like [scikit-image](https://scikit-image.org/), [ITK](/software/itk), [OpenCV](/software/opencv) and more in a single Python program.
    -   **Disadvantage:** Wrapping ImageJ in Python has some limitations, particularly surrounding use of [original ImageJ](/software/imagej) features when running [headless](/scripting/headless).
 
    {% include notice icon="info" content='If you are new to Python or image analysis using Python and would like to learn about it, check out the [tutorials](https://imaging.epfl.ch/field-guide/sections/python/#tutorials) and [resources](https://imaging.epfl.ch/field-guide/sections/python/#tutorials) from the [EPFL Center for Imaging - image analysis field guide](https://imaging.epfl.ch/field-guide/index.html) ' %}
