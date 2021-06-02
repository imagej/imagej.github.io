---
mediawiki: 2015-12-22_-_The_road_to_Java_8
title: 2015-12-22 - The road to Java 8
---

<div style="float: right; padding-left: 1em">
</div>

For {% include github org='imagej' repo='imagej' issue='135' label='many reasons' %}, ImageJ needs to switch to Java 8. Hence, in recent months, the ImageJ team at [LOCI](/orgs/loci) has been [taking steps toward migrating ImageJ and Fiji toward Java 8](/news/2015-06-15-major-updates-in-the-works). This week marks a significant milestone in that effort:

1.  Several ImageJ and Fiji components migrated to Java 7 or 8; and
2.  A new Java-8 [update site](/update-sites) was created, which offers the latest releases of these components.

## Key points about ImageJ's Java 8 migration strategy

1.  Individual ImageJ and Fiji components are being migrated to Java 7 or Java 8 as needed (see below for a current list).
2.  The **ImageJ** and **Fiji** update site will continue to ship the final Java-6-compatible versions of these components.
3.  Updates for components which require Java 7 or 8 will be provided using the new **Java-8** update site—not the **ImageJ** or **Fiji** update sites.

## How to update

-   If you **still need Java 6, do nothing.**
    -   You will keep receiving updates of the latest Java-6-compatible component versions.
    -   But you will no longer receive updates for components which have migrated to Java 7 or 8.
