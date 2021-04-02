---
title: Plugin Grid
categories: admin
layout: page
---

<div class="plugin-grid">
<table>
<tbody>
{% assign plugin_page_1 = null %}
{% assign plugin_page_2 = null %}
{% assign plugin_page_3 = null %}

{% for page in site.pages %}
{% assign url_array = page.url | split: "/" %}
{% if url_array[1] == "plugins" %}

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
</tbody>
</table>
</div>