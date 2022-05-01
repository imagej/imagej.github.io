---
title: Quizzes
section: Contribute:Editing the Wiki
nav-links: true
---

This page demonstrates how to use the `quiz` include tag.

## Usage

A `quiz` allows you to pose a question to the reader with an expandable answer that is hidden by default. This can be useful when writing tutorials with challenge questions, for example.

{% highlight liquid %}{% raw %}{% include quiz q="What is the air-speed velocity of an unladen swallow?" a="No cheating!"%}{% endraw %}{% endhighlight %}
{% include quiz q="What is the air-speed velocity of an unladen swallow?" a="24 miles per hour"%}

