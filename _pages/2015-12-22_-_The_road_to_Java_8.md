<div style="float: right; padding-left: 1em">__TOC__</div>
For {{GitHub | org=imagej | repo=imagej | issue=135 | label=many reasons}}, ImageJ needs to switch to Java 8. Hence, in recent months, the ImageJ team at [[LOCI]] has been [[2015-06-15 - Major updates in the works|taking steps toward migrating ImageJ and Fiji toward Java 8]]. This week marks a significant milestone in that effort:

# Several ImageJ and Fiji components migrated to Java 7 or 8; and
# A new Java-8 [[update site]] was created, which offers the latest releases of these components.

== Key points about ImageJ's Java 8 migration strategy ==

# Individual ImageJ and Fiji components are being migrated to Java 7 or Java 8 as needed (see below for a current list).
# The '''ImageJ''' and '''Fiji''' update site will continue to ship the final Java-6-compatible versions of these components.
# Updates for components which require Java 7 or 8 will be provided using the new '''Java-8''' update site—not the '''ImageJ''' or '''Fiji''' update sites.

== How to update ==

* If you '''still need Java 6, do nothing.'''
** You will keep receiving updates of the latest Java-6-compatible component versions.
** But you will no longer receive updates for components which have migrated to Java 7 or 8.
* If you '''want the latest updates''', [[FAQ#How_do_I_launch_ImageJ_with_a_different_version_of_Java.3F|update your ImageJ installation to use Java 8]] and then [[How to follow a 3rd party update site|enable the Java-8 update site]].
** '''Make sure you switch your ImageJ over to Java 8 ''before'' enabling the Java-8 update site!'''

== Components which have already migrated ==

The following ImageJ and Fiji components now require a minimum Java version of Java 7 or Java 8:

{| class="program"
! Component
! Requires
! Why?
! Latest version
! Final Java 6 version
|-
| colspan=5 class="section-minor" | [[ImageJ2]]
|-
| [[ImageJ Ops|imagej-ops]]
| Java 8
| See {{GitHub | org=imagej | repo=imagej-ops | commit=0137b89b5265a1cd6a26ffbe1b36d1e6e2ccdbeb | label=0137b89b}}
| {{GitHub | org=imagej | repo=imagej-ops | tag=imagej-ops-0.24.1 | label=0.24.1}}
| {{GitHub | org=imagej | repo=imagej-ops | tag=imagej-ops-0.23.0 | label=0.23.0}}
|-
| {{GitHub | org=imagej | repo=imagej-ui-swing | label=imagej-ui-swing}}
| Java 8
| Depends on imagej-ops
| {{GitHub | org=imagej | repo=imagej-ui-swing | tag=imagej-ui-swing-0.17.1 | label=0.17.1}}
| {{GitHub | org=imagej | repo=imagej-ui-swing | tag=imagej-ui-swing-0.16.0 | label=0.16.0}}
|-
| [[ImageJ2|imagej]]
| Java 8
| Depends on imagej-ops
| {{GitHub | org=imagej | repo=imagej | tag=imagej-2.0.0-rc-44 | label=2.0.0-rc-44}}
| {{GitHub | org=imagej | repo=imagej | tag=imagej-2.0.0-rc-43 | label=2.0.0-rc-43}}
|-
| colspan=5 class="section-minor" | [[Fiji]]
|-
| [[ImgLib1|legacy-imglib1]]
| Java 7
| Depends on mines-jtk
| {{GitHub | org=fiji | repo=legacy-imglib1 | tag=legacy-imglib1-1.1.5 | label=1.1.5}}
| {{GitHub | org=fiji | repo=legacy-imglib1 | tag=legacy-imglib1-1.1.4-DEPRECATED | label=1.1.4-DEPRECATED}}
|-
| [[3D Blob Segmentation|3D_Blob_Segmentation]]
| Java 7
| Depends on 3D_Viewer
| {{GitHub | org=fiji | repo=3D_Blob_Segmentation | tag=3D_Blob_Segmentation-3.0.0 | label=3.0.0}}
| {{GitHub | org=fiji | repo=3D_Blob_Segmentation | tag=3D_Blob_Segmentation-2.0.2 | label=2.0.2}}
|-
| [[3D Viewer|3D_Viewer]]
| Java 7
| Depends on {{GitHub | org=scijava | repo=java3d-core | label=j3dcore}} and {{GitHub | org=scijava | repo=java3d-core | label=j3dutils}}
| {{GitHub | org=fiji | repo=3D_Viewer | tag=3D_Viewer-4.0.1 | label=4.0.1}}
| {{GitHub | org=fiji | repo=3D_Viewer | tag=3D_Viewer-3.1.0 | label=3.1.0}}
|-
| [[Descriptor-based registration (2d/3d)|Descriptor_based_registration]]
| Java 7
| Depends on SPIM_Registration, mines-jtk, {{GitHub | org=scijava | repo=java3d-core | label=j3dcore}}
| {{GitHub | org=fiji | repo=Descriptor_based_registration | tag=Descriptor_based_registration-2.0.12 | label=2.0.12}}
| {{GitHub | org=fiji | repo=Descriptor_based_registration | tag=Descriptor_based_registration-2.0.11 | label=2.0.11}}
|-
| Fiji_Developer
| Java 8
| Depends on imagej-ui-swing
| {{GitHub | org=fiji | repo=Fiji_Developer | tag=Fiji_Developer-2.0.4 | label=2.0.4}}
| {{GitHub | org=fiji | repo=Fiji_Developer | tag=Fiji_Developer-2.0.3 | label=2.0.3}}
|-
| [[Multiview-Reconstruction|SPIM_Registration]]
| Java 7
| Depends on 3D_Viewer, {{GitHub | org=scijava | repo=java3d-core | label=j3dcore}}, {{GitHub | org=scijava | repo=java3d-core | label=j3dutils}}, legacy-imglib1
| {{GitHub | org=fiji | repo=SPIM_Registration | tag=SPIM_Registration-4.0.0 | label=4.0.0}}
| {{GitHub | org=fiji | repo=SPIM_Registration | tag=SPIM_Registration-3.0.5 | label=3.0.5}}
|-
| [[Simple Neurite Tracer|Simple_Neurite_Tracer]]
| Java 7
| Depends on 3D_Viewer, {{GitHub | org=scijava | repo=java3d-core | label=j3dcore}}, {{GitHub | org=scijava | repo=java3d-core | label=j3dutils}}
| {{GitHub | org=fiji | repo=Simple_Neurite_Tracer | tag=Simple_Neurite_Tracer-3.0.0 | label=3.0.0}}
| {{GitHub | org=fiji | repo=Simple_Neurite_Tracer | tag=Simple_Neurite_Tracer-2.0.4 | label=2.0.4}}
|-
| [[TrackMate|TrackMate_]]
| Java 7
| Depends on 3D_Viewer, {{GitHub | org=scijava | repo=java3d-core | label=j3dcore}}, {{GitHub | org=scijava | repo=java3d-core | label=j3dutils}}
| {{GitHub | org=fiji | repo=TrackMate | tag=TrackMate_-3.0.0 | label=3.0.0}}
| {{GitHub | org=fiji | repo=TrackMate | tag=TrackMate_-2.8.1 | label=2.8.1}}
|-
| [[Trainable Weka Segmentation|Trainable_Segmentation]]
| Java 7
| Depends on mines-jtk
| {{GitHub | org=fiji | repo=Trainable_Segmentation | tag=Trainable_Segmentation-3.0.0 | label=3.0.0}}
| {{GitHub | org=fiji | repo=Trainable_Segmentation | tag=Trainable_Segmentation-2.3.0 | label=2.3.0}}
|-
| [[Fiji Archipelago#TrakEM2_Archipelago|TrakEM2_Archipelago]]
| Java 7
| Depends on Simple_Neurite_Tracer, legacy-imglib1 (via TrakEM2)
| {{GitHub | org=fiji | repo=TrakEM2_Archipelago | tag=TrakEM2_Archipelago-2.0.1 | label=2.0.1}}
| {{GitHub | org=fiji | repo=TrakEM2_Archipelago | tag=TrakEM2_Archipelago-2.0.0 | label=2.0.0}}
|-
| [[VIB Protocol|VIB_]]
| Java 7
| Depends on 3D_Viewer, {{GitHub | org=scijava | repo=java3d-core | label=j3dcore}}, {{GitHub | org=scijava | repo=java3d-core | label=j3dutils}}
| {{GitHub | org=fiji | repo=VIB | tag=VIB_-3.0.0 | label=3.0.0}}
| {{GitHub | org=fiji | repo=VIB | tag=VIB_-2.0.3 | label=2.0.3}}
|-
| [[Volume Calculator]]
| Java 7
| Depends on 3D_Viewer, {{GitHub | org=scijava | repo=java3d-core | label=j3dcore}}, {{GitHub | org=scijava | repo=java3d-core | label=j3dutils}}
| {{GitHub | org=fiji | repo=Volume_Calculator | tag=Volume_Calculator-2.0.0 | label=2.0.0}}
| {{GitHub | org=fiji | repo=Volume_Calculator | tag=Volume_Calculator-1.0.2 | label=1.0.2}}
|}

== Conflicting update sites ==

It is the responsibility of individual update site maintainers to decide if and when they follow this migration process. The following [[update sites]] are known to cause conflicts when enabled with the '''Java-8''' update site. If your workflow requires components from these sites, we do not recommend enabling the '''Java-8''' update site.

''Note:'' if you are a maintainer of one of these update sites and need any guidance on how to update your project to comply with the '''Java-8''' update site, please contact us on the [[Help|ImageJ forum]].

{| class="wikitable"
|-
|style="vertical-align: bottom;"|'''Name'''
|style="vertical-align: bottom;"|'''Site'''
|style="vertical-align: bottom;"|'''Maintainer'''
|style="vertical-align: bottom;"|'''Issue'''
|- valign="top"
|'''ClearVolume'''
|http://sites.imagej.net/ClearVolume/
|[[User:ClearVolume|ClearVolume]]
|[https://fiji.sc/bugzilla/show_bug.cgi?id=1209 BugZilla #1209]
|}

== Feedback ==

Please post any comments to the [[Help|ImageJ forum]]. Thank you for the continued feedback and support!

[[Category:ImageJ2]]
[[Category:Fiji]]
[[Category:News]]
