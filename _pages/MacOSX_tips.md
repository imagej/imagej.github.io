'''Critical:''' if you update and Fiji does not work anymore, you need to follow [[Fix_non-functional_Fiji_after_Update_on_MacOSX|these instructions]].

==Installing Fiji==

#Download the .dmg package from the [[Downloads]] page, and then double-click it to open it.
#Create a folder under /Applications/, such as /Applications/Fiji
#Drag the 3 items (Fiji.app, and the plugins and macros symlinks) into the /Applications/Fiji folder.


Fiji is ready to run!

==Running Fiji in 32-bit mode==
{{Warning | 1=It may no longer be possible to start Fiji in 32-bit on recent versions of OS X. See [https://fiji.sc/bugzilla/show_bug.cgi?id=1018 this bug report] for details.}}
Fiji on Intel Macs runs on Java 1.6 in 64-bit mode. If you need to run it in 32-bit mode, you can do so as follows:

# Launch Fiji normally, and choose {{bc | Edit | Options | Memory & Threads}}.
# Reduce your Maximum Memory setting to ~1800 MB or less.
# Quit Fiji.
# {{key|Ctrl}}+{{key|click}} the Fiji dock icon and choose {{bc | Options | Show in Finder}}.
# {{key|Ctrl}}+{{key|click}} on the Fiji application icon that pops up, and choose Show Info (or press {{key|Cmd}}+{{key|I}}).
# Check the "Open in 32-bit mode" box in the Fiji info window.
# Press the red X on the Fiji info window to close it.
# Launch Fiji again, and the status bar should report "[32-bit]" in brackets.

Alternately, you can execute the following code from the Terminal:
 arch -i386 /Applications/Fiji.app/Contents/MacOS/ImageJ-macosx

Either way, you will need to make sure your maximum memory limit is set below ~1800 MB.  If your maximum memory is set higher than the 32-bit limit, Fiji will not be able to start up successfully in 32-bit mode.

== Limited PowerPC (G4/G5) Mac support ==

We offer [https://fiji.sc/downloads/Heidelberg/fiji-macosx-ppc-20100802.dmg a special intermediate release of Fiji specific to PowerPC Macs (G4/G5)].

'''Note:''' There is no Java 1.6 for PowerPC from Apple, meaning that Java comes at a considerable performance penalty on this platform. In addition, we will not be able to support Java versions prior to Java 1.6 at some stage, since that version offers a few features we want to rely on, such as [http://java.sun.com/developer/technicalArticles/J2SE/Desktop/scripting/ a versatile scripting framework].

===Advanced===
You can also install a third party Java 6, part of the OpenJDK project. 
You will need a [http://developer.apple.com/opensource/tools/x11.html working X11 server], that you can find on your OS X disk, and MacPorts. 

Execute '''sudo port install openjdk6''' on your Terminal. You can also install the SoyLatte Binaries, as an alternate choice.
Then you can proceed with the generic Fiji Installation

Check more info at 
[http://landonf.bikemonkey.org/static/soylatte/ landonf.bikemonkey.org/static/soylatte/]

==Accessing the plugins and macros folders==

To access the plugins or macros folders, set the Finder window to either icons or lists mode, <b>not</b> in column mode, and double-click them.

Alternatively, right-click (or {{key|Ctrl}}+{{key|click}}) the Fiji.app and select "Show package contents", to open the folder where the actual plugins and macros folders are.

==Adding new plugins and macros==

For plugins, please follow the instructions about [[Installing 3rd party plugins]]. Otherwise, access the plugins folder as explained above and just drag and drop any plugin into the plugins folder, like you would do for ImageJ. Same for macros.

== Installing OpenJDK for MacOSX ==

Oracle now supports MacOSX JavaSE 7 [http://www.h-online.com/open/news/item/Java-SE-7-Update-6-hands-OS-X-support-to-Oracle-1667714.html officially].

It is based on [http://openjdk.java.net/projects/macosx-port/ an Apple-backed effort] to get a proper MacOSX backend into the BSD port of OpenJDK. So far, only Snow Leopard and later are supported, and preliminary builds can be found [http://code.google.com/p/openjdk-osx-build/ here].

If you are experiencing problems, say, with AWT-AppKit related crashes, and if you do not mind working with an X11-based graphical user display, you might want to try OpenJDK.

As of mid-April 2011, OpenJDK for MacOSX has basic working support for Aqua, which you have to activate explicitly by passing the Java option ''-Dswing.defaultlaf=com.apple.laf.AquaLookAndFeel''.

Since the development of OpenJDK for MacOSX is driven exclusively by Apple employees, the minimal MacOSX version required to run OpenJDK/Aqua is 10.6. If you require Fiji to run on earlier versions of MacOSX, you will have to go back to [http://landonf.bikemonkey.org/static/soylatte/ SoyLatte], where you will also find an X11-only OpenJDK version that runs on MacOSX 10.5/PowerPC (MacOSX 10.6+ does not support PowerPC). In the alternative, you can put in a considerable effort to "backport" OpenJDK :-).

== Running Fiji in the command line ==

Often it is necessary to run Fiji in the command line, e.g. to pass some command-line options. To do so, start a Terminal (in the Finder, ''Go>Utilities''), and switch to the correct directory using the ''cd'' command. Note that the application itself is actually a directory called ''Fiji.app''. For example, if you installed Fiji into ''/Applications'' as recommended, do this:

<source lang="bash">cd /Applications/Fiji.app</source>

If you unpacked Fiji onto your desktop, do this:

<source lang="bash">cd $HOME/Desktop/Fiji.app</source>

Once you switched to the correct directory, start the Fiji launcher:

<source lang="bash">Contents/MacOS/ImageJ-macosx</source>

'''Note for Windows users''': A backslash is not the same as a slash. So: ''Contents\MacOS\ImageJ-macosx'' will '''not''' work.

Now you can pass, say, [[Java Options]]:

<source lang="bash">Contents/MacOS/ImageJ-macosx -verbose:gc --</source>

'''Note''': to distinguish between options intended for Java and options intended for ImageJ, you need to separate the former from the latter with a double-dash: '''--'''. Since the default is to accept ImageJ options, you have to pass a trailing double-dash if you want to pass only Java options.

== MacOSX keyboard shortcuts ==

It is often helpful to use keyboard shortcuts when using Fiji. There are also operating system specific shortcuts which can be quite helpful. For example, pressing {{key|Command}}+{{key|Tab}} and releasing first only the {{key|Tab}} key will allow you to cycle through the running applications, while {{key|Command}}+{{key|`}} will do the same for the windows opened by the current application. [http://davespicks.com/ Dave Polaschek] has [http://davespicks.com/writing/programming/mackeys.html a comprehensive list].
