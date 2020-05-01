---
title: Documentation categories
breadcrumb: Documentation
layout: page
---

<div class="search" markdown="1">

{% assign raw_site_categories = site.pages | map: 'category' | compact %}

{% capture x %}
{% for item in raw_site_categories %}
    {{item}}
{% endfor %}
{% endcapture %}

{% assign site_categories = x | strip_newlines | downcase | split: ' ' | uniq | sort %}

{% for page in site.pages %}{% if page.url contains "category-docs" %}
<h2><a href="{{page.url}}">{{page.title}}</a></h2>{% endif %}
{% endfor %}

</div>