-   If you **want the latest updates**, [update your ImageJ installation to use Java 8](/learn/faq#how-do-i-launch-imagej-with-a-different-version-of-java) and then [enable the Java-8 update site](/update-sites/following).
    -   **Make sure you switch your ImageJ over to Java 8 *before* enabling the Java-8 update site!**

## Components which have already migrated

The following ImageJ and Fiji components now require a minimum Java version of Java 7 or Java 8:

{::nomarkdown}
<table>
  <thead>
    <tr class="header">
      <th>
        <p>Component</p>
      </th>
      <th>
        <p>Requires</p>
      </th>
      <th>
        <p>Why?</p>
      </th>
      <th>
        <p>Latest version</p>
      </th>
      <th>
        <p>Final Java 6 version</p>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <p><a href="/software/imagej2">ImageJ2</a></p>
      </td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>
        <p><a href="/libs/imagej-ops">imagej-ops</a></p>
      </td>
      <td>
        <p>Java 8</p>
      </td>
      <td>
        <p>See {% include github org='imagej' repo='imagej-ops' commit='0137b89b5265a1cd6a26ffbe1b36d1e6e2ccdbeb' label='0137b89b' %}</p>
      </td>
      <td>
        <p>{% include github org='imagej' repo='imagej-ops' tag='imagej-ops-0.24.1' label='0.24.1' %}</p>
      </td>
      <td>
        <p>{% include github org='imagej' repo='imagej-ops' tag='imagej-ops-0.23.0' label='0.23.0' %}</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>{% include github org='imagej' repo='imagej-ui-swing' label='imagej-ui-swing' %}</p>
      </td>
      <td>
        <p>Java 8</p>
      </td>
      <td>
        <p>Depends on imagej-ops</p>
      </td>
      <td>
        <p>{% include github org='imagej' repo='imagej-ui-swing' tag='imagej-ui-swing-0.17.1' label='0.17.1' %}</p>
      </td>
      <td>
        <p>{% include github org='imagej' repo='imagej-ui-swing' tag='imagej-ui-swing-0.16.0' label='0.16.0' %}</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><a href="/software/imagej2">imagej</a></p>
      </td>
      <td>
        <p>Java 8</p>
      </td>
      <td>
        <p>Depends on imagej-ops</p>
      </td>
      <td>
        <p>{% include github org='imagej' repo='imagej' tag='imagej-2.0.0-rc-44' label='2.0.0-rc-44' %}</p>
      </td>
      <td>
        <p>{% include github org='imagej' repo='imagej' tag='imagej-2.0.0-rc-43' label='2.0.0-rc-43' %}</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><a href="/software/fiji">Fiji</a></p>
      </td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>
        <p><a href="/libs/imglib1">legacy-imglib1</a></p>
      </td>
      <td>
        <p>Java 7</p>
      </td>
      <td>
        <p>Depends on mines-jtk</p>
      </td>
      <td>
        <p>{% include github org='fiji' repo='legacy-imglib1' tag='legacy-imglib1-1.1.5' label='1.1.5' %}</p>
      </td>
      <td>
        <p>{% include github org='fiji' repo='legacy-imglib1' tag='legacy-imglib1-1.1.4-DEPRECATED' label='1.1.4-DEPRECATED' %}</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><a href="/plugins/3d-blob-segmentation">3D_Blob_Segmentation</a></p>
      </td>
      <td>
        <p>Java 7</p>
      </td>
      <td>
        <p>Depends on 3D_Viewer</p>
      </td>
      <td>
        <p>{% include github org='fiji' repo='3D_Blob_Segmentation' tag='3D_Blob_Segmentation-3.0.0' label='3.0.0' %}</p>
      </td>
      <td>
        <p>{% include github org='fiji' repo='3D_Blob_Segmentation' tag='3D_Blob_Segmentation-2.0.2' label='2.0.2' %}</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><a href="/plugins/3d-viewer">3D_Viewer</a></p>
      </td>
      <td>
        <p>Java 7</p>
      </td>
      <td>
        <p>Depends on {% include github org='scijava' repo='java3d-core' label='j3dcore' %} and {% include github org='scijava' repo='java3d-core' label='j3dutils' %}</p>
      </td>
      <td>
        <p>{% include github org='fiji' repo='3D_Viewer' tag='3D_Viewer-4.0.1' label='4.0.1' %}</p>
      </td>
      <td>
        <p>{% include github org='fiji' repo='3D_Viewer' tag='3D_Viewer-3.1.0' label='3.1.0' %}</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><a href="/plugins/descriptor-based-registration-2d-3d">Descriptor_based_registration</a></p>
      </td>
      <td>
        <p>Java 7</p>
      </td>
      <td>
        <p>Depends on SPIM_Registration, mines-jtk, {% include github org='scijava' repo='java3d-core' label='j3dcore' %}</p>
      </td>
      <td>
        <p>{% include github org='fiji' repo='Descriptor_based_registration' tag='Descriptor_based_registration-2.0.12' label='2.0.12' %}</p>
      </td>
      <td>
        <p>{% include github org='fiji' repo='Descriptor_based_registration' tag='Descriptor_based_registration-2.0.11' label='2.0.11' %}</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Fiji_Developer</p>
      </td>
      <td>
        <p>Java 8</p>
      </td>
      <td>
        <p>Depends on imagej-ui-swing</p>
      </td>
      <td>
        <p>{% include github org='fiji' repo='Fiji_Developer' tag='Fiji_Developer-2.0.4' label='2.0.4' %}</p>
      </td>
      <td>
        <p>{% include github org='fiji' repo='Fiji_Developer' tag='Fiji_Developer-2.0.3' label='2.0.3' %}</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><a href="/plugins/multiview-reconstruction">SPIM_Registration</a></p>
      </td>
      <td>
        <p>Java 7</p>
      </td>
      <td>
        <p>Depends on 3D_Viewer, {% include github org='scijava' repo='java3d-core' label='j3dcore' %}, {% include github org='scijava' repo='java3d-core' label='j3dutils' %}, legacy-imglib1</p>
      </td>
      <td>
        <p>{% include github org='fiji' repo='SPIM_Registration' tag='SPIM_Registration-4.0.0' label='4.0.0' %}</p>
      </td>
      <td>
        <p>{% include github org='fiji' repo='SPIM_Registration' tag='SPIM_Registration-3.0.5' label='3.0.5' %}</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><a href="/plugins/snt">Simple_Neurite_Tracer</a></p>
      </td>
      <td>
        <p>Java 7</p>
      </td>
      <td>
        <p>Depends on 3D_Viewer, {% include github org='scijava' repo='java3d-core' label='j3dcore' %}, {% include github org='scijava' repo='java3d-core' label='j3dutils' %}</p>
      </td>
      <td>
        <p>{% include github org='fiji' repo='Simple_Neurite_Tracer' tag='Simple_Neurite_Tracer-3.0.0' label='3.0.0' %}</p>
      </td>
      <td>
        <p>{% include github org='fiji' repo='Simple_Neurite_Tracer' tag='Simple_Neurite_Tracer-2.0.4' label='2.0.4' %}</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><a href="/plugins/trackmate">TrackMate_</a></p>
      </td>
      <td>
        <p>Java 7</p>
      </td>
      <td>
        <p>Depends on 3D_Viewer, {% include github org='scijava' repo='java3d-core' label='j3dcore' %}, {% include github org='scijava' repo='java3d-core' label='j3dutils' %}</p>
      </td>
      <td>
        <p>{% include github org='fiji' repo='TrackMate' tag='TrackMate_-3.0.0' label='3.0.0' %}</p>
      </td>
      <td>
        <p>{% include github org='fiji' repo='TrackMate' tag='TrackMate_-2.8.1' label='2.8.1' %}</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><a href="/plugins/tws">Trainable_Segmentation</a></p>
      </td>
      <td>
        <p>Java 7</p>
      </td>
      <td>
        <p>Depends on mines-jtk</p>
      </td>
      <td>
        <p>{% include github org='fiji' repo='Trainable_Segmentation' tag='Trainable_Segmentation-3.0.0' label='3.0.0' %}</p>
      </td>
      <td>
        <p>{% include github org='fiji' repo='Trainable_Segmentation' tag='Trainable_Segmentation-2.3.0' label='2.3.0' %}</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><a href="/plugins/fijiarchipelago#trakem2-archipelago">TrakEM2_Archipelago</a></p>
      </td>
      <td>
        <p>Java 7</p>
      </td>
      <td>
        <p>Depends on Simple_Neurite_Tracer, legacy-imglib1 (via TrakEM2)</p>
      </td>
      <td>
        <p>{% include github org='fiji' repo='TrakEM2_Archipelago' tag='TrakEM2_Archipelago-2.0.1' label='2.0.1' %}</p>
      </td>
      <td>
        <p>{% include github org='fiji' repo='TrakEM2_Archipelago' tag='TrakEM2_Archipelago-2.0.0' label='2.0.0' %}</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><a href="/plugins/vib-protocol">VIB_</a></p>
      </td>
      <td>
        <p>Java 7</p>
      </td>
      <td>
        <p>Depends on 3D_Viewer, {% include github org='scijava' repo='java3d-core' label='j3dcore' %}, {% include github org='scijava' repo='java3d-core' label='j3dutils' %}</p>
      </td>
      <td>
        <p>{% include github org='fiji' repo='VIB' tag='VIB_-3.0.0' label='3.0.0' %}</p>
      </td>
      <td>
        <p>{% include github org='fiji' repo='VIB' tag='VIB_-2.0.3' label='2.0.3' %}</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><a href="/plugins/volume-calculator">Volume Calculator</a></p>
      </td>
      <td>
        <p>Java 7</p>
      </td>
      <td>
        <p>Depends on 3D_Viewer, {% include github org='scijava' repo='java3d-core' label='j3dcore' %}, {% include github org='scijava' repo='java3d-core' label='j3dutils' %}</p>
      </td>
      <td>
        <p>{% include github org='fiji' repo='Volume_Calculator' tag='Volume_Calculator-2.0.0' label='2.0.0' %}</p>
      </td>
      <td>
        <p>{% include github org='fiji' repo='Volume_Calculator' tag='Volume_Calculator-1.0.2' label='1.0.2' %}</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

## Conflicting update sites

It is the responsibility of individual update site maintainers to decide if and when they follow this migration process. The following [update sites](/update-sites) are known to cause conflicts when enabled with the **Java-8** update site. If your workflow requires components from these sites, we do not recommend enabling the **Java-8** update site.

{% include notice icon="note" content="If you are a maintainer of one of these update sites and need any guidance on how to update your project to comply with the **Java-8** update site, please contact us on the [ImageJ forum](/discuss)." %}

|                 |                                        |                                            |                                                                  |
|-----------------|----------------------------------------|--------------------------------------------|------------------------------------------------------------------|
| **Name**        | **Site**                               | **Maintainer**                             | **Issue**                                                        |
| **ClearVolume** | http://sites.imagej.net/ClearVolume/ | [ClearVolume](User_ClearVolume) | [BugZilla \#1209](https://fiji.sc/bugzilla/show_bug.cgi?id=1209) |

## Feedback

Please post any comments to the [ImageJ forum](/discuss). Thank you for the continued feedback and support!

  
