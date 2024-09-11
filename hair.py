from flask import Flask, render_template
from markupsafe import Markup
from pandas import json_normalize
from paginator import Paginator
import json

app = Flask(__name__)

def JSON_To_Dataframe():
  data = None
  with open('coiffeurs.json', 'r') as file:
    data = json.loads(file.read())
    file.close()
  satanize_json = json.loads(json.dumps(data).replace("null", '""'))
  features = satanize_json["data"]["features"]
  dataframe = json_normalize(features)
  return dataframe

@app.route("/")
def index():
  dataframe = JSON_To_Dataframe()
  paginator_data = Paginator(15)
  print(paginator_data.extract_data(dataframe))
  return render_template("index.html", data=paginator_data.extract_data(dataframe).to_dict(orient="records"),
                                       page=paginator_data.retrieve_page(),
                                       has_next=paginator_data.has_next(dataframe),
                                       has_previous=paginator_data.has_previous())
