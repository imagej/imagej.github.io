---
mediawiki: Dynamic_Kymograph
title: Dynamic Kymograph
---


{% capture author%}
{% include person name='Rudy Zhou' %}
{% endcapture %}

{% capture maintainer%}
{% include person name='Rudy Zhou' %}
{% endcapture %}

{% capture source%}
{% include github org='rudyzhou' repo='Dynamic\_Kymograph' %}
{% endcapture %}
{% include info-box name='Dynamic\_Kymograph' software='Fiji' author=author maintainer=maintainer released='26 July 2018' source=source category='[Plugins](/plugin-index)' %}

Dynamic\_Kymograph is a plugin for ImageJ that generates kymographs from stack videos using key-framing and linear interpolation.

## Features

The main features are:

-   Allows user to specify polyline ROIs on multiple frames of a stack video
-   Automatically interpolates between ROIs drawn on different frames
-   Generates a kymograph using the interpolated ROI throughout the stack video

## Download and Usage

See [https://github.com/rudyzhou/Dynamic_Kymograph](https://github.com/rudyzhou/Dynamic_Kymograph) for download and detailed usage instructions.

## Authors

-   Rudy Zhou - \[rudyzhou\](https://github.com/rudyzhou)

## License

This project is licensed under the [GNU General Public License](/licensing/gpl).

## Acknowledgements

Some code used from [Multiple Kymograph Plugin](/plugins/multi-kymograph) by Jens Reitdorf, Arne Seitz, and Johannes Schindelin.
