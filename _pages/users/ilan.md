---
title: Ilan Tal
name: Ilan Tal
email: ilan.tal@gmail.com
github: ilan
---

## Installation

After installing Fiji, go to {% include bc path="Help | Update... | Manage update site" %} and select "PET-CT" and click {% include button label="Apply changes" %}.

This will bring up a list of all plugins, not all of which need be installed. For example you may not want `Read_ClearCanvas_Studies.jar` and/or `Read_BI_Studies.jar.` In such cases click on "Status/Action" and choose "Keep as-is"

### The software

-   `Pet_Ct_Viewer.jar`
    This is the basic package needed by all other plugins. [Help](http://sourceforge.net/p/bifijiplugins/wiki/Pet-Ct%20Viewer/)
-   `Read_CD.jar`
    This reads from multiple sources and automatically calls Pet Ct Viewer if appropriate. [Help](http://sourceforge.net/p/bifijiplugins/wiki/CD%20Dialog/)
-   `Gastric_Emptying.jar`
    This contains multiple Nuclear Medicine and general purpose programs:

    -   Gastric Emptying [Help](http://sourceforge.net/p/bifijiplugins/wiki/Gastric%20Emptying/)
    -   Renal Clearance [Help](http://sourceforge.net/p/bifijiplugins/wiki/Renal%20Clearance/)
    -   Save As Dicom [Help](http://sourceforge.net/p/bifijiplugins/wiki/Save%20as%20myDicom/)
    -   Postage Stamps [Help](http://sourceforge.net/p/bifijiplugins/wiki/Postage%20stamps/)
    -   Mask [Help](http://sourceforge.net/p/bifijiplugins/wiki/Mask/)
-   `Read_BI_Studies.jar`
    This is for read-write to the Beth Israel miniPacs. [Help](http://sourceforge.net/p/bifijiplugins/wiki/Reading%20studies/) The program to set up the database [createBIdatabase.jar](http://sourceforge.net/projects/bifijiplugins/files/) is not part of Fiji and needs to be downloaded and run separately. [Help](http://sourceforge.net/p/bifijiplugins/wiki/BI%20Database/)
-   `Read_ClearCanvas_Studies.jar`
    This is used for reading Clear Canvas studies. [Help](http://sourceforge.net/p/bifijiplugins/wiki/Clear%20Canvas%20Dialog/)
-   `StartupMacros.ijm`
    This is the suggested list of programs to automatically start when Fiji is started.

For questions please contact me at ilan.tal@gmail.com
