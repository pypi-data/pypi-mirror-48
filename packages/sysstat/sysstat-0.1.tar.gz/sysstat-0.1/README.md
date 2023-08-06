####Summary

`Systeminfo` is a library for retrieving information (Overall CPU load, overall memory usage, overall virtual memory usage, IO information, network information) in Python. It creates snapshots of the state of the system in necessary period of time. It supports output in two formats - text file or  json file. Should be configurable with configuration file (See section "Settings").

Example of the structure for output data is about as follows:
* SNAPSHOT 1: TIMESTAMP : SYSTEM DATA
* SNAPSHOT 2: TIMESTAMP : SYSTEM DATA
* SNAPSHOT 3: TIMESTAMP : SYSTEM DATA

####Installation

`pip install systeminfo-1.0-py3-none-any.whl` 

####Settings

You can define your own settings in configuration file `.../site-packages/systeminfo/config.ini`

1. Option "output =" - set output format file (this module support json, txt)
1. Option "interval =" - set required time interval between snapshots in seconds.
1. Option "snapshots =" - set quantity of snapshots.  

####HowToUse

To run application, from `.../site-packages` location in console enter `python systeminfo`. 


