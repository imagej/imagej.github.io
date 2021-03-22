---
title: Plugin List
author: admin
categories: plugins
layout: page
use_math: false
description: This page describes the technical structure of SciJava and ImageJ projects. For maximum benefit, we suggest readers familiarize themselves with Maven, Git and GitHub before reading the sections here.
---
{% include warning-box content="This section is out of date, potentially misleading or invalid. Be careful with any instructions here. When in doubt, [ask for help from the community](/help)." %}

The hierarchy of the Fiji's Menu is shown here, with a few words of explanation for each menu entry and links to more documentation where available. If you know about a menu entry that is in this list, but which doesn't yet have a description, please add it.

This list is generated automatically from a script that can be found in the development folder. It is stored in this template.
<div id="mw-content-text" lang="en" dir="ltr" class="mw-content-ltr">

<h2><span class="mw-headline" id="Analyze">Analyze</span></h2>
<ul><li> <a href="Color_Histogram" title="Color Histogram">Color Histogram</a> - file <tt>ColorHistogram_</tt>  -- <i>java jar file</i></li>
<li> <a href="Color_Inspector_3D" title="Color Inspector 3D">Color Inspector 3D</a> - file <tt>Color_Inspector_3D</tt>  -- <i>java jar file</i></li>
<li> <a href="Directionality" title="Directionality">Directionality</a> - file <tt>fiji.analyze.directionality.Directionality_</tt>  -- <i>java jar file</i></li>
<li> <a href="Helmholtz_Analysis" title="Helmholtz Analysis">Helmholtz Analysis</a> - file <tt>Helmholtz_Analysis</tt>  -- <i>java jar file</i></li>
<li> <a href="3D_Surface_Plot" title="3D Surface Plot">3D Surface Plot</a> - file <tt>Interactive_3D_Surface_Plot</tt>  -- <i>java jar file</i></li>
<li> <a href="Shape_Index_Map" title="Shape Index Map">Shape Index Map</a> - file <tt>fiji.geom.Shape_Index_Map</tt>  -- <i>java jar file</i></li>
<li> <a href="3D_OC_Options" class="mw-redirect" title="3D OC Options">3D OC Options</a> - file <tt>_3D_OC_Options</tt>  -- <i>java jar file</i></li>
<li> <a href="3D_Objects_Counter" title="3D Objects Counter">3D Objects Counter</a> - file <tt>_3D_objects_counter</tt>  -- <i>java jar file</i></li></ul>
<p><br>
</p>
<h3><span class="mw-headline" id="Analyze_.3E_Classification">Analyze &gt; Classification</span></h3>
<ul><li> <a href="IsoData_Classifier" title="IsoData Classifier">IsoData Classifier</a> - file <tt>IsoData_Classifier</tt>  -- <i>java jar file</i></li></ul>
<p><br>
</p>
<h3><span class="mw-headline" id="Analyze_.3E_Colocalization">Analyze &gt; Colocalization</span></h3>
<ul><li> <a href="Coloc_2" title="Coloc 2">Coloc 2</a> - file <tt>Coloc_2</tt>  -- <i>java jar file</i></li>
<li> <a href="Colocalization_Test" title="Colocalization Test">Colocalization Test</a> - file <tt>Colocalisation_Test</tt>  -- <i>java jar file</i></li>
<li> <a href="Colocalization_Threshold" title="Colocalization Threshold">Colocalization Threshold</a> - file <tt>Colocalisation_Threshold</tt>  -- <i>java jar file</i></li></ul>
<p><br>
</p>
<h3><span class="mw-headline" id="Analyze_.3E_Local_Thickness">Analyze &gt; Local Thickness</span></h3>
<ul><li> <a href="Local_Thickness_to_Cleaned-Up_Local_Thickness" class="mw-redirect" title="Local Thickness to Cleaned-Up Local Thickness">Local Thickness to Cleaned-Up Local Thickness</a> - file <tt>Clean_Up_Local_Thickness("run")</tt>  -- <i>java jar file</i></li>
<li> <a href="Distance_Map_to_Distance_Ridge" class="mw-redirect" title="Distance Map to Distance Ridge">Distance Map to Distance Ridge</a> - file <tt>Distance_Ridge("run")</tt>  -- <i>java jar file</i></li>
<li> <a href="Geometry_to_Distance_Map" class="mw-redirect" title="Geometry to Distance Map">Geometry to Distance Map</a> - file <tt>EDT_S1D("run")</tt>  -- <i>java jar file</i></li>
<li> <a href="Local_Thickness_(complete_process)" class="mw-redirect" title="Local Thickness (complete process)">Local Thickness (complete process)</a> - file <tt>Local_Thickness_Driver("run")</tt>  -- <i>java jar file</i></li>
<li> <a href="Distance_Ridge_to_Local_Thickness" class="mw-redirect" title="Distance Ridge to Local Thickness">Distance Ridge to Local Thickness</a> - file <tt>Local_Thickness_Parallel("run")</tt>  -- <i>java jar file</i></li></ul>
<p><br>
</p>
<h3><span class="mw-headline" id="Analyze_.3E_Optic_Flow">Analyze &gt; Optic Flow</span></h3>
<ul><li> <a href="FlowJ" title="FlowJ">FlowJ</a> - file <tt>FlowJ_</tt>  -- <i>java jar file</i></li>
<li> <a href="PIV_analysis" class="mw-redirect" title="PIV analysis">PIV analysis</a> - file <tt>PIV_analyser</tt>  -- <i>java jar file</i></li></ul>
<p><br>
</p>
<h3><span class="mw-headline" id="Analyze_.3E_QuickPALM">Analyze &gt; QuickPALM</span></h3>
<ul><li> <a href="Analyse_Particles" class="mw-redirect" title="Analyse Particles">Analyse Particles</a> - file <tt>QuickPALM.Analyse_Particles</tt>  -- <i>java jar file</i></li>
<li> <a href="Correct_Particles_Drift_(based_on_ROI)" class="mw-redirect" title="Correct Particles Drift (based on ROI)">Correct Particles Drift (based on ROI)</a> - file <tt>QuickPALM.Correct_Drift2</tt>  -- <i>java jar file</i></li>
<li> <a href="Create_3D_calibration_(requires_astigmatism)" class="mw-redirect" title="Create 3D calibration (requires astigmatism)">Create 3D calibration (requires astigmatism)</a> - file <tt>QuickPALM.Create_3D_calibration</tt>  -- <i>java jar file</i></li>
<li> <a href="Load_Particles_(.tif_file_-_fast)" class="mw-redirect" title="Load Particles (.tif file - fast)">Load Particles (.tif file - fast)</a> - file <tt>QuickPALM.Load_particles_tableFromImg</tt>  -- <i>java jar file</i></li>
<li> <a href="Reconstruct_Dataset" class="mw-redirect" title="Reconstruct Dataset">Reconstruct Dataset</a> - file <tt>QuickPALM.Reconstruct_Dataset</tt>  -- <i>java jar file</i></li>
<li> <a href="Save_Particles_(.tif_file_-_fast)" class="mw-redirect" title="Save Particles (.tif file - fast)">Save Particles (.tif file - fast)</a> - file <tt>QuickPALM.Save_particles_table2img</tt>  -- <i>java jar file</i></li>
<li> <a href="Stop_Analyse_Particles_(kills_the_threads)" class="mw-redirect" title="Stop Analyse Particles (kills the threads)">Stop Analyse Particles (kills the threads)</a> - file <tt>QuickPALM.Stop_processing</tt>  -- <i>java jar file</i></li>
<li> <a href="About..." class="mw-redirect" title="About...">About...</a> - file <tt>QuickPALM.Run_MyMacro("About_.txt")</tt>  -- <i>java jar file</i></li>
<li> <a href="Fast_VirtualStack_Opener" class="mw-redirect" title="Fast VirtualStack Opener">Fast VirtualStack Opener</a> - file <tt>QuickPALM.Run_MyMacro("Fast_VirtualStack_Opener.txt")</tt>  -- <i>java jar file</i></li>
<li> <a href="Sort_Particles_by_frame_(in_a_.tif_particle_table_file)" class="mw-redirect" title="Sort Particles by frame (in a .tif particle table file)">Sort Particles by frame (in a .tif particle table file)</a> - file <tt>QuickPALM.Run_MyMacro("Sort_particles.txt")</tt>  -- <i>java jar file</i></li>
<li> <a href="Update_QuickPALM" class="mw-redirect" title="Update QuickPALM">Update QuickPALM</a> - file <tt>QuickPALM.Run_MyMacro("Update_.txt")</tt>  -- <i>java jar file</i></li></ul>
<p><br>
</p>
<h3><span class="mw-headline" id="Analyze_.3E_Tools">Analyze &gt; Tools</span></h3>
<ul><li> <a href="PointPicker" title="PointPicker">PointPicker</a> - file <tt>PointPicker_</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Sync_Measure_3D&amp;action=edit&amp;redlink=1" class="new" title="Sync Measure 3D (page does not exist)">Sync Measure 3D</a> - file <tt>Sync_Measure_3D("")</tt>  -- <i>java jar file</i></li>
<li> <a href="Sync_Windows" title="Sync Windows">Sync Windows</a> - file <tt>Sync_Windows("")</tt>  -- <i>java jar file</i></li></ul>
<p><br>
</p>
<h3><span class="mw-headline" id="Analyze_.3E_TopoJ">Analyze &gt; TopoJ</span></h3>
<ul><li> <a href="Compute_Topography" class="mw-redirect" title="Compute Topography">Compute Topography</a> - file <tt>Compute_Topography</tt>  -- <i>java jar file</i></li>
<li> <a href="Remove_Slope" class="mw-redirect" title="Remove Slope">Remove Slope</a> - file <tt>Remove_Slope</tt>  -- <i>java jar file</i></li></ul>
<p><br>
</p>
<h2><span class="mw-headline" id="Edit">Edit</span></h2>
<h3><span class="mw-headline" id="Edit_.3E_Selection">Edit &gt; Selection</span></h3>
<ul><li> <a href="index.php?title=Points_from_Mask&amp;action=edit&amp;redlink=1" class="new" title="Points from Mask (page does not exist)">Points from Mask</a> - file <tt>fiji.selection.Binary_to_Point_Selection</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Fit_Circle_to_Image&amp;action=edit&amp;redlink=1" class="new" title="Fit Circle to Image (page does not exist)">Fit Circle to Image</a> - file <tt>fiji.util.Circle_Fitter</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Fill_ROI_holes&amp;action=edit&amp;redlink=1" class="new" title="Fill ROI holes (page does not exist)">Fill ROI holes</a> - file <tt>Fill_holes</tt>  -- <i>java jar file</i></li>
<li> <a href="Select_Bounding_Box" class="mw-redirect" title="Select Bounding Box">Select Bounding Box</a> - file <tt>fiji.selection.Select_Bounding_Box</tt>  -- <i>java jar file</i></li>
<li> <a href="Select_Bounding_Box_(guess_background_color)" class="mw-redirect" title="Select Bounding Box (guess background color)">Select Bounding Box (guess background color)</a> - file <tt>fiji.selection.Select_Bounding_Box("autoselect")</tt>  -- <i>java jar file</i></li></ul>
<p><br>
</p>
<h2><span class="mw-headline" id="File">File</span></h2>
<h3><span class="mw-headline" id="File_.3E_Import">File &gt; Import</span></h3>
<ul><li> <a href="index.php?title=Amira...&amp;action=edit&amp;redlink=1" class="new" title="Amira... (page does not exist)">Amira...</a> - file <tt>AmiraMeshReader_</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Show_Amira_Surface&amp;action=edit&amp;redlink=1" class="new" title="Show Amira Surface (page does not exist)">Show Amira Surface</a> - file <tt>isosurface.AmiraSurface</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Analyze...&amp;action=edit&amp;redlink=1" class="new" title="Analyze... (page does not exist)">Analyze...</a> - file <tt>Analyze_Reader</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Animated_Gif...&amp;action=edit&amp;redlink=1" class="new" title="Animated Gif... (page does not exist)">Animated Gif...</a> - file <tt>io.Animated_Gif_Reader</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Biorad...&amp;action=edit&amp;redlink=1" class="new" title="Biorad... (page does not exist)">Biorad...</a> - file <tt>Biorad_Reader</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=DM3_Reader...&amp;action=edit&amp;redlink=1" class="new" title="DM3 Reader... (page does not exist)">DM3 Reader...</a> - file <tt>io.DM3_Reader</tt>  -- <i>java jar file</i></li>
<li> <a href="Extract_Images_From_PDF..." title="Extract Images From PDF...">Extract Images From PDF...</a> - file <tt>io.Extract_Images_From_PDF</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=FIB-SEM_...&amp;action=edit&amp;redlink=1" class="new" title="FIB-SEM ... (page does not exist)">FIB-SEM ...</a> - file <tt>io.FIBSEM_Reader</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=ICO...&amp;action=edit&amp;redlink=1" class="new" title="ICO... (page does not exist)">ICO...</a> - file <tt>io.ICO_Reader</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=IPLab_Reader...&amp;action=edit&amp;redlink=1" class="new" title="IPLab Reader... (page does not exist)">IPLab Reader...</a> - file <tt>io.IPLab_Reader</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Icns...&amp;action=edit&amp;redlink=1" class="new" title="Icns... (page does not exist)">Icns...</a> - file <tt>io.Icns_Reader</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Open_with_preview_...&amp;action=edit&amp;redlink=1" class="new" title="Open with preview ... (page does not exist)">Open with preview ...</a> - file <tt>net.sf.ij.plugin.ImageIOOpenPlugin("preview")</tt>  -- <i>java jar file</i></li>
<li> [[Open [Image IO]]] - file <tt>net.sf.ij.plugin.ImageIOOpenPlugin("simple")</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=LSM...&amp;action=edit&amp;redlink=1" class="new" title="LSM... (page does not exist)">LSM...</a> - file <tt>LSM_Reader</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Show_LSMToolbox&amp;action=edit&amp;redlink=1" class="new" title="Show LSMToolbox (page does not exist)">Show LSMToolbox</a> - file <tt>LSM_Toolbox("")</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=LSS16...&amp;action=edit&amp;redlink=1" class="new" title="LSS16... (page does not exist)">LSS16...</a> - file <tt>io.LSS16_Reader</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Leica_SP...&amp;action=edit&amp;redlink=1" class="new" title="Leica SP... (page does not exist)">Leica SP...</a> - file <tt>leica.Leica_SP_Reader</tt>  -- <i>java jar file</i></li>
<li> <a href="Bio-Formats_(Remote)" class="mw-redirect" title="Bio-Formats (Remote)">Bio-Formats (Remote)</a> - file <tt>loci.plugins.LociImporter("location=[Internet]")</tt>  -- <i>java jar file</i></li>
<li> <a href="Bio-Formats" title="Bio-Formats">Bio-Formats</a> - file <tt>loci.plugins.LociImporter("location=[Local machine] windowless=false ")</tt>  -- <i>java jar file</i></li>
<li> <a href="Bio-Formats_(Windowless)" class="mw-redirect" title="Bio-Formats (Windowless)">Bio-Formats (Windowless)</a> - file <tt>loci.plugins.LociImporter("location=[Local machine] windowless=true ")</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Amira_as_TrakEM2...&amp;action=edit&amp;redlink=1" class="new" title="Amira as TrakEM2... (page does not exist)">Amira as TrakEM2...</a> - file <tt>ini.trakem2.New_Project("amira")</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Nrrd_...&amp;action=edit&amp;redlink=1" class="new" title="Nrrd ... (page does not exist)">Nrrd ...</a> - file <tt>io.Nrrd_Reader</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=DAT_EMMENU_...&amp;action=edit&amp;redlink=1" class="new" title="DAT EMMENU ... (page does not exist)">DAT EMMENU ...</a> - file <tt>io.Open_DAT_EMMENU</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=DF3...&amp;action=edit&amp;redlink=1" class="new" title="DF3... (page does not exist)">DF3...</a> - file <tt>io.Open_DF3</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=MRC_Leginon_...&amp;action=edit&amp;redlink=1" class="new" title="MRC Leginon ... (page does not exist)">MRC Leginon ...</a> - file <tt>io.Open_MRC_Leginon</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=TrakEM2_XML...&amp;action=edit&amp;redlink=1" class="new" title="TrakEM2 XML... (page does not exist)">TrakEM2 XML...</a> - file <tt>ini.trakem2.Open_Project</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=PDF_...&amp;action=edit&amp;redlink=1" class="new" title="PDF ... (page does not exist)">PDF ...</a> - file <tt>io.PDF_Viewer</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Reconstruct_Project...&amp;action=edit&amp;redlink=1" class="new" title="Reconstruct Project... (page does not exist)">Reconstruct Project...</a> - file <tt>reconstructreader.reconstruct.Reconstruct_Reader</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=SPIM&amp;action=edit&amp;redlink=1" class="new" title="SPIM (page does not exist)">SPIM</a> - file <tt>spimopener.SPIM_Opener</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=SVG...&amp;action=edit&amp;redlink=1" class="new" title="SVG... (page does not exist)">SVG...</a> - file <tt>io.SVG_Reader</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=TorstenRaw_GZ_Reader...&amp;action=edit&amp;redlink=1" class="new" title="TorstenRaw GZ Reader... (page does not exist)">TorstenRaw GZ Reader...</a> - file <tt>io.TorstenRaw_GZ_Reader</tt>  -- <i>java jar file</i></li></ul>
<h4><span class="mw-headline" id="File_.3E_Import_.3E_QuickPALM">File &gt; Import &gt; QuickPALM</span></h4>
<ul><li> <a href="Load_Particles_(.tif_file_-_fast)" class="mw-redirect" title="Load Particles (.tif file - fast)"> Load Particles (.tif file - fast)</a> - file <tt>QuickPALM.Load_particles_tableFromImg</tt>  -- <i>java jar file</i></li>
<li> <a href="Save_Particles_(.tif_file_-_fast)" class="mw-redirect" title="Save Particles (.tif file - fast)"> Save Particles (.tif file - fast)</a> - file <tt>QuickPALM.Save_particles_table2img</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Open_VirtualStack&amp;action=edit&amp;redlink=1" class="new" title="Open VirtualStack (page does not exist)"> Open VirtualStack</a> - file <tt>QuickPALM.Run_MyMacro("Fast_VirtualStack_Opener.txt")</tt>  -- <i>java jar file</i></li></ul>
<p><br>
</p>
<h3><span class="mw-headline" id="File_.3E_New">File &gt; New</span></h3>
<ul><li> <a href="TrakEM2_(from_template)" class="mw-redirect" title="TrakEM2 (from template)">TrakEM2 (from template)</a> - file <tt>ini.trakem2.New_Project</tt>  -- <i>java jar file</i></li>
<li> <a href="TrakEM2_(blank)" class="mw-redirect" title="TrakEM2 (blank)">TrakEM2 (blank)</a> - file <tt>ini.trakem2.New_Project("blank")</tt>  -- <i>java jar file</i></li>
<li> <a href="Script" class="mw-redirect" title="Script">Script</a> - file <tt>fiji.scripting.Script_Editor</tt>  -- <i>java jar file</i></li></ul>
<p><br>
</p>
<h3><span class="mw-headline" id="File_.3E_Open_Samples">File &gt; Open Samples</span></h3>
<ul><li> <a href="Shepp-Logan_Phantom_(Plugin)" class="mw-redirect" title="Shepp-Logan Phantom (Plugin)">Shepp-Logan Phantom (Plugin)</a> - file <tt>SheppLogan_</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=The_New_Lenna_(95K)&amp;action=edit&amp;redlink=1" class="new" title="The New Lenna (95K) (page does not exist)">The New Lenna (95K)</a> - file <tt>ij.plugin.URLOpener("<img src="https://fiji.sc/samples/new-lenna.jpg" alt="new-lenna.jpg">")</tt>  -- <i>java jar file</i></li>
<li> <a href="Malaria_Sporozoites_(9.2MB)" title="Malaria Sporozoites (9.2MB)">Malaria Sporozoites (9.2MB)</a> - file <tt>ij.plugin.URLOpener("<a rel="nofollow" class="external free" href="https://fiji.sc/samples/_malaria_parasites.tif">https://fiji.sc/samples/_malaria_parasites.tif</a>")</tt>  -- <i>java jar file</i></li>
<li> <a href="First-instar_brain_(6.3MB)" title="First-instar brain (6.3MB)">First-instar brain (6.3MB)</a> - file <tt>ij.plugin.URLOpener("<a rel="nofollow" class="external free" href="https://fiji.sc/samples/first-instar-brain.zip">https://fiji.sc/samples/first-instar-brain.zip</a>")</tt>  -- <i>java jar file</i></li>
<li> <a href="Sintered_Alumina_(2.6MB)" class="mw-redirect" title="Sintered Alumina (2.6MB)">Sintered Alumina (2.6MB)</a> - file <tt>ij.plugin.URLOpener("<a rel="nofollow" class="external free" href="https://fiji.sc/samples/Sintered_Alumina.tif.zip">https://fiji.sc/samples/Sintered_Alumina.tif.zip</a>")</tt>  -- <i>java jar file</i></li></ul>
<p><br>
</p>
<h3><span class="mw-headline" id="File_.3E_Open_Samples_2">File &gt; Open_Samples</span></h3>
<ul><li> <a href="Adelsons_Squares" class="mw-redirect" title="Adelsons Squares">Adelsons Squares</a> - file <tt>Adelsons_Squares.ijm</tt>  -- <i>macro</i></li>
<li> <a href="Spirals" title="Spirals">Spirals </a> - file <tt>Spirals_.ijm</tt>  -- <i>macro</i></li></ul>
<p><br>
</p>
<h3><span class="mw-headline" id="File_.3E_Save_As">File &gt; Save As</span></h3>
<ul><li> <a href="index.php?title=AmiraMesh_...&amp;action=edit&amp;redlink=1" class="new" title="AmiraMesh ... (page does not exist)">AmiraMesh ...</a> - file <tt>AmiraMeshWriter_</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=AmiraTable_...&amp;action=edit&amp;redlink=1" class="new" title="AmiraTable ... (page does not exist)">AmiraTable ...</a> - file <tt>AmiraTableWriter_</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Analyze...&amp;action=edit&amp;redlink=1" class="new" title="Analyze... (page does not exist)">Analyze... </a> - file <tt>Analyze_Writer</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Biorad_...&amp;action=edit&amp;redlink=1" class="new" title="Biorad ... (page does not exist)">Biorad ...</a> - file <tt>Biorad_Writer</tt>  -- <i>java jar file</i></li>
<li> <a href="Wavefront_.OBJ_..." title="Wavefront .OBJ ...">Wavefront .OBJ ...</a> - file <tt>marchingcubes.ExportMesh_</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=EPS_...&amp;action=edit&amp;redlink=1" class="new" title="EPS ... (page does not exist)">EPS ...</a> - file <tt>io.Export_EPS</tt>  -- <i>java jar file</i></li>
<li> <a href="Animated_Gif_..." class="mw-redirect" title="Animated Gif ...">Animated Gif ... </a> - file <tt>io.Gif_Stack_Writer</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=ICO_...&amp;action=edit&amp;redlink=1" class="new" title="ICO ... (page does not exist)">ICO ...</a> - file <tt>io.ICO_Writer</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Icns_...&amp;action=edit&amp;redlink=1" class="new" title="Icns ... (page does not exist)">Icns ...</a> - file <tt>io.Icns_Writer</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=PNG_...&amp;action=edit&amp;redlink=1" class="new" title="PNG ... (page does not exist)">PNG ...</a> - file <tt>net.sf.ij.plugin.ImageIOSaveAsPlugin("PNG")</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=PNM_...&amp;action=edit&amp;redlink=1" class="new" title="PNM ... (page does not exist)">PNM ...</a> - file <tt>net.sf.ij.plugin.ImageIOSaveAsPlugin("PNM")</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Compressed_TIFF_...&amp;action=edit&amp;redlink=1" class="new" title="Compressed TIFF ... (page does not exist)">Compressed TIFF ...</a> - file <tt>net.sf.ij.plugin.ImageIOSaveAsPlugin("TIFF")</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=LSS16_...&amp;action=edit&amp;redlink=1" class="new" title="LSS16 ... (page does not exist)">LSS16 ...</a> - file <tt>io.LSS16_Writer</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Leica_SP_...&amp;action=edit&amp;redlink=1" class="new" title="Leica SP ... (page does not exist)">Leica SP ...</a> - file <tt>leica.Leica_SP_Writer</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Nrrd_...&amp;action=edit&amp;redlink=1" class="new" title="Nrrd ... (page does not exist)">Nrrd ... </a> - file <tt>io.Nrrd_Writer</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=PDF_...&amp;action=edit&amp;redlink=1" class="new" title="PDF ... (page does not exist)">PDF ... </a> - file <tt>io.PDF_Writer</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=DF3_...&amp;action=edit&amp;redlink=1" class="new" title="DF3 ... (page does not exist)">DF3 ...</a> - file <tt>io.Save_DF3</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=XPM_...&amp;action=edit&amp;redlink=1" class="new" title="XPM ... (page does not exist)">XPM ...</a> - file <tt>io.XPM_Writer</tt>  -- <i>java jar file</i></li></ul>
<p><br>
</p>
<h2><span class="mw-headline" id="Help">Help</span></h2>
<ul><li> <a href="Report_a_Bug" title="Report a Bug">Report a Bug</a> - file <tt>Bug_Submitter.Bug_Submitter</tt>  -- <i>java jar file</i></li>
<li> <a href="Help_on_Menu_Item" title="Help on Menu Item">Help on Menu Item</a> - file <tt>fiji.help.Context_Help</tt>  -- <i>java jar file</i></li>
<li> <a href="Upload_Sample_Image" title="Upload Sample Image">Upload Sample Image</a> - file <tt>fiji.util.Fiji_Uploader</tt>  -- <i>java jar file</i></li>
<li> <a href="Update_Fiji" class="mw-redirect" title="Update Fiji">Update Fiji</a> - file <tt>fiji.updater.Updater("update")</tt>  -- <i>java jar file</i></li>
<li> <a href="Licenses" class="mw-redirect" title="Licenses">Licenses</a> - file <tt>ij.plugin.BrowserLauncher("<a rel="nofollow" class="external free" href="https://fiji.sc/cgi-bin/gitweb.cgi?p=fiji.git;a=blob_plain;f=LICENSES;hb=HEAD">https://fiji.sc/cgi-bin/gitweb.cgi?p=fiji.git;a=blob_plain;f=LICENSES;hb=HEAD</a>")</tt>  -- <i>java jar file</i></li>
<li> <a href="Fiji_Wiki" title="Fiji Wiki">Fiji Wiki</a> - file <tt>ij.plugin.BrowserLauncher("<a rel="nofollow" class="external free" href="https://fiji.sc/">https://fiji.sc/</a>")</tt>  -- <i>java jar file</i></li></ul>
<p><br>
</p>
<h3><span class="mw-headline" id="Help_.3E_About_Plugins">Help &gt; About Plugins</span></h3>
<ul><li> <a href="LOCI_Plugins..." class="mw-redirect" title="LOCI Plugins...">LOCI Plugins...</a> - file <tt>loci.plugins.About("")</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Image_IO_...&amp;action=edit&amp;redlink=1" class="new" title="Image IO ... (page does not exist)">Image IO ...</a> - file <tt>net.sf.ij.plugin.AboutImageIO("")</tt>  -- <i>java jar file</i></li>
<li> <a href="Robust_Automatic_Threshold_Selection" class="mw-redirect" title="Robust Automatic Threshold Selection">Robust Automatic Threshold Selection </a> - file <tt>About_RATS</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Color_Histogram...&amp;action=edit&amp;redlink=1" class="new" title="Color Histogram... (page does not exist)">Color Histogram...</a> - file <tt>ColorHistogram_("about")</tt>  -- <i>java jar file</i></li>
<li> <a href="About_bUnwarpJ..." class="mw-redirect" title="About bUnwarpJ...">About bUnwarpJ...</a> - file <tt>bunwarpj.Credits</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=FeatureJ...&amp;action=edit&amp;redlink=1" class="new" title="FeatureJ... (page does not exist)">FeatureJ...</a> - file <tt>FJ_Website</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Gray_Morphology...&amp;action=edit&amp;redlink=1" class="new" title="Gray Morphology... (page does not exist)">Gray Morphology...</a> - file <tt>GrayMorphology_("about")</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Image5D...&amp;action=edit&amp;redlink=1" class="new" title="Image5D... (page does not exist)">Image5D...</a> - file <tt>I5D_about("about")</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=LSMReader...&amp;action=edit&amp;redlink=1" class="new" title="LSMReader... (page does not exist)">LSMReader...</a> - file <tt>LSM_Reader("about")</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=LSMToolbox...&amp;action=edit&amp;redlink=1" class="new" title="LSMToolbox... (page does not exist)">LSMToolbox...</a> - file <tt>LSM_Toolbox("about")</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=RandomJ...&amp;action=edit&amp;redlink=1" class="new" title="RandomJ... (page does not exist)">RandomJ...</a> - file <tt>RJ_Website</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Sync_Measure_3D...&amp;action=edit&amp;redlink=1" class="new" title="Sync Measure 3D... (page does not exist)">Sync Measure 3D...</a> - file <tt>Sync_Measure_3D("about")</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Sync_Windows...&amp;action=edit&amp;redlink=1" class="new" title="Sync Windows... (page does not exist)">Sync Windows...</a> - file <tt>Sync_Windows("about")</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=TransformJ...&amp;action=edit&amp;redlink=1" class="new" title="TransformJ... (page does not exist)">TransformJ...</a> - file <tt>TJ_Website</tt>  -- <i>java jar file</i></li>
<li> <a href="About_TrakEM2..." class="mw-redirect" title="About TrakEM2...">About TrakEM2...</a> - file <tt>ini.trakem2.utils.Utils</tt>  -- <i>java jar file</i></li></ul>
<p><br>
</p>
<h2><span class="mw-headline" id="Image">Image</span></h2>
<h3><span class="mw-headline" id="Image_.3E_Adjust">Image &gt; Adjust</span></h3>
<ul><li> <a href="Auto_Local_Threshold" title="Auto Local Threshold">Auto Local Threshold</a> - file <tt>fiji.threshold.Auto_Local_Threshold</tt>  -- <i>java jar file</i></li>
<li> <a href="Auto_Threshold" title="Auto Threshold">Auto Threshold</a> - file <tt>fiji.threshold.Auto_Threshold</tt>  -- <i>java jar file</i></li>
<li> <a href="Bleach_Correction" title="Bleach Correction">Bleach Correction</a> - file <tt>emblcmci.BleachCorrection</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Scale_to_DPI&amp;action=edit&amp;redlink=1" class="new" title="Scale to DPI (page does not exist)">Scale to DPI</a> - file <tt>Scale_to_DPI.js</tt>  -- <i>javascript script</i></li>
<li> <a href="Auto_Crop_(guess_background_color)" class="mw-redirect" title="Auto Crop (guess background color)">Auto Crop (guess background color)</a> - file <tt>fiji.selection.Select_Bounding_Box("autoautocrop")</tt>  -- <i>java jar file</i></li>
<li> <a href="Auto_Crop" title="Auto Crop">Auto Crop</a> - file <tt>fiji.selection.Select_Bounding_Box("autocrop")</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Threshold_Colour&amp;action=edit&amp;redlink=1" class="new" title="Threshold Colour (page does not exist)">Threshold Colour</a> - file <tt>Threshold_Colour</tt>  -- <i>java jar file</i></li></ul>
<p><br>
</p>
<h3><span class="mw-headline" id="Image_.3E_Annotate">Image &gt; Annotate</span></h3>
<ul><li> <a href="Arrow" title="Arrow">Arrow </a> - file <tt>fiji.util.ArrowTool</tt>  -- <i>java jar file</i></li></ul>
<p><br>
</p>
<h3><span class="mw-headline" id="Image_.3E_Color">Image &gt; Color</span></h3>
<ul><li> <a href="index.php?title=Average_Color&amp;action=edit&amp;redlink=1" class="new" title="Average Color (page does not exist)">Average Color</a> - file <tt>Average_Color</tt>  -- <i>java jar file</i></li>
<li> <a href="Colour_Deconvolution" title="Colour Deconvolution">Colour Deconvolution</a> - file <tt>Colour_Deconvolution</tt>  -- <i>java jar file</i></li>
<li> <a href="Replace_Red_with_Magenta" title="Replace Red with Magenta">Replace Red with Magenta</a> - file <tt>fiji.color.Convert_Red_To_Magenta</tt>  -- <i>java jar file</i></li>
<li> <a href="Replace_Red_with_Magenta_(system_clipboard)" class="mw-redirect" title="Replace Red with Magenta (system clipboard)">Replace Red with Magenta (system clipboard)</a> - file <tt>fiji.color.Convert_Red_To_Magenta_Clipboard</tt>  -- <i>java jar file</i></li>
<li> <a href="Dichromacy" title="Dichromacy">Dichromacy</a> - file <tt>Dichromacy_</tt>  -- <i>java jar file</i></li>
<li> <a href="Simulate_Color_Blindness" title="Simulate Color Blindness">Simulate Color Blindness</a> - file <tt>Dichromacy_</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=RGB_to_CIELAB&amp;action=edit&amp;redlink=1" class="new" title="RGB to CIELAB (page does not exist)">RGB to CIELAB</a> - file <tt>RGB_to_CIELAB</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=RGB_to_Luminance&amp;action=edit&amp;redlink=1" class="new" title="RGB to Luminance (page does not exist)">RGB to Luminance</a> - file <tt>util.RGB_to_Luminance</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=RGBtoLab&amp;action=edit&amp;redlink=1" class="new" title="RGBtoLab (page does not exist)">RGBtoLab </a> - file <tt>RGBtoLab_</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=RGBtoYUV&amp;action=edit&amp;redlink=1" class="new" title="RGBtoYUV (page does not exist)">RGBtoYUV </a> - file <tt>RGBtoYUV_</tt>  -- <i>java jar file</i></li>
<li> <a href="Retinex" title="Retinex">Retinex</a> - file <tt>Retinex_</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Set_Color_By_Wavelength&amp;action=edit&amp;redlink=1" class="new" title="Set Color By Wavelength (page does not exist)">Set Color By Wavelength</a> - file <tt>Set_Color_By_Wavelength.ijm</tt>  -- <i>macro</i></li></ul>
<p><br>
</p>
<h3><span class="mw-headline" id="Image_.3E_Drawing">Image &gt; Drawing</span></h3>
<ul><li> <a href="index.php?title=Linear_Gradient&amp;action=edit&amp;redlink=1" class="new" title="Linear Gradient (page does not exist)">Linear Gradient</a> - file <tt>fiji.drawing.Linear_Gradient</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Radial_Gradient&amp;action=edit&amp;redlink=1" class="new" title="Radial Gradient (page does not exist)">Radial Gradient</a> - file <tt>fiji.drawing.Radial_Gradient</tt>  -- <i>java jar file</i></li></ul>
<p><br>
</p>
<h3><span class="mw-headline" id="Image_.3E_Hyperstacks">Image &gt; Hyperstacks</span></h3>
<ul><li> <a href="index.php?title=Re-order_Hyperstack_...&amp;action=edit&amp;redlink=1" class="new" title="Re-order Hyperstack ... (page does not exist)">Re-order Hyperstack ...</a> - file <tt>fiji.stacks.Hyperstack_rearranger</tt>  -- <i>java jar file</i></li>
<li> <a href="Temporal-Color_Code" title="Temporal-Color Code">Temporal-Color Code</a> - file <tt>Temporal-Color_Code.ijm</tt>  -- <i>macro</i></li></ul>
<p><br>
</p>
<h3><span class="mw-headline" id="Image_.3E_Selection">Image &gt; Selection</span></h3>
<ul><li> <a href="index.php?title=Make_rectangular_selection_rounded&amp;action=edit&amp;redlink=1" class="new" title="Make rectangular selection rounded (page does not exist)">Make rectangular selection rounded</a> - file <tt>fiji.selection.Rounded_Rectangle</tt>  -- <i>java jar file</i></li></ul>
<p><br>
</p>
<h3><span class="mw-headline" id="Image_.3E_Stacks">Image &gt; Stacks</span></h3>
<ul><li> <a href="Dynamic_Reslice" title="Dynamic Reslice">Dynamic Reslice</a> - file <tt>fiji.stacks.Dynamic_Reslice</tt>  -- <i>java jar file</i></li>
<li> <a href="Kalman_Stack_Filter" title="Kalman Stack Filter">Kalman Stack Filter</a> - file <tt>Kalman_Filter</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Radial_Reslice&amp;action=edit&amp;redlink=1" class="new" title="Radial Reslice (page does not exist)">Radial Reslice</a> - file <tt>fiji.stacks.Radial_Reslice</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Reslice_Z&amp;action=edit&amp;redlink=1" class="new" title="Reslice Z (page does not exist)">Reslice Z</a> - file <tt>Reslice_Z</tt>  -- <i>java jar file</i></li>
<li> <a href="Series_Labeler" title="Series Labeler">Series Labeler</a> - file <tt>Series_Labeler</tt>  -- <i>java jar file</i></li>
<li> <a href="Time_Stamper" title="Time Stamper">Time Stamper</a> - file <tt>Time_Stamper</tt>  -- <i>java jar file</i></li></ul>
<h4><span class="mw-headline" id="Image_.3E_Stacks_.3E_Tools">Image &gt; Stacks &gt; Tools_</span></h4>
<ul><li> <a href="Deinterleave" class="mw-redirect" title="Deinterleave">Deinterleave</a> - file <tt>DeInterleave_</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Slice_Keeper&amp;action=edit&amp;redlink=1" class="new" title="Slice Keeper (page does not exist)">Slice Keeper</a> - file <tt>Slice_Keeper</tt>  -- <i>java jar file</i></li>
<li> <a href="Slice_Remover" class="mw-redirect" title="Slice Remover">Slice Remover</a> - file <tt>Slice_Remover</tt>  -- <i>java jar file</i></li>
<li> <a href="Interleave" class="mw-redirect" title="Interleave">Interleave</a> - file <tt>Stack_Interleaver</tt>  -- <i>java jar file</i></li>
<li> <a href="Stack_Sorter" class="mw-redirect" title="Stack Sorter">Stack Sorter</a> - file <tt>Stack_Sorter</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Stack_Splitter&amp;action=edit&amp;redlink=1" class="new" title="Stack Splitter (page does not exist)">Stack Splitter</a> - file <tt>Stack_Splitter</tt>  -- <i>java jar file</i></li></ul>
<h4><span class="mw-headline" id="Image_.3E_Stacks_.3E_View5D">Image &gt; Stacks &gt; View5D</span></h4>
<ul><li> <a href="index.php?title=Start_viewer&amp;action=edit&amp;redlink=1" class="new" title="Start viewer (page does not exist)">start viewer</a> - file <tt>view5d.View5D_("")</tt>  -- <i>java jar file</i></li></ul>
<p><br>
</p>
<h3><span class="mw-headline" id="Image_.3E_Video_Editing">Image &gt; Video Editing</span></h3>
<ul><li> <a href="index.php?title=Add_Empty_Frame&amp;action=edit&amp;redlink=1" class="new" title="Add Empty Frame (page does not exist)">Add Empty Frame</a> - file <tt>video2.Add_Empty_Frame</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Delete_Frame&amp;action=edit&amp;redlink=1" class="new" title="Delete Frame (page does not exist)">Delete Frame</a> - file <tt>video2.Delete_Frame</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Draw_Roi&amp;action=edit&amp;redlink=1" class="new" title="Draw Roi (page does not exist)">Draw Roi</a> - file <tt>video2.Draw_Roi</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Duplicate_Frame&amp;action=edit&amp;redlink=1" class="new" title="Duplicate Frame (page does not exist)">Duplicate Frame</a> - file <tt>video2.Duplicate_Frame</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Insert_Stack&amp;action=edit&amp;redlink=1" class="new" title="Insert Stack (page does not exist)">Insert Stack</a> - file <tt>video2.Insert_Stack</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Make_Transition&amp;action=edit&amp;redlink=1" class="new" title="Make Transition (page does not exist)">Make Transition</a> - file <tt>video2.Make_Transition</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Move_Roi&amp;action=edit&amp;redlink=1" class="new" title="Move Roi (page does not exist)">Move Roi</a> - file <tt>video2.Move_Roi</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=New_Video&amp;action=edit&amp;redlink=1" class="new" title="New Video (page does not exist)">New Video</a> - file <tt>video2.New_Video</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Open_Video&amp;action=edit&amp;redlink=1" class="new" title="Open Video (page does not exist)">Open Video</a> - file <tt>video2.Open_Video</tt>  -- <i>java jar file</i></li></ul>
<p><br>
</p>
<h2><span class="mw-headline" id="Plugins">Plugins</span></h2>
<ul><li> <a href="3D_Viewer" title="3D Viewer">3D Viewer</a> - file <tt>ImageJ_3D_Viewer</tt>  -- <i>java jar file</i></li>
<li> <a href="Volume_Viewer" title="Volume Viewer">Volume Viewer</a> - file <tt>Volume_Viewer</tt>  -- <i>java jar file</i></li></ul>
<p><br>
</p>
<h3><span class="mw-headline" id="Plugins_.3E_Analyze">Plugins &gt; Analyze</span></h3>
<ul><li> <a href="Compute_Curvatures" title="Compute Curvatures">Compute Curvatures</a> - file <tt>Compute_Curvatures</tt>  -- <i>java jar file</i></li>
<li> <a href="Delaunay_Voronoi" title="Delaunay Voronoi">Delaunay Voronoi</a> - file <tt>Delaunay_Voronoi</tt>  -- <i>java jar file</i></li>
<li> <a href="Dynamic_ROI_Profiler" title="Dynamic ROI Profiler">Dynamic ROI Profiler</a> - file <tt>Dynamic_ROI_Profiler.clj</tt>  -- <i>clojure script</i></li>
<li> <a href="index.php?title=Find_differences&amp;action=edit&amp;redlink=1" class="new" title="Find differences (page does not exist)">Find differences</a> - file <tt>FindIt_</tt>  -- <i>java jar file</i></li>
<li> <a href="2D_Histogram" title="2D Histogram">2D Histogram</a> - file <tt>util.Histogram_2D</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Measure_RGB&amp;action=edit&amp;redlink=1" class="new" title="Measure RGB (page does not exist)">Measure RGB</a> - file <tt>Measure_RGB.txt</tt>  -- <i>macro</i></li>
<li> <a href="Surfaceness" title="Surfaceness">Surfaceness</a> - file <tt>features.Surfaceness_</tt>  -- <i>java jar file</i></li>
<li> <a href="Tubeness" title="Tubeness">Tubeness</a> - file <tt>features.Tubeness_</tt>  -- <i>java jar file</i></li>
<li> <a href="VIB_Protocol" title="VIB Protocol">VIB Protocol</a> - file <tt>VIB_Protocol</tt>  -- <i>java jar file</i></li>
<li> <a href="View5D" title="View5D">View5D </a> - file <tt>view5d.View5D_</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Visual_grep&amp;action=edit&amp;redlink=1" class="new" title="Visual grep (page does not exist)">Visual grep</a> - file <tt>Visual_Grep</tt>  -- <i>java jar file</i></li></ul>
<p><br>
</p>
<h3><span class="mw-headline" id="Plugins_.3E_Examples">Plugins &gt; Examples</span></h3>
<ul><li> <a href="index.php?title=Add_Popup_Split_Channels&amp;action=edit&amp;redlink=1" class="new" title="Add Popup Split Channels (page does not exist)">Add Popup Split Channels</a> - file <tt>Add_Popup_Split_Channels.bsh</tt>  -- <i>beanshell script</i></li>
<li> <a href="Anaglyph_for_Red_Cyan_glasses" title="Anaglyph for Red Cyan glasses">Anaglyph for Red Cyan glasses</a> - file <tt>Anaglyph_for_Red_Cyan_glasses.rb</tt>  -- <i>jruby script</i></li>
<li> <a href="Blobs_Demo_in_Ruby" title="Blobs Demo in Ruby">Blobs Demo in Ruby</a> - file <tt>Blobs_Demo_in_Ruby.rb</tt>  -- <i>jruby script</i></li>
<li> <a href="Delayed_Snapshot" title="Delayed Snapshot">Delayed Snapshot</a> - file <tt>Delayed_Snapshot.py</tt>  -- <i>jython script</i></li>
<li> <a href="index.php?title=Delayed_Snapshot_Window&amp;action=edit&amp;redlink=1" class="new" title="Delayed Snapshot Window (page does not exist)">Delayed Snapshot Window</a> - file <tt>Delayed_Snapshot_Window.bsh</tt>  -- <i>beanshell script</i></li>
<li> <a href="Edit_LUT_As_Text" title="Edit LUT As Text">Edit LUT As Text</a> - file <tt>Edit_LUT_As_Text.py</tt>  -- <i>jython script</i></li>
<li> <a href="index.php?title=Extended_Profile_Plot&amp;action=edit&amp;redlink=1" class="new" title="Extended Profile Plot (page does not exist)">Extended Profile Plot</a> - file <tt>Extended_Profile_Plot.bsh</tt>  -- <i>beanshell script</i></li>
<li> <a href="index.php?title=Fiji_Cube&amp;action=edit&amp;redlink=1" class="new" title="Fiji Cube (page does not exist)">Fiji Cube</a> - file <tt>Fiji_Cube.ijm</tt>  -- <i>macro</i></li>
<li> <a href="Fiji_Logo_3D" title="Fiji Logo 3D">Fiji Logo 3D</a> - file <tt>Fiji_Logo_3D.js</tt>  -- <i>javascript script</i></li>
<li> <a href="Find_Dimension_of_Raw_Image" title="Find Dimension of Raw Image">Find Dimension of Raw Image</a> - file <tt>Find_Dimension_of_Raw_Image.py</tt>  -- <i>jython script</i></li>
<li> <a href="index.php?title=Image_To_Tool_Icon&amp;action=edit&amp;redlink=1" class="new" title="Image To Tool Icon (page does not exist)">Image To Tool Icon</a> - file <tt>Image_To_Tool_Icon.bsh</tt>  -- <i>beanshell script</i></li>
<li> <a href="Spheres_and_Tubes_in_3D" title="Spheres and Tubes in 3D">Spheres and Tubes in 3D</a> - file <tt>customnode.Mesh_Maker</tt>  -- <i>java jar file</i></li>
<li> <a href="Multithreaded_Image_Processing" class="mw-redirect" title="Multithreaded Image Processing">Multithreaded Image Processing</a> - file <tt>Multithreaded_Image_Processing.clj</tt>  -- <i>clojure script</i></li>
<li> <a href="Multithreaded_Image_Processing_in_Javascript" class="mw-redirect" title="Multithreaded Image Processing in Javascript">Multithreaded Image Processing in Javascript</a> - file <tt>Multithreaded_Image_Processing_in_Javascript.js</tt>  -- <i>javascript script</i></li>
<li> <a href="Plasma_Cloud" title="Plasma Cloud">Plasma Cloud</a> - file <tt>Plasma_Cloud.rb</tt>  -- <i>jruby script</i></li>
<li> <a href="Same_Slice_in_Multiple_Images" title="Same Slice in Multiple Images">Same Slice in Multiple Images</a> - file <tt>Same_Slice_in_Multiple_Images.rb</tt>  -- <i>jruby script</i></li>
<li> <a href="index.php?title=Single_Voxel_in_3D&amp;action=edit&amp;redlink=1" class="new" title="Single Voxel in 3D (page does not exist)">Single Voxel in 3D</a> - file <tt>tracing.Test_Single_Voxel</tt>  -- <i>java jar file</i></li>
<li> <a href="The_Hue_Game" title="The Hue Game">The Hue Game</a> - file <tt>The_Hue_Game.bsh</tt>  -- <i>beanshell script</i></li>
<li> <a href="Blend_two_images" title="Blend two images">blend two images</a> - file <tt>blend_two_images.clj</tt>  -- <i>clojure script</i></li>
<li> <a href="Celsius_to_fahrenheit" title="Celsius to fahrenheit">celsius to fahrenheit</a> - file <tt>celsius_to_fahrenheit.clj</tt>  -- <i>clojure script</i></li>
<li> <a href="Chess" title="Chess">chess </a> - file <tt>chess_.py</tt>  -- <i>jython script</i></li>
<li> <a href="Downsample" title="Downsample">downsample </a> - file <tt>downsample_.js</tt>  -- <i>javascript script</i></li>
<li> <a href="List_all_threads" title="List all threads">list all threads</a> - file <tt>list_all_threads.py</tt>  -- <i>jython script</i></li>
<li> <a href="index.php?title=Random_noise_example&amp;action=edit&amp;redlink=1" class="new" title="Random noise example (page does not exist)">random noise example</a> - file <tt>random_noise_example.clj</tt>  -- <i>clojure script</i></li></ul>
<h4><span class="mw-headline" id="Plugins_.3E_Examples_.3E_Command_Launchers">Plugins &gt; Examples &gt; Command_Launchers</span></h4>
<ul><li> <a href="index.php?title=Command_Launcher_BeanShell&amp;action=edit&amp;redlink=1" class="new" title="Command Launcher BeanShell (page does not exist)">Command Launcher BeanShell</a> - file <tt>Command_Launcher_BeanShell.bsh</tt>  -- <i>beanshell script</i></li>
<li> <a href="Command_Launcher_Clojure" class="mw-redirect" title="Command Launcher Clojure">Command Launcher Clojure</a> - file <tt>Command_Launcher_Clojure.clj</tt>  -- <i>clojure script</i></li>
<li> <a href="Command_Launcher_Javascript" class="mw-redirect" title="Command Launcher Javascript">Command Launcher Javascript</a> - file <tt>Command_Launcher_Javascript.js</tt>  -- <i>javascript script</i></li>
<li> <a href="Command_Launcher_Python" class="mw-redirect" title="Command Launcher Python">Command Launcher Python</a> - file <tt>Command_Launcher_Python.py</tt>  -- <i>jython script</i></li>
<li> <a href="Command_Launcher_Ruby" class="mw-redirect" title="Command Launcher Ruby">Command Launcher Ruby</a> - file <tt>Command_Launcher_Ruby.rb</tt>  -- <i>jruby script</i></li></ul>
<h4><span class="mw-headline" id="Plugins_.3E_Examples_.3E_CoverMaker">Plugins &gt; Examples &gt; CoverMaker</span></h4>
<ul><li> <a href="Cover_Maker" title="Cover Maker">Cover Maker</a> - file <tt>Cover_Maker.py</tt>  -- <i>jython script</i></li>
<li> <a href="Prepare_Cover_Maker_Database" class="mw-redirect" title="Prepare Cover Maker Database">Prepare Cover Maker Database</a> - file <tt>Prepare_Cover_Maker_Database.py</tt>  -- <i>jython script</i></li></ul>
<h4><span class="mw-headline" id="Plugins_.3E_Examples_.3E_TrakEM2_Example_Scripts">Plugins &gt; Examples &gt; TrakEM2_Example_Scripts</span></h4>
<ul><li> <a href="index.php?title=Homogenize_Ball_Radius&amp;action=edit&amp;redlink=1" class="new" title="Homogenize Ball Radius (page does not exist)">Homogenize Ball Radius</a> - file <tt>Homogenize_Ball_Radius.py</tt>  -- <i>jython script</i></li>
<li> <a href="index.php?title=Measure_AreaLists&amp;action=edit&amp;redlink=1" class="new" title="Measure AreaLists (page does not exist)">Measure AreaLists</a> - file <tt>Measure_AreaLists.py</tt>  -- <i>jython script</i></li>
<li> <a href="index.php?title=T2_Select_All&amp;action=edit&amp;redlink=1" class="new" title="T2 Select All (page does not exist)">T2 Select All</a> - file <tt>T2_Select_All.py</tt>  -- <i>jython script</i></li>
<li> <a href="index.php?title=T2_set_all_transforms_to_identity&amp;action=edit&amp;redlink=1" class="new" title="T2 set all transforms to identity (page does not exist)">T2 set all transforms to identity</a> - file <tt>T2_set_all_transforms_to_identity.py</tt>  -- <i>jython script</i></li>
<li> <a href="index.php?title=Extract_stack_under_arealist&amp;action=edit&amp;redlink=1" class="new" title="Extract stack under arealist (page does not exist)">extract stack under arealist</a> - file <tt>extract_stack_under_arealist.py</tt>  -- <i>jython script</i></li></ul>
<p><br>
</p>
<h3><span class="mw-headline" id="Plugins_.3E_Feature_Extraction">Plugins &gt; Feature Extraction</span></h3>
<ul><li> <a href="index.php?title=Extract_Block_Matching_Correspondences&amp;action=edit&amp;redlink=1" class="new" title="Extract Block Matching Correspondences (page does not exist)">Extract Block Matching Correspondences</a> - file <tt>mpicbg.ij.plugin.BlockMatching_ExtractPoinRoi</tt>  -- <i>java jar file</i></li>
<li> <a href="Extract_MOPS_Correspondences" class="mw-redirect" title="Extract MOPS Correspondences">Extract MOPS Correspondences</a> - file <tt>MOPS_ExtractPointRoi</tt>  -- <i>java jar file</i></li>
<li> <a href="Extract_SIFT_Correspondences" class="mw-redirect" title="Extract SIFT Correspondences">Extract SIFT Correspondences</a> - file <tt>SIFT_ExtractPointRoi</tt>  -- <i>java jar file</i></li></ul>
<h4><span class="mw-headline" id="Plugins_.3E_Feature_Extraction_.3E_FeatureJ">Plugins &gt; Feature Extraction &gt; FeatureJ</span></h4>
<ul><li> <a href="FeatureJ_Derivatives" class="mw-redirect" title="FeatureJ Derivatives">FeatureJ Derivatives</a> - file <tt>FJ_Derivatives</tt>  -- <i>java jar file</i></li>
<li> <a href="FeatureJ_Edges" class="mw-redirect" title="FeatureJ Edges">FeatureJ Edges</a> - file <tt>FJ_Edges</tt>  -- <i>java jar file</i></li>
<li> <a href="FeatureJ_Hessian" class="mw-redirect" title="FeatureJ Hessian">FeatureJ Hessian</a> - file <tt>FJ_Hessian</tt>  -- <i>java jar file</i></li>
<li> <a href="FeatureJ_Laplacian" class="mw-redirect" title="FeatureJ Laplacian">FeatureJ Laplacian</a> - file <tt>FJ_Laplacian</tt>  -- <i>java jar file</i></li>
<li> <a href="FeatureJ_Options" class="mw-redirect" title="FeatureJ Options">FeatureJ Options</a> - file <tt>FJ_Options</tt>  -- <i>java jar file</i></li>
<li> <a href="FeatureJ_Panel" class="mw-redirect" title="FeatureJ Panel">FeatureJ Panel</a> - file <tt>FJ_Panel</tt>  -- <i>java jar file</i></li>
<li> <a href="FeatureJ_Statistics" class="mw-redirect" title="FeatureJ Statistics">FeatureJ Statistics</a> - file <tt>FJ_Statistics</tt>  -- <i>java jar file</i></li>
<li> <a href="FeatureJ_Structure" class="mw-redirect" title="FeatureJ Structure">FeatureJ Structure</a> - file <tt>FJ_Structure</tt>  -- <i>java jar file</i></li></ul>
<p><br>
</p>
<h3><span class="mw-headline" id="Plugins_.3E_Image5D">Plugins &gt; Image5D</span></h3>
<ul><li> <a href="index.php?title=Duplicate&amp;action=edit&amp;redlink=1" class="new" title="Duplicate (page does not exist)">Duplicate</a> - file <tt>Duplicate_Image5D("")</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Hypervolume_Opener&amp;action=edit&amp;redlink=1" class="new" title="Hypervolume Opener (page does not exist)">Hypervolume Opener</a> - file <tt>Hypervolume_Opener("")</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Image5D_Extensions&amp;action=edit&amp;redlink=1" class="new" title="Image5D Extensions (page does not exist)">Image5D Extensions</a> - file <tt>Image5D_Extensions("")</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Image5D_Stack_to_RGB&amp;action=edit&amp;redlink=1" class="new" title="Image5D Stack to RGB (page does not exist)">Image5D Stack to RGB</a> - file <tt>Image5D_Stack_to_RGB("")</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Image5D_to_Stack&amp;action=edit&amp;redlink=1" class="new" title="Image5D to Stack (page does not exist)">Image5D to Stack</a> - file <tt>Image5D_to_Stack("")</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Make_Montage&amp;action=edit&amp;redlink=1" class="new" title="Make Montage (page does not exist)">Make Montage</a> - file <tt>Make_Montage("")</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=New_Image5D&amp;action=edit&amp;redlink=1" class="new" title="New Image5D (page does not exist)">New Image5D</a> - file <tt>New_Image5D("")</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Open_Image5D&amp;action=edit&amp;redlink=1" class="new" title="Open Image5D (page does not exist)">Open Image5D</a> - file <tt>Open_Image5D("")</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Open_Series_As_Image5D&amp;action=edit&amp;redlink=1" class="new" title="Open Series As Image5D (page does not exist)">Open Series As Image5D</a> - file <tt>Open_Series_As_Image5D("")</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=RGB_to_Image5D&amp;action=edit&amp;redlink=1" class="new" title="RGB to Image5D (page does not exist)">RGB to Image5D</a> - file <tt>RGB_to_Image5D("")</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Save_Image5D&amp;action=edit&amp;redlink=1" class="new" title="Save Image5D (page does not exist)">Save Image5D</a> - file <tt>Save_Image5D("")</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Set_Channel_Display&amp;action=edit&amp;redlink=1" class="new" title="Set Channel Display (page does not exist)">Set Channel Display</a> - file <tt>Set_Channel_Display("")</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Set_Channel_Labels&amp;action=edit&amp;redlink=1" class="new" title="Set Channel Labels (page does not exist)">Set Channel Labels</a> - file <tt>Set_Channel_Labels("")</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Set_Position&amp;action=edit&amp;redlink=1" class="new" title="Set Position (page does not exist)">Set Position</a> - file <tt>Set_Position("")</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Stack_to_Image5D&amp;action=edit&amp;redlink=1" class="new" title="Stack to Image5D (page does not exist)">Stack to Image5D</a> - file <tt>Stack_to_Image5D("")</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Transfer_Channel_Settings&amp;action=edit&amp;redlink=1" class="new" title="Transfer Channel Settings (page does not exist)">Transfer Channel Settings</a> - file <tt>Transfer_Channel_Settings("")</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Virtual_Image5D_Opener&amp;action=edit&amp;redlink=1" class="new" title="Virtual Image5D Opener (page does not exist)">Virtual Image5D Opener</a> - file <tt>Virtual_Image5D_Opener("")</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Z_Project&amp;action=edit&amp;redlink=1" class="new" title="Z Project (page does not exist)">Z Project</a> - file <tt>Z_Project("")</tt>  -- <i>java jar file</i></li></ul>
<p><br>
</p>
<h3><span class="mw-headline" id="Plugins_.3E_Integral_Image_Filters">Plugins &gt; Integral Image Filters</span></h3>
<ul><li> <a href="index.php?title=Mean&amp;action=edit&amp;redlink=1" class="new" title="Mean (page does not exist)">Mean</a> - file <tt>mpicbg.ij.plugin.Mean</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Normalize_Local_Contrast&amp;action=edit&amp;redlink=1" class="new" title="Normalize Local Contrast (page does not exist)">Normalize Local Contrast</a> - file <tt>mpicbg.ij.plugin.NormalizeLocalContrast</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Remove_Outliers&amp;action=edit&amp;redlink=1" class="new" title="Remove Outliers (page does not exist)">Remove Outliers</a> - file <tt>mpicbg.ij.plugin.RemoveOutliers</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Sample_Variance&amp;action=edit&amp;redlink=1" class="new" title="Sample Variance (page does not exist)">Sample Variance</a> - file <tt>mpicbg.ij.plugin.SampleVariance</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Standard_Deviation&amp;action=edit&amp;redlink=1" class="new" title="Standard Deviation (page does not exist)">Standard Deviation</a> - file <tt>mpicbg.ij.plugin.StandardDeviation</tt>  -- <i>java jar file</i></li></ul>
<p><br>
</p>
<h3><span class="mw-headline" id="Plugins_.3E_LOCI">Plugins &gt; LOCI</span></h3>
<ul><li> <a href="LOCI_Plugins_Configuration" class="mw-redirect" title="LOCI Plugins Configuration">LOCI Plugins Configuration</a> - file <tt>loci.plugins.config.LociConfig("")</tt>  -- <i>java jar file</i></li>
<li> <a href="Bio-Formats_Exporter" class="mw-redirect" title="Bio-Formats Exporter">Bio-Formats Exporter</a> - file <tt>loci.plugins.LociExporter("")</tt>  -- <i>java jar file</i></li>
<li> <a href="Bio-Formats_Macro_Extensions" class="mw-redirect" title="Bio-Formats Macro Extensions">Bio-Formats Macro Extensions</a> - file <tt>loci.plugins.macro.LociFunctions("")</tt>  -- <i>java jar file</i></li>
<li> <a href="Bio-Formats_Remote_Importer" class="mw-redirect" title="Bio-Formats Remote Importer">Bio-Formats Remote Importer</a> - file <tt>loci.plugins.LociImporter("location=[Internet]")</tt>  -- <i>java jar file</i></li>
<li> <a href="Bio-Formats_Importer" class="mw-redirect" title="Bio-Formats Importer">Bio-Formats Importer</a> - file <tt>loci.plugins.LociImporter("location=[Local machine] windowless=false ")</tt>  -- <i>java jar file</i></li>
<li> <a href="Bio-Formats_Windowless_Importer" class="mw-redirect" title="Bio-Formats Windowless Importer">Bio-Formats Windowless Importer</a> - file <tt>loci.plugins.LociImporter("location=[Local machine] windowless=true ")</tt>  -- <i>java jar file</i></li>
<li> <a href="LOCI_Plugins_Shortcut_Window" class="mw-redirect" title="LOCI Plugins Shortcut Window">LOCI Plugins Shortcut Window</a> - file <tt>loci.plugins.shortcut.ShortcutPanel("")</tt>  -- <i>java jar file</i></li>
<li> <a href="Stack_Slicer" class="mw-redirect" title="Stack Slicer">Stack Slicer</a> - file <tt>loci.plugins.Slicer("")</tt>  -- <i>java jar file</i></li>
<li> <a href="Update_LOCI_Plugins" class="mw-redirect" title="Update LOCI Plugins">Update LOCI Plugins</a> - file <tt>loci.plugins.Updater("")</tt>  -- <i>java jar file</i></li></ul>
<p><br>
</p>
<h3><span class="mw-headline" id="Plugins_.3E_Landmarks">Plugins &gt; Landmarks</span></h3>
<ul><li> <a href="Name_Landmarks_and_Register" title="Name Landmarks and Register">Name Landmarks and Register</a> - file <tt>landmarks.Name_Points</tt>  -- <i>java jar file</i></li></ul>
<p><br>
</p>
<h3><span class="mw-headline" id="Plugins_.3E_Macros">Plugins &gt; Macros</span></h3>
<ul><li> <a href="index.php?title=About_Plugin_Macros&amp;action=edit&amp;redlink=1" class="new" title="About Plugin Macros (page does not exist)">About Plugin Macros</a> - file <tt>About_Plugin_Macros.txt</tt>  -- <i>macro</i></li>
<li> <a href="index.php?title=Bulls_Eye&amp;action=edit&amp;redlink=1" class="new" title="Bulls Eye (page does not exist)">Bulls Eye</a> - file <tt>Bulls_Eye.txt</tt>  -- <i>macro</i></li>
<li> <a href="index.php?title=Polygon&amp;action=edit&amp;redlink=1" class="new" title="Polygon (page does not exist)">Polygon </a> - file <tt>Polygon_.txt</tt>  -- <i>macro</i></li>
<li> <a href="index.php?title=RGB_Histogram&amp;action=edit&amp;redlink=1" class="new" title="RGB Histogram (page does not exist)">RGB Histogram</a> - file <tt>RGB_Histogram.txt</tt>  -- <i>macro</i></li>
<li> <a href="index.php?title=Batch_convert_any_to_tif&amp;action=edit&amp;redlink=1" class="new" title="Batch convert any to tif (page does not exist)">batch convert any to tif</a> - file <tt>batch_convert_any_to_tif.txt</tt>  -- <i>macro</i></li></ul>
<p><br>
</p>
<h3><span class="mw-headline" id="Plugins_.3E_Optic_Flow">Plugins &gt; Optic Flow</span></h3>
<ul><li> <a href="index.php?title=Integral_Block_MSE&amp;action=edit&amp;redlink=1" class="new" title="Integral Block MSE (page does not exist)">Integral Block MSE</a> - file <tt>mpicbg.ij.plugin.MSEBlockFlow</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Gaussian_Window_MSE&amp;action=edit&amp;redlink=1" class="new" title="Gaussian Window MSE (page does not exist)">Gaussian Window MSE</a> - file <tt>mpicbg.ij.plugin.MSEGaussianFlow</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Integral_Block_PMCC&amp;action=edit&amp;redlink=1" class="new" title="Integral Block PMCC (page does not exist)">Integral Block PMCC</a> - file <tt>mpicbg.ij.plugin.PMCCBlockFlow</tt>  -- <i>java jar file</i></li></ul>
<p><br>
</p>
<h3><span class="mw-headline" id="Plugins_.3E_Process">Plugins &gt; Process</span></h3>
<ul><li> <a href="index.php?title=ImgLib_Algorithm_Launcher&amp;action=edit&amp;redlink=1" class="new" title="ImgLib Algorithm Launcher (page does not exist)">ImgLib Algorithm Launcher</a> - file <tt>AlgorithmLauncher("")</tt>  -- <i>java jar file</i></li>
<li> <a href="Anisotropic_Diffusion_2D" title="Anisotropic Diffusion 2D">Anisotropic Diffusion 2D</a> - file <tt>anisotropic_diffusion.Anisotropic_Diffusion_2D</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Bilateral_Filter&amp;action=edit&amp;redlink=1" class="new" title="Bilateral Filter (page does not exist)">Bilateral Filter</a> - file <tt>Bilateral_Filter</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Convolve_(3D)&amp;action=edit&amp;redlink=1" class="new" title="Convolve (3D) (page does not exist)">Convolve (3D)</a> - file <tt>process3d.Convolve_3d</tt>  -- <i>java jar file</i></li>
<li> <a href="Dilate_(3D)" class="mw-redirect" title="Dilate (3D)">Dilate (3D)</a> - file <tt>process3d.Dilate_</tt>  -- <i>java jar file</i></li>
<li> <a href="Distance_Transform_3D" title="Distance Transform 3D">Distance Transform 3D</a> - file <tt>process3d.Distance_Transform_3D</tt>  -- <i>java jar file</i></li>
<li> <a href="Extended_Depth_of_Field_(Easy_mode)..." class="mw-redirect" title="Extended Depth of Field (Easy mode)...">Extended Depth of Field (Easy mode)...</a> - file <tt>EDF_Easy_</tt>  -- <i>java jar file</i></li>
<li> <a href="Extended_Depth_of_Field_(Expert_mode)..." class="mw-redirect" title="Extended Depth of Field (Expert mode)...">Extended Depth of Field (Expert mode)...</a> - file <tt>EDF_Expert_</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Exact_Euclidean_Distance_Transform_(3D)&amp;action=edit&amp;redlink=1" class="new" title="Exact Euclidean Distance Transform (3D) (page does not exist)">Exact Euclidean Distance Transform (3D)</a> - file <tt>fiji.process3d.EDT</tt>  -- <i>java jar file</i></li>
<li> <a href="Erode_(3D)" class="mw-redirect" title="Erode (3D)">Erode (3D)</a> - file <tt>process3d.Erode_</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Fast_FFT_(2D/3D)&amp;action=edit&amp;redlink=1" class="new" title="Fast FFT (2D/3D) (page does not exist)">Fast FFT (2D/3D)</a> - file <tt>registration3d.Fast_FourierTransform</tt>  -- <i>java jar file</i></li>
<li> <a href="Find_Connected_Regions" title="Find Connected Regions">Find Connected Regions</a> - file <tt>util.Find_Connected_Regions</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Flood_Fill(3D)&amp;action=edit&amp;redlink=1" class="new" title="Flood Fill(3D) (page does not exist)">Flood Fill(3D)</a> - file <tt>process3d.Flood_Fill</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Frangi_Vesselness_(imglib,_experimental)&amp;action=edit&amp;redlink=1" class="new" title="Frangi Vesselness (imglib, experimental) (page does not exist)">Frangi Vesselness (imglib, experimental)</a> - file <tt>fiji.features.Frangi_("")</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Gradient_(3D)&amp;action=edit&amp;redlink=1" class="new" title="Gradient (3D) (page does not exist)">Gradient (3D)</a> - file <tt>process3d.Gradient_</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=IFT_(3D)&amp;action=edit&amp;redlink=1" class="new" title="IFT (3D) (page does not exist)">IFT (3D)</a> - file <tt>process3d.IFT_</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Implicit_Interpolate_Binary&amp;action=edit&amp;redlink=1" class="new" title="Implicit Interpolate Binary (page does not exist)">Implicit Interpolate Binary</a> - file <tt>Implicit_Interpolate_Binary</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Laplace_(3D)&amp;action=edit&amp;redlink=1" class="new" title="Laplace (3D) (page does not exist)">Laplace (3D)</a> - file <tt>process3d.Laplace_</tt>  -- <i>java jar file</i></li>
<li> <a href="Mask_Of_Nearby_Points" title="Mask Of Nearby Points">Mask Of Nearby Points</a> - file <tt>util.Mask_Of_Nearby_Points</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Max_(3D)&amp;action=edit&amp;redlink=1" class="new" title="Max (3D) (page does not exist)">Max (3D)</a> - file <tt>process3d.Maximum_</tt>  -- <i>java jar file</i></li>
<li> <a href="Maximum_(3D)" class="mw-redirect" title="Maximum (3D)">Maximum (3D)</a> - file <tt>process3d.Maximum_</tt>  -- <i>java jar file</i></li>
<li> <a href="Median_(3D)" class="mw-redirect" title="Median (3D)">Median (3D)</a> - file <tt>process3d.Median_</tt>  -- <i>java jar file</i></li>
<li> <a href="Minimum_(3D)" class="mw-redirect" title="Minimum (3D)">Minimum (3D)</a> - file <tt>process3d.Minimum_</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Particle_Analyzer_(3D)&amp;action=edit&amp;redlink=1" class="new" title="Particle Analyzer (3D) (page does not exist)">Particle Analyzer (3D)</a> - file <tt>process3d.Particle_Analyzer_3D</tt>  -- <i>java jar file</i></li>
<li> <a href="Quantile_Based_Normalization" title="Quantile Based Normalization">Quantile Based Normalization</a> - file <tt>util.Quantile_Based_Normalization</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Rebin_(3D)&amp;action=edit&amp;redlink=1" class="new" title="Rebin (3D) (page does not exist)">Rebin (3D)</a> - file <tt>process3d.Rebin_</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Replace_value&amp;action=edit&amp;redlink=1" class="new" title="Replace value (page does not exist)">Replace value</a> - file <tt>Replace_Value</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Resample&amp;action=edit&amp;redlink=1" class="new" title="Resample (page does not exist)">Resample</a> - file <tt>vib.Resample_</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Shape-Based_Averaging_(Experimental)&amp;action=edit&amp;redlink=1" class="new" title="Shape-Based Averaging (Experimental) (page does not exist)">Shape-Based Averaging (Experimental)</a> - file <tt>util.RohlfingSBA</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Shape-based_averaging&amp;action=edit&amp;redlink=1" class="new" title="Shape-based averaging (page does not exist)">Shape-based averaging</a> - file <tt>Rohlfing_SBA</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Exact_Signed_Euclidean_Distance_Transform_(3D)&amp;action=edit&amp;redlink=1" class="new" title="Exact Signed Euclidean Distance Transform (3D) (page does not exist)">Exact Signed Euclidean Distance Transform (3D)</a> - file <tt>fiji.process3d.SEDT</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Seam_remover&amp;action=edit&amp;redlink=1" class="new" title="Seam remover (page does not exist)">Seam remover</a> - file <tt>Seam_Remover</tt>  -- <i>java jar file</i></li>
<li> <a href="Show_Color_Surfaces" title="Show Color Surfaces">Show Color Surfaces</a> - file <tt>isosurface.Show_Colour_Surfaces</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Show_label_centers&amp;action=edit&amp;redlink=1" class="new" title="Show label centers (page does not exist)">Show label centers</a> - file <tt>Show_Label_Centers</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Smooth_(3D)&amp;action=edit&amp;redlink=1" class="new" title="Smooth (3D) (page does not exist)">Smooth (3D)</a> - file <tt>process3d.Smooth_</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Triangle_Algorithm&amp;action=edit&amp;redlink=1" class="new" title="Triangle Algorithm (page does not exist)">Triangle Algorithm</a> - file <tt>Triangle_Algorithm</tt>  -- <i>java jar file</i></li></ul>
<p><br>
</p>
<h3><span class="mw-headline" id="Plugins_.3E_Registration">Plugins &gt; Registration</span></h3>
<ul><li> <a href="Align_Image_by_line_ROI" title="Align Image by line ROI">Align Image by line ROI</a> - file <tt>Align_Image</tt>  -- <i>java jar file</i></li>
<li> <a href="Correct_3D_drift" class="mw-redirect" title="Correct 3D drift">Correct 3D drift</a> - file <tt>Correct_3D_drift.py</tt>  -- <i>jython script</i></li>
<li> <a href="Descriptor-based_registration_(2d/3d)" title="Descriptor-based registration (2d/3d)">Descriptor-based registration (2d/3d)</a> - file <tt>plugin.Descriptor_based_registration</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Descriptor-based_series_registration_(2d/3d_%2B_t)&amp;action=edit&amp;redlink=1" class="new" title="Descriptor-based series registration (2d/3d + t) (page does not exist)">Descriptor-based series registration (2d/3d + t)</a> - file <tt>plugin.Descriptor_based_series_registration</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Manual_landmark_selection_(3d)&amp;action=edit&amp;redlink=1" class="new" title="Manual landmark selection (3d) (page does not exist)">Manual landmark selection (3d)</a> - file <tt>plugin.Manual_Landmark_Selection</tt>  -- <i>java jar file</i></li>
<li> <a href="Moving_Least_Squares" title="Moving Least Squares">Moving Least Squares</a> - file <tt>Moving_Least_Squares</tt>  -- <i>java jar file</i></li>
<li> <a href="Register_Virtual_Stack_Slices" title="Register Virtual Stack Slices">Register Virtual Stack Slices</a> - file <tt>register_virtual_stack.Register_Virtual_Stack_MT</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Rigid_Registration&amp;action=edit&amp;redlink=1" class="new" title="Rigid Registration (page does not exist)">Rigid Registration</a> - file <tt>vib.RigidRegistration_</tt>  -- <i>java jar file</i></li>
<li> <a href="Linear_Stack_Alignment_with_SIFT" title="Linear Stack Alignment with SIFT">Linear Stack Alignment with SIFT</a> - file <tt>SIFT_Align</tt>  -- <i>java jar file</i></li>
<li> <a href="StackReg" title="StackReg">StackReg</a> - file <tt>StackReg_</tt>  -- <i>java jar file</i></li>
<li> <a href="TurboReg" title="TurboReg">TurboReg </a> - file <tt>TurboReg_</tt>  -- <i>java jar file</i></li>
<li> <a href="UnwarpJ" title="UnwarpJ">UnwarpJ</a> - file <tt>UnwarpJ_</tt>  -- <i>java jar file</i></li>
<li> <a href="BUnwarpJ" title="BUnwarpJ">bUnwarpJ</a> - file <tt>bunwarpj.bUnwarpJ_</tt>  -- <i>java jar file</i></li></ul>
<h4><span class="mw-headline" id="Plugins_.3E_Registration_.3E_Elastic">Plugins &gt; Registration &gt; Elastic</span></h4>
<ul><li> <a href="Test_Block_Matching_Parameters" title="Test Block Matching Parameters">Test Block Matching Parameters</a> - file <tt>mpicbg.ij.plugin.BlockMatching_TestParameters</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Elastic_Stack_Alignment&amp;action=edit&amp;redlink=1" class="new" title="Elastic Stack Alignment (page does not exist)">Elastic Stack Alignment</a> - file <tt>mpicbg.ij.plugin.ElasticAlign</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Elastic_Montaging&amp;action=edit&amp;redlink=1" class="new" title="Elastic Montaging (page does not exist)">Elastic Montaging</a> - file <tt>mpicbg.ij.plugin.ElasticMontage</tt>  -- <i>java jar file</i></li></ul>
<p><br>
</p>
<h3><span class="mw-headline" id="Plugins_.3E_SPIM_Registration">Plugins &gt; SPIM Registration</span></h3>
<ul><li> <a href="index.php?title=Bead-based_registration&amp;action=edit&amp;redlink=1" class="new" title="Bead-based registration (page does not exist)">Bead-based registration</a> - file <tt>fiji.plugin.Bead_Registration</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Multi-view_fusion&amp;action=edit&amp;redlink=1" class="new" title="Multi-view fusion (page does not exist)">Multi-view fusion</a> - file <tt>fiji.plugin.Multi_View_Fusion</tt>  -- <i>java jar file</i></li></ul>
<h4><span class="mw-headline" id="Plugins_.3E_SPIM_Registration_.3E_Utilities">Plugins &gt; SPIM Registration &gt; Utilities</span></h4>
<ul><li> <a href="index.php?title=Apply_external_transformation&amp;action=edit&amp;redlink=1" class="new" title="Apply external transformation (page does not exist)">Apply external transformation</a> - file <tt>fiji.plugin.Apply_External_Transformation</tt>  -- <i>java jar file</i></li></ul>
<h4><span class="mw-headline" id="Plugins_.3E_SPIM_Registration_.3E_deprecated">Plugins &gt; SPIM Registration &gt; deprecated</span></h4>
<ul><li> <a href="index.php?title=MultiChannel_Registration&amp;action=edit&amp;redlink=1" class="new" title="MultiChannel Registration (page does not exist)">MultiChannel Registration</a> - file <tt>MultiChannel_SPIM_Registration</tt>  -- <i>java jar file</i></li>
<li> <a href="Registration" title="Registration">Registration</a> - file <tt>SPIM_Registration</tt>  -- <i>java jar file</i></li>
<li> <a href="Advanced_Registration" class="mw-redirect" title="Advanced Registration">Advanced Registration</a> - file <tt>SPIM_Registration_File</tt>  -- <i>java jar file</i></li></ul>
<p><br>
</p>
<h3><span class="mw-headline" id="Plugins_.3E_Scripting">Plugins &gt; Scripting</span></h3>
<ul><li> <a href="BeanShell_Interpreter" class="mw-redirect" title="BeanShell Interpreter">BeanShell Interpreter</a> - file <tt>BSH.BSH_Interpreter</tt>  -- <i>java jar file</i></li>
<li> <a href="Macro_Interpreter" class="mw-redirect" title="Macro Interpreter">Macro Interpreter</a> - file <tt>CLI.CLI_</tt>  -- <i>java jar file</i></li>
<li> <a href="Clojure_Interpreter" class="mw-redirect" title="Clojure Interpreter">Clojure Interpreter</a> - file <tt>Clojure.Clojure_Interpreter</tt>  -- <i>java jar file</i></li>
<li> <a href="JRuby_Interpreter" class="mw-redirect" title="JRuby Interpreter">JRuby Interpreter</a> - file <tt>JRuby.JRuby_Interpreter</tt>  -- <i>java jar file</i></li>
<li> <a href="Javascript_Interpreter" class="mw-redirect" title="Javascript Interpreter">Javascript Interpreter</a> - file <tt>Javascript.Javascript_Interpreter</tt>  -- <i>java jar file</i></li>
<li> <a href="Jython_Interpreter" class="mw-redirect" title="Jython Interpreter">Jython Interpreter</a> - file <tt>Jython.Jython_Interpreter</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Open_Source_for_Menu_Item&amp;action=edit&amp;redlink=1" class="new" title="Open Source for Menu Item (page does not exist)">Open Source for Menu Item</a> - file <tt>fiji.scripting.OpenSourceForMenuItem</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Refresh_BSH_Scripts&amp;action=edit&amp;redlink=1" class="new" title="Refresh BSH Scripts (page does not exist)">Refresh BSH Scripts</a> - file <tt>BSH.Refresh_BSH_Scripts</tt>  -- <i>java jar file</i></li>
<li> <a href="Refresh_Clojure_Scripts" class="mw-redirect" title="Refresh Clojure Scripts">Refresh Clojure Scripts</a> - file <tt>Clojure.Refresh_Clojure_Scripts</tt>  -- <i>java jar file</i></li>
<li> <a href="Refresh_JRuby_Scripts" class="mw-redirect" title="Refresh JRuby Scripts">Refresh JRuby Scripts</a> - file <tt>JRuby.Refresh_JRuby_Scripts</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Refresh_Javas&amp;action=edit&amp;redlink=1" class="new" title="Refresh Javas (page does not exist)">Refresh Javas</a> - file <tt>fiji.scripting.java.Refresh_Javas</tt>  -- <i>java jar file</i></li>
<li> <a href="Refresh_Javascript_Scripts" class="mw-redirect" title="Refresh Javascript Scripts">Refresh Javascript Scripts</a> - file <tt>Javascript.Refresh_Javascript_Scripts</tt>  -- <i>java jar file</i></li>
<li> <a href="Refresh_Jython_Scripts" class="mw-redirect" title="Refresh Jython Scripts">Refresh Jython Scripts</a> - file <tt>Jython.Refresh_Jython_Scripts</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Refresh_Macros&amp;action=edit&amp;redlink=1" class="new" title="Refresh Macros (page does not exist)">Refresh Macros</a> - file <tt>CLI.Refresh_Macros</tt>  -- <i>java jar file</i></li>
<li> <a href="Script_Editor" class="mw-redirect" title="Script Editor">Script Editor</a> - file <tt>fiji.scripting.Script_Editor</tt>  -- <i>java jar file</i></li></ul>
<p><br>
</p>
<h3><span class="mw-headline" id="Plugins_.3E_Segmentation">Plugins &gt; Segmentation</span></h3>
<ul><li> <a href="Balloon" title="Balloon">Balloon</a> - file <tt>BalloonSegmentation_</tt>  -- <i>java jar file</i></li>
<li> <a href="Segment_blob_in_3D_Viewer" title="Segment blob in 3D Viewer">Segment blob in 3D Viewer</a> - file <tt>ij3d.segmentation.Blob_Segmentation_in_3D</tt>  -- <i>java jar file</i></li>
<li> <a href="Graph_Cut" title="Graph Cut">Graph Cut</a> - file <tt>graphcut.Graph_Cut</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Blow/Lasso_Tool&amp;action=edit&amp;redlink=1" class="new" title="Blow/Lasso Tool (page does not exist)">Blow/Lasso Tool</a> - file <tt>plugin.Lasso_</tt>  -- <i>java jar file</i></li>
<li> <a href="Level_Sets" title="Level Sets">Level Sets</a> - file <tt>levelsets.ij.LevelSet</tt>  -- <i>java jar file</i></li>
<li> <a href="Apply_saved_SIOX_segmentator" class="mw-redirect" title="Apply saved SIOX segmentator">Apply saved SIOX segmentator</a> - file <tt>siox.Load_Segmentation</tt>  -- <i>java jar file</i></li>
<li> <a href="Robust_Automatic_Threshold_Selection" class="mw-redirect" title="Robust Automatic Threshold Selection">Robust Automatic Threshold Selection</a> - file <tt>RATS_</tt>  -- <i>java jar file</i></li>
<li> <a href="Statistical_Region_Merging" title="Statistical Region Merging">Statistical Region Merging</a> - file <tt>SRM_</tt>  -- <i>java jar file</i></li>
<li> <a href="Segmentation_Editor" title="Segmentation Editor">Segmentation Editor</a> - file <tt>Segmentation_Editor</tt>  -- <i>java jar file</i></li>
<li> <a href="Simple_Neurite_Tracer" class="mw-redirect" title="Simple Neurite Tracer">Simple Neurite Tracer</a> - file <tt>tracing.Simple_Neurite_Tracer</tt>  -- <i>java jar file</i></li>
<li> <a href="./SIOX:_Simple_Interactive_Object_Extraction" title="SIOX: Simple Interactive Object Extraction">SIOX: Simple Interactive Object Extraction</a> - file <tt>siox.Siox_Segmentation</tt>  -- <i>java jar file</i></li>
<li> <a href="Snakuscule" title="Snakuscule">Snakuscule</a> - file <tt>Snakuscule_</tt>  -- <i>java jar file</i></li>
<li> <a href="Trainable_Segmentation" class="mw-redirect" title="Trainable Segmentation">Trainable Segmentation</a> - file <tt>trainableSegmentation.Trainable_Segmentation</tt>  -- <i>java jar file</i></li>
<li> <a href="Advanced_Weka_Segmentation" class="mw-redirect" title="Advanced Weka Segmentation">Advanced Weka Segmentation</a> - file <tt>trainableSegmentation.Weka_Segmentation</tt>  -- <i>java jar file</i></li></ul>
<p><br>
</p>
<h3><span class="mw-headline" id="Plugins_.3E_Skeleton">Plugins &gt; Skeleton</span></h3>
<ul><li> <a href="Analyze_Skeleton_(2D/3D)" class="mw-redirect" title="Analyze Skeleton (2D/3D)">Analyze Skeleton (2D/3D)</a> - file <tt>skeleton_analysis.AnalyzeSkeleton_</tt>  -- <i>java jar file</i></li>
<li> <a href="Skeletonize_(2D/3D)" class="mw-redirect" title="Skeletonize (2D/3D)">Skeletonize (2D/3D)</a> - file <tt>Skeletonize3D_.Skeletonize3D_</tt>  -- <i>java jar file</i></li></ul>
<p><br>
</p>
<h3><span class="mw-headline" id="Plugins_.3E_Stacks">Plugins &gt; Stacks</span></h3>
<ul><li> <a href="Average_Images" title="Average Images">Average Images</a> - file <tt>vib.Average_Images</tt>  -- <i>java jar file</i></li>
<li> <a href="Crop_(3D)" title="Crop (3D)">Crop (3D)</a> - file <tt>stacks.Three_Pane_Crop</tt>  -- <i>java jar file</i></li></ul>
<p><br>
</p>
<h3><span class="mw-headline" id="Plugins_.3E_Stitching">Plugins &gt; Stitching</span></h3>
<ul><li> <a href="MosaicJ" title="MosaicJ">MosaicJ</a> - file <tt>MosaicJ_</tt>  -- <i>java jar file</i></li>
<li> <a href="Grid/Collection_stitching" class="mw-redirect" title="Grid/Collection stitching">Grid/Collection stitching</a> - file <tt>plugin.Stitching_Grid</tt>  -- <i>java jar file</i></li>
<li> <a href="Pairwise_stitching" class="mw-redirect" title="Pairwise stitching">Pairwise stitching</a> - file <tt>plugin.Stitching_Pairwise</tt>  -- <i>java jar file</i></li></ul>
<h4><span class="mw-headline" id="Plugins_.3E_Stitching_.3E_deprecated">Plugins &gt; Stitching &gt; deprecated</span></h4>
<ul><li> <a href="Stitch_Collection_of_Images" class="mw-redirect" title="Stitch Collection of Images">Stitch Collection of Images</a> - file <tt>Stitch_Image_Collection</tt>  -- <i>java jar file</i></li>
<li> <a href="Stitch_Directory_with_Images_(unknown_configuration)" class="mw-redirect" title="Stitch Directory with Images (unknown configuration)">Stitch Directory with Images (unknown configuration)</a> - file <tt>Stitch_Image_Directory</tt>  -- <i>java jar file</i></li>
<li> <a href="Stitch_Grid_of_Images" class="mw-redirect" title="Stitch Grid of Images">Stitch Grid of Images</a> - file <tt>Stitch_Image_Grid</tt>  -- <i>java jar file</i></li>
<li> <a href="Stitch_Sequence_of_Grids_of_Images" class="mw-redirect" title="Stitch Sequence of Grids of Images">Stitch Sequence of Grids of Images</a> - file <tt>Stitch_Image_Grid_Sequence</tt>  -- <i>java jar file</i></li>
<li> <a href="Stitch_Multiple_Series_or_Tile_Scan_File" class="mw-redirect" title="Stitch Multiple Series or Tile Scan File">Stitch Multiple Series or Tile Scan File</a> - file <tt>Stitch_Multiple_Series_File</tt>  -- <i>java jar file</i></li>
<li> <a href="2D_Stitching" class="mw-redirect" title="2D Stitching">2D Stitching</a> - file <tt>Stitching_2D</tt>  -- <i>java jar file</i></li>
<li> <a href="3D_Stitching" class="mw-redirect" title="3D Stitching">3D Stitching</a> - file <tt>Stitching_3D</tt>  -- <i>java jar file</i></li></ul>
<p><br>
</p>
<h3><span class="mw-headline" id="Plugins_.3E_Tracking">Plugins &gt; Tracking</span></h3>
<ul><li> <a href="MTrack2" title="MTrack2">MTrack2 </a> - file <tt>MTrack2_</tt>  -- <i>java jar file</i></li>
<li> <a href="Manual_Tracking" title="Manual Tracking">Manual Tracking</a> - file <tt>Manual_Tracking</tt>  -- <i>java jar file</i></li>
<li> <a href="ToAST" title="ToAST">ToAST</a> - file <tt>ToAST25_</tt>  -- <i>java jar file</i></li>
<li> <a href="TrackMate" title="TrackMate">TrackMate</a> - file <tt>fiji.plugin.trackmate.TrackMate_</tt>  -- <i>java jar file</i></li></ul>
<p><br>
</p>
<h3><span class="mw-headline" id="Plugins_.3E_Transform">Plugins &gt; Transform</span></h3>
<ul><li> <a href="Distortion_Correction" title="Distortion Correction">Distortion Correction</a> - file <tt>lenscorrection.Distortion_Correction</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Panorama_equirectangular_view&amp;action=edit&amp;redlink=1" class="new" title="Panorama equirectangular view (page does not exist)">Panorama equirectangular view</a> - file <tt>mpicbg.panorama.Panorama_View</tt>  -- <i>java jar file</i></li>
<li> <a href="Spline_Deformation_Generator" title="Spline Deformation Generator">Spline Deformation Generator</a> - file <tt>SplineDeformationGenerator.SplineDeformationGenerator_</tt>  -- <i>java jar file</i></li>
<li> <a href="Interactive_Stack_Rotation" title="Interactive Stack Rotation">Interactive Stack Rotation</a> - file <tt>Stack_Rotate</tt>  -- <i>java jar file</i></li>
<li> <a href="Interactive_Affine" title="Interactive Affine">Interactive Affine</a> - file <tt>Transform_Affine</tt>  -- <i>java jar file</i></li>
<li> <a href="Interactive_Moving_Least_Squares" title="Interactive Moving Least Squares">Interactive Moving Least Squares</a> - file <tt>Transform_MovingLeastSquaresMesh</tt>  -- <i>java jar file</i></li>
<li> <a href="Interactive_Perspective" title="Interactive Perspective">Interactive Perspective</a> - file <tt>Transform_Perspective</tt>  -- <i>java jar file</i></li>
<li> <a href="Interactive_Rigid" title="Interactive Rigid">Interactive Rigid</a> - file <tt>Transform_Rigid</tt>  -- <i>java jar file</i></li>
<li> <a href="Landmark_Correspondences" title="Landmark Correspondences">Landmark Correspondences</a> - file <tt>Transform_Roi</tt>  -- <i>java jar file</i></li>
<li> <a href="Interactive_Similarity" title="Interactive Similarity">Interactive Similarity</a> - file <tt>Transform_Similarity</tt>  -- <i>java jar file</i></li>
<li> <a href="Transform_Virtual_Stack_Slices" title="Transform Virtual Stack Slices">Transform Virtual Stack Slices</a> - file <tt>register_virtual_stack.Transform_Virtual_Stack_MT</tt>  -- <i>java jar file</i></li></ul>
<h4><span class="mw-headline" id="Plugins_.3E_Transform_.3E_TransformJ">Plugins &gt; Transform &gt; TransformJ</span></h4>
<ul><li> <a href="index.php?title=TransformJ_Affine&amp;action=edit&amp;redlink=1" class="new" title="TransformJ Affine (page does not exist)">TransformJ Affine</a> - file <tt>TJ_Affine</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=TransformJ_Crop&amp;action=edit&amp;redlink=1" class="new" title="TransformJ Crop (page does not exist)">TransformJ Crop</a> - file <tt>TJ_Crop</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=TransformJ_Embed&amp;action=edit&amp;redlink=1" class="new" title="TransformJ Embed (page does not exist)">TransformJ Embed</a> - file <tt>TJ_Embed</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=TransformJ_Matrix&amp;action=edit&amp;redlink=1" class="new" title="TransformJ Matrix (page does not exist)">TransformJ Matrix</a> - file <tt>TJ_Matrix</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=TransformJ_Mirror&amp;action=edit&amp;redlink=1" class="new" title="TransformJ Mirror (page does not exist)">TransformJ Mirror</a> - file <tt>TJ_Mirror</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=TransformJ_Options&amp;action=edit&amp;redlink=1" class="new" title="TransformJ Options (page does not exist)">TransformJ Options</a> - file <tt>TJ_Options</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=TransformJ_Panel&amp;action=edit&amp;redlink=1" class="new" title="TransformJ Panel (page does not exist)">TransformJ Panel</a> - file <tt>TJ_Panel</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=TransformJ_Rotate&amp;action=edit&amp;redlink=1" class="new" title="TransformJ Rotate (page does not exist)">TransformJ Rotate</a> - file <tt>TJ_Rotate</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=TransformJ_Scale&amp;action=edit&amp;redlink=1" class="new" title="TransformJ Scale (page does not exist)">TransformJ Scale</a> - file <tt>TJ_Scale</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=TransformJ_Translate&amp;action=edit&amp;redlink=1" class="new" title="TransformJ Translate (page does not exist)">TransformJ Translate</a> - file <tt>TJ_Translate</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=TransformJ_Turn&amp;action=edit&amp;redlink=1" class="new" title="TransformJ Turn (page does not exist)">TransformJ Turn</a> - file <tt>TJ_Turn</tt>  -- <i>java jar file</i></li></ul>
<p><br>
</p>
<h3><span class="mw-headline" id="Plugins_.3E_Utilities">Plugins &gt; Utilities</span></h3>
<ul><li> <a href="CPU_Meter" title="CPU Meter">CPU Meter</a> - file <tt>CPU_Meter</tt>  -- <i>java jar file</i></li>
<li> <a href="Close_All_Without_Saving" title="Close All Without Saving">Close All Without Saving</a> - file <tt>Close_All_Without_Saving.txt</tt>  -- <i>macro</i></li>
<li> <a href="index.php?title=Collect_Garbage&amp;action=edit&amp;redlink=1" class="new" title="Collect Garbage (page does not exist)">Collect Garbage</a> - file <tt>CollectGarbage_</tt>  -- <i>java jar file</i></li>
<li> <a href="IJ_Robot" title="IJ Robot">IJ Robot</a> - file <tt>IJ_Robot</tt>  -- <i>java jar file</i></li>
<li> <a href="Make_Fiji_Package" title="Make Fiji Package">Make Fiji Package</a> - file <tt>fiji.packaging.Package_Maker</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Repeat_a_Recent_Command&amp;action=edit&amp;redlink=1" class="new" title="Repeat a Recent Command (page does not exist)">Repeat a Recent Command</a> - file <tt>fiji.util.Recent_Commands</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Thread_killer&amp;action=edit&amp;redlink=1" class="new" title="Thread killer (page does not exist)">Thread killer</a> - file <tt>Thread_Killer</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Record_Desktop&amp;action=edit&amp;redlink=1" class="new" title="Record Desktop (page does not exist)">Record Desktop</a> - file <tt>Jython.Refresh_Jython_Scripts("../scripts/Record_Desktop.py")</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Record_Window&amp;action=edit&amp;redlink=1" class="new" title="Record Window (page does not exist)">Record Window</a> - file <tt>Jython.Refresh_Jython_Scripts("../scripts/Record_Window.py")</tt>  -- <i>java jar file</i></li></ul>
<h4><span class="mw-headline" id="Plugins_.3E_Utilities_.3E_Debugging">Plugins &gt; Utilities &gt; Debugging</span></h4>
<ul><li> <a href="index.php?title=Test_Marching_Cubes&amp;action=edit&amp;redlink=1" class="new" title="Test Marching Cubes (page does not exist)">Test Marching Cubes</a> - file <tt>MC_Test</tt>  -- <i>java jar file</i></li>
<li> <a href="Test_Java3D" title="Test Java3D">Test Java3D</a> - file <tt>Test_Java3D</tt>  -- <i>java jar file</i></li></ul>
<h4><span class="mw-headline" id="Plugins_.3E_Utilities_.3E_Fiji">Plugins &gt; Utilities &gt; Fiji</span></h4>
<ul><li> <a href="index.php?title=Inspect_Java_Objects&amp;action=edit&amp;redlink=1" class="new" title="Inspect Java Objects (page does not exist)">Inspect Java Objects</a> - file <tt>fiji.debugging.Object_Inspector</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=Upload_Image_to_Fiji_Wiki&amp;action=edit&amp;redlink=1" class="new" title="Upload Image to Fiji Wiki (page does not exist)">Upload Image to Fiji Wiki</a> - file <tt>fiji.Upload_Image_To_Wiki</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=New_Fiji_News&amp;action=edit&amp;redlink=1" class="new" title="New Fiji News (page does not exist)">New Fiji News</a> - file <tt>fiji.Wiki_Editor("news")</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=New_Fiji_Wiki_Screenshot&amp;action=edit&amp;redlink=1" class="new" title="New Fiji Wiki Screenshot (page does not exist)">New Fiji Wiki Screenshot</a> - file <tt>fiji.Wiki_Editor("screenshot")</tt>  -- <i>java jar file</i></li>
<li> <a href="New_Fiji_Tutorial" class="mw-redirect" title="New Fiji Tutorial">New Fiji Tutorial</a> - file <tt>fiji.Wiki_Editor("tutorial-maker")</tt>  -- <i>java jar file</i></li></ul>
<p><br>
</p>
<h2><span class="mw-headline" id="Process">Process</span></h2>
<ul><li> <a href="Calculator_Plus" title="Calculator Plus">Calculator Plus</a> - file <tt>Calculator_Plus</tt>  -- <i>java jar file</i></li>
<li> <a href="Image_Expression_Parser" title="Image Expression Parser">Image Expression Parser</a> - file <tt>fiji.process.Image_Expression_Parser</tt>  -- <i>java jar file</i></li>
<li> <a href="Multiple_Image_Processor" title="Multiple Image Processor">Multiple Image Processor</a> - file <tt>MultipleImageProcessor</tt>  -- <i>java jar file</i></li>
<li> <a href="Enhance_Local_Contrast_(CLAHE)" title="Enhance Local Contrast (CLAHE)">Enhance Local Contrast (CLAHE)</a> - file <tt>mpicbg.ij.clahe.PlugIn</tt>  -- <i>java jar file</i></li></ul>
<p><br>
</p>
<h3><span class="mw-headline" id="Process_.3E_Filters">Process &gt; Filters</span></h3>
<ul><li> <a href="Differentials" title="Differentials">Differentials</a> - file <tt>Differentials_</tt>  -- <i>java jar file</i></li>
<li> <a href="Linear_Kuwahara" title="Linear Kuwahara">Linear Kuwahara</a> - file <tt>Kuwahara_LinearStructure_Filter_v3</tt>  -- <i>java jar file</i></li></ul>
<p><br>
</p>
<h3><span class="mw-headline" id="Process_.3E_Morphology">Process &gt; Morphology</span></h3>
<ul><li> <a href="Gray_Morphology" title="Gray Morphology">Gray Morphology</a> - file <tt>GrayMorphology_</tt>  -- <i>java jar file</i></li></ul>
<p><br>
</p>
<h3><span class="mw-headline" id="Process_.3E_Noise">Process &gt; Noise</span></h3>
<ul><li> <a href="index.php?title=ROF_Denoise&amp;action=edit&amp;redlink=1" class="new" title="ROF Denoise (page does not exist)">ROF Denoise</a> - file <tt>fiji.denoise.ROF_Denoise</tt>  -- <i>java jar file</i></li></ul>
<h4><span class="mw-headline" id="Process_.3E_Noise_.3E_RandomJ">Process &gt; Noise &gt; RandomJ</span></h4>
<ul><li> <a href="index.php?title=RandomJ_Binomial&amp;action=edit&amp;redlink=1" class="new" title="RandomJ Binomial (page does not exist)">RandomJ Binomial</a> - file <tt>RJ_Binomial</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=RandomJ_Exponential&amp;action=edit&amp;redlink=1" class="new" title="RandomJ Exponential (page does not exist)">RandomJ Exponential</a> - file <tt>RJ_Exponential</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=RandomJ_Gamma&amp;action=edit&amp;redlink=1" class="new" title="RandomJ Gamma (page does not exist)">RandomJ Gamma</a> - file <tt>RJ_Gamma</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=RandomJ_Gaussian&amp;action=edit&amp;redlink=1" class="new" title="RandomJ Gaussian (page does not exist)">RandomJ Gaussian</a> - file <tt>RJ_Gaussian</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=RandomJ_Options&amp;action=edit&amp;redlink=1" class="new" title="RandomJ Options (page does not exist)">RandomJ Options</a> - file <tt>RJ_Options</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=RandomJ_Panel&amp;action=edit&amp;redlink=1" class="new" title="RandomJ Panel (page does not exist)">RandomJ Panel</a> - file <tt>RJ_Panel</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=RandomJ_Poisson&amp;action=edit&amp;redlink=1" class="new" title="RandomJ Poisson (page does not exist)">RandomJ Poisson</a> - file <tt>RJ_Poisson</tt>  -- <i>java jar file</i></li>
<li> <a href="index.php?title=RandomJ_Uniform&amp;action=edit&amp;redlink=1" class="new" title="RandomJ Uniform (page does not exist)">RandomJ Uniform</a> - file <tt>RJ_Uniform</tt>  -- <i>java jar file</i></li></ul>

<!--
NewPP limit report
Cached time: 20200713073922
Cache expiry: 86400
Dynamic content: false
CPU time usage: 0.080 seconds
Real time usage: 0.086 seconds
Preprocessor visited node count: 266/1000000
Preprocessor generated node count: 272/1000000
Post‐expand include size: 0/2097152 bytes
Template argument size: 0/2097152 bytes
Highest expansion depth: 2/40
Expensive parser function count: 0/3
-->

<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%    0.000      1 - -total
-->
</div>
