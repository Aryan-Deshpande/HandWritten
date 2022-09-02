from flask import Flask
from flask_cors import CORS

app = Flask(__name__, template_folder='../src')
CORS(app)

from backend import routes
