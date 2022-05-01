---
mediawiki: CARE
title: CARE
artifact: de.csbdresden:csbdeep
categories: [Uncategorized]
---

## Install

### ImageJ update site

The CSBDeep plugin can be installed from the ImageJ update site [1](http://sites.imagej.net/CSBDeep/). See the [CSBDeep Wiki Pages](https://github.com/CSBDeep/CSBDeep_website/wiki/CSBDeep-in-Fiji) for more details.

### From source

1.  Clone this repository.
2.  Run the following command from inside the repo:

```shell
mvn -Dimagej.app.directory=/path/to/Fiji.app/ -Ddelete.other.versions=true
```

## Run demos

1.  Download the [exemplary image data](http://csbdeep.bioimagecomputing.com/exemplary-image-data.zip)
2.  Open Fiji.
3.  Open an example image, e.g. `tribolium.tif`.
4.  Run the plugin via {% include bc path="Plugins | CSBDeep | Demo" %}.
5.  Run the plugin by pressing `Ok`.

If all goes well, an image will be displayed representing the result of the model execution.

See the [CSBDeep Wiki Pages](https://github.com/CSBDeep/CSBDeep_website/wiki/CSBDeep-in-Fiji) for more details.

## Run your own model

1.  Use the [python code](https://github.com/CSBDeep/CSBDeep) to train your network with your data. Export it as ZIP.
2.  Open Fiji.
3.  Open an image.
4.  Run the plugin for any network via {% include bc path="Plugins | CSBDeep | Run your network" %}.
5.  Load your exported network by pressing `Browse` on the `Import model (.zip)` line.
6.  Run the plugin by pressing `Ok`.

If all goes well, an image will be displayed representing the result of the model execution.

See the [CSBDeep Wiki Page](https://github.com/CSBDeep/CSBDeep_website/wiki/Your-Model-in-Fiji) for more details.

## GPU support

Please read [this page](/develop/tensorflow) for GPU support.

## License

This project is licensed under the BSD 2-clause "Simplified" License -- see the [LICENSE.txt](https://github.com/CSBDeep/CSBDeep_fiji/blob/master/LICENSE.txt) file for details.
