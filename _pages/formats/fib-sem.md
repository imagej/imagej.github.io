---
title: FIBSEM importer
section: Learn:ImageJ Basics:File Formats
categories: [Import-Export]
artifact: sc.fiji:IO_
name: FIBSEM importer
---

## Overview

The FIBSEM importer is able to read the image files produced by the FIB-SEM machine at Janelia Farm. It can be used via:

-   Drag & Drop
-   {% include bc path='File | Import | FIB-SEM ...'%}

It will be opened as unsigned 16-bit data ranging from 0 to 65535, where 0 corresponds to a detector voltage of -10 volts and 65535 to a voltage of +10 volts. It will automatically set the pixel resolution in the image calibration.

For access to all the other meta-data, see the special options paragraph below.

## Special options

### Open image as float

It might make sense to open the image as float and not convert it into an unsigned short. To do so, one can set a switch in the FIBSEM importer using the **script editor**:

-   {% include bc path='File | New | Script'%}
-   {% include bc path='Language | Beanshell'%}
-   type the following lines

````
import io.FIBSEM_Reader;
FIBSEM_Reader.openAsFloat = true;
````

-   click Run

From now on, every FIBSEM image of the **currently running Fiji instance** will be opened as float, the float values represent directly the measured voltage for each pixel.

### Access the complete metadata

In order to access the complete metadata you have to make a new instance of the FIBSEM importer, load the dataset and afterwards request the metadata object. Here is the code how do it using the script editor and the Beanshell language (see above):
````
import io.FIBSEM_Reader;
import io.FIBSEM_Reader.FIBSEMData;

// open the file
FIBSEM_Reader reader = new FIBSEM_Reader();
reader.run( "/Users/preibischs/Desktop/Zeiss_12-01-14_210123.dat" );

// get the metadata
FIBSEMData metadata = reader.getHeader();

// print all data into the log window
IJ.log( "" + metadata );

// print a single field
IJ.log( "The resolution of the image is " + metadata.xRes + " x " + metadata.yRes + " pixels." );
````

Below you will find a complete list of all fields of **FIBSEMData**, i.e. all metadata information that you can access:
````
/* the magic number identifying the file, should be 3555587570 */
public long magicNumber;
/* the version of the file, supported until now is 1,2,3 */
public int fileVersion;
/* file type, 1 is Zeiss Neon detectors */
public int fileType;
/* AI sampling time (including oversampling) in seconds */
public double timeStep;
/* the number of channels */
public int numChannels;
/* the parameters required to transform the 16 bit signed signal back to volts:
 * volts = offset + intensity*gain
 * (we ignore second and third order as they are zero anyways)
 */
public float[] offset, gain, secondOrder, thirdOrder;
/* number of pixels in x per channel */
public long xRes;
/* number of pixels in y per channel */
public long yRes;
/* AI oversampling */
public int oversampling;
/* Read AI delay (# of samples) - only v3*/
public int AIdelay = 0;
/* Scan speed (Zeiss #) */
public int zeissScanSpeed;

/* Actual AO (scanning) rate */
public double scanRate;
/* Frameline rampdown ratio */
public double framelineRampdownRatio;
/* X coil minimum voltage */
public double xMin;
/* X coil maximum voltage */
public double xMax;
/* Detector minimum voltage */
public double detMin;
/* Detector maximum voltage */
public double detMax;

/* AI Ch1 */
public int AI1;
/* AI Ch2 */
public int AI2;
/* AI Ch3 */
public int AI3;
/* AI Ch4 */
public int AI4;

/* notes */
public String notes;

/* Name of detector A */
public String detectorA = "";
/* Name of detector B */
public String detectorB = "";
/* Name of detector C */
public String detectorC = "";
/* Name of detector D */
public String detectorD = "";

/* Magnification */
public double magnification;
/* Pixel size in nm */
public double pixelSize;
/* Working distance in mm */
public double wd;
/* EHT in kV */
public double eht;
/* SEM aperture number */
public int semApr;
/* high current mode (1=on, 0=off) */
public int highCurrent;
/* FIB mode: 0=SEM, 1=FIB, 2=Milling, 3=SEM+FIB, 4=Mill+SEM, 5=SEM Drift Correction, 6=FIB Drift Correction, 7=No Beam, 8=External, 9=External+SEM */
public int mode;

/* SEM probe current in A */
public double semCurr;
/* SEM scan roation in degree */
public double semRot;
/* Chamber Vacuum */
public double chamVac;
/* Gun vacuum */
public double gunVac;
/* SEM beam shift X */
public double semShiftX;
/* SEM beam shift Y */
public double semShiftY;
/* SEM stigmation X */
public double semStiX;
/* SEM stigmation Y */
public double semStiY;
/* SEM aperture alignment X */
public double semAlnX;
/* SEM aperture alignment Y */
public double semAlnY;
/* Stage position X in mm */
public double stageX;
/* Stage position Y in mm */
public double stageY;
/* Stage position Z in mm */
public double stageZ;
/* Stage position T in degree */
public double stageT;
/* Stage position R in degree */
public double stageR;
/* Stage position M in mm */
public double stageM;
/* Detector A brightness (%) */
public double brightnessA;
/* Detector A contrast (%) */
public double contrastA;
/* Detector B brightness (%) */
public double brightnessB;
/* Detector B contrast (%) */
public double contrastB;
/* FIB focus in kV */
public double fibFocus;
/* FIB probe number */
public int fibProb;
/* FIB emission current */
public double fibCurr;
/* FIB scan rotation */
public double fibRot;
/* FIB aperture alignment X */
public double fibAlnX;
/* FIB aperture alignment Y */
public double fibAlnY;
/* FIB stigmation X */
public double fibStiX;
/* FIB stigmation Y */
public double fibStiY;
/* FIB beam shift X in micron */
public double fibShiftX;
/* FIB beam shift Y in micron */
public double fibShiftY;

/* name of the machine */
public String machineID;
/* file length in bytes */
public long fileLength;
````

