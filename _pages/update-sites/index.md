---
mediawiki: Update_Sites
title: Update Sites
section: Extend:Update Sites
nav-links: true
nav-title: Overview
---

An **update site** is web space used by the [Updater](/plugins/updater) which enables users to share their macros, scripts and plugins with other researchers. With update sites, you do not need to manually download and install anything; [ImageJ](/software/imagej) takes care of it for you.

## Following an update site

<div style="clear: right; float: right">

{% include notice icon="fiji" content='The [Fiji](/software/fiji) distribution of ImageJ ships with both the `/about` and `/fiji` sites enabled. You can transform your ImageJ installation into a Fiji one simply by enabling the `/fiji` update site.' %}

</div>

Out of the box, ImageJ has only the core *ImageJ* update site enabled. To enable additional features, choose {% include bc path='Help|Update...'%}, then click the "Manage update sites" button.

For further details, see [How to follow a 3rd party update site](/update-sites/following).

## Check if an update site is activated

In Fiji, if you write macros and plugins that rely on some functionalities provided by a specific update site (dependencies), you can use the following command to check if the update site is activated, and print a message if not.  
This uses the update site service.  
Example in Jython.

    #@ UpdateService updateService

    if not updateService.getUpdateSite("Fiji-Legacy").isActive():
        print "Please activate the Fiji-legacy update site"

## Creating your own update site

Anyone can share their extensions ([plugins](/plugins), [scripts](/scripting), etc.) by [creating their own update site](/update-sites/setup). You can use ImageJ's [personal update site](/update-sites/setup#add-your-personal-update-site) service (hosted on the [ImageJ web server](http://sites.imagej.net/)), or host it on your own server.

## Frequently asked questions

See the [Update site FAQ](/update-sites/faq).
