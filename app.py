# By Greyson B
# Started July 24, 2019.
# During summer school.

from flask import Flask, render_template, url_for, request
import csv, json

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
    return render_template("home.html", posts=posts)


@app.route("/downloads")
def downloads():
    return render_template(
        "downloads.html", downloads=json.loads(jsonDownloads())["downloads"]
    )
