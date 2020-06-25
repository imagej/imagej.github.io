{{Component
| project = CSBDresden
| name = CARE Fiji Plugin
| url = https://imagej.net/CARE
| source = {{GitHub | org=CSBDeep | repo=CSBDeep_fiji | tag=csbdeep-0.3.4}}
| license = [[BSD-2]]
| release = {{Maven | g=de.csbdresden | a=csbdeep | v=0.3.4 | label=0.3.4}}
| date = Tue Dec 11 00:00:00 CDT 2018
| devStatus = {{DevStatus | developer=yes | incubating=yes | obsolete=no}}
| supportStatus = {{SupportStatus | debugger=yes | reviewer=yes | support=yes}}
| founders = {{Person|frauzufall}}
| leads = {{Person|frauzufall}}, {{Person|HedgehogCode}}, {{Person|fjug}}
| developers = {{Person|frauzufall}}, {{Person|HedgehogCode}}, {{Person|fjug}}
| debuggers = {{Person|frauzufall}}, {{Person|HedgehogCode}}
| reviewers = {{Person|frauzufall}}, {{Person|HedgehogCode}}
| support = {{Person|frauzufall}}, {{Person|HedgehogCode}}
| maintainers = {{Person|frauzufall}}, {{Person|tpietzsch}}, {{Person|HedgehogCode}}
}}

== Install ==

=== ImageJ update site ===
The CSBDeep plugin can be installed from the ImageJ update site [http://sites.imagej.net/CSBDeep/]. See the [https://github.com/CSBDeep/CSBDeep_website/wiki/CSBDeep-in-Fiji CSBDeep Wiki Pages] for more details.

=== From source ===
# Clone this repository.
# Run the following command from inside the repo:
<code>
mvn -Dimagej.app.directory=/path/to/Fiji.app/ -Ddelete.other.versions=true
</code>

== Run demos ==
# Download the [http://csbdeep.bioimagecomputing.com/exemplary-image-data.zip exemplary image data]
# Open Fiji.
# Open an example image, e.g. `tribolium.tif`.
# Run the plugin via `Plugins > CSBDeep > Demo`.
# Run the plugin by pressing `Ok`.

If all goes well, an image will be displayed representing the result of the model execution.

See the [https://github.com/CSBDeep/CSBDeep_website/wiki/CSBDeep-in-Fiji CSBDeep Wiki Pages] for more details.

== Run your own model ==
# Use the [https://github.com/CSBDeep/CSBDeep python code] to train your network with your data. Export it as ZIP.
# Open Fiji.
# Open an image.
# Run the plugin for any network via `Plugins > CSBDeep > Run your network`.
# Load your exported network by pressing `Browse` on the `Import model (.zip)` line.
# Run the plugin by pressing `Ok`.

If all goes well, an image will be displayed representing the result of the model execution.

See the [https://github.com/CSBDeep/CSBDeep_website/wiki/Your-Model-in-Fiji CSBDeep Wiki Page] for more details.

== GPU support ==

Please read [https://imagej.net/TensorFlow-GPU this page] for GPU support.

== License ==

This project is licensed under the BSD 2-clause "Simplified" License -- see the [https://github.com/CSBDeep/CSBDeep_fiji/blob/master/LICENSE.txt LICENSE.txt] file for details.
