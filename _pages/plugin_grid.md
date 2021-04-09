---
title: Plugin Grid
categories: admin
---

# Analysis

{% assign plugin_page_1 = null %}
{% assign plugin_page_2 = null %}
{% assign plugin_page_3 = null %}
{% assign plugin_filter = "analysis" %}
<div class="plugin-grid">
<table>
<tbody>
{% for page in site.pages %}
{% assign analysis_url_array = page.url | split: "/" %}
{% if analysis_url_array[1] == "plugins"%}
{% assign category_array = page.categories| downcase | split: "," %}
{% for item in category_array %}
{% if item contains plugin_filter %}
{% if plugin_page_1 == null %}
{% capture plugin_page_1 %}
<img src="/images/placeholder.png" height="25"><a href="{{page.url | relative_url}}">{{page.title}}</a>
{% endcapture %}
{% continue %}
{% endif %}
{% if plugin_page_2 == null %}
{% capture plugin_page_2 %}
<img src="/images/placeholder.png" height="25"><a href="{{page.url | relative_url}}">{{page.title}}</a>
{% endcapture %}
{% continue %}
{% endif %}
{% if plugin_page_3 == null %}
{% capture plugin_page_3 %}
<img src="/images/placeholder.png" height="25"><a href="{{page.url | relative_url}}">{{page.title}}</a>
{% endcapture %}
{% endif %}
<tr>
<td>{{plugin_page_1}}</td>
<td>{{plugin_page_2}}</td>
<td>{{plugin_page_3}}</td>
</tr>
{% assign plugin_page_1 = null %}
{% assign plugin_page_2 = null %}
{% assign plugin_page_3 = null %}
{% endif %}
{% endfor %}
{% endif %}
{% endfor %}
</tbody>
</table>
</div>

# Binary

{% assign plugin_page_1 = null %}
{% assign plugin_page_2 = null %}
{% assign plugin_page_3 = null %}
{% assign plugin_filter = "binary" %}
<div class="plugin-grid">
<table>
<tbody>
{% for page in site.pages %}
{% assign analysis_url_array = page.url | split: "/" %}
{% if analysis_url_array[1] == "plugins"%}
{% assign category_array = page.categories| downcase | split: "," %}
{% for item in category_array %}
{% if item contains plugin_filter %}
{% if plugin_page_1 == null %}
{% capture plugin_page_1 %}
<img src="/images/placeholder.png" height="25"><a href="{{page.url | relative_url}}">{{page.title}}</a>
{% endcapture %}
{% continue %}
{% endif %}
{% if plugin_page_2 == null %}
{% capture plugin_page_2 %}
<img src="/images/placeholder.png" height="25"><a href="{{page.url | relative_url}}">{{page.title}}</a>
{% endcapture %}
{% continue %}
{% endif %}
{% if plugin_page_3 == null %}
{% capture plugin_page_3 %}
<img src="/images/placeholder.png" height="25"><a href="{{page.url | relative_url}}">{{page.title}}</a>
{% endcapture %}
{% endif %}
<tr>
<td>{{plugin_page_1}}</td>
<td>{{plugin_page_2}}</td>
<td>{{plugin_page_3}}</td>
</tr>
{% assign plugin_page_1 = null %}
{% assign plugin_page_2 = null %}
{% assign plugin_page_3 = null %}
{% endif %}
{% endfor %}
{% endif %}
{% endfor %}
</tbody>
</table>
</div>

# Colocalization

{% assign plugin_page_1 = null %}
{% assign plugin_page_2 = null %}
{% assign plugin_page_3 = null %}
{% assign plugin_filter = "colocalization" %}
<div class="plugin-grid">
<table>
<tbody>
{% for page in site.pages %}
{% assign analysis_url_array = page.url | split: "/" %}
{% if analysis_url_array[1] == "plugins"%}
{% assign category_array = page.categories| downcase | split: "," %}
{% for item in category_array %}
{% if item contains plugin_filter %}
{% if plugin_page_1 == null %}
{% capture plugin_page_1 %}
<img src="/images/placeholder.png" height="25"><a href="{{page.url | relative_url}}">{{page.title}}</a>
{% endcapture %}
{% continue %}
{% endif %}
{% if plugin_page_2 == null %}
{% capture plugin_page_2 %}
<img src="/images/placeholder.png" height="25"><a href="{{page.url | relative_url}}">{{page.title}}</a>
{% endcapture %}
{% continue %}
{% endif %}
{% if plugin_page_3 == null %}
{% capture plugin_page_3 %}
<img src="/images/placeholder.png" height="25"><a href="{{page.url | relative_url}}">{{page.title}}</a>
{% endcapture %}
{% endif %}
<tr>
<td>{{plugin_page_1}}</td>
<td>{{plugin_page_2}}</td>
<td>{{plugin_page_3}}</td>
</tr>
{% assign plugin_page_1 = null %}
{% assign plugin_page_2 = null %}
{% assign plugin_page_3 = null %}
{% endif %}
{% endfor %}
{% endif %}
{% endfor %}
</tbody>
</table>
</div>

