---
mediawiki: ClearVolume
title: ClearVolume
categories: [Visualization]
doi: 10.1038/nmeth.3372
---


{% capture author%}
{% include person id='fjug' %}, {% include person id='royerloic' %}, Martin Weigert, {% include person id='skalarproduktraum' %}
{% endcapture %}

{% capture maintainer%}
{% include person id='fjug' %}
{% endcapture %}

{% capture source%}
{% include github org='ClearVolume' repo='imglib2-clearvolume' %}
{% endcapture %}
{% include info-box name='ClearVolume' logo='![](/media/logos/clearvolume.png)' software='Fiji' author=author maintainer=maintainer source=source status='active' category='Visualization' website='https://clearvolume.github.io/' %}== Problems and Solutions == We work constantly on improving the Fiji and KNIME plugins. Help us doing so by letting us know if you encounter problems.

-   **Problem:** on a Linux machine ClearVolume would not start but throw an ugly exception like

    `java.lang.ExceptionInInitializerError at clearvolume.renderer.opencl.OpenCLAvailability...`.
-   **Solution:** you might not have OpenCL installed or your installation is corrupted.

    On Ubuntu the following instructions turned out to be useful for some of our users: [http://askubuntu.com/questions/541114/how-to-make-opencl-work-on-14-10-nvidia-331-89-drivers](http://askubuntu.com/questions/541114/how-to-make-opencl-work-on-14-10-nvidia-331-89-drivers)

<!-- -->

-   **Problem:** on a Mac, after ClearVolume opens in Fiji I see a large grey area where the 3D viewer should be.
-   **Solution:** we work on a fix... so far, double click on the grey area to switch to full screen, then double click again to go back to window mode.

## What is ClearVolume?

{% include testimonial person='komodovaran'
  quote='I checked out ClearVolume. Extremely well-made plugin! Does exactly what I want :)'
  source='http://forum.imagej.net/t/1907/3' %}

ClearVolume is a volume renderer developed at MPI-CBG. Its sources are open and
can be cloned [from GitHub](https://github.com/ClearVolume). If you use
ClearVolume in your research, please cite it—see reference below.

## Screenshots

<center>

<figure><img src="/media/clearvolumeinfiji.png" title="The main ClearVolume plugin can render volumetric multi-channel data. Channel LUTs, transparency, rendering quality, etc. can easily be set in the plugins user interface. We thank Tzumin Lee&#39;s group at Janelia for being allowed to use their twin-spot MARCM (Yu et al., Nature Neuroscience, 2009) labeled neurons." width="750" alt="The main ClearVolume plugin can render volumetric multi-channel data. Channel LUTs, transparency, rendering quality, etc. can easily be set in the plugins user interface. We thank Tzumin Lee&#39;s group at Janelia for being allowed to use their twin-spot MARCM (Yu et al., Nature Neuroscience, 2009) labeled neurons." /><figcaption aria-hidden="true">The main ClearVolume plugin can render volumetric multi-channel data. Channel LUTs, transparency, rendering quality, etc. can easily be set in the plugins user interface. We thank Tzumin Lee's group at Janelia for being allowed to use their twin-spot MARCM (Yu et al., Nature Neuroscience, 2009) labeled neurons.</figcaption></figure>

</center>
<center>

<figure><img src="/media/plugins/clearvolumenetworkclientinfiji.png" title="The ClearVolume network client can be started from Fiji/ImageJ2 and enables users to receive volumetric data from a remote source, e.g. live from a microscope in the basement of your collaborators institute." width="750" alt="The ClearVolume network client can be started from Fiji/ImageJ2 and enables users to receive volumetric data from a remote source, e.g. live from a microscope in the basement of your collaborators institute." /><figcaption aria-hidden="true">The ClearVolume network client can be started from Fiji/ImageJ2 and enables users to receive volumetric data from a remote source, e.g. live from a microscope in the basement of your collaborators institute.</figcaption></figure>

</center>

See ClearVolume in action!

{% include video platform='youtube' id='IyUpkgTJJvc' %}
