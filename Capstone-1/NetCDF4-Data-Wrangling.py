# -*- coding: utf-8 -*-
"""
Created on Thu May 23 18:01:15 2019

@author: Connor McAnuff
"""

import numpy as np
import netCDF4 as nc
import pandas as pd
import xarray as xr
from pathlib import Path

#data_folder = Path("C:\Users\conno\Documents\Springboard\Projects\Springboard-Projects\Capstone-1\Raw-data\gefs_test\test\")
#file_to_open = data_folder + "apcp_sfc_latlon_subset_20080101_20121130.nc"

nc_data = nc.Dataset('apcp_sfc_latlon_subset_19940101_20071231.nc')

#ens = nc_data.variables['ens']
#print(ens)



for v in nc_data.variables.items():
    print(v)

#for d in nc_data.dimensions.values():
    #print(d)

#nc_data.variables['time'][-1]

#precip = list(data.variables.values())[-1]

#precip.dimensions

#precip = data['Total_precipitation']

#precip = data.variables.values()

#print(precip)
