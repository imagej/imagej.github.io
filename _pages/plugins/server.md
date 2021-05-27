---
mediawiki: ImageJ_Server
title: ImageJ Server
categories: [SciJava, software]
---


{% capture source%}
{% include github org='imagej' repo='imagej-server' %}
{% endcapture %}
{% include notice icon="info" content='Plugin' software='ImageJ' name='ImageJ Server' author='ImageJ developers' maintainer='ImageJ developers' status='Experimental' source=source %}The ImageJ Server is an extension and [update site](/update-sites) for ImageJ that enables ImageJ to act as a {% include wikipedia title='Representational state transfer' text='RESTful'%} image server.

Client software can:

-   Send images to, and receive images from, the server.
-   Discover and execute ImageJ modules.

## Installation

-   [Enable](/update-sites/following) the Server [update site](/update-sites).
-   Start the server via the {% include bc path='Plugins | Utilities | Start Server'%} command.
-   Or launch ImageJ in server mode using the `--server` flag.

## Documentation

See the {% include github org='imagej' repo='imagej-server' label='GitHub site' %}.
