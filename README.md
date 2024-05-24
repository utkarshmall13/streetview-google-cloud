# streetview-google-cloud

The google streetview api takes a lat-long pair (and camera orientation) to and finds the nearest streetview images.

Therefore instead of sampling randomly everywhere, we first figure out where the streets are and sample on these streets.

## step-1: download shapefile and openstreetmaps.
The shapefile for major us cities is already in the repo, so there is no need to download unless other cities/towns are needed.

For street locations, Openstreetmap extracts are also needed along with the shapefiles.

[bbbike](https://extract.bbbike.org/) is the best source for this. 
* Just select your area of interest either using bounding box aor polygon tool.
* Remember to download in *OSM XML gzip'd* format.
* After clicking extract it redirects you to download page. Once the download is ready move it to the 'cities_osm' directory.

## step-2: sample locations
*Use the `sampler.ipynb` notebook to sample useful locations for a city. It currently has detroit as an examples.
* This should create a npy file of location, that can be used by downloading script.


## step-3: get google cloud api key.
* Follow the instructions on the [google api page](https://developers.google.com/maps/documentation/streetview/overview) to see instrutions on obtaining the api key.
* Put the api key in the `streetview_downloader.py`, `google_key` variable.


## step-4: run `streetview_downloader.py`
* Finally run the python downloader script. You should find images in a directory named `images` 