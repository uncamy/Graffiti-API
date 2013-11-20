import os
import sqlite3
import string
import pandas as pd

from geopy.geocoders import GoogleV3
import geopy.distance
from googlemap import GoogleMaps
import api_key

from pygeocoder import Geocoder
from flask  import Flask, request, session, g, redirect, url_for,\
                  abort, render_template, flash, json
from flask.ext import restful
from contextlib import closing


#configuration
DEBUG = True
CSV = './data/geocoded_manhattan.csv'
df = pd.read_csv(CSV)
gmaps = GoogleMaps(api_key)

app = Flask(__name__)
app.config.from_object(__name__)

def geocode(address):
    lat_lon = Geocoder.geocode(address)
    return(lat_lon[0].coordinates)


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        address = request.form['address']
    return render_template('index.html', address)

if __name__ == '__main__':
    app.run()
