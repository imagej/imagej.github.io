---
title: 2016-05-10 - ImageJ HOWTO - Java 8, Java 6, Java 3D
---

[ImageJ2](/software/imagej2) (and hence also [Fiji](/software/fiji)) is currently in the midst of a [transition to Java 8](/news/2015-12-22-the-road-to-java-8).

However, at the moment, it is still possible to run a (slightly outdated now) version of [Fiji](/software/fiji) with Java 6.

## Current recommendations and possibilities

{::nomarkdown}
<table>
<tr>
  <th><a href="/software/imagej#flavors">Flavor</a></th>
  <th style="text-align: center">Java<br>version</th>
  <th>Platforms</th>
  <th style="width: 30%">Installation</th>
  <th style="width: 30%">Updates</th>
  <th style="width: 30%"><a href="/libs/java-3d" title="Java 3D">Java 3D</a></th>
</tr>
<tr>
  <td rowspan="3"><a href="/software/fiji" title="/software/fiji"><img alt="/software/fiji" src="/media/icons/fiji.png" width="64" height="64" /></a></td>
  <td>Java 8</td>
  <td style="white-space: nowrap">
  <p><a href="/media/icons/windows.svg"><img alt="/platforms/windows" src="/media/icons/windows.svg" width="32" height="32" /></a>
  <br><a href="/media/icons/macos.png"><img alt="macOS" src="/media/icons/macos.png" width="26" height="32" /></a>
  <br><a href="/media/icons/linux.svg"><img alt="/platforms/linux" src="/media/icons/linux.svg" width="32" height="32" /></a>
  </p>
  </td>
  <td><b>Recommended.</b>
  <p><a href="/software/fiji/downloads" title="Fiji Downloads">Download the newest Fiji</a> for your platform. It comes bundled with Java 8, with the Java-8 update site enabled.
  </p>
  </td>
  <td>Run <a href="/plugins/updater" title="/plugins/updater"><span><em><span style="border-bottom:1px dotted #ccc;">Help</span>&#160;&#8250; <span style="border-bottom:1px dotted #ccc;">Update...</span></em></span></a> to update to the latest version of ImageJ core and Fiji components.
  </td>
  <td>This version of Fiji comes bundled with <a href="/libs/java-3d" title="Java 3D">Java 3D</a> 1.6. The <a href="/plugins/3d-viewer" title="3D Viewer">3D Viewer</a> works out of the box, though there are <a href="https://github.com/search?q=label%3Ajava-3d+is%3Aopen+user%3Afiji+user%3Aimagej&amp;type=Issues">still some bugs</a>.
  </td>
</tr>
<tr>
  <td rowspan="2">Java 6</td>
  <td style="white-space: nowrap">
  <p><a href="/media/icons/windows.svg"><img alt="/platforms/windows" src="/media/icons/windows.svg" width="32" height="32" /></a>
  <br><a href="/media/icons/linux.svg"><img alt="/platforms/linux" src="/media/icons/linux.svg" width="32" height="32" /></a>
  </p>
  </td>
  <td>Download the final (2017-May-30) <a href="/software/fiji/downloads#java-6" title="Fiji Downloads">Java-6 version of Fiji</a>. It comes bundled with Java 6 and all platform launchers.
  </td>
  <td rowspan="2">Run <a href="/plugins/updater" title="/plugins/updater"><span><em><span style="border-bottom:1px dotted #ccc;">Help</span>&#160;&#8250; <span style="border-bottom:1px dotted #ccc;">Update...</span></em></span></a> to update to the latest Java-6-compatible version. Your Fiji will become outdated over time, stuck on the final Java-6-compatible plugin versions.
  </td>
  <td rowspan="2">Run <a href="/plugins/3d-viewer" title="3D Viewer"><span><em><span style="border-bottom:1px dotted #ccc;">Plugins</span>&#160;&#8250; <span style="border-bottom:1px dotted #ccc;">3D Viewer</span></em></span></a> to trigger installation of <a href="/libs/java-3d" title="Java 3D">Java 3D</a> 1.5 if you need 3D viz.
  </td>
</tr>
<tr>
  <td><a href="/media/icons/macos.png"><img alt="macOS" src="/media/icons/macos.png" width="26" height="32" /></a>
  </td>
  <td>Download the final (2017-May-30) <a href="/software/fiji/downloads#java-6" title="Fiji Downloads">Java-6 version of Fiji</a>. It is distributed <i>without</i> Java, so you must <a href="/learn/faq#how-do-i-set-up-java-6-on-macos" title="Frequently Asked Questions">install Apple Java 6</a> on your system.
  <ul>
  <li>If you have Java 7 and/or Java 8 installed, uninstall them—or else ImageJ will not use your Java 6 installation.</li>
  <li>Afterwards, <a href="/learn/troubleshooting#checking-the-java-version" title="/learn/troubleshooting">verify that Fiji is using Java 6</a>.</li>
  </ul>
  </td>
