---
title: Serial Macro Extensions
project: /software/imagej
categories: [Utilities, Macro, MacroExtensions]
---

# Serial Macro Extensions

## Introduction

This plugin provides methods to talk to a device attached to a serial
port, directly from the ImageJ Macro language, using the Macro Extension
mechanism. You can:

-   list the available serial ports
-   establish a serial connection
-   check if the serial connection is alive
-   send commands over the serial connection
-   recieve what is available from the serial port
-   close the connection

## See also

-   IJSerial plugin (<http://www.eslide.net/>) (but requires a separate config file, does not provide persistence to
    the serial connection)

## Authors

Jérôme Mutterer, Tom Mueller, Graeme Awcock, Michael Schmid

## Installation (all platforms)

-   Requires JSSC library
-   Download serial_ext2.jar to the plugins folder
-   Restart ImageJ

## Usage

-   Make the macro interpreter aware of the new extensions:

`run("serial ext2");`

-   Get a list of available serial ports:

`ports = Ext.ports(); `

-   Establish a serial connection to the serial device, using COM8 port
    and a bitrate of 9600 bps:

` Ext.open("COM8",9600,""); ``
This is enough e.g. for the Arduino, defaults parameters are DATABITS_8,STOPBITS_1,PARITY_NONE


` Ext.open("COM1",14400,"DATABITS_8 STOPBITS_2 PARITY_ODD");`
An example of advanced serial port configuration

Available options

// DEFAULT: 8 data bits, 1 stop bit, no parity

// Databits: // DATABITS_5 // DATABITS_6 // DATABITS_7 // DATABITS_8

// Stopbits: // STOPBITS_1 // STOPBITS_2 // STOPBITS_1\_5

// Parity: // PARITY_NONE // PARITY_EVEN // PARITY_ODD // PARITY_MARK //
PARITY_SPACE

-   Read what the serial device sends:

` data = Ext.readUntil("\n"); `

-   Send a string command to the serial device:

` Ext.write("a"); `

-   Close the active serial port:

` Ext.close(); `

-   Poll if a serial connection is already there:

` active = Ext.alive(); // returns "0" or "1" `

-   Get help:

` print ( Ext.help() );`

## History

-   2023-06-17 (): Move doc to ImageJ.net wiki; Use JSSC as underlying library

-   2018-10-8 (MIFOBIO2018): a working RXTX version for Windows 64-bit
    systems was obtained from <http://fizzed.com/oss/rxtx-for-java>.
    Copy RXTXcomm.jar to jre/lib/ext/ and rxtxSerial.dll and
    rxtxParallel.dll to jre/bin

-   0.12 : GA and MS fixed a byte encoding issue.