# Deconvolution

{% assign plugin_page_1 = null %}
{% assign plugin_page_2 = null %}
{% assign plugin_page_3 = null %}
{% assign plugin_filter = "deconvolution" %}
<div class="plugin-grid">
<table>
<tbody>
{% for page in site.pages %}
{% assign analysis_url_array = page.url | split: "/" %}
{% if analysis_url_array[1] == "plugins"%}
{% assign category_array = page.categories| downcase | split: "," %}
{% for item in category_array %}
{% if item contains plugin_filter %}
{% if plugin_page_1 == null %}
{% capture plugin_page_1 %}
<img src="/images/placeholder.png" height="25"><a href="{{page.url | relative_url}}">{{page.title}}</a>
{% endcapture %}
{% continue %}
{% endif %}
{% if plugin_page_2 == null %}
{% capture plugin_page_2 %}
<img src="/images/placeholder.png" height="25"><a href="{{page.url | relative_url}}">{{page.title}}</a>
{% endcapture %}
{% continue %}
{% endif %}
{% if plugin_page_3 == null %}
{% capture plugin_page_3 %}
<img src="/images/placeholder.png" height="25"><a href="{{page.url | relative_url}}">{{page.title}}</a>
{% endcapture %}
{% endif %}
<tr>
<td>{{plugin_page_1}}</td>
<td>{{plugin_page_2}}</td>
<td>{{plugin_page_3}}</td>
</tr>
{% assign plugin_page_1 = null %}
{% assign plugin_page_2 = null %}
{% assign plugin_page_3 = null %}
{% endif %}
{% endfor %}
{% endif %}
{% endfor %}
</tbody>
</table>
</div>

# Filtering

{% assign plugin_page_1 = null %}
{% assign plugin_page_2 = null %}
{% assign plugin_page_3 = null %}
{% assign plugin_filter = "filtering" %}
<div class="plugin-grid">
<table>
<tbody>
{% for page in site.pages %}
{% assign analysis_url_array = page.url | split: "/" %}
{% if analysis_url_array[1] == "plugins"%}
{% assign category_array = page.categories| downcase | split: "," %}
{% for item in category_array %}
{% if item contains plugin_filter %}
{% if plugin_page_1 == null %}
{% capture plugin_page_1 %}
<img src="/images/placeholder.png" height="25"><a href="{{page.url | relative_url}}">{{page.title}}</a>
{% endcapture %}
{% continue %}
{% endif %}
{% if plugin_page_2 == null %}
{% capture plugin_page_2 %}
<img src="/images/placeholder.png" height="25"><a href="{{page.url | relative_url}}">{{page.title}}</a>
{% endcapture %}
{% continue %}
{% endif %}
{% if plugin_page_3 == null %}
{% capture plugin_page_3 %}
<img src="/images/placeholder.png" height="25"><a href="{{page.url | relative_url}}">{{page.title}}</a>
{% endcapture %}
{% endif %}
<tr>
<td>{{plugin_page_1}}</td>
<td>{{plugin_page_2}}</td>
<td>{{plugin_page_3}}</td>
</tr>
{% assign plugin_page_1 = null %}
{% assign plugin_page_2 = null %}
{% assign plugin_page_3 = null %}
{% endif %}
{% endfor %}
{% endif %}
{% endfor %}
</tbody>
</table>
</div>

# Registration