</tr>
<tr><td colspan="6"></td></tr>
<tr>
  <td rowspan="2"><a href="/software/imagej2" title="/software/imagej2"><img alt="/software/imagej2" src="/media/icons/imagej.png" width="64" height="64" /></a></td>
  <td>Java 8</td>
  <td style="white-space: nowrap">
  <p><a href="/media/icons/windows.svg"><img alt="/platforms/windows" src="/media/icons/windows.svg" width="32" height="32" /></a>
  <br><a href="/media/icons/macos.png"><img alt="macOS" src="/media/icons/macos.png" width="26" height="32" /></a>
  <br><a href="/media/icons/linux.svg"><img alt="/platforms/linux" src="/media/icons/linux.svg" width="32" height="32" /></a>
  </p>
  </td>
  <td>
  <p>
  <a href="/downloads" title="/downloads">Download the newest ImageJ</a> for your platform. It comes bundled <i>without</i> Java, and <i>without</i> the Java-8 update site enabled.
  </p>
  <ul><li>If you have not already done so: install Java 8 from <a href="http://java.com/">java.com</a>.</li>
  <li>Do <b>not</b> enable the Java-8 update site, because (at the moment) it contains a mixture of core ImageJ and Fiji components.</li></ul>
  </td>
  <td rowspan="2">Run <a href="/plugins/updater" title="/plugins/updater"><span><em><span style="border-bottom:1px dotted #ccc;">Help</span>&#160;&#8250; <span style="border-bottom:1px dotted #ccc;">Update...</span></em></span></a> to update to the latest <b>Java-6-compatible</b> version. Your ImageJ will become outdated over time, stuck on the final Java-6-compatible plugin versions.</td>
  <td rowspan="2">The <a href="/plugins/3d-viewer" title="3D Viewer">3D Viewer</a> is not bundled with "plain" ImageJ2 (yet). It is (for now) part of the Fiji update site.
  </td>
</tr>
<tr>
  <td rowspan="2">Java 6</td>
  <td style="white-space: nowrap">
  <p>
  <a href="/media/icons/windows.svg"><img alt="/platforms/windows" src="/media/icons/windows.svg" width="32" height="32" /></a>
  <br><a href="/media/icons/macos.png"><img alt="macOS" src="/media/icons/macos.png" width="26" height="32" /></a>
  <br><a href="/media/icons/linux.svg"><img alt="/platforms/linux" src="/media/icons/linux.svg" width="32" height="32" /></a>
  </p>
  </td>
  <td>It is possible to set up a "plain" ImageJ2 with Java 6, but <b>not recommended</b>:
  <ul>
  <li>Set up <a href="/software/fiji">Fiji</a> + Java 6 as described above.</li>
  <li>Disable the Fiji update site.</li>
  <li>Restart ImageJ.</li>
  <li>Delete all Fiji-specific files using the updater's Advanced mode, View "Local only files" and deleting them all.</li>
  </ul>
  </td>
</tr>
<tr><td colspan="6"></td></tr>
<tr>
<td><a href="/software/imagej1" title="/software/imagej1"><img alt="/software/imagej1" src="/media/icons/imagej1.png" width="64" height="64" /></a>
</td>
<td colspan="5">See the <a href="download.html">ImageJ 1.x downloads page</a> for instructions.
</td></tr></table>
{:/}

## Upgrading an old installation

If you have downloaded Fiji or ImageJ2 quite some time ago (before 2016), you probably have the Java 6 version ([how do I find out?](/learn/troubleshooting#checking-the-java-version)). So when you update, you will not receive the latest plugin releases anymore, as described above.

-   If you **still need Java 6, do nothing.**
    -   For now, you will keep receiving updates of [ImageJ 1.x](/software/imagej1).
    -   But you will no longer receive updates for most ImageJ2 or Fiji components—they have all migrated to Java 8.
-   If you **want the latest updates**, [update your ImageJ installation to use Java 8](/learn/faq#how-do-i-launch-imagej-with-a-different-version-of-java) and then [enable the Java-8 update site](/update-sites/following).
    -   **Make sure you switch your ImageJ over to Java 8 *before* enabling the Java-8 update site!**

{% include notice icon="warning" content='If you enable the Java-8 update site while still running Java 6, your installation will become non-functional!' %}

Alternately, you can simply download a new Fiji as described above.

## About the Java-8 update site

Right now, the `Java-8` update site includes the latest Java-8 versions of all core ImageJ **and** Fiji components. So unfortunately, at the moment, there is no way to get a "latest and greatest plain ImageJ2" built on Java 8, but without Fiji components.

But later this year, we will migrate the latest Java-8 components back to the core `ImageJ` and `Fiji` update sites, respectively, so that users can choose between "plain" ImageJ2 (lighter weight without "plugin bloat") and Fiji (with "more parts on the table"). We only want to proceed with this migration once there is a mechanism in place to notify users that Java 8 is now required, without breaking existing installations.

## About Java 3D

-   [Java 3D](/libs/java-3d) 1.6 requires Java 7 or newer. Hence, we ship it **on the Java-8 update site only**.
-   [Java 3D](/libs/java-3d) 1.5 works with Java 6, but:
    -   It has a restrictive license.
    -   It does not work with Java 7 or 8 on macOS.
    -   It does not work with Java 8 (or 7?) on some Windows systems.

Please be aware that [Java 3D](/libs/java-3d) is essentially a dead technology. The future of 3D visualization in ImageJ is the [ClearVolume](/plugins/clearvolume) and [SciView](/plugins/sciview) plugins. But it will be a lot of work to rewrite all [3D Viewer](/plugins/3d-viewer) functionality, so the ImageJ and Fiji teams are still exploring the best ways to proceed here.
