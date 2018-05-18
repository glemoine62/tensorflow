# tensorflow for multi-temporal S1 analysis

This document describes the basic procedure for classification of parcels using multi-temporal Sentinel-1 backscattering time series and the deep neural network machine learning routines in the tensorflow open source library. This procedure currently relies on the use of Google Earth Engine, as it is the only "Big Data" repository that provides access to geocoded, calibrated Sentinel-1 backscattering coefficients at the full 10 m resolution, and for arbitrary selections. The choice of tensorflow is practical and based on its growing reputation as a versatile open source toolkit for a wide range of machine learning problems. However, similar results are likely to be reproducable in other [python based] open source machine learning libraries (theano, scikit-learn, etc.).

A number of data preparation and post-processing routine, written in python, are required to execute the distinct steps in the workflow, as described below.

## Extract S1 backscattering signatures from GEE

Sentinel-1 backscattering intensity images are stored in the Google Earth Engine COPERNICS/S1_GRD catalogue. The Google Earth Engine team downloads GRD images from the [Copernicus Sentinel hub] and runs them through the SNAP Sentinel-1 toolbox, using a standard recipe, to convert them to geocoded, calibrated backscattering intensity imagery, which are then added to the catalogue (currently with a 1 day delay after publication on the Copernicus Sentinel Hub). Because Sentinel-1 data is acquired in distinct orbits, and in both ascending and descending orbits, a consistent, country-wide coverage can only be derived from a time-averaged stack of image scenes. Since the temporal revisit of both S1A and S1B is excellent of the EU, the more so towards Northern lattitudes

to extract S1 multi-temporal signatures for buffered parcel polyogns .
Generate [temporal] average for a pre-defined period. Configuable, set to 7 days.
Exports CSV formatted result at full resolution to Google Drive table.

## Prepare data for tensorflow run

```samplePreparation.py``` reads in CSV export as pandas DataFrame, cleans up for unwanted
columns, groups gewasc classes as distinct class sets, removes non-selected classes, 
and writes result to 

* _cropselect.csv set with centroid lon, lan as extra attributes
* _cropselect_nocrds.csv, idem, but with centroid coords removed

## Split in training and testing

### Alternative 1: select 1 set for training, remainder for testing
```
python sampleSelect.py selection.csv N
```

splits the data set into a set of N records that will serve as training set and the remainder (total_size - N) as test set,
whwre total_size is the total number of records. Results are saved as:

```
selection_train_N.csv
selection_test_{totalsize-M}.csv
```

### Alternative 2: Split in N chunks 

```
python sampleSelectMulti.py selection.csv N
```

splits the data set into N sets with total/N records that will serve as training set and the remainder (total_size - total_size/N) as test sets,
where total_size is the total number of records. Results are saved as:

```
selection_train_N.csv
selection_test_N.csv
```




## Run tensorflow

Make sure the [tflearn module](http://tflearn.org/ "tflearn") is installed.

Switch off the GPU:

```
export CUDA_VISIBLE_DEVICES=''
```

