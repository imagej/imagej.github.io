---
mediawiki: Java_3D
title: Java 3D
section: Explore:Libraries
---

{% include wikipedia title='Java 3D' text='Java 3D'%} is a technology used for 3D visualization in Java. It is used by ImageJ's [3D Viewer](/plugins/3d-viewer) plugin, and hence transitively by other plugins which rely on the 3D Viewer for their visualization, such as [TrakEM2](/plugins/trakem2) and [Simple Neurite Tracer](/plugins/simple-neurite-tracer).

## Status of Java 3D

The Java 3D project, originally developed at Sun (now Oracle), has been abandoned for several years in favor of [JavaFX 3D](https://docs.oracle.com/javase/8/javafx/graphics-tutorial/javafx-3d-graphics.htm). However, it has been adopted by the [JogAmp](https://jogamp.org/) community, and is now maintained there—though no longer under active development.

From the perspective of new features, Java 3D is essentially a dead technology. The future of 3D visualization in ImageJ is the [sciview](/plugins/sciview) plugin. But it will be a lot of work to make sciview comparable to—and eventually better than—3D Viewer, so the ImageJ and [Fiji](/software/fiji) teams are still exploring the best ways to proceed here.

## Versions of Java 3D

### Java 3D 1.5

The last version of Java 3D supported by Sun/Oracle was 1.5.2. It was packaged as an extension of Java, meaning it needed to be installed into your Java Runtime Environment, rather than shipped as a normal Java library.

It works with Java 6, but:

-   It has a restrictive license.
-   It does not work with Java 7 or 8 on macOS.
-   It does not work with Java 8 (or 7?) on some Windows systems.

The Java 6 version of ImageJ works with Java 3D 1.5.2, by launching the 3D Viewer and allowing it to automatically install Java 3D; see [this page](/news/2016-05-10-imagej-howto-java-8-java-6-java-3d) for further details.

### Java 3D 1.6

Java 3D 1.6 and later are community versions maintained by JogAmp. Java 3D 1.6 was rewritten to work on top of {% include wikipedia title='Java OpenGL' text='JOGL'%}, and requires Java 7 or newer.

The [Fiji](/software/fiji) distribution of ImageJ includes Java 3D 1.6; see [this page](/news/2016-05-10-imagej-howto-java-8-java-6-java-3d) for further details.

## Troubleshooting Java 3D

When Java 3D does not work, the first order of business is to use {% include bc path='Plugins | Utilities | Debugging | Test Java3D'%}. If this shows a rotating cube, but the [3D Viewer](/plugins/3d-viewer) does not work, please click on {% include bc path='Help | Java3D Properties...'%} in the [3D Viewer](/plugins/3d-viewer)'s menu bar.

### Command line debugging

If this information is not enough to solve the trouble, or if `Test Java3D` did not work, then you need to [call ImageJ from the command line](https://imagej.net/learn/troubleshooting#launching-imagej-from-the-console) to find out more.

### Show Java3D debug messages

From the command line, you have several options to show more or less information about Java3D.

```shell
./fiji -Dj3d.debug=true
```

### Windows-specific stuff

On Windows, you can choose between OpenGL and Direct3D by passing `-Dj3d.rend=ogl` or `-Dj3d.rend=d3d`, respectively.

Further, some setups require enough RAM to be reserved, so you might need to pass an option like `--mem=1200m` (make sure that you have enough RAM free before starting ImageJ that way, though!). If it turns out that memory was the issue, you can make the setting permanent by clicking ImageJ's {% include bc path='Edit | Options | Memory & Threads...'%} menu entry.

### More Java 3D properties

You can control quite a few things in Java 3D through setting Java properties. Remember, you can set properties using a command line like this:

```shell
./fiji -D<property-name>=<property-value>
```

where you substitute `<property-name>` and `<property-values>` appropriately. You can have more than one such option.

This list of Java 3D properties was salvaged from the now-defunct j3d.org website:

| Property                         | Values                | Java 3D version | Explanation |
|----------------------------------|-----------------------|-----------------|-------------|
| `j3d.rend`                       | `ogl` or `d3d`        | 1.3.2           | Win32-only. Specifies which underlying rendering API should be used (thus allowing both Direct3D and OpenGL native DLLs to be installed on a singe machine. (default value `ogl`) |
| `j3d.deviceSampleTime`           | A time in millseconds | 1.1             | The sample time for non-blocking input devices (default value is 5ms). |
| `j3d.disablecompile`             | N/A                   | 1.2             | If set turns off the ability to internally .compile() the scenegraph. |
| `j3d.docompaction`               | true or false         | 1.3             | Default true. Controls whether or not objects are removed from the render cache when they haven't been visibile for a while. If it is disabled, they stay in the render cache from when they are first visible until they are removed from the scene graph. |
| `j3d.forceReleaseView`           | true or false         | 1.3.2           | Default false. If this flag is set to true, the view is released after the Canvas3D is removed from the view. Can be used if you have memory leaks after disposing Canvas3D. Note: Setting this flag as true disables the bug fix 4267395 in View deactivate() |
| `j3d.implicitAntialiasing`       | true or false         | 1.3             | Default false. By default, full scene antialiasing is disabled if a multisampling pixel format (or visual) is chosen. To honor a display drivers multisample antialiasing setting (e.g. force scene antialiasing), set the implicitAntialiasing property to true. This causes Java3D to ignore its own scene antialias settings, letting the driver implicitly implement the feature |
| `j3d.optimizeForSpace`           | true or false         | 1.3             | Default true Java3d only builds display list for by-copy geometry. Set to false will cause Java3d to build display list for by-ref geometry and infrequently changing geometry using more space, but having greater speed. |
| `j3d.renderLock`                 | true or false         | 1.3             | JDK requires getting the JAWT_DrawingSurfaceInfo and lock the surface before Java3D render on the canvas. (see comment on jdk/include/jawt.h in the SDK) Default false causes Java3D to lock the surface before rendering and unlock it afterwards for onScreen rendering in the Renderer thread. For OffScreen rendering and for front/back buffer swapping the lock will not acquired. Setting the value to true will force Java3D lock the surface using the AWT mechanism before swap() and for offScreen rendering. This may be useful for some driver/OS to workaround problem. But in general the default should work. |
| `j3d.threadLimit`                | An integer            | 1.2             | Controls how many threads may run in parallel regardless of how many cpu's the system has. Setting it to "1" will make the system act like a traditional OpenGL render loop. The default value is the number of CPUs in your machine + 1. |
| `j3d.transparentOffScreen`       | true or false         | 1.3.2           | Default false. If this flag is set to true the background of the off screen canvas is set to transparent. |
| `j3d.usePbuffer`                 | true or false         | 1.3.2           | Default true. If this flag is set to false pbuffer will not be use for off screen rendering. |
| `j3d.viewFrustumCulling`         | true or false         | 1.3.2           | Default true. If this flag is set to false, the renderer view frustum culling is turned off. Java 3D uses a 2 pass view culling. The first pass is a loose view culling of the spatial tree, and the second pass is a tight view frustum culling in the renderer before sending the geometry down to the low level graphics API. This property is to control the renderer view frustum culling, and it will not affect the first pass view culling. |
| `javax.media.j3d.compileStats`   | N/A                   | ??              | Output scenegraph compilation statistics |
| `javax.media.j3d.compileVerbose` | N/A                   | ??              | Output verbose message when compiling scenegraph |

#### OpenGL only

| Property                      | Values        | Java 3D version | Explanation |
|-------------------------------|---------------|-----------------|-------------|
| `j3d.backgroundtexture`       | true or false | 1.3             | Prior to Java3D 1.3 OGL version of Java3D used `glDrawPixels()` to render background, which is known to be very slow under Windows since most window driver did not accelerate the function. To workaround this performance problem current release uses textures for the backgrond under windows by default (`glDrawPixels()` is used as default under Solaris). Setting this flag to false will force Java3D fall back to use `glDrawPixels()` instead of texture when drawing background texture in case it provide better performance under some drivers. |
| `j3d.disableSeparateSpecular` | true or false | 1.2             | Default true enables the use of specular highlights in textures when using OpenGL 1.2. |
| `j3d.disableXinerama`         | true or false | 1.3             | Solaris version only. Allows major performance boost when using dual screen environments with the X11 Xinerama extension enabled. To disable this feature you need JDK1.4. Detailed information in the release notes. |
| `j3d.displaylist`             | true or false | 1.2             | Default true to use display lists (an OpenGL performance enhancing feature). False to disable for debugging. |
| `j3d.g2ddrawpixel`            | true or false | 1.1             | If false, this will use texture mapping instead of glDrawPixel to flush the graphics2D to the screen. glDrawPixel is not accelerated on some older video cards (windows). |
| `j3d.sharedctx`               | true or false | 1.2             | Default true for Solaris and false for windows. Shared contexts are used in OpenGL for DisplayLists and Texture Objects to improve performance. However some drivers have bugs causing weird rendering artifacts. This can be used to disable their use to see if this is the problem. |
| `j3d.sharedstereozbuffer`     | true or false | 1.2             | Some framebuffers only have one Z buffer and share this between the left and right eyes. This may be the reason why they don't have quad buffer but can still support stereo by setting this flag to true. |
| `j3d.usecombiners`            | true or false | 1.3             | Default false, uses the standard OpenGL all environment options. When set to true, it will make use of the Nvidia register combiner extensions to OpenGL for for Texture combine modes such as `COMBINE_INTERPOLATE`, `COMBINE_DOT3`. (i.e. `GL_NV_register_combiners` instead of standard OpenGL call `glTexEnvi(GL_TEXTURE_ENV, ...)`). It can be use in case like Dot3 texture when the driver does not support OpenGL extension `GL_ARB_texture_env_dot3/GL_EXT_texture_env_dot3` but it supports the `GL_NV_register_combiners` extension instead. |

#### Direct3D only

| Property                  | Values                                                    | Java 3D version | Explanation |
|---------------------------|-----------------------------------------------------------|-----------------|-------------|
| `j3d.d3ddevice`           | `emulation` or `hardware` or `tnlhardware` or `reference` | 1.2             | Forces the software to use a particular mode for the underlying graphics accelaration. The reference option is only available if you have the Direct3D SDK installed (very unlikely). |
| `j3d.d3ddriver`           | `idx`                                                     | 1.2             | For cards like Voodoo that run fullscreen 3D only. idx is the order DirectX enumerates its driver using DirectDrawEnumerateEx(). This number starts at 1. This will force Java3D to use the driver specified by the user (may fail if the driver is not compatible with display). The driver number and details can be found by using the j3d.debug property. For a typical setup of a 3D only card attach to a graphics card in a single monitor system, use idx=2. This will automatically toggle to fullscreen hardware accelerated mode since if the 3D card support 3D only. |
| `j3d.debug`               | true or false                                             | 1.1             | Prints out startup and running information. Useful for finding out information about the underlying hardware setup. |
| `j3d.fullscreen`          | `PREFERRED` or `REQUIRED` or `UNNECESSARY`                | 1.2             | Option to force Java3D to run in fullscreen mode for video cards that will only use hardware accelaration when using fullscreen (non-windowed) mode, like the older Voodoo series. |
| `j3d.vertexbuffer`        | true or false                                             | 1.2             | false to turn off the use of vertex buffers (a D3D performance enhancing feature equivalent to OpenGL display lists). Some drivers have implementation problems so it might be worth turning this off if you get crashes. Utility Classes |
| `j3d.audiodevice`         | A quote string containing a class name                    | 1.3.2           | SimpleUniverse utility classes. Takes the name of a concrete subclass of com.sun.j3d.audioengines.AudioEngine3DL2 that will be constructed by Viewer.createAudioDevice(). The default value is null, which means that audio is disabled by default for applications that call Viewer.createAudioDevice(). j3d.configURL Unknown 1.3.1 Found in the ConfiguredUniverse class. Functionality unknown currently. |
| `j3d.io.ImageCompression` | `None` or `GZIP` or `JPEG`                                | 1.3.1           | Found in the scenegraph I/O package. Functionality unknown currently. |
| `j3d.stereo`              | `PREFERRED` or `REQUIRED`                                 | 1.1             | Only used by SimpleUniverse. If you roll your own VirtualUniverse, this property is not used. Controls whether you want Java3D to definitely create stereo mode capable canvases or not |
| `sun.java2d.d3d`          | true or false                                             | ??              | Default true. Enable Direct3D in Java 2D (not Java 3D, actually). |
| `sun.java2d.ddoffscreen`  | true or false                                             | ??              | Default true. Enable DirectDraw and Direct3D by Java 2D for off screen images, such as the Swing back buffer (not Java 3D, actually). |
| `sun.java2d.noddraw`      | true or false                                             | ??              | Default false. Completely disable DirectDraw and Direct3D by Java 2D (not Java 3D, actually). This avoids any problems associated with use of these APIs and their respective drivers. |

