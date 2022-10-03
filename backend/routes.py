import json
from flask import render_template, redirect, jsonify, request
from backend import app
from backend.behind import inference

@app.route('/predictimage',methods=['GET','POST'])
def predictimage():
    if request.method == 'POST':
        print(request.form)
        
        image = request.files['img']
        print(image)
        print('hey there2')
        value = inference(image)
        print(value)
        return render_template('je.html')
    return render_template('index.html')
