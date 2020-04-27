---
title: Analysis
breadcrumb: Analysis
author: admin
category: admin
layout: page
use_math: false
---

{% assign current_page_category = page.title | downcase%}

{% for page in site.pages %}{% assign p = page.category | downcase %}{% if p == current_page_category %}
<p><a href="{{site.baseurl}}{{page.url}}">{{page.title}}</a><p> {% endif %}{% endfor %}