{% assign plugin_page_1 = null %}
{% assign plugin_page_2 = null %}
{% assign plugin_page_3 = null %}
{% assign plugin_filter = "registration" %}
<div class="plugin-grid">
<table>
<tbody>
{% for page in site.pages %}
{% assign analysis_url_array = page.url | split: "/" %}
{% if analysis_url_array[1] == "plugins"%}
{% assign category_array = page.categories| downcase | split: "," %}
{% for item in category_array %}
{% if item contains plugin_filter %}
{% if plugin_page_1 == null %}
{% capture plugin_page_1 %}
<img src="/images/placeholder.png" height="25"><a href="{{page.url | relative_url}}">{{page.title}}</a>
{% endcapture %}
{% continue %}
{% endif %}
{% if plugin_page_2 == null %}
{% capture plugin_page_2 %}
<img src="/images/placeholder.png" height="25"><a href="{{page.url | relative_url}}">{{page.title}}</a>
{% endcapture %}
{% continue %}
{% endif %}
{% if plugin_page_3 == null %}
{% capture plugin_page_3 %}
<img src="/images/placeholder.png" height="25"><a href="{{page.url | relative_url}}">{{page.title}}</a>
{% endcapture %}
{% endif %}
<tr>
<td>{{plugin_page_1}}</td>
<td>{{plugin_page_2}}</td>
<td>{{plugin_page_3}}</td>
</tr>
{% assign plugin_page_1 = null %}
{% assign plugin_page_2 = null %}
{% assign plugin_page_3 = null %}
{% endif %}
{% endfor %}
{% endif %}
{% endfor %}
</tbody>
</table>
</div>

# Scripting

{% assign plugin_page_1 = null %}
{% assign plugin_page_2 = null %}
{% assign plugin_page_3 = null %}
{% assign plugin_filter = "scripting" %}
<div class="plugin-grid">
<table>
<tbody>
{% for page in site.pages %}
{% assign analysis_url_array = page.url | split: "/" %}
{% if analysis_url_array[1] == "plugins"%}
{% assign category_array = page.categories| downcase | split: "," %}
{% for item in category_array %}
{% if item contains plugin_filter %}
{% if plugin_page_1 == null %}
{% capture plugin_page_1 %}
<img src="/images/placeholder.png" height="25"><a href="{{page.url | relative_url}}">{{page.title}}</a>
{% endcapture %}
{% continue %}
{% endif %}
{% if plugin_page_2 == null %}
{% capture plugin_page_2 %}
<img src="/images/placeholder.png" height="25"><a href="{{page.url | relative_url}}">{{page.title}}</a>
{% endcapture %}
{% continue %}
{% endif %}
{% if plugin_page_3 == null %}
{% capture plugin_page_3 %}
<img src="/images/placeholder.png" height="25"><a href="{{page.url | relative_url}}">{{page.title}}</a>
{% endcapture %}
{% endif %}
<tr>
<td>{{plugin_page_1}}</td>
<td>{{plugin_page_2}}</td>
<td>{{plugin_page_3}}</td>
</tr>
{% assign plugin_page_1 = null %}
{% assign plugin_page_2 = null %}
{% assign plugin_page_3 = null %}
{% endif %}
{% endfor %}
{% endif %}
{% endfor %}
</tbody>
</table>
</div>

# Segmentation

{% assign plugin_page_1 = null %}
{% assign plugin_page_2 = null %}
{% assign plugin_page_3 = null %}
{% assign plugin_filter = "segmentation" %}
<div class="plugin-grid">
<table>
<tbody>
{% for page in site.pages %}
{% assign analysis_url_array = page.url | split: "/" %}
{% if analysis_url_array[1] == "plugins"%}
{% assign category_array = page.categories| downcase | split: "," %}
{% for item in category_array %}
{% if item contains plugin_filter %}
{% if plugin_page_1 == null %}
{% capture plugin_page_1 %}
<img src="/images/placeholder.png" height="25"><a href="{{page.url | relative_url}}">{{page.title}}</a>
{% endcapture %}
{% continue %}
{% endif %}
{% if plugin_page_2 == null %}
{% capture plugin_page_2 %}
<img src="/images/placeholder.png" height="25"><a href="{{page.url | relative_url}}">{{page.title}}</a>
{% endcapture %}
{% continue %}
{% endif %}
{% if plugin_page_3 == null %}
{% capture plugin_page_3 %}
<img src="/images/placeholder.png" height="25"><a href="{{page.url | relative_url}}">{{page.title}}</a>
{% endcapture %}
{% endif %}
<tr>
<td>{{plugin_page_1}}</td>
<td>{{plugin_page_2}}</td>
<td>{{plugin_page_3}}</td>
</tr>
{% assign plugin_page_1 = null %}
{% assign plugin_page_2 = null %}
{% assign plugin_page_3 = null %}
{% endif %}
{% endfor %}
{% endif %}
{% endfor %}
</tbody>
</table>
</div>

# Tracking

