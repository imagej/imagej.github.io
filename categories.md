---
title: Browse categories
breadcrumb: Browse
layout: page
---

<div class="search" markdown="1">


{% for page in site.pages %}{% if page.url contains "category-" %}
<h2><a href="{{page.url}}">{{page.title}}</a></h2>{% endif %}
{% endfor %}

</div>