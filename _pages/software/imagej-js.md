---
title: ImageJ.JS
section: Explore:Software
extensions: ["imjoy"]
icon: https://ij.imjoy.io/assets/icons/chrome/chrome-installprocess-128-128.png
name: ImageJ.JS
affiliation: ImJoy Team
website: https://ij.imjoy.io
forum: https://forum.image.sc/tag/imagej-js
twitter: ImJoyTeam
github: imjoy-team
license-url: /licensing/mit
license-label: MIT
team-leads: Wei Ouyang | /people/oeway
---

ImageJ.JS is web version of ImageJ, we compiled ImageJ (version 1) from Java into Javascript with a Java compiler called [CheerpJ](https://www.leaningtech.com/pages/cheerpj.html). In addition to the modification for making it work better within the browser, importantly, we integrated it with the [ImJoy](https://imjoy.io) plugin ecosystem. The project is currently under active development within the [ImJoy Team](https://github.com/imjoy-team) led by Wei Ouyang.


***The latest documentation with full details are avaiable at [ImageJ.JS github repo](https://github.com/imjoy-team/imagej.js), we hightlight a few features below.***


# Getting started

You can run ImageJ with all mainstream browsers with one click, no installation and no Java runtime environment needed. It also works on mobile devices.

To see how it works, click the "Run" button below:
<!-- ImJoyPlugin: { "type": "macro", "hide_code_block": true } -->
```javascript
print("You just started ImageJ.JS!")
```

To use ImageJ.JS outside the wiki, you can click this link: [https://ij.imjoy.io](https://ij.imjoy.io).

Please also checkout our interactive introduction slides by clicking the "Run" button below:
<!-- ImJoyPlugin: { "type": "web-worker", "hide_code_block": true } -->
```javascript
api.createWindow({ src: 'https://slides.imjoy.io/?slides=https://gist.githubusercontent.com/oeway/3968df06b663088eca66f9bd8df94e81/raw/ImageJ.JS-slides-for-OME-Meetings-2021.md', passive: true })
```
(There is also a [3-minute introduction video](https://www.youtube.com/embed/QCuKls8NjqY) associated with the interactive slides)

# Sharing images or macro via URL
To facilitate the sharing of images, macro, and plugins, ImageJ.JS web app supports loading predefined images, macro or plugin by constructing a URL. If you made a ImageJ macro that you want to share, you can store them in your project repo on Github, or simply go to Gist(https://gist.github.com), paste it and get the URL. For example, we stored a demo macro here: [https://gist.github.com/oeway/ab45cc8295efbb0fb5ae1c6f9babd4ac](https://gist.github.com/oeway/ab45cc8295efbb0fb5ae1c6f9babd4ac). Then wen can construct an URL for sharing where user can directly click and run: [https://ij.imjoy.io/?run=https://gist.github.com/oeway/ab45cc8295efbb0fb5ae1c6f9babd4ac](https://ij.imjoy.io/?run=https://gist.github.com/oeway/ab45cc8295efbb0fb5ae1c6f9babd4ac) . This URL can be shared as is, or further shorten by one of the short URL service (e.g. tiny.cc).


# ImJoy Integration

ImageJ.JS supports two-way integration with [ImJoy](/software/imjoy), meaning you can either use it as an ImJoy plugin or load other ImJoy plugins into ImageJ.JS. This a a powerful combination, since it brings useful features from ImageJ including file IO, image processing plugins, macro scripting together with web plugins in ImJoy for building easy to use modern UI and powerful deep learning libraries.

In the standalone mode (simply go to https://ij.imjoy.io), you will have acess to ImJoy features via the ImJoy icon located in the top-left corner of ImageJ. You can load ImJoy plugins into the workspace via a plugin URL, especially for those plugin that calls ImageJ.JS.

For example, the following code shows how to call ImageJ.JS api from an ImJoy plugin:
<!-- ImJoyPlugin: { "type": "web-worker", "editor_height": "400px"} -->
```javascript
async function run(){
    const ij = await api.createWindow({src: "https://ij.imjoy.io"})
    await ij.runMacro(`print("hello world");`)
}

run()
```

The most common use case is to use it with Python, e.g. in a Jupyter notebook or in ImJoy.

Try an online demo: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/imjoy-team/imagej.js/master?filepath=examples%2Fgetting-started.ipynb)

# Interactive documentation

ImageJ.JS is a browser application that can be easily embedded into an website including project site and documentation. 

In fact, we have added the support for running ImageJ in the ImageJ wiki, so you can directly run ImageJ macro and other ImJoy plugins.

For example, you can click and try the `Run` button bellow to see a basic imagej macro for image segmentation (Thanks to Romain Guiet who provided this minimal example):
<!-- ImJoyPlugin: { "type": "macro" } -->
```javascript
run("Blobs (25K)");
setAutoThreshold("Default");
setOption("BlackBackground", true);
run("Convert to Mask");
run("Analyze Particles...", "size=5-Infinity add");
```

# Run ImageJ.JS and ImJoy in ImageJ wiki
You can easily turn a markdown code block into executable and editable code block by: 
 1. Set add `"imjoy"` to `extensions` in the metadata of your markdown file (a.k.a [Front Matter](https://jekyllrb.com/docs/front-matter/));
 2. Add a comment `<!-- ImJoyPlugin: { ... } -->` before your code block. Inside the `{}` you can pass settings for setting up the ImJoy plugin.
 
For example, you may have the following in the begining of your page:
```yaml
---
title: My Awesome Page
extensions: ["imjoy"]
---
```

And now, whthin the page, you can use the following to add a executable and editable code block:
````markdown
<!-- ImJoyPlugin: { "type": "macro"} -->
```javascript
print("hello");
```
````

To make it editable immediately, you can set `startup_mode` to `"edit"`:
````markdown
<!-- ImJoyPlugin: { "type": "macro", "startup_mode": "edit", "editor_height": "100px"} -->
```javascript
print("hello");
```
````

For more detailed usage, please refer to [ImJoy Docs](https://imjoy-team.github.io/imjoy-docs/#/).

# Run ImageJ.JS in interactive slides

Similarily to the ImageJ wiki integration, you can also create interactive slides which has ImageJ.JS directly embeded in. 
This features is useful for teaching purposes, it enables seamless interactive live demo during the presentation and the students can also go back to the same slides and interact with the demos.

You can click [this link](https://slides.imjoy.io/?slides=https://raw.githubusercontent.com/imjoy-team/imjoy-slides/master/slides/run-imagej.js-side-by-side.md) or the "Run" button below:

<!-- ImJoyPlugin: { "type": "web-worker", "hide_code_block": true } -->
```javascript
api.createWindow({ src: 'https://slides.imjoy.io/?slides=https://raw.githubusercontent.com/imjoy-team/imjoy-slides/master/slides/run-imagej.js-side-by-side.md', passive: true })
```

For more detailed usage, please refer to [ImJoy Slides](https://github.com/imjoy-team/imjoy-slides).

# Citation

ImageJ.JS is a part of the ImJoy project, please consider citing the ImJoy paper on Nature Methods ([https://www.nature.com/articles/s41592-019-0627-0](https://www.nature.com/articles/s41592-019-0627-0), [free access](https://rdcu.be/bYbGO) ):

```
Ouyang, W., Mueller, F., Hjelmare, M. et al. ImJoy: an open-source computational platform for the deep learning era. Nat Methods (2019) doi:10.1038/s41592-019-0627-0
```

Alternatively, you can also cite: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4944984.svg)](https://doi.org/10.5281/zenodo.4944984).
