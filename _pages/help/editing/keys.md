---
title: Demo keys
---

The `key` include enables declaration of keyboard shortcuts in a clear way.

## Single keys

The syntax to write {% include key key="ctrl" %} is:
```liquid
{% raw %}{% include key key="ctrl" %}{% endraw %}
```

## Key combinations

You can declare a combination of keys such as {% include key keys="ctrl|c" %}
by separating them with `|` symbols:
```liquid
{% raw %}{% include key keys="ctrl|c" %}{% endraw %}
```

## Keyboard styles

By default, keys are rendered in a platform-agnostic way, but you can use the
`style` parameter to render the keys to better match certain keyboards.

{%- highlight liquid -%}
{% raw %}{% include key key="super|f2" %}{% endraw %}
{% raw %}{% include key key="super|f2" style="pc" %}{% endraw %}
{% raw %}{% include key key="super|f2" style="mac" %}{% endraw %}
{%- endhighlight -%}
results in
{% include key key="super|f2" %},
{% include key key="super|f2" style="pc" %}, and
{% include key key="super|f2" style="mac" %} respectively.

## Custom chain symbols

Finally, if you want to connect a key combination together with something
other than the default `+` symbol, you can use the `chain` parameter
to do something different,
e.g. {% include key key="ctrl|cmd|esc" chain="&#9939;" %}:
{%- highlight liquid -%}
{% raw %}{% include key key="ctrl|cmd|esc" chain="&#9939;" %}{% endraw %}
{%- endhighlight -%}

## List of key codes

{%- assign keys = "Menu, Hyper, Meta, Windows, Command, Super, Fn, AltGr, Ctrl, Alt, Option, Shift, Num Lock, Caps Lock, Scroll Lock, Print Screen, Eject, Enter, Enter2, Backspace, Delete, Insert, Esc, Right, Left, Up, Down, Page Up, Page Down, Home, End, Tab, Space Bar, Clear, F1, ..., F20, A, ..., Z, Bar, Backslash" | split: ", " -%}

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
