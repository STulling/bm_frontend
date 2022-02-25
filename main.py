from flask import Flask, redirect, url_for, render_template, request, flash
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

url = 'http://192.168.1.7:5000/api/DJ/'
data = [
    "wave",
    "sparkle",
    "mond",
    "fill",
    "diamond",
    "circle",
    "bars",
    "clear",
    "snake"
]

@app.route("/")
def hello_world():
    return render_template("index.html", url=url, data=data)

app.run(host='0.0.0.0', port=80)