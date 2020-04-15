---
title: List of categories
layout: page
---

<div class="search" markdown="1">

{% assign raw_site_categories = site.pages | map: "category" | compact %}

{% capture x %}
{% for item in raw_site_categories %}
    {{item}}
{% endfor %}
{% endcapture %}

{% assign site_categories = x | strip_newlines | downcase | split: ' ' | uniq | sort %}

{% for category in site_categories %}{% if category == "your-category" %}{% continue %}{% endif %}
<h2>{{category | capitalize}}</h2>{% for page in site.pages %}{% assign p = page.category | downcase%}{% if p == category %}
<p><a href="{{site.baseurl}}{{page.url}}">{{page.title}}</a></p> {% endif %}{% endfor %}
{% endfor %}

</div>