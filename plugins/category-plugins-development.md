---
title: Development
breadcrumb: Development
author: admin
category: admin
layout: page
use_math: false
---

{% assign current_page_category = page.title | downcase%}

{% for page in site.pages %}{% assign p = page.category | downcase %}{% if p contains "plugins:"%}{% assign p_category = p | remove: "plugins:" %}{% if p_category == current_page_category %}
<p><a href="{{page.url | relative_url}}">{{page.title}}</a></p>
{% endif %}{% endif %}{% endfor %}