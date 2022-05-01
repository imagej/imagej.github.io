---
title: Keyboard Shortcuts
section: Contribute:Editing the Wiki
nav-links: true
---

The `key` include enables declaration of keyboard shortcuts in a clear way.

## Single keys

The syntax for talking about a key such as {% include key key="enter" %} is:
```liquid
{% raw %}{% include key key="enter" %}{% endraw %}
```

You can describe mouse actions such as {% include key key="right click" %}, too:
```liquid
{% raw %}{% include key key="right click" %}{% endraw %}
```

See the [list of input codes](#list-of-input-codes) below for a complete
summary of available key and mouse codes.

## Key combinations

You can declare a combination of keys such as {% include key keys="ctrl|c" %}
by separating them with `|` symbols:
{% capture key-combos-code %}
{% raw %}{% include key keys="ctrl|c" %}{% endraw %}
{% endcapture %}
{% capture key-combos-result %}
{% include key keys="ctrl|c" %}
{% endcapture %}
{% include editing/example code=key-combos-code result=key-combos-result %}

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
{% include editing/example code=keyboard-style-code result=keyboard-style-result %}

## Special code for OS-dependent Ctrl/Command

Frequently, keyboard combos using {% include key key="Ctrl" %} on Windows and
Linux will instead use {% include key key="command" style="mac" %} on macOS.
There is a special key code, `ctlcmd`, which can be used in this circumstance
to succinctly communicate this fact via a tooltip, to avoid needing a
parenthetical note about macOS every time.

{% capture ctlcmd-code %}
{% raw %}{% include key keys="ctlcmd|L" %}{% endraw %}
{% endcapture %}
{% capture ctlcmd-result %}
<div style="padding-left: 2em; width: 9rem; height: 4rem">{% include key keys="ctlcmd|L" %}</div>
{% endcapture %}
{% include editing/example code=ctlcmd-code result=ctlcmd-result %}

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
{% include editing/example code=custom-chain-symbols-code result=custom-chain-symbols-result %}

## List of input codes

{% assign keys = "Menu, Hyper, Meta, Windows, Command, Super, Fn, AltGr, Ctrl, Ctlcmd, Alt, Option, Shift, Num Lock, Caps Lock, Scroll Lock, Print Screen, Eject, Enter, Enter2, Backspace, Delete, Insert, Esc, Right, Left, Up, Down, Page Up, Page Down, Home, End, Tab, Space Bar, Clear, F1, ..., F20, A, ..., Z, Bar, Backslash, Left Click, Middle Click, Right Click, Double Click, Left Drag, Middle Drag, Right Drag, Mouse Wheel, Mouse Wheel Up, Mouse Wheel Down" | split: ", " -%}
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
