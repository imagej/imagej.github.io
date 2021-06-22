---
mediawiki: Neuroanatomy
title: Neuroanatomy
categories: [Uncategorized]
project: /software/fiji
---

{% capture author%}
{% include person id='tferr' %}
{% endcapture %}

{% capture maintainer%}
{% include person id='tferr' %}
{% endcapture %}

{% capture source%}
{% include github org='morphonets' %}
{% endcapture %}
{% include info-box software='Fiji' name='Neuroanatomy update site' author=author maintainer=maintainer source=source status='Active' category='Plugins, Analysis, Neuroanatomy' %} The Neuroanatomy update site is used for distribution of [SNT](/plugins/snt). A few other (legacy) plugins for *Image Processing for NeuroAnatomy and Tree-like Structures* are also included.

# Installation

The requirements to run the Neuroanatomy suite of plugins are twofold: i) [Fiji](/software/fiji) (i.e., an ImageJ installation subscribed to the Fiji update site) running at least Java 8. If you are running an older version of Java, you can either i) [Download the latest Fiji release](/software/fiji/downloads) (newer releases come pre-bundled with Java 8); or ii) If you have downloaded Fiji while ago and want to keep your existing installation, you will have to download Java 8 and make your [Fiji installation aware of it](/learn/troubleshooting#checking-the-java-version).

**Subscribing to the Neuroanatomy update site:**

1.  Run [{% include bc path='Help|Update...'%}](/update-sites)
2.  Click *Manage update sites*
3.  Select the *Neuroanatomy* checkbox (see also [list of update sites](/list-of-update-sites)
)
4.  Click *Apply changes* and Restart ImageJ

## Notes

SNT has its own [documentation](/plugins/snt). The list of *Image Processing for NeuroAnatomy and Tree-like Structures* ({% include github org='tferr' repo='hIPNAT' label='source' %}) is as follows:

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td>
        <p><strong>Name</strong></p>
      </td>
      <td>
        <p><strong>Menu Path</strong></p>
      </td>
      <td>
        <p><strong>Description</strong></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><em>Topological Skeletons</em></p>
      </td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>
        <p>Strahler classifier</p>
      </td>
      <td>
        <p>{% include bc path='Analyze|Skeleton|Strahler Analysis...'%}</p>
      </td>
      <td>
        <p>Described in <a href="/plugins/strahler-analysis">Strahler Analysis</a>. Implemented as a {% include github org='tferr' repo='hIPNAT' branch='master' path='src/main/java/ipnat/skel' label='Java plugin' %}.</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Summarize Skeleton</p>
      </td>
      <td>
        <p>{% include bc path='Analyze|Skeleton|Summarize Skeleton'%}</p>
      </td>
      <td>
        <p>Bulk statistics of skeletonized images. Implemented as a {% include github org='tferr' repo='hIPNAT' branch='master' path='src/main/java/ipnat/skel' label='Java plugin' %}.</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Particles classifier</p>
      </td>
      <td>
        <p>{% include bc path='Analyze|Skeleton|Classify Particles Using Skeleton'%}</p>
      </td>
      <td>
        <p>Tags particles according to skeleton features. Detects maxima on a masked image and clusters detected maxima using features of the skeletonized mask. A maxima is considered to be associated to a skeleton feature (e.g., a junction or end-point, see <a href="/plugins/analyze-skeleton">AnalyzeSkeleton</a>) if the distance between its centroid and the feature is less than or equal to a cuttoff ("snap to") distance. Implemented as a {% include github org='tferr' repo='hIPNAT' branch='master' path='src/main/resources/scripts/' label='Python script' %}.</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><em>Utilities</em></p>
      </td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>
        <p>Fractal Trees</p>
      </td>
      <td>
        <p>{% include bc path='File|Open Samples|Fractal Tree'%}</p>
      </td>
      <td>
        <p>Synthetic images (<a href="https://en.wikipedia.org/wiki/L-system">L-System</a> Trees) useful for debugging, testing or prototyping. Implemented as a {% include github org='tferr' repo='hIPNAT' branch='master' path='src/main/java/ipnat/skel' label='Java plugin' %}.</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

# Further information

-   A list of all ImageJ extensions related to the neurosciences can be found on the [list of extensions](/list-of-extensions) page, by filtering to the Neuroanatomy category.
