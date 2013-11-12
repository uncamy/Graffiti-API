import os
import sqlite3
import string
import pandas as pd

from pygeocoder import Geocoder
from flask  import Flask, request, session, g, redirect, url_for,\
                  abort, render_template, flash, json
from flask.ext import restful
from contextlib import closing

#configuration
DATABASE = 'data_graffiti.db'
DEBUG = True
SECRET_KEY = 'graffiti_key'
SCHEMA = 'schema.sql'
CSV = 'Graffiti_Locations.csv'

app = Flask(__name__)
api = restful.Api(app)


def geocode(address):
    lat_lon = Geocoder.geocode(address)
    return(lat_lon[0].coordinates)

print(geocode('455 Broadway, New York, NY 10013'))

def convert_geocode(address):
    geocode(address)
    x= lat_lon[0]
    y= lat_lon[1]
    print x
    print y
