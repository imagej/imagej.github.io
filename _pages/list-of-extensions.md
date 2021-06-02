---
mediawiki: Plugin_Index
title: List of Extensions
section: Extend
---
{%- assign category-string = "" -%}
{%- for page in site.pages -%}
  {%- assign tokens = page.url | split: "/" -%}
  {%- if tokens[3] and tokens[3] != 'index' -%} {%- continue -%} {%- endif -%}
  {%- comment -%}
  It would be nicer to use the concat filter below, no?
  But that filter only became available in Jekyll 4.0.
  {%- endcomment -%}
  {%- for category in page.categories -%}
    {%- capture c -%} {{category | strip}} {%- endcapture -%}
    {%- assign category-string = category-string | append: "|" | append: c -%}
  {%- endfor -%}
{%- endfor -%}
{%- assign all-categories = category-string | split: "|" | sort | uniq -%}

<script>
function hasClass(item, cls) {
  for (i in item.classList) {
    if (item.classList[i] == cls) return true;
  }
  return false;
}
function allCheckboxes() {
  return document.getElementById('filter-checkboxes').querySelectorAll('input');
}
function refreshVisiblePages() {
  var all = document.getElementById('filter-mode-all').checked;
  document.getElementById('list-of-extensions').querySelectorAll('li').forEach(function(item) {
    var enabled = all;
    allCheckboxes().forEach(function(box) {
      var catClass = box.id.replace('toggle', 'category');
      if (hasClass(item, catClass)) {
        if (!all && box.checked) enabled = true;
        if (all && !box.checked) enabled = false;
      }
    });
    item.style.display = enabled ? 'block' : 'none';
  });
}
function toggleAllCategories(checked) {
  allCheckboxes().forEach(function(box) { box.checked = checked });
  refreshVisiblePages();
}
</script>
<style>
#list-of-extensions {
  column-width: 15em;
}
#list-of-extensions img {
  vertical-align: middle;
}
#list-of-extensions li {
  padding-bottom: 1em;
  align-items: center;
  line-height: 0.9em;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
#list-of-extensions li div {
  display: inline-block;
  vertical-align: middle;
  padding-left: 0.3em;
}
#list-of-extensions .categories {
  font-size: 0.7em;
  white-space: normal;
}
</style>
<details id="categories-filter" class="shadowed-box">
  <summary><b>Categories filter</b></summary>
  <div id='filter-container'>
    <div id='filter-buttons'>
      <button onclick="toggleAllCategories(true)">Select all</button>
      <button onclick="toggleAllCategories(false)">Select none</button>
      <input type="radio" id="filter-mode-all" name="mode" value="all" onchange="refreshVisiblePages()">
      <label for="filter-mode-all">All</label>
      <input type="radio" id="filter-mode-any" name="mode" value="any" checked onchange="refreshVisiblePages()">
      <label for="filter-mode-any">Any</label>
    </div>
    <div id='filter-checkboxes' style="column-width: 10em">
    {%- for category in all-categories -%}
      {%- if category == "" -%} {%- continue -%} {%- endif %}
      <input type="checkbox" id="toggle-{{category}}" name="{{category}}" checked onchange="refreshVisiblePages()">
      <label for="toggle-{{category}}">{{category}}</label><br>
    {%- endfor %}
    </div>
  </div>
</details>

<ul id="list-of-extensions">
{%- for p in site.pages -%}
  {%- assign tokens = p.url | split: "/" -%}
  {%- if tokens[1] != 'plugins' and tokens[1] != 'formats' -%} {%- continue -%} {%- endif -%}
  {%- if tokens[3] and tokens[3] != 'index' -%} {%- continue -%} {%- endif -%}
  {%- assign classes = "" -%}
  {%- for cat in p.categories -%}
    {%- assign c = cat | strip -%}
    {%- unless forloop.first -%} {%- assign classes = classes | append: ' ' -%} {%- endunless -%}
    {%- assign classes = classes | append: 'category-' | append: c -%}
  {%- endfor %}
  <li class="{{classes}}">
    <img src="{{p.icon}}" height=25>
    <div>
      <a href="{{p.url}}">{{p.title}}</a><br>
      <span class="categories">{{ p.categories | join: ', ' }}</span>
    </div>
  </li>
{%- endfor %}
</ul>

{%- comment -%}
# vi:syntax=liquid
{%- endcomment -%}
