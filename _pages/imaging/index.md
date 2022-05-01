---
title: Scientific Imaging Tutorials
section: Learn:Scientific Imaging
nav-links: true
nav-title: Overview
---

This section is an introduction to scientific imaging, including both
image acquisition and image analysis, with a focus on ImageJ.

Cooks call them *recipes*, biologists *protocols*, and programmers call them
*HOWTOs*. No matter how you refer to them, you'll find all the topics in the
nav-bar at the top of the page!

Like the rest of this wiki, this guide is a community project.
Please feel welcome to [edit and expand](/editing) the material here!

{% include notice content="If you are new to scientific imaging,
  *please peruse the [Principles](/imaging/principles)* for a primer!" %}

## Installation

Some parts of this guide describe plugins from the [Fiji](/software/fiji)
distribution of ImageJ, as well as from the
[Cookbook update site](/update-sites/cookbook). Here's how to set it up:

<style>
  .cookbook-install-table { width: auto; }
  .cookbook-install-table img { max-width: 400px; max-height: 200px; }
</style>

| 1. | [Download and install](/software/fiji/downloads) the Fiji distribution of ImageJ. |                                               |
| 2. | From the Fiji menu, select {% include bc path='Help | Update...' %}               | {% include img src="1-update-fiji" %}         |
| 3. | Click {% include button label="Manage update sites" %}                            | {% include img src="2-manage-update-sites" %} |
| 4. | Check the **Cookbook** update site                                                | {% include img src="3-enable-cookbook" %}     |
| 5. | Click {% include button label="Close" %}                                          |                                               |
| 6. | Click {% include button label="Apply changes" %} to download the Cookbook plugins | {% include img src="4-apply-changes" %}       |
| 7. | Restart Fiji to complete the plugin installation                                  |                                               |
| 8. | Enjoy your new plugins from the **Cookbook** menu!                                | {% include img src="5-use-the-cookbook" %}    |
{:.cookbook-install-table}

## Source

The source code of the Cookbook plugins can be found
{% include github org='fiji' repo='cookbook' label='on GitHub' %}.

## Credits

Many of the pages in this section were adapted from the defunct
[MBF "ImageJ for microscopy" manual](/software/mbf-imagej), originally
created by Tony Collins, which went offline in November 2012.

The Cookbook technical writer team includes:

-   {% include person id='ctrueden' %} (technical oversight and maintenance)
-   {% include person id='apal4' %} (January 2014 - May 2015)
-   {% include person id='dscho' %} (June 2013 - November 2014)
-   {% include person id='kghildebrand' %} (June 2013 - December 2013)
-   {% include person id='amanda-macallister' %} (June 2013 - December 2013)
-   {% include person id='RuizhiLiao' %} (November 2013 - December 2013)
-   {% include person id='gabby-campagnola' %} (June 2013 - August 2013)

The plugins featured in the Cookbook were collated from various sources and
have various authors and licenses.
