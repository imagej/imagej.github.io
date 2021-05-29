---
mediawiki: Dynamic_ROI_Profiler
title: Dynamic ROI Profiler
categories: [Scripting,Unmaintained]
---


{% capture source%}
{% include github repo='fiji' path='plugins/Analyze/Dynamic\_ROI\_Profiler.clj' %}
{% endcapture %}
{% include info-box name='Dynamic ROI Profiler' software='Clojure' author='Albert Cardona' maintainer='' filename='Dynamic\_ROI\_Profiler.clj' source=source latest-version='16 November 2008' status='unknown' %}

Dynamically updates a profile plot for an image with a line, freeline, polyline or a rectangular ROI, as the ROI is moved across the image. Written in [Clojure](/scripting/clojure).

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td>
        <p>style="vertical-align:top" |{% include thumbnail src='/media/plugins/profiler-movie.gif' title='Dragging a line ROI across an image shows the pixel intensity profile across that line in a separate image window.'%}</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

  
