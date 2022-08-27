from flask import redirect, jsonify
from backend import app

@app.route('/')
def a():
    return 'hello'

@app.route('/getprediction', methods=['POST'])
def getprediction():
    pass

@app.route('/handwritten',methods=['GET'])
def landing():
    pass


# external APIs