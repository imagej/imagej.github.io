---
title: JavaCV Installer
name: JavaCVInstaller
categories: [Development, Utilities]
source-url: https://github.com/anotherche/imagej-javacv-installer
release-date: March 11 2025
release-version: 0.6.0
dev-status: Active
support-status: Active
team-founders: "@anotherche"
team-maintainers: "@anotherche"
---

## What is JavaCV

In short, JavaCV is a collection of Java interfaces to various native computer vision libraries originally written in C/C++.

The collection currently includes interfaces to libraries such as OpenCV, FFmpeg, libdc1394, FlyCapture, libfreenect, librealsense, videoInput, ARToolKitPlus, Leptonica, and Tesseract.

The interfaces are based on the original JavaCPP technology developed by Samuel Audet, which allows automatic generation of JNI code for Java wrappers of native libraries using C/C++ header files.

More information is available at [Bytedeco site](https://bytedeco.org/) and [Github](https://github.com/bytedeco).

## How can JavaCV help with ImageJ

JavaCV itself does not contain any plugins for direct use in ImageJ. 
However, the interfaces it provides contain many classes and methods for image analysis and manipulation that can be used to develop plugins. 
Thus, JavaCV may be needed primarily by plugin developers.

For example, JavaCV was used to develop the [FFmpeg_Video](https://forum.image.sc/t/plugins-for-reading-and-writing-compressed-video/8777) plugin, which uses FFmpeg API to implement import/export of video files of almost any format in ImageJ. 
In [PhotoBend](https://imagej.net/plugins/photobend) plugins, the OpenCV interface is used for specific object recognition and tracking, while FFmpeg allows to use video files as sources of sequences of analyzed images.

## What is the JavaCV installer plugin and who might need it

When using third party libraries, developers are always faced with the need to ensure that all dependencies are in place without causing conflicts with other parts of the software. 
Since JavaCV contains a large number of interfaces and native libraries for different types of platforms, 
simultaneous use of JavaCV components by different ImageJ plugins can lead to problems with over-provisioning dependencies of all the different plugins, 
as well as incompatibility between different versions of the components. 

To solve this problem, one needs to be able to centrally manage the installation of JavaCV components, and this is exactly what the JavaCV Installer plugin does.

## How it works

***internal operation***

Using the Apache Maven Artifact Resolver library, the installer queries the central Maven repository to determine the available versions of JavaCV and the interfaces provided by its various releases.
A user or programmatic interface allows the user to select JavaCV components of the desired versions and install them in ImageJ.

During installation, the installer checks for and resolves any version conflicts that may occur. 
For the final installation of dependencies (jar files), the installer uses a built-in ImageJ update mechanism that requires a restart of ImageJ after the installation is complete.
Additionally, the installer creates a local cache of the repository, allowing quick switching between JavaCV versions 
("local-maven-repo" forlder inside ImageJ installation that can be freely deleted at any moment - the installer will recreate it if necessary).

***user front-end***

Manual JavaCV installation can be done using the plugin's user interface:

![](/media/plugins/javacv-installer-ui.png)

Using macro or public methods of the plugin, developers can automatically check for required interfaces and install missing JavaCV dependencies in ImageJ.

For example, to silently install ffmpeg and opencv from JavaCV 1.5.10, one can run the following macro:
```java
IJ.run("Install JavaCV libraries", "version=1.5.10 select_installation_option=[Install missing] treat_selected_version_as_minimal_required ffmpeg opencv");
```

To implement interactive installation of missing dependencies, one can use the following code 
(note that the first part of this method checks if the installer itself is installed, and installs it in ImageJ if it is missing.):

```java
boolean checkJavaCV(String version, boolean treatAsMinVer, String components) {

		String javaCVInstallCommand = "Install JavaCV libraries";
		Hashtable table = Menus.getCommands();
		String javaCVInstallClassName = (String) table.get(javaCVInstallCommand);
		if (javaCVInstallClassName == null) {
			int result = JOptionPane.showConfirmDialog(null,
					"<html><h2>JavaCV Installer not found.</h2>"
							+ "<br>Please install it from from JavaCVInstaller update site:"
							+ "<br>https://sites.imagej.net/JavaCVInstaller/"
							+ "<br>Do you whant it to be installed now for you?"
							+ "<br><i>you need to restart ImageJ after the install</i></html>",
					"JavaCV check", JOptionPane.YES_NO_OPTION, JOptionPane.QUESTION_MESSAGE);
			if (result == JOptionPane.YES_OPTION) {
				net.imagej.updater.CommandLine updCmd = new net.imagej.updater.CommandLine(
						AppUtils.getBaseDirectory("ij.dir", CommandLine.class, "updater"), 80);
				updCmd.addOrEditUploadSite("JavaCVInstaller", "https://sites.imagej.net/JavaCVInstaller/", null, null,
						false);
				net.imagej.updater.CommandLine updCmd2 = new net.imagej.updater.CommandLine(
						AppUtils.getBaseDirectory("ij.dir", CommandLine.class, "updater"), 80);
				updCmd2.update(Arrays.asList("plugins/JavaCV_Installer/JavaCV_Installer.jar"));
				IJ.run("Refresh Menus");
				table = Menus.getCommands();
				javaCVInstallClassName = (String) table.get(javaCVInstallCommand);
				if (javaCVInstallClassName == null) {
					IJ.showMessage("JavaCV check",
							"Failed to install JavaCV Installer plugin.\nPlease install it manually.");
				}
			}
			return false;
		}

		String installerCommand = "version=" + version + " select_installation_option=[Install missing] "
				+ (treatAsMinVer ? "treat_selected_version_as_minimal_required " : "") + components;

		boolean saveRecorder = Recorder.record; // save state of the macro Recorder
		Recorder.record = false; // disable the macro Recorder to avoid the JavaCV installer plugin being
									// recorded instead of this plugin
		String saveMacroOptions = Macro.getOptions();
		IJ.run("Install JavaCV libraries", installerCommand);
		if (saveMacroOptions != null)
			Macro.setOptions(saveMacroOptions);
		Recorder.record = saveRecorder; // restore the state of the macro Recorder

		String result = Prefs.get("javacv.install_result", "");
		String launcherResult = Prefs.get("javacv.install_result_launcher", "");
		if (!(result.equalsIgnoreCase("success") && launcherResult.equalsIgnoreCase("success"))) {
			if (result.indexOf("restart") > -1 || launcherResult.indexOf("restart") > -1) {
				IJ.log("Please restart ImageJ to proceed with installation of necessary JavaCV libraries.");
				return false;
			} else {
				IJ.log("JavaCV installation failed. Trying to use JavaCV as is...");
				return true;
			}
		}
		return true;
	}
```
## Installation in Fiji

To install the plugin manually:
<ol>
  <li>add JavaCV Installer update site https://sites.imagej.net/JavaCVInstaller using the update sites manager </li>
  <li>install the plugin normally using the updater</li>
</ol>

For the automated installation see the above code example of the `checkJavaCV` method.

## Additional information and support

The plugin is discussed at [imagej forum](https://forum.image.sc/t/new-javacv-installer-plugin/55392)
