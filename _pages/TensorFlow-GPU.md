<b>The notes on this page are relevant for any tool shipping the <code>imagej-tensorflow</code> library (e.g. the update sites <code>imagej-tensorflow</code> and <code>CSBDeep</code>).</b>

== How to install TensorFlow GPU native libraries ==
GPU support is available for Linux and Windows machines with NVIDIA graphics cards. Please be warned that the TensorFlow Java native bindings are considered experimental and while some hardware / OS setups easily gained GPU support with the tools described on this page, on other machines we were not successful.

=== Install TensorFlow with GPU support for Java ===

# Open <code>Edit &gt; Options &gt; TensorFlow...</code>
# Choose the TensorFlow version matching your system
# Wait until the library is downloaded and installed (a popup will tell you when it’s done)
# Restart Fiji

[[File:tensorflow-installer.png|Edit &gt; Options &gt; TensorFlow…]]

You can for example switch from CPU to GPU by finding the option which is already selected (in the screenshot, <code>TF 1.15.0 CPU</code>) and choose the same TensorFlow version but with GPU support (e.g. <code>TF 1.15.0 GPU</code>).

=== Install the CUDA® Toolkit and cuDNN ===

Install these NVIDIA requirements to run TensorFlow with GPU support as described in the [https://www.tensorflow.org/install/gpu TensorFlow Documentation].

=== Which specific CUDA and cuDNN versions to install? ===

The CUDA and CuDNN versions displayed in the ImageJ TensorFlow installer (pictured above) are there to help you setup the right environment.

Example: The <code>CSBDeep</code> update site comes with <code>TensorFlow 1.15.0</code>, which requires <code>CUDA 10.1</code> and <code>cuDNN &gt;= 7.5.1</code>.

You can also use the filters on the top of the display to filter for a specific TensorFlow or CUDA version or to only list libraries with GPU support.

If you trained your model on a different TensorFlow version, running the model with with the default installation might fail. In this case, choose a specific TensorFlow version via <code>Edit &gt; Options &gt; TensorFlow...</code> and install CUDA and cuDNN compatible to the TensorFlow version.

== How to check if GPU support works ==
* Go to <code>Edit &gt; Options &gt; TensorFlow...</code> and make sure a GPU version is selected an no error is displayed
* When running a command using <code>imagej-tensorflow</code>, you can open the console via <code>Window &gt; Console</code>. There might be a line similar to this (in this example, no GPU version manually installed and therefore the default CPU TensorFlow version is used): 
<code><pre>
[INFO] No TF library found in /media/data/Programs/Fiji.app/lib/.
[INFO] Using default TensorFlow version from JAR: TF 1.15.0 CPU
</pre></code>
* Sometimes that's still not sufficient and even though the right library is chosen and the console confirms that, the GPU is not used. Please read the notes for the specific operating systems below.

== Hints for Windows ==

=== Set the environment variables ===
To set the CUDA environment variables in Windows, please follow the steps described on [https://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html#install-windows this page] (section 4.3.4).

=== Step-by-step example ===
Here is a step-by-step example of a successful GPU support installation (keep in mind that the person who tested this has little Windows experience and would benefit a lot from hints if this guide should be improved somehow):
* in Fiji, opened <code>Edit &gt; Options &gt; TensorFlow...</code> and switched to TF 1.15.0 GPU
* Installed <code>CUDA 10.1</code> from [https://developer.nvidia.com/cuda-10.1-download-archive-base?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exenetwork here]
* Downloaded <code>cuDNN 7.6.5 for CUDA 10.1</code> from [https://developer.nvidia.com/rdp/form/cudnn-download-survey here] (you need to register / login)
* copied cuDNN files from the ZIP into CUDA as described [https://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html#installwindows here]
* add <code>/PATH/TO/Fiji.app/lib/win64/tensorflow_jni.dll</code> to your <code>PATH</code> (here’s a guide [https://www.techjunkie.com/environment-variables-windows-10/ how to set system variables])

== Hints for Linux ==

=== Set the library path ===

<code>CUDA</code> and <code>cuDNN</code> need to be added to your system variables in order for Fiji to be able to use them. You can do that by adding lines similar to this to your <code>.bashrc</code> or <code>.zshrc</code> file:

<pre>export PATH=/usr/local/cuda/bin${PATH}
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:${LD_LIBRARY_PATH}</pre>
.. and then launch Fiji from command line. Another possibility is to edit the Fiji launcher to something like this:

<pre>export PATH=/usr/local/cuda/bin${PATH};export LD_LIBRARY_PATH=/usr/local/cuda/lib64:${LD_LIBRARY_PATH};/PATH_TO_APPS/Fiji.app/ImageJ-linux64</pre>


=== Multiple GPUs ===

If you have multiple CUDA enabled GPUs you may want to set the environment variable <code>CUDA_VISIBLE_DEVICES</code> to specify the GPU which should be used.

As CUDA will try to enumerate the GPUs by speed

<pre>$ export CUDA_VISIBLE_DEVICES=0</pre>

should give you only the fastest GPU. Execute this line before you start Fiji or put it into your <code>~/.bashrc</code> or set the environment variable somewhere else like in <code>~/.pam_environment</code>. See the documentation of your distribution for options on how to set environment variables.

'''Optional:'''

If this is not sufficient for your setup. You can find out the ID (in PCI bus order) of your GPU with:

<pre>$ nvidia-smi
Thu Sep 14 17:39:33 2017       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 375.66                 Driver Version: 375.66                    |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  NVS 310             Off  | 0000:A1:00.0     N/A |                  N/A |
| 30%   56C    P0    N/A /  N/A |    294MiB /   961MiB |     N/A      Default |
+-------------------------------+----------------------+----------------------+
|   1  TITAN Xp            Off  | 0000:03:00.0     Off |                  N/A |
| 23%   28C    P8     9W / 250W |      1MiB / 12189MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+</pre>
and also set the environment variable <code>CUDA_​DEVICE_​ORDER</code>:

<pre>$ export CUDA_​DEVICE_​ORDER=&quot;PCI_BUS_ID&quot;
$ export CUDA_VISIBLE_DEVICES=1</pre>

See the [http://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#env-vars CUDA Programming Guide] for more information.


== HELP ==
Is something not working? Please post your question [https://forum.image.sc in the forum]!
