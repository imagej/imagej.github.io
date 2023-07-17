---
title: Fiji Downloads
---

[Fiji](/software/fiji) is a distribution of ImageJ which includes many useful plugins [contributed by the community](/contribute/fiji).

{% include fiji/download-links %}

# System requirements

Fiji is supported on the following systems:

-   Windows XP, Vista, 7, 8, 10, 11, etc.
-   Mac OS X 10.8 "Mountain Lion" or later
-   Linux on amd64 and x86 architectures

However, Fiji (like ImageJ) should run on any system for which a Java 8 runtime is available (Solaris, Raspbian, etc.).

* MacOS Arm64 Note: The default MacOS download should run on Arm64 via the Rosetta translator (https://en.wikipedia.org/wiki/Rosetta_(software)) which may come at some performance cost.  Alternatively you can install the no-JRE version which defaults to the Mac Java and will limit some native library functionality that does not yet have Arm64 support (https://forum.image.sc/t/fiji-clij-etc-native-on-apple-silicon-arm64-m1/53627/25).

# Installation

{% include warning/avoid-program-files %}

{% include aside title="Flatpak app for Linux" content="
Support for installing Fiji via Flatpak is in the works; see
[fiji/fiji-builds#8](https://github.com/fiji/fiji-builds/pull/8)
to follow the progress." %}

Fiji is distributed as a
{% include wikipedia title='Portable application' text='portable application' %}.
That means that you do not have to run an installer; just download, unpack and
start it.

# Troubleshooting

-   Many common questions are answered on the [FAQ](/learn/faq).
-   If you encounter bugs, please see the [Getting Help](/discuss) page.

# Source code

See the [source code](/develop/source) page for details on obtaining the Fiji source code.

# Other downloads

## Archive

You can download previous Fiji builds by date stamp from the [archive](https://downloads.imagej.net/fiji/archive/).

## Life-Line Fiji versions

This sections offers older downloads of Fiji, preserved just prior to introducing major changes. The idea is that if something goes horribly wrong, you can fall back to a stable version.

### Java 8

Here are Life-Line versions of Fiji created after the switch to Java 8.

{::nomarkdown}
<table>
  <thead>
    <tr class="header">
      <th style="text-align: center">Date</th>
      <th colspan=6 style="text-align: center">Downloads</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td style="font-size: small; text-align: center; white-space: nowrap">64-bit</td>
      <td style="font-size: small; text-align: center; white-space: nowrap">32-bit</td>
      <td style="font-size: small; text-align: center; white-space: nowrap">macOS</td>
      <td style="font-size: small; text-align: center; white-space: nowrap">64-bit</td>
      <td style="font-size: small; text-align: center; white-space: nowrap">32-bit</td>
      <td style="font-size: small; text-align: center; white-space: nowrap">no-JRE</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td style="text-align: center">2017 May 30</td>
      <td style="text-align: center">
        {% include icon name='Windows' size='24px' link='https://downloads.imagej.net/fiji/Life-Line/fiji-win64-20170530.zip' %}
      </td>
      <td style="text-align: center">
        {% include icon name='Windows' size='24px' link='https://downloads.imagej.net/fiji/Life-Line/fiji-win32-20170530.zip' %}
      </td>
      <td style="text-align: center">
        {% include icon name='MacOS' size='24px' link='https://downloads.imagej.net/fiji/Life-Line/fiji-macosx-20170530.dmg' %}
      </td>
      <td style="text-align: center">
        {% include icon name='Linux' size='24px' link='https://downloads.imagej.net/fiji/Life-Line/fiji-linux64-20170530.zip' %}
      </td>
      <td style="text-align: center">
        {% include icon name='Linux' size='24px' link='https://downloads.imagej.net/fiji/Life-Line/fiji-linux32-20170530.zip' %}
      </td>
      <td style="text-align: center">
        {% include icon name='Fiji' size='24px' link='https://downloads.imagej.net/fiji/Life-Line/fiji-nojre-20170530.zip' %}
      </td>
      <td>Just prior to a sweeping update to nearly all components.</td>
    </tr>
  </tbody>
</table>
{:/}

### Java 6

Here are Life-Line versions from before Fiji switched to Java 8.

{::nomarkdown}
<table>
  <thead>
    <tr class="header">
      <th style="text-align: center">Date</th>
      <th colspan=6 style="text-align: center">Downloads</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td style="font-size: small; text-align: center; white-space: nowrap">64-bit</td>
      <td style="font-size: small; text-align: center; white-space: nowrap">32-bit</td>
      <td style="font-size: small; text-align: center; white-space: nowrap">macOS</td>
      <td style="font-size: small; text-align: center; white-space: nowrap">64-bit</td>
      <td style="font-size: small; text-align: center; white-space: nowrap">32-bit</td>
      <td style="font-size: small; text-align: center; white-space: nowrap">no-JRE</td>
      <td></td>
    </tr>
    <tr>
      <td>2017 May 30</td>
      <td colspan=6 style="text-align: center">
        {% include icon name='Fiji' size='48px' link='https://downloads.imagej.net/fiji/Life-Line/fiji-java6-20170530.zip' %}
      </td>
      <td>
        The final version of Fiji using Java 6, for all platforms.
      </td>
    </tr>
    <tr>
      <td>2015 December 22</td>
      <td style="text-align: center">
        {% include icon name='Windows' size='24px' link='https://downloads.imagej.net/fiji/Life-Line/fiji-win64-20151222.zip' %}
      </td>
      <td style="text-align: center">
        {% include icon name='Windows' size='24px' link='https://downloads.imagej.net/fiji/Life-Line/fiji-win32-20151222.zip' %}
      </td>
      <td style="text-align: center">
        {% include icon name='MacOS' size='24px' link='https://downloads.imagej.net/fiji/Life-Line/fiji-macosx-20151222.dmg' %}
      </td>
      <td style="text-align: center">
        {% include icon name='Linux' size='24px' link='https://downloads.imagej.net/fiji/Life-Line/fiji-linux64-20151222.zip' %}
      </td>
      <td style="text-align: center">
        {% include icon name='Linux' size='24px' link='https://downloads.imagej.net/fiji/Life-Line/fiji-linux32-20151222.zip' %}
      </td>
      <td style="text-align: center">
        {% include icon name='Fiji' size='24px' link='https://downloads.imagej.net/fiji/Life-Line/fiji-nojre-20151222.zip' %}
      </td>
      <td>
        Just prior to <a href="/news/2015-12-22-the-road-to-java-8">starting the transition to Java 8</a>.
      </td>
    </tr>
    <tr>
      <td>2014 November 25</td>
      <td style="text-align: center">
        {% include icon name='Windows' size='24px' link='https://downloads.imagej.net/fiji/Life-Line/fiji-win64-20141125.zip' %}
      </td>
      <td style="text-align: center">
        {% include icon name='Windows' size='24px' link='https://downloads.imagej.net/fiji/Life-Line/fiji-win32-20141125.zip' %}
      </td>
      <td style="text-align: center">
        {% include icon name='MacOS' size='24px' link='https://downloads.imagej.net/fiji/Life-Line/fiji-macosx-20141125.dmg' %}
      </td>
      <td style="text-align: center">
        {% include icon name='Linux' size='24px' link='https://downloads.imagej.net/fiji/Life-Line/fiji-linux64-20141125.tar.gz' %}
      </td>
      <td style="text-align: center">
        {% include icon name='Linux' size='24px' link='https://downloads.imagej.net/fiji/Life-Line/fiji-linux32-20141125.tar.gz' %}
      </td>
      <td style="text-align: center">
        {% include icon name='Fiji' size='24px' link='https://downloads.imagej.net/fiji/Life-Line/fiji-nojre-20141125.zip' %}
      </td>
      <td>
        Just prior to a <a href="https://groups.google.com/g/fiji-devel/c/49a7q7e9g44/m/xuhp0nQRVnAJ">big update</a> to facilitate <a href="reproducible_builds">reproducible builds</a>.
      </td>
    </tr>
    <tr>
      <td>2014 June 02</td>
      <td style="text-align: center">
        {% include icon name='Windows' size='24px' link='https://downloads.imagej.net/fiji/Life-Line/fiji-win64-20140602.zip' %}
      </td>
      <td style="text-align: center">
        {% include icon name='Windows' size='24px' link='https://downloads.imagej.net/fiji/Life-Line/fiji-win32-20140602.zip' %}
      </td>
      <td style="text-align: center">
        {% include icon name='MacOS' size='24px' link='https://downloads.imagej.net/fiji/Life-Line/fiji-macosx-20140602.dmg' %}
      </td>
      <td style="text-align: center">
        {% include icon name='Linux' size='24px' link='https://downloads.imagej.net/fiji/Life-Line/fiji-linux64-20140602.tar.gz' %}
      </td>
      <td style="text-align: center">
        {% include icon name='Linux' size='24px' link='https://downloads.imagej.net/fiji/Life-Line/fiji-linux32-20140602.tar.gz' %}
      </td>
      <td style="text-align: center">
        {% include icon name='Fiji' size='24px' link='https://downloads.imagej.net/fiji/Life-Line/fiji-nojre-20140602.zip' %}
      </td>
      <td>
        Just prior to <a href="/news/2014-06-04-imagej-2-0-0-release-candidate">some big changes to ImageJ2 under the hood</a>.
      </td>
    </tr>
    <tr>
      <td>2013 July 15</td>
      <td style="text-align: center">
        {% include icon name='Windows' size='24px' link='https://downloads.imagej.net/fiji/Life-Line/fiji-win64-20130715.zip' %}
      </td>
      <td style="text-align: center">
        {% include icon name='Windows' size='24px' link='https://downloads.imagej.net/fiji/Life-Line/fiji-win32-20130715.zip' %}
      </td>
      <td style="text-align: center">
        {% include icon name='MacOS' size='24px' link='https://downloads.imagej.net/fiji/Life-Line/fiji-macosx-20130715.dmg' %}
      </td>
      <td style="text-align: center">
        {% include icon name='Linux' size='24px' link='https://downloads.imagej.net/fiji/Life-Line/fiji-linux64-20130715.tar.gz' %}
      </td>
      <td style="text-align: center">
        {% include icon name='Linux' size='24px' link='https://downloads.imagej.net/fiji/Life-Line/fiji-linux32-20130715.tar.gz' %}
      </td>
      <td style="text-align: center">
        {% include icon name='Fiji' size='24px' link='https://downloads.imagej.net/fiji/Life-Line/fiji-nojre-20130715.zip' %}
      </td>
      <td>
        Just prior to <a href="https://groups.google.com/g/fiji-devel/c/KpuWJ6kNgbk/m/XX2pR8jjam8J">extensive changes reconciling Fiji with ImageJ2</a>.
      </td>
    </tr>
  </tbody>
</table>
{:/}

## See also

-   [https://downloads.imagej.net/fiji/](https://downloads.imagej.net/fiji/) for early versions of [Fiji](/software/fiji), and other miscellany.
