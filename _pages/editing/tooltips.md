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

### Styling

Optional `style` can be applied to the anchor text.

{% highlight liquid %}{% raw %}{% include tooltip text="Here is some blue anchor text." tooltip="Non-blue tooltip" style="color:blue;" %}{% endraw %}{% endhighlight %}
{% include tooltip text="Here is some blue anchor text." tooltip="Non-blue tooltip" style="color:blue;" %}

### Position

Tooltips are aligned down and to the right of the anchor text, but in some cases, a different location would be preferable. For example:

{% highlight liquid %}{% raw %}
<div style="text-align: right">
{% include tooltip width="350px" text="Bad" tooltip="This tooltip, unfortunately, goes off the right-hand side of the screen, because we didn't take steps to position it differently." %}
</div>
{% endraw %}{% endhighlight %}

<div style="text-align: right">
{% include tooltip width="350px" text="Bad" tooltip="This tooltip, unfortunately, goes off the right-hand side of the screen, because we didn't take steps to position it differently." %}
</div>

But we can fix it using the `left` property:

{% highlight liquid %}{% raw %}
<div style="text-align: right">
{% include tooltip width="350px" left="-320px" text="Good" tooltip="This tooltip, fortunately, does not go off the right-hand side of the screen, because we took steps to position it differently." %}
</div>
{% endraw %}{% endhighlight %}

<div style="text-align: right">
{% include tooltip width="350px" left="-320px" text="Good" tooltip="This tooltip, fortunately, does not go off the right-hand side of the screen, because we took steps to position it differently." %}
</div>

Similarly, the `top` property can be used to control a tooltip's vertical placement.

{% highlight liquid %}{% raw %}
<div style="text-align: center">
{% include tooltip top="-2em" text="Vertical override" tooltip="Rarely needed, but good to know!" %}
</div>
{% endraw %}{% endhighlight %}

<div style="text-align: center">
{% include tooltip top="-2em" text="Vertical override" tooltip="Rarely needed, but good to know!" %}
</div>

### Length

By default, short tooltips are rendered on a single line, while longer tooltips (48 characters or more) are given a fixed width of `20em`:

{% highlight liquid %}{% raw %}{% include tooltip text="Here's a long tooltip with default width." tooltip="Uh oh I have so much to say... should I really put it all in a tooltip? Sure, let's go ahead and do it, just to demonstrate what it looks like." %}{% endraw %}{% endhighlight %}
{% include tooltip text="Here's a long tooltip with default width." tooltip="Uh oh I have so much to say... should I really put it all in a tooltip? Sure, let's go ahead and do it, just to demonstrate what it looks like." %}

But you can set the `width` parameter to override it:

{% highlight liquid %}{% raw %}{% include tooltip width="16em" text="Here's the same tooltip but 16em wide." tooltip="Uh oh I have so much to say... should I really put it all in a tooltip? Sure, let's go ahead and do it, just to demonstrate what it looks like." %}{% endraw %}{% endhighlight %}
{% include tooltip width="16em" text="Here's the same tooltip but 16em wide." tooltip="Uh oh I have so much to say... should I really put it all in a tooltip? Sure, let's go ahead and do it, just to demonstrate what it looks like." %}
