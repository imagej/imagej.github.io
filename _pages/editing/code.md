---
title: Source Code
section: Contribute:Editing the Wiki
nav-links: true
---

This page describes nice ways of embedding source code in a page.

# Inline code snippets

If you just want to write a short snippet of code as part of a sentence,
surround the code in backtick symbols (<code>`</code>).

{% capture inline-code-snippet %}
Type `print('Hello world!')` and save as `hello.py`.
{% endcapture %}
{% include editing/example code=inline-code-snippet %}

## Code fences

A "code fence" is three backtick symbols (<code>```</code>) preceding your
code, and another three concluding it. Optionally, you can write the name of
the language in small case next to the leading fence to declare syntax
highlighting is desired with the stated language.

**NB:** code fence syntax highlighting is currently not working locally due to
differences in local build configuration. However, highlighting *will* display as
appropriate on the public wiki.

### Java example

{% capture code-fence-java %}
```java
Image3DUniverse univ = new Image3DUniverse();
univ.show();
univ.addMesh(yourImagePlus, null, "somename", 50,
  new boolean[] {true, true, true}, 2);
```
{% endcapture %}
{% include editing/example code=code-fence-java %}

### Python example

{% capture code-fence-python %}
```python
def update_progress(progress):
    barLength = 10 # length of progress bar
    block = int(round(barLength*progress))
    text = f'\rPercent complete: ' +
      f'[{"#"*block + "-"*(barLength-block)}] ' +
      f'{progress*100}%'
    sys.stdout.write(text)
    sys.stdout.flush()
```
{% endcapture %}
{% include editing/example code=code-fence-python %}

## Highlight directive

Alternately, there is a `highlight` Liquid directive you can try.
It looks like this:

{% capture liquid-highlight-code %}
{% raw %}{% highlight java %}
log.info("You're a wizard, Harry!");
log.error("I'm a what?");
{% endhighlight %}{% endraw %}
{% endcapture %}
{% capture liquid-highlight-result %}
{% highlight java %}
log.info("You're a wizard, Harry!");
log.error("I'm a what?");
{% endhighlight %}
{% endcapture %}
{% include editing/example code=liquid-highlight-code result=liquid-highlight-result %}

The `highlight` directive and code fences are separate features, but
functionally very similar. If code fences are not working as you like,
give the `highlight` directive a try to see if it does any better.

## Line numbers

