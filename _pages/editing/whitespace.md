---
title: Whitespace
section: Contribute:Editing the Wiki
nav-links: true
---

This page explains ways to manage whitespace rendering. It
demonstrates how the site treats whitespace, illustrating common
techniques, pitfalls, and workarounds to achieve needed formatting.

## Inserting newlines

### Default newline behavior

{% capture default-newline-behavior %}
What's
*up*?

How
are you?
{% endcapture %}
{% include code-example code=default-newline-behavior %}

### Two spaces at end of line

{% capture two-spaces-eol %}
Hello  
there
{% endcapture %}
{% include code-example code=two-spaces-eol %}

NB: This is a Markdown feature; note that there is no whitespace rendered after "Hello" at the end of the line.

### Two backslashes at end of line

{% capture two-backslashes-eol %}
What happens \\
if we use backslashes?
{% endcapture %}
{% include code-example code=two-backslashes-eol %}

NB: This is a Kramdown feature; note that there is a space included after "What happens" at the end of the line, because we included one before the backslashes.

### Using an explicit &lt;br&gt;

{% capture explicit-br %}
*Lions*<br>and **tigers**
{% endcapture %}
{% include code-example code=explicit-br %}

## Aligning text

Most fonts are variable width, and so you cannot rely on the characters lining up over multiple lines:

{% capture variable-width-misalignment %}
+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=+\\
| -=-=- Initializing Invincibility -=-=- |\\
+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=+
{% endcapture %}
{% include code-example code=variable-width-misalignment %}

### Aligning via code fences

If you need fixed-width font, you can use code fences:

{% capture fixed-width-code-fences %}
```
+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=+
| -=-=- Initializing Invincibility -=-=- |
+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=+
```
{% endcapture %}
{% include code-example code=fixed-width-code-fences %}

### Aligning via span style

If you really just want a fixed-width font, without additional styling,
you can use the `style` attribute on a surrounding `<span>` element:

{% capture fixed-width-span-style %}
<span style="font-family: monospace">
+-=-=-=-=-=-=-=-=-=-=-=-=-+\\
| -=- I'm *Invincible!* -=- |\\
+-=-=-=-=-=-=-=-=-=-=-=-=-+
</span>
{% endcapture %}
{% include code-example code=fixed-width-span-style %}

But if you do this on a block-level HTML element such as `<div>`, you won't be able to mix in Markdown anymore:

{% capture fixed-width-div-style-fail %}
What are you going to do, bleed on me?
<div style="font-family: monospace">
+-=-=-=-=-=-=-=-=-=-=-=-=-+\\
| -=- I'm *Invincible!* -=- |\\
+-=-=-=-=-=-=-=-=-=-=-=-=-+
</div> You're a loony.
{% endcapture %}
{% include code-example code=fixed-width-div-style-fail %}

...unless you add `markdown=1` to the element in question:

{% capture fixed-width-block-markdown %}
What are you going to do, bleed on me?
<div style="font-family: monospace" markdown=1>
+-=-=-=-=-=-=-=-=-=-=-=-=-+\\
| -=- I'm *Invincible!* -=- |\\
+-=-=-=-=-=-=-=-=-=-=-=-=-+
</div> You're a loony.
{% endcapture %}
{% include code-example code=fixed-width-block-markdown %}

...or [wrap the Markdowny parts in a
`<span markdown=1>`](/editing/pitfalls#markdown-inside-block-elements).

## Multiple spaces in a row

Normally, multiple spaces are squashed into one:

{% capture multiple-spaces-squashed %}
It's a   REALLY   big deal!
{% endcapture %}
{% include code-example code=multiple-spaces-squashed %}

If you want the extra spaces to stay, use HTML's `&nbsp;` code:

{% capture multiple-spaces-squashed %}
It's a &nbsp;&nbsp;&nbsp;REALLY&nbsp;&nbsp;&nbsp; big deal!
{% endcapture %}
{% include code-example code=multiple-spaces-squashed %}

## Preventing lines from wrapping at whitespace

Normally, lines can wrap wherever there is whitespace:

{% capture line-wrapping-at-whitespace %}
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
{% endcapture %}
{% include code-example code=line-wrapping-at-whitespace %}

If you don't want it to wrap at a particular place, you can use `&nbsp;` instead of a regular space, but for whole paragraphs as above, it quickly becomes tiresome. Another way is to use a styled span:

{% capture suppress-whitespace-wrapping %}
<span style="white-space: nowrap">
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
</span>
{% endcapture %}
{% include code-example code=suppress-whitespace-wrapping %}

## Beware of leading whitespace

If you use more than three spaces to indent lines, the Markdown processor will think you meant a code block:

{% capture beware-leading-whitespace %}
It works to indent 4 spaces without a leading blank line:
    although you may be surprised that it continues on the same line.

But if you indent 4 spaces after a blank line, watch out:

    Markdown kicks in, treating it as a block of code.
Even if a subsequent line is not indented!
{% endcapture %}
{% include code-example code=beware-leading-whitespace %}
