---
title: Search demo
layout: search
---

<form action="search" method="get">
    <label for="search-box">Enter text to search:</label>
    <input type="text" id="search-box" name="query">
    <input type="submit" value="search" onclick="displaySearchResults();">
</form>

<ul id="search-results"></ul>

<script>
    window.store = {
        {% for page in site.pages %}
            "{{ page.url | slugify }}": {
                "title": "{{ page.title | xml_escape }}",
                "author": "{{ page.author | xml_escape }}",
                "category": "{{ page.category | xml_escape }}",
                "content": {{ page.content | strip_html | strip_newlines | jsonify }},
                "url": "{{ page.url | xml_escape }}"
            }
            {% unless forloop.last %}, {% endunless %}
        {% endfor %}
    };
</script>
<script src="../assets/js/lunr.js"></script>
<script src="../assets/js/search.js"></script>