Right now, inline code snippets cannot have line numbers; see
{% include github org='imagej' repo='imagej.github.io' issue=128 label='issue 128' %}
for technical details. For now, if you want to have line numbers, use the
[Embedding external code](#embedding-external-code) approach below.

{% include notice icon='warning' content="
You might be familiar with the `linenos` argument to the `highlight` directive.
Please ___do not use this___. As of this writing (Q3 2021), it produces badly
formed HTML output, which can break wiki pages.
" %}

## Making code snippets executable and editable

By enabling the `imjoy` extension, you can make your code snippets executable and editable.
It makes wiki pages more interactive, thus suited for building demos and tutorials.
Currently, it support ImageJ macro and ImJoy plugin scripts.

To enable it, you need to:
 1. add `imjoy` to `extensions` in the [front matter](/editing#add-the-pages-front-matter) of your page;
 2. add a HTML comment `<!-- ImJoyPlugin: { ... } -->` before your code block. Inside the `{}` you can pass settings for setting up the ImJoy plugin.

Here is an example for making an ImageJ macro code snippet executable.

First, enable the `imjoy` extension in the beginning of your page:
```yaml
---
title: My Awesome Page
extensions: ["imjoy"]
---
```

Let's say you have the following macro:
```javascript
print("hello world");
```

To make it executable, you just need to add an HTML comment:
~~~markdown
<!-- ImJoyPlugin: { "type": "macro"} -->
```javascript
print("hello world");
```
~~~

For more detailed instructions about using ImageJ macro with ImageJ.JS, please refer to [ImageJ.JS](/software/imagej-js). 

Similarily, you can execute an ImJoy plugin in code fences which can be used for integrating image viewers such as 
[Kaibu](https://kaibu.org), [vizarr](https://github.com/hms-dbmi/vizarr) and [ITK/VTK viewer](https://kitware.github.io/itk-vtk-viewer/), or running ImageJ2 and Fiji through [pyimagej](https://github.com/imagej/pyimagej) on a remote Jupyter server (e.g. on [Binder](https://mybinder.org)). For more details, please refer to [ImJoy](/software/imjoy).

# Embedding external code

If you have code in a repository such as GitHub, GitLab, or BitBucket,
you can embed code blocks dynamically into the page using the
`code` include. This approach has the advantage of avoiding
copy-paste skew as the code evolves over time.

Parameters supported by the `code` include are:

| Parameter    | Description                                | Supported values                | Default  |
|:-------------|:-------------------------------------------|:--------------------------------|----------|
| `service`    | Which repository hosting service           | `github`, `gitlab`, `bitbucket` | `github` |
| `org`        | Name of the organization                   | any string                      | none     |
| `repo`       | Name of the repository                     | any string                      | none     |
| `branch`     | Which branch, tag, or commit               | any string                      | none     |
| `path`       | Path to the resource in source control     | any string                      | none     |
| `line-start` | First line to embed                        | `>= 1`                          | `1`      |
| `line-end`   | Last line to embed                         | `>= 1`                          | `99999`  |
| `label`      | Hyperlinked label to place before the code | any string                      | no label |

## Embedding from GitHub

{% capture github-embed-code %}
{% raw %}
{% include code
     org="duckythescientist"
     repo="obfuscatedLife"
     branch="original"
     path="life.c"
     label="Conway's Obfuscated Game of Life" %}
{% endraw %}
{% endcapture %}
{% capture github-embed-result %}
{% include code
     org="duckythescientist"
     repo="obfuscatedLife"
     branch="original"
     path="life.c"
     label="Conway's Obfuscated Game of Life" %}
{% endcapture %}
{% include editing/example code=github-embed-code result=github-embed-result %}

Additional parameters supported by embeds from GitHub specifically:

| Parameter           | Description                                     | Supported values  | Default  |
|:--------------------|:------------------------------------------------|:------------------|----------|
| `style`             | Syntax highlighting color scheme                | various[^1]       | `github` |
| `show-border`       | Whether to draw a border around the frame       | `true` or `false` | `true`   |
| `show-line-numbers` | Whether to number the lines                     | `true` or `false` | `true`   |
| `show-file-meta`    | Whether to include the footer with links        | `true` or `false` | `true`   |
| `show-copy`         | Whether to include the Copy button on mouseover | `true` or `false` | `true`   |

## Embedding from GitLab

We want to support embedding from GitLab, but it's not implemented yet:

{% capture gitlab-embed-code %}
{% raw %}
{% include code
     service="gitlab"
     org="tjian-darzacq-lab"
     repo="Spot-On-TrackMate"
     branch="master"
     path="src/main/java/plugin/trackmate/action/ExportTracksToSpotOn.java"
     line-start=91 line-end=112
     label="Spot-On export TrackMate tracks to XML" %}
{% endraw %}
{% endcapture %}
{% capture gitlab-embed-result %}
{% include code
     service="gitlab"
     org="tjian-darzacq-lab"
     repo="Spot-On-TrackMate"
     branch="master"
     path="src/main/java/plugin/trackmate/action/ExportTracksToSpotOn.java"
     line-start=91 line-end=112
     label="Spot-On export TrackMate tracks to XML" %}
{% endcapture %}
{% include editing/example code=gitlab-embed-code result=gitlab-embed-result %}

## Embedding from BitBucket

We want to support embedding from GitLab, but it's not implemented yet:

{% capture bitbucket-embed-code %}
{% raw %}
{% include code
     service="bitbucket"
     org="fernandoamat"
     repo="keller-lab-block-filetype"
     branch="d4755438000475d60e51ee2b793a7fd92c1be7fe"
     path="src/main/java/org/janelia/simview/klb/KLB.java"
     line-start=279 line-end=297
     label="Reading KLB data as ImgLib2 image" %}
{% endraw %}
{% endcapture %}
{% capture bitbucket-embed-result %}
{% include code
     service="bitbucket"
     org="fernandoamat"
     repo="keller-lab-block-filetype"
     branch="d4755438000475d60e51ee2b793a7fd92c1be7fe"
     path="src/main/java/org/janelia/simview/klb/KLB.java"
     line-start=279 line-end=297
     label="Reading KLB data as ImgLib2 image" %}
{% endcapture %}
{% include editing/example code=bitbucket-embed-code result=bitbucket-embed-result %}

# Footnotes

[^1]: Valid style values for GitHub embeds are:

    <ul style="column-width: 11em; list-style: none;">
    <li>a11y-dark</li>
    <li>a11y-light</li>
    <li>agate</li>
    <li>an-old-hope</li>
    <li>androidstudio</li>
    <li>arduino-light</li>
    <li>arta</li>
    <li>ascetic</li>
    <li>atelier-cave-dark</li>
    <li>atelier-cave-light</li>
    <li>atelier-dune-dark</li>
    <li>atelier-dune-light</li>
    <li>atelier-estuary-dark</li>
    <li>atelier-estuary-light</li>
    <li>atelier-forest-dark</li>
    <li>atelier-forest-light</li>
    <li>atelier-heath-dark</li>
    <li>atelier-heath-light</li>
    <li>atelier-lakeside-dark</li>
    <li>atelier-lakeside-light</li>
    <li>atelier-plateau-dark</li>
    <li>atelier-plateau-light</li>
    <li>atelier-savanna-dark</li>
    <li>atelier-savanna-light</li>
    <li>atelier-seaside-dark</li>
    <li>atelier-seaside-light</li>
    <li>atelier-sulphurpool-dark</li>
    <li>atelier-sulphurpool-light</li>
    <li>atom-one-dark</li>
    <li>atom-one-dark-reasonable</li>
    <li>atom-one-light</li>
    <li>codepen-embed</li>
    <li>color-brewer</li>
    <li>darcula</li>
    <li>dark</li>
    <li>default</li>
    <li>docco</li>
    <li>dracula</li>
    <li>far</li>
    <li>foundation</li>
    <li>github</li>
    <li>github-gist</li>
    <li>gml</li>
    <li>googlecode</li>
    <li>gradient-dark</li>
    <li>grayscale</li>
    <li>gruvbox-dark</li>
    <li>gruvbox-light</li>
    <li>hopscotch</li>
    <li>hybrid</li>
    <li>idea</li>
    <li>ir-black</li>
    <li>isbl-editor-dark</li>
    <li>isbl-editor-light</li>
    <li>kimbie.dark</li>
    <li>kimbie.light</li>
    <li>lightfair</li>
    <li>magula</li>
    <li>mono-blue</li>
    <li>monokai</li>
    <li>monokai-sublime</li>
    <li>night-owl</li>
    <li>nord</li>
    <li>obsidian</li>
    <li>ocean</li>
    <li>paraiso-dark</li>
    <li>paraiso-light</li>
    <li>purebasic</li>
    <li>qtcreator_dark</li>
    <li>qtcreator_light</li>
    <li>railscasts</li>
    <li>rainbow</li>
    <li>routeros</li>
    <li>shades-of-purple</li>
    <li>solarized-dark</li>
    <li>solarized-light</li>
    <li>sunburst</li>
    <li>tomorrow</li>
    <li>tomorrow-night</li>
    <li>tomorrow-night-blue</li>
    <li>tomorrow-night-bright</li>
    <li>tomorrow-night-eighties</li>
    <li>vs</li>
    <li>vs2015</li>
    <li>xcode</li>
    <li>xt256</li>
    <li>zenburn</li>
    </ul>
