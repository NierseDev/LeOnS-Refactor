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
@app.route('/home')
def home():
    show_navbar = True
    return render_template("home.html", show_navbar=show_navbar)

@app.route('/dashboard')
def dashboard():
    show_navbar = True
    return render_template("dashboard.html", show_navbar=show_navbar)

@app.route('/login')
def login():
    show_navbar = False
    return render_template("login.html", show_navbar=show_navbar)

@app.route('/courses')
def courses():
    show_navbar = True
    return render_template("courses.html", show_navbar=show_navbar)

@app.route('/')
def course_post():
    show_navbar = True
    return render_template("course_post.html", show_navbar=show_navbar)

@app.route('/forum')
def forum():
    show_navbar = True
    return render_template("forum.html", show_navbar=show_navbar)

@app.route('/')
def forum_post():
    show_navbar = True
    return render_template("forum_post.html", show_navbar=show_navbar)