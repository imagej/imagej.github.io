---
title: People
section: Help:Editing the Wiki
nav-links: true
---

This page demonstrates how to use the `person` include tag.

## Individuals

Specify a person using their ID from the
{% include github label="`/users` folder" org="imagej" repo="imagej.github.io" path="_pages/users" %},
or a plain/unlinked name.

## Examples

{% capture ex1-code %}
{% raw %}{% include person id='rasband' %}{% endraw %}
{% endcapture %}
{% capture ex1-result %}
{% include person id='rasband' %}
{% endcapture %}
{% include code-example code=ex1-code result=ex1-result %}

{% capture ex2-code %}
{% raw %}{% include person id='ctrueden' name='Chuckles' %}{% endraw %}
{% endcapture %}
{% capture ex2-result %}
{% include person id='ctrueden' name='Chuckles' %}
{% endcapture %}
{% include code-example code=ex2-code result=ex2-result %}

{% capture ex3-code %}
{% raw %}{% include person name='Jane Doe' %}{% endraw %}
{% endcapture %}
{% capture ex3-result %}
{% include person name='Jane Doe' %}
{% endcapture %}
{% include code-example code=ex3-code result=ex3-result %}

## Lists of people

{% capture list-ex1-code %}
{% raw %}{% include person-list ids="dietzc | marktsuchida | Julius Caesar" %}{% endraw %}
{% endcapture %}
{% capture list-ex1-result %}
{% include person-list ids="dietzc | marktsuchida | Julius Caesar" %}
{% endcapture %}
{% include code-example code=list-ex1-code result=list-ex1-result %}
