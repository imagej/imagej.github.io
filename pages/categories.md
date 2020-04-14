---
title: List of categories
layout: page
---

<div class="search" markdown="1">

{% assign site_categories = site.pages | map: "category" | compact | sort | uniq %}

{% for category in site_categories %}{% if category == "YOUR-CATEGORY" %}{% continue %}{% endif %}
<h2>{{ category }}</h2>{% for page in site.pages %}{% if page.category == category %}
<p><a href="{{site.baseurl}}{{page.url}}">{{ page.title }}</a></p> {% endif %}{% endfor %}
{% endfor %}

</div>