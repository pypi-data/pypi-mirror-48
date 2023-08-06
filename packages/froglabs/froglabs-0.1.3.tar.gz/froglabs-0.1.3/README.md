# Froglabs Client Library

This package provides Froglabs CLI that supports weather and training services.

### Installing

Clone the repository if you do not have it already:

```bash
$ git clone http://github.com/froglabs/froglabs && cd froglabs
```

Install and update:

```bash
$ python3 setup.py install
```

Froglabs supports Python 3.4 and newer.

## Weather Service

Request Black Sea surface temperature for 2019-06-16 - 2019-06-17 period:

```bash
$ froglabs weather get_weather result.nc "Black Sea" sst 2019-06-16 2019-06-17
```

Request Black Sea surface temperature and salinity for 2019-06-16 - 2019-06-17 period:

```bash
$ froglabs weather get_weather result.nc "Black Sea" sst,sss 2019-06-16 2019-06-17
```

Now plot the result:

```bash
$ froglabs weather plot result.nc output.png sst
```

You can also plot on a map (install `cartopy` with `pip install cartopy` or `sudo apt-get install python3-cartopy`):

```bash
$ froglabs weather plot result.nc output.png sst --projection=PlateCarree
$ froglabs weather plot result.nc output.png sst --draw-gridlines=true --central-latitude=45 --projection=Orthographic
```
