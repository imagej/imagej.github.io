---
mediawiki: NONE
title: Pages for Review
---

<style>
.todo-list {
  column-width: 18em;
  column-gap: 2em;
  line-height: 1em;
}
.todo-list ul {
  break-inside: avoid;
}
.todo-list li {
  padding-bottom: 0.5em;
}
</style>

## Review Needed

{%- assign todo-pages = site.pages | where_exp: "p", "p.mediawiki != nil" | sort: "url" -%}
{%- assign depth = 1 %}
<div class="todo-list">
<ul>
<h3>/</h3>
{%- assign bucket = '' -%}
{% for p in todo-pages %}
{%- capture this-bucket -%} {%- include util/dir path=p.url -%} {%- endcapture -%}
{%- if bucket == this-bucket -%}
  {%- comment -%} Same directory -- carry on! {%- endcomment -%}
{%- else -%}
  {%- assign bucket = this-bucket -%}
  </ul>
  <ul>
  <h3>{{bucket}}</h3>
{%- endif -%}
<li><a href="{{p.url | replace: "/index", ""}}">{{p.title}}</a></li>
{% endfor %}
</ul>
</div>

## Review Complete

{% assign done-pages = site.pages | where:"mediawiki", nil | sort: "url" %}

<ul class="todo-list">
{% for p in done-pages %}
<li><a href="{{p.url}}">{{p.title}}</a></li>
{% endfor %}
</ul>
