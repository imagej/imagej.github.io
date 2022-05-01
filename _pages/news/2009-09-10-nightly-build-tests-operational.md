---
title: 2009-09-10 - Nightly build tests operational
---

Long time ago, Mark Longair suggested to have nightly builds of the complete sources in [fiji.git](https://fiji.sc/cgi-bin/gitweb.cgi?p=fiji.git). Finally we have it up and running.

For those who are interested in some trivia:

-   The nightly build runs every night at 3:14am.
-   If the build fails (and only then), a mail is sent to [the fiji-devel mailing list](mailto:fiji-devel@googlegroups.com), with details.
-   The build will only test what is in the main development branch (*master*).
-   Only the main project is built (*fiji.git*; subprojects, such as [TrakEM2](/plugins/trakem2) are not being rebuilt).
-   To ensure compatibility with [32-bit MacOSX](/platforms/macos), we build against Java 5 (update 19, to be precise).


