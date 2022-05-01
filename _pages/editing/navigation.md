---
title: Navigation
section: Contribute:Editing the Wiki
nav-links: true
---

This page explains the mechanisms for linking navigation between pages.

## nav-links

![nav-links](/media/editing/nav-links.png){:width="600px"}

`nav-links` provide a navigation bar at the top of your page. This is a nice way to tie together several related pages, without affecting the site-wide side menu.

`nav-links` are enabled in the front matter of a page. Simply turning them on with a `true` value will automatically link to all pages in the same directory:

```
---
title: Navigation
nav-links: true
---
```

By default, pages will appear in the navigation section using their `title`. If desired, this can be overridden using the `nav-title` front matter:

```
---
title: Navigation
nav-links: true
nav-title: Navigating the Site
---
```

For more control over the links, you can also manually specify a list of pages to link to, and the title to give each page:

```
---
nav-links:
- title: Overview
  url: /develop/index
- title: Philosophy
  url: /develop/philosophy
- title: Source code
  url: /develop/source
---
```



## Menu

{% include notice icon="warning" content="Changes to the navigation menu affect all pages. Items should be reserved for general topics." %}

![menu](/media/editing/menu.png){:width="200px"}

The navigation menu allows hierarchical organization of wiki topics. Items are added to the menu by editing [the `menu` include](https://github.com/imagej/imagej.github.io/blob/main/_includes/layout/menu) and creating a new `<li>` element as appropriate:

{% highlight html %}
            {% raw %}{% include menu/section title="Editing the Wiki" link="/editing" %}{% endraw %}
              <li><a href="/editing/advanced">Advanced Editing</a></li>
              <li><a href="/editing/buttons">Buttons</a></li>
              <li><a href="/editing/citations">Citations</a></li>
              <li><a href="/editing/code">Source Code</a></li>
              <li><a href="/editing/debugging">Debugging</a></li
{% endhighlight %}

In the linked page itself, we add a `section` entry in the front matter to indicate what section of the menu should be opened by default when navigating to that page. Note that the sections only need to be specified to the containing section: for example, in this page:

```
---
title: Navigation
section: Contribute:Editing the Wiki
---
```
