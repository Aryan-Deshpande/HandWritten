import json
from flask import render_template, redirect, jsonify, request
from backend import app
from backend.behind import inference

@app.route('/predictimage',methods=['GET','POST'])
def predictimage():
    if request.method == 'POST':
        image = request.data
        value, Success = inference(image)
        if value == -1 and Success == False:
            return 'err' 
        return value
    return render_template('index.html')
