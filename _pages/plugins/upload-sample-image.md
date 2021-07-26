---
mediawiki: Upload_Sample_Image
title: Upload Sample Image
categories: [Uncategorized]
---


{% capture source%}
{% include github org='imagej' repo='imagej-plugins-commands' branch='master' source='net/imagej/plugins/commands/upload/SampleImageUploader.java' %}
{% endcapture %}
{% include info-box software='ImageJ' name='Upload Sample Image' maintainer='Johannes Schindelin' author='Johannes Schindelin' source=source released='2009-06-11' latest-version='2014-07-01' status='stable' category='Plugins' website='' %}== Upload Sample Image ==

Use the {% include bc path='Help | Upload Sample Image'%} command to upload a file (not just images) meant for the ImageJ developers. You might need to do this e.g. when the file is too large for email attachments, or when you want to accompany a [bug report](/discuss/bugs) with a large image.

To prevent abuse of this facility, access to the uploaded images is restricted to trusted community admins.

If you upload a sample image and would like it to be deleted, just let us know [on the forum](http://forum.imagej.net/) with a post or private message to an admin.


