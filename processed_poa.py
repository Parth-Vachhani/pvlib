# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 19:26:11 2023

@author: parthvachhani
"""

import pandas as pd

global_2016 = pd.read_csv("pvgis_2016.csv", skiprows=8,
                          nrows=8784, index_col=0)

components_2016 = pd.read_csv("pvgis_2016_components.csv", skiprows=8, 
                              nrows=8784, index_col=0)

# print(global_2016)

# print(components_2016)

poa_data_2016 = pd.DataFrame(columns=[
    'poa_global','poa_direct','poa_diffuse', 'temp_air', 'wind_speed'],
    index=global_2016.index)

poa_data_2016['poa_global'] = global_2016['G(i)']
poa_data_2016['poa_direct'] = components_2016['Gb(i)']
poa_data_2016['poa_diffuse'] = components_2016['Gd(i)'] + components_2016['Gr(i)']
poa_data_2016['temp_air'] = components_2016['T2m']
poa_data_2016['wind_speed'] = components_2016['WS10m']


poa_data_2016.index = pd.to_datetime(poa_data_2016.index,
                                     format="%Y%m%d:%H%M")

print(poa_data_2016)

poa_data_2016.to_csv("poa_data_2016.csv")














