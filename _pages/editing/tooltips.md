---
title: Tooltips
section: Contribute:Editing the Wiki
nav-links: true
---

This page demonstrates how to use the `tooltip` include tag.

## Usage

Tooltips allow you to add text that only shows up when the reader's hovers their mouse over some anchor text.

{% highlight liquid %}{% raw %}{% include tooltip text="This is the anchor text that will be displayed." tooltip="I'm a tooltip!" %}{% endraw %}{% endhighlight %}
{% include tooltip text="This is the anchor text that will be displayed." tooltip="I'm a tooltip!" %}

### Style

Optional `style` can be applied to the anchor text.

{% highlight liquid %}{% raw %}{% include tooltip text="Here is some blue anchor text." tooltip="Non-blue tooltip" style="color:blue;" %}{% endraw %}{% endhighlight %}
{% include tooltip text="Here is some blue anchor text." tooltip="Non-blue tooltip" style="color:blue;" %}

### Length

Note that tooltips have a [200 piexl width by default](https://github.com/imagej/imagej.github.io/blob/4b671bffa49203e2396f07b585c123e792854cc8/assets/css/includes.css#L267-L292).

{% highlight liquid %}{% raw %}{% include tooltip text="This isn't going to end well." tooltip="Uh oh I have too much to say I shouldn't put it all in a tooltip!" style="color:blue;" %}{% endraw %}{% endhighlight %}
{% include tooltip text="This isn't going to end well." tooltip="Uh oh I have too much to say I shouldn't put it all in a tooltip!" style="color:blue;" %}
