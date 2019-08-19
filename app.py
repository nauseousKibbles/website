# By Greyson B
# Started July 24, 2019.
# During summer school.

import json
import csv
from flask import Flask, render_template, url_for, request
version = "2019.8.19"


app = Flask(__name__)

fieldnames = ["title", "content"]


def jsonPosts():
    with open("jsons/posts.json", "r") as file:
        return file.read()


def jsonDownloads():
    with open("jsons/downloads.json", "r") as dfile:
        return dfile.read()


posts = json.loads(jsonPosts())["posts"]


@app.route("/")
@app.route("/home")
def home():
    # print(homeContent())
    return render_template("home.html", posts=posts, titletag="Home")


@app.route("/downloads")
def downloads():
    return render_template(
        "downloads.html",
        titletag="Download",
        downloads=json.loads(jsonDownloads())["downloads"],
    )


@app.route("/about")
def about():
    return render_template(
        "about.html",
        titletag="About",
        version=version
    )
