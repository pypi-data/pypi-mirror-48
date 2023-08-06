﻿# SPTEMP

A Python package for the representation, processing and analysis of spatio-temporal vector data.

The documentation for this package can be found at:
https://baumanndaniel.github.io/sptemp/

The source code of the package can be found at:
https://github.com/BaumannDaniel/sptemp

This package was created by Daniel Baumann, baumann-dan@outlook.com

## Prerequisites

The package can be installed without any dependencies, however to use the full functionality of the package, four third party packages are required.

  - [dateutil](https://dateutil.readthedocs.io/en/stable/) : needed for the Time_Period.from_iso() method
  - [shapely](https://shapely.readthedocs.io/en/stable/index.html) : needed for the interpolation, moving_geometry and analysis modules
  - [pyproj](https://pypi.org/project/pyproj/) : needed if coordinate reference systems are used
  - [pandas](https://pandas.pydata.org/) : needed for the analysis module

## Getting Started

The package provides classes to represent timestamped data, as well as discretely and continuesly changing values.

### Create a moving real number

In the following example a moving real number is created from timestamped floats. Such data could for example represent a temperature timeseries or stock prices.

```python
import datetime as dt

from sptemp import zeit
from sptemp.interpolation import ICollection as IC

tso1 = zeit.TS_Object(1.5, dt.datetime(2019, 7, 4, 14, 15, 10))
tso2 = zeit.TS_Object(5.2, dt.datetime(2019, 7, 4, 14, 15, 20))
tso3 = zeit.TS_Object(2.4, dt.datetime(2019, 7, 4, 14, 15, 35))
tso4 = zeit.TS_Object(8.9, dt.datetime(2019, 7, 4, 14, 15, 50))

tsu1 = zeit.TS_Unit(IC.linear, zeit.Time_Period(dt.datetime(2019, 7, 4, 14, 15, 10), dt.datetime(2019, 7, 4, 14, 15, 50)))
ip1 = zeit.Interpolator([tsu1])

mvr = zeit.Moving_Object([tso1, tso2, tso3, tso4], ip1)
print mvr.interpolate(dt.datetime(2019, 7, 4, 14, 15, 17)).value  # == 4.09
```

<img src="https://raw.githubusercontent.com/BaumannDaniel/sptemp/develop/readme_source/mvr.gif" align="center" width="800" height="450" />


### Create a moving point geometry

In this example a moving point is created from timestamped shapely point geometries.

```python
import datetime as dt

import shapely.geometry as sg
import sptemp.moving_geometry as mg
from sptemp import zeit
from sptemp.interpolation import ICollection as IC
from sptemp.interpolation import IPoint

tsp1 = mg.TS_Point(sg.Point(1,1), dt.datetime(2019, 7, 4, 14, 15, 10))
tsp2 = mg.TS_Point(sg.Point(2,3), dt.datetime(2019, 7, 4, 14, 15, 15))
tsp3 = mg.TS_Point(sg.Point(5,4), dt.datetime(2019, 7, 4, 14, 15, 20))
tsp4 = mg.TS_Point(sg.Point(6,2), dt.datetime(2019, 7, 4, 14, 15, 26))
tsp5 = mg.TS_Point(sg.Point(7,2), dt.datetime(2019, 7, 4, 14, 15, 30))

tsu1 = zeit.TS_Unit(IPoint.linear_point, zeit.Time_Period(dt.datetime(2019, 7, 4, 14, 15, 10), dt.datetime(2019, 7, 4, 14, 15, 21)))
tsu2 = zeit.TS_Unit(IC.constant, zeit.Time_Period(dt.datetime(2019, 7, 4, 14, 15, 21), dt.datetime(2019, 7, 4, 14, 15, 24)))
tsu3 = zeit.TS_Unit(IPoint.linear_point, zeit.Time_Period(dt.datetime(2019, 7, 4, 14, 15, 24), dt.datetime(2019, 7, 4, 14, 15, 30)))
ip1 = zeit.Interpolator([tsu1, tsu2, tsu3])

mvp = mg.Moving_Point([tsp1, tsp2, tsp3, tsp4, tsp5], ip1)
print mvp.interpolate(dt.datetime(2019, 7, 4, 14, 15, 17)).value  # == sg.Point(3.2,3.4)
```

<img src="https://raw.githubusercontent.com/BaumannDaniel/sptemp/develop/readme_source/mvp.gif" align="center" width="800" height="450" />


### Create a moving point geometry follwing the course defined by a LineString

In this example the moving point follows the course defined by a shapely LineString geometry.

```python
import datetime as dt

import shapely.geometry as sg
import sptemp.moving_geometry as mg
from sptemp import zeit
from sptemp.interpolation import IPoint

tsp1 = mg.TS_Point(sg.Point(1,1), dt.datetime(2019, 7, 4, 14, 15, 10))
tsp2 = mg.TS_Point(sg.Point(7,2), dt.datetime(2019, 7, 4, 14, 15, 30))

tsu1 = zeit.TS_Unit(IPoint.curve_point, zeit.Time_Period(dt.datetime(2019, 7, 4, 14, 15, 10), dt.datetime(2019, 7, 4, 14, 15, 30)))
ip1 = zeit.Interpolator([tsu1])

mvp2 = mg.Moving_Point([tsp1, tsp2], ip1)

lr = sg.LineString([(1,1),(2,3),(5,4),(6,2),(7,2)])
print mvp2.interpolate(dt.datetime(2019, 7, 4, 14, 15, 17), lr).value  # = sg.Point(2.74564305 3.24854768)
```

<img src="https://raw.githubusercontent.com/BaumannDaniel/sptemp/develop/readme_source/mvp2.gif" align="center" width="800" height="450" />


### Create a moving linestring geometry

In this example a continuesly moving linestring geometry is created.

```python
import datetime as dt

import shapely.geometry as sg
import sptemp.moving_geometry as mg
from sptemp import zeit
from sptemp.interpolation import ICurve

tsl1 = mg.TS_LineString(sg.LineString([(1,2),(3,1),(7,4)]), dt.datetime(2019, 7, 4, 14, 15, 10))
tsl2 = mg.TS_LineString(sg.LineString([(1,1),(2,0.5),(3,1),(5,1),(6,2),(7,3)]),
                        zeit.Time_Period(dt.datetime(2019, 7, 4, 14, 15, 18), dt.datetime(2019, 7, 4, 14, 15, 22)))
tsl3 = mg.TS_LineString(sg.LineString([(1,1),(3,1.5),(5,3),(7,4)]), dt.datetime(2019, 7, 4, 14, 15, 30))

tsu1 = zeit.TS_Unit(ICurve.basic_linear, zeit.Time_Period(dt.datetime(2019, 7, 4, 14, 15, 10), dt.datetime(2019, 7, 4, 14, 15, 30)))
ip1 = zeit.Interpolator([tsu1])

mvl = mg.Moving_LineString([tsl1, tsl2, tsl3], ip1)

print mvl.interpolate(dt.datetime(2019, 7, 4, 14, 15, 15)).value.coords[:]
# = [(1.0, 1.375), (2.375, 0.6875), (3.2820250483634053, 1.211518786272554),
# (5.036526791961998, 1.589895093971498), (6.018263395980998, 2.4824475469857488), (7.0, 3.375)]
```

<img src="https://raw.githubusercontent.com/BaumannDaniel/sptemp/develop/readme_source/mvl.gif" align="center" width="800" height="450" />


### Create a moving linear ring geometry

In this example a continuesly moving linear ring geometry is created.

```python
import datetime as dt

import shapely.geometry as sg
import sptemp.moving_geometry as mg
from sptemp import zeit
from sptemp.interpolation import IRing

tslr1 = mg.TS_LinearRing(sg.LinearRing([(1,1),(7,1.5),(6,4),(3,3),(1,1)]), dt.datetime(2019, 7, 4, 14, 15, 10))
tslr2 = mg.TS_LinearRing(sg.LinearRing([(2,1),(4,0.5),(6.5,2),(6,4),(4,4),(4,2),(2,2),(2,1)]), dt.datetime(2019, 7, 4, 14, 15, 18))
tslr3 = mg.TS_LinearRing(sg.LinearRing([(3,2),(6,2),(5.5,3.5),(3,3),(3,2)]), dt.datetime(2019, 7, 4, 14, 15, 30))

tsu1 = zeit.TS_Unit(IRing.basic_linear, zeit.Time_Period(dt.datetime(2019, 7, 4, 14, 15, 10), dt.datetime(2019, 7, 4, 14, 15, 30)))
ip1 = zeit.Interpolator([tsu1])

mvlr = mg.Moving_LinearRing([tslr1, tslr2, tslr3], ip1)

print mvlr.interpolate(dt.datetime(2019, 7, 4, 14, 15, 15)).value.coords[:]
# = [(3.625, 3.625), (3.25, 2.0), (1.625, 1.625), (3.875, 1.1875), (4.969669914110089, 1.2633252147247767),
# (6.3125, 2.75), (5.428975315279473, 3.809658438426491), (3.625, 3.625)]
```

<img src="https://raw.githubusercontent.com/BaumannDaniel/sptemp/develop/readme_source/mvlr.gif" align="center" width="800" height="450" />

### Implement your own interpolation function

The users of the sptemp package can provide their own interpolation functions for moving objects.
These functions must take a minimum of three arguments:

  - **start_ts** (TS_Object): An instance of the sptemp.zeit.TS_Object class or one of its subclasses.
  - **end_ts** (TS_Object): An instance of the sptemp.zeit.TS_Object class or one of its subclasses, that lays after start_ts on the time axis.
  - **time** (datetime.datetime): datetime object specifying the time for which the function interpolates the value.
  
The function then can define an arbitrary number of additional arguments, that are then passed by the user to the Moving_Object.interpolate() method.
The function must return a TS_Object instance or an instance of a subclass of the TS_Object class. Alternatively the function can also return None.

In the following example an interpolation function "decelerate" is defined, which provides interpolation functionality for moving points.

```python
import datetime as dt

import shapely.geometry as sg
import sptemp.moving_geometry as mg
from sptemp import zeit

def decelerate(start_ts, end_ts, time):
    decelerate_factor = 1 + ((end_ts.start_time() - time).total_seconds()/(end_ts.start_time() - start_ts.end_time()).total_seconds())
	                    if time < end_ts.start_time() else 1.0
    t = (time - start_ts.end_time()).total_seconds() * decelerate_factor/(end_ts.start_time() - start_ts.end_time()).total_seconds()
    
    t_x = (1 - t)*start_ts.value.x + t*end_ts.value.x
    t_y = (1 - t)*start_ts.value.y + t*end_ts.value.y
        
    if start_ts.has_z and end_ts.has_z:
        t_z = (1 - t)*start_ts.value.z + t*end_ts.value.z
        return mg.TS_Point(sg.Point(t_x, t_y, t_z), time)
    else:
        return mg.TS_Point(sg.Point(t_x, t_y), time)
            
tsp1 = mg.TS_Point(sg.Point(1,1), dt.datetime(2019, 7, 4, 14, 15, 10))
tsp2 = mg.TS_Point(sg.Point(2,3), dt.datetime(2019, 7, 4, 14, 15, 15))
tsp3 = mg.TS_Point(sg.Point(5,4), dt.datetime(2019, 7, 4, 14, 15, 20))
tsp4 = mg.TS_Point(sg.Point(6,2), dt.datetime(2019, 7, 4, 14, 15, 26))
tsp5 = mg.TS_Point(sg.Point(7,2), dt.datetime(2019, 7, 4, 14, 15, 30))

tsu1 = zeit.TS_Unit(decelerate, zeit.Time_Period(dt.datetime(2019, 7, 4, 14, 15, 10), dt.datetime(2019, 7, 4, 14, 15, 30)))
ip1 = zeit.Interpolator([tsu1])

mvp3 = mg.Moving_Point([tsp1, tsp2, tsp3, tsp4, tsp5], ip1)

print mvp3.interpolate(dt.datetime(2019, 7, 4, 14, 15, 20)).value  # == sg.Point(5,4)
```

<img src="https://raw.githubusercontent.com/BaumannDaniel/sptemp/develop/readme_source/mvp3.gif" align="center" width="800" height="450" />


### Create a SPT_DataFrame object

The analysis module of the 'sptemp' package provides the class 'SPT_DataFrame', with which spatio-temporal vector data can be represented with a
relational data structure.

In the following example the data of two buoys floating in the water and recording the air- and water temperature, is represented with
a SPT_DataFrame.

```python
import datetime as dt

import pyproj
import pandas
import shapely.geometry as sg
import sptemp.moving_geometry as mg
from sptemp import zeit
from sptemp.analysis import SPT_DataFrame
from sptemp.interpolation import ICollection as IC
from sptemp.interpolation import IPoint

utm32n = pyproj.Proj(init="epsg:32632")

ip = zeit.Interpolator([zeit.TS_Unit(IC.linear, zeit.Time_Period(dt.datetime(2019, 7, 4, 14, 15, 0), dt.datetime(2019, 7, 4, 15, 0, 0)))])
ip2 = zeit.Interpolator([zeit.TS_Unit(IPoint.linear_point, zeit.Time_Period(dt.datetime(2019, 7, 4, 14, 15, 0), dt.datetime(2019, 7, 4, 15, 0, 0)))])

air_temp1 = zeit.Moving_Object([zeit.TS_Object(22.4, dt.datetime(2019, 7, 4, 14, 15, 10)),
                               zeit.TS_Object(22.7, dt.datetime(2019, 7, 4, 14, 28, 45)),
                               zeit.TS_Object(21.9, dt.datetime(2019, 7, 4, 14, 47, 22))],ip)

air_temp2 = zeit.Moving_Object([zeit.TS_Object(21.4, dt.datetime(2019, 7, 4, 14, 17, 30)),
                               zeit.TS_Object(21.7, dt.datetime(2019, 7, 4, 14, 42, 32))],ip)      
                               
water_temp1 = zeit.Moving_Object([zeit.TS_Object(19.3, dt.datetime(2019, 7, 4, 14, 15, 20)),
                                 zeit.TS_Object(19.1, dt.datetime(2019, 7, 4, 14, 28, 45))],ip)
                                 
water_temp2 = zeit.Moving_Object([zeit.TS_Object(18.8, dt.datetime(2019, 7, 4, 14, 17, 30)),
                                 zeit.TS_Object(19.2, dt.datetime(2019, 7, 4, 14, 42, 45))],ip)
                                 
      
mvp1 = mg.Moving_Point([mg.TS_Point(sg.Point(473925.42, 6354541.11), dt.datetime(2019, 7, 4, 14, 15, 10), utm32n),
                        mg.TS_Point(sg.Point(473953.76, 6354877.23), dt.datetime(2019, 7, 4, 14, 30, 0), utm32n),
                        mg.TS_Point(sg.Point(473967.12, 6354854.73), dt.datetime(2019, 7, 4, 14, 50, 0), utm32n)], ip2)
                        
mvp2 = mg.Moving_Point([mg.TS_Point(sg.Point(474176.89, 6354701.98), dt.datetime(2019, 7, 4, 14, 17, 20), utm32n),
                        mg.TS_Point(sg.Point(474533.54, 6354770.11), dt.datetime(2019, 7, 4, 14, 50, 0), utm32n)], ip2)
                        
id = ["a", "b"]
air_temp = [air_temp1, air_temp2]
water_temp = [water_temp1, water_temp2]
geometry = [mvp1, mvp2]
                                 
df = pandas.DataFrame({"id" : id, "air_temp" : air_temp, "water_temp" : water_temp, "geometry" : geometry})
spt_df = SPT_DataFrame(df)

print spt_df.interpolate(dt.datetime(2019, 7, 4, 14, 30, 0)).dataframe
```

| id | water_temp | air_temp |                                        geometry |
| -- | ----------:| --------:| -----------------------------------------------:|
| a  |       None |  22.6363 |                 sg.Point(473953.76, 6354877.23) |
| b  |     18.998 |  21.5498 |  sg.Point(474315.1828571429, 6354728.397755102) |



