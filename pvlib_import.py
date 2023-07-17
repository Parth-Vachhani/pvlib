# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 22:16:36 2023

@author: parthvachhani
"""

import pvlib

import pandas as pd
import matplotlib.pyplot as plt

from pvlib.modelchain import ModelChain
from pvlib.location import Location
from pvlib.pvsystem import PVSystem
from pvlib.temperature import TEMPERATURE_MODEL_PARAMETERS

location = Location(latitude=22.485148679632847,
                    longitude=70.06132108195024,
                    tz='Asia/Kolkata',
                    altitude=80,
                    name='UMA-Girls Hostel')

sandia_modules = pvlib.pvsystem.retrieve_sam('SandiaMod')
cec_inverters = pvlib.pvsystem.retrieve_sam('CECInverter')

module = sandia_modules['Canadian_Solar_CS5P_220M___2009_']
inverter = cec_inverters['ABB__PVI_3_0_OUTD_S_US__208V_']

temperature_parameters = TEMPERATURE_MODEL_PARAMETERS['sapm']['open_rack_glass_glass']

system = PVSystem(surface_tilt=30, surface_azimuth=90,
                  module_parameters=module,
                  inverter_parameters=inverter,
                  temperature_model_parameters=temperature_parameters,
                  modules_per_string=8,
                  strings_per_inverter=2)

modelchain = ModelChain(system, location)

# time = pd.date_range(start="2021-07-01", end="2021-07-07",
#                      freq="1min", tz=location.tz)

# clear_sky = location.get_clearsky(time)

# clear_sky.plot(figsize=(16,9))
# plt.show()

# tmy = pd.read_csv("pvlib_UMA_girls_hostel.csv",index_col=0)

# tmy.index = pd.to_datetime(tmy.index)

# modelchain.run_model(tmy)
# modelchain.results.ac.plot(figsize=(16,9))
# plt.show()

# modelchain.results.ac.resample("M").sum().plot(figsize=(16,9))
# plt.show()


poa_data_2016 = pd.read_csv("poa_data_2016.csv", index_col=0)

poa_data_2016.index = pd.to_datetime((poa_data_2016.index))

modelchain.run_model_from_poa(poa_data_2016)
modelchain.results.ac.plot(figsize=(16,9))
plt.show()




































