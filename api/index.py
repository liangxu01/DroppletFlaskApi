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

    
    return jsonify(cords)