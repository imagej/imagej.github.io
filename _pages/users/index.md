---
title: Users
---

{%- assign users = site.pages
	| where_exp:"page", "page.url contains '/users/'"
	| where_exp:"page", "page.url != '/users/index'"
	| sort: "title" -%}

<ul style="height: 80vw; display: flex; flex-direction: column; flex-wrap: wrap; list-style: none;">
{%- for user in users -%}
  <li><a href="{{user.url}}">{{user.title}}</a></li>
{%- endfor -%}
</ul>
