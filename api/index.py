from flask import Flask, jsonify
import json
import geopy
from classes.Utility import *


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

    report = createReport(lat, lon)
    return report

@app.route('/user=<string:user>/add=<int:water>')
def user(user, water):
    if water == 0:
        report = {'user': user, 'liters': 0}
    else: 
        report = {'user': user, 'liters': water}

    return json.dumps(report)



