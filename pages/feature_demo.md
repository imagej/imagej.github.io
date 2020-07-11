---
title: Feature Demo
breadcrumb: Feature Demo
layout: page
author: Edward Evans
categories: plugins, demo, help
use_math: true
description: This page is a feature demo.
---

# DEMO LINKS

| Action | Link to demo page|
| : --- : | :---: |
| Generate info/details box | [details-box]({{"/pages/demo-details-box" | relative_url}}) | 
| Insert figure | [figure]({{"/pages/demo-figure" | relative_url}})
| Link to github files | [github]({{"/pages/demo-github" | relative_url}}) |
| Insert images | [image]({{"/pages/demo-image" | relative_url}}) |
| Insert info-box | [info-box]({{"/pages/demo-info-box" | relative_url}})
| Insert logos | [logo]({{"/pages/demo-logo" | relative_url}}) |
| Insert person details | [person]({{"/pages/demo-person" | relative_url}})


<center>
<h1>Information/Warning/Tech boxes</h1>
</center>

**Information and warning boxes allow you to notify the reader of something important details to keep in mind. To use the information and warning boxes, include them in your markdown document, and utilize the `content` variable to contain your text. For example:**

{% raw %}
```
{% include info-box content="Hey this is the info box! 

- item 1
- item 2

If you want to learn more about how to create an info box, view the source of this page! Such wow!" %}
```
{% endraw %}

**Creates:**

