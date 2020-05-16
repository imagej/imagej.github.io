---
title: Feature Demo
breadcrumb: Feature Demo
layout: page
author: Edward Evans
category: plugins:Demo
use_math: true
description: This page is a feature demo.
---

{% include info-box icon_path="/images/icons/40px-Information-sign.png" content="Hey this is the info box! If you want to learn more about how to create an info box, view the source of this page!" %}

<div class="sidebar" markdown="1">

Sidebar
<hr>
[Introduction](#Introduction)
<hr>
[Left image](#Left image)
[Right image](#Right image)
[Center image](#Center image)
[Fit image](#Fit image)
[Figure left](#Figure left)
[Figure right](#Figure right)
[Figure center](#Figure center)
[Figure row](#Figure row)
[Markdown table](#Markdown table)
[YouTube video](#YouTube video)
[Imbedded images in table](#Imbedded images in table)
[Math equations](#Math equations)
[Sidebox](#Sidebox)
[Syntax highlighting](#Syntax highlighting)

</div>

## <a name="Introduction"></a> **Introduction**

While in Clojure one is able to declare types if desired, it's not required; the low computational requirements of the plugin do not invite to make it verbose unnecessarily. But java demands type declarations just so that the plugin can be compiled and thus a binary .class file generated.

## <a name="Left image"></a> **Left image**

{% include image-left name="place holder image" image_path="/images/placeholder.png" %}

While both the java and clojure versions encapsulate the variables in a local namespace -in Clojure, by using let statements to declare local variables-, the jython version does not, so they are all global when defined outside the class definition. One can achieve, though, variable encapsulation by declaring the entire script inside a class or function definition -but its not required as in java, neither as natural and straightforward as in Clojure.

## <a name="Right image"></a> **Right image**

{% include image-right name="place holder image" image_path="/images/placeholder.png" %}

While both the java and clojure versions encapsulate the variables in a local namespace -in Clojure, by using let statements to declare local variables-, the jython version does not, so they are all global when defined outside the class definition. One can achieve, though, variable encapsulation by declaring the entire script inside a class or function definition -but its not required as in java, neither as natural and straightforward as in Clojure.

## <a name="Center image"></a> **Center image**

{% include image-center name="place holder image" image_path="/images/placeholder.png" %}

While both the java and clojure versions encapsulate the variables in a local namespace -in Clojure, by using let statements to declare local variables-, the jython version does not, so they are all global when defined outside the class definition. One can achieve, though, variable encapsulation by declaring the entire script inside a class or function definition -but its not required as in java, neither as natural and straightforward as in Clojure.

## <a name="Fit image"></a> **Fit image**

{% include image-fit name="place holder image" image_path="/images/placeholder.png" %}

While both the java and clojure versions encapsulate the variables in a local namespace -in Clojure, by using let statements to declare local variables-, the jython version does not, so they are all global when defined outside the class definition. One can achieve, though, variable encapsulation by declaring the entire script inside a class or function definition -but its not required as in java, neither as natural and straightforward as in Clojure.

## <a name="Figure left"></a> **Figure left**

{% include figure-left name="place holder image" image_path="/images/placeholder.png" content="Figure legend - left" %}

While both the java and clojure versions encapsulate the variables in a local namespace -in Clojure, by using let statements to declare local variables-, the jython version does not, so they are all global when defined outside the class definition. One can achieve, though, variable encapsulation by declaring the entire script inside a class or function definition -but its not required as in java, neither as natural and straightforward as in Clojure.

While both the java and clojure versions encapsulate the variables in a local namespace -in Clojure, by using let statements to declare local variables-, the jython version does not, so they are all global when defined outside the class definition. One can achieve, though, variable encapsulation by declaring the entire script inside a class or function definition -but its not required as in java, neither as natural and straightforward as in Clojure.

## <a name="Figure right"></a> **Figure right**

{% include figure-right name="place holder image" image_path="/images/placeholder.png" content="Figure legend - right" %}

While both the java and clojure versions encapsulate the variables in a local namespace -in Clojure, by using let statements to declare local variables-, the jython version does not, so they are all global when defined outside the class definition. One can achieve, though, variable encapsulation by declaring the entire script inside a class or function definition -but its not required as in java, neither as natural and straightforward as in Clojure.

While both the java and clojure versions encapsulate the variables in a local namespace -in Clojure, by using let statements to declare local variables-, the jython version does not, so they are all global when defined outside the class definition. One can achieve, though, variable encapsulation by declaring the entire script inside a class or function definition -but its not required as in java, neither as natural and straightforward as in Clojure.

## <a name="Figure center"></a> **Figure center**

{% include figure-center name="place holder image" image_path="/images/placeholder.png" content="Figure legend - center" %}

While both the java and clojure versions encapsulate the variables in a local namespace -in Clojure, by using let statements to declare local variables-, the jython version does not, so they are all global when defined outside the class definition. One can achieve, though, variable encapsulation by declaring the entire script inside a class or function definition -but its not required as in java, neither as natural and straightforward as in Clojure.

While both the java and clojure versions encapsulate the variables in a local namespace -in Clojure, by using let statements to declare local variables-, the jython version does not, so they are all global when defined outside the class definition. One can achieve, though, variable encapsulation by declaring the entire script inside a class or function definition -but its not required as in java, neither as natural and straightforward as in Clojure.


## <a name="Figure row"></a> **Figure row**

While both the java and clojure versions encapsulate the variables in a local namespace -in Clojure, by using let statements to declare local variables-, the jython version does not, so they are all global when defined outside the class definition. One can achieve, though, variable encapsulation by declaring the entire script inside a class or function definition -but its not required as in java, neither as natural and straightforward as in Clojure.

<div class="figure row" markdown="1">

| ![placeholder image 1]({{site.baseurl}}/images/placeholder.png){: .image.fit} Row legend 1 | ![placeholder image 2]({{site.baseurl}}/images/placeholder.png){: .image.fit} Row legend 2 | ![placeholder image 3]({{site.baseurl}}/images/placeholder.png){: .image.fit} Row legend 3 | 

</div>

## <a name="Markdown table"></a> **Markdown table**

| Item 1 | Item 2 | Item 3 |
| :---: | :---: | :---: |
| A | B | C |
| 1 | 2 | 3 |

## <a name="YouTube video"></a> **YouTube video**

{% include youtube url="https://www.youtube.com/embed/4NOM-kLfDR8" %}

## <a name="Imbedded images in table"></a> **Imbedded images in table**

A table with images, use the .image.table to make it align with text:

| :---: | :---: |
|![Plugins]({{"/images/icons/plugins_icon.png" | relative_url}}){: .image.table} | A powerful mechanism for extending ImageJ in all kinds of useful ways. 
| ![Extend]({{"/images/icons/extend_icon.png" | relative_url}}){: .image.table} | Automated, reproducible workflows via scripts and macros, including headless on a remote server or cluster. |

## <a name="Math equations"></a> **Math equations**

When $$a \ne 0$$ , there are two solutions to $$(ax^2 + bx + c = 0)$$ and they are

$$x = {-b \pm \sqrt{b^2-4ac} \over 2a}.$$

Wow such pretty math!

## <a name="Sidebox"></a> **Sidebox**

{% include sidebox-right content="Hey this is the sidebox-right style!" %}

While both the java and clojure versions encapsulate the variables in a local namespace -in Clojure, by using let statements to declare local variables-, the jython version does not, so they are all global when defined outside the class definition. One can achieve, though, variable encapsulation by declaring the entire script inside a class or function definition -but its not required as in java, neither as natural and straightforward as in Clojure.

{% include sidebox-left content="Oh wow!! This is the sidebox-left style! Fantastic!" %}

While both the java and clojure versions encapsulate the variables in a local namespace -in Clojure, by using let statements to declare local variables-, the jython version does not, so they are all global when defined outside the class definition. One can achieve, though, variable encapsulation by declaring the entire script inside a class or function definition -but its not required as in java, neither as natural and straightforward as in Clojure.

{% include info-box icon_path="/images/icons/40px-Important-sign.png" content="Stop! This is an important message! Did you check out the plugins categories page? What do you think? Okay please continue reading.
" %}

## <a name="Syntax highlighting"></a> **Syntax highlighting**

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

## Menu breadcrumbs:

You can access the plugin by opening Fiji and navigating the menus: {% include bc color="black" content="Menu1|Menu2|Menu3|Menu4|Plugin" %} 