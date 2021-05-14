---
title: Editing the Wiki - Formatting Pitfalls
section: Help:Editing the Wiki
---

This page covers pitfalls to be aware of when writing content for the site.

This site uses Markdown for rich text formatting. It is powerful and friendly,
but not a full replacement for raw HTML. Fortunately, you can mix HTML into
your Markdown, as long as you are careful!

## Mixing Markdown and HTML

You can apply CSS styles to inline HTML elements such as `<span>`,
and any nearby Markdown will still be applied:

{% capture markdown-plus-html %}
Enjoy some
*<span style="color: red">colored</span>
<span style="color: green">text</span>
<span style="color: blue">in italics</span>*!
{% endcapture %}
{% include example code=markdown-plus-html %}

### Markdown inside block elements

If you use a block element, Markdown won't be rendered inside:

{% capture block-elements-pitfall %}
<div>
Why isn't *this* in italics?
</div>
{% endcapture %}
{% include example code=block-elements-pitfall %}

Add `markdown=1` to force Markdown rendering inside that element:

{% capture block-elements-with-markdown %}
<div markdown=1>
Yay, *this* is now in italics!
</div>
{% endcapture %}
{% include example code=block-elements-with-markdown %}

{% include warning-box content="Be sure to ***put a newline before your `</div>`***! Otherwise you will get broken HTML. (Might be a bug in the Kramdown renderer?)" %}

To avoid the pitfall with `</div>` and newlines, you can instead
target the parts you want Markdownified using `<span markdown=1>`:

{% capture targeted-markdown %}
<div>I like *asterisks*.
They are so <span markdown=1>**pretty**</span>!
Do you like *asterisks* too?</div>
{% endcapture %}
{% include example code=targeted-markdown %}

## Suppressing Markdown rendering

The `markdown` attribute can also be used the other way, to suppress
Markdown rendering inside an HTML element:

{% capture suppress-markdown %}
<span markdown=0>
Here are some **asterisks**.
</span>
{% endcapture %}
{% include example code=suppress-markdown %}

## Coming soon

More pitfalls will be described here. Until then, this section
exists to trigger creation of the table of contents. ;-)
