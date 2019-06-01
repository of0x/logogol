from todo import app

from flask import jsonify, request, url_for
from flask import json


@app.route("/", methods=["GET", "POST", "DELETE"])
def index():

@app.route("/<int:entry_id>", methods=["GET", "PATCH", "DELETE"])
def entry(entry_id):
