import os
import webbrowser
from flask import Flask, render_template
from flask_cors import CORS


app = Flask(__name__, static_folder="../../build", static_url_path="/")
CORS(app)


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/test")
def test():
    testdik = [
        {
            "name": "bernt",
            "robots": [{
                "name": "1",
                "ip": "4"
            }, {
                "name": "2",
                "ip": "42"
            }, {
                "name": "3",
                "ip": "42"
            }, {
                "name": "4",
                "ip": "42"
            }],
        },

        {
            "name": "hans",
            "robots": [{
                "name": "ahhhhh",
                "ip": "42"
            }, {
                "name": "ahhhhh",
                "ip": "42"
            }, {
                "name": "ahhhhh",
                "ip": "42"
            }, {
                "name": "ahhhhh",
                "ip": "42"
            }],
        }

    ]
    return testdik


@app.route("/test_robots_gripper")
def test_robots_gripper():
    robots = [{
        "name": "1",
        "ip": "4"
    }, {
        "name": "2",
        "ip": "42"
    }, {
        "name": "3",
        "ip": "42"
    }, {
        "name": "4",
        "ip": "42"
    }]

    return robots


@app.route("/test_robots_experiment")
def test_robots_exp():
    robots = [{
        "name": "1",
        "ip": "4"
    }, {
        "name": "2",
        "ip": "424"
    }, {
        "name": "3",
        "ip": "423"
    }, {
        "name": "4",
        "ip": "42"
    }]

    return robots
