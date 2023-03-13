from flask import Flask, render_template
from io import BytesIO
import base64
import matplotlib.pyplot as plt
import numpy as np
import requests
import json

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/index", methods=["GET"])
def index():

    url = "https://api.open-meteo.com/v1/forecast?latitude=35.69&longitude=139.69&hourly=temperature_2m&forecast_days=1&timezone=Asia%2FTokyo"
    r = requests.get(url)

    json_load = json.loads(r.text)


    
    fig = plt.figure()
    x = np.arange(24)
    y = json_load['hourly']['temperature_2m']
    plt.bar(x, y,  label="test")
    io = BytesIO()
    fig.savefig(io, format="png")
    io.seek(0)
    base64_img = base64.b64encode(io.read()).decode()

    return render_template('index.html', img=base64_img)