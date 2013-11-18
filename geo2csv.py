import sqlite3
import pandas as pd
from pygeocoder import Geocoder
from time import sleep


graffiti = pd.read_csv('./Graffiti_Locations.csv')

#geocode data with pauses
def geocode(address):
    lat_lon = Geocoder.geocode(address)
    sleep(2)
    return(lat_lon[0].coordinates)

#setting up data:
#filter by bourough to only get Manhattan Graffiti that is 'open'
manhattan = graffiti[graffiti['Borough']== 'MANHATTAN']
current_graffiti = manhattan[manhattan['Status']== 'Open']

#add new column for the address
current_graffiti['full_address'] = \
        current_graffiti['Incident Address Display'] + ', NEW YORK, NEW YORK'


#geocode data and catch errors
def address2geocode():
    print 'starting geocoding'
    try:
        current_graffiti['geocode'] = \
                current_graffiti['full_address'].map(geocode)
    except:
        current_graffiti['geocode'] = None
    print 'end geocoding'

current_graffiti.to_csv =('graffiti_geocode.csv')


'''
reduced_dataset = address[:10]
#graff_data[]

#correct for borough
full_address = address + ' NEW YORK, NEW YORK'
for row in full_address:
    lat = geocode(row)
    #return lat, lon

#use map function
#e.g. reduced_dataset.map(geocode)
'''
