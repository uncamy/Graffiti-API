import sqlite3
import pandas as pd
from pygeocoder import Geocoder



graff_data = pd.read_csv('./Graffiti_Locations.csv')

def geocode(address):
    lat_lon = Geocoder.geocode(address)
    return(lat_lon[0].coordinates)

address = graff_data['Incident Address Display']
reduced_dataset = address[:10]
graff_data[]

#correct for brough
full_addy = address + ' NEW YORK, NEW YORK'
for row in full_addy:
    lat = geocode(row)
    #return lat, lon

#use map function
#e.g. reduced_dataset.map(geocode)
