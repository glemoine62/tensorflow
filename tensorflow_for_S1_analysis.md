# tensorflow for multi-temporal S1 analysis

## Extract S1 backscattering signatures from GEE

GEE script to extract S1 multi-temporal signatures for buffered [BRP] parcel areas.
Generate [temporal] average for a pre-defined period. Configuable, set to 7 days.
Exports CSV formatted result at full resolution to Google Drive table.

## Prepare data for tensorflow run

samplePreparation.py reads in CSV export as pandas DataFrame, cleans up for unwanted
columns, groups gewasc classes as distinct class sets, removes non-selected classes, 
and writes result to 

* _cropselect.csv set with centroid lon, lan as extra attributes
* _cropselect_nocrds.csv, idem, but with centroid coords removed

##  

