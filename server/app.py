import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import db_uri
from actions import (
    GetParts,
    CheckPartCompatability,
    CalculateRequiredPower,
)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
CORS(app)


@app.route("/ping", methods=["GET"])
def ping():
    method = request.method
    if method == "GET":
        return str("pong"), 200
    return 405


@app.route("/parts/<part_name>", methods=["GET"])
def parts(part_name):
    method = request.method
    if method == "GET":
        args = dict(request.args)
        page = args.pop("page") if "page" in args else 1
        filters = args
        action = GetParts()
        return jsonify(action.perform(db, page, filters, part_name)), 200
    return 405


@app.route("/compatability", methods=["GET"])
def compatability():
    method = request.method
    if method == "GET":
        args = dict(request.args)
        part_ids = args
        action = CheckPartCompatability()
        return jsonify(action.perform(db, part_ids)), 200
    return 405


@app.route("/calculate_required_power", methods=["GET"])
def required_power():
    method = request.method
    if method == "GET":
        args = dict(request.args)
        part_ids = args
        action = CalculateRequiredPower()
        return jsonify(action.perform(db, part_ids)), 200
    return 405
