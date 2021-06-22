---
mediawiki: How_to_set_up_and_populate_an_update_site
title: How to set up and populate an update site
section: Extend:Update Sites
project: /software/imagej2
nav-links: true
nav-title: How to Create
---

## Introduction

This tutorial explains how to **set up a website to distribute your plugins**. It assumes that your plugins are correctly installed in your local ImageJ setup.

## Rationale

See the [Distribution](/contribute/distributing) page for a discussion of the benefits of update sites and how they fit in to plugin development.

## Add your personal update site

By far the easiest method to provide your macros, scripts and plugins to other users, letting them keep up-to-date in the most convenient manner, is to set up your *personal update site*.

A *personal update site* is hosted on https://sites.imagej.net/&lt;imagej-wiki-account&gt;. If you do not have an ImageJ Wiki account yet, no need to worry, you can register one while setting up your update site.

{% include notice icon="info" content='There are some minimal *Terms of Service* for personal update sites. See the [Personal Update Site Terms of Service](/update-sites/tos) for details.' %}

First of all, create a wiki account on https://imagej.net.

Please note, that the password for the corresponding update site is NOT the one for your wiki account. In order to set your update site password, use the link at the bottom of the wiki or click [here](Special_ChangeUploadPassword).

start the updater with {% include bc path='Help | Update'%} and click on the *Manage update sites* button:

<img src="/media/mamed-3.jpg" width="770"/>

### Specifying your existing ImageJ Wiki account

Enter the name of that account and click *OK*:

<img src="/media/update-sites/personal-update-site-1.png" width="770"/>

If your upload password (separate from your wiki password) was not initialized, you will then be asked to provide your wiki password, which will be used to initialize your upload password. The two passwords can differ. This can be source of confusion during setting up of the update.

You can also manually [change or initialize your upload password](Special_ChangeUploadPassword).

### Dedicated plugin update sites

