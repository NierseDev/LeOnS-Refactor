from flask import Flask, render_template, request, url_for
import requests

app = Flask(__name__)

"""
URL Routes:
    Primary:
    Home (Logged Out) / Dashboard (Logged In)

    Secondary:
    Courses (Logged In) / Forum (Logged Out / Logged In) / ARReS
"""
@app.route('/')
def home():
    return render_template("home.html")