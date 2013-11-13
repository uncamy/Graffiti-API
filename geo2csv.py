import sqlite3
import pandas as pd
from pygeocoder import Geocoder



data_file = pd.read_csv('./Graffiti_Locations.csv')
address_field = 'Incident Address Display' #input address available in dataset


def geocode(address):
    lat_lon = Geocoder.geocode(address)
    return(lat_lon[0].coordinates)

address = data_file[address_field]

# need to add city state to addressess in this dataset before geocode
 #getting ambigous error... array with more than one element is ambiguous use a.any or an.all
def add_city_state():
    if (data_file['Borough'] == 'Queens'):
        full_address = address + 'QUEENS, NEW YORK'
    elif(data_file['Borough']== 'BROOKLYN'):
        full_address = address + 'BROOKLYN, NEW YORK'
    elif(data_file['Borough'] == 'STATEN ISLAND'):
        full_address = address + 'STATEN ISLAND, NEW YORK'
    else:
        full_address = address + 'NEW YORK, NEW YORK'
    return full_address

reduced_dataset = address[:10]
graff_data[]

#correct for borough
full_address = address + ' NEW YORK, NEW YORK'
for row in full_addy:
    lat = geocode(row)
    #return lat, lon

#use map function
#e.g. reduced_dataset.map(geocode)
