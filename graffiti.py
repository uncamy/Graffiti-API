import os
import sqlite3
import string
import pandas as pd

#from geopy.geocoders import GoogleV3
#import geopy.distance
#from googlemap import GoogleMaps
#import api_key.py

from pygeocoder import Geocoder
from flask  import Flask, request, session, g, redirect, url_for,\
                  abort, render_template, flash, json
from flask.ext import restful



#configuration
DEBUG = True
CSV = './data/geocoded_manhattan.csv'
df = pd.read_csv(CSV)
#gmaps = GoogleMaps(api_key)
API_KEY = './api_key.txt'
app = Flask(__name__)
app.config.from_object(__name__)

#process data to allow for calculations on lat/lng
def fix_geocodes(sample):
    sample = sample.replace("(", "")
    sample = sample.replace(")", "")
    sample = sample.split(',')
    lat  = float(sample[0])
    lng = float(sample[1])
    new_geo= (lat, lng)
    return new_geo

geo_pairs= df['geocode'].map(fix_geocodes)
df['lat'] = geo_pairs.map(lambda x: x[0])
df['lng'] = geo_pairs.map(lambda x: x[1])

#df.to_csv('./data/final_data.csv')

def geocode(address):
    try:
        lat_lon = Geocoder.geocode(address)
        return(lat_lon[0].coordinates)
    except:
        return 'unable to geocode'

#test address
def locations(address):
    geo_loc = geocode(address)
    return geo_loc

def vicinity(geo_loc):
#there must be a better way to do this...
    distance = 0.000001
    lat = geo_loc[0]
    lng = geo_loc[1]
    lat_max = lat + distance
    lat_min = lat - distance
    lng_max = lng + distance
    lng_min = lng - distance
#pass in the df[] variables so that it can be tested
    #equalities
    nearby = df[df['lng']> lng_min] and df[df['lng'] <lng_max] \
    and df[df['lat']> lat_min] and df[df['lng'] <lng_max]
    graffiti = list(zip(nearby['lat'], nearby['lng']))
    return graffiti

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        address = request.form['address']
        user_loc = locations(address)
        graffiti_locs = json.dumps(vicinity(user_loc))
        return render_template('index.html', your_loc = user_loc,\
                               graffiti = graffiti_locs)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()

    A
    A
