from flask import Flask
import json

app = Flask(__name__)

x = ''

with open('coiffeurs.json', 'r') as f:
  data = json.loads(f.read())
  features = data["data"]["features"]
  for feature in features:
    x += f'{feature["properties"]["markerinnerhtml"]}'

@app.route("/")
def hello_world():
    return x 