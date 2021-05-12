---
title: Demo Source Code
---

This page describes nice ways of embedding source code in a page.

## Inline code snippets

If you just want to write a short snippet of code as part of a sentence,
surround the code in backtick symbols (<code>`</code>).

{% capture inline-code-snippet %}
Type `print('Hello world!')` and save as `hello.py`.
{% endcapture %}
{% include example code=inline-code-snippet %}

## Code fences

A "code fence" is three backtick symbols (<code>```</code>) preceding your
code, and another three concluding it. Optionally, you can write the name of
the language in small case next to the leading fence to declare syntax
highlighting is desired with the stated language.

### Java example

{% capture code-fence-java %}
```java
Image3DUniverse univ = new Image3DUniverse();
univ.show();
univ.addMesh(yourImagePlus, null, "somename", 50,
  new boolean[] {true, true, true}, 2);
```
{% endcapture %}
{% include example code=code-fence-java %}

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
{% include example code=code-fence-python %}

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
{% include example code=liquid-highlight-code result=liquid-highlight-result %}

The `highlight` directive and code fences are separate features, but
functionally very similar. If code fences are not working as you like,
give the `highlight` directive a try to see if it does any better.

## Embedding code from GitHub

If you have a block of code in a GitHub repository, you can embed it
dynamically into the page using the `github-embed` include. This approach has
the advantage of avoiding copy-paste skew as the code evolves over time.

{% capture github-embed-code %}
{% raw %}
{% include github-embed
     org="duckythescientist"
     repo="obfuscatedLife"
     branch="original"
     path="life.c"
     label="Conway's Obfuscated Game of Life" %}
{% endraw %}
{% endcapture %}
{% capture github-embed-result %}
{% include github-embed
     org="duckythescientist"
     repo="obfuscatedLife"
     branch="original"
     path="life.c"
     label="Conway's Obfuscated Game of Life" %}
{% endcapture %}
{% include example code=github-embed-code result=github-embed-result %}

Other parameters supported by the `github-embed` include are:

| Parameter           | Description                                     | Values            | Default  |
|:--------------------|:------------------------------------------------|:------------------|----------|
| `line-start`        | First line to embed                             | `>= 1`            | `1`      |
| `line-end`          | Last line to embed                              | `>= 1`            | `99999`  |
| `label`             | Hyperlinked label to place before the code      | any string        | no label |
| `style`             | Syntax highlighting color scheme                | various*          | `github` |
| `show-border`       | Whether to draw a border around the frame       | `true` or `false` | `true`   |
| `show-line-numbers` | Whether to number the lines                     | `true` or `false` | `true`   |
| `show-file-meta`    | Whether to include the footer with links        | `true` or `false` | `true`   |
| `show-copy`         | Whether to include the Copy button on mouseover | `true` or `false` | `true`   |

\* Valid style values are:
<ul style="display: flex; flex-wrap: wrap; list-style: none;">
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
