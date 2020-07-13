---
title: Feature Demo
breadcrumb: Feature Demo
layout: page
author: Edward Evans
categories: plugins, demo, help
description: This page is a feature demo.
---

# DEMO LINKS

| Action | Link to demo page|
| : --- : | :---: |
| Generate info/details box | [details-box]({{"/pages/demo-details-box" | relative_url}}) | 
| Insert figure | [figure]({{"/pages/demo-figure" | relative_url}})
| Link to github files | [github]({{"/pages/demo-github" | relative_url}}) |
| Insert images | [image]({{"/pages/demo-image" | relative_url}}) |
| Insert a notice | [info-box]({{"/pages/demo-info-box" | relative_url}})
| Insert logos | [logo]({{"/pages/demo-logo" | relative_url}}) |
| Insert menu breadcrumb | [menu-bc]({{"/pages/demo-menu-breadcrumb" | relative_url}}) |
| Insert math | [math]({{"/pages/demo-math" | relative_url}}) |
| Insert person details | [person]({{"/pages/demo-person" | relative_url}})
| Insert a sidebox | [sidebox]({{"/pages/demo-sidebox" | relative_url}})
| Insert a tech box | [tech-box]({{"/pages/demo-tech-box" | relative_url}})
| Insert a warning | [warning-box]({{"/pages/demo-warning-box" | relative_url}})

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