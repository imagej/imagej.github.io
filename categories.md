---
title: Browse categories
breadcrumb: Browse categories
layout: browse
---

{% for page in site.pages %}{% if page.url contains "category-" %}
<h2><a href="{{page.url}}">{{page.title}}</a></h2>{% endif %}
{% endfor %}