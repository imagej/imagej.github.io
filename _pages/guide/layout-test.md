---
mediawiki: User_Guide_Layout_Test
title: User Guide Layout Test
---

This page should be used internally to discuss the new IJ user guide layout. Once polished, it should serve to orient on when converting old user guide sections or preparing new sections to end up with a uniform layout.

The syntax is always shown in the gray boxes and the actual look you will see directly below each syntax specification.

If you want to add other templates, here you can find the existing ones [here](https://github.com/imagej/imagej.github.io/tree/main/_includes).

## Different headline levels

    == 1 Main Menu Items ==     
    === 1.1 Submenus/Direct commands ===
    ==== 1.1.1 Sub-submenu ====
    ===== 1.1.1.1 Sub-submenu =====

## 1 Main Menu Items

### 1.1 Submenus/Direct commands

#### 1.1.1 Sub-submenu

##### 1.1.1.1 Sub-sub-submenu (if needed)



## Plugin parameters

Plugin parameters such as number fields, text fields, checkboxes, or radio buttons will be shown **bold**

dropdown choices will be indeícated ***bold/italic***

## TODO / Task list

The `guide/task` include enables to make a tasklist with up to 10 entries. This could either be appended to the bottom of each article, or to article's discussion page. We could use the Todo

{% capture  content %}
add link to wiki page|add info on shortcut {% include key keys='Shift|F' %}|mention alternative plugins
{% endcapture %}
{% include guide/task content=content %}


{% capture  content %}
add link to wiki page\|add info on usage of {% include key keys='Shift|F' %}\|mention alternative plugins
{% endcapture %}
{% include guide/task content=content %}
