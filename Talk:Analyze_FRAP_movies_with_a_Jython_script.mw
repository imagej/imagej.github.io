this seems to be broken on linux 64 bit java 1.8, ij 1.51c ?
is the import wrong?
Dan

<pre>
Started New_.py at Tue Jun 28 12:45:12 CEST 2016
Traceback (most recent call last):
  File "New_.py", line 40, in <module>
	at ij.ImageStack.getProcessor(ImageStack.java:269)
	at sun.reflect.GeneratedMethodAccessor32.invoke(Unknown Source)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:497)

java.lang.IllegalArgumentException: java.lang.IllegalArgumentException: Argument out of range: 11

	at org.python.core.Py.JavaError(Py.java:495)
	at org.python.core.Py.JavaError(Py.java:488)
	at org.python.core.PyReflectedFunction.__call__(PyReflectedFunction.java:188)
	at org.python.core.PyReflectedFunction.__call__(PyReflectedFunction.java:204)
	at org.python.core.PyObject.__call__(PyObject.java:404)
	at org.python.core.PyObject.__call__(PyObject.java:408)
	at org.python.core.PyMethod.__call__(PyMethod.java:124)
	at org.python.pycode._pyx1.f$0(New_.py:127)
	at org.python.pycode._pyx1.call_function(New_.py)
	at org.python.core.PyTableCode.call(PyTableCode.java:165)
	at org.python.core.PyCode.call(PyCode.java:18)
	at org.python.core.Py.runCode(Py.java:1275)
	at org.scijava.plugins.scripting.jython.JythonScriptEngine.eval(JythonScriptEngine.java:76)
	at org.scijava.script.ScriptModule.run(ScriptModule.java:174)
	at org.scijava.module.ModuleRunner.run(ModuleRunner.java:167)
	at org.scijava.module.ModuleRunner.call(ModuleRunner.java:126)
	at org.scijava.module.ModuleRunner.call(ModuleRunner.java:65)
	at org.scijava.thread.DefaultThreadService$2.call(DefaultThreadService.java:191)
	at java.util.concurrent.FutureTask.run(FutureTask.java:266)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1142)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:617)
	at java.lang.Thread.run(Thread.java:745)
Caused by: java.lang.IllegalArgumentException: Argument out of range: 11
	at ij.ImageStack.getProcessor(ImageStack.java:269)
	at sun.reflect.GeneratedMethodAccessor32.invoke(Unknown Source)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:497)
	at org.python.core.PyReflectedFunction.__call__(PyReflectedFunction.java:186)
	... 19 more
</pre>


----
Sorry, I can't reproduce (on Win7, Java8, ImageJ 2.0.0-rc-49/1.51d)

What are the steps you were taking? What update sites do you have activated?

--[[User:Eglinger|eglinger]] ([[User talk:Eglinger|talk]]) 06:03, 28 June 2016 (CDT)


----
Oh, wait:
<pre>
Caused by: java.lang.IllegalArgumentException: Argument out of range: 11
	at ij.ImageStack.getProcessor(ImageStack.java:269)
</pre>

Let me guess: you were running the script on a 10-frame stack and didn't adjust the line:

 # Specify up to what frame to fit and plot.
 n_slices = 30


Right?

In the future, let's post discussions like this one on the [http://forum.imagej.net/ forum], where the chance is higher that someone else than the last author of this page will actually respond.

--[[User:Eglinger|eglinger]] ([[User talk:Eglinger|talk]]) 06:11, 28 June 2016 (CDT)

-----
yes that's it!
I should have read it first!!!!
Dan
