import sqlite3
import pandas as pd
import access_db as db
from pygeocoder import Geocoder

db_file = 'nyc_graffiti.db'
schema = 'schema.sql'
csv = 'Graffiti_Locations.csv'




def geocode(address):
    lat_lon = Geocoder.geocode(address)
    return(lat_lon[0].coordinates)

def convert_geocode():
    graff_add= graff_data['Incident Address Display']
    (lat, lon) = geocode(graff_add)
    return (lat, lon)

db.create_database(db_file, schema, csv)
