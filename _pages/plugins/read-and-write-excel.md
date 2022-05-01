---
mediawiki: Read_and_Write_Excel
title: Read and Write Excel
categories: [Import-Export]
---

{% capture source%}
{% include github org='antinos' repo='Read_and_Write_Excel_Modified' %}
{% endcapture %}
{% include info-box name='Read and Write Excel' software='ImageJ/Fiji' latest-version='1.1.7' author='Anthony Sinadinos, Brenden Kromhout' maintainer='Anthony Sinadinos [(antinos)](https://forum.image.sc/u/antinos/)' source=source category='Plugins' website=' [Youtube tutorial](https://www.youtube.com/watch?v=dLkoB25MTIY)' %}

## Introduction

By default, this plugin extracts data from the Results Table and adds it to a sheet-tab "A" in an .xlsx Excel file on the user's desktop. The plugin will create a file named "Rename me after writing is done" on the desktop if none-exists already, and will update this file if it has already been created. Data is added to the latest sheet (created as "A" if the file is new) or to a user specified sheet using a passed argument (see below). Within the latest sheet, data will be added adjacent to previous data, unless an argument is passed to stack data underneath pre-existing column headers and data. Results Table column headers are added automatically. A row count is added by default but the user can choose to deny this with a passed argument.

Created in Eclipse IDE. Requires jre 1.8, which is current ImageJ compatible.

{% capture version-release-table %}
| Version | Release Date | Notes |
|---|---|---|
| v1.0.0  | 19 Nov 2015 |      |
| v1.0.1  | 25 Nov 2015 |      |
| v1.0.2  | 10 Apr 2017 |      |
| v1.1.0  | 27 Feb 2018 | <span style="font-size:80%; line-height: 0.9em;">This version contains many new features that have been added by <a href="https://github.com/bkromhout">Brenden Kromhout</a></span> |
| v1.1.1  | 02 Jul 2018 |      |
| v1.1.2  | 04 Nov 2018 |      |
| v1.1.3  | Jan 2019    |      |
| v1.1.4  | 17 Apr 2019 |      |
| v1.1.5  | 30 Nov 2019 |      |
| v1.1.6  | 20 May 2020 |      |
| v1.1.7  | 26 Sep 2020 |      |
{:.left}
{% endcapture %}
<details><summary>Version release date table</summary>
{{ version-release-table | markdownify }}
</details>

## Usage

**Youtube tutorial:**

{% include video platform='youtube' id='dLkoB25MTIY' align='left'%}

This plugin can be called from a macro using:

```java
run("Read and Write Excel");
```

and it works very well with batching. A major change for v1.1.0, is that, if called slightly differently (see below), the plugin is now much better at handling large data sets and/or excel files that become large over time.

The title of the **most recent** open image is added as a label for exported results data by default, but this can be changed with passed arguments.

### Optional arguments

Arguments will be parsed from the second argument string as follows.

`dataset_label=` The label to write in the cell above the data in the excel file. Strings and numbers can also be fed to the custom title modifier from a macro/loop:

```java
run("Read and Write Excel", "dataset_label=[My new results data label]");
//example with passed variable 'i'
run("Read and Write Excel", "dataset_label=Table"+i);
```

`no_count_column` Prevents the plugin from adding a "Count" column automatically:

```java
run("Read and Write Excel", "no_count_column");
```

`stack_results` Causes the plugin to export results data underneath pre-existing data (instead of adjacent to it). NOTE: The dataset label for the now stacked data will be that determined for the most recent import:

```java
run("Read and Write Excel", "stack_results");
```

`file=` The path to the excel file to create and/or update (uses the default desktop file otherwise):

```java
run("Read and Write Excel", "file=[C:/Users/antinos/Desktop/My_file.xlsx]");
```

`sheet=` Which sheet in the excel file to put the results in. For example, `sheet=banana` will create and/or append a sheet named `banana`:

```java
run("Read and Write Excel", "sheet=banana");
```

Join arguments as follows:

```java
run("Read and Write Excel", "no_count_column file=[C:/Users/antinos/Documents/My_cool_file.xlsx] sheet=[Custom name here] dataset_label=[Custom data title here]");
```

### Large data import and export

`file_mode=` This requires a slightly different way of calling the plugin but **is very useful for expected large datasets**. There are three options.

`file_mode=read_and_open` Will just load/open an excel file into computer memory (the one you specify with `file=`)...make sure you do `write_and_close` when you're done or you'll have problems:

```java
run("Read and Write Excel", "file=[C:/Users/antinos/Documents/My_cool_file.xlsx] file_mode=read_and_open");
```

`file_mode=queue_write` Will queue something to be written to the excel file you've opened previously with `read_and_open:`

```java
run("Read and Write Excel", "file_mode=queue_write");
```

`file_mode=write_and_close` Will write everything you've queued with `queue_write,` then close the excel file:

```java
run("Read and Write Excel", "file_mode=write_and_close");
```

Example large data macro workflow:

```javascript
//macro to read and write large datasets

//open or create the .xlsx file we want to add data to
run("Read and Write Excel", "file=[C:/Users/antinos/Documents/My_cool_file.xlsx] file_mode=read_and_open");

//add multiple and/or large datasets
///do macro analysis and generate a big results table
run("Read and Write Excel", "file_mode=queue_write");
///do macro analysis and generate a big results table
run("Read and Write Excel", "file_mode=queue_write");
///do macro analysis and generate a big results table
run("Read and Write Excel", "file_mode=queue_write");
///do macro analysis and generate a big results table
run("Read and Write Excel", "file_mode=queue_write");
//for example in a loop
for (i = 0; i < 100; i++) {
    //macro code here
    run("Read and Write Excel", "file_mode=queue_write");
}

//finally write the queued results data to the file
run("Read and Write Excel", "file_mode=write_and_close");
```

