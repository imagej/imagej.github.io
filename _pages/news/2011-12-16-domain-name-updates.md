---
mediawiki: 2011-12-16_-_Domain_name_updates
title: 2011-12-16 - Domain name updates
---

As [mentioned on the mailing list](/ij/pipermail/imagej-devel/2011-November/000544.html), we have updated our web resources to be more unified under the **imagej.net** domain name:

-   **imagejdev.org** is now **developer.imagej.net**
-   **dev.imagejdev.org** is now **code.imagej.net**
-   The toplevel **imagej.net** currently redirects to **imagej.nih.gov/ij** but will become the main portal into ImageJ topics later in 2012.

Most of the links on the site have been updated accordingly, but any old links should also redirect properly.

Those who have the code checked out from Subversion will need to run:

    svn switch --relocate http://dev.imagejdev.org/svn/imagej http://code.imagej.net/svn/imagej

Or if you have cloned the Git mirror:

    git remote set-url origin git://code.imagej.net/imagej.git

We hope the new domain is less confusing and easier to remember!

 
