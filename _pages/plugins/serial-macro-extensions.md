---
title: Serial Macro Extensions
project: /software/imagej
categories: [Utilities, Macro]
---

# Serial Macro Extensions

## Introduction

This plugin provides methods to talk to a device attached to a serial
port, directly from the ImageJ Macro language, using the Macro Extension
mechanism. You can easily:

-   list the available serial ports
-   establish a serial connection
-   check if the serial connection is alive
-   send commands over the serial connection
-   recieve what is available from the serial port
-   close the connection

It works with any serial device, but was developped to talk with the
Arduino board, an open-source electronics prototyping platform
(<http://arduino.cc/>).

## See also

-   IJSerial plugin (<http://www.eslide.net/>) can also be used, but it
    requires a separate config file, and does not provide persistence to
    the serial connection.

## Authors

Jérôme Mutterer, Tom Mueller, Graeme Awcock, Michael Schmid

## Installation

### Windows

-   Requires RXTX library
-   2018-10-8 (MIFOBIO2018): a working RXTX version for Windows 64-bit
    systems was obtained from <http://fizzed.com/oss/rxtx-for-java>.
    Copy RXTXcomm.jar to jre/lib/ext/ and rxtxSerial.dll and
    rxtxParallel.dll to jre/bin
-   Download serial_ext.jar to the plugins folder
-   Restart ImageJ

### Other platforms

-   Install RXTX according to
    <http://rxtx.qbang.org/wiki/index.php/Installation>
-   Download serial_ext.jar to the plugins folder
-   Restart ImageJ

## Usage

-   Make the macro interpreter aware of the new extensions:

\<code\> run(\"serial ext\"); \</code\>

-   Get a list of available serial ports:

\<code\> ports = Ext.ports(); \</code\>

-   Establish a serial connection to the serial device, using COM8 port
    and a bitrate of 9600 bps:

\<code\> Ext.open(\"COM8\",9600,\"\"); // this is enough e.g. for the
Arduino, defaults parameters are DATABITS_8,STOPBITS_1,PARITY_NONE
\</code\>

\<code\> Ext.open(\"COM1\",14400,\"DATABITS_8 STOPBITS_2 PARITY_ODD\");
// advanced serial port configuration

// Available options

// DEFAULT: 8 data bits, 1 stop bit, no parity

// Databits: // DATABITS_5 // DATABITS_6 // DATABITS_7 // DATABITS_8

// Stopbits: // STOPBITS_1 // STOPBITS_2 // STOPBITS_1\_5

// Parity: // PARITY_NONE // PARITY_EVEN // PARITY_ODD // PARITY_MARK //
PARITY_SPACE

\</code\>

-   Read what the serial device sends:

\<code\> data = Ext.read(); \</code\>

-   Send a string command to the serial device:

\<code\> Ext.write(\"a\"); \</code\>

-   Close the active serial port:

\<code\> Ext.close(); \</code\>

-   Poll if a serial connection is already there:

\<code\> active = Ext.alive(); // returns \"0\" or \"1\" \</code\>

## Download

-   \<del\>Install RXTX Library (<http://rxtx.qbang.org/>).\</del\>

```{=html}
<!-- -->
```
-   2018-10-8 (MIFOBIO2018): a working RXTX version for Windows 64-bit
    systems was obtained from <http://fizzed.com/oss/rxtx-for-java>.
    Copy RXTXcomm.jar to jre/lib/ext/ and rxtxSerial.dll and
    rxtxParallel.dll to jre/bin
-   Download
    ![](/plugin/utilities/serial_macro_extensions/serial_ext.jar) to the
    plugins folder

## History

-   0.12 : GA and MS fixed a byte encoding issue.
