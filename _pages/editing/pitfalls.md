---
mediawiki: NONE
title: Pitfalls
section: Contribute:Editing the Wiki
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
{% include editing/example code=markdown-plus-html %}

### Markdown inside block elements

If you use a block element, Markdown won't be rendered inside:

{% capture block-elements-pitfall %}
<div>
Why isn't *this* in italics?
</div>
{% endcapture %}
{% include editing/example code=block-elements-pitfall %}

Add `markdown=1` to force Markdown rendering inside that element:

{% capture block-elements-with-markdown %}
<div markdown=1>
Yay, *this* is now in italics!
</div>
{% endcapture %}
{% include editing/example code=block-elements-with-markdown %}

{% include notice icon="warning" content="Be sure to ***put a newline before your `</div>`***! Otherwise you will get broken HTML. (Might be a bug in the kramdown renderer?)" %}

To avoid the pitfall with `</div>` and newlines, you can instead
target the parts you want Markdownified using `<span markdown=1>`:

{% capture targeted-markdown %}
<div>I like *asterisks*.
They are so <span markdown=1>**pretty**</span>!
Do you like *asterisks* too?</div>
{% endcapture %}
{% include editing/example code=targeted-markdown %}

### Using `capture` and `markdownify`

In some scenarios, it is easier to use Liquid's `capture` directive to store a
block of Markdown into a variable, and then use Jekyll's `markdownify` filter
to convert it to HTML, so that it can be more easily mixed with other HTML. One
such case is with the `<details>` to create an expandable block of content.
Here is an example:

{% capture capture-markdownify-code %}{% raw %}
{% capture periodic-table %}
| 1 | H  | Hydrogen  |  1.008 |
| 2 | He | Helium    |  4.003 |
| 3 | Li | Lithium   |  6.938 |
| 4 | Be | Beryllium |  9.102 |
| 5 | B  | Boron     | 10.806 |
| 6 | C  | Carbon    | 12.009 |
| 7 | N  | Nitrogen  | 14.006 |
| 8 | O  | Oxygen    | 15.999 |
| 9 | F  | Fluorine  | 18.998 |
{:.left}
{% endcapture %}
<details><summary>Check out this amazing table!</summary>
{{ periodic-table | markdownify }}
</details>
{% endraw %}{% endcapture %}
{% capture periodic-table %}
| 1 | H  | Hydrogen  |  1.008 |
| 2 | He | Helium    |  4.003 |
| 3 | Li | Lithium   |  6.938 |
| 4 | Be | Beryllium |  9.102 |
| 5 | B  | Boron     | 10.806 |
| 6 | C  | Carbon    | 12.009 |
| 7 | N  | Nitrogen  | 14.006 |
| 8 | O  | Oxygen    | 15.999 |
| 9 | F  | Fluorine  | 18.998 |
{:.left}
{% endcapture %}
{% capture capture-markdownify-result %}
<details><summary>Check out this amazing table!</summary>
{{ periodic-table | markdownify }}
</details>
{% endcapture %}
{% include editing/example
  code=capture-markdownify-code
  result=capture-markdownify-result %}

The `markdownify` filter can be very useful, but watch out: it does
not work well for inline elements because it will surround your
Markdown expression in `<p>...</p>` tags, ruining the inline effect:

{% capture bad-inline-markdownify-code %}{% raw %}
{% capture question %} Does *Monday* work? {% endcapture %}
<div>I asked: "{{ question | markdownify }}" and she nodded.</div>
{% endraw %}{% endcapture %}
{% capture question %} Does *Monday* work? {% endcapture %}
{% capture bad-inline-markdownify-result %}
<div>I asked: "{{ question | markdownify }}" and she nodded.</div>
{% endcapture %}
{% include editing/example
  code=bad-inline-markdownify-code
  result=bad-inline-markdownify-result %}

## Suppressing Markdown rendering

The `markdown` attribute can also be used the other way, to suppress
Markdown rendering inside an HTML element:

{% capture suppress-markdown %}
<span markdown=0>
Here are some **asterisks**.
</span>
{% endcapture %}
{% include editing/example code=suppress-markdown %}

## Conditional expressions

### Where conditionals work

Conditional expressions *may only be used with `if` and `unless` tags*!
They notably *do not work* with `assign` tags. So you cannot write a
truthy conditional expression and assign it to variable expecting it
to be set as `true` or `false`. If you need that, you can write:

{% highlight liquid %}{% raw %}
{%- if a or b or c -%}
  {%- assign my-boolean-flag = true -%}
{%- else -%}
  {%- assign my-boolean-flag = false -%}
{% endraw %}{% endhighlight %}

### Truthiness and falsiness

