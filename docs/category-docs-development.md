---
title: Development
breadcrumb: Development
author: admin
category: docs:admin
layout: page
use_math: false
---

{% assign current_page_category = page.title | downcase%}

{% for page in site.pages %}{% assign p = page.category | downcase %}{% if p contains "docs:"%}{% assign p_category = p | remove: "docs:" %}{% if p_category == current_page_category %}
<p><a href="{{page.url | relative_url}}">{{page.title}}</a></p>
{% endif %}{% endif %}{% endfor %}