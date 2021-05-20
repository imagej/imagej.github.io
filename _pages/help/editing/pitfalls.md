---
title: Pitfalls
section: Help:Editing the Wiki
nav-links: true
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
{% include code-example code=markdown-plus-html %}

### Markdown inside block elements

If you use a block element, Markdown won't be rendered inside:

{% capture block-elements-pitfall %}
<div>
Why isn't *this* in italics?
</div>
{% endcapture %}
{% include code-example code=block-elements-pitfall %}

Add `markdown=1` to force Markdown rendering inside that element:

{% capture block-elements-with-markdown %}
<div markdown=1>
Yay, *this* is now in italics!
</div>
{% endcapture %}
{% include code-example code=block-elements-with-markdown %}

{% include notice icon="warning" content="Be sure to ***put a newline before your `</div>`***! Otherwise you will get broken HTML. (Might be a bug in the Kramdown renderer?)" %}

To avoid the pitfall with `</div>` and newlines, you can instead
target the parts you want Markdownified using `<span markdown=1>`:

{% capture targeted-markdown %}
<div>I like *asterisks*.
They are so <span markdown=1>**pretty**</span>!
Do you like *asterisks* too?</div>
{% endcapture %}
{% include code-example code=targeted-markdown %}

## Suppressing Markdown rendering

The `markdown` attribute can also be used the other way, to suppress
Markdown rendering inside an HTML element:

{% capture suppress-markdown %}
<span markdown=0>
Here are some **asterisks**.
</span>
{% endcapture %}
{% include code-example code=suppress-markdown %}

## Conditional expressions

### Where conditionals work

Conditional expressions *may only be used with `if` and `unless` tags*!
They notably *do not work* with `assign` tags. So you cannot write a
truthy conditional expression and assign it to variable expecting it
to be set as `true` or `false`. If you need that, you can write:

{% highlight liquid %}{% raw %}
{%- capture my-boolean-flag %}
{%- if a or b or c -%} true {%- else -%} false {%- endif -%}
{%- endcapture -%}
{% endraw %}{% endhighlight %}

### Truthiness and falsiness

In Liquid, the [*only conditional expressions that evaluate to false* are
`false` and `nil`](https://shopify.github.io/liquid/basics/truthy-and-falsy/).
Unlike other languages, in Liquid even the empty string (`''`)
and the number zero (`0`) evaluate to `true`!

<details><summary>Table of truthy and falsy example expressions</summary>

<table style="width: auto">
<tbody>
<tr><th>Expression</th><th>truthiness</th></tr>
<tr><td><code>"have a cow"</code></td><td>{% if "have a cow" %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>""</code></td><td>{% if "" %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>nil</code></td><td>{% if nil %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>nil or ""</code></td><td>{% if nil or "" %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>nil or "" or "hello" or "goodbye"</code></td><td>{% if nil or "" or "hello" or "goodbye" %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>"" or "hello" or "goodbye"</code></td><td>{% if "" or "hello" or "goodbye" %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>"hello" or "goodbye"</code></td><td>{% if "hello" or "goodbye" %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>nil or ""</code></td><td>{% if nil or "" %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>"" or nil</code></td><td>{% if "" or nil %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>true or false</code></td><td>{% if true or false %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>false or true</code></td><td>{% if false or true %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>true or true</code></td><td>{% if true or true %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>false or false</code></td><td>{% if false or false %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>true or nil</code></td><td>{% if true or nil %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>nil or true</code></td><td>{% if nil or true %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>false or nil</code></td><td>{% if false or nil %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>nil or false</code></td><td>{% if nil or false %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>false or nil or true</code></td><td>{% if false or nil or true %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>nil or false or true</code></td><td>{% if nil or false or true %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>nil and ""</code></td><td>{% if nil and "" %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>"" and nil</code></td><td>{% if "" and nil %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>true and false</code></td><td>{% if true and false %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>false and true</code></td><td>{% if false and true %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>true and true</code></td><td>{% if true and true %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>false and false</code></td><td>{% if false and false %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>true and nil</code></td><td>{% if true and nil %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>nil and true</code></td><td>{% if nil and true %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>false and nil</code></td><td>{% if false and nil %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>nil and false</code></td><td>{% if nil and false %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>false and nil and true</code></td><td>{% if false and nil and true %} true {% else %} false {% endif %}</td></tr>
<tr><td><code>nil and false and true</code></td><td>{% if nil and false and true %} true {% else %} false {% endif %}</td></tr>
</tbody>
</table>

</details>

### Order of operations

Unlike other languages, the `and` and `or` operators in Liquid have the same
precedence. And even more surprisingly, Liquid
[evaluates conditionals from right to left with equal operator
precedence](https://shopify.dev/docs/themes/liquid/reference/basics/operators#order-of-operations).

Here is an example:

{% highlight liquid %}{% raw %}
{%- if nil and 'me' or 'yes' and 'OK' -%} true {%- else -%} false {%- endif -%}
{% endraw %}{% endhighlight %}

equals {% if nil and 'me' or 'yes' and 'OK' -%} true {%- else -%} false {%- endif -%}.

Here is a breakdown of how Liquid is evaluating the above:

&rarr; `nil and ('me' or ('yes' and 'OK'))`\\
&rarr; `nil and ('me' or true)`\\
&rarr; `nil and true`\\
&rarr; `false`

The parentheses above are merely for illustration; *Liquid does not support
parentheses in conditional expressions* and your expression will be wrongly
evaluated if you try to use them.

In most other languages such as Python or JavaScript, it would be `true`:

```javascript
$ js
> console.log(null && 'me' || 'yes' && 'OK' ? 'true' : 'false')
true
```
```python
$ python
>>> print('true' if None and 'me' or 'yes' and 'OK' else 'false')
true
```

![](https://thumbs.gfycat.com/OblongJaggedBluemorphobutterfly-small.gif)
