---
title: 2011-11-17 - SFTP support for update sites
---

Thanks to [Jarek Sacha](http://ij-plugins.sourceforge.net/), our [Fiji Updater](/plugins/updater) now has support for SFTP in addition to SSH. Many sites do not allow for direct SSH access but only for SFTP, like [SourceForge](http://sourceforge.net). Now we support such sites, too!

To enable SFTP support, just prefix *sftp:* in front of the SSH host in the [update site configuration](/update-sites/setup).


