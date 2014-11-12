A first working version of the [[Updater]] was integrated into the [[ImageJ2]] code base. This is an important step: the Updater can connect not only to the primary ImageJ2 update site, but to any number of update sites a user might configure. Likewise, advanced users may wish to set up their own update sites, which only requires a web site with either direct file access, or SSH/SFTP access (SFTP support was contributed by Jarek Sacha).

The Updater is a heavily adapted [[Fiji]] Updater and works in conjunction with the ImageJ [[Launcher]] which we still have to integrate into the ImageJ2 code base from {{GitHub|repo=fiji|label=fiji.git}}.

The reason the Launcher is required is because no Java Runtime Environment handles overwrites of .jar files gracefully when classes from the .jar files are still in use. (Probably this is a tribute to Windows, older version of which had a very small number of file handles available.) As an example: the ImageJ1 updater&mdash;which overwrites ij.jar &quot;in flight&quot;&mdash;consistently crashes ImageJ1 in this developer's setup. The Updater/Launcher combo works around this as following: the Updater stores the files-to-be-updated in &lt;IJDIR&gt;/update/ and the Launcher picks them up and overwrites the respective files before Java is actually started.

As a consequence of integrating the Updater, proper regression tests have been written to guarantee that the functionality of the Updater is not broken by future changes. Our trusty [[Jenkins]] will make sure that these regression tests run very soon after new changes were published in the source code repository, so that regressions will be caught pretty quickly&mdash;way before any user might experience the issues. Indeed, a number of issues which would have come up in conjunction with multiple update sites have been fixed due to the improved regression tests.

A few minor things need to be done still: regression tests need to be added for cross-update-site issues and native dependencies, and we need to come up with a proper upgrade path from the Fiji Updater so that our long-term plan comes true to make Fiji a first-class update site of ImageJ2 and to move all Fiji components which are not directly related to life sciences into ImageJ2.

In related news, the Updater was enhanced such that it could&mdash;in theory&mdash;handle an update site for projects which are only loosely related to Fiji/ImageJ2, such as [[OMERO]].

[[Category:News]]
[[Category:ImageJ2]]
