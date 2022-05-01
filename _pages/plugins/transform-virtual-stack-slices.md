---
mediawiki: Transform_Virtual_Stack_Slices
title: Transform Virtual Stack Slices
categories: [Uncategorized]
---


{% capture author%}
{% include person id='iarganda' %}, Albert Cardona and Stephan Saalfeld
{% endcapture %}

{% capture maintainer%}
{% include person id='iarganda' %}
{% endcapture %}

{% capture filename%}
{% include maven g='sc.fiji' a='register_virtual_stack_slices' %}
{% endcapture %}

{% capture source%}
{% include github org='fiji' repo='register_virtual_stack_slices' %}
{% endcapture %}
{% include info-box name='Transform Virtual Stack Slices' software='Fiji' author=author maintainer=maintainer filename=filename source=source released='September 24<sup>th</sup>, 2009' latest-version='3.0.0, February 17<sup>th</sup>, 2016' status='stable, active' category='Registration, Transform' %}{\| \|style="vertical-align:top" \| <img src="/media/plugins/transform-virtual-stack-scheme.png" title="fig:Transform Virtual Stack scheme - All images are transformed based on the XML files" width="381" alt="Transform Virtual Stack scheme - All images are transformed based on the XML files" /> \|}

This plugin takes a sequence of image slices stored in a folder, and delivers a list of transformed image slices (with enlarged canvas) applying a list of transforms stored as **.XML** files in another folder.

This is a **complementary plugin** of [Register Virtual Stack Slices](/plugins/register-virtual-stack-slices). It allows reproducing the results of [Register Virtual Stack Slices](/plugins/register-virtual-stack-slices) by loading the corresponding transform files (saved by checking the option [ "Save transforms"](/plugins/register-virtual-stack-slices#save-transforms) in the main dialog).

## User Manual

**Premises**:

-   **Source folder**: You have a folder with an ordered list of image files in it that Fiji can open.
-   Each image represents a slice in a sequence.
-   **Output folder**: You have or create a folder to store the resulting virtual stack with the transformed images.
-   **Transform folder**: You have a folder with the transform files (from a [Register Virtual Stack Slices](/plugins/register-virtual-stack-slices) execution).
-   **Interpolate**: Toggle the interpolation for the result images.

**Step 1**: launch the "Plugins - Transform - Transform Virtual Stack Slices" plugin. {% include thumbnail src='/media/plugins/main-dialog-transform-virtual-stack.png' title='Transform Virtual Stack main dialog'%} **Step 2**: choose the source, output and transform folders:

-   Select a source folder containing the slices, at one slice per image file.
-   Select the target folder where resulting transformed slices will be automatically stored as TIFF files.
-   Select the transform folder, where the .XML files from a [Register Virtual Stack Slices](/plugins/register-virtual-stack-slices) are stored.

**Results**: on success, a virtual stack will open showing all the transformed images contained in the output folder. The virtual stack can be closed with no ill effect: images are saved in the output folder.

## API documentation

The latest documentation of the package can be found here:

[https://fiji.sc/javadoc/register_virtual_stack/package-summary.html](https://fiji.sc/javadoc/register_virtual_stack/package-summary.html)

## License

This program is **free software**; you can redistribute it and/or modify it under the terms of the **GNU General Public License** as published by the Free Software Foundation ([http://www.gnu.org/licenses/gpl.txt](http://www.gnu.org/licenses/gpl.txt)).

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

  
