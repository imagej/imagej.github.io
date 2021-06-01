---
title: The Great Wiki Launch › Page List
section: Explore:Events
nav-links: true
nav-title: Page List
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

## Pages on the site

As we review pages and mark them done, they will automatically
disappear from the [Pages remaining](#pages-remaining) list,
and advance the progress bar. Our goal is to review every page
by the end of Friday, June 4! WE CAN DO IT! 💪

## Pages remaining

{%- assign todo-pages = site.pages | where_exp: "p", "p.mediawiki != nil" -%}

{%- assign remain = todo-pages | size -%}
{%- assign total = site.pages | size -%}
{%- assign done = total | minus: remain -%}
{%- assign percent = done | times: 100 | divided_by: total -%}

{%- comment -%} Progress bar! {%- endcomment %}
<style>
.progress-bar {
  width: 100%;
  border: 1px solid gray;
  position: relative;
  margin: 1em 0;
  text-align: center;
  font-weight: bold;
}
.progress-bar div {
  position: absolute;
  top: 0;
  opacity: 0.3;
  background-image: repeating-linear-gradient(120deg, skyblue, gold 30px, skyblue 30px, gold 60px);
  border-right: 1px solid black;
  height: 100%;
}
</style>
<div class="progress-bar">
  Pages complete: {{done}}/{{total}} ({{percent}}%)
  <div style="width: {{percent}}%"></div>
</div>

{%- comment -%} Sort pages by directory. {%- endcomment -%}
{%- assign last-page = todo-pages.size | minus: 1 -%}
{%- assign sort-pages = "" -%}
{%- for p in todo-pages -%}
  {%- capture dir -%} {%- include util/dir path=p.url -%} {%- endcapture -%}
  {%- assign sort-pages = sort-pages | append: "|"
    | append: dir | append: "#" | append: p.url
    | append: "#" | append: forloop.index0 -%}
{%- endfor -%}
{%- assign sort-keys = sort-pages | split: "|" | sort -%}

<div class="todo-list">
<ul>
<h3>/</h3>
{%- assign bucket = '' -%}
{% for s in sort-keys %}
  {%- if s == '' -%} {%- continue -%} {%- endif -%}
  {%- assign tokens = s | split: "#" -%}
  {%- assign dir = tokens[0] -%}
  {%- assign index0 = tokens[2] | plus: 0 -%}
  {%- assign p = todo-pages[index0] -%}
  {%- if bucket == dir -%}
    {%- comment -%} Same directory -- carry on! {%- endcomment -%}
  {%- else -%}
    {%- assign bucket = dir -%}
  </ul>
  <ul>
  <h3>{{bucket}}</h3>
  {%- endif -%}
<li><a href="{{p.url | replace: "/index", ""}}">{{p.title}}</a></li>
{% endfor %}
</ul>
</div>