In Liquid, the [*only conditional expressions that evaluate to false* are
`false` and `nil`](https://shopify.github.io/liquid/basics/truthy-and-falsy/).
Unlike other languages, in Liquid even the empty string (`''`)
and the number zero (`0`) evaluate to `true`!

{% capture truthiness-table %}
| Expression                          | truthiness                                                                   |
|-------------------------------------|------------------------------------------------------------------------------|
| `"have a cow"`                      | {% if "have a cow" %} true {% else %} false {% endif %}                      |
| `""`                                | {% if "" %} true {% else %} false {% endif %}                                |
| `0`                                 | {% if 0 %} true {% else %} false {% endif %}                                 |
| `1`                                 | {% if 1 %} true {% else %} false {% endif %}                                 |
| `false`                             | {% if false %} true {% else %} false {% endif %}                             |
| `"false"`                           | {% if "false" %} true {% else %} false {% endif %}                           |
| `nil`                               | {% if nil %} true {% else %} false {% endif %}                               |
| `nil or ""`                         | {% if nil or "" %} true {% else %} false {% endif %}                         |
| `nil or "" or "hello" or "goodbye"` | {% if nil or "" or "hello" or "goodbye" %} true {% else %} false {% endif %} |
| `"" or "hello" or "goodbye"`        | {% if "" or "hello" or "goodbye" %} true {% else %} false {% endif %}        |
| `"hello" or "goodbye"`              | {% if "hello" or "goodbye" %} true {% else %} false {% endif %}              |
| `nil or ""`                         | {% if nil or "" %} true {% else %} false {% endif %}                         |
| `"" or nil`                         | {% if "" or nil %} true {% else %} false {% endif %}                         |
| `true or false`                     | {% if true or false %} true {% else %} false {% endif %}                     |
| `false or true`                     | {% if false or true %} true {% else %} false {% endif %}                     |
| `true or true`                      | {% if true or true %} true {% else %} false {% endif %}                      |
| `false or false`                    | {% if false or false %} true {% else %} false {% endif %}                    |
| `true or nil`                       | {% if true or nil %} true {% else %} false {% endif %}                       |
| `nil or true`                       | {% if nil or true %} true {% else %} false {% endif %}                       |
| `false or nil`                      | {% if false or nil %} true {% else %} false {% endif %}                      |
| `nil or false`                      | {% if nil or false %} true {% else %} false {% endif %}                      |
| `false or nil or true`              | {% if false or nil or true %} true {% else %} false {% endif %}              |
| `nil or false or true`              | {% if nil or false or true %} true {% else %} false {% endif %}              |
| `nil and ""`                        | {% if nil and "" %} true {% else %} false {% endif %}                        |
| `"" and nil`                        | {% if "" and nil %} true {% else %} false {% endif %}                        |
| `true and false`                    | {% if true and false %} true {% else %} false {% endif %}                    |
| `false and true`                    | {% if false and true %} true {% else %} false {% endif %}                    |
| `true and true`                     | {% if true and true %} true {% else %} false {% endif %}                     |
| `false and false`                   | {% if false and false %} true {% else %} false {% endif %}                   |
| `true and nil`                      | {% if true and nil %} true {% else %} false {% endif %}                      |
| `nil and true`                      | {% if nil and true %} true {% else %} false {% endif %}                      |
| `false and nil`                     | {% if false and nil %} true {% else %} false {% endif %}                     |
| `nil and false`                     | {% if nil and false %} true {% else %} false {% endif %}                     |
| `false and nil and true`            | {% if false and nil and true %} true {% else %} false {% endif %}            |
| `nil and false and true`            | {% if nil and false and true %} true {% else %} false {% endif %}            |
{:.left}
{% endcapture %}

<details><summary>Table of truthy and falsy example expressions</summary>
{{ truthiness-table | markdownify }}
</details>

### Order of operations

Unlike other languages, the `and` and `or` operators in Liquid have the same
precedence. And even more surprisingly, Liquid
[evaluates conditionals from right to left with equal operator
precedence](https://shopify.dev/docs/themes/liquid/reference/basics/operators#order-of-operations).

Here is an example:

{% capture operator-precedence-code %}{% raw %}
{%- if nil and 'me' or 'yes' and 'OK' -%}
  Oh yes I did!
{%- else -%}
  Oh no you didn't!
{%- endif -%}
{% endraw %}{% endcapture %}
{% capture operator-precedence-result %}
{%- if nil and 'me' or 'yes' and 'OK' -%}
  Oh yes I did!
{%- else -%}
  Oh no you didn't!
{%- endif -%}
{% endcapture %}
{% include editing/example
  code=operator-precedence-code
  result=operator-precedence-result %}

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
