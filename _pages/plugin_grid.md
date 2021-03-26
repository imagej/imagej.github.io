---
title: Plugin Grid
categories: admin
layout: page
---

<table>
<tbody>
{% assign plugin_page_1 = null %}
{% assign plugin_page_2 = null %}
{% assign plugin_page_3 = null %}

{% for page in site.pages %}
{% assign p = page.categories | downcase %}
{% if p contains "plugins" %}

{% if plugin_page_1 == null %}
{% capture plugin_page_1 %}
<a href="{{page.url | relative_url}}">{{page.title}}</a>
{% endcapture %}
{% continue %}
{% endif %}

{% if plugin_page_2 == null %}
{% capture plugin_page_2 %}
<a href="{{page.url | relative_url}}">{{page.title}}</a>
{% endcapture %}
{% continue %}
{% endif %}

{% if plugin_page_3 == null %}
{% capture plugin_page_3 %}
<a href="{{page.url | relative_url}}">{{page.title}}</a>
{% endcapture %}
{% continue %}
{% endif %}

<tr>
<td style="text-align: center">{{plugin_page_1}}</td>
<td style="text-align: center">{{plugin_page_2}}</td>
<td style="text-align: center">{{plugin_page_3}}</td>
</tr>

{% assign plugin_page_1 = null %}
{% assign plugin_page_2 = null %}
{% assign plugin_page_3 = null %}

{% endif %}
{% endfor %}
</tbody>
</table>