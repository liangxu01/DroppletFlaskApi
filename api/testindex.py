import json

def home():
    
    with open('nearestStation.json') as f:
        data = json.load(f)
    

    return data

print(home())