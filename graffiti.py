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

def fix_geocodes(sample):
    print type(sample)
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

def geocode(address):
    try:
        lat_lon = Geocoder.geocode(address)
        return(lat_lon[0].coordinates)
    except:
        return 'unable to geocode'


#test address
address = '455 Broadway, New York, NY'
def locations(address):
    geo_loc = geocode(address)
    return geo_loc

def vicinity(geo_loc):
#there must be a better way to do this...
    lat = geo_loc[0]
    lng = geo_loc[1]
    lat_max = lat + 0.000001
    lat_min = lat - 0.000001
    lng_max = lng + 0.000001
    lng_min = lng - 0.000001

    #df[df['lng']]


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        address = request.form['address']
        find_loc = locations(address)
        return render_template('index.html', graffiti = find_loc)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()
