from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Home"

@app.route("/clinics")
def clinics():
    return render_template("clinics.html")