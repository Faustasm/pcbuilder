import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import db_uri
from actions import GetParts, GetBuilds, \
    GetVendors, GetProducts, CreateNewBuild

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)


@app.route('/ping', methods = ['GET'])
def ping():
    method = request.method
    if method == 'GET':
        return str('pong'), 200
    return 405

@app.route('/parts/<part_name>', methods = ['GET'])
def parts(part_name):
    method = request.method
    if method == 'GET':
        args = dict(request.args)
        page = args.pop('page') if 'page' in args else 1
        filters = args
        action = GetParts()
        return jsonify(
            action.perform(
                db,
                page,
                filters,
                part_name
            )
        ), 200
    return 405

@app.route('/builds', methods = ['GET', 'POST'])
def builds():
    method = request.method
    if method == 'GET':
        args = dict(request.args)
        page = args.pop('page') if 'page' in args else 1
        by_popularity = args.pop('by_popularity') if 'by_popularity' in args else False
        action = GetBuilds()
        filters = args
        return jsonify(
            action.perform(
                db,
                page,
                filters,
                by_popularity
            )
        ), 200
    if method == 'POST':
        data = request.json.get('payload')
        action = CreateNewBuild()
        action.perform(db, data)
        return 201
    return 405

@app.route('/vendors', methods = ['GET'])
def vendors():
    method = request.method
    if method == 'GET':
        args = dict(request.args)
        page = args.pop('page') if 'page' in args else 1
        filters = args
        action = GetVendors()
        return jsonify(
            action.perform(
                db,
                page,
                filters
            )
        ), 200

@app.route('/products', methods = ['GET'])
def products():
    method = request.method
    if method == 'GET':
        args = dict(request.args)
        page = args.pop('page') if 'page' in args else 1
        filters = args
        action = GetProducts()
        return jsonify(
            action.perform(
                db,
                page,
                filters
            )
        ), 200
    return 405
