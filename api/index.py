from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():

    with open('nearestStation.json') as f:
        data = json.load(f)


    return jsonify(data)

@app.route('/<string:cords>')
def cordinates(cords):
    return cords