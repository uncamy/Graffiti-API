import sqlite3
import pandas as pd
from pygeocoder import Geocoder


graff_data = pd.read_csv('./Graffiti_Locations.csv')

def geocode(address):
    lat_lon = Geocoder.geocode(address)
    return(lat_lon[0].coordinates)

def convert_geocode():
    graff_add= graff_data['Incident Address Display']
    geocode(graff_add)
    return geocode

graff_coded= convert_geocode()
