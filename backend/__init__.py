from flask import Flask
from flask_cors import CORS

app = Flask(__name__, template_folder='../content/template', static_folder='../content/static')
CORS(app)

from backend import routes
