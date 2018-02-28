{{Infobox
| software               = ImageJ
| name                   = FPBioimage Helper Plugin
| logo                   = [[File:FPB_Logo.png|96px]]
| author                 = [http://fpb.ceb.cam.ac.uk FPBioimage]<br/> Marcus Fantham
| Maintainer             =  Marcus Fantham
| source                 = {{GitHub|org=fpBioimage|repo=FPBioimageHelper-FIJI}}
}}FPBioimage is an interactive tool for viewing volumetric data in the web browser. To quickly share 3D data with your collaborators using FPBioimage, we provide this useful plugin for ImageJ and FIJI.
{{TOC}}

== Installation ==

Add FPBioimage to your 'Update' sites:

# Launch the updater by selecting '''Update''' from the '''Help''' menu.
# Click the '''Manage update sites''' button.
# Tick the '''FPBioimage''' box: [[File:FPB-manage-update-sites.png|700px|center]]
# Click the '''Close''' button. The updater should now want to install or update some files: [[File:FPB-jars-to-update.png|700px|center]]
# Click the '''Apply changes''' button.
# Restart Fiji when prompted.

=== Manual Installation ===

If you want to install FPBioimage manually, copy the [https://github.com/fpBioImage/FPBioimageHelper-FIJI/releases|latest .jar release] to the Fiji/plugins folder. 

== Usage ==

FPBioimage Helper will appear under the '''Plugins''' menu of ImageJ. Open an image stack, then click it to run the plugin! 

Note that, to ensure color appears correctly in the web app, images must be of type RGB. You can change the type of your image by selecting from the menus: Image > Type > RGB Color. 

FPBioimage Helper will set the XYZ voxel ratio from the image properties (Image > Properties...), although you can overwrite this data in the plugin in case it is incorrect. 

== One-click Macro ==

Copy the following macro to the bottom of the Fiji/macros/StartupMacros.fiji.ijm file to add a macro button for one-click uploading to FPBioimage. 

<source lang="js">
macro "FPB Upload Action Tool - C111F00ffCeeeD21D24D71D81Dc1Dd1De1CfffL3137L393eL4161L4464D49D4bD4eD59D5bD5eD6aD6cD6dL9197D99D9bD9cDa1Da4Db1Db4DbbDc2Dc3DcaDccDdb" {
	rW = getWidth();
	rH = getHeight();
	t = getTitle();
    index = indexOf(t, ' ');
    if (index>-1){t = substring(t, 0, index);}
    index = indexOf(t, '.');
    if (index>-1){t = substring(t, 0, index);}

	if (rW>500){rW = 499;}
	if (rH>500){rH = 499;}
	getVoxelSize(vW, vH, vD, x);

	run("FPBioimage Helper", "unique=" + t + " x-voxel=" +vW + " y-voxel=" + vH + " z-voxel=" + vD + " x-resolution=" + rW + " y-resolution=" + rH + " upload");
}
</source>

== Source code ==

The source code for the FPBioimage FIJI plugin is {{GitHub | org = fpbioimage | repo = FPBioimageHelper-FIJI}}.

The source code for the FPBioimage web app can also be accessed {{GitHub | org = fpbioimage | repo = unity}}. 

== Publication ==

* Fantham, M. and Kaminski, C.F. (2017). [https://www.nature.com/articles/nphoton.2016.273 A new online tool for visualization of volumetric data]. Nature photonics, 11(2), 69.
