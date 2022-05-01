---
title: Excel Functions
description: Functions to save basic ImageJ tables as well as arrays in .xlsx worksheets as well as add images and plots to Excel worksheets
project: /plugins/excel-functions
name: Jan Brocher
affiliation: BioVoxxel
website: https://www.biovoxxel.de
repository: https://mvnrepository.com/artifact/de.biovoxxel/excel.macro.extensions
source-url: https://gitlab.com/biovoxxel/excel-table-macro-extensions/-/tree/main/excel.macro.extensions
pom-url: https://gitlab.com/biovoxxel/excel-table-macro-extensions/-/blob/main/excel.macro.extensions/pom.xml
---

# ImageJ Excel Macro Extensions

<a name="introduction"></a>
## Introduction
The Excel macro extensions for ImageJ and Fiji are meant to make saving results tables in ImageJ and Fiji easily accessible on various different levels:

- ImageJ2 / Fiji menu commands (fully recordable)
- ImageJ macro language including the usage of auto-completion
- Access via Java
- Access via Jython (Python)
- [Headless command line](https://imagej.net/learn/headless#running-macros-in-headless-mode) accessibility via running a pre-designed macro using the extension functions is the easiest solution

### Remarks
_I am also fully aware of the existance and similarity to the [Read and Write Excel plugin](https://imagej.net/plugins/read-and-write-excel)_
However, I wanted to create something, which could be useable in different ways to connect Imagej with Excel as well as make it simpler to use from the macro language. So, it is rather complementary. One current advantage is being able to add images as well as ImageJ data plots into any Excel workbook sheet as desired. 
Drawback of adding images to Excel is that they mostly appear horizontally distorted. This is not solvable via the [Apache POI](https://poi.apache.org/) used as dependency for this extensions. But right-clicking in Excel on the respective image and choosing the image settings for "size and position" pressing the "Reset" button will set the correct image aspect ratio. There is currently no function more convenient than that.
Limitation regarding data plots is that the Apache POI library still has some difficulties or missing functions to fully enable the seamless transfer of data plots into Excel. Therefore, a saved plot might need to be optically adjusted in Excel directly.

### Usage via the ImageJ2 / Fiji menu
Most implemented functions also come with a menu entry which can easily be used by non-programmers directly in the Fiji (and ImageJ2) UI. Those functions are fully recordable by the ImageJ macro recorder and can thus be used even without any knowledge of the IJ macro language.

### Usage via IJ Macro Extensions
The first and foremost command to be able to use the extensions is to record or add `run("Excel Macro Extensions");`. This "installs" the extensions and makes them accessible via the script editor by using the auto-completion supported commands. There are few commands which are only accessible via the macro extensions but not via the menu commands (such as `Ext.xlsx_GetAllWorkbookSheetNames(dir);`). However, both methods can also be combined if desired.
The ImageJ macro language auto-completion support is added thanks to the amazing description from Robert Haase [Extending ImageJ Macro auto completion in Fijis script editor](https://github.com/haesleinhuepf/extend-macro-autocompletion). This makes it super easy especially for beginners using it directly from the script editor.

### Usage as Java library
The publically accessible [ExcelFunctions](https://gitlab.com/biovoxxel/excel-table-macro-extensions/-/blob/main/excel.macro.extensions/src/main/java/excel/functions/plugins/ExcelFunctions.java) allow Java developers as well as users who prefer scripting ImageJ routines in Python (Jython) to access all current functionalities supportes. The [ExcelUtils](https://gitlab.com/biovoxxel/excel-table-macro-extensions/-/blob/main/excel.macro.extensions/src/main/java/excel/functions/utils/ExcelUtils.java) options in Java (not tested yet) give some finer level of interaction but this should not be necessary to be used in case of an image analysis routine.

### Usage via Jython (Python 2)
Since ImageJ2/Fiji also can be scripted viy Python, the functions of this extensions are available in the same way as mentioned for the Java library usage. ExcelFunctions (and ExcelUtils respectively) need to be imported and can then be used right out of the box.

## Development
In case you have any wishes or use cases which currently are not covered by the existing functionality, feel free to [contact me](mailto:jan.brocher@biovoxxel.de) and we can add your idea to the wish-list for upcoming future versions. Regarding any issues, either contact me or create a new issue [here](https://gitlab.com/biovoxxel/excel-table-macro-extensions/-/issues)

## Installation
The **Excel Macro Extension** can be installed the Fiji update site _Excel Functions_. To be able to install it do as follows:
* Running Fiji start _→Help →Update..._
* Click the **Manage update sites** button
* In the new popup window search for the site names _Excel Functions_ and activate the checkbox
* Press the **Close** button
* Finally, press the **Apply changes** button and restart Fiji after the successful update... 
* The Excel Functions are appearing under the menu _Plugins > Excel Functions_

Done! Congratulations and happy data saving!

***Known issue: If additionally the *Read and Write Excel plugin* is installed in parallel the two will clash. Make sure to just install the Excel Macro Extension alone to ensure full functionality.***


## Usage Examples
### Macro Extension Example
```java
run("Excel Macro Extensions");  //necessary to be able to use the extension commands

dir = getDirectory("home") + "Desktop/Test.xlsx";

if (File.exists(dir)) {
	deleted = File.delete(dir);
}
run("Set Measurements...", "area mean standard modal min centroid center perimeter bounding fit shape feret's integrated median skewness kurtosis area_fraction display redirect=None decimal=3");
setOption("BlackBackground", true);
run("Blobs (25K)");
run("Make Binary");
blobImageID = getImageID();

run("Analyze Particles...", "display exclude clear summarize");
Plot.create("Plot_of_Results", "x", "Area");
Plot.add("Separated Bars", Table.getColumn("Area", "Results"));
Plot.setStyle(0, "blue,#a0a0ff,1.0,Separated Bars");
Plot.show();
plotImageID = getImageID();

Ext.xlsx_SaveAllTablesToWorkbook(dir, true);
Ext.xlsx_AppendTableAsRows("Results", dir, 0, false);
Ext.xlsx_SaveTableAsWorksheet("Results", dir, "WithSheetName", true);
Ext.xlsx_AddImageToWorksheet(blobImageID, dir, 0, 5, 5);
Ext.xlsx_AddExcelChartFromPlot(dir, 1, "AREA"); //experimental
Ext.xlsx_AddImageToWorksheet(plotImageID, dir, 1, -1, -1);
Ext.xlsx_AppendArrayAsExcelColumn(newArray("Heading","b","c","d","e","f","g","h"), dir, 1, 0);
Ext.xlsx_AppendArrayAsExcelRow(newArray(0,1,2,3,4,5,6,7,8,9), dir, 1, 1);
close("*");
close("Results");
close("Summary");

Ext.xlsx_SetColumnDataFormat(dir, 2, 3, "@");

workSheetNameString = Ext.xlsx_GetAllWorkbookSheetNames(dir);
workSheetNames = split(workSheetNameString, ",");
for (i = 0; i < workSheetNames.length; i++) {
	Ext.xlsx_ImportXlsxWorksheetAsTable(dir, workSheetNames[i], true);
}
``` 

### Macro Auto Completion usage
To be able to use the ImageJ excel table macro extension the macro needs to contain `run("Excel Macro Extensions");` before any the the excel related commands can be recognized and executed. Typing `xlsx` in the script editor should bring up the auto completion window with all the currently possible extension commands and related explanations.

![Image](https://www.biovoxxel.de/images/wiki_documentation/ExcelMacroExtension_AutoCompletion.png)

### Java Example
To code plugins in Java one can add the following dependency in to the POM file of ones Maven Project. Always check out the newest version number e.g. on [MVNRepository](https://mvnrepository.com/artifact/de.biovoxxel/excel.macro.extensions).

```
<dependency>
  <groupId>de.biovoxxel</groupId>
  <artifactId>excel.macro.extensions</artifactId>
  <version>3.2.1</version> <!-- adapt to most recent version -->
</dependency>
```

Therafter, importing the `excel.functions.plugins.ExcelFunctions` should enable you to make use of the [ExcelFunctions](https://gitlab.com/biovoxxel/excel-table-macro-extensions/-/blob/main/excel.macro.extensions/src/main/java/excel/functions/plugins/ExcelFunctions.java) options.
Furthermore, the [ExcelUtils](https://gitlab.com/biovoxxel/excel-table-macro-extensions/-/blob/main/excel.macro.extensions/src/main/java/excel/functions/utils/ExcelUtils.java) contain additional `public` methods which might be helpful when creating a plugin, but are not necessary for the general functionality of the ExcelFunctions. They are rather used internally by the latter.

```java
package my.awesome.pckg;
import java.io.File;

import org.apache.poi.xddf.usermodel.chart.ChartTypes;

import excel.functions.plugins.ExcelFunctions;
import ij.IJ;
import ij.ImagePlus;
import ij.Prefs;
import ij.WindowManager;
import ij.gui.Plot;
import ij.measure.Measurements;
import ij.measure.ResultsTable;
import ij.plugin.filter.ParticleAnalyzer;

public class IJExcelFunctionsJavaExample {
	
    private static ResultsTable RESULTS_TABLE = new ResultsTable();
    private static ResultsTable SUMMARY_TABLE = new ResultsTable();
    private static final boolean INCLUDE_HEADINGS = true;
    private static final int ROW_NUMBER = 5;
    private static final int COLUMN_NUMBER = 10;
    private static final int STARTING_COLUMN = 0;
    private static final int STARTING_ROW = 0;
    private static final String DATA_FORMAT_STRING = "@";  //The @ sign stands for "Text" formatting of cells
    private static File WORKBOOK_FILE = new File(IJ.getDirectory("home") + "Desktop/Test.xlsx");
    
    public static void main(String[] args) {
        
    	Prefs.blackBackground = true;
    	IJ.run("Blobs (25K)");
        IJ.run("Make Binary");
        ImagePlus imp = WindowManager.getCurrentImage();
		    	
        ParticleAnalyzer.setSummaryTable(SUMMARY_TABLE);
        int CURRENT_PA_OPTIONS = ParticleAnalyzer.CLEAR_WORKSHEET|ParticleAnalyzer.RECORD_STARTS|ParticleAnalyzer.SHOW_MASKS|ParticleAnalyzer.SHOW_SUMMARY;
        int MEASUREMENT_PA_FLAGS = Measurements.AREA|Measurements.MEAN|Measurements.STD_DEV|Measurements.MODE|Measurements.MIN_MAX|Measurements.CENTROID|Measurements.CENTER_OF_MASS|Measurements.PERIMETER|Measurements.RECT|Measurements.ELLIPSE|Measurements.SHAPE_DESCRIPTORS|Measurements.FERET|Measurements.INTEGRATED_DENSITY|Measurements.MEDIAN|Measurements.SKEWNESS|Measurements.KURTOSIS|Measurements.AREA_FRACTION|Measurements.STACK_POSITION|Measurements.LIMIT|Measurements.LABELS;
		
        ParticleAnalyzer pa = new ParticleAnalyzer(CURRENT_PA_OPTIONS, MEASUREMENT_PA_FLAGS, RESULTS_TABLE, 0, Double.POSITIVE_INFINITY);
        pa.setHideOutputImage(true);
        pa.analyze(imp);
        
        RESULTS_TABLE.show("CompleteResults");
        SUMMARY_TABLE.show("Summary");
        
        ExcelFunctions.saveAllOpenTablesAsWorkbookSheets(WORKBOOK_FILE, INCLUDE_HEADINGS);
        ExcelFunctions.addImageToWorkbookSheet(imp, WORKBOOK_FILE, 1, COLUMN_NUMBER, ROW_NUMBER);
        
        Plot plot = new Plot("TestPlot", "X", "Y");
        plot.add("circle", RESULTS_TABLE.getColumnAsDoubles(1), RESULTS_TABLE.getColumnAsDoubles(11));
        plot.show();
        plot.setStyle(0, "black,black,1,circle");
        ExcelFunctions.addPlotToWorksheet(WORKBOOK_FILE, 1, plot, ChartTypes.AREA);
        
        //individual arrays can be added as columns or rows as follows
        String[] stringArray = new String[] {"a", "b", "c", "d", "e", "f", "g"};
        ExcelFunctions.appendArrayAsExcelColumn(stringArray, WORKBOOK_FILE, "NewSheet", STARTING_ROW);
        
        Number[] numberArray = new Number[] {1.2f,2.565f,334.6d,3.0d,5,6,7,8,9};    //different primitive number formats will finally be converted to doubles in Excel
        ExcelFunctions.appendArrayAsExcelRow(numberArray, WORKBOOK_FILE, 2, STARTING_COLUMN);
        
        //specify the data format of specific columns
        ExcelFunctions.setColumnDataFormat(WORKBOOK_FILE, 0, 0, DATA_FORMAT_STRING);
        
    }
}
```

### Python (Jython) Example
In Python/Jython once the Excel Macro Extension update site is installed and the related .jar file is present in your Fiji/ImageJ installations' plugins folder, the code can be equivalently be used as shown for the Java plugins. _The python usage is currently still not fully tested. So, please [contact me](mailto:jan.brocher@biovoxxel.de) of file an [issue](https://gitlab.com/biovoxxel/excel-table-macro-extensions/-/issues) in case you encounter any issues._


```python
from ij import IJ
from excel.functions.plugins import ExcelFunctions

//code of your analysis leading to ImageJ ResultsTables (e.g. named "Results") and/or ImagePlus instances you want to save in Excel files.

ExcelFunctions.saveTableAsWorkbookSheet("Results", "C:/path/to/excel/file.xlsx", "sheet_name_or_index_as_string", 1)
ExcelFunctions.addImageToWorksheet(imp, "C:/path/to/excel/file.xlsx", "sheet_name_or_index_as_string", 5, 5)
...

```
