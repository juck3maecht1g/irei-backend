import os
import webbrowser
from flask import Flask, render_template
from flask_cors import CORS




app = Flask(__name__, static_folder="../../build", static_url_path="/")
CORS(app)

@app.route("/")
def index():
    return app.send_static_file("index.html")
import ControlPageController

