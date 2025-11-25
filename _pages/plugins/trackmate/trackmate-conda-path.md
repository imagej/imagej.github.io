---
title: Configuring TrackMate conda path
description: How to configure conda path to use Python tools in TrackMate.
categories: [Tracking, Segmentation]
artifact: sc.fiji:TrackMate
project: /software/fiji
---

The new v8 version of TrackMate ships many new detectors, trackers and actions that are based on existing Python tools. 
We introduced in TrackMate v8 a framework to facilitate the integration of Python tools that are deployed within a conda (or mamba, of any flavor) environment. 
Using these tools in TrackMate requires you to

- install a conda distribution on your computer.
- install the individual TrackMate modules that are you interested in.
- configure the path to your conda environment.

To install conda, we recommend using [miniforge](https://github.com/conda-forge/miniforge).
You can use the recommended settings for your platform.

The TrackMate modules that depend on Python and external tools are all optional and documented on this wiki.
[This path](/plugins/trackmate/index#trackmate-components) is a good starting point to find them.
If you try to use one of the Python TrackMate module without configuring conda (next step), an error will be shown in the TrackMate wizard.

To configure conda in TrackMate, launch Fiji.
In Fiji, click on the {% include bc path="Edit|Options|Configure TrackMate Conda path..."%} menu item.
This window should appear:

{% include img src="/media/plugins/trackmate/trackmate-configure-conda-01.png"  %}

In the first text box, simply enter the path to the conda (or mamba of any flavor) executable that you have installed and use on your system. 

In the second box, enter the path where the base conda installation is located.
Classically, this will be the home directory of the executable. 

Once you click OK, and if the parameters are correct, the log should output the list of conda environments found on your computer. 

{% include img src="/media/plugins/trackmate/trackmate-configure-conda-02.png"  %}

If this is correct, you can **relaunch Fiji for the new settings to be used**.

## How to find the right path and values on your system 

In a terminal (where conda is runnable), run the following
```sh
conda info
```


#### 1. Conda Executable Location


**How to find `{base_env}`**:
Look for the **`base environment`** line in `conda info` output.
Example:
```
base environment : /Users/username/mambaforge  (writable)
```
→ `{base_env} = /Users/username/mambaforge`.



Examples:

| **OS**       | **Path Format**                          | **Example**                             |
|--------------|-----------------------------------------|------------------------------------------|
| **Windows**  | `{base_env}\Scripts\conda.exe`         | `C:\ProgramData\miniconda3\Scripts\conda.exe` |
| **macOS/Linux** | `{base_env}/bin/conda`               | `/Users/username/mambaforge/bin/conda`    |


#### 2. `CONDA_ROOT_PREFIX`

This is **always the `base environment` path** from `conda info`.
Look for:
```
base environment : <PATH>  # <-- This is CONDA_ROOT_PREFIX
```

**Examples**:
- Windows: `C:\ProgramData\miniconda3`
- macOS/Linux: `/Users/username/mambaforge` or `/home/username/anaconda3`



### Quick Reference Table

| **Field**               | **Where to Look in `conda info`**       | **Example (Windows)**       | **Example (macOS/Linux)**      |
|-------------------------|----------------------------------------|-----------------------------|--------------------------------|
| **Conda Executable**    | `{base_env}/Scripts/conda.exe` or `{base_env}/bin/conda` | `C:\ProgramData\miniconda3\Scripts\conda.exe` | `/Users/username/mambaforge/bin/conda` |
| **`CONDA_ROOT_PREFIX`** | `base environment : <PATH>`           | `C:\ProgramData\miniconda3` | `/Users/username/mambaforge`   |

---

### **Platform-Specific Notes**

- **Windows**:
  - Use backslashes (`\`) and `.exe` (e.g., `Scripts\conda.exe`).
  - System-wide installs are often in `C:\ProgramData\`.
  - User installs are in `C:\Users\<username>\`.

- **macOS/Linux**:
  - Use forward slashes (`/`) and no `.exe` (e.g., `bin/conda`).
  - User installs are typically in `/Users/<username>/` or `/home/<username>/`.
  - System installs may be in `/opt/`.

- **Read-Only vs. Writable**:
  - If `conda info` shows `(read only)`, the installation is system-wide (requires admin rights).
  - If `(writable)`, it’s user-specific.

### Example


For instance on my system this yields:

```sh
❯ conda info

     active environment : base
    active env location : /Users/tinevez/mambaforge
            shell level : 1
       user config file : /Users/tinevez/.condarc
 populated config files : /Users/tinevez/mambaforge/.condarc
          conda version : 23.1.0
    conda-build version : not installed
         python version : 3.10.10.final.0
       virtual packages : __archspec=1=arm64
                          __osx=15.7.1=0
                          __unix=0=0
       base environment : /Users/tinevez/mambaforge  (writable)
      conda av data dir : /Users/tinevez/mambaforge/etc/conda
  conda av metadata url : None
           channel URLs : https://conda.anaconda.org/conda-forge/osx-arm64
                          https://conda.anaconda.org/conda-forge/noarch
          package cache : /Users/tinevez/mambaforge/pkgs
                          /Users/tinevez/.conda/pkgs
       envs directories : /Users/tinevez/mambaforge/envs
                          /Users/tinevez/.conda/envs
               platform : osx-arm64
             user-agent : conda/23.1.0 requests/2.28.2 CPython/3.10.10 Darwin/24.6.0 OSX/15.7.1
                UID:GID : 503:20
             netrc file : None
           offline mode : False
```

And with this I put this in TrackMate conda config:

{% include img src="/media/plugins/trackmate/trackmate-configure-conda-03.png"  %}
