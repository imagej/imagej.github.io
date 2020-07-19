You can use ImageJ from [https://python.org/ Python]:

* If you want to write ImageJ [[scripts]] in the Python language, which run from inside ImageJ similar to other scripts, check out the [[Jython Scripting]] page.
** '''Advantage:''' Such scripts are able to take advantage of SciJava [[script parameters]] and run within several tools that support [[SciJava]].
** '''Disadvantage:''' You will not be able to use many of the Python modules requiring native code such as numpy or scipy.
** '''Disadvantage:''' As of this writing, Jython implements only Python 2, not Python 3.

* If you want to embed an ImageJ inside of your Python code, such as within a [https://jupyter.org/ Jupyter notebook] using the Python kernel, check out the [https://pypi.org/project/pyimagej/ pyimagej] Python package. It allows you to create an ImageJ with full access to its API from Python. See the [https://imagej.github.io/tutorials/ ImageJ tutorial notebooks] for an introduction.
** '''Advantage:''' It is possible to combine ImageJ with other image analysis libraries like [[scikit-image]], [[ITK]], [[OpenCV]] and more in a single Python program.
** '''Disadvantage:''' Wrapping ImageJ in Python has some limitations and bugs, particularly surrounding use of [[ImageJ1]] features, compared to using ImageJ from Java-based kernels such as [https://beakerx.com/ BeakerX].

[[Category:Development]]
