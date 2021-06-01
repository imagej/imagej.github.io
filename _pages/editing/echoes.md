---
title: Echoes
section: Contribute:Editing the Wiki
nav-links: true
---

This page demonstrates how to use the `echo` include tag.

## Usage

This include just echoes its arguments, for debugging/learning purposes. This can be helpful in seeing how strings are being read internally in your `include`.

Note that liquid allows the passing of [arbitrary arguments](https://jekyllrb.com/docs/includes/) to `include` templates. All these arguments will be stored, but won't have any effect unless the `include`'s [source](https://github.com/imagej/imagej.github.io/tree/main/_includes) actually does something with those arguments.

{% highlight liquid %}{% raw %}{% include echo content="This is the content argument" bracket="what if I pass {}?" gorilla="Why do we have a gorilla argument?" %}{% endraw %}{% endhighlight %}
{% include echo content="This is the content argument" bracket="what if I pass {}?" gorilla="Why do we have a gorilla argument?" %}
