---
title: Software Libraries
section: Explore:Libraries
---

This page catalogs software libraries upon which ImageJ is built,
and/or that may be of interest to the ImageJ community.

<ul style="height: 23em; display: flex; flex-direction: column; flex-wrap: wrap;">
{%- for p in site.pages -%}
  {%- assign tokens = p.url | split: "/" -%}
  {%- if tokens[1] != 'libs' -%} {%- continue -%} {%- endif -%}
  {%- if tokens[2] == 'index' -%} {%- continue -%} {%- endif -%}
  {%- if tokens[3] and tokens[3] != 'index' -%} {%- continue -%} {%- endif -%}
  <li><a href="{{p.url}}">{{p.title}}</a></li>
{%- endfor -%}
</ul>