{% include info-box content="Hey this is the info box! 

- item 1
- item 2

If you want to learn more about how to create an info box, view the source of this page! Such wow!" %}

**Note that you can still use markdown inside the `""` where your text is placed. In this example I'm using markdown to create a list inside the information box.**

**A warning box can be created like this:**

{% raw %}
```
{% include warning-box content="Stop! This is an important message! Did you check out the plugins categories page? What do you think? Make sure you wash your hands! Okay please continue reading.
" %}
```
{% endraw %}

{% include warning-box content="Stop! This is an important message! Did you check out the plugins categories page? What do you think? Make sure you wash your hands! Okay please continue reading.
" %}

**You can also use a tech-box to highlight a technology:**

{% raw %}
```
{% include tech-box content="Wait stop! There's some tech going on here!

- Tech item 1
- Tech item 2
- Tech item 3

" %}
```
{% endraw %}

{% include tech-box content="Wait stop! There's some tech going on here!

- Tech item 1
- Tech item 2
- Tech item 3

" %}

<center>
<h1>Left/Right sidebox</h1>
</center>

**Sideboxes on the left or right of a body of text can be added easily by including `sidebox-right` or `sidebox-left`. Here's a box on the right:**

{% include sidebox-right content="Hey this is the sidebox-right style!" %}

Lorem ipsum dolor sit amet, qui possit aeterno denique ea, te usu affert consequuntur, vix in utinam mentitum reformidans. Sed ea vidisse eripuit aliquid, no usu ullum dictas, an epicurei maluisset vix. Ne posse virtute impedit duo. Eos homero euripidis honestatis no.

Sed ex magna honestatis, ea illud honestatis pri. Vix libris nemore suscipiantur cu. Offendit posidonium has ad, nec ad vocent maiorum consetetur. Vis ei iisque phaedrum atomorum, vis ea esse cetero. In est qualisque adipiscing reformidans, ut sint habeo libris quo.

Mel tempor consetetur posidonium in, mei admodum mentitum ullamcorper cu. Ius no prima dolorum. Mea electram imperdiet adversarium in, vide reque ei sed. Ut duo putant dictas theophrastus. Ne vim etiam theophrastus, cu vel minimum detracto, modus possit phaedrum ius an. Noster nominavi persequeris has ex, brute mnesarchum intellegebat eu eum.

**And here's a box on the left:**

{% include sidebox-left content="Oh wow!! This is the sidebox-left style! Fantastic!" %}

Albucius eligendi est ei. Graeco alterum prodesset pro ad. Eum movet populo mediocrem ad, ut vix scaevola legendos tractatos. Omnes adolescens voluptatibus qui eu. Ut sea quando soluta qualisque, qui in simul reprehendunt, pro ei dico abhorreant. Ius amet munere erroribus te.

Eum ei melius salutandi urbanitas, id duo modo discere dolorum. Tota nonumes ei vis, mea ne reque efficiantur, forensibus reprimique id duo. Ocurreret voluptaria in est, an sed nemore similique, affert aeterno recteque an nam. Porro integre detracto et sea, eum ne nulla ancillae intellegat. Ex dolorum referrentur cum, nec ei officiis convenire, ad vis cibo timeam.

<center>
<h1>Math eqations</h1>
</center>

Note, Because MathJax 3 broke support for MathJax 2 style equations parsed by Kramdown, equations are only recognized by the `$$` tag.

When $$a \ne 0$$ , there are two solutions to $$(ax^2 + bx + c = 0)$$ and they are

$$x = {-b \pm \sqrt{b^2-4ac} \over 2a}$$

Wow such pretty math!


{% include sidebar title="Demo" content="Introduction, |, Left image, Right image, Center image, Fit image, Figure left, Figure right,Figure center, Figure row, Markdown table, YouTube video, Embedded images in table, Math equations, Sidebox, Syntax highlighting, Menu breadcrumbs" %}


{% include anchor content="Introduction" %}

While in Clojure one is able to declare types if desired, it's not required; the low computational requirements of the plugin do not invite to make it verbose unnecessarily. But java demands type declarations just so that the plugin can be compiled and thus a binary .class file generated.

While in Clojure one is able to declare types if desired, it's not required; the low computational requirements of the plugin do not invite to make it verbose unnecessarily. But java demands type declarations just so that the plugin can be compiled and thus a binary .class file generated.

{% include anchor content="Figure center" %}

{% include figure-center name="place holder image" image_path="/images/placeholder.png" content="**Figure 3** : This is a center figure." %}

While both the java and clojure versions encapsulate the variables in a local namespace -in Clojure, by using let statements to declare local variables-, the jython version does not, so they are all global when defined outside the class definition. One can achieve, though, variable encapsulation by declaring the entire script inside a class or function definition -but its not required as in java, neither as natural and straightforward as in Clojure.

While both the java and clojure versions encapsulate the variables in a local namespace -in Clojure, by using let statements to declare local variables-, the jython version does not, so they are all global when defined outside the class definition. One can achieve, though, variable encapsulation by declaring the entire script inside a class or function definition -but its not required as in java, neither as natural and straightforward as in Clojure.


{% include anchor content="Figure row" %}

While both the java and clojure versions encapsulate the variables in a local namespace -in Clojure, by using let statements to declare local variables-, the jython version does not, so they are all global when defined outside the class definition. One can achieve, though, variable encapsulation by declaring the entire script inside a class or function definition -but its not required as in java, neither as natural and straightforward as in Clojure.

<div class="figure row" markdown="1">

| ![placeholder image 1]({{site.baseurl}}/images/placeholder.png){: .image.fit} Row legend 1 | ![placeholder image 2]({{site.baseurl}}/images/placeholder.png){: .image.fit} Row legend 2 | ![placeholder image 3]({{site.baseurl}}/images/placeholder.png){: .image.fit} Row legend 3 | 

</div>

{% include anchor content="Markdown table" %}

| Item 1 | Item 2 | Item 3 |
| :---: | :---: | :---: |
| A | B | C |
| 1 | 2 | 3 |

{% include anchor content="YouTube video" %}

{% include youtube url="https://www.youtube.com/embed/4NOM-kLfDR8" %}

{% include anchor content="Embedded images in table" %}

A table with images, use the .image.table to make it align with text:

| :---: | :---: |
|![Plugins]({{"/images/icons/plugins_icon.png" | relative_url}}){: .image.table} | A powerful mechanism for extending ImageJ in all kinds of useful ways. 
| ![Extend]({{"/images/icons/extend_icon.png" | relative_url}}){: .image.table} | Automated, reproducible workflows via scripts and macros, including headless on a remote server or cluster. |

{% include anchor content="Syntax highlighting" %}

Java example:

```java
Image3DUniverse univ = new Image3DUniverse();
univ.show();
univ.addMesh(yourImagePlus, null, "somename", 50, new boolean[] {true, true, true}, 2);
...
```

Python example:

```python
def update_progress(progress):
    barLength = 10 # Modify this to change the length of the progress bar
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "Done...\r\n"
    block = int(round(barLength*progress))
    text = "\rPercent complete: [{0}] {1}% {2}".format( "#"*block + "-"*(barLength-block), progress*100, status)
    sys.stdout.write(text)
    sys.stdout.flush()
```

{% include anchor content="Menu breadcrumbs" %}

_Black menu breadcrumb_:
{% include bc color="black" content="Menu1|Menu2|Menu3|Menu4|**Plugin**" %} 

_White menu breadcrumb_:
{% include bc color="white" content="Menu1|Menu2|Menu3|Menu4|**Plugin**" %} 

_None menu breadcrumb_:
{% include bc color="none" content="Menu1|Menu2|Menu3|Menu4|**Plugin**" %} 