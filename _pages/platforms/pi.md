---
title: Raspberry Pi
section: Learn:ImageJ Basics:Supported Platforms
---

{% include img src='icons/pi' align='right' class="box" width=150 caption='Learn programming through fun, practical projects!' %}

The {% include wikipedia title='Raspberry Pi' text='Raspberry Pi' %} is an inexpensive single-board computer system which runs the {% include wikipedia title='Raspbian' text='Raspbian' %} operating system, a flavor of Debian [Linux](/platforms/linux). This page provides advice and guidance for running [ImageJ](/software/imagej) and [Fiji](/software/fiji) on Raspberry Pi systems.

# Installation

{% include aside content='You might notice there is as an `imagej` package available from your package manager. Please be aware that this provides [ImageJ 1.x](/software/imagej1) only, packaged by a third party, without cooperation from the core ImageJ development team. You will not have access to any [ImageJ2](/software/imagej2)-specific features such as [parameterized scripts](/scripting/parameters), and you will likely have permissions errors because it is a system-wide ImageJ installation.' %}

The following steps describe how to install ImageJ on a Raspberry Pi:

1.  Open the terminal.
2.  Install Java 8 on your Pi (`sudo apt-get install openjdk-8-jre`).
3.  Choose Java 8 (`sudo update-alternatives --config java`).
4.  Verify it works using `java -version`.
5.  Download and install the [platform-independent "no JRE" distribution of Fiji](http://downloads.imagej.net/fiji/latest/fiji-nojre.zip).
6.  Download the [ImageJ.sh](https://github.com/imagej/imagej/blob/master/bin/ImageJ.sh) shell script
7.  Move the ImageJ.sh file to the Fiji.app folder
8.  Set the executable bit (`chmod +x ImageJ.sh`)
9.  Run it (`./ImageJ.sh`) to launch ImageJ.

You may also need to disable (comment out) `assistive_technologies=org.GNOME.Accessibility.AtkWrapper` in `/etc/java-8-openjdk/accessibility.properties`.

Note that the shell script supports only a subset of the functionality of the native [ImageJ Launcher](/Launcher), but it should be able to run ImageJ successfully.

The following steps describe how to create a desktop icon to launch Fiji on a Raspberry Pi:

1.  Download the Fiji icon image: [Fiji icon link](/media/icons/fiji.png)
2.  Press {% include key keys='ctrl|alt|t' %} to open the terminal window
3.  Type `nano Fiji.desktop` and press return. This will load Nano which will allow you to create a desktop icon.
4.  Type the following code, replacing `/path/to` with the paths to the `ImageJ.sh` file and the Fiji icon:

<!-- -->

    [Desktop Entry]
    Name=Fiji
    Version=1.0
    Comment=Launches Fiji
    Exec=/path/to/ImageJ.sh
    Icon=/path/to/48px-Fiji-icon.png
    Terminal=false
    Type=Application
    Categories=Education

1.  Press {% include key keys='ctrl|x' %} and then press {% include key key='Y' %} to exit and save the new desktop icon.
2.  Enter your desired file name, such as `Fiji.desktop` and press return. Once complete, an icon should be visible on the desktop.
3.  Press {% include key keys='ctrl|x' %} to return to the terminal window
4.  In the terminal window, type the following to navigate to the Desktop `cd ~/Desktop`
5.  Then type the following to make the new icon executable `chmod +x Fiji.desktop`

# 3D Visualization

It is supposedly possible to run [Java 3D](/libs/java-3d) on the Pi; see [this StackOverflow thread](http://stackoverflow.com/questions/28529344/how-to-run-java3d-on-rpi-2). However, there have been no official reported successes on ImageJ community channels yet. If you get it working, please edit this section to describe the steps you used!

Even better, if you get [ClearVolume](/plugins/clearvolume) and/or [SciView](/plugins/sciview) working on the Pi, please update this page, and announce it on the [Image.sc Forum](/discuss)!

# Troubleshooting

See the [Troubleshooting](/learn/troubleshooting) page.

# Frequently Asked Questions

See the [Frequently Asked Questions](/learn/faq) page.

# See also

-   Topics tagged [raspberry-pi](https://forum.image.sc/tags/raspberry-pi) on the [Image.sc Forum](/discuss).
-   The [Linux](/platforms/linux) page, for general information about ImageJ on Linux systems.


