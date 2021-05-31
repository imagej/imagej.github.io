---
title: Software Index
section: Explore:Software
---

This page catalogs software projects that may be of interest to the ImageJ community.

<ul style="height: 23em; display: flex; flex-direction: column; flex-wrap: wrap;">
{%- for page in site.pages -%}
  {%- assign tokens = page.url | split: "/" -%}
  {%- if tokens[1] != 'software' -%} {%- continue -%} {%- endif -%}
  {%- if tokens[2] == 'index' -%} {%- continue -%} {%- endif -%}
  {%- if tokens[3] and tokens[3] != 'index' -%} {%- continue -%} {%- endif -%}
  <li><a href="{{page.url}}">{{page.title}}</a></li>
{%- endfor -%}
</ul>
