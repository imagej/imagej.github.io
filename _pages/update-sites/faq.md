---
mediawiki: Update_site_FAQ
title: Update site FAQ
description: This pages answers frequently asked questions about update sites.
section: Extend:Update Sites
project: /software/imagej2
nav-links: true
nav-title: FAQ
---

## How do I make my update site appear in ImageJ's *Manage update sites* dialog?

The dialog is based on the [list of update sites](/list-of-update-sites)
 wiki page. You can edit that page to add your own update site.

## How do I remove a file from my update site?

An update site is a {% include wikipedia title='Revision control' text='revision control'%} system where nothing is ever really deleted from the history.

Hence, there are two levels of removal:

-   marking a file **Obsolete** effectively deletes it from the update site, but preserves the file's history. This is the most common method of removing a file from an update site.
-   **Deleting a file completely from the history** is sometimes necessary e.g., for legal or privacy reasons.

The practical effects in both cases are the same: the file in question is no longer served by the update site.

### Marking a file obsolete

You can mark any file previously uploaded as obsolete. The steps vary slightly depending on if this file is hosted on another update site (**shadowing**) or not.

#### Unshadow a file

The process of marking the file obsolete will automatically revert it to the shadowed update site's version:

1.  Start the [updater](/plugins/updater) and click the *Advanced mode* button.
2.  Select the *View files of the '\[your site name here\]*' option.
3.  Right click and choose "**Mark obsolete (unshadowing)**" for the file.
4.  Click "**Apply changes (upload)**" to finalize the unshadowing.

#### Delete a file

If the file is not hosted by any other active update site you need to tell the updater to delete the file:

1.  Delete the file locally
2.  Start the [updater](/plugins/updater) and click the *Advanced mode* button.
3.  Select the *View files of the '\[your site name here\]*' option.
4.  The updater will see the file is missing and automatically flag it "**Install it**". You need to right-click the file and change it to "**Keep as-is**". See [Why don't I have an upload option?](#why-don't_I_have_an_upload_option?) below for an explanation.
5.  Right-click the deleted file again and choose "**Mark obsolete**".
6.  Click "**Apply changes (upload)**" to finalize the deletion.

### Deleting a file completely from the history

Deleting a file from the history is strongly not recommended, but if you *must* do so (e.g., for legal or privacy reasons):

-   If you using a [hosted update site](/update-sites/setup#creating-a-hosted-update-site), then [contact an administrator](/discuss) to have the offending file(s) removed.
-   If you are hosting your own update site, then you must delete all versions of the file from the file system, *and* edit the `db.xml.gz` file to remove the `<plugin>` entry as well as any `<dependency>` elements in other entries which reference it.

## What are the Terms of Service for hosted update sites?

Please see the [Hosted Update Site Terms of Service](/update-sites/tos) page.

## How do I set a password for my hosted update site?

Please see the instructions on the [Hosted Update Sites](/update-sites/setup#creating-a-hosted-update-site) page.

If you want to restrict which users can *access* your update site, please note that the [Hosted Update Sites](/update-sites/setup#creating-a-hosted-update-site) service is only intended for freely available plugins. To restrict user access, you will need to host the update site yourself, sharing the URL only with your customers. Implementing an authentication scheme on top of an ImageJ update site is outside the scope of ImageJ—consider using something like [OAuth](http://oauth.net/).

## How do I delete my hosted update site?

If you want to completely remove your update site, [contact an administrator](/discuss) to have the site removed.

## Can I manipulate the files on my update site directly? (E.g., via WebDAV?)

Please don't! Update sites are intended to be accessed *only* via ImageJ2's [Updater](/plugins/updater). There is important metadata in the `db.xml.gz` file which *must* be kept in sync with the files in the directory structure. Otherwise, your update site will stop working properly.

## Why don't I have an upload option?

When working with the updater, it's important to understand that there are two types of operations: upload and download. To avoid corrupting local or remote plugin databases, the two classes of operation are mutually exclusive—if actions of one type are scheduled, actions of the other type will not be available. For most users, the updater only performs download operations and this is not an issue. However, when managing an update site, there can be scenarios of conflict between these operations.

A typical sequence of events:

-   You start the updater
-   The updater sees new remote updates and marks them for installation/update.
-   Or, the updater sees you deleted a file (i.e. one you are about to mark obsolete) and flags it for installation—since it's still tracked by the remote update site.
-   You try to mark your file to upload it, but the Upload to server/Obsolete options are not available.

To continue with your upload, you have to resolve the pending downloads in one of two ways:

-   If there are legitimate pending updates, perform the download/installation and restart ImageJ.
-   If you deleted files locally to make them obsolete, mark the files "Keep as-is".

The *View changes* option is helpful to identify what downloads are pending. Once all of these are at a neutral state—with everything up-to-date or keep as-is—you can start flagging your files for upload as intended.

Other options to check if still not resolved:

-   Be sure that under "Manage update sites" that your credentials are inserted for your update site. See [Uploading files to your update site](/update-sites/setup#uploading-files-to-your-update-site) on the ImageJ wiki to double-check how to do this.
