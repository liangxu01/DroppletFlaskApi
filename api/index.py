from flask import Flask, jsonify
from Utility import *
import json


app = Flask(__name__)

@app.route('/')
def home():

    with open('nearestStation.json') as f:
        data = json.load(f)


    return jsonify(data)

@app.route('/cords=<string:cords>')
def cordinates(cords):
    cordsArray = cords.split(',')
    report = createReport(float(cordsArray[0]), float(cordsArray[1]))
    return jsonify(report)