import sqlite3
import string

from googlemaps import GoogleMaps
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

def addr_to_latlng (address):
    #convert given address to google lat lng
    #sensor = false is used if the device does NOT have a location sensor
    maps_api ='http://maps.googleapis.com/maps/api/geocode/json?address=%s\
              &sensor=false' %(address)
    try:
        resp_json = json.loads(urllib2.urlopen(maps_api_url.read()))
        goog_lat = resp_json["results"][0][2][0]["lat"]
        goog_lon = resp_json["results"][0][2][0]["lon"]
        print goog_lat
        print goog_lon
    except: #need better error handling
        print "something went wrong"
'''
class graffiti(restful.Resource):
    def get(self):
        return {
            'location': '250 Manhattan Ave',
            'clean': 'nope'
        }

    def put(self, location)
api.add_resource(graffiti, '/')

if __name__ == '__main__':
    app.run(debug=True)

'''
@app.route('/get_data')
def get_graffiti_data():
    url = 'https://data.cityofnewyork.us/api/views/2j99-6h29/rows.json?accessType=DOWNLOAD'
    r = requests.get(url)
    return json.dumps(r.json, indent=4)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
'''
