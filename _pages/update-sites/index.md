---
mediawiki: Update_Sites
title: Update Sites
section: Extend:Update Sites
project: /software/imagej2
nav-links: true
nav-title: Overview
---

An **update site** is web space used by the [Updater](/plugins/updater) which enables users to share their macros, scripts and plugins with other researchers. With update sites, you do not need to manually download and install anything; [ImageJ2](/software/imagej2) takes care of it for you.

## Available update sites

{% include notice icon='info' size='large' content='You can browse the [list of available update sites](/list-of-update-sites).' %}

## Following an update site

<div style="clear: right; float: right">

{% include notice icon="fiji" content='The [Fiji](/software/fiji) distribution of ImageJ2 ships with both the `ImageJ` and `Fiji` sites enabled. You can transform your ImageJ2 installation into a Fiji one simply by enabling the `Fiji` update site.' %}

</div>

Out of the box, ImageJ2 has only the core *ImageJ* update site enabled. To enable additional features, choose {% include bc path='Help|Update...'%}, then click the "Manage update sites" button.

For further details, see [Following an update site](/update-sites/following).

## Check if an update site is activated

In Fiji, if you write macros and plugins that rely on some functionalities provided by a specific update site (dependencies), you can use the following command to check if the update site is activated, and print a message if not.  
This uses the update site service.  
Example in Jython.

```python
#@ UpdateService updateService

if not updateService.getUpdateSite("Fiji-Legacy").isActive():
    print "Please activate the Fiji-legacy update site"
```

## Creating your own update site

Anyone can share their extensions ([plugins](/plugins), [scripts](/scripting), etc.) by [creating their own update site](/update-sites/setup). You can use ImageJ2's [personal update site](/update-sites/setup#add-your-personal-update-site) service (hosted on the [ImageJ2 web server](http://sites.imagej.net/)), or host it on your own server.

## Frequently asked questions

See the [Update site FAQ](/update-sites/faq).
