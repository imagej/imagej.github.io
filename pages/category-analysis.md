---
title: Analysis
author: admin
category: admin
layout: page
use_math: false
---

{% assign current_page_category = page.title %}

{% for page in site.pages %}{% if page.category == current_page_category %}
<p><a href="{{site.baseurl}}{{page.url}}">{{page.title}}</a><p> {% endif %}{% endfor %}