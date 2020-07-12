# Libraries for flask web libraries
import flask
from flask import request, render_template
from flask_restful import Api

# Libraries for main construction block.
# Allow users to make a request to a web page e.g. an external API to get data.
import requests
# Transform a description of a location into such as a pair of coordinates.
import geocoder
# Use math module to access different mathematical functions.
import math

# __name__ is the name of the current Python module.
app = flask.Flask(__name__)

# Use the config attribute of the Flask object.
app.config['DEBUG'] = True

# Create the main entry point for the application.
api = Api(app)

# We then use the route() decorator to tell Flask what URL should trigger our function.
@app.route('/', methods = ['get'])
def index():
    # Insert government's 中央氣象局 API URL & my API key.
    url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0003-001?Authorization={}&format={}&elementName={}&parameterName={}'
    # insert arguments according to its API document.
    auth_arg = 'CWB-D8D8ED46-F9A0-4E90-92CA-112E792E76FB'
    format_arg = 'JSON'
    ele_arg = 'TEMP,HUMD,24R'
    para_arg = 'CITY,TOWN'
    # Receive API data according to my specific arguments and it's in JSON format.
    req = requests.get(url.format(auth_arg, format_arg, ele_arg, para_arg)).json()
        # Find location data from the returned JSON.
    data = req['records']['location']
    # Find where I am with geocoder.
    location = geocoder.ip('me').latlng
    my_lat = location[0]
    my_lon = location[1]
    # Append distances of each weather station versus my current location.
    result = []
    for location in data:
        any_lat = location['lat']
        any_lon = location['lon']
        p1 = [float(my_lat), float(my_lon)]
        p2 = [float(any_lat), float(any_lon)]
        distance = math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))
        result.append(distance)
    # Find the smallest values among all distances.
    nearest = min(result)
    # Get the index of the the smallest distance.
    nearest_index = result.index(nearest)
    # Get the data of the nearest weather station.
    nearest_location = data[nearest_index]
    # Pass this weather station's data as arguments from main.py to weather.html.
    weather = {
    'lat': nearest_location['lat'],
    'lon': nearest_location['lon'],
    'station_name': nearest_location['locationName'],
    'station_city': nearest_location['parameter'][0]['parameterValue'],
    'station_town': nearest_location['parameter'][1]['parameterValue'],
    'time': nearest_location['time']['obsTime'],
    'temperature': nearest_location['weatherElement'][0]['elementValue'],
    'humidity': nearest_location['weatherElement'][1]['elementValue'],
    'rainfall': nearest_location['weatherElement'][2]['elementValue'],
    }
    # weather.html will display above arguments with render_template function.
    return render_template('weather.html', weather = weather)
  
# __main__ is the name of the current Python module.  
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 3333)