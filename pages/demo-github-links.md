---
title: Demo github links
layout: page
author: 
categories: 
description: this page demonstrates how to use the github include tag
---

Please click on <code>View source</code> to see how this page was written.

Use `path` to link to a file off the repository root:

{% include github path='WELCOME.md' %}

Use `source` to link to a source file within the repository's
`src/main/java` subtree:

{% include github source='net/imagej/ImageJ.java' %}

Use `org` and `repo` to link to a different repository than
`imagej/imagej`:

{% include github org='fiji' repo='TrackMate' path='README.md' %}

You can give just a `repo` (or just an `org`), and it will be used for
both `org` and `repo`:

{% include github repo='fiji' path='plugins/Examples/Fiji_Cube.ijm' %}

If you give neither a `path` nor a `source` then it links to the
repository as a whole:  
{% include github repo='fiji' %}  

Use `tag` to specify a tag (rather than `master`):  
{% include github tag='imagej-2.0.0-beta-7.9' path='app/src/test/java/imagej/debug/TypeHierarchy.java' %}  

Specifying `tag` alone links to the tag description:  
{% include github tag='imagej-2.0.0-rc-44' %}  

Use `commit` to specify a commit hash:  
{% include github commit='7a10880d485a13fc449d84c7e2eca3e1481064ee' label='imagej@7a10880d' %}  

Use `issue` or `pr` to specify an issue or PR number:  
{% include github issue='83' label='imagej\#83' %} {% include github pr='88' label='imagej\#88' %}  

Use `label` to override the label:  
{% include github repo='fiji' path='plugins/Examples/Fiji_Logo_3D.js' label='Fiji...' %}  

It should also work {% include github org='scijava' repo='pom-scijava' label='as an in-line link' %}.