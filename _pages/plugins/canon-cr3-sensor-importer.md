---
title: Canon CR3 Sensor Importer
description: Open Canon CR3 files in Fiji as native Bayer samples, a 16-bit RGB composite or the camera's JPEG preview.
categories: [Import-Export]
name: Canon CR3 Sensor Importer
source-url: https://github.com/carstenartur/Photographer/tree/main/cr3-imagej
license-label: MIT
license-url: https://github.com/carstenartur/Photographer/blob/main/LICENSE
release-url: https://github.com/carstenartur/Photographer/releases/latest
release-version: latest
team-maintainers: 'Carsten Hammer | https://github.com/carstenartur'
update-site: Canon CR3 Sensor Importer
---

Canon CR3 Sensor Importer opens supported Canon RAW and C-RAW files in
[Fiji](/software/fiji). Version 0.1.8 provides two commands under **File › Import**.
Choose **CR3 Sensor Data...** to measure the original Bayer samples or
**CR3 Color Image...** to open a developed image with three 16-bit color channels.
The plugin is part of [Photographer](https://github.com/carstenartur/Photographer).

## Choosing an output

<div class="table-wrapper" markdown="1">

| Output | How to open it | Pixel data |
| --- | --- | --- |
| **Sensor mosaic** | **File › Import › CR3 Sensor Data...** | One Bayer sample per pixel in an unsigned 16-bit image, including the masked sensor margins. Useful for inspecting the decoded sensor values. |
| **Developed RGB** | **File › Import › CR3 Color Image...** | An sRGB composite with three unsigned 16-bit channels, cropped to the active area and oriented using EXIF metadata. Color rendering is experimental. |
| **Camera JPEG** | Run the [Groovy example](#opening-the-camera-jpeg) with **Develop RAW to 16-bit RGB** cleared. | The camera's embedded color preview, when present. |

</div>

The sensor image is displayed in grayscale because each Bayer site holds one
sample under a color filter. It is not a conversion of the camera's color image
to grayscale. For the verified 14-bit layouts, a sample such as `2048` remains
`2048`; 16-bit storage does not add sensor precision or scale the values to fill
the 16-bit range. With C-RAW, these are the samples reconstructed from the
lossy compressed capture.

## Installation

Use **Fiji with Java 21 or later**. [Fiji Latest](/software/fiji/downloads) is the
appropriate starting point; the Java 8 runtime bundled with Fiji Stable cannot
load this plugin.

1. Choose **Help › Update... › Manage update sites**.
2. Enable **Canon CR3 Sensor Importer** in the list.
3. Close the site manager, apply changes and restart Fiji.

If the entry is not listed, choose **Add Unlisted Site**, use the same name and
enter this URL:

```text
https://carstenartur.github.io/Photographer/fiji/cr3/
```

Run **Help › Update...** again to receive later versions. The
[update-site version file](https://carstenartur.github.io/Photographer/fiji/cr3/version.txt)
identifies the current published build. For offline installation, follow the
[ZIP installation instructions](https://github.com/carstenartur/Photographer/blob/main/docs/cr3/fiji-update-site.md#install-from-the-zip).

## Importing a file

Choose **File › Import › CR3 Sensor Data...** and select a CR3 file.
The image retains full sensor coordinates and margins. The importer leaves
black-level subtraction, white balance, cropping, rotation and demosaicing to
subsequent processing.

### Try a sample image

1. Download the original [sample-tele.cr3](https://github.com/carstenartur/Photographer/raw/3780019670b4fe16defee44a6cba57b1a11bc021/canon-cr3-imageio/src/test/resources/samples/sample-tele.cr3)
   from the Photographer sample collection.
2. Open it with **File › Import › CR3 Sensor Data...**. This PowerShot G5 X Mark II
   image opens as a **5632 × 3710**, **16-bit** image containing **14-bit RGGB** samples.
3. Choose **Image › Show Info...** to inspect the camera model, Bayer pattern and
   available calibration metadata.
4. To reproduce the display below, choose **Image › Adjust › Brightness/Contrast... › Set**
   and set the display minimum to **2048** and maximum to **6473**.

Changing the display limits preserves the pixel values. Leave **Apply** unused
when inspecting or measuring the sensor data, and use **Reset** to restore the
display range. Other exposures may need different limits. Move the pointer over
the image to inspect individual pixel values in ImageJ's status bar.

{% include img src="/media/plugins/canon-cr3-sensor-importer.webp" align="center" style="max-width: 100%;"
   alt="ImageJ showing sample-tele.cr3 as a 5632 by 3710 pixel, 16-bit sensor image at 16.7 percent zoom."
   caption="PowerShot G5 X Mark II sensor image with the display range set to 2048–6473. Screenshot from [Photographer's Fiji guide](https://github.com/carstenartur/Photographer/blob/3780019670b4fe16defee44a6cba57b1a11bc021/docs/cr3/fiji-update-site.md), by Carsten Hammer." %}

### Sensor metadata

**Image › Show Info...** displays these properties when they are available in the
capture. Recording a black level or white-balance gain does not apply it to the
imported pixels.

<div class="table-wrapper" markdown="1">

| Property | Meaning |
| --- | --- |
| `CR3.CameraModel` | Camera model. |
| `CR3.BitDepth` | Sensor sample depth, separate from ImageJ's 16-bit storage. |
| `CR3.CFA` | Bayer pattern at the full sensor origin. |
| `CR3.ActiveAreaLTRBInclusive` | Active rectangle: left, top, right, bottom. Coordinates start at zero; both end coordinates are included. |
| `CR3.BlackLevelRGGB` | Black levels in R, green-on-red-row, green-on-blue-row, B order. |
| `CR3.WhiteBalanceGainRGGB` | White-balance gains in the same four-channel order. |
| `CR3.WhiteLevel` | Recorded white level. |

</div>

### Macro import

To import a file from an ImageJ macro:

```ijm
run("CR3 Sensor Data...", "path=[/data/capture.cr3]");
```

Replace the path with your CR3 file. This command opens the sensor mosaic.

## Opening a color image

Choose **File › Import › CR3 Color Image...** and select a supported RAW or
C-RAW file. Fiji opens the developed active area as an EXIF-oriented composite
with red, green and blue planes. Each plane contains unsigned 16-bit sRGB
values and starts with a display range of 0–65535.

An ImageJ macro can open the composite directly:

```ijm
run("CR3 Color Image...", "path=[/data/capture.cr3]");
```

### Opening the camera JPEG

To open the camera's embedded preview, download
[open-cr3-color.groovy](https://carstenartur.github.io/Photographer/fiji/cr3/open-cr3-color.groovy).
Open it in Fiji's [Script Editor](/scripting/script-editor), select **Groovy**,
run the script and choose a CR3 file. Leave **Develop RAW to 16-bit RGB**
cleared for the camera JPEG. Selecting it runs the same 16-bit importer as
the color menu command. The camera JPEG may include the camera's picture
style and other corrections. For installations still using 0.1.7, see the
[earlier 8-bit color script](https://github.com/carstenartur/Photographer/blob/v0.1.7/docs/cr3/fiji-update-site.md#open-a-color-image).

## Memory for an import

The sensor image retains 2 bytes of pixel data per sensor site. The color
composite retains 6 bytes per developed pixel across its three planes. For
example, a 5496 × 3668 composite retains about 115 MiB of pixel data. Decoder
buffers, other open images and rendering the composite need additional memory.

Both RAW menu commands use the decoder's automatic memory policy (`AUTO`).
When the normal read would exceed its estimated Java heap budget, the decoder
selects compact processing and writes one line beginning `CR3 low-memory:` to
standard error. The line reports the worker limit selected for the read. If
the estimated memory needed with one worker still exceeds the budget, the
decoder attempts the import with one worker. This estimate is advisory, and
the final image must fit in memory. Dimensions, orientation and sample precision
are preserved.

## Supported files

The documented verification covers **14-bit, four-plane V1** configurations from
the **Canon EOS R, EOS RP, EOS M50 and PowerShot G5 X Mark II**. The reference panel
contains 15 lossless RAW captures and six three-level C-RAW captures. This
describes the tested files and layouts, rather than every recording mode of
those camera models.

Other sensor depths, V2 CRX and RAW bursts are outside that verified scope.
See the [decoder support and verification notes](https://github.com/carstenartur/Photographer/blob/main/docs/cr3/decoder.md#full-sensor-verification)
for the measurements and current limitations.

## Troubleshooting

<div class="table-wrapper" markdown="1">

| Symptom | What to check |
| --- | --- |
| A CR3 import command is missing | Confirm the update site is enabled, apply its changes and restart Fiji. Check that Fiji is actually running Java 21 or newer. The color menu command requires plugin version 0.1.8 or later. |
| Dark image, grayscale display or visible sensor borders | These can be expected for the full Bayer mosaic. Adjust the display limits as above, or choose **CR3 Color Image...** for a developed view. |
| RAW import reports an unsupported or unreadable layout | Check the supported configurations. The color example can still open an embedded JPEG if one is present and readable; this supplies a preview rather than sensor data. |

</div>

For a reproducible [bug report](https://github.com/carstenartur/Photographer/issues),
include the plugin version, Fiji and Java versions, camera model, RAW/C-RAW mode
and the complete error message.

## For developers

The [minimal Maven and Java example](https://github.com/carstenartur/Photographer/tree/main/examples/cr3-imageio)
reads the Bayer samples and counts distinct sensor values. It demonstrates the
data retained beyond an 8-bit image. Java ImageIO is part of the JDK; the CR3
reader is supplied by the `io.github.carstenartur:cr3-imageio` dependency.

See the [ImageIO guide](https://github.com/carstenartur/Photographer/blob/main/docs/cr3/imageio.md)
for Maven setup, metadata and explicit output selection. Its ordinary
`ImageIO.read(file)` call develops RGB; request `rawSensor()` explicitly to work
with native sensor units. The [ImageJ plugin source](https://github.com/carstenartur/Photographer/tree/main/cr3-imagej),
[releases](https://github.com/carstenartur/Photographer/releases) and
[CR3 format reference](https://github.com/carstenartur/Photographer/blob/main/docs/cr3/format.md)
provide the implementation and technical details.

The color importer uses the exact 16-bit sRGB quantizer. The optional Java 25
SIMD color-matrix acceleration applies to the packed 8-bit RGB ImageIO path.
Both Fiji menu commands work on Java 21 without a vector module flag.
The [ImageJ adapter guide](https://github.com/carstenartur/Photographer/blob/main/docs/developer/modules.md#imagej-adapter)
covers headless calls and ownership of the sensor and color planes.

The [installed-plugin checks](https://github.com/carstenartur/Photographer/blob/main/docs/cr3/fiji-qa-2026-11-19/README.md)
compare full-image fingerprints for four sensor images and four color composites
with the ImageIO references and include two constrained-heap imports. The separate
[complete-import measurements](https://github.com/carstenartur/Photographer/blob/main/docs/cr3/optimization-2026-11-19/README.md)
time ImageIO reads. Opening and rendering Fiji windows are outside those timings.
