---
title: TrackMate-CSVImporter
logo: /media/icons/trackmate-csv-importer.png
description: The TrackMate module to import detections saved in CSV fies into TrackMate.
source-url: https://github.com/tinevez/TrackMate-CSVImporter
license-url: /licensing/lgpl
license-label: LGPLv3
dev-status: Active
support-status: Active
team-founders: Jean-Yves Tinevez
team-leads:  Jean-Yves Tinevez
team-developers:  Jean-Yves Tinevez
team-debuggers:  Jean-Yves Tinevez
team-reviewers:  Jean-Yves Tinevez
team-support:  Jean-Yves Tinevez
team-maintainers:  Jean-Yves Tinevez
---

# CSV to TrackMate importer.

This plugin allows for importing detections and tracks contained in CSV files into TrackMate, or to export them as TrackMate XML file in headless mode.

## Installation.

This plugin lives on a separate [update site](/list-of-update-sites). If you want to use it, you first need to subscribe to the update site named `TrackMateCSVImporter`, as explained [here](/update-sites/following).

The importer can be found in the {% include bc path='Plugins | Tracking | TrackMate CSV importer'%} menu.

## Using the GUI.

The example below shows a capture of the GUI when re-importing a CSV file created by TrackMate itself (from the `Analysis` button).

<figure><img src="/media/plugins/trackmate/trackmatecsvimporter-01.png" title="TrackMateCSVImporter_01.png" width="800" alt="TrackMateCSVImporter_01.png" /><figcaption aria-hidden="true">TrackMateCSVImporter_01.png</figcaption></figure>

Open the target image in Fiji, and browse to the CSV file from the GUI. It will be parsed and the parameter lists will be populated with the headers of the CSV file. Some columns are mandatory (X, Y, frame). If you uncheck `Compute all features?` box, only a minimal set of features will be declared and computed.

Depending on whether you specify to import the track values or not, the TrackMate GUI will be created at a different stage.

## Running the exporter from the command line.

After installation, a Jython script called `CsvToTrackMate.py` will be addede to the `scripts` folder of your Fiji installation. It is meant to be called in [headless mode](/learn/headless) to directly convert a CSV file and an image file into a TrackMate file.

You can use Fiji in headless mode, to call the Jython script `CsvToTrackMate.py` that will parse arguments and configure the importer properly. Here is an example:

    ./ImageJ-macosx --headless   /path/to/scripts/CsvToTrackMate.py 
        --csvFilePath="/path/to/MyCsvFile.csv" 
        --imageFilePath="/path/to/MyImage.tif"
         --xCol=1 
         --radius=2 
         --yCol=2 
         --zCol=3 
         --frameCol=0
         --targetFilePath="/path/to/plugins/trackmateFile.xml"

This will create a new TrackMate file `/path/to/plugins/trackmateFile.xml` with detections created from the CSV file `/path/to/MyCsvFile.csv` and reading the image metadata from image file `/path/to/MyImage.tif`.
