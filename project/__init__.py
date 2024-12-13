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

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/courses')
def courses():
    return render_template("courses.html")

@app.route('/')
def course_post():
    return render_template("course_post.html")

@app.route('/forum')
def forum():
    return render_template("forum.html")

@app.route('/')
def forum_post():
    return render_template("forum_post.html")