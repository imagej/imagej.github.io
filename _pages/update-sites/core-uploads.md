---
mediawiki: How_to_upload_to_core_update_sites
title: How to upload to core update sites
section: Extend:Update Sites
project: /software/imagej2
nav-links: true
nav-title: Core Sites
---

## Introduction

This tutorial explains how to upload changes to core [ImageJ2](/software/imagej2) and [Fiji](/software/fiji) libraries.

The typical workflow is:

1.  Update {% include github org='fiji' repo='fiji' label='Fiji.git' %} to depend on the latest {% include github org='scijava' repo='pom-scijava' label='pom-scijava' %}
2.  Use `mvn -Dimagej.app.directory=$HOME/Desktop/Fiji.app/ -Ddelete.other.versions=true` to install into an existing (up-to-date) Fiji installation
3.  NOTE: if there are any version downgrades at this point, this indicates dependency skew. Fiji.git should be updated appropriately, restarting from step 1
4.  Upload changes to ImageJ update site
5.  Upload changes to Fiji update site

{% include notice icon="warning" content='There is a known issue where `bio-formats_plugins.jar` is placed in `/jars/bio-formats` by this maven job. It should be manually moved to `/plugins/`' %}

## Responsibility of uploaders

To facilitate [reproducibility](/develop/architecture#reproducible-builds) and present a unified application to both users and developers, uploaders should strive to keep each core update site synchronized with its corresponding source code.

Because releases are tied to the source code (and the update site contents are not explicitly versioned), the order of update should always be:

1.  Source code
2.  Update site

Source repository for each core update site:

| Update Site | Source                                                              |
|-------------|---------------------------------------------------------------------|
| ImageJ      | *master* branch of [imagej2.git](https://github.com/imagej/imagej2) |
| Fiji        | *master* branch of [fiji.git](https://github.com/fiji/fiji)         |

## Getting started

First of all, start the [updater](/plugins/updater) with {% include bc path='Help | Update' %} and click on {% include button label="Manage update sites" %}:

<img src="/media/mamed-3.jpg" width="770"/>

From this dialog, you can edit the desired update site(s) to add your authentication information.

## Configuring Fiji update site

The Fiji update site uses {% include wikipedia title='WebDAV' text='webDAV' %} authentication. To upload something, you will need to:

-   Ask an administrator to create a WebDAV account for you, and grant permission for uploading to update.fiji.sc.

In the *Manage update sites* dialog, on the Fiji update site line, add the following information:

-   Host = **webdav:YourWebDAVLogin**
-   Directory on host = **./**

Note that your username will always start with an upper case letter. It should look like this:

<img src="/media/update-sites/update-site-fiji-creds.png" width="770"/>

You can now close the *Manage update sites* window and go on to [ Uploading your resources](#uploading-your-resources).

## Configuring the ImageJ update site

The ImageJ update site uses {% include wikipedia title='Secure Shell' text='ssh' %} authentication. You will need a login with [the imageJ update site](http://update.imagej.net) that some administrator will have to add to the *ij-update* group.

In the *Manage update sites* dialog, on the ImageJ update site line, add the following information:

-   Host = `yourImageJLogin@update.imagej.net`
-   Directory on host = `/home/imagej/update-site/`

It should look like this:

<img src="/media/update-sites/update-site-ij2-creds.png" width="770"/>

You can now close the *Manage update sites* window and go on to [Uploading your resources](#uploading-your-resources).

## Uploading your resources

See the [Uploading files to your update site](/update-sites/setup#uploading-files-to-your-update-site) section of the set up and populate tutorial.
