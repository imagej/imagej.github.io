---
title: ImJoy
section: Explore:Software
doi: 10.1038/s41592-019-0627-0
imjoy: true
---

# ImJoy: Supercharging interactivity and scalability of data science!

ImJoy is a plugin powered hybrid computing platform for deploying deep learning applications such as advanced image analysis tools.

The ImJoy project was started at Institut Pasteur in 2018. It is currently actively improved and maintained by the ImJoy Team led by Wei Ouyang (SciLifeLab & KTH in Stockholm). The team consists of members from different institutions who meet weekly and continuously improving the software and expanding the plugin ecosystem.

# Getting started
ImJoy is a progressive web application which you can run directly in your browser without installation. Go to [https://imjoy.io](https://imjoy.io) and click "Start ImJoy".

ImJoy can also be embedded directly into documentations, for example, if you click "Run", you will see the same ImJoy interface:
<!-- ImJoyPlugin: { "type": "web-worker","editor_height": "200px", "hide_code_block": true } -->
```js
api.createWindow({src: 'https://imjoy.io/#/app', passive: true})
```

Since ImJoy itself doesn't provide any functional plugins, for any actual application, you will need to work with the corresponding plugins. For example, if you click "Run" below, you will see a demo plugin which does image classification with lightweight deep learning model running in the browser:
<!-- ImJoyPlugin: { "type": "web-worker","editor_height": "200px", "hide_code_block": true } -->
```js
api.createWindow({src: 'https://github.com/imjoy-team/imjoy-plugins/blob/master/repository/HPA-Classification.imjoy.html'})
```

For more plugin examples, please check out the [gallery](https://imjoy.io/docs/#/gallery).

# ImJoy Plugin development

ImJoy plugins can be provide as a single text file ( `*.imjoy.html`) or a web URL hosted somehwere else. The most common way to build ImJoy is to provide a plugin file.

Here is an basic plugin file for ImJoy:
<!-- ImJoyPlugin: { "type": "web-worker","editor_height": "400px", "hide_code_block": false } -->
```html
<config lang="json">
{
  "name": "Pokémon Chooser",
  "type": "web-worker",
  "tags": [],
  "ui": "",
  "version": "0.1.0",
  "cover": "",
  "description": "This is a demo plugin for choosing Pokémons",
  "icon": "extension",
  "inputs": null,
  "outputs": null,
  "api_version": "0.1.8",
  "env": "",
  "permissions": [],
  "requirements": [],
  "dependencies": []
}
</config>
<script lang="javascript">
class ImJoyPlugin{
    async setup(){
        await api.log("plugin initialized")
    }
    async choosePokemon(){
        const pokemon = await api.prompt("What is your favorite Pokémon?", "Pikachu")
        await api.showMessage("Your have chose " + pokemon + " as your Pokémon.")
    }
    async run(ctx){
        await this.choosePokemon()
    }
}
api.export(new ImJoyPlugin())
</script>
```

If you are interested in learning how to develop ImJoy plugins, We recommend the tutorial we made for the I2K conference: [https://imjoy.io/docs/#/i2k_tutorial](https://imjoy.io/docs/#/i2k_tutorial). It is an interactive documentation where you can follow step by step.


# Open integrations
As part of our mission, we try to bring existing aand future software tools together by connecting them with the [ImJoy RPC protocol](https://github.com/imjoy-team/imjoy-rpc). This is not only internally for connecting plugins in the same workflow, but it also provide a way to integrate other software tools into the same workflow, or bring the ImJoy plugin system to website, online data repository, web applications and other software tools.

We support two-way integration: 1) connect existing web app or software tools as an ImJoy plugin 2) integrate ImJoy core to other website or software tools. For more implementation details, please refer to the [integration docs](https://github.com/imjoy-team/imjoy-core/blob/master/docs/integration.md).

Here is a list of integration examples:
 * [ImageJ.JS](https://ij.imjoy.io)
 * [Jupyter Notebooks Extension](https://github.com/imjoy-team/imjoy-jupyter-extension)
 * [BioImage Model Zoo](https://bioimage.io)
 * [OpenFlexure](https://openflexure.org/)
 * [OMERO](https://github.com/will-moore/omero-imjoy)
 * [ImJoy Slides](https://slides.imjoy.io)
 * [ImJoy Docs](https://imjoy-team.github.io/imjoy-docs/)

# Running ImJoy plugins in the ImageJ wiki
As another example of open integration, ImJoy can be enabled in the ImageJ wiki. In any markdown page, you can easily turn a markdown code block into executable and editable code block by: 
 1. Set `imjoy: true` to the metadata of your markdown file (a.k.a [Front Matter](https://jekyllrb.com/docs/front-matter/));
 2. Add a comment `<!-- ImJoyPlugin: { ... } -->` before your code block. Inside the `{}` you can pass settings for setting up the ImJoy plugin.

For example, the following code block with Run button is rendered with the above setting:
<!-- ImJoyPlugin: { "type": "web-worker","editor_height": "200px"} -->
```js
api.alert("Hello from ImJoy!")
```

Here is the corresponding markdown code:
````markdown
<!-- ImJoyPlugin: { "type": "web-worker","editor_height": "200px"} -->
```js
api.alert("Hello from ImJoy!")
```
````

You can also embed a plugin window into the page:
<!-- ImJoyPlugin: { "type": "web-worker","editor_height": "200px"} -->
```js
api.createWindow({src: "https://hms-dbmi.github.io/vizarr", name: "Vizarr Demo"}).then((viewer)=>{
    viewer.add_image({source: "https://s3.embassy.ebi.ac.uk/idr/zarr/v0.1/4495402.zarr", name: "Demo Image"})
})
```

Or show a popup dialog:
<!-- ImJoyPlugin: { "type": "web-worker","editor_height": "200px", "hide_code_block": true} -->
```js
api.showDialog({src: "https://hms-dbmi.github.io/vizarr", name: "visualizating HCS zarr images with vizarr"}).then((viewer)=>{
    viewer.add_image({source: "https://minio-dev.openmicroscopy.org/idr/idr0001-graml-sysgro/JL_120731_S6A/pr_45/2551.zarr", name: "Demo Image"})
})
```

You can also run other plugin types, including Python plugins which will be executed via mybinder.org. 

<!-- ImJoyPlugin: { "type": "native-python","editor_height": "200px", "hide_code_block": false} -->
```python
from imjoy import api

class ImJoyPlugin():
    async def setup(self):
        pass

    async def choosePokemon(self):
        pokemon = await api.prompt("What is your favorite Pokémon?", "Pikachu")
        await api.showMessage("Your have chose " + pokemon + " as your Pokémon.")

    async def run(self, ctx):
        await self.choosePokemon()

api.export(ImJoyPlugin())
```

As a more useful demoo, the following code load an [pixel classifier plugin](https://github.com/imjoy-team/imjoy-plugins/blob/master/repository/PixelClassifier.imjoy.html) for interactive image segmentation with scikit-image and scikit-learn. 
(Please note that it can take a few minutes to run for the first time.)
<!-- ImJoyPlugin: { "type": "web-worker","editor_height": "200px", "hide_code_block": true} -->
```js
api.getPlugin({src: 'https://github.com/imjoy-team/imjoy-plugins/blob/master/repository/PixelClassifier.imjoy.html'}).then((plugin)=>{
    plugin.run()
})
```

For more detailed usage, please refer to [ImJoy Docs](https://imjoy-team.github.io/imjoy-docs/#/).

## Running ImageJ.JS in ImageJ wiki
[ImageJ.JS](https://ij.imjoy.io) is a web version of ImageJ, and it can be used as an ImJoy plugin and embeded directly in the ImageJ wiki. For more details, please refer to the [ImageJ.JS page](/software/imagej-js).


# Documentation

Full documentation can be found at [https://imjoy.io/docs/](https://imjoy.io/docs/)


## Publication

* Ouyang, W., Mueller, F., Hjelmare, M. et al. ImJoy: an open-source computational platform for the deep learning era. Nature Methods (2019), https://doi.org/10.1038/s41592-019-0627-0, [free access](https://rdcu.be/bYbGO)

## Code of Conduct

Help us keep the ImJoy community open and inclusive. Please read and follow our [Code of Conduct](https://github.com/imjoy-team/ImJoy/blob/master/docs/CODE_OF_CONDUCT.md).

## License

[MIT License](https://github.com/imjoy-team/ImJoy/blob/master/LICENSE)
