---
title: Widget ›YouTube
categories: Widgets
---

<iframe width="<!--{$width|escape:'html'|default:'425'}-->" height="<!--{$height|escape:'html'|default:355}-->" src="https://www.youtube.com/embed/<!--{if isset($playlist)}-->?listType=playlist&list=<!--{$playlist|escape:'urlpathinfo'}--><!--{else}--><!--{$id|escape:'urlpathinfo'}--><!--{/if}-->" frameborder="0" allowfullscreen></iframe>
