---
title: Visualization
breadcrumb: Visualization
author: admin
categories: admin, plugins
layout: page
use_math: false
---

{% assign current_page_category = page.title | downcase%}

<div class="category">
{% for page in site.pages %}{% assign p = page.categories | downcase %}{% if p contains "admin" %}{% continue %}{% endif %}{% if p contains current_page_category %}
<p><a href="{{page.url | relative_url}}">{{page.title}}</a></p>
{% endif %}{% endfor %}
</div>