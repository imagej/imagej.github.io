---
title: Following an update site
section: Extend:Update Sites
project: /software/imagej2
nav-links: true
nav-title: How to Use
---

{% include notice icon="warning" content="Update sites are a fantastic way to
get new functionality in your ImageJ app. Unfortunately, they are also one of
the easiest ways to break an installation, by adding an update site that
clashes with another update site, or even the ImageJ core. So, before enabling
a new update site, it's safest to
[back up your installation](/plugins/make-fiji-package)." %}

## Introduction

This tutorial will explain how to **add an update site to your install of ImageJ** such that the plugins maintained there will be installed and updated just like core ImageJ plugins.

## Start the [Updater](/plugins/updater)

First, start the [updater](/plugins/updater):

{% include img src="how-to-setup-a-plugin-distribution-site-1" %}

## Add update sites

Click on the *Manage update sites* button to bring up the site management dialog:

{% include img src="mamed-3" %}

If the update site you want to follow is listed, just click the checkbox next to its name. If it is not listed, you can add Click the *Add update site* button and fill in the name of your choice for the site and the URL, which would be provided by the plugin's author or distributor.

{% include notice icon="note" content="The list of update sites shown by default is generated from a special page, which you can [view and edit here](/list-of-update-sites). Update site maintainers are encouraged to add their update site to this list, as it both helps the community and the developers." %}

After you have selected your desired update site(s), close the dialog. The list of plugins that will be installed or updated from the chosen sites will now show up:

{% include img src="addpluginsite-5" %}

{% include notice icon="warning" content="If an entry's action is **Update It**, that means it is changing an existing plugin. This action is dangerous and can break other plugins, or ImageJ itself.  
Ideally the maintainers of these sites would work with the core ImageJ maintainers to centralize important plugins.  
When you find plugin conflicts between update sites, you can greatly help the community by [starting a discussion](/discuss) with the maintainers!" %}

## Choose and download plugins

You can select whether you want to install a particular plugin by clicking in the **Status/Action** column and changing the option - for example, select **Keep as-is** to avoid installing a clashing plugin.

{% include img src="addpluginsite-6" %}

Once you are happy with what will be installed, click on the *Apply Changes* button to download your updates.

## Verify install

{% include notice icon="warning" content='An update is not finalized until **restarting the application.** After initiating an update, **do not modify your ImageJ installation manually** until after restarting at least once.' %}

Restart ImageJ as instructed to finish the install. Check to see that the plugin was installed:

{% include img src="addpluginsite-7" %}

...and that it works:

{% include img src="addpluginsite-8" %}

...and that's all there is to it.


