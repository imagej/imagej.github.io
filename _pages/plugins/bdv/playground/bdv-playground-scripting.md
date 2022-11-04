---
title: 3 - Script
artifact: sc.fiji:bigdataviewer-playground
nav-links: true
toc: true
---


By using the SciJava framework to store BigDataViewer windows through its `BdvHandle` interface, it is possible to communicate bdv instances between scripts and commands (see [script parameter page](/scripting/parameters)). This also facilitates the use of Fiji GUI because the commands of this repository can be chained easily. Any script or Command which declares a `BdvHandle` parameter can retrieve or provide reference to existing BigDataViewer instances.

In practice, Bdv windows created via the commands from this update site are put by default in the `ObjectService`. To get a reference to these windows:

-   In groovy, add this at the beginning of your script

```java
#@BdvHandle bdvh
```

```java
@Parameter
BdvHandle bdvh;
```

## How to make your BigDataViewer workflow compatible with SciJava ?

Two options:

-   Use any command from bigdataviewer-playground which generates a BDV window. It corresponding `BdvHandle` will be registered and can be retrieved through a SciJava parameter annotation. This will make your Bdv Window accessible to other plugins / commands.

-   Create your own Bdv window, but declare the associated `BdvHandle` as an output of your Command:
    -   in Java: `@Parameter(type = ItemIO.OUTPUT); BdvHandle bdvh_out;`

The type of the parameter annotation can also be `ItemIO.BOTH` if your command is modifying an existing `BdvHandle`

### Example scripts

#### Groovy

-   Display a recursive Fiji image:

```java
// Input : provided by Single Input Preprocessor in case no widow is present
#@BdvHandle bdv_h 
// Output : allow to updates list of sources
#@output BdvHandle bdv_h
#@output SourceAndConverter source

// Simple Fiji Image stored as an array
fijiData =
			[[0,0,0,0,0,0,0,0,0],
			 [0,1,1,1,1,1,1,1,0],
			 [0,1,0,0,0,0,0,0,0],
			 [0,1,0,1,0,1,0,1,0],
			 [0,1,0,1,0,1,0,1,0],
			 [0,1,0,1,0,1,0,1,0],
			 [0,1,0,0,0,1,0,0,0],
			 [0,1,0,1,1,1,0,0,0],
			 [0,0,0,0,0,0,0,0,0]] as short[][];

// Declare a procedural image
def s = new Procedural3DImageShort({p -> getRecursiveFiji(p[1], p[0], p[2])}).getRRA();  

// Interval (mainly useless here, but required by BdvFunctions
Interval interval = new FinalInterval([ 0, 0, 0] as long[], [ 9, 9, 0 ] as long[]);

// Display the source in the bdv_h window
bss = BdvFunctions.show( s , interval, "Fiji", BdvOptions.options().addTo(bdv_h) );

// Display options
bss.setDisplayRange(0,1);
bss.setColor(new ARGBType(ARGBType.rgba(101,164,227,255)));

source = bss.getSources().get(0) // to register the created source


//------------- FUNCTION for recursive Fiji Image generation

int getRecursiveFiji(double x, double y, double level) {
	def valueLevel = (int) (fijiData[((int)x%9)][((int)y%9)])
	if (level<=0) {
		return valueLevel
	} else {
		if (valueLevel==1) {
			if (level>2) {
				level=2;
			}
			return getRecursiveFiji(x*9,y*9,level-1)
		} else {
			return 0
		}
	}
}

import bdv.util.Procedural3DImageShort
import net.imglib2.RealRandomAccessible
import bdv.util.BdvFunctions
import bdv.util.BdvOptions
import bdv.util.BdvHandle
import net.imglib2.type.numeric.integer.UnsignedShortType
import net.imglib2.FinalInterval
import net.imglib2.Interval
import net.imglib2.type.numeric.ARGBType

```

#### ImageJ Macro Language

TODO

## List of all commands

The list of commands of this repository is available in the git repository : https://github.com/bigdataviewer/bigdataviewer-playground