Also see [Read_and_Write_Excel_Modified](https://github.com/bkromhout/Read_and_Write_Excel_Modified) for examples. **(However please note: whilst Brenden did an amazing job updating the plugin for the version 1.1 release, the most up-to-date version is currently not represented on his github repo)**

## Disclaimers and Licencing stuff

I am aware that another Excel_Writer plugin exists but it did not work very well for me (hence me creating this). I did not consult their source code but did find out about Apache POI(\*) from them.

Since Brenden modified the plugin, the code is now a lot neater. Feel free to consult it as per your needs.

(\*)This plugin uses the Apache POI api, which is distributed under the terms of the Apache Licence (available from https://poi.apache.org/legal.html). I believe this software to be free and open source.

## Plugin technical details

### Change log

{% capture change-log %}

Version 1.0.1 changes:

1.  package is not bloated by dependency .jar files.
2.  now contains source-code for reference.
3.  removed platform specification as I believe this plugin will work across operating systems.

Version 1.0.2 changes:

1.  the legacy feature was removed that allowed data to be fed to the plugin in a single-line string to the 'arg' function
2.  all data is now exported as string/text into the generated spreadsheet. This is sub-optimal, in that cells will then need to be converted back to a number format in the spreadsheet, but was required to immediately fix an issue whereby string data (when it exists within the Results table) was not being handled properly by the plugin
3.  Replaced the legacy data import function of the argument line (note 1 above) with an allowance for user supplied headings for each import; the argument now accepts a string title (e.g "this is my new title") that will then be used to label the results when exported.

Version 1.1.0 changes:

1.  Brenden Kromhout added the optional argument features mentioned above and described on his [GitHub](https://github.com/bkromhout/Read_and_Write_Excel_Modified) repo
2.  Data imported into an .xlsx file is now recognised as either text or numbers automatically
3.  An imageJ progress bar is now visible for each export
4.  Now using the latest Apache POI releases (3.17)

Version 1.1.1 changes:

1.  Fixed an error whereby the plugin would fail to export data if the 'Label' column of the results table contained empty cells. Empty cells are now replace with a "null" string/text upon export.

Version 1.1.2 changes:

1.  Added an argument so that results data can be exported so that it appears underneath pre-existing data in the created/amended .xlsx file. To implement this function, call the plugin with the argument `stack_results`.

Version 1.1.3 changes:

1.  Bug fix. Results data exported with the `stack_results` argument was being incorrectly referenced after the plugin handled empty cells (from the 'Label' column). When they arise, these empty cells are now handled better.

Version 1.1.4 changes:

1.  Bug fix. Label column issue fixed. Label data was not being exported; it now is.

Version 1.1.5 changes:

1.  Bug fix. Export can now proceed when there are non-Label-column empty cells.

Version 1.1.6 changes:

1.  Bug fix. Fixed a rare `stack_results` issue whereby the data was exported incorrectly if the results table and the excel file both contained a single-row of data.

Version 1.1.7 changes:

1.   Feature added. `cell_ref` argument now allows data to be imported to the specified cell. User request from Stein Rørvik (steinr). NOTE: the plugin does not check to see if data is already present at the specified location, so overwriting is possible. Column headers are also not exported with the data.

{:.left}
{% endcapture %}
<details><summary>(click to expand)</summary>
{{ change-log | markdownify }}
</details>

### Dependencies

| Dependency | Maven Repo |
|---|:-:|
| jars/commons-collections4.jar | [1](https://mvnrepository.com/artifact/org.apache.commons/commons-collections4) |
| jars/xmlbeans.jar             | [2](https://mvnrepository.com/artifact/org.apache.xmlbeans/xmlbeans)            |
| jars/poi-ooxml.jar            | [3](https://mvnrepository.com/artifact/org.apache.poi/poi-ooxml)                |
| jars/poi-ooxml-schemas.jar    | [4](https://mvnrepository.com/artifact/org.apache.poi/poi-ooxml-schemas)        |
| jars/poi.jar                  | [5](https://mvnrepository.com/artifact/org.apache.poi/poi)                      |
| jars/ij.jar                   | [6](https://mvnrepository.com/artifact/net.imagej/ij)                           |
{:.left}

### Update site

http://sites.imagej.net/ResultsToExcel

## Installation

-   With ImageJ open, navigate to {% include bc path="Help" %}
-   In the presented drop down menu, then select {% include bc path="Update..." %}
-   Allow ImageJ to check for updates
-   If required, download updates and restart ImageJ as prompted
-   Repeat the first two steps = {% include bc path="Help|Update..." %}
-   This time ImageJ should let you know that there are no updates available
-   Click on 'OK' but do not close the 'ImageJ Updater' window that is also open
-   In the bottom left of the 'ImageJ Updater' window, find and click on 'Manage update sites'
-   In the newly presented 'Manage update sites' window, find and check the 'ResultsToExcel' check box
-   Then close the 'Manage update sites' window
-   The 'ImageJ Updater' window will now present you with the plugin files for installation
-   Press 'Apply changes'
-   After the update has been applied successfully, restart ImageJ
