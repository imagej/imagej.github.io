---
title: Editing the Wiki - Keyboard Shortcuts
section: Help:Editing the Wiki
---

The `key` include enables declaration of keyboard shortcuts in a clear way.

## Single keys

The syntax for talking about a key such as {% include key key="enter" %} is:
```liquid
{% raw %}{% include key key="enter" %}{% endraw %}
```

See the [list of key codes](#list-of-key-codes) below for a complete summary of
available key codes.

## Key combinations

You can declare a combination of keys such as {% include key keys="ctrl|c" %}
by separating them with `|` symbols:
{% capture key-combos-code %}
{% raw %}{% include key keys="ctrl|c" %}{% endraw %}
{% endcapture %}
{% capture key-combos-result %}
{% include key keys="ctrl|c" %}
{% endcapture %}
{% include example code=key-combos-code result=key-combos-result %}

## Keyboard styles

By default, keys are rendered in a platform-agnostic way, but you can use the
`style` parameter to render the keys to better match certain keyboards.

{% capture keyboard-style-code -%}
{% raw %}| Default   | {% include key key="ctrl|tab" %}             |{% endraw %}
{% raw %}| PC style  | {% include key key="ctrl|tab" style="pc" %}  |{% endraw %}
{% raw %}| Mac style | {% include key key="ctrl|tab" style="mac" %} |{% endraw %}
{% endcapture %}
{% capture keyboard-style-result %}
| Default   | {% include key key="ctrl|tab" %}             |
| PC style  | {% include key key="ctrl|tab" style="pc" %}  |
| Mac style | {% include key key="ctrl|tab" style="mac" %} |
{% endcapture %}
{% include example code=keyboard-style-code result=keyboard-style-result %}

## Custom chain symbols

Finally, if you want to connect a key combination together with something
other than the default `+` symbol, you can use the `chain` parameter
to do something different:

{% capture custom-chain-symbols-code %}
{% raw %}{% include key keys="ctrl|shift|esc" chain="&#9939;" %}{% endraw %}
{% endcapture %}
{% capture custom-chain-symbols-result %}
{% include key keys="ctrl|shift|esc" chain="&#9939;" %}
{% endcapture %}
{% include example code=custom-chain-symbols-code result=custom-chain-symbols-result %}

## List of key codes

{% assign keys = "Menu, Hyper, Meta, Windows, Command, Super, Fn, AltGr, Ctrl, Alt, Option, Shift, Num Lock, Caps Lock, Scroll Lock, Print Screen, Eject, Enter, Enter2, Backspace, Delete, Insert, Esc, Right, Left, Up, Down, Page Up, Page Down, Home, End, Tab, Space Bar, Clear, F1, ..., F20, A, ..., Z, Bar, Backslash" | split: ", " -%}
{::nomarkdown}
<table>
  <tr>
    <th>Key code</th>
    <th>Default style</th>
    <th>PC style</th>
    <th>Mac style</th>
  </tr>
  {%- for key in keys -%}
    {%- if key == "..." -%}
  <tr><td>&#8942;</td><td>&#8942;</td><td>&#8942;</td><td>&#8942;</td></tr>
    {%- else -%}
  <tr>
    <td>{{key}}</td>
    <td>{% include key key=key %}</td>
    <td>{% include key key=key style="pc" %}</td>
    <td>{% include key key=key style="mac" %}</td>
  </tr>
    {%- endif -%}
  {%- endfor -%}
</table>
{:/}
