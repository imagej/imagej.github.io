---
title: List of Extensions
section: Extend
---
{%- assign category-string = "" -%}
{%- for p in site.pages -%}
  {%- comment -%}
  It would be nicer to use the concat filter below, no?
  But that filter only became available in Jekyll 4.0.
  {%- endcomment -%}
  {%- for category in p.categories -%}
    {%- capture c -%} {{category | strip}} {%- endcapture -%}
    {%- assign category-string = category-string | append: "|" | append: c -%}
  {%- endfor -%}
{%- endfor -%}
{%- assign all-categories = category-string | split: "|" | sort | uniq -%}

<style>
#categories-filter {
  margin-bottom: 2em;
  margin-top: -2em;
}
#filter-checkboxes {
  column-width: 13em;
}
#list-of-extensions {
  column-width: 16em;
  list-style: none;
}
#list-of-extensions img {
  vertical-align: middle;
}
#list-of-extensions li {
  padding-bottom: 1em;
  align-items: center;
  line-height: 0.9em;
  overflow: hidden;
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
  <div id="filter-container">
    <div id="filter-buttons">
      <button onclick="toggleAllCategories(true, true)">Select all</button>
      <button onclick="toggleAllCategories(false, true)">Select none</button>
      <input type="radio" id="filter-mode-all" name="mode" value="all" onchange="refreshVisibleItems()">
      <label for="filter-mode-all">All</label>
      <input type="radio" id="filter-mode-any" name="mode" value="any" checked onchange="refreshVisibleItems()">
      <label for="filter-mode-any">Any</label>
    </div>
    <div id="filter-checkboxes">
    {%- for category in all-categories -%}
      {%- if category == "" -%} {%- continue -%} {%- endif %}
      {%- assign c = category | slugify -%}
      <input type="checkbox" id="toggle-{{c}}" name="{{category}}" checked onchange="refreshVisibleItems()">
      <label for="toggle-{{c}}">{{category}}</label><br>
    {%- endfor %}
    </div>
  </div>
</details>

<ul id="list-of-extensions">
{%- for p in site.pages -%}
  {%- comment -%} Only pages declaring categories are listed. {%- endcomment -%}
  {%- unless p.categories.size > 0 -%} {%- continue -%} {%- endunless -%}
  {%- assign classes = "" -%}
  {%- for category in p.categories -%}
    {%- assign c = category | slugify -%}
    {%- unless forloop.first -%} {%- assign classes = classes | append: ' ' -%} {%- endunless -%}
    {%- assign classes = classes | append: 'category-' | append: c -%}
  {%- endfor %}
  <li class="{{classes}}">
    <img src="{{p.icon}}" height=25>
    <div>
      <a href="{{p.url | replace: '/index', ''}}">{{p.title}}</a><br>
      <span class="categories">{{ p.categories | join: ', ' }}</span>
    </div>
  </li>
{%- endfor %}
</ul>

<script>
function allCheckboxes() {
  return document.getElementById('filter-checkboxes').querySelectorAll('input');
}

function hasClass(item, cls) {
  for (var i=0; i<item.classList.length; i++) {
    if (cls == item.classList[i]) return true;
  }
  return false;
}

function refreshVisibleItems() {
  var allMode = document.getElementById('filter-mode-all').checked;

  // Populate a hashset with the enabled categories.
  var catset = [];
  allCheckboxes().forEach(function(box) {
    if (box.checked) catset[box.id.replace('toggle-', 'category-')] = 1;
  });
  console.log('catset:');
  console.log(catset);
  for (var cat in catset) {
    console.log(`- ${cat}`);
  }
  console.log("and that's it");

  document.getElementById('list-of-extensions').querySelectorAll('li').forEach(function(item) {
    var enabled;
    if (allMode) {
      // Discern whether the item includes all checked categories.
      enabled = true;
      for (var cat in catset) {
        if (!hasClass(item, cat)) { enabled = false; break; }
      }
    }
    else {
      // Discern whether the item includes any checked category.
      enabled = false;
      for (var i=0; i<item.classList.length; i++) {
        if (item.classList[i] in catset) { enabled = true; break; }
      }
    }
    item.style.display = enabled ? 'block' : 'none';
  });
}

function toggleAllCategories(checked, refresh) {
  allCheckboxes().forEach(function(box) { box.checked = checked });
  if (refresh) refreshVisibleItems();
}

/* Credit: https://css-tricks.com/snippets/javascript/get-url-variables/ */
function getQueryVariable(variable) {
  var query = window.location.search.substring(1);
  var vars = query.split("&");
  for (var i=0; i<vars.length; i++) {
    var pair = vars[i].split("=");
    if (pair[0] == variable) return pair[1];
  }
  return false;
}

var mode = getQueryVariable("mode");
var category = getQueryVariable("category");
var categories = getQueryVariable("categories");
if (mode || category || categories) {
  if (mode == "all") document.getElementById('filter-mode-all').checked = true;
  toggleAllCategories(false, false);
  if (category) {
    var box = document.getElementById(`toggle-${category}`);
    if (box) box.checked = true;
  }
  if (categories) {
    var category_array = categories.split(',');
    for (var i=0; i<category_array.length; i++) {
      var cat = category_array[i];
      var box = document.getElementById(`toggle-${cat}`);
      if (box) box.checked = true;
    }
  }
  refreshVisibleItems();
}
</script>

{%- comment -%}
# vi:syntax=liquid
{%- endcomment -%}
