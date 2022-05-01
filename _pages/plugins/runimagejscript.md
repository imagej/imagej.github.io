---
title: RunImageJScript
name: RunImageJScript
affiliation: Center for Open Bioimage Analysis | https://openbioimageanalysis.org/
dev-status: Active
support-status: Active
source-url: https://github.com/CellProfiler/CellProfiler-plugins/
team-lead: '@hinerm'
team-developers: '@alicelucas, @bethac07, @hinerm'
team-maintainers: '@alicelucas, @hinerm'
icon: /media/icons/cellprofiler.png
categories: [CellProfiler]
---

RunImageJScript is a [CellProfiler](/software/cellprofiler) plugin that allows the addition of a new module type that runs ImageJ scripts. Built on the [PyImageJ](/scripting/pyimagej) core, image data can be freely exchanged between the two applications across what has long been a Java-Python boundary.

## Installation

{% include notice icon="warning" content="Note: you will need to build CellProfiler from source to support RunImageJScript" %}

CellProfiler has a [plugin mechanism](https://github.com/CellProfiler/CellProfiler/blob/v4.2.1/cellprofiler/data/help/other_plugins.rst) that allows runtime extension of modules, with the caveat that **plugins requiring external libraries are not supported out-of-the-box**. Unfortunately this includes `RunImageJScript` due to its dependency on PyImageJ and related software.

### Build from source

You will need to create a python environment (whether through [venv](https://docs.python.org/3/tutorial/venv.html), [conda](https://docs.conda.io/en/latest/), or your systemwide environment) that contains both PyImageJ and CellProfiler:

1. Activate the environment of your choice
1. [Install PyImageJ](https://github.com/imagej/pyimagej/blob/1.0.2/doc/Install.md)
1. Install [Maven](/develop/maven), either by [downloading it](https://maven.apache.org/) or through your platform's package manager. The `mvn` command must be available on your system path.
1. Using [Git](/develop/git), clone {% include github org='CellProfiler' repo='CellProfiler' label='CellProfiler' %} to get the source code
1. On the [CellProfiler wiki](https://github.com/CellProfiler/CellProfiler/wiki) follow the installation instructions appropriate for your operating system

### Add CellProfiler-plugins


1. Using [Git](/develop/git), clone {% include github org='CellProfiler' repo='CellProfiler-plugins' label='CellProfiler-plugins' %} to get the `RunImageJScript` module
1. Open the `CellProfiler` you installed previously and set the `CellProfiler plugins directory` to the top level of the `CellProfiler-plugins` repository you just cloned
1. Restart `CellProfiler` to complete the installation

![CellProfiler preferences screen](/media/plugins/cellprofiler/cp_prefs.png)

## Using the RunImageJScript module

After [Installation](#Installation) we can now create `RunImageJScript` modules in a running CellProfiler.

1. Use {% include bc path='Edit | Add Module | Advanced | RunImageJScript' %} to add the new module to your pipeline
1. Select how your ImageJ/Fiji will be initialized. This follows the same principles of [PyImageJ initialization](https://github.com/imagej/pyimagej/blob/master/doc/Initialization.md#ways-to-initialize):
   * ![RunImageJScript local initialization](/media/plugins/cellprofiler/cp_init_local.png) ![RunImageJScript endpoint initialization](/media/plugins/cellprofiler/cp_init_endpoint.png) ![RunImageJScript latest initialization](/media/plugins/cellprofiler/cp_init_latest.png)
   * **Local** will point to a `Fiji.app` on disk. This is the only option which does not automatically download and cache additional assets
   * **Endpoint** will take a list of one or more endpoint(s), e.g. `sc.fiji:fiji:2.3.1`
   * **Latest** will default to the latest release
1. Select your ImageJ script to run. This can be any ImageJ2-style script, so it is highly recommended to read about [Scripting in ImageJ](https://imagej.net/scripting/) to understand the basic concepts and syntax. You can select scripts of any supported language (not just Python). One starting point are the [Tutorials script templates]( https://github.com/imagej/imagej-scripting/blob/imagej-scripting-0.8.3/src/main/resources/script_templates/Tutorials/). There are a few additional notes about scripting particular to RunImageJScript:
   * ![Select script](/media/plugins/cellprofiler/cp_select_script.png)
   * Note that saving your CellProfiler workflow will save the *path* to the script, but not the script's body. You will have to version and distribute the script with the workflow to attain reproducibility.

1. Click the `Get parameters from script` button to detect your script's parameters and expose them in CellProfiler. Note that the first time you run this it may be slow as the Java process running ImageJ is created. Subsequent parsing within the same CellProfiler session should be much faster.
   * ![Parsing parameters](/media/plugins/cellprofiler/cp_parse_params.png)
   * `@Parameters` that are Image or basic (numeric, text) types will be automatically converted to CellProfiler settings. This may mean scripts with specialized parameters are not suitable for RunImageJScript at this time
1. Adjust the parameter values as needed
   * ![Set parameters](/media/plugins/cellprofiler/cp_set_params.png)
   * Parameter settings can be removed from the CellProfiler GUI. This will stop outputs for showing. For inputs, ImageJ tries to make sensible guesses about defaults, but removing a critical input may cause the script to fail.
1. *(Optional)* Disable `Adjust image type`
   * ![Adjust image type](/media/plugins/cellprofiler/cp_adjust_image.png)
   * This setting is enabled by default because ImageJ typically expects images to be an unsigned integer type, while CellProfiler always uses signed float types. It should only be disabled if your script accounts for images being signed floats.
1. Run your workflow
   * ![Output](/media/plugins/cellprofiler/cp_results.png)
   * If `RunImageJScript` is your only module you can run things at this point (assuming you've loaded image(s) into the pipeline). You can also connect more modules up/downstream as desired.

## Troubleshooting

If you run into any issues, please connect with us on [the Image.sc forum](https://forum.image.sc/).
