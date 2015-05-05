from app import app
from app.controllers import *
from flask import redirect
from flask import jsonify

@app.route('/')
def index():
    return redirect('/recipe/list')

@app.route('/recipe/list')
def list_recipes():
    return jsonify(**{"message": "Hello, World!"})