Rather than having a single update site for many plugins, it is highly advised to set up dedicated update sites for each plugin that could be of interest to the community.  
Such dedicated update site can have a more intuitive name.  
A given user/wiki account can own several update sites. To request a new update site for your user account, post your request on the forum (see [related post](https://forum.image.sc/t/distributing-several-update-sites/21219/2?u=lthomas)), or on the [ImageJ Gitter](https://gitter.im/imagej/imagej).

## Group update site

In addition to [personal update sites](/update-sites/setup#add-your-personal-update-site), it is possible for groups of people to share an update site.

To create such an update site, post on the [Image.sc Forum](https://forum.image.sc/tags/imagej), or in the [imagej Gitter channel](https://gitter.im/imagej/imagej), requesting the creation of the site on `sites.imagej.net`, including the desired name of the site, as well as the wiki usernames to be granted upload permission to the group update site. An administrator will then create the site skeleton and grant those users upload permission to the new site.

## Adding an update site on your own server

If you have an own server or web space with WebDAV, SFTP or SSH access, you can create a directory in that web space and initialize it as an update site, too. Just call the updater with {% include bc path='Help | Update'%} and click the *Manage update sites* button:

<img src="/media/mamed-3.jpg" width="770"/>

Now press the *Add* button, provide a nick name for your update site, the URL of your web space, and *upload information*.

The *upload information* depends on the protocol available for uploading:

| Protocol | Host                                 | Directory on Host |
|----------|--------------------------------------|-------------------|
| WebDAV   | *webdav:*, or *webdav:<webdav-user>* | *.*               |
| SFTP     | *sftp:<sftp-user>@<sftp-host>*       | *<absolute-path>* |
| SSH      | *ssh:<ssh-user>@<ssh-host>*          | *<absolute-path>* |
|          |                                      |                   |

In case you want to use an SFTP/SSH server, it must have an empty, public web accessible folder where you intend to publish your updates. The ImageJ updater will not create that empty folder.

{% include aside title="A note about SSH and `known_hosts`" content='For ImageJ to connect to your server over SSH, you must have configured your SSH credentials as normal—i.e.: `$HOME/.ssh/known_hosts` must contain the host key, and optionally `$HOME/.ssh/config` may contain the host configuration/credentials. We recommend that the given host be specified in `$HOME/.ssh/config` and equipped with a private key.
  
Note that you need to connect with command-line ssh first, to record the finger-print of the host. It might be necessary to call `ssh-keyscan test.imagej.net >> $HOME/.ssh/known_hosts` to ensure the correctly formatted key appears in your configuration file. There is an issue with newer SSH servers offering host keys in `ecdsa-sha2-nistp256` format, but the [JSch](http://www.jcraft.com/jsch/) library wanting them in `ssh-rsa` format instead. If you receive the error `com.jcraft.jsch.JSchException: UnknownHostKey` then you might be bitten by this discrepancy; try using the `ssh-keyscan` invocation above. If you still have trouble, please write to the [Image.sc Forum](https://forum.image.sc/) to troubleshoot further.' %}

*Example:* Let's assume you have SFTP access to a machine known as *imagej.example.org* to the internet, and let's assume that you have a user account *myself* that has write access to the path */var/www/my-update-site/* on that machine that is served via http://imagej.example.org/my-update-site/. Then the line you need to add might look like this:

| Name           | URL                                         | Host                      | Directory on Host        |
|----------------|---------------------------------------------|---------------------------|--------------------------|
| My Update Site | http://imagej.example.org/my-update-site/ | myself@imagej.example.org | /var/www/my-update-site/ |
|                |                                             |                           |                          |

If the update site has not been initialized yet (i.e. if nobody else has initialized that site yet), you will see a dialog like this:

![](/media/update-sites/how-to-setup-a-plugin-distribution-site-6a.jpg)

Just click *OK* and let the updater upload an empty file index (it is stored in the file *db.xml.gz* which is also called the *database* in the documentation of the updater).

## Uploading files to your update site

Note: you cannot simply copy files to your web space; the updater would miss all kinds of important information, and consequently refuse to accept that update site. You **need** to let the updater handle the file uploading.

### Start the [updater](/plugins/updater) and check your update site

First, start the [updater](/plugins/updater):

![](/media/update-sites/how-to-setup-a-plugin-distribution-site-1.jpg)

Click on the *Manage update sites* button and verify:

-   Your update site is present and enabled
-   The *Host* column of your update site contains your user name, in the form: `webdav:`<WikiUsername>

For example:

<img src="/media/update-sites/personal-update-site-7.png" width="770"/>

Once your login information is set you can *Close* the update site window.

### Prepare your files for upload

Click on the *Advanced mode* button and set the view options to see your plugins:

-   If your have never uploaded your plugins, select *View local-only files*

**For .ijm macro**, the files must be located in the *macro* or *scripts* folder (or any subfolder in it).

**For .py scripts**, they can be either in the *Jars/Lib* or *scripts* folder (or any subfolder).

Out of those folder, the updater might not see them.

-   If you are uploading new versions of your plugins, select *View locally modified files only*

In this case, the plugin we'll be uploading is contained in *A\_Jolly\_Useful\_Plugin.jar*.

Select the file to upload, click under the *Stats/Action* column, or right-click (on macOS, {% include key keys='Ctrl|Left Click' %}) in any column, for the context menu and select *Upload to <update site name>*.

<img src="/media/update-sites/upload-to-update-site.png" width="770"/>

{% include notice icon="info" content='The *Upload to <update site name>* option is only available if you entered your [wiki credentials](#start-the-updater-and-check-your-update-site) and no other changes are pending. Be aware that the password for the update site [*is not* your Wiki password](/update-sites/faq#how-do-i-set-a-password-for-my-personal-update-site). This is to avoid potentially corrupting your ImageJ installation. If the Upload option is not available, select the *View changes* view and resolve any pending changes - e.g. by updating or reverting to **Keep as-is**.' %}

### Modifying Dependencies

When a plugin is selected, a *Details* panel becomes available. The plugin's dependencies, e.g. *ij.jar* and *someJarOrOther.jar*, are automatically determined by the updater. Hence if you require 3rd party packages for your plugin you can place them into the jars folder of ImageJ and the updater will automatically upload them to the site.

You can also manually enter or edit any information in the *Details* panel:

<img src="/media/update-sites/how-to-setup-a-plugin-distribution-site-15.jpg" width="770"/>

{% include notice icon="info" content='The *Details* panel can only be edited if you have entered upload credentials for the appropriate update site. After modifying the *Details* panel you can mark the jar for upload, even though the jar contents itself has not changed.' %}

{% include notice icon="warning" content='Sometimes the updater will mis-detect your dependencies. This may prevent you from uploading to your update site! If a dependency is wrong, you can manually add or delete dependencies from the *Details* tab to correct the problem. Please [let us know](/discuss) when this happens so we can try to improve the updater' %}

### Upload your files

Finally, click *Apply changes (upload)* to upload your plugin to the server and allow others to access it. If you have dependencies that are not part of ImageJ, the updater will ask you if you want to upload that jar as well. Finally, you will be asked for your login credentials again and the files will be uploaded to the server.

Check that your plugins are now registered as ImageJ plugins by selecting the *View files of the '\[your site name here\]' site* view option:

<img src="/media/update-sites/updaterfinalscreen.jpg" width="770"/>

That's it - you're done. Now, anyone who wants a copy of your plugins merely needs to [add your update site](/update-sites/following) to the Update manger via the URL you specified, and your plugins will be downloaded and updated in their ImageJ installations just like the standard ImageJ plugins.  
For even more visibility and practicability, you can ask to have your update site listed in the Fiji Updater (see section below).

## Publishing your update site

If you want your update site to be listed in the ImageJ update manager, follow the instructions at this page : [list of update sites](/list-of-update-sites)
.

## Further Reading

For additional information on common topics regarding update site maintenance, please see the [update site FAQ](/update-sites/faq).


