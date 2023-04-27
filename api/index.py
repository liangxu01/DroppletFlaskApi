from flask import Flask, jsonify
import json
import geopy
from classes.IntializeData import IntializeBuildings


app = Flask(__name__)

@app.route('/')
def home():

    with open('nearestStation.json') as f:
        data = json.load(f)

    return jsonify(data)

@app.route('/cords=<string:cords>')
def cordinates(cords):

    cordsArray = cords.split(',')
    lat = float(cordsArray[0])
    lon = float(cordsArray[1])

    #newCords = Coordinates(lat, lon)
    return "Works!"