---
mediawiki: Category:Fundamental
title: Plugin Index
section: Extend
---

{%- assign category-string = "" -%}
{%- for p in site.pages -%}
  {%- assign tokens = p.url | split: "/" -%}
  {%- if tokens[1] != 'plugins' and tokens[1] != 'formats' -%} {%- continue -%} {%- endif -%}
  {%- if tokens[3] and tokens[3] != 'index' -%} {%- continue -%} {%- endif -%}
  {%- comment -%}
  It would be nicer to use the concat filter below, no?
  But that filter only became available in Jekyll 4.0.
  {%- endcomment -%}
  {%- for category in p.categories -%}
    {%- capture c -%} {{category | strip | capitalize}} {%- endcapture -%}
    {%- assign category-string = category-string | append: "|" | append: c -%}
  {%- endfor -%}
{%- endfor -%}
{%- assign all-categories = category-string | split: "|" | sort | uniq -%}
<div class="plugin-index" markdown=1>
{%- for category in all-categories -%}
  {%- if category == "" -%} {%- continue -%} {%- endif -%}
# {{category}}

{% include plugin-index/section category=category %}
{% endfor -%}
</div>

{%- comment -%}
# vi:syntax=liquid
{%- endcomment -%}
