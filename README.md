About setwave5200
=================

![Spreadsheet](https://raw.githubusercontent.com/wd5gnr/mhs5200a/master/images/screenshot_211.png "The system in action")

The MHS5200A () is an inexpensive family of DDS signal generators that have
16 arbitrary wave functions. However, the software is for Windows and not
especially good (giant Labview compiled program with lots of issues).

This software does not attempt to operate the device although you may
find the enclosed reverse engineer of its protocol useful. However, it
does allow you to start with a handy spreadsheet, define a waveform, and
upload it.

Here are the basic steps:

1) Copy mhs5200.xls to some unique name
2) Open that new file with your spreadsheet program
3) On the first tab, you can set the total period, min/max values if you like
4) You can fill in column C and if you want to use data from the rest of the spreadsheet to fill in your formula, you can. Each waveform has 1024 samples and data ranges from 0 to 255. The spreadsheet scales for you if you set min and max.
5) Observe the waveform graph to ensure you have the right shape.
6) Switch to the export tab and export it as a CSV file.
7) Run setwave5200 with the following arguments: port #, csv file, slot #

For example:

setwave5200 /dev/ttyUSB0 test.csv 15

Slot numbers are 0 to 15. You can send multiple files:
setwave5200 /dev/ttyUSB0 test.csv 15 sine.csv 0 noise.csv 5

The CSV file format is pretty forgiving. You can seperate data by
commas or newlines and quotes are allowed but not required. Blank lines
and lines starting with # are skipped.

Due to rounding errors, going all the way to the limit may cause some
distortion at the edges. The example formula limits the amplitude to 95%

       =0.95*SIN(2*PI()/1024*$A2)

In English, take a 1/1024 of a full sample, multiply it by the sample #
(N) and take the sine. Then Take 95% of the full value.


Install
=======
Just put the three files on your path in the same directory:
setwave5200
setwave5200.dat
setwave5200.awk

You will also want the xls file and an Excel-compatible spreadsheet

