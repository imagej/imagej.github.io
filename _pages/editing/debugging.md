---
title: Debugging
section: Contribute:Editing the Wiki
nav-links: true
---

The best way to collect debugging information is to [build the site locally](/editing/advanced). However if that isn't an option, this page documents tags which can be helpful.

## Echo

This `echo` include just prints its arguments, for debugging/learning purposes. This can be helpful in understanding Liquid syntax and how strings are being read internally by an `include`.

Arguments are printed as a comma-separated list of `"argument"==>"value"` pairs.

Note that liquid allows the passing of [arbitrary arguments](https://jekyllrb.com/docs/includes/) to `include` templates. All these arguments will be stored, but won't have any effect unless the `include`'s [source](https://github.com/imagej/imagej.github.io/tree/main/_includes) actually does something with those arguments.

{% highlight liquid %}{% raw %}{% include echo content="This is the content argument" bracket="what if I pass {}?" gorilla="Why do we have a gorilla argument?" %}{% endraw %}{% endhighlight %}
{% include echo content="This is the content argument" bracket="what if I pass {}?" gorilla="Why do we have a gorilla argument?" %}

### What's in a `page`?

{% include notice icon="tech" content="Ever wonder what all is part of the `page` data structure? Let's find out! 

(You can also do this with the `site` data structure, but be warned: the output will include every page body across the whole site!)" %}

{% highlight liquid %}{% raw %}{% include echo p=page %}{% endraw %}{% endhighlight %}
{% include echo p=page %}
