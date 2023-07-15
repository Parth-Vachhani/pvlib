# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 01:23:02 2023

@author: parthvachhani
"""

import pandas as pd

tmy = pd.read_csv("pvgis_UMA_girls_hostel.csv", skiprows=16, nrows=8760,
                  usecols=["time(UTC)","T2m","G(h)","Gb(n)","Gd(h)","WS10m"],
                  index_col=0)

# tmy.index = pd.to_datetime(tmy.index, format="%Y%m%d:%H%M")

tmy.index = pd.date_range(start="2021-01-01 00:00",
                          end="2021-12-31 23:00",
                          freq="h")

tmy.columns = ["temp-air","ghi","dni","dhi","wind_speed"]

print(tmy)

tmy.plot(figsize=(16,9))

tmy.to_csv("pvlib_UMA_girls_hostel.csv")