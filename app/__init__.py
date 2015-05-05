from flask import Flask
from flaskext.markdown import Markdown

app = Flask(__name__)
Markdown(app)
from app import routes