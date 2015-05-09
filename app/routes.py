from app import app
from flask import redirect
from flask import jsonify
from flask import render_template
from app.controllers import *
from app.models.BasicError import BasicError

recipe_controller = RecipeController.RecipeController()

@app.route('/')
def index():
    return redirect('/recipe/list')

@app.route('/recipe/list')
def list_recipes():
    return jsonify(**{"recipes": recipe_controller.list_all()})

@app.route('/recipe/new')
def load_create_recipe_page():
    return render_template('create_recipe.html')

@app.route('/recipe/<recipe_id>')
def display_recipe(recipe_id):
    recipe = recipe_controller.by_id(recipe_id)
    return render_template('display_recipe.html', recipe=recipe) if recipe else jsonify(**BasicError("error", "Recipe Not Found").__dict__)