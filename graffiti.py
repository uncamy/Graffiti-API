import sqlite3
import string
from pygeocoder import Geocoder
from flask  import Flask, request, session, g, redirect, url_for,\
                  abort, render_template, flash, json
from flask.ext import restful
from contextlib import closing

#configuration
DATABASE = 'data_graffiti.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
api = restful.Api(app)

graffiti = {}

def geocode(address):
    lat_lon = Geocoder.geocode(address)
    print(lat_lon[0].coordinates)


geocode('455 Broadway, New York, NY 10013')