{% assign plugin_page_1 = null %}
{% assign plugin_page_2 = null %}
{% assign plugin_page_3 = null %}
{% assign plugin_filter = "tracking" %}
<div class="plugin-grid">
<table>
<tbody>
{% for page in site.pages %}
{% assign analysis_url_array = page.url | split: "/" %}
{% if analysis_url_array[1] == "plugins"%}
{% assign category_array = page.categories| downcase | split: "," %}
{% for item in category_array %}
{% if item contains plugin_filter %}
{% if plugin_page_1 == null %}
{% capture plugin_page_1 %}
<img src="/images/placeholder.png" height="25"><a href="{{page.url | relative_url}}">{{page.title}}</a>
{% endcapture %}
{% continue %}
{% endif %}
{% if plugin_page_2 == null %}
{% capture plugin_page_2 %}
<img src="/images/placeholder.png" height="25"><a href="{{page.url | relative_url}}">{{page.title}}</a>
{% endcapture %}
{% continue %}
{% endif %}
{% if plugin_page_3 == null %}
{% capture plugin_page_3 %}
<img src="/images/placeholder.png" height="25"><a href="{{page.url | relative_url}}">{{page.title}}</a>
{% endcapture %}
{% endif %}
<tr>
<td>{{plugin_page_1}}</td>
<td>{{plugin_page_2}}</td>
<td>{{plugin_page_3}}</td>
</tr>
{% assign plugin_page_1 = null %}
{% assign plugin_page_2 = null %}
{% assign plugin_page_3 = null %}
{% endif %}
{% endfor %}
{% endif %}
{% endfor %}
</tbody>
</table>
</div>

# Tutorials

{% assign plugin_page_1 = null %}
{% assign plugin_page_2 = null %}
{% assign plugin_page_3 = null %}
{% assign plugin_filter = "tutorials" %}
<div class="plugin-grid">
<table>
<tbody>
{% for page in site.pages %}
{% assign analysis_url_array = page.url | split: "/" %}
{% if analysis_url_array[1] == "plugins"%}
{% assign category_array = page.categories| downcase | split: "," %}
{% for item in category_array %}
{% if item contains plugin_filter %}
{% if plugin_page_1 == null %}
{% capture plugin_page_1 %}
<img src="/images/placeholder.png" height="25"><a href="{{page.url | relative_url}}">{{page.title}}</a>
{% endcapture %}
{% continue %}
{% endif %}
{% if plugin_page_2 == null %}
{% capture plugin_page_2 %}
<img src="/images/placeholder.png" height="25"><a href="{{page.url | relative_url}}">{{page.title}}</a>
{% endcapture %}
{% continue %}
{% endif %}
{% if plugin_page_3 == null %}
{% capture plugin_page_3 %}
<img src="/images/placeholder.png" height="25"><a href="{{page.url | relative_url}}">{{page.title}}</a>
{% endcapture %}
{% endif %}
<tr>
<td>{{plugin_page_1}}</td>
<td>{{plugin_page_2}}</td>
<td>{{plugin_page_3}}</td>
</tr>
{% assign plugin_page_1 = null %}
{% assign plugin_page_2 = null %}
{% assign plugin_page_3 = null %}
{% endif %}
{% endfor %}
{% endif %}
{% endfor %}
</tbody>
</table>
</div>

# Visualization

{% assign plugin_page_1 = null %}
{% assign plugin_page_2 = null %}
{% assign plugin_page_3 = null %}
{% assign plugin_filter = "visualization" %}
<div class="plugin-grid">
<table>
<tbody>
{% for page in site.pages %}
{% assign analysis_url_array = page.url | split: "/" %}
{% if analysis_url_array[1] == "plugins"%}
{% assign category_array = page.categories| downcase | split: "," %}
{% for item in category_array %}
{% if item contains plugin_filter %}
{% if plugin_page_1 == null %}
{% capture plugin_page_1 %}
<img src="/images/placeholder.png" height="25"><a href="{{page.url | relative_url}}">{{page.title}}</a>
{% endcapture %}
{% continue %}
{% endif %}
{% if plugin_page_2 == null %}
{% capture plugin_page_2 %}
<img src="/images/placeholder.png" height="25"><a href="{{page.url | relative_url}}">{{page.title}}</a>
{% endcapture %}
{% continue %}
{% endif %}
{% if plugin_page_3 == null %}
{% capture plugin_page_3 %}
<img src="/images/placeholder.png" height="25"><a href="{{page.url | relative_url}}">{{page.title}}</a>
{% endcapture %}
{% endif %}
<tr>
<td>{{plugin_page_1}}</td>
<td>{{plugin_page_2}}</td>
<td>{{plugin_page_3}}</td>
</tr>
{% assign plugin_page_1 = null %}
{% assign plugin_page_2 = null %}
{% assign plugin_page_3 = null %}
{% endif %}
{% endfor %}
{% endif %}
{% endfor %}
</tbody>
</table>
</div>