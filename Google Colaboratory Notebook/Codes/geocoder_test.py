# importing geopy library
from geopy.geocoders import Nominatim
import numpy as np
import pandas as pd

#importing 'Port_houses_compact' file 
# import listing file using pandas

port_houses = pd.read_csv('./Data/port_houses_compact.csv')

addresses = port_houses['Address']

type(addresses)
