from flask import Flask, jsonify
import json
from Coordinates import * 


app = Flask(__name__)

@app.route('/')
def home():

    with open('nearestStation.json') as f:
        data = json.load(f)


    return jsonify(data)

@app.route('/cords=<string:cords>')
def cordinates(cords):

    #cordsArray = cords.split(',')
    #lat = float(cordsArray[0])
    #lon = float(cordsArray[1])

    lat = 42.00
    lon = 42.00 

    #newCords = Coordinates(lat, lon)
    return "str(lat) + ',' + str(lon)"