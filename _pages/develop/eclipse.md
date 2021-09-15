---
mediawiki: Developing_ImageJ_in_Eclipse
title: Developing ImageJ2 in Eclipse
section: Extend:Development:Tools:IDEs
project: /software/imagej2
---

This article explains how to install, configure and use Eclipse to develop
[ImageJ2](/software/imagej2) [components](/develop/architecture#definitions) and
[plugins](/plugins). Directions correspond to Eclipse 4.4 Luna, and may need
adjustment for other versions.

# Initial setup

## Install the Java Development Kit

-	To be safe, since you may need JavaFX (for the GUI) download [Java8 JDK with FX from Azul](https://www.azul.com/downloads/?version=java-8-lts&package=jdk-fx). Make sure to scroll down and choose the appropriate Operating System (Windows, Linux, etc) and Architecture (x86 64 bit for most systems, though older systems may be 32 bit). Pay attention to where you install this, as you will need to find it again within Eclipse!
-   Alternatively, download and install the Java Development Kit (JDK) from the
    [Java web site](https://www.oracle.com/java/technologies/javase-downloads.html). 

## Install and configure Eclipse

### Install Eclipse

-   Download "Eclipse IDE for Java Developers" from the
    [Eclipse web site](http://www.eclipse.org/downloads/).

{% include notice icon="warning" content='It is **important** to choose "Eclipse IDE for Java Developers" because it contains Maven support built-in. Otherwise, you will have to [install the M2E plugin manually](http://eclipse.org/m2e/).' %}

-   Unpack the archive to a location of your choice.

### Configure Eclipse for your platform

<div class="tab">
  <button class="tablinks" onclick="openTab(event, 'windows')">Windows</button>
  <button class="tablinks" onclick="openTab(event, 'macos')">MacOS</button>
  <button class="tablinks" onclick="openTab(event, 'linux')">Linux</button>
</div>

<div id="windows" class="tabcontent" markdown="1">
{%- include icon name="Windows" size="32px" -%}
<br/>

**Avoid permissions issues.** We recommend installing Eclipse *outside* of the `Program Files` directory. E.g.: `C:\Users\frood\Programs\eclipse`, where `C:\Users\frood` is your user directory.

**Configure Eclipse.** After installing Eclipse, you will need to configure it to know about your JDK.

Use Wordpad to edit the `eclipse.ini` file in your Eclipse installation (e.g., `C:\Users\frood\Programs\eclipse`). (Do not use Notepad, because it will not handle the Unix-style line breaks properly.) Carefully follow [these instructions](http://wiki.eclipse.org/Eclipse.ini#specifying-the-jvm) to specify the proper JDK. Then save the file and quit Wordpad.

Now update Eclipse's JRE to be JDK-aware:

-   Launch Eclipse
-   From the menu choose {% include bc path='Window | Preferences' %}
-   Select {% include bc path='Java | Installed JREs' %}
-   Click Search..., navigate to your JDK installation folder (e.g., `C:\Program Files\Java\jdk1.8.0_11`) and click OK
-   Check the box next to the JRE that appears and click OK

</div>
<div id="macos" class="tabcontent" markdown="1">
{%- include icon name="MacOS" width="32px" -%}
<br/>

**Understand Java 6 vs. Java 8.** Eclipse should work on macOS with no further configuration. However, we recommend reading the [macOS section of the FAQ](/learn/faq#macos), as there are several Java-related issues on macOS.

</div>
<div id="linux" class="tabcontent" markdown="1">
{%- include icon name="Linux" width="32px" -%}
<br/>

**Avoid permissions issues.** We recommend installing to `$HOME/eclipse`.

**Do not use a package manager.** For several reasons, we do not recommend installing Eclipse from a package manager. You may not get a new enough version of Eclipse (we recommend 4.3+), you will not get the Java Developers version that includes the M2E plugins, and you will likely have trouble installing additional plugins due to the permissions issues with the system-wide installation.

**Adjust the Eclipse font size.** Sometimes it is desirable to change the Eclipse font size. To do so, create a GTK configuration file (e.g. `~/.gtkrc-eclipse`) and place the following lines there:

```
style "eclipse" {
    font_name = "Sans Condensed 8"
}
class "GtkWidget" style "eclipse"
```

Then run eclipse using this command: `GTK2_RC_FILES=~/.gtkrc-eclipse eclipse`
</div>

## Clone the source code

Using your [Git client of choice](http://git-scm.com/downloads/guis), clone the source code which interests you:

-   If you want to work on an existing project, see the [list of sources](/develop/source).
-   If you are creating your own project, see the [building a pom](/develop/building-a-pom) guide.

## Import the source code

1.  Choose {% include bc path='File | Import' %} from the Eclipse menu
2.  Select "Existing Maven Projects" and click Next
3.  Browse to the folder where you cloned the project source code
4.  Click Finish

Eclipse will import and automatically build the project(s). There should not be any build errors, but it is normal to see a large number (often hundreds) of warnings. These mostly come from Java-1.4-style code or unnecessary imports, variables or methods in the sources of authors who do not use an IDE and thus have no automatic assistance at cleaning up. All these warnings can be ignored, having no effect on the functionality of the code.

If you're having trouble, how to import and build your Maven + Eclipse project, follow this video: [How To Setup and Make a Fiji Plugin](https://www.youtube.com/watch?v=YIWpoBnnLio)

# Keyboard shortcuts

<table style="width: auto">
  <tbody>
    <tr><td colspan=2 style="text-align: center"><strong>Navigation</strong></td></tr>
    <tr>
      <td style="text-align: right">{% include key keys='CtlCmd|Shift|T' %}</td>
      <td>Open a Java class from the workspace</td>
    </tr>
    <tr>
      <td style="text-align: right">{% include key keys='CtlCmd|Shift|R' %}</td>
      <td>Open a file from the workspace</td>
    </tr>
    <tr>
      <td style="text-align: right">{% include key key='F3' %}</td>
      <td>
        Jump to selected class<br>
        (to edit the code, see <a href="/develop/architecture#using-snapshot-couplings-during-development">snapshot coupling</a>)
      </td>
    </tr>
    <tr>
      <td style="text-align: right; ">{% include key keys='CtlCmd|O' %}</td>
      <td>Show superclass/subclass hierarchy</td>
    </tr>
    <tr>
      <td style="text-align: right">{% include key keys='CtlCmd|T' %}</td>
      <td>Show implementations of interface or class</td>
    </tr>
    <tr>
      <td style="text-align: right">{% include key keys='CtlCmd|L' %}</td>
      <td>Go to line number</td>
    </tr>
    <tr>
      <td style="text-align: right">{% include key keys='CtlCmd|Q' %}</td>
      <td>Go to last edit location</td>
    </tr>
    <tr>
      <td style="text-align: right">{% include key keys='CtlCmd|E' %}</td>
      <td>Go to next file in editor</td>
    </tr>
    <tr><td colspan=2 style="text-align: center"><strong>Editing</strong></td></tr>
    <tr>
      <td style="text-align: right">{% include key keys='Alt|Up' %}, {% include key keys='Alt|Down' %}</td>
      <td>Move current line up or down</td>
    </tr>
    <tr>
      <td style="text-align: right">{% include key keys='CtlCmd|D' %}</td>
      <td>Delete the current line</td>
    </tr>
    <tr>
      <td style="text-align: right">{% include key keys='CtlCmd|/' %}</td>
      <td>Comment/uncomment the selected line(s)</td>
    </tr>
    <tr>
      <td style="text-align: right">{% include key keys='CtlCmd|1' %}</td>
      <td>Quick fix selected error</td>
    </tr>
    <tr>
      <td style="text-align: right">{% include key keys='CtlCmd|Space' %}</td>
      <td>Auto-complete current selection</td>
    </tr>
    <tr><td colspan=2 style="text-align: center"><strong>Code cleanup</strong></td></tr>
    <tr>
      <td style="text-align: right">{% include key keys='CtlCmd|Shift|O' %}</td>
      <td>Organize imports</td>
    </tr>
    <tr>
      <td style="text-align: right">{% include key keys='CtlCmd|Shift|F' %}</td>
      <td>
        Format code<br>
        (BUT make sure you set the <a href="/develop/coding-style#eclipse-code-style-profiles">coding style</a>)
      </td>
    </tr>
    <tr>
      <td style="text-align: right; ">{% include key keys='Alt|Shift|S' %}, {% include key key='U' %}</td>
      <td>Clean up (does format and much more)</td>
    </tr>
    <tr>
      <td style="text-align: right">{% include key keys='Alt|Shift|R' %}</td>
      <td>Refactor/rename selected class/variable</td>
    </tr>
    <tr><td colspan="2" style="text-align: center"><strong>Debugging</strong></td></tr>
    <tr>
      <td style="text-align: right">{% include key keys='CtlCmd|Shift|B' %}</td>
      <td>Set/Remove breakpoint</td>
    </tr>
    <tr>
      <td style="text-align: right">{% include key key='F5' %}</td>
      <td>Step into</td>
    </tr>
    <tr>
      <td style="text-align: right">{% include key key='F6' %}</td>
      <td>Step over</td>
    </tr>
    <tr>
      <td style="text-align: right">{% include key key='F7' %}</td>
      <td>Step out</td>
    </tr>
  </tbody>
</table>

# The Run-Debug cycle

Now that you have the project successfully nestled within Eclipse, you can run
it, change the code, and run it again, iterating as needed to develop features
and fix bugs. This process is known as the *run-debug cycle*—although some
people call it *compile-debug* or *edit-compile-debug* or *edit-compile-run* or
*debug-edit-compile* or *edit-build-test-debug* or *edit-compile-link-debug*
or...

## Launch ImageJ2

If you cloned the [imagej2 project](https://github.com/imagej/imagej2),
you can launch the program as follows:

1. In the Package Explorer, expand the `imagej2` project
2. Navigate into `src/main/java`
3. Navigate into `net.imagej`
4. Right-click on `Main.java`
5. Choose "Run As" and then "Java Application"

Other projects will have different main classes,
but the general procedure is the same.

## Testing your plugin in an existing installation

When you run your plugin from Eclipse, you're only testing with the classpath
*of this project*&mdash;which may or may not reflect the environment of an
actual user's installation. To test your plugin in an existing installation you
can either simply copy the jar, or use Maven to install your plugin and its
dependencies.

{% include thumbnail src='/media/develop/mavenrunconfig.png' title='Setting up a new Maven Build configuration' %}

### Option 1: Copying the jar

All modern Eclipse installations have the m2e plugin, so you can simply tell
Maven to
[build the project](http://www.vogella.com/tutorials/EclipseMaven/article.html#example_eclipsemavenproject_runningthebuild).
This creates a `.jar` in the `/target` subdirectory,
which you can then copy to an `ImageJ.app/jars/` directory.

This is a simple option that makes minimal changes to the existing
installation.

### Option 2: Install dependencies

All mavenized ImageJ projects have built-in support for installing directly
into an existing installation, overwriting previous versions of any components,
and pulling in up-to-date versions of any dependencies. This is the most robust
way to test your plugin, but note that it may make additional changes to your
existing ImageJ installation.

Steps are as follows:

1. Right-click your project in Eclipse and select
   {% include bc path='Run As|Run Configurations...' %}

2. Scroll down to Maven Build. If you've built this project with Maven via
   Eclipse before there will already be a configuration for it. Otherwise you
   can double-click "Maven Build" to create a new run configuration.

3. Add a parameter: `imagej.app.directory` with value:
   `<path/to/ImageJ.app>` (e.g. `/home/hinerm/Fiji.app`)

4. Add a parameter: `imagej.deleteOtherVersions` with value: `always`

5. Click `Apply`

You can now run the project from this dialog. You only need to perform this
configuration once though—future uses of the
[Maven Build](http://www.vogella.com/tutorials/EclipseMaven/article.html#example_eclipsemavenproject_runningthebuild)
option will automatically copy your plugin and its dependencies to the
specified ImageJ app.

## Adding new plugins

The easiest method is to start with a
[minimal project](https://github.com/imagej/example-legacy-plugin), renamed to
the desired name of your plugin. By convention, the project directory should
match the base name of the `.jar` file to be generated.

The format of such a `pom.xml` is described briefly on the
[Maven](/develop/maven) page.

Most importantly, you will need to adjust the `artifactId` and the
`dependencies` section. Should you require a dependency that is not used in
Fiji yet, you might want to search for the appropriate `groupId` and `version`
in the [SciJava Maven repository](/develop/project-management#maven).

Next, you will put your Java sources into `src/main/java/`
and adjust `src/main/resources/plugins.config`.

After that, ask Eclipse to import it:
{% include bc path='File | Import | Maven | Import Existing Maven Project' %}.

## Viewing Dependency Source

When jumping into a dependency class in Eclipse (using
{% include key key='F3' %}), you may see a message stating "Source not found".

For Maven dependencies there must be a `-sources` classifier JAR in the
repository along side the main JAR. For example, `imagej-common` has an
`imagej-common-0.24.4.jar` and an `imagej-common-0.24.4-sources.jar`. In
theory, the Eclipse M2E plugin should download this `-sources` JAR and
automatically display it to you when you jump to the class.

However, if for some reason this doesn't happen
you can try the following steps.

1.  Try right-clicking the JAR in the Maven dependencies in Eclipse, and
    selecting "Download Sources". This should force Eclipse to download the
    `-sources` JAR.

2.  Check that the `-sources` JAR has been downloaded locally.
    -   Navigate to
        `<path-to-.m2-repo>/repository/<groupId>/<artifactId>/<version>`
        and see if there is a `-sources` JAR there.
    -   If it is not, then in a terminal navigate to the folder containing your
        project's pom.xml file. And then from the command line run:
        ```
        mvn dependency:get -Dartifact=groupId:artifactId:version:packaging:classifier
        ```
        -   For example if a project depended on imagej-common and you needed
            to retrieve the `-sources` JAR, the command you'd type would be:
            ```
            mvn dependency:get -Dartifact=net.imagej:imagej-common:0.24.4:jar:sources
            ```

3.  If the `-sources` JAR was there, you could check its contents by running
    the following command from the terminal:
    ```
    jar tr <path-to-.m2-repo>/repository/<groupId>/<artifactId>/<version>/<jar-name>-sources.jar
    ```
    -   If the file in question isn't there, then unfortunately
        this project doesn't have source for that class.

If the class you're trying to view is a part of the JRE and you're on Linux,
you may need to run `sudo apt install openjdk-<java-version-number>-sources`
to retrieve the sources.

Note that doing this only allows you to view the source code, it does **not**
allow you to edit it. If you need to edit these files, see the
[snapshot coupling](/develop/architecture#using-snapshot-couplings-during-development)
section for more information.

## See also

* [Developing plugins for ImageJ2](/develop/plugins)
* [Developing plugins for ImageJ 1.x](/develop/ij1-plugins)
* [Contributing to a plugin](/develop/improving-the-code)
* {% include github org='imagej' repo='example-imagej-command' label='example-imagej-command' %} ([ImageJ2](/software/imagej2)-style command)
* {% include github org='imagej' repo='example-legacy-plugin' label='example-legacy-plugin' %} ([ImageJ 1.x](/software/imagej)-